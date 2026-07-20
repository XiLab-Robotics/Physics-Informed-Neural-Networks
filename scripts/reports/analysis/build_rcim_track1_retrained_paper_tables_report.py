"""Build RCIM Track1 retrained paper-table equivalents."""

from __future__ import annotations

# Import Python Utilities
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import yaml

REPORT_DIRECTORY = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "te_curve_verification_pipeline"
    / "03_family_reports"
    / "rcim_track1"
    / "[2026-07-19]"
)
REPORT_FILENAME = "track2_rcim_track1_retrained_paper_tables_report.md"
TARGET_PATTERN = re.compile(
    r"^fft_y_(?P<surface_short_name>Fw|Bw|Global)_filtered_"
    r"(?P<target_kind>ampl|phase)_(?P<harmonic_order>\d+)$"
)
FAMILY_ORDER_LIST = ["SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM", "ELM"]
MAX_FAMILY_COLUMNS_PER_TABLE = 6
SURFACE_ORDER_LIST = ["forward", "backward", "global"]
SURFACE_TITLE_DICTIONARY = {
    "forward": "Forward",
    "backward": "Backward",
    "global": "Global",
}
TARGET_KIND_TITLE_DICTIONARY = {
    "amplitude": "Amplitude",
    "phase": "Phase",
}
METRIC_TITLE_DICTIONARY = {
    "mae": "MAE",
    "rmse": "RMSE",
}
TABLE_NUMBER_MAP = {
    ("amplitude", "mae"): "Table 2",
    ("amplitude", "rmse"): "Table 3",
    ("phase", "mae"): "Table 4",
    ("phase", "rmse"): "Table 5",
}


@dataclass(frozen=True)
class DatasetSpecification:

    """Store one dataset/input-mode source for the paper-table report."""

    dataset_id: str
    input_mode: str
    display_name: str
    source_kind: str
    archive_root: Path
    promotion_inventory_path: Path | None = None


@dataclass(frozen=True)
class ComponentMetric:

    """Store one harmonic component metric for one family."""

    target_name: str
    target_kind: str
    harmonic_order: int
    surface: str
    family_name: str
    mae: float
    rmse: float
    source_path: Path


DATASET_SPECIFICATION_LIST = [
    DatasetSpecification(
        dataset_id="simplified_dataset",
        input_mode="setpoints",
        display_name="Simplified Dataset + Setpoints",
        source_kind="reference_inventory",
        archive_root=PROJECT_PATH / "models" / "simplified_dataset" / "paper_reference" / "rcim_track1",
    ),
    DatasetSpecification(
        dataset_id="polished_dataset",
        input_mode="setpoints",
        display_name="Polished Dataset + Setpoints",
        source_kind="validation_summary",
        archive_root=PROJECT_PATH
        / "models"
        / "polished_dataset"
        / "paper_reference"
        / "rcim_track1"
        / "setpoints",
        promotion_inventory_path=PROJECT_PATH
        / "models"
        / "polished_dataset"
        / "paper_reference"
        / "rcim_track1"
        / "setpoints"
        / "promotion_inventory.yaml",
    ),
    DatasetSpecification(
        dataset_id="polished_dataset",
        input_mode="actual_values",
        display_name="Polished Dataset + Actual Values",
        source_kind="validation_summary",
        archive_root=PROJECT_PATH
        / "models"
        / "polished_dataset"
        / "paper_reference"
        / "rcim_track1"
        / "actual_values",
        promotion_inventory_path=PROJECT_PATH
        / "models"
        / "polished_dataset"
        / "paper_reference"
        / "rcim_track1"
        / "actual_values"
        / "promotion_inventory.yaml",
    ),
]


def load_yaml_file(yaml_path: Path) -> dict[str, Any]:
    """Load a YAML file and return a dictionary."""

    if not yaml_path.exists():
        raise FileNotFoundError(f"Missing YAML file: {yaml_path}")
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_payload = yaml.safe_load(yaml_file)
    if not isinstance(loaded_payload, dict):
        raise ValueError(f"YAML root is not a dictionary: {yaml_path}")
    return loaded_payload


