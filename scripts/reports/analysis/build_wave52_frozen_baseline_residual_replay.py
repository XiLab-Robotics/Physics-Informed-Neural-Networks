"""Replay frozen Wave 5.2 baselines over canonical dataset splits.

This non-training workflow resolves four accepted polished-setpoint ONNX
baselines, reconstructs their original train/validation/test datasets, and
emits per-curve residual metrics compatible with the Wave 5.2 MMT
residual-explanatory diagnostic.
"""

from __future__ import annotations

# Import Standard Libraries
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
import math
from pathlib import Path
import sys
from typing import Any

# Import Numerical And Serialization Libraries
import numpy as np
import onnxruntime as ort
import yaml
from tqdm import tqdm


PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))


# Import Repository Modules
from scripts.reports.analysis import build_shape_gated_te_curve_reranker
from scripts.reports.analysis import build_track2_familywise_onnx_report
from scripts.training import shared_training_infrastructure


DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "analysis"
    / "wave52_frozen_baseline_residual_replay.yaml"
)
PER_CURVE_METRICS_FILENAME = "per_curve_residual_metrics.csv"
BASELINE_MANIFEST_FILENAME = "resolved_baseline_manifest.yaml"
SPLIT_COVERAGE_FILENAME = "split_coverage_audit.csv"
VALIDATION_SUMMARY_FILENAME = "validation_summary.yaml"
RUN_CONFIGURATION_FILENAME = "run_configuration.yaml"
SELF_TEST_SUMMARY_FILENAME = "self_test_summary.yaml"


@dataclass(frozen=True)
class BaselineReplaySpecification:

    """Store one frozen baseline replay contract."""

    candidate_id: str
    surface: str
    direction_label: str
    architecture_class: str
    registry_path: Path
    reference_inventory_path: Path


