"""Build the Wave 5.2A paired dataset diagnostic report."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import csv
import json
import math
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))


SIMPLIFIED_DATASET_ROOT = PROJECT_PATH / "data" / "simplified_dataset"
POLISHED_DATASET_ROOT = PROJECT_PATH / "data" / "polished_dataset"
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave52a_paired_dataset_diagnostics"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "wave5_2" / "paired_dataset_diagnostics"
REPORT_FILENAME = "wave52a_paired_dataset_diagnostics.md"
SUMMARY_FILENAME = "summary.json"
PAIR_METRICS_FILENAME = "pair_metrics.csv"
HARMONIC_METRICS_FILENAME = "harmonic_metrics.csv"
AGGREGATE_SUMMARY_FILENAME = "aggregate_summary.csv"
FILENAME_PATTERN = re.compile(
    r"(?P<speed_rpm>[-+]?\d+(?:\.\d+)?)"
    r"rpm(?P<torque_nm>[-+]?\d+(?:\.\d+)?)"
    r"Nm(?P<temperature_deg>[-+]?\d+(?:\.\d+)?)"
    r"deg\.csv$"
)
DIAGNOSTIC_HARMONIC_INDEX_LIST = [0, 1, 2, 3, 6, 12, 24, 48, 96, 156, 162, 240]
FORWARD_DIRECTION = "forward"
BACKWARD_DIRECTION = "backward"
ROW_COUNT_DIFFERENCE_THRESHOLD = 10
THETA_RANGE_DIFFERENCE_THRESHOLD_DEG = 1.000000
OFFSET_SHIFT_THRESHOLD_DEG = 0.000500
SHAPE_DIFFERENCE_THRESHOLD_DEG = 0.000250
SMOOTHNESS_DIFFERENCE_THRESHOLD_DEG = 0.000001
MAXIMUM_DELTA_DIFFERENCE_THRESHOLD_DEG = 0.000500
HARMONIC_DIFFERENCE_THRESHOLD_DEG = 0.000250


@dataclass(frozen=True)
class DatasetRecord:

    """Describe one directional dataset file.

    Attributes:
        dataset_name: Dataset selector.
        direction_label: Direction label.
        speed_rpm: Nominal speed parsed from the file name.
        torque_nm: Nominal torque parsed from the file name.
        temperature_deg: Nominal temperature parsed from the file name.
        csv_file_path: Absolute CSV path.
    """

    dataset_name: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    temperature_deg: float
    csv_file_path: Path

    @property
    def pair_key(self) -> tuple[float, float, float, str]:

        """Return the operating-condition and direction pairing key."""

        return (self.speed_rpm, self.torque_nm, self.temperature_deg, self.direction_label)


@dataclass
class CurveMetricAccumulator:

    """Accumulate streaming curve metrics."""

    row_count: int = 0
    theta_minimum: float = math.inf
    theta_maximum: float = -math.inf
    te_minimum: float = math.inf
    te_maximum: float = -math.inf
    te_sum: float = 0.0
    te_square_sum: float = 0.0
    previous_te: float | None = None
    absolute_delta_sum: float = 0.0
    maximum_absolute_delta: float = 0.0
    theta_dot_minimum: float | None = None
    theta_dot_maximum: float | None = None
    theta_dot_sum: float = 0.0
    tau_load_minimum: float | None = None
    tau_load_maximum: float | None = None
    tau_load_sum: float = 0.0
    temperature_minimum: float | None = None
    temperature_maximum: float | None = None
    temperature_sum: float = 0.0
    harmonic_sine_sum_by_index: dict[int, float] = field(default_factory=dict)
    harmonic_cosine_sum_by_index: dict[int, float] = field(default_factory=dict)

    def update(
        self,
        theta_deg: float,
        transmission_error_deg: float,
        theta_dot_rpm: float | None = None,
        tau_load_nm: float | None = None,
        temperature_deg: float | None = None,
    ) -> None:

        """Update metric accumulators from one curve row.

        Args:
            theta_deg: Angular position in degrees.
            transmission_error_deg: Transmission error in degrees.
            theta_dot_rpm: Optional measured or derived speed.
            tau_load_nm: Optional measured load torque.
            temperature_deg: Optional measured oil temperature.
        """

        # Update Scalar Statistics
        self.row_count += 1
        self.theta_minimum = min(self.theta_minimum, theta_deg)
        self.theta_maximum = max(self.theta_maximum, theta_deg)
        self.te_minimum = min(self.te_minimum, transmission_error_deg)
        self.te_maximum = max(self.te_maximum, transmission_error_deg)
        self.te_sum += transmission_error_deg
        self.te_square_sum += transmission_error_deg * transmission_error_deg

        # Update Smoothness Surrogate
        if self.previous_te is not None:
            absolute_delta = abs(transmission_error_deg - self.previous_te)
            self.absolute_delta_sum += absolute_delta
            self.maximum_absolute_delta = max(self.maximum_absolute_delta, absolute_delta)
        self.previous_te = transmission_error_deg

        # Update Optional Polished State Statistics
        self._update_optional_value("theta_dot", theta_dot_rpm)
        self._update_optional_value("tau_load", tau_load_nm)
        self._update_optional_value("temperature", temperature_deg)

        # Update Harmonic Projection
        theta_rad = math.radians(theta_deg)
        for harmonic_index in DIAGNOSTIC_HARMONIC_INDEX_LIST:
            self.harmonic_sine_sum_by_index[harmonic_index] = (
                self.harmonic_sine_sum_by_index.get(harmonic_index, 0.0)
                + transmission_error_deg * math.sin(harmonic_index * theta_rad)
            )
            self.harmonic_cosine_sum_by_index[harmonic_index] = (
                self.harmonic_cosine_sum_by_index.get(harmonic_index, 0.0)
                + transmission_error_deg * math.cos(harmonic_index * theta_rad)
            )

    def _update_optional_value(self, value_name: str, value: float | None) -> None:

        """Update one optional measured polished-state statistic."""

        if value is None:
            return

        minimum_name = f"{value_name}_minimum"
        maximum_name = f"{value_name}_maximum"
        sum_name = f"{value_name}_sum"
        current_minimum = getattr(self, minimum_name)
        current_maximum = getattr(self, maximum_name)
        setattr(self, minimum_name, value if current_minimum is None else min(current_minimum, value))
        setattr(self, maximum_name, value if current_maximum is None else max(current_maximum, value))
        setattr(self, sum_name, getattr(self, sum_name) + value)

    def to_metric_dictionary(self) -> dict[str, float | int | None]:

        """Convert accumulated metrics to a serializable dictionary."""

        assert self.row_count > 0, "Cannot summarize an empty curve accumulator"
        delta_count = max(1, self.row_count - 1)
        te_mean = self.te_sum / self.row_count
        te_variance = max(0.0, self.te_square_sum / self.row_count - te_mean * te_mean)
        return {
            "row_count": self.row_count,
            "theta_minimum_deg": self.theta_minimum,
            "theta_maximum_deg": self.theta_maximum,
            "theta_range_deg": self.theta_maximum - self.theta_minimum,
            "te_mean_deg": te_mean,
            "te_rmse_about_zero_deg": math.sqrt(self.te_square_sum / self.row_count),
            "te_standard_deviation_deg": math.sqrt(te_variance),
            "te_minimum_deg": self.te_minimum,
            "te_maximum_deg": self.te_maximum,
            "te_peak_to_peak_deg": self.te_maximum - self.te_minimum,
            "mean_absolute_delta_deg": self.absolute_delta_sum / delta_count,
            "maximum_absolute_delta_deg": self.maximum_absolute_delta,
            "theta_dot_mean_rpm": self._optional_mean("theta_dot"),
            "theta_dot_minimum_rpm": self.theta_dot_minimum,
            "theta_dot_maximum_rpm": self.theta_dot_maximum,
            "tau_load_mean_nm": self._optional_mean("tau_load"),
            "tau_load_minimum_nm": self.tau_load_minimum,
            "tau_load_maximum_nm": self.tau_load_maximum,
            "temperature_mean_deg_c": self._optional_mean("temperature"),
            "temperature_minimum_deg_c": self.temperature_minimum,
            "temperature_maximum_deg_c": self.temperature_maximum,
        }

    def _optional_mean(self, value_name: str) -> float | None:

        """Return an optional measured-state mean."""

        minimum_value = getattr(self, f"{value_name}_minimum")
        if minimum_value is None:
            return None
        return getattr(self, f"{value_name}_sum") / self.row_count

    def build_harmonic_rows(self) -> list[dict[str, float | int]]:

        """Build diagnostic harmonic projection rows."""

        assert self.row_count > 0, "Cannot build harmonic rows from an empty curve accumulator"
        row_list: list[dict[str, float | int]] = []
        for harmonic_index in DIAGNOSTIC_HARMONIC_INDEX_LIST:
            sine_sum = self.harmonic_sine_sum_by_index.get(harmonic_index, 0.0)
            cosine_sum = self.harmonic_cosine_sum_by_index.get(harmonic_index, 0.0)
            if harmonic_index == 0:
                amplitude = abs(cosine_sum / self.row_count)
            else:
                amplitude = 2.0 * math.sqrt(sine_sum * sine_sum + cosine_sum * cosine_sum) / self.row_count
            row_list.append(
                {
                    "harmonic_index": harmonic_index,
                    "amplitude_deg": amplitude,
                }
            )
        return row_list


def format_float(value: float | int | None, digits: int = 9) -> str:

    """Format a scalar for CSV or Markdown output."""

    if value is None:
        return ""
    return f"{float(value):.{digits}f}"


def format_count(value: float | int | None) -> str:

    """Format a row-count metric for CSV output."""

    if value is None:
        return ""
    return str(int(value))


def parse_operating_conditions(csv_file_path: Path) -> tuple[float, float, float]:

    """Parse nominal operating conditions from one CSV filename."""

    filename_match = FILENAME_PATTERN.search(csv_file_path.name)
    assert filename_match is not None, f"Unable to parse operating conditions | {csv_file_path}"
    return (
        float(filename_match.group("speed_rpm")),
        float(filename_match.group("torque_nm")),
        float(filename_match.group("temperature_deg")),
    )


def collect_simplified_records(dataset_root: Path) -> dict[tuple[float, float, float, str], DatasetRecord]:

    """Collect directional simplified dataset records."""

    record_dictionary: dict[tuple[float, float, float, str], DatasetRecord] = {}
    for csv_file_path in sorted(dataset_root.rglob("*.csv")):
        speed_rpm, torque_nm, temperature_deg = parse_operating_conditions(csv_file_path)
        for direction_label in [FORWARD_DIRECTION, BACKWARD_DIRECTION]:
            record = DatasetRecord("simplified_dataset", direction_label, speed_rpm, torque_nm, temperature_deg, csv_file_path.resolve())
            record_dictionary[record.pair_key] = record
    return record_dictionary


def collect_polished_records(dataset_root: Path) -> dict[tuple[float, float, float, str], DatasetRecord]:

    """Collect directional polished dataset records."""

    record_dictionary: dict[tuple[float, float, float, str], DatasetRecord] = {}
    for csv_file_path in sorted(dataset_root.rglob("*.csv")):
        relative_parts = csv_file_path.resolve().relative_to(dataset_root.resolve()).parts
        direction_label = relative_parts[0].lower()
        if direction_label not in [FORWARD_DIRECTION, BACKWARD_DIRECTION]:
            continue
        speed_rpm, torque_nm, temperature_deg = parse_operating_conditions(csv_file_path)
        record = DatasetRecord("polished_dataset", direction_label, speed_rpm, torque_nm, temperature_deg, csv_file_path.resolve())
        record_dictionary[record.pair_key] = record
    return record_dictionary


def select_evenly_spaced_keys(key_list: list[tuple[float, float, float, str]], maximum_count: int) -> list[tuple[float, float, float, str]]:

    """Select a deterministic spread of paired keys."""

    if maximum_count <= 0 or maximum_count >= len(key_list):
        return list(key_list)
    if maximum_count == 1:
        return [key_list[0]]

    selected_key_list = []
    for selected_index in range(maximum_count):
        source_index = round(selected_index * (len(key_list) - 1) / (maximum_count - 1))
        selected_key_list.append(key_list[source_index])
    return list(dict.fromkeys(selected_key_list))


def number_from_text(text: str) -> float:

    """Parse a numeric CSV value."""

    normalized_text = text.strip()
    if "," in normalized_text and "." not in normalized_text:
        normalized_text = normalized_text.replace(",", ".")
    return float(normalized_text)


def should_keep_row(row_index: int, row_stride: int, maximum_rows: int, kept_rows: int) -> bool:

    """Return whether a streamed row should contribute to bounded diagnostics."""

    if maximum_rows > 0 and kept_rows >= maximum_rows:
        return False
    return row_index % max(1, row_stride) == 0


def is_finite_curve_sample(theta_deg: float, transmission_error_deg: float) -> bool:

    """Return whether a parsed curve sample can contribute to diagnostics."""

    return math.isfinite(theta_deg) and math.isfinite(transmission_error_deg)


def summarize_simplified_record(record: DatasetRecord, row_stride: int, maximum_rows: int) -> tuple[dict[str, float | int | None], list[dict[str, float | int]]]:

    """Summarize one simplified directional curve."""

    accumulator = CurveMetricAccumulator()
    position_column = "Poisition_Output_Reducer_Fw" if record.direction_label == FORWARD_DIRECTION else "Position_Output_Reducer_Bw"
    te_column = "Transmission_Error_Fw" if record.direction_label == FORWARD_DIRECTION else "Transmission_Error_Bw"

    with record.csv_file_path.open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        kept_rows = 0
        for row_index, row in enumerate(reader):
            if not should_keep_row(row_index, row_stride, maximum_rows, kept_rows):
                continue
            theta_deg = number_from_text(row[position_column])
            transmission_error_deg = number_from_text(row[te_column])
            if not is_finite_curve_sample(theta_deg, transmission_error_deg):
                continue
            accumulator.update(theta_deg, transmission_error_deg)
            kept_rows += 1

    return accumulator.to_metric_dictionary(), accumulator.build_harmonic_rows()


def summarize_polished_record(record: DatasetRecord, row_stride: int, maximum_rows: int) -> tuple[dict[str, float | int | None], list[dict[str, float | int]]]:

    """Summarize one polished directional point cloud."""

    accumulator = CurveMetricAccumulator()
    with record.csv_file_path.open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        kept_rows = 0
        for row_index, row in enumerate(reader):
            if not should_keep_row(row_index, row_stride, maximum_rows, kept_rows):
                continue
            theta_deg = number_from_text(row["theta"])
            transmission_error_deg = number_from_text(row["theta_TE"])
            if not is_finite_curve_sample(theta_deg, transmission_error_deg):
                continue
            accumulator.update(
                theta_deg=theta_deg,
                transmission_error_deg=transmission_error_deg,
                theta_dot_rpm=number_from_text(row["theta_dot"]),
                tau_load_nm=number_from_text(row["tau_load"]),
                temperature_deg=number_from_text(row["T"]),
            )
            kept_rows += 1

    return accumulator.to_metric_dictionary(), accumulator.build_harmonic_rows()


def build_pair_metric_row(
    pair_key: tuple[float, float, float, str],
    simplified_record: DatasetRecord,
    polished_record: DatasetRecord,
    simplified_metrics: dict[str, float | int | None],
    polished_metrics: dict[str, float | int | None],
    maximum_harmonic_amplitude_difference_deg: float,
) -> dict[str, str]:

    """Build one paired metric CSV row."""

    speed_rpm, torque_nm, temperature_deg, direction_label = pair_key
    row_dictionary = {
        "speed_rpm": format_float(speed_rpm, 1),
        "torque_nm": format_float(torque_nm, 1),
        "temperature_deg": format_float(temperature_deg, 1),
        "direction_label": direction_label,
        "simplified_path": simplified_record.csv_file_path.relative_to(PROJECT_PATH).as_posix(),
        "polished_path": polished_record.csv_file_path.relative_to(PROJECT_PATH).as_posix(),
    }

    metric_name_list = [
        "row_count",
        "theta_range_deg",
        "te_mean_deg",
        "te_standard_deviation_deg",
        "te_peak_to_peak_deg",
        "mean_absolute_delta_deg",
        "maximum_absolute_delta_deg",
        "theta_dot_mean_rpm",
        "tau_load_mean_nm",
        "temperature_mean_deg_c",
    ]
    for metric_name in metric_name_list:
        if metric_name == "row_count":
            row_dictionary[f"simplified_{metric_name}"] = format_count(simplified_metrics.get(metric_name))
            row_dictionary[f"polished_{metric_name}"] = format_count(polished_metrics.get(metric_name))
        else:
            row_dictionary[f"simplified_{metric_name}"] = format_float(simplified_metrics.get(metric_name))
            row_dictionary[f"polished_{metric_name}"] = format_float(polished_metrics.get(metric_name))

    row_dictionary["mean_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["te_mean_deg"]) - float(simplified_metrics["te_mean_deg"])
    )
    row_dictionary["peak_to_peak_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["te_peak_to_peak_deg"]) - float(simplified_metrics["te_peak_to_peak_deg"])
    )
    row_dictionary["smoothness_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["mean_absolute_delta_deg"]) - float(simplified_metrics["mean_absolute_delta_deg"])
    )
    row_dictionary["row_count_difference_polished_minus_simplified"] = format_count(
        int(polished_metrics["row_count"]) - int(simplified_metrics["row_count"])
    )
    row_dictionary["theta_range_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["theta_range_deg"]) - float(simplified_metrics["theta_range_deg"])
    )
    row_dictionary["standard_deviation_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["te_standard_deviation_deg"]) - float(simplified_metrics["te_standard_deviation_deg"])
    )
    row_dictionary["maximum_delta_difference_polished_minus_simplified_deg"] = format_float(
        float(polished_metrics["maximum_absolute_delta_deg"]) - float(simplified_metrics["maximum_absolute_delta_deg"])
    )
    row_dictionary["maximum_harmonic_amplitude_difference_deg"] = format_float(maximum_harmonic_amplitude_difference_deg)
    row_dictionary["classification"] = classify_pair_metric_row(row_dictionary)
    return row_dictionary


def build_harmonic_metric_rows(
    pair_key: tuple[float, float, float, str],
    simplified_harmonic_rows: list[dict[str, float | int]],
    polished_harmonic_rows: list[dict[str, float | int]],
) -> list[dict[str, str]]:

    """Build paired harmonic diagnostic rows."""

    speed_rpm, torque_nm, temperature_deg, direction_label = pair_key
    polished_by_index = {int(row["harmonic_index"]): row for row in polished_harmonic_rows}
    output_rows: list[dict[str, str]] = []
    for simplified_row in simplified_harmonic_rows:
        harmonic_index = int(simplified_row["harmonic_index"])
        polished_row = polished_by_index[harmonic_index]
        simplified_amplitude = float(simplified_row["amplitude_deg"])
        polished_amplitude = float(polished_row["amplitude_deg"])
        output_rows.append(
            {
                "speed_rpm": format_float(speed_rpm, 1),
                "torque_nm": format_float(torque_nm, 1),
                "temperature_deg": format_float(temperature_deg, 1),
                "direction_label": direction_label,
                "harmonic_index": str(harmonic_index),
                "simplified_amplitude_deg": format_float(simplified_amplitude),
                "polished_amplitude_deg": format_float(polished_amplitude),
                "amplitude_difference_polished_minus_simplified_deg": format_float(polished_amplitude - simplified_amplitude),
            }
        )
    return output_rows


def calculate_maximum_harmonic_amplitude_difference(
    simplified_harmonic_rows: list[dict[str, float | int]],
    polished_harmonic_rows: list[dict[str, float | int]],
) -> float:

    """Calculate the maximum absolute paired harmonic-amplitude difference."""

    polished_by_index = {int(row["harmonic_index"]): row for row in polished_harmonic_rows}
    maximum_difference = 0.0
    for simplified_row in simplified_harmonic_rows:
        harmonic_index = int(simplified_row["harmonic_index"])
        if harmonic_index == 0:
            continue
        polished_row = polished_by_index[harmonic_index]
        simplified_amplitude = float(simplified_row["amplitude_deg"])
        polished_amplitude = float(polished_row["amplitude_deg"])
        maximum_difference = max(maximum_difference, abs(polished_amplitude - simplified_amplitude))
    return maximum_difference


def parse_metric(row_dictionary: dict[str, str], column_name: str) -> float:

    """Parse one numeric metric from a CSV-ready row dictionary."""

    value_text = row_dictionary[column_name]
    if value_text == "":
        return 0.0
    return float(value_text)


def classify_pair_metric_row(row_dictionary: dict[str, str]) -> str:

    """Classify one paired dataset comparison row."""

    row_count_difference = abs(int(row_dictionary["row_count_difference_polished_minus_simplified"]))
    theta_range_difference = abs(parse_metric(row_dictionary, "theta_range_difference_polished_minus_simplified_deg"))
    offset_difference = abs(parse_metric(row_dictionary, "mean_difference_polished_minus_simplified_deg"))
    peak_to_peak_difference = abs(parse_metric(row_dictionary, "peak_to_peak_difference_polished_minus_simplified_deg"))
    standard_deviation_difference = abs(parse_metric(row_dictionary, "standard_deviation_difference_polished_minus_simplified_deg"))
    smoothness_difference = abs(parse_metric(row_dictionary, "smoothness_difference_polished_minus_simplified_deg"))
    maximum_delta_difference = abs(parse_metric(row_dictionary, "maximum_delta_difference_polished_minus_simplified_deg"))
    harmonic_difference = abs(parse_metric(row_dictionary, "maximum_harmonic_amplitude_difference_deg"))

    sampling_changed = (
        row_count_difference > ROW_COUNT_DIFFERENCE_THRESHOLD
        or theta_range_difference > THETA_RANGE_DIFFERENCE_THRESHOLD_DEG
    )
    shape_changed = (
        peak_to_peak_difference > SHAPE_DIFFERENCE_THRESHOLD_DEG
        or standard_deviation_difference > SHAPE_DIFFERENCE_THRESHOLD_DEG
    )
    smoothness_changed = (
        smoothness_difference > SMOOTHNESS_DIFFERENCE_THRESHOLD_DEG
        or maximum_delta_difference > MAXIMUM_DELTA_DIFFERENCE_THRESHOLD_DEG
    )
    harmonic_changed = harmonic_difference > HARMONIC_DIFFERENCE_THRESHOLD_DEG
    offset_shifted = offset_difference > OFFSET_SHIFT_THRESHOLD_DEG

    if sampling_changed:
        return "sampling_anomaly"
    if shape_changed:
        return "shape_changed"
    if smoothness_changed:
        return "smoothness_changed"
    if harmonic_changed:
        return "harmonic_changed"
    if offset_shifted:
        return "offset_shifted"
    return "nearly_identical"


def count_by_column(row_list: Iterable[dict[str, str]], column_name: str) -> dict[str, int]:

    """Count rows by one string column."""

    count_dictionary: dict[str, int] = {}
    for row in row_list:
        key = row[column_name]
        count_dictionary[key] = count_dictionary.get(key, 0) + 1
    return dict(sorted(count_dictionary.items()))


def build_aggregate_rows(pair_metric_rows: list[dict[str, str]]) -> list[dict[str, str]]:

    """Build aggregate rows for global and operating-condition groupings."""

    grouping_specification_list = [
        ("global", lambda row: "all"),
        ("direction", lambda row: row["direction_label"]),
        ("speed_rpm", lambda row: row["speed_rpm"]),
        ("torque_nm", lambda row: row["torque_nm"]),
        ("temperature_deg", lambda row: row["temperature_deg"]),
    ]
    output_rows: list[dict[str, str]] = []
    for group_name, key_function in grouping_specification_list:
        grouped_rows: dict[str, list[dict[str, str]]] = {}
        for row in pair_metric_rows:
            group_value = key_function(row)
            grouped_rows.setdefault(group_value, []).append(row)

        for group_value in sorted(grouped_rows):
            row_list = grouped_rows[group_value]
            class_counts = count_by_column(row_list, "classification")
            output_rows.append(
                {
                    "group_name": group_name,
                    "group_value": group_value,
                    "pair_count": str(len(row_list)),
                    "mean_offset_delta_deg": format_float(mean_of_column(row_list, "mean_difference_polished_minus_simplified_deg")),
                    "mean_abs_offset_delta_deg": format_float(mean_absolute_of_column(row_list, "mean_difference_polished_minus_simplified_deg")),
                    "mean_peak_to_peak_delta_deg": format_float(mean_of_column(row_list, "peak_to_peak_difference_polished_minus_simplified_deg")),
                    "mean_abs_peak_to_peak_delta_deg": format_float(mean_absolute_of_column(row_list, "peak_to_peak_difference_polished_minus_simplified_deg")),
                    "mean_smoothness_delta_deg": format_float(mean_of_column(row_list, "smoothness_difference_polished_minus_simplified_deg")),
                    "mean_abs_smoothness_delta_deg": format_float(mean_absolute_of_column(row_list, "smoothness_difference_polished_minus_simplified_deg")),
                    "mean_max_harmonic_delta_deg": format_float(mean_of_column(row_list, "maximum_harmonic_amplitude_difference_deg")),
                    "mean_abs_max_harmonic_delta_deg": format_float(mean_absolute_of_column(row_list, "maximum_harmonic_amplitude_difference_deg")),
                    "nearly_identical_count": str(class_counts.get("nearly_identical", 0)),
                    "offset_shifted_count": str(class_counts.get("offset_shifted", 0)),
                    "shape_changed_count": str(class_counts.get("shape_changed", 0)),
                    "smoothness_changed_count": str(class_counts.get("smoothness_changed", 0)),
                    "harmonic_changed_count": str(class_counts.get("harmonic_changed", 0)),
                    "sampling_anomaly_count": str(class_counts.get("sampling_anomaly", 0)),
                }
            )
    return output_rows


def write_csv(output_path: Path, row_list: list[dict[str, str]]) -> None:

    """Write a list of dictionaries to CSV."""

    assert row_list, f"No rows available for CSV output | {output_path}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def mean_of_column(row_list: Iterable[dict[str, str]], column_name: str) -> float:

    """Return a mean value from a numeric string column."""

    value_list = [float(row[column_name]) for row in row_list if row[column_name] not in ["", "nan"]]
    assert value_list, f"No numeric values found for column | {column_name}"
    return sum(value_list) / len(value_list)


def mean_absolute_of_column(row_list: Iterable[dict[str, str]], column_name: str) -> float:

    """Return a mean absolute value from a numeric string column."""

    value_list = [abs(float(row[column_name])) for row in row_list if row[column_name] not in ["", "nan"]]
    assert value_list, f"No numeric values found for column | {column_name}"
    return sum(value_list) / len(value_list)


def build_report_lines(
    run_id: str,
    selected_pair_count: int,
    paired_key_count: int,
    row_stride: int,
    maximum_rows_per_file: int,
    pair_metric_rows: list[dict[str, str]],
    aggregate_summary_rows: list[dict[str, str]],
    output_directory: Path,
) -> list[str]:

    """Build the paired dataset diagnostic Markdown report."""

    mean_offset_delta = mean_of_column(pair_metric_rows, "mean_difference_polished_minus_simplified_deg")
    mean_absolute_offset_delta = mean_absolute_of_column(pair_metric_rows, "mean_difference_polished_minus_simplified_deg")
    mean_peak_to_peak_delta = mean_of_column(pair_metric_rows, "peak_to_peak_difference_polished_minus_simplified_deg")
    mean_absolute_peak_to_peak_delta = mean_absolute_of_column(pair_metric_rows, "peak_to_peak_difference_polished_minus_simplified_deg")
    mean_smoothness_delta = mean_of_column(pair_metric_rows, "smoothness_difference_polished_minus_simplified_deg")
    mean_absolute_smoothness_delta = mean_absolute_of_column(pair_metric_rows, "smoothness_difference_polished_minus_simplified_deg")
    mean_maximum_harmonic_delta = mean_of_column(pair_metric_rows, "maximum_harmonic_amplitude_difference_deg")
    classification_count_dictionary = count_by_column(pair_metric_rows, "classification")
    global_aggregate_row = next(row for row in aggregate_summary_rows if row["group_name"] == "global")
    direction_aggregate_rows = [row for row in aggregate_summary_rows if row["group_name"] == "direction"]
    preview_rows = pair_metric_rows[:12]
    matrix_scope = "full paired matrix" if selected_pair_count == paired_key_count else "bounded paired sample"

    report_lines = [
        "# Wave 5.2A Paired Dataset Diagnostics",
        "",
        "## Overview",
        "",
        "This diagnostic compares matched `simplified_dataset` and `polished_dataset`",
        "directional curves. It is a dataset-alignment and noise-awareness report,",
        "not a training result and not a `TE Curve Verification Pipeline` promotion.",
        "",
        f"This run covers the {matrix_scope}.",
        "",
        "The externally running full-wave `polished_dataset` retraining campaign",
        "remains out of scope for this artifact.",
        "",
        "## Run Configuration",
        "",
        "| Field | Value |",
        "| --- | ---: |",
        f"| Run ID | `{run_id}` |",
        f"| Available paired directional records | {paired_key_count} |",
        f"| Selected paired directional records | {selected_pair_count} |",
        f"| Row stride | {row_stride} |",
        f"| Maximum rows per file | {maximum_rows_per_file} |",
        "",
        "## Aggregate Signals",
        "",
        "| Metric | Mean polished minus simplified delta |",
        "| --- | ---: |",
        f"| Curve mean / offset [deg] | {mean_offset_delta:.9f} |",
        f"| Peak-to-peak [deg] | {mean_peak_to_peak_delta:.9f} |",
        f"| Mean absolute adjacent TE delta [deg] | {mean_smoothness_delta:.9f} |",
        f"| Maximum harmonic amplitude delta [deg] | {mean_maximum_harmonic_delta:.9f} |",
        "",
        "| Metric | Mean absolute delta |",
        "| --- | ---: |",
        f"| Curve mean / offset [deg] | {mean_absolute_offset_delta:.9f} |",
        f"| Peak-to-peak [deg] | {mean_absolute_peak_to_peak_delta:.9f} |",
        f"| Mean absolute adjacent TE delta [deg] | {mean_absolute_smoothness_delta:.9f} |",
        "",
        "## Classification Thresholds",
        "",
        "| Class | Trigger |",
        "| --- | --- |",
        f"| `sampling_anomaly` | row-count delta above `{ROW_COUNT_DIFFERENCE_THRESHOLD}` or theta-range delta above `{THETA_RANGE_DIFFERENCE_THRESHOLD_DEG:.9f} deg` |",
        f"| `shape_changed` | peak-to-peak or standard-deviation delta above `{SHAPE_DIFFERENCE_THRESHOLD_DEG:.9f} deg` |",
        f"| `smoothness_changed` | mean adjacent-delta delta above `{SMOOTHNESS_DIFFERENCE_THRESHOLD_DEG:.9f} deg` or max adjacent-delta delta above `{MAXIMUM_DELTA_DIFFERENCE_THRESHOLD_DEG:.9f} deg` |",
        f"| `harmonic_changed` | maximum diagnostic harmonic-amplitude delta above `{HARMONIC_DIFFERENCE_THRESHOLD_DEG:.9f} deg` |",
        f"| `offset_shifted` | curve mean / offset delta above `{OFFSET_SHIFT_THRESHOLD_DEG:.9f} deg` after the previous checks pass |",
        "| `nearly_identical` | none of the above thresholds fires |",
        "",
        "## Classification Summary",
        "",
        "| Class | Pair Count |",
        "| --- | ---: |",
        f"| `nearly_identical` | {classification_count_dictionary.get('nearly_identical', 0)} |",
        f"| `offset_shifted` | {classification_count_dictionary.get('offset_shifted', 0)} |",
        f"| `shape_changed` | {classification_count_dictionary.get('shape_changed', 0)} |",
        f"| `smoothness_changed` | {classification_count_dictionary.get('smoothness_changed', 0)} |",
        f"| `harmonic_changed` | {classification_count_dictionary.get('harmonic_changed', 0)} |",
        f"| `sampling_anomaly` | {classification_count_dictionary.get('sampling_anomaly', 0)} |",
        "",
        "## Direction Aggregates",
        "",
        "| Direction | Pairs | Mean Abs Offset Delta [deg] | Mean Abs P2P Delta [deg] | Offset-Shifted | Nearly Identical |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in direction_aggregate_rows:
        report_lines.append(
            "| "
            f"{row['group_value']} | "
            f"{row['pair_count']} | "
            f"{float(row['mean_abs_offset_delta_deg']):.9f} | "
            f"{float(row['mean_abs_peak_to_peak_delta_deg']):.9f} | "
            f"{row['offset_shifted_count']} | "
            f"{row['nearly_identical_count']} |"
        )

    report_lines.extend(
        [
            "",
            "## Global Aggregate Row",
            "",
            "| Pairs | Mean Abs Offset Delta [deg] | Mean Abs P2P Delta [deg] | Mean Abs Smoothness Delta [deg] | Mean Abs Max Harmonic Delta [deg] |",
            "| ---: | ---: | ---: | ---: | ---: |",
            "| "
            f"{global_aggregate_row['pair_count']} | "
            f"{float(global_aggregate_row['mean_abs_offset_delta_deg']):.9f} | "
            f"{float(global_aggregate_row['mean_abs_peak_to_peak_delta_deg']):.9f} | "
            f"{float(global_aggregate_row['mean_abs_smoothness_delta_deg']):.9f} | "
            f"{float(global_aggregate_row['mean_abs_max_harmonic_delta_deg']):.9f} |",
            "",
            "## Paired Preview",
            "",
            "| Direction | Speed | Torque | Temperature | Mean Delta [deg] | P2P Delta [deg] | Smoothness Delta [deg] | Class |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )

    for row in preview_rows:
        report_lines.append(
            "| "
            f"{row['direction_label']} | "
            f"{row['speed_rpm']} | "
            f"{row['torque_nm']} | "
            f"{row['temperature_deg']} | "
            f"{float(row['mean_difference_polished_minus_simplified_deg']):.9f} | "
            f"{float(row['peak_to_peak_difference_polished_minus_simplified_deg']):.9f} | "
            f"{float(row['smoothness_difference_polished_minus_simplified_deg']):.9f} | "
            f"`{row['classification']}` |"
        )

    report_lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This pass proves that the two dataset surfaces can be paired by",
            "operating condition and direction across the full available matrix",
            "without touching training campaign state. The reported deltas are",
            "diagnostic signals for choosing the next model-design branch; they are",
            "not model-validation metrics.",
            "",
            "The full-matrix evidence keeps peak-to-peak and smoothness deltas near",
            "zero while exposing offset and nonzero-harmonic differences. The next",
            "model-design gate should therefore prioritize offset / mean heads,",
            "centered-shape loss, harmonic-consistency diagnostics, and",
            "dirty-to-clean supervision before a heavy first PINN. Sampling anomalies",
            "remain isolated and should be handled as masks or exclusions, not as the",
            "main modeling target.",
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / PAIR_METRICS_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / HARMONIC_METRICS_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / AGGREGATE_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python -B scripts/reports/analysis/build_wave52a_paired_dataset_diagnostics.py --max-pairs 0",
            "```",
        ]
    )
    return report_lines


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--simplified-root", type=Path, default=SIMPLIFIED_DATASET_ROOT)
    argument_parser.add_argument("--polished-root", type=Path, default=POLISHED_DATASET_ROOT)
    argument_parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    argument_parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    argument_parser.add_argument("--run-id", type=str, default="")
    argument_parser.add_argument("--report-date", type=str, default="")
    argument_parser.add_argument("--max-pairs", type=int, default=24)
    argument_parser.add_argument("--row-stride", type=int, default=1)
    argument_parser.add_argument("--maximum-rows-per-file", type=int, default=20000)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def run_wave52a_paired_dataset_diagnostics(arguments: argparse.Namespace) -> tuple[Path, Path]:

    """Run the Wave 5.2A paired dataset diagnostic workflow."""

    # Resolve Output Paths
    run_id = arguments.run_id or f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__wave52a_paired_dataset_diagnostics"
    report_date = arguments.report_date or datetime.now().strftime("%Y-%m-%d")
    output_directory = arguments.output_root / run_id
    report_directory = arguments.report_topic_root / f"[{report_date}]"
    report_path = report_directory / REPORT_FILENAME

    # Build Pair Manifests
    simplified_records = collect_simplified_records(arguments.simplified_root)
    polished_records = collect_polished_records(arguments.polished_root)
    paired_key_list = sorted(set(simplified_records) & set(polished_records))
    selected_key_list = select_evenly_spaced_keys(paired_key_list, arguments.max_pairs)
    assert selected_key_list, "No paired dataset records found"

    # Summarize Selected Pairs
    pair_metric_rows: list[dict[str, str]] = []
    harmonic_metric_rows: list[dict[str, str]] = []
    for pair_key in selected_key_list:
        simplified_record = simplified_records[pair_key]
        polished_record = polished_records[pair_key]
        simplified_metrics, simplified_harmonic_rows = summarize_simplified_record(
            simplified_record,
            arguments.row_stride,
            arguments.maximum_rows_per_file,
        )
        polished_metrics, polished_harmonic_rows = summarize_polished_record(
            polished_record,
            arguments.row_stride,
            arguments.maximum_rows_per_file,
        )
        maximum_harmonic_amplitude_difference_deg = calculate_maximum_harmonic_amplitude_difference(
            simplified_harmonic_rows,
            polished_harmonic_rows,
        )
        pair_metric_rows.append(
            build_pair_metric_row(
                pair_key,
                simplified_record,
                polished_record,
                simplified_metrics,
                polished_metrics,
                maximum_harmonic_amplitude_difference_deg,
            )
        )
        harmonic_metric_rows.extend(build_harmonic_metric_rows(pair_key, simplified_harmonic_rows, polished_harmonic_rows))

    # Write Machine-Readable Artifacts
    aggregate_summary_rows = build_aggregate_rows(pair_metric_rows)
    write_csv(output_directory / PAIR_METRICS_FILENAME, pair_metric_rows)
    write_csv(output_directory / HARMONIC_METRICS_FILENAME, harmonic_metric_rows)
    write_csv(output_directory / AGGREGATE_SUMMARY_FILENAME, aggregate_summary_rows)
    classification_count_dictionary = count_by_column(pair_metric_rows, "classification")
    summary_dictionary = {
        "run_id": run_id,
        "paired_key_count": len(paired_key_list),
        "selected_pair_count": len(selected_key_list),
        "row_stride": int(arguments.row_stride),
        "maximum_rows_per_file": int(arguments.maximum_rows_per_file),
        "simplified_root": arguments.simplified_root.resolve().relative_to(PROJECT_PATH).as_posix(),
        "polished_root": arguments.polished_root.resolve().relative_to(PROJECT_PATH).as_posix(),
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "pair_metrics_path": (output_directory / PAIR_METRICS_FILENAME).relative_to(PROJECT_PATH).as_posix(),
        "harmonic_metrics_path": (output_directory / HARMONIC_METRICS_FILENAME).relative_to(PROJECT_PATH).as_posix(),
        "aggregate_summary_path": (output_directory / AGGREGATE_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix(),
        "classification_counts": classification_count_dictionary,
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with (output_directory / SUMMARY_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file:
        json.dump(summary_dictionary, output_file, indent=2)
        output_file.write("\n")

    # Write Authored Report
    report_lines = build_report_lines(
        run_id,
        len(selected_key_list),
        len(paired_key_list),
        arguments.row_stride,
        arguments.maximum_rows_per_file,
        pair_metric_rows,
        aggregate_summary_rows,
        output_directory,
    )
    report_directory.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")

    return output_directory, report_path


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_command_line_arguments()
    output_directory, report_path = run_wave52a_paired_dataset_diagnostics(arguments)
    print(f"Prepared Wave 5.2A paired dataset artifacts | {output_directory}")
    print(f"Prepared Markdown report | {report_path}")


if __name__ == "__main__":
    main()