def parse_target_name(target_name: str, default_surface: str) -> tuple[str, int, str]:
    """Parse RCIM target names into target kind, harmonic order, and surface."""

    match = TARGET_PATTERN.match(target_name)
    if match is None:
        raise ValueError(f"Unsupported RCIM target name: {target_name}")

    target_kind = "amplitude" if match.group("target_kind") == "ampl" else "phase"
    harmonic_order = int(match.group("harmonic_order"))
    surface_short_name = match.group("surface_short_name")
    parsed_surface = {
        "Fw": "forward",
        "Bw": "backward",
        "Global": "global",
    }[surface_short_name]
    if parsed_surface != default_surface:
        raise ValueError(
            f"Target {target_name} belongs to {parsed_surface}, not expected {default_surface}"
        )
    return target_kind, harmonic_order, parsed_surface


def normalize_family_name(raw_family_name: str) -> str:
    """Normalize family labels used by different archive generations."""

    normalized_family_name = str(raw_family_name).strip().upper()
    if normalized_family_name == "SVM":
        return "SVR"
    return normalized_family_name


def choose_metric_value(metric_payload: dict[str, Any], metric_name: str) -> float:
    """Read a metric from either benchmark or validation-summary keys."""

    candidate_key_list = [
        metric_name,
        f"training_metric_{metric_name}",
        f"benchmark_{metric_name}",
        f"winning_{metric_name}",
    ]
    for candidate_key in candidate_key_list:
        if candidate_key in metric_payload and metric_payload[candidate_key] is not None:
            return float(metric_payload[candidate_key])
    raise KeyError(f"Missing {metric_name} in metric payload for {metric_payload.get('target_name')}")


def collect_reference_inventory_metrics(specification: DatasetSpecification) -> list[ComponentMetric]:
    """Collect component metrics from simplified reference inventories."""

    component_metric_list: list[ComponentMetric] = []
    for surface in SURFACE_ORDER_LIST:
        surface_root = specification.archive_root / surface
        if not surface_root.exists():
            continue
        for inventory_path in sorted(surface_root.glob("*_reference_models/reference_inventory.yaml")):
            inventory_payload = load_yaml_file(inventory_path)
            raw_family_name = inventory_payload.get(
                "implementation_family_name",
                inventory_payload.get("paper_family_name", inventory_path.parent.name),
            )
            family_name = normalize_family_name(str(raw_family_name))
            reference_models = inventory_payload.get("reference_models", [])
            if not isinstance(reference_models, list):
                raise ValueError(f"reference_models is not a list in {inventory_path}")
            for model_payload in reference_models:
                if not isinstance(model_payload, dict):
                    continue
                target_name = str(model_payload["target_name"])
                target_kind, harmonic_order, parsed_surface = parse_target_name(target_name, surface)
                component_metric_list.append(
                    ComponentMetric(
                        target_name=target_name,
                        target_kind=target_kind,
                        harmonic_order=harmonic_order,
                        surface=parsed_surface,
                        family_name=family_name,
                        mae=choose_metric_value(model_payload, "mae"),
                        rmse=choose_metric_value(model_payload, "rmse"),
                        source_path=inventory_path,
                    )
                )
    return component_metric_list