@dataclass(frozen=True)
class ResolvedBaseline:

    """Store validated baseline provenance and runtime objects."""

    specification: BaselineReplaySpecification
    model_entry: build_track2_familywise_onnx_report.ExportedModelEntry
    training_config: dict[str, Any]
    registry_run_instance_id: str
    archive_run_instance_id: str
    registry_archive_run_aligned: bool


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Replay the four frozen Wave 5.2 baselines over canonical dataset "
            "splits without training."
        )
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Residual replay YAML configuration.",
    )
    argument_parser.add_argument(
        "--output-directory",
        type=Path,
        default=None,
        help="Optional explicit output directory.",
    )
    argument_parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run a bounded synthetic metric/schema check before replay.",
    )
    return argument_parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve one repository-relative path."""

    candidate_path = Path(path_value)
    if candidate_path.is_absolute():
        return candidate_path.resolve()
    return (PROJECT_PATH / candidate_path).resolve()


def format_project_path(path_value: str | Path) -> str:

    """Return a stable repository-relative path when possible."""

    resolved_path = Path(path_value).resolve()
    try:
        return str(resolved_path.relative_to(PROJECT_PATH))
    except ValueError:
        return str(resolved_path)


def load_yaml_dictionary(path_value: str | Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    yaml_path = resolve_project_path(path_value)
    assert yaml_path.exists(), f"YAML path does not exist | {yaml_path}"
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        payload = yaml.safe_load(yaml_file)
    assert isinstance(payload, dict), f"YAML root must be a dictionary | {yaml_path}"
    return payload


def write_yaml(path_value: str | Path, payload: dict[str, Any]) -> Path:

    """Write one stable YAML artifact."""

    yaml_path = Path(path_value)
    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8", newline="\n") as yaml_file:
        yaml.safe_dump(payload, yaml_file, sort_keys=False, allow_unicode=False)
    return yaml_path


def write_csv(path_value: str | Path, row_list: list[dict[str, Any]]) -> Path:

    """Write one stable CSV artifact."""

    csv_path = Path(path_value)
    assert row_list, f"Cannot write an empty CSV artifact | {csv_path}"
    field_name_list = list(row_list[0])
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)
    return csv_path


def format_float(value: float) -> str:

    """Format one finite float for machine-readable output."""

    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        return ""
    return f"{numeric_value:.9f}"


def normalize_surface(surface_value: str) -> str:

    """Normalize a configured surface to the repository ONNX surface label."""

    normalized_surface = str(surface_value).strip().lower()
    surface_alias_dictionary = {
        "fw": "forward",
        "forward": "forward",
        "bw": "backward",
        "backward": "backward",
    }
    assert normalized_surface in surface_alias_dictionary, (
        f"Unsupported replay surface | {surface_value}"
    )
    return surface_alias_dictionary[normalized_surface]


def build_baseline_specification_list(
    config_dictionary: dict[str, Any],
) -> list[BaselineReplaySpecification]:

    """Build and validate configured baseline specifications."""

    raw_baseline_list = config_dictionary.get("baselines", [])
    assert isinstance(raw_baseline_list, list) and raw_baseline_list, (
        "Replay configuration requires a non-empty baselines list"
    )

    specification_list: list[BaselineReplaySpecification] = []
    for raw_baseline in raw_baseline_list:
        assert isinstance(raw_baseline, dict), "Baseline entry must be a dictionary"
        specification_list.append(
            BaselineReplaySpecification(
                candidate_id=str(raw_baseline["candidate_id"]),
                surface=str(raw_baseline["surface"]),
                direction_label=str(raw_baseline["direction_label"]).strip().lower(),
                architecture_class=str(raw_baseline["architecture_class"]),
                registry_path=resolve_project_path(raw_baseline["registry_path"]),
                reference_inventory_path=resolve_project_path(
                    raw_baseline["reference_inventory_path"]
                ),
            )
        )

    candidate_id_list = [
        specification.candidate_id for specification in specification_list
    ]
    assert len(candidate_id_list) == len(set(candidate_id_list)), (
        "Replay candidate IDs must be unique"
    )
    return specification_list


def resolve_frozen_baseline(
    specification: BaselineReplaySpecification,
) -> ResolvedBaseline:

    """Resolve one registry-backed archived ONNX baseline."""

    registry_dictionary = load_yaml_dictionary(specification.registry_path)
    inventory_dictionary = load_yaml_dictionary(
        specification.reference_inventory_path
    )
    best_entry_dictionary = registry_dictionary.get("best_entry", {})

    archive_run_instance_id = str(inventory_dictionary["run_instance_id"])
    registry_run_instance_id = str(best_entry_dictionary.get("run_instance_id", ""))
    registry_archive_run_aligned = (
        registry_run_instance_id == archive_run_instance_id
    )

    model_surface = normalize_surface(str(inventory_dictionary["surface"]))
    expected_surface = normalize_surface(specification.surface)
    assert model_surface == expected_surface, (
        "Configured and archived surfaces differ | "
        f"candidate={specification.candidate_id} | "
        f"configured={expected_surface} | archived={model_surface}"
    )
    assert model_surface == specification.direction_label, (
        "Directional baseline must match its replay direction | "
        f"candidate={specification.candidate_id} | "
        f"surface={model_surface} | direction={specification.direction_label}"
    )
    assert str(inventory_dictionary["dataset_id"]) == "polished_dataset", (
        f"Unexpected baseline dataset | {specification.candidate_id}"
    )
    assert str(inventory_dictionary["input_mode"]) == "setpoints", (
        f"Unexpected baseline input mode | {specification.candidate_id}"
    )
    assert str(inventory_dictionary["onnx_export_status"]) == "exported", (
        f"Baseline ONNX export is not complete | {specification.candidate_id}"
    )

    onnx_model_path = resolve_project_path(inventory_dictionary["onnx_model_path"])
    python_model_path = resolve_project_path(
        inventory_dictionary["python_model_path"]
    )
    training_config_path = resolve_project_path(
        inventory_dictionary["source_run_snapshot_path_map"][
            "training_config.snapshot.yaml"
        ]
    )
    assert onnx_model_path.exists(), f"Missing ONNX model | {onnx_model_path}"
    assert python_model_path.exists(), f"Missing Python checkpoint | {python_model_path}"
    assert training_config_path.exists(), (
        f"Missing training config snapshot | {training_config_path}"
    )

    training_config = load_yaml_dictionary(training_config_path)
    dataset_dictionary = training_config.get("dataset", {})
    assert str(dataset_dictionary.get("name", "")) == "polished_dataset", (
        f"Training snapshot dataset mismatch | {training_config_path}"
    )
    assert str(dataset_dictionary.get("input_mode", "")) == "setpoints", (
        f"Training snapshot input-mode mismatch | {training_config_path}"
    )

    model_entry = build_track2_familywise_onnx_report.ExportedModelEntry(
        dataset_id=str(inventory_dictionary["dataset_id"]),
        input_mode=str(inventory_dictionary["input_mode"]),
        model_family=str(inventory_dictionary["model_family"]),
        model_type=str(inventory_dictionary["model_type"]),
        surface=model_surface,
        run_name=str(inventory_dictionary["run_name"]),
        run_instance_id=archive_run_instance_id,
        dataset_schema=str(inventory_dictionary["dataset_schema"]),
        onnx_model_path=onnx_model_path,
        python_model_path=python_model_path,
        training_config_path=training_config_path,
        source_output_directory=str(inventory_dictionary["source_output_directory"]),
        source_best_checkpoint_path=str(
            inventory_dictionary["source_best_checkpoint_path"]
        ),
        source_inventory_path=specification.reference_inventory_path,
    )
    return ResolvedBaseline(
        specification=specification,
        model_entry=model_entry,
        training_config=training_config,
        registry_run_instance_id=registry_run_instance_id,
        archive_run_instance_id=archive_run_instance_id,
        registry_archive_run_aligned=registry_archive_run_aligned,
    )


def build_permissive_shape_thresholds(
) -> build_shape_gated_te_curve_reranker.ShapeGateThresholds:

    """Build thresholds that retain metrics without making promotion claims."""

    return build_shape_gated_te_curve_reranker.ShapeGateThresholds(
        minimum_fft_amplitude_similarity=-math.inf,
        minimum_derivative_correlation=-math.inf,
        minimum_smoothed_derivative_correlation=-math.inf,
        minimum_derivative_sign_agreement_rate=-math.inf,
        maximum_normalized_derivative_rmse=math.inf,
        maximum_mean_harmonic_amplitude_error_pct=math.inf,
        maximum_mean_harmonic_phase_error_deg=math.inf,
        maximum_peak_to_peak_error_pct=math.inf,
        minimum_per_curve_shape_pass_rate=0.0,
        near_pass_minimum_fft_amplitude_similarity=-math.inf,
        near_pass_maximum_mean_harmonic_amplitude_error_pct=math.inf,
        near_pass_maximum_mean_harmonic_phase_error_deg=math.inf,
        near_pass_maximum_peak_to_peak_error_pct=math.inf,
        near_pass_minimum_derivative_sign_agreement_rate=-math.inf,
        near_pass_maximum_normalized_derivative_rmse=math.inf,
    )


def build_candidate_metric_entry(
    resolved_baseline: ResolvedBaseline,
    curve_sample: dict[str, Any],
    angular_position_deg: np.ndarray,
    target_curve_deg: np.ndarray,
    prediction_curve_deg: np.ndarray,
) -> dict[str, Any]:

    """Build one shape-metric-compatible candidate entry."""

    metric_dictionary = build_track2_familywise_onnx_report.compute_curve_metrics(
        target_curve_deg,
        prediction_curve_deg,
    )
    specification = resolved_baseline.specification
    return {
        "candidate_id": specification.candidate_id,
        "candidate_family": resolved_baseline.model_entry.model_family,
        "candidate_kind": "frozen_archive_onnx",
        "candidate_source_label": "wave52_frozen_baseline_residual_replay",
        "candidate_surface": specification.surface,
        "direction_label": specification.direction_label,
        "source_file_path": format_project_path(curve_sample["source_file_path"]),
        "speed_rpm": float(curve_sample["speed_rpm"]),
        "torque_nm": float(curve_sample["torque_nm"]),
        "oil_temperature_deg": float(curve_sample["oil_temperature_deg"]),
        "angular_position_deg": np.asarray(angular_position_deg, dtype=float),
        "truth_curve_deg": np.asarray(target_curve_deg, dtype=float),
        "predicted_curve_deg": np.asarray(prediction_curve_deg, dtype=float),
        "metrics": metric_dictionary,
    }


def evaluate_baseline_split(
    resolved_baseline: ResolvedBaseline,
    split_name: str,
    split_dataset: Any,
    session: ort.InferenceSession,
    harmonic_order_list: list[int],
    mdn_playback_channel: str,
) -> list[dict[str, Any]]:

    """Evaluate one frozen baseline over one canonical dataset split."""

    row_list: list[dict[str, Any]] = []
    thresholds = build_permissive_shape_thresholds()
    specification = resolved_baseline.specification

    for dataset_index in tqdm(
        range(len(split_dataset)),
        desc=f"{specification.candidate_id}:{split_name}",
        unit="curve",
        ascii=True,
        ncols=100,
        dynamic_ncols=False,
        leave=False,
    ):
        curve_sample = split_dataset[dataset_index]
        direction_label = str(curve_sample["direction_label"]).strip().lower()
        assert direction_label == specification.direction_label, (
            "Directional split contamination detected | "
            f"candidate={specification.candidate_id} | "
            f"expected={specification.direction_label} | observed={direction_label}"
        )

        (
            input_feature_matrix,
            target_curve_deg,
            angular_position_deg,
        ) = build_track2_familywise_onnx_report.build_model_input_payload(
            curve_sample=curve_sample,
            session=session,
            training_config=resolved_baseline.training_config,
        )
        raw_prediction_curve_deg = (
            build_track2_familywise_onnx_report.predict_curve(
                session=session,
                input_feature_matrix=np.ascontiguousarray(
                    input_feature_matrix,
                    dtype=np.float32,
                ),
                training_config=resolved_baseline.training_config,
            )
        )
        prediction_curve_deg = (
            build_track2_familywise_onnx_report.select_deterministic_prediction_curve(
                raw_prediction_curve_deg=raw_prediction_curve_deg,
                target_curve_deg=target_curve_deg,
                training_config=resolved_baseline.training_config,
                mdn_playback_channel=mdn_playback_channel,
            )
        )
        assert prediction_curve_deg.shape == target_curve_deg.shape, (
            "Prediction and target curve shapes differ | "
            f"candidate={specification.candidate_id} | split={split_name} | "
            f"prediction={prediction_curve_deg.shape} | target={target_curve_deg.shape}"
        )

        candidate_entry = build_candidate_metric_entry(
            resolved_baseline=resolved_baseline,
            curve_sample=curve_sample,
            angular_position_deg=angular_position_deg,
            target_curve_deg=target_curve_deg,
            prediction_curve_deg=prediction_curve_deg,
        )
        curve_metric = build_shape_gated_te_curve_reranker.compute_curve_metric(
            candidate_entry=candidate_entry,
            harmonic_order_list=harmonic_order_list,
            thresholds=thresholds,
        )
        metric_row = curve_metric.to_csv_row()
        metric_row["split_name"] = split_name
        metric_row["dataset_index"] = dataset_index
        metric_row["run_instance_id"] = resolved_baseline.archive_run_instance_id
        row_list.append(metric_row)

    assert row_list, (
        f"Replay produced no rows | candidate={specification.candidate_id} | "
        f"split={split_name}"
    )
    return row_list


def update_p95_metric_values(row_list: list[dict[str, Any]]) -> None:

    """Populate per-candidate, per-split P95 percentage-error values."""

    grouped_row_dictionary: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in row_list:
        key = (str(row["candidate_id"]), str(row["split_name"]))
        grouped_row_dictionary.setdefault(key, []).append(row)

    for grouped_row_list in grouped_row_dictionary.values():
        percentage_error_array = np.asarray(
            [
                float(row["mean_percentage_error_pct"])
                for row in grouped_row_list
            ],
            dtype=float,
        )
        p95_value = float(np.percentile(percentage_error_array, 95.0))
        for row in grouped_row_list:
            row["p95_candidate_percentage_error_pct"] = format_float(p95_value)


def build_split_coverage_row_list(
    residual_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build per-candidate split and direction coverage evidence."""

    count_dictionary: dict[tuple[str, str, str, str], int] = {}
    for row in residual_row_list:
        key = (
            str(row["candidate_id"]),
            str(row["candidate_surface"]),
            str(row["direction_label"]),
            str(row["split_name"]),
        )
        count_dictionary[key] = count_dictionary.get(key, 0) + 1

    return [
        {
            "candidate_id": key[0],
            "surface": key[1],
            "direction_label": key[2],
            "split_name": key[3],
            "residual_row_count": count,
            "fit_allowed": str(key[3] == "train").lower(),
        }
        for key, count in sorted(count_dictionary.items())
    ]