def collect_validation_summary_metrics(specification: DatasetSpecification) -> list[ComponentMetric]:
    """Collect component metrics from retraining validation summaries."""

    if specification.promotion_inventory_path is None:
        raise ValueError(f"Missing promotion inventory path for {specification.display_name}")

    promotion_payload = load_yaml_file(specification.promotion_inventory_path)
    component_metric_list: list[ComponentMetric] = []
    surfaces = promotion_payload.get("surfaces", [])
    if not isinstance(surfaces, list):
        raise ValueError(f"surfaces is not a list in {specification.promotion_inventory_path}")

    for surface_payload in surfaces:
        if not isinstance(surface_payload, dict):
            continue
        surface = str(surface_payload["surface"])
        validation_directory = PROJECT_PATH / str(surface_payload["source_validation_directory"])
        validation_summary_path = validation_directory / "validation_summary.yaml"
        validation_payload = load_yaml_file(validation_summary_path)
        family_ranking = validation_payload.get("family_ranking", [])
        if not isinstance(family_ranking, list):
            raise ValueError(f"family_ranking is not a list in {validation_summary_path}")
        for family_payload in family_ranking:
            if not isinstance(family_payload, dict):
                continue
            family_name = normalize_family_name(str(family_payload["family_name"]))
            target_metrics = family_payload.get("target_metrics", [])
            if not isinstance(target_metrics, list):
                raise ValueError(f"target_metrics is not a list in {validation_summary_path}")
            for metric_payload in target_metrics:
                if not isinstance(metric_payload, dict):
                    continue
                target_name = str(metric_payload["target_name"])
                target_kind, harmonic_order, parsed_surface = parse_target_name(target_name, surface)
                component_metric_list.append(
                    ComponentMetric(
                        target_name=target_name,
                        target_kind=target_kind,
                        harmonic_order=harmonic_order,
                        surface=parsed_surface,
                        family_name=family_name,
                        mae=choose_metric_value(metric_payload, "mae"),
                        rmse=choose_metric_value(metric_payload, "rmse"),
                        source_path=validation_summary_path,
                    )
                )
    return component_metric_list


def collect_dataset_metrics(specification: DatasetSpecification) -> list[ComponentMetric]:
    """Collect metrics for one dataset specification."""

    if specification.source_kind == "reference_inventory":
        return collect_reference_inventory_metrics(specification)
    if specification.source_kind == "validation_summary":
        return collect_validation_summary_metrics(specification)
    raise ValueError(f"Unsupported source kind: {specification.source_kind}")


def build_metric_lookup(
    component_metric_list: list[ComponentMetric],
) -> dict[tuple[str, str, int, str], ComponentMetric]:
    """Build a surface, kind, harmonic, family lookup."""

    metric_lookup: dict[tuple[str, str, int, str], ComponentMetric] = {}
    for component_metric in component_metric_list:
        lookup_key = (
            component_metric.surface,
            component_metric.target_kind,
            component_metric.harmonic_order,
            component_metric.family_name,
        )
        if lookup_key in metric_lookup:
            existing_metric = metric_lookup[lookup_key]
            if (
                abs(existing_metric.mae - component_metric.mae) > 1e-15
                or abs(existing_metric.rmse - component_metric.rmse) > 1e-15
            ):
                raise ValueError(f"Conflicting duplicate metric for {lookup_key}")
        metric_lookup[lookup_key] = component_metric
    return metric_lookup


def ordered_family_list(component_metric_list: list[ComponentMetric], surface: str) -> list[str]:
    """Return stable family labels for one surface."""

    present_family_set = {
        component_metric.family_name
        for component_metric in component_metric_list
        if component_metric.surface == surface
    }
    ordered_list = [family_name for family_name in FAMILY_ORDER_LIST if family_name in present_family_set]
    ordered_list.extend(sorted(present_family_set.difference(ordered_list)))
    return ordered_list


def ordered_harmonic_list(component_metric_list: list[ComponentMetric], surface: str, target_kind: str) -> list[int]:
    """Return stable harmonic order for one surface and target kind."""

    return sorted(
        {
            component_metric.harmonic_order
            for component_metric in component_metric_list
            if component_metric.surface == surface and component_metric.target_kind == target_kind
        }
    )


def format_metric_value(metric_value: float) -> str:
    """Format metric values compactly for wide Markdown tables."""

    return f"{metric_value:.6g}"


def chunk_family_list(family_list: list[str]) -> list[list[str]]:
    """Split family columns into PDF-safe table panels."""

    return [
        family_list[family_index : family_index + MAX_FAMILY_COLUMNS_PER_TABLE]
        for family_index in range(0, len(family_list), MAX_FAMILY_COLUMNS_PER_TABLE)
    ]


def render_metric_table(
    component_metric_list: list[ComponentMetric],
    surface: str,
    target_kind: str,
    metric_name: str,
) -> list[str]:
    """Render one paper-equivalent metric table."""

    metric_lookup = build_metric_lookup(component_metric_list)
    family_list = ordered_family_list(component_metric_list, surface)
    harmonic_list = ordered_harmonic_list(component_metric_list, surface, target_kind)
    table_number = TABLE_NUMBER_MAP[(target_kind, metric_name)]
    title = TARGET_KIND_TITLE_DICTIONARY[target_kind]
    metric_title = METRIC_TITLE_DICTIONARY[metric_name]

    line_list = [
        f"#### {table_number} Equivalent - {title} {metric_title}",
        "",
    ]
    family_panel_list = chunk_family_list(family_list)
    for panel_index, family_panel in enumerate(family_panel_list, start=1):
        if len(family_panel_list) > 1:
            line_list.extend(
                [
                    f"Panel {panel_index} of {len(family_panel_list)}: "
                    f"`{', '.join(family_panel)}`.",
                    "",
                ]
            )
        line_list.extend(
            [
                f"| Target | Harmonic | {' | '.join(family_panel)} |",
                f"| --- | ---: | {' | '.join(['---:'] * len(family_panel))} |",
            ]
        )
        for harmonic_order in harmonic_list:
            target_label = "ampl" if target_kind == "amplitude" else "phase"
            row_metric_dictionary: dict[str, float] = {}
            for family_name in family_list:
                component_metric = metric_lookup.get((surface, target_kind, harmonic_order, family_name))
                if component_metric is None:
                    continue
                row_metric_dictionary[family_name] = getattr(component_metric, metric_name)
            best_value = min(row_metric_dictionary.values()) if row_metric_dictionary else None
            value_list = []
            for family_name in family_panel:
                metric_value = row_metric_dictionary.get(family_name)
                if metric_value is None:
                    value_list.append("-")
                    continue
                formatted_value = format_metric_value(metric_value)
                if best_value is not None and abs(metric_value - best_value) <= max(1e-15, abs(best_value) * 1e-12):
                    formatted_value = f"**{formatted_value}**"
                value_list.append(formatted_value)
            line_list.append(
                f"| {target_label}_{harmonic_order} | {harmonic_order} | {' | '.join(value_list)} |"
            )
        line_list.append("")
    return line_list


def render_selection_ledger(component_metric_list: list[ComponentMetric], surface: str) -> list[str]:
    """Render the MAE-first component selection ledger for one surface."""

    metric_lookup = build_metric_lookup(component_metric_list)
    family_list = ordered_family_list(component_metric_list, surface)
    selection_rows: list[tuple[str, int, str, float, str, float, str]] = []

    for target_kind in ["amplitude", "phase"]:
        for harmonic_order in ordered_harmonic_list(component_metric_list, surface, target_kind):
            mae_candidate_list: list[tuple[float, str]] = []
            rmse_candidate_list: list[tuple[float, str]] = []
            for family_name in family_list:
                component_metric = metric_lookup.get((surface, target_kind, harmonic_order, family_name))
                if component_metric is None:
                    continue
                mae_candidate_list.append((component_metric.mae, family_name))
                rmse_candidate_list.append((component_metric.rmse, family_name))
            if not mae_candidate_list or not rmse_candidate_list:
                continue
            best_mae, best_mae_family = min(mae_candidate_list)
            best_rmse, best_rmse_family = min(rmse_candidate_list)
            composite_candidate = best_mae_family
            if best_mae_family != best_rmse_family:
                composite_candidate = f"{best_mae_family} (RMSE check: {best_rmse_family})"
            selection_rows.append(
                (
                    target_kind,
                    harmonic_order,
                    best_mae_family,
                    best_mae,
                    best_rmse_family,
                    best_rmse,
                    composite_candidate,
                )
            )

    line_list = [
        "#### Best-Cell Selection Ledger",
        "",
        "| Target | Harmonic | MAE fam | MAE | RMSE fam | RMSE | Candidate |",
        "| --- | ---: | --- | ---: | --- | ---: | --- |",
    ]
    for (
        target_kind,
        harmonic_order,
        best_mae_family,
        best_mae,
        best_rmse_family,
        best_rmse,
        composite_candidate,
    ) in selection_rows:
        target_label = "ampl" if target_kind == "amplitude" else "phase"
        line_list.append(
            "| "
            f"{target_label}_{harmonic_order} | "
            f"{harmonic_order} | "
            f"**{best_mae_family}** | "
            f"**{format_metric_value(best_mae)}** | "
            f"{best_rmse_family} | "
            f"{format_metric_value(best_rmse)} | "
            f"{composite_candidate} |"
        )
    line_list.append("")
    return line_list