def build_baseline_manifest(
    resolved_baseline_list: list[ResolvedBaseline],
) -> dict[str, Any]:

    """Build machine-readable frozen baseline provenance."""

    return {
        "schema_version": 1,
        "baseline_count": len(resolved_baseline_list),
        "baseline_list": [
            {
                "candidate_id": baseline.specification.candidate_id,
                "surface": baseline.specification.surface,
                "direction_label": baseline.specification.direction_label,
                "architecture_class": baseline.specification.architecture_class,
                "registry_path": format_project_path(
                    baseline.specification.registry_path
                ),
                "reference_inventory_path": format_project_path(
                    baseline.specification.reference_inventory_path
                ),
                "registry_run_instance_id": baseline.registry_run_instance_id,
                "archive_run_instance_id": baseline.archive_run_instance_id,
                "registry_archive_run_aligned": (
                    baseline.registry_archive_run_aligned
                ),
                "dataset_id": baseline.model_entry.dataset_id,
                "dataset_schema": baseline.model_entry.dataset_schema,
                "input_mode": baseline.model_entry.input_mode,
                "model_family": baseline.model_entry.model_family,
                "model_type": baseline.model_entry.model_type,
                "onnx_model_path": format_project_path(
                    baseline.model_entry.onnx_model_path
                ),
                "python_model_path": format_project_path(
                    baseline.model_entry.python_model_path
                ),
                "training_config_path": format_project_path(
                    baseline.model_entry.training_config_path
                ),
            }
            for baseline in resolved_baseline_list
        ],
    }