def render_dataset_section(specification: DatasetSpecification) -> list[str]:
    """Render one dataset/input-mode report section."""

    component_metric_list = collect_dataset_metrics(specification)
    if not component_metric_list:
        raise ValueError(f"No component metrics found for {specification.display_name}")

    present_surface_list = [
        surface
        for surface in SURFACE_ORDER_LIST
        if any(component_metric.surface == surface for component_metric in component_metric_list)
    ]
    line_list = [
        f"## {specification.display_name}",
        "",
        f"- Dataset: `{specification.dataset_id}`",
        f"- Input mode: `{specification.input_mode}`",
        f"- Metric rows loaded: `{len(component_metric_list)}`",
        f"- Source mode: `{specification.source_kind}`",
        "",
    ]

    if "global" not in present_surface_list:
        line_list.extend(
            [
                "No `global` surface archive was found for this dataset/input mode; only",
                "`forward` and `backward` paper-table equivalents are reported.",
                "",
            ]
        )

    for surface in present_surface_list:
        line_list.extend(
            [
                f"### {SURFACE_TITLE_DICTIONARY[surface]} Surface",
                "",
                f"Family columns: `{', '.join(ordered_family_list(component_metric_list, surface))}`.",
                "",
            ]
        )
        for target_kind, metric_name in [
            ("amplitude", "mae"),
            ("amplitude", "rmse"),
            ("phase", "mae"),
            ("phase", "rmse"),
        ]:
            line_list.extend(render_metric_table(component_metric_list, surface, target_kind, metric_name))
        line_list.extend(render_selection_ledger(component_metric_list, surface))
    return line_list


def build_report() -> str:
    """Build the complete Markdown report."""

    line_list = [
        "# RCIM Track1 Retrained Paper Tables Report",
        "",
        "This report reconstructs the paper Table 2-5 equivalents for the current",
        "`rcim_track1` model-bank archives across the simplified setpoint archive,",
        "the polished setpoint retraining campaign, and the polished actual-value",
        "retraining campaign.",
        "",
        "Best cells are highlighted per target row and metric. The selection ledger",
        "uses MAE as the primary composite-model candidate rule and reports the RMSE",
        "winner as a secondary consistency check.",
        "",
        "## Table Mapping",
        "",
        "| Paper table | Report equivalent |",
        "| --- | --- |",
        "| Table 2 | Amplitude MAE by harmonic and family |",
        "| Table 3 | Amplitude RMSE by harmonic and family |",
        "| Table 4 | Phase MAE by harmonic and family |",
        "| Table 5 | Phase RMSE by harmonic and family |",
        "",
        "## Sources",
        "",
        "| Dataset/input mode | Source evidence |",
        "| --- | --- |",
    ]
    for specification in DATASET_SPECIFICATION_LIST:
        source_path = specification.promotion_inventory_path or specification.archive_root
        line_list.append(
            f"| {specification.display_name} | `{source_path.relative_to(PROJECT_PATH).as_posix()}` |"
        )
    line_list.append("")

    for specification in DATASET_SPECIFICATION_LIST:
        line_list.extend(render_dataset_section(specification))
    return "\n".join(line_list).rstrip() + "\n"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-path",
        type=Path,
        default=REPORT_DIRECTORY / REPORT_FILENAME,
        help="Markdown report path.",
    )
    return parser.parse_args()


def main() -> None:
    """Run report generation."""

    argument_namespace = parse_arguments()
    output_path = argument_namespace.output_path
    if not output_path.is_absolute():
        output_path = PROJECT_PATH / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_report(), encoding="utf-8")
    print(f"Wrote {output_path.relative_to(PROJECT_PATH)}")


if __name__ == "__main__":
    main()