def build_aggregate_summary_row_list(
    residual_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Summarize residual metrics per candidate and split."""

    grouped_row_dictionary: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in residual_row_list:
        key = (str(row["candidate_id"]), str(row["split_name"]))
        grouped_row_dictionary.setdefault(key, []).append(row)

    target_name_list = [
        "raw_mae_deg",
        "absolute_offset_error_deg",
        "centered_mae_deg",
        "peak_to_peak_error_pct",
        "mean_harmonic_amplitude_error_pct",
        "mean_harmonic_phase_error_deg",
        "normalized_derivative_rmse",
    ]
    summary_row_list: list[dict[str, Any]] = []
    for key, grouped_row_list in sorted(grouped_row_dictionary.items()):
        summary_row: dict[str, Any] = {
            "candidate_id": key[0],
            "split_name": key[1],
            "row_count": len(grouped_row_list),
        }
        for target_name in target_name_list:
            value_array = np.asarray(
                [
                    float(row[target_name])
                    for row in grouped_row_list
                    if str(row[target_name]).strip()
                ],
                dtype=float,
            )
            summary_row[f"mean_{target_name}"] = format_float(
                float(np.mean(value_array))
            )
        summary_row_list.append(summary_row)
    return summary_row_list


def run_self_test(
    output_directory: Path,
    harmonic_order_list: list[int],
) -> Path:

    """Run a bounded synthetic metric and schema self-test."""

    angle_array = np.linspace(0.0, 360.0, 361, dtype=float)
    truth_curve = (
        0.02 * np.sin(np.deg2rad(angle_array))
        + 0.004 * np.sin(3.0 * np.deg2rad(angle_array))
    )
    prediction_curve = truth_curve + 0.001
    candidate_entry = {
        "candidate_id": "synthetic_baseline",
        "candidate_family": "synthetic",
        "candidate_kind": "self_test",
        "candidate_source_label": "wave52_frozen_baseline_residual_replay",
        "candidate_surface": "Fw",
        "direction_label": "forward",
        "source_file_path": "synthetic.csv",
        "speed_rpm": 1000.0,
        "torque_nm": 1000.0,
        "oil_temperature_deg": 25.0,
        "angular_position_deg": angle_array,
        "truth_curve_deg": truth_curve,
        "predicted_curve_deg": prediction_curve,
        "metrics": build_track2_familywise_onnx_report.compute_curve_metrics(
            truth_curve,
            prediction_curve,
        ),
    }
    metric = build_shape_gated_te_curve_reranker.compute_curve_metric(
        candidate_entry,
        harmonic_order_list,
        build_permissive_shape_thresholds(),
    )
    assert math.isclose(metric.raw_mae_deg, 0.001, rel_tol=0.0, abs_tol=1.0e-12)
    assert math.isclose(
        metric.absolute_offset_error_deg,
        0.001,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert metric.centered_mae_deg <= 1.0e-12
    assert metric.fft_amplitude_similarity >= 0.999999
    return write_yaml(
        output_directory / SELF_TEST_SUMMARY_FILENAME,
        {
            "schema_version": 1,
            "status": "passed",
            "synthetic_raw_mae_deg": metric.raw_mae_deg,
            "synthetic_absolute_offset_error_deg": metric.absolute_offset_error_deg,
            "synthetic_centered_mae_deg": metric.centered_mae_deg,
            "synthetic_fft_amplitude_similarity": metric.fft_amplitude_similarity,
        },
    )


def build_report(
    report_path: Path,
    run_instance_id: str,
    config_path: Path,
    output_directory: Path,
    resolved_baseline_list: list[ResolvedBaseline],
    split_coverage_row_list: list[dict[str, Any]],
    aggregate_summary_row_list: list[dict[str, Any]],
    residual_row_count: int,
) -> Path:

    """Generate the residual replay analytical report."""

    report_line_list = [
        "# Wave 5.2 Frozen-Baseline Residual Replay",
        "",
        "## Overview",
        "",
        "This non-training replay evaluated the four frozen accepted",
        "`polished_dataset` setpoint baselines over their canonical training,",
        "validation, and test datasets. It generated the per-curve residual schema",
        "required by the Wave 5.2 MMT residual-explanatory diagnostic.",
        "",
        "No checkpoint was changed, no model was trained, no random split was",
        "introduced, and no model or program registry was updated.",
        "",
        "## Provenance",
        "",
        f"- run instance: `{run_instance_id}`;",
        f"- configuration: `{format_project_path(config_path)}`;",
        f"- output directory: `{format_project_path(output_directory)}`;",
        f"- total residual rows: `{residual_row_count}`;",
        "- inference provider: `CPUExecutionProvider`;",
        "- replay input mode: `polished_dataset + setpoints`.",
        "",
        "## Split And Registry Provenance",
        "",
        "The authoritative split is reconstructed separately from each archived",
        "direction-specific training snapshot. Each baseline therefore contributes",
        "678 training, 194 validation, and 97 test curves. These memberships must",
        "not be replaced by the earlier global audit split over the combined",
        "`Fw` and `Bw` file inventory.",
        "",
        "The selected July setpoint archives do not share run IDs with the current",
        "family-registry `best_entry` records, which still identify older June",
        "point-schema runs. This mismatch is retained as an explicit provenance",
        "caveat rather than treated as a replay failure: the frozen selected-model",
        "reference inventories and their training snapshots are the authoritative",
        "sources for this replay.",
        "",
        "| Candidate | Registry run | Selected archive run | Aligned |",
        "| --- | --- | --- | --- |",
    ]
    for baseline in resolved_baseline_list:
        report_line_list.append(
            f"| `{baseline.specification.candidate_id}` | "
            f"`{baseline.registry_run_instance_id}` | "
            f"`{baseline.archive_run_instance_id}` | "
            f"`{str(baseline.registry_archive_run_aligned).lower()}` |"
        )

    report_line_list.extend(
        [
        "",
        "## Split Coverage",
        "",
        "| Candidate | Surface | Direction | Split | Residual rows | Fit allowed |",
        "| --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in split_coverage_row_list:
        report_line_list.append(
            f"| `{row['candidate_id']}` | `{row['surface']}` | "
            f"`{row['direction_label']}` | `{row['split_name']}` | "
            f"{row['residual_row_count']} | `{row['fit_allowed']}` |"
        )

    report_line_list.extend(
        [
            "",
            "## Residual Summary",
            "",
            "| Candidate | Split | Rows | Raw MAE [deg] | Offset [deg] | "
            "Centered MAE [deg] |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in aggregate_summary_row_list:
        report_line_list.append(
            f"| `{row['candidate_id']}` | `{row['split_name']}` | "
            f"{row['row_count']} | {float(row['mean_raw_mae_deg']):.6f} | "
            f"{float(row['mean_absolute_offset_error_deg']):.6f} | "
            f"{float(row['mean_centered_mae_deg']):.6f} |"
        )

    report_line_list.extend(
        [
            "",
            "## Validation Decision",
            "",
            "The residual replay closes the provenance blocker only when every",
            "configured candidate has non-zero training, validation, and test",
            "coverage and every residual row resolves to its canonical source file.",
            "",
            "The resulting per-curve artifact is an inference result, not evidence",
            "that MMT is useful. Its next authorized consumer is the leakage-safe",
            "MMT explanatory comparison, which must fit on training residuals only",
            "and compare held-out value against metadata-only and shuffled controls.",
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- baseline manifest: `{format_project_path(output_directory / BASELINE_MANIFEST_FILENAME)}`;",
            f"- split coverage: `{format_project_path(output_directory / SPLIT_COVERAGE_FILENAME)}`;",
            f"- residual metrics: `{format_project_path(output_directory / PER_CURVE_METRICS_FILENAME)}`;",
            f"- run configuration: `{format_project_path(output_directory / RUN_CONFIGURATION_FILENAME)}`;",
            f"- validation summary: `{format_project_path(output_directory / VALIDATION_SUMMARY_FILENAME)}`.",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        "\n".join(report_line_list) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return report_path


def run_replay(
    config_path: Path,
    output_directory_override: Path | None,
    run_self_test_first: bool,
) -> list[Path]:

    """Run the full non-training frozen baseline residual replay."""

    resolved_config_path = resolve_project_path(config_path)
    config_dictionary = load_yaml_dictionary(resolved_config_path)
    metadata_dictionary = config_dictionary.get("metadata", {})
    assert metadata_dictionary.get("training_allowed") is False, (
        "Residual replay configuration must explicitly disable training"
    )
    assert metadata_dictionary.get("registry_update_allowed") is False, (
        "Residual replay configuration must explicitly disable registry updates"
    )

    run_instance_id = (
        datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")
        + "__wave52_frozen_baseline_residual_replay"
    )
    path_dictionary = config_dictionary["paths"]
    output_directory = (
        resolve_project_path(output_directory_override)
        if output_directory_override is not None
        else resolve_project_path(path_dictionary["output_root"]) / run_instance_id
    )
    output_directory.mkdir(parents=True, exist_ok=False)

    runtime_dictionary = config_dictionary["runtime"]
    split_name_list = [
        str(value) for value in runtime_dictionary["split_name_list"]
    ]
    assert split_name_list == ["train", "validation", "test"], (
        "Residual replay requires ordered train, validation, and test coverage"
    )
    provider_list = [
        str(value) for value in runtime_dictionary["provider_list"]
    ]
    assert provider_list == ["CPUExecutionProvider"], (
        "Frozen residual replay must use the explicit CPU execution provider"
    )
    harmonic_order_list = [
        int(value)
        for value in config_dictionary["metrics"]["harmonic_order_list"]
    ]

    artifact_path_list: list[Path] = []
    if run_self_test_first:
        artifact_path_list.append(
            run_self_test(output_directory, harmonic_order_list)
        )

    specification_list = build_baseline_specification_list(config_dictionary)
    resolved_baseline_list = [
        resolve_frozen_baseline(specification)
        for specification in specification_list
    ]
    baseline_manifest_path = write_yaml(
        output_directory / BASELINE_MANIFEST_FILENAME,
        build_baseline_manifest(resolved_baseline_list),
    )
    artifact_path_list.append(baseline_manifest_path)

    residual_row_list: list[dict[str, Any]] = []
    for resolved_baseline in resolved_baseline_list:
        datamodule = shared_training_infrastructure.create_datamodule_from_training_config(
            resolved_baseline.training_config
        )
        datamodule.setup(stage="fit")
        dataset_dictionary = {
            "train": datamodule.train_dataset,
            "validation": datamodule.validation_dataset,
            "test": datamodule.test_dataset,
        }
        assert all(dataset_dictionary.values()), (
            f"One or more canonical splits are empty | "
            f"{resolved_baseline.specification.candidate_id}"
        )
        session = ort.InferenceSession(
            str(resolved_baseline.model_entry.onnx_model_path),
            providers=provider_list,
        )
        assert session.get_providers()[0] == "CPUExecutionProvider", (
            f"Unexpected ONNX provider order | {session.get_providers()}"
        )

        for split_name in split_name_list:
            residual_row_list.extend(
                evaluate_baseline_split(
                    resolved_baseline=resolved_baseline,
                    split_name=split_name,
                    split_dataset=dataset_dictionary[split_name],
                    session=session,
                    harmonic_order_list=harmonic_order_list,
                    mdn_playback_channel=str(
                        runtime_dictionary["mdn_playback_channel"]
                    ),
                )
            )

    update_p95_metric_values(residual_row_list)
    residual_metrics_path = write_csv(
        output_directory / PER_CURVE_METRICS_FILENAME,
        residual_row_list,
    )
    artifact_path_list.append(residual_metrics_path)

    split_coverage_row_list = build_split_coverage_row_list(residual_row_list)
    expected_coverage_row_count = len(resolved_baseline_list) * len(split_name_list)
    assert len(split_coverage_row_list) == expected_coverage_row_count, (
        "Residual replay split coverage is incomplete | "
        f"expected={expected_coverage_row_count} | "
        f"observed={len(split_coverage_row_list)}"
    )
    assert all(
        int(row["residual_row_count"]) > 0
        for row in split_coverage_row_list
    ), "Residual replay contains an empty candidate/split cell"
    split_coverage_path = write_csv(
        output_directory / SPLIT_COVERAGE_FILENAME,
        split_coverage_row_list,
    )
    artifact_path_list.append(split_coverage_path)

    aggregate_summary_row_list = build_aggregate_summary_row_list(
        residual_row_list
    )
    aggregate_summary_path = write_csv(
        output_directory / "aggregate_residual_summary.csv",
        aggregate_summary_row_list,
    )
    artifact_path_list.append(aggregate_summary_path)

    copied_config_path = write_yaml(
        output_directory / RUN_CONFIGURATION_FILENAME,
        config_dictionary,
    )
    artifact_path_list.append(copied_config_path)

    report_path = resolve_project_path(path_dictionary["report_path"])
    build_report(
        report_path=report_path,
        run_instance_id=run_instance_id,
        config_path=resolved_config_path,
        output_directory=output_directory,
        resolved_baseline_list=resolved_baseline_list,
        split_coverage_row_list=split_coverage_row_list,
        aggregate_summary_row_list=aggregate_summary_row_list,
        residual_row_count=len(residual_row_list),
    )
    artifact_path_list.append(report_path)

    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "status": "completed",
        "decision": "residual_replay_ready_for_mmt_explanatory_rerun",
        "training_executed": False,
        "registry_updated": False,
        "baseline_count": len(resolved_baseline_list),
        "split_name_list": split_name_list,
        "residual_row_count": len(residual_row_list),
        "coverage_row_count": len(split_coverage_row_list),
        "all_candidate_split_cells_non_empty": True,
        "artifact_path_list": [
            format_project_path(path_value)
            for path_value in artifact_path_list
        ],
    }
    validation_summary_path = write_yaml(
        output_directory / VALIDATION_SUMMARY_FILENAME,
        validation_summary,
    )
    artifact_path_list.append(validation_summary_path)

    print("Wave 5.2 frozen-baseline residual replay completed")
    print(f"Run instance: {run_instance_id}")
    print(f"Residual rows: {len(residual_row_list)}")
    print(f"Output directory: {format_project_path(output_directory)}")
    print(f"Report: {format_project_path(report_path)}")
    return artifact_path_list


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_arguments()
    run_replay(
        config_path=arguments.config,
        output_directory_override=arguments.output_directory,
        run_self_test_first=bool(arguments.self_test),
    )


if __name__ == "__main__":
    main()
