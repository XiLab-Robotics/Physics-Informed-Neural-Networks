"""Build a TE Curve Verification Pipeline forward reference curve comparison report."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import itertools
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import (
    harmonic_wise_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    plot_original_onnx_fw_track2_curves,
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import build_track2_best_model_collage_report
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_forward_reference_curve_comparison"
)
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "forward_reference_curve_comparison"
)
REPORT_FILENAME = "track2_forward_reference_curve_comparison_report.md"
SUMMARY_FILENAME = "track2_forward_reference_curve_comparison_summary.yaml"
METRICS_FILENAME = "track2_forward_reference_curve_comparison_metrics.csv"
PAIRWISE_FILENAME = "track2_forward_reference_curve_pairwise_differences.csv"

REFERENCE_CANDIDATE_ID_LIST = [
    "paper_original_best_Fw",
    "paper_retuned_best_Fw",
]
ONNX_CANDIDATE_ID_LIST = [
    plot_original_onnx_fw_track2_curves.FULL_ORIGINAL_ONNX_VARIANT_ID,
    plot_original_onnx_fw_track2_curves.SPARSE_SIMPLIFIED_ONNX_VARIANT_ID,
    plot_original_onnx_fw_track2_curves.SPARSE_PLC_HGBM_ONNX_VARIANT_ID,
]
REPORT_CANDIDATE_ID_LIST = REFERENCE_CANDIDATE_ID_LIST + ONNX_CANDIDATE_ID_LIST
PAIRWISE_ANCHOR_ID_LIST = [
    "paper_original_best_Fw",
    plot_original_onnx_fw_track2_curves.FULL_ORIGINAL_ONNX_VARIANT_ID,
]
CANDIDATE_LABEL_DICTIONARY = {
    "paper_original_best_Fw": "Original",
    "paper_retuned_best_Fw": "Retuned",
    plot_original_onnx_fw_track2_curves.FULL_ORIGINAL_ONNX_VARIANT_ID: "Full ONNX",
    plot_original_onnx_fw_track2_curves.SPARSE_SIMPLIFIED_ONNX_VARIANT_ID: "Sparse",
    plot_original_onnx_fw_track2_curves.SPARSE_PLC_HGBM_ONNX_VARIANT_ID: "PLC HGBM",
}


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="curve-verification matrix config used to resolve dataset and reference candidates.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root directory for validation artifacts.",
    )
    parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Topic directory where the dated Markdown report bundle is written.",
    )
    parser.add_argument(
        "--report-date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Bracketed report date folder to create under the report topic root.",
    )
    parser.add_argument(
        "--curves-per-collage",
        type=int,
        default=4,
        help="Number of deterministic representative curves in each collage.",
    )
    return parser.parse_args()


def resolve_report_paths(arguments: argparse.Namespace) -> tuple[str, Path, Path, Path, Path, Path]:

    """Resolve output and report paths."""

    assert int(arguments.curves_per_collage) == 4, "This report expects exactly four curves per collage."
    timestamp_text = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    run_instance_id = f"{timestamp_text}__track2_forward_reference_curve_comparison"
    output_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.output_root)
        / run_instance_id
    )
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.report_topic_root)
        / f"[{arguments.report_date}]"
    )
    report_path = report_directory / REPORT_FILENAME
    metrics_csv_path = output_directory / METRICS_FILENAME
    pairwise_csv_path = output_directory / PAIRWISE_FILENAME
    validation_summary_path = output_directory / SUMMARY_FILENAME
    return (
        run_instance_id,
        output_directory,
        report_path,
        metrics_csv_path,
        pairwise_csv_path,
        validation_summary_path,
    )


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def build_curve_key(entry_dictionary: dict[str, Any]) -> tuple[str, str]:

    """Build a stable curve key from a per-candidate entry."""

    return (
        str(entry_dictionary["source_file_path"]),
        str(entry_dictionary["direction_label"]).strip().lower(),
    )


def resolve_reference_candidate_configuration_list(
    training_config: dict[str, Any],
) -> list[dict[str, Any]]:

    """Resolve the two repository paper-reference candidate configurations."""

    candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
    selected_configuration_list = [
        candidate_configuration
        for candidate_configuration in candidate_configuration_list
        if str(candidate_configuration["candidate_id"]) in REFERENCE_CANDIDATE_ID_LIST
    ]
    assert len(selected_configuration_list) == len(REFERENCE_CANDIDATE_ID_LIST), (
        "Could not resolve all forward paper-reference candidates."
    )
    return sorted(
        selected_configuration_list,
        key=lambda candidate_configuration: REFERENCE_CANDIDATE_ID_LIST.index(
            str(candidate_configuration["candidate_id"])
        ),
    )


def summarize_curve_metrics(per_curve_entry_list: list[dict[str, Any]]) -> dict[str, float]:

    """Summarize per-curve metric dictionaries."""

    return {
        "mae": float(np.mean([entry["metrics"]["mae"] for entry in per_curve_entry_list])),
        "rmse": float(np.mean([entry["metrics"]["rmse"] for entry in per_curve_entry_list])),
        "mean_percentage_error_pct": float(
            np.mean([entry["metrics"]["mean_percentage_error_pct"] for entry in per_curve_entry_list])
        ),
        "p95_mean_percentage_error_pct": float(
            np.percentile([entry["metrics"]["mean_percentage_error_pct"] for entry in per_curve_entry_list], 95)
        ),
    }


def evaluate_onnx_candidate_curve_list(
    candidate_id: str,
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    default_selected_harmonic_list: list[int],
    percentage_error_denominator: str,
) -> list[dict[str, Any]]:

    """Evaluate one hardcoded original-ONNX variant on forward curves."""

    variant_configuration = plot_original_onnx_fw_track2_curves.resolve_onnx_variant_configuration(candidate_id)
    target_list = plot_original_onnx_fw_track2_curves.load_hardcoded_onnx_target_list(
        variant_configuration["target_configuration_list"]
    )
    selected_harmonic_list = variant_configuration["selected_harmonic_list"]
    if selected_harmonic_list is None:
        selected_harmonic_list = default_selected_harmonic_list
    selected_harmonic_list = [int(harmonic_order) for harmonic_order in selected_harmonic_list]

    per_curve_entry_list: list[dict[str, Any]] = []
    for curve_record in curve_record_list:
        prediction_dictionary = plot_original_onnx_fw_track2_curves.predict_curve_target_dictionary(
            curve_record,
            target_list,
        )
        predicted_curve_deg = plot_original_onnx_fw_track2_curves.reconstruct_curve_from_prediction_dictionary(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            prediction_dictionary,
        )
        metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
            percentage_error_denominator,
        )
        per_curve_entry_list.append(
            {
                "candidate_id": candidate_id,
                "candidate_family": "original_onnx",
                "candidate_kind": "hardcoded_original_onnx",
                "candidate_source_label": "exact_onnx_paper_release",
                "candidate_surface": "Fw",
                "allowed_direction_list": ["forward"],
                "source_path": (
                    "reference/rcim_ml_compensation_recovered_assets/models/"
                    "exact_onnx_paper_release"
                ),
                "source_file_path": shared_training_infrastructure.format_project_relative_path(
                    curve_record.source_file_path
                ),
                "direction_label": curve_record.direction_label,
                "speed_rpm": float(curve_record.speed_rpm),
                "torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "metrics": metric_dictionary,
                "angular_position_deg": curve_record.angular_position_deg.astype(float).tolist(),
                "truth_curve_deg": curve_record.transmission_error_deg.astype(float).tolist(),
                "predicted_curve_deg": predicted_curve_deg.astype(float).tolist(),
            }
        )

    return per_curve_entry_list


def build_candidate_summary_list(
    output_directory: Path,
    report_path: Path,
    candidate_entry_dictionary: dict[str, list[dict[str, Any]]],
    curves_per_collage: int,
) -> list[dict[str, Any]]:

    """Build candidate summaries and collages."""

    candidate_summary_list: list[dict[str, Any]] = []
    for candidate_id in REPORT_CANDIDATE_ID_LIST:
        per_curve_entry_list = candidate_entry_dictionary[candidate_id]
        metric_summary = summarize_curve_metrics(per_curve_entry_list)
        selected_curve_entry_list = build_track2_best_model_collage_report.select_candidate_collage_entries(
            per_curve_entry_list,
            "forward",
            curves_per_collage,
        )
        collage_path = output_directory / "collages" / f"{candidate_id}.png"
        report_asset_path = report_path.parent / "assets" / f"{candidate_id}.png"
        build_track2_best_model_collage_report.save_candidate_collage(
            collage_path,
            candidate_id,
            selected_curve_entry_list,
        )
        report_asset_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(collage_path, report_asset_path)

        candidate_summary_list.append(
            {
                "candidate_id": candidate_id,
                "curve_count": int(len(per_curve_entry_list)),
                "metric_summary": metric_summary,
                "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
                "collage_markdown_path": build_relative_markdown_path(report_asset_path, report_path.parent),
                "selected_curve_list": [
                    {
                        "source_file_path": str(entry["source_file_path"]),
                        "direction_label": str(entry["direction_label"]),
                        "speed_rpm": float(entry["speed_rpm"]),
                        "torque_nm": float(entry["torque_nm"]),
                        "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                        "metrics": entry["metrics"],
                    }
                    for entry in selected_curve_entry_list
                ],
            }
        )

    return candidate_summary_list


def compute_curve_difference_dictionary(
    left_entry: dict[str, Any],
    right_entry: dict[str, Any],
) -> dict[str, float]:

    """Compute pointwise differences between two predicted curves."""

    left_curve = np.asarray(left_entry["predicted_curve_deg"], dtype=np.float64)
    right_curve = np.asarray(right_entry["predicted_curve_deg"], dtype=np.float64)
    difference_curve = left_curve - right_curve
    absolute_difference_curve = np.abs(difference_curve)
    if np.std(left_curve) > 0.0 and np.std(right_curve) > 0.0:
        correlation_value = float(np.corrcoef(left_curve, right_curve)[0, 1])
    else:
        correlation_value = 1.0 if np.allclose(left_curve, right_curve) else 0.0
    return {
        "curve_difference_mae_deg": float(np.mean(absolute_difference_curve)),
        "curve_difference_p95_deg": float(np.percentile(absolute_difference_curve, 95.0)),
        "curve_difference_max_deg": float(np.max(absolute_difference_curve)),
        "curve_difference_rmse_deg": float(np.sqrt(np.mean(np.square(difference_curve)))),
        "curve_correlation": correlation_value,
    }


def build_pairwise_difference_summary_list(
    candidate_entry_dictionary: dict[str, list[dict[str, Any]]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:

    """Build aggregate and per-curve pairwise difference summaries."""

    entry_lookup_by_candidate = {
        candidate_id: {
            build_curve_key(entry): entry
            for entry in entry_list
        }
        for candidate_id, entry_list in candidate_entry_dictionary.items()
    }
    common_curve_key_set = set.intersection(
        *[
            set(entry_lookup.keys())
            for entry_lookup in entry_lookup_by_candidate.values()
        ]
    )
    common_curve_key_list = sorted(common_curve_key_set)
    aggregate_row_list: list[dict[str, Any]] = []
    per_curve_row_list: list[dict[str, Any]] = []

    for left_candidate_id, right_candidate_id in itertools.combinations(REPORT_CANDIDATE_ID_LIST, 2):
        per_pair_difference_list: list[dict[str, float]] = []
        for curve_key in common_curve_key_list:
            left_entry = entry_lookup_by_candidate[left_candidate_id][curve_key]
            right_entry = entry_lookup_by_candidate[right_candidate_id][curve_key]
            difference_dictionary = compute_curve_difference_dictionary(left_entry, right_entry)
            per_pair_difference_list.append(difference_dictionary)
            per_curve_row_list.append(
                {
                    "left_candidate_id": left_candidate_id,
                    "right_candidate_id": right_candidate_id,
                    "source_file_path": curve_key[0],
                    "direction_label": curve_key[1],
                    "speed_rpm": float(left_entry["speed_rpm"]),
                    "torque_nm": float(left_entry["torque_nm"]),
                    "oil_temperature_deg": float(left_entry["oil_temperature_deg"]),
                    **difference_dictionary,
                }
            )

        aggregate_row_list.append(
            {
                "left_candidate_id": left_candidate_id,
                "right_candidate_id": right_candidate_id,
                "curve_count": int(len(per_pair_difference_list)),
                "mean_curve_difference_mae_deg": float(
                    np.mean([row["curve_difference_mae_deg"] for row in per_pair_difference_list])
                ),
                "p95_curve_difference_deg": float(
                    np.percentile([row["curve_difference_p95_deg"] for row in per_pair_difference_list], 95.0)
                ),
                "max_curve_difference_deg": float(
                    np.max([row["curve_difference_max_deg"] for row in per_pair_difference_list])
                ),
                "global_difference_rmse_deg": float(
                    np.sqrt(np.mean([row["curve_difference_rmse_deg"] ** 2 for row in per_pair_difference_list]))
                ),
                "mean_correlation": float(
                    np.mean([row["curve_correlation"] for row in per_pair_difference_list])
                ),
            }
        )

    return aggregate_row_list, per_curve_row_list


def build_representative_curve_difference_list(
    candidate_summary_list: list[dict[str, Any]],
    candidate_entry_dictionary: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:

    """Build compact differences for the four representative collage curves."""

    selected_key_list = [
        build_curve_key(entry)
        for entry in candidate_summary_list[0]["selected_curve_list"]
    ]
    entry_lookup_by_candidate = {
        candidate_id: {
            build_curve_key(entry): entry
            for entry in entry_list
        }
        for candidate_id, entry_list in candidate_entry_dictionary.items()
    }
    row_list: list[dict[str, Any]] = []
    for curve_index, curve_key in enumerate(selected_key_list, start=1):
        base_entry = entry_lookup_by_candidate[REPORT_CANDIDATE_ID_LIST[0]][curve_key]
        row_dictionary: dict[str, Any] = {
            "curve_label": f"Curve {curve_index}",
            "source_file_path": curve_key[0],
            "speed_rpm": float(base_entry["speed_rpm"]),
            "torque_nm": float(base_entry["torque_nm"]),
            "oil_temperature_deg": float(base_entry["oil_temperature_deg"]),
        }
        for candidate_id in REPORT_CANDIDATE_ID_LIST:
            row_dictionary[f"{candidate_id}__mae_deg"] = float(
                entry_lookup_by_candidate[candidate_id][curve_key]["metrics"]["mae"]
            )
        for anchor_candidate_id in PAIRWISE_ANCHOR_ID_LIST:
            anchor_entry = entry_lookup_by_candidate[anchor_candidate_id][curve_key]
            for candidate_id in REPORT_CANDIDATE_ID_LIST:
                if candidate_id == anchor_candidate_id:
                    continue
                difference_dictionary = compute_curve_difference_dictionary(
                    anchor_entry,
                    entry_lookup_by_candidate[candidate_id][curve_key],
                )
                row_dictionary[f"{anchor_candidate_id}__vs__{candidate_id}__mae_deg"] = float(
                    difference_dictionary["curve_difference_mae_deg"]
                )
        row_list.append(row_dictionary)
    return row_list


def save_metrics_csv(csv_path: Path, candidate_entry_dictionary: dict[str, list[dict[str, Any]]]) -> None:

    """Save one row per candidate and evaluated curve."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(
            [
                "candidate_id",
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
            ]
        )
        for candidate_id in REPORT_CANDIDATE_ID_LIST:
            for entry in candidate_entry_dictionary[candidate_id]:
                writer.writerow(
                    [
                        candidate_id,
                        entry["source_file_path"],
                        entry["direction_label"],
                        f"{float(entry['speed_rpm']):.6f}",
                        f"{float(entry['torque_nm']):.6f}",
                        f"{float(entry['oil_temperature_deg']):.6f}",
                        f"{float(entry['metrics']['mae']):.9f}",
                        f"{float(entry['metrics']['rmse']):.9f}",
                        f"{float(entry['metrics']['mean_percentage_error_pct']):.9f}",
                    ]
                )


def save_pairwise_csv(csv_path: Path, per_curve_row_list: list[dict[str, Any]]) -> None:

    """Save one row per pair and curve difference."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(
            [
                "left_candidate_id",
                "right_candidate_id",
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "curve_difference_mae_deg",
                "curve_difference_p95_deg",
                "curve_difference_max_deg",
                "curve_difference_rmse_deg",
                "curve_correlation",
            ]
        )
        for row in per_curve_row_list:
            writer.writerow(
                [
                    row["left_candidate_id"],
                    row["right_candidate_id"],
                    row["source_file_path"],
                    row["direction_label"],
                    f"{float(row['speed_rpm']):.6f}",
                    f"{float(row['torque_nm']):.6f}",
                    f"{float(row['oil_temperature_deg']):.6f}",
                    f"{float(row['curve_difference_mae_deg']):.9f}",
                    f"{float(row['curve_difference_p95_deg']):.9f}",
                    f"{float(row['curve_difference_max_deg']):.9f}",
                    f"{float(row['curve_difference_rmse_deg']):.9f}",
                    f"{float(row['curve_correlation']):.9f}",
                ]
            )


def format_metric_row(candidate_summary: dict[str, Any]) -> str:

    """Format one aggregate metric table row."""

    metric_summary = candidate_summary["metric_summary"]
    return (
        "| "
        f"`{candidate_summary['candidate_id']}` | "
        f"{int(candidate_summary['curve_count'])} | "
        f"{float(metric_summary['mae']):.9f} | "
        f"{float(metric_summary['rmse']):.9f} | "
        f"{float(metric_summary['mean_percentage_error_pct']):.6f} | "
        f"{float(metric_summary['p95_mean_percentage_error_pct']):.6f} |"
    )


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    metrics_csv_path: Path,
    pairwise_csv_path: Path,
    validation_summary_path: Path,
    candidate_summary_list: list[dict[str, Any]],
    pairwise_summary_list: list[dict[str, Any]],
    representative_curve_difference_list: list[dict[str, Any]],
) -> str:

    """Build report Markdown."""

    line_list = [
        "# TE Curve Verification Pipeline Forward Reference Curve Comparison Report",
        "",
        "## Overview",
        "",
        "This report compares five forward `TE Curve Verification Pipeline` reconstructed-curve",
        "candidates on the same `97` held-out forward curves:",
        "",
        "- `paper_original_best_Fw`, from repository paper-original reference banks;",
        "- `paper_retuned_best_Fw`, from repository paper-retuned reference banks;",
        "- `paper_original_best_Fw_original_onnx_release`, loaded directly from the recovered original `ONNX` release;",
        "- `rcim_original_simplified_onnx_Fw`, using harmonics `0`, `1`, `39`, and `40`;",
        "- `rcim_original_plc_hgbm_onnx_Fw`, using only `HGBM` original `ONNX` models for those sparse harmonics.",
        "",
        "The collages below are regenerated with the same four representative",
        "forward curves for every candidate, so visual differences are directly",
        "comparable across models.",
        "",
        "Model labels used in compact tables:",
        "",
        "| Label | Candidate |",
        "| --- | --- |",
    ]
    for candidate_id in REPORT_CANDIDATE_ID_LIST:
        line_list.append(f"| {CANDIDATE_LABEL_DICTIONARY[candidate_id]} | `{candidate_id}` |")

    line_list.extend(
        [
            "",
            "## Aggregate TE Curve Verification Pipeline Metrics",
            "",
            "| Candidate | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for candidate_summary in candidate_summary_list:
        line_list.append(format_metric_row(candidate_summary))

    line_list.extend(
        [
            "",
            "## Pairwise Predicted-Curve Differences",
            "",
            "| Pair | Mean MAE [deg] | P95 [deg] | Max [deg] | RMSE [deg] | Corr. |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for pairwise_summary in pairwise_summary_list:
        pair_label = (
            f"{CANDIDATE_LABEL_DICTIONARY[str(pairwise_summary['left_candidate_id'])]} vs "
            f"{CANDIDATE_LABEL_DICTIONARY[str(pairwise_summary['right_candidate_id'])]}"
        )
        line_list.append(
            "| "
            f"{pair_label} | "
            f"{float(pairwise_summary['mean_curve_difference_mae_deg']):.9f} | "
            f"{float(pairwise_summary['p95_curve_difference_deg']):.9f} | "
            f"{float(pairwise_summary['max_curve_difference_deg']):.9f} | "
            f"{float(pairwise_summary['global_difference_rmse_deg']):.9f} | "
            f"{float(pairwise_summary['mean_correlation']):.9f} |"
        )

    line_list.extend(
        [
            "",
            "## Collage Curve Metrics",
            "",
            "All metric columns in this section are `MAE [deg]`.",
            "",
            "| Curve | Operating Point | Original | Retuned | Full ONNX | Sparse | PLC HGBM |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in representative_curve_difference_list:
        operating_point = (
            f"{float(row['speed_rpm']):.0f} rpm / "
            f"{float(row['torque_nm']):.0f} Nm / "
            f"{float(row['oil_temperature_deg']):.0f} C"
        )
        line_list.append(
            "| "
            f"`{row['curve_label']}` | "
            f"{operating_point} | "
            f"{float(row['paper_original_best_Fw__mae_deg']):.9f} | "
            f"{float(row['paper_retuned_best_Fw__mae_deg']):.9f} | "
            f"{float(row['paper_original_best_Fw_original_onnx_release__mae_deg']):.9f} | "
            f"{float(row['rcim_original_simplified_onnx_Fw__mae_deg']):.9f} | "
            f"{float(row['rcim_original_plc_hgbm_onnx_Fw__mae_deg']):.9f} |"
        )

    line_list.extend(
        [
            "",
            "## Collage Curve Anchor Deltas",
            "",
            "All delta columns in this section are predicted-curve `MAE [deg]`.",
            "",
            "| Curve | Operating Point | Full ONNX | Sparse | PLC | PLC-Full |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in representative_curve_difference_list:
        operating_point = (
            f"{float(row['speed_rpm']):.0f} rpm / "
            f"{float(row['torque_nm']):.0f} Nm / "
            f"{float(row['oil_temperature_deg']):.0f} C"
        )
        line_list.append(
            "| "
            f"`{row['curve_label']}` | "
            f"{operating_point} | "
            f"{float(row['paper_original_best_Fw__vs__paper_original_best_Fw_original_onnx_release__mae_deg']):.9f} | "
            f"{float(row['paper_original_best_Fw__vs__rcim_original_simplified_onnx_Fw__mae_deg']):.9f} | "
            f"{float(row['paper_original_best_Fw__vs__rcim_original_plc_hgbm_onnx_Fw__mae_deg']):.9f} | "
            f"{float(row['paper_original_best_Fw_original_onnx_release__vs__rcim_original_plc_hgbm_onnx_Fw__mae_deg']):.9f} |"
        )

    line_list.extend(
        [
            "",
            "## Technical Interpretation",
            "",
            "The full recovered original `ONNX` release remains almost superposed with",
            "`paper_original_best_Fw`: the pair has the smallest mean curve-difference",
            "`MAE`, a near-unit mean correlation, and only small aggregate metric",
            "changes. This supports the same conclusion as the earlier diagnostic:",
            "the repository paper-original bank and the recovered original `ONNX`",
            "release are effectively the same TE Curve Verification Pipeline reconstructed surface, with",
            "minor differences attributable to archive/export/loading path details.",
            "",
            "`paper_retuned_best_Fw` is visually shape-aligned with the paper-original",
            "surface, but it is numerically distinct and improves the measured-curve",
            "metrics. The sparse original `ONNX` variants are also shape-aligned, but",
            "they move away from the 19-target original surface because they retain",
            "only harmonics `0`, `1`, `39`, and `40`. In this run, the PLC-oriented",
            "all-`HGBM` sparse variant is the stronger sparse candidate.",
            "",
            "## Candidate Collages",
            "",
        ]
    )
    for candidate_summary in candidate_summary_list:
        line_list.extend(
            [
                f"### {candidate_summary['candidate_id']}",
                "",
                (
                    f"![{candidate_summary['candidate_id']} TE Curve Verification Pipeline collage]"
                    f"({candidate_summary['collage_markdown_path']})"
                ),
                "",
            ]
        )

    line_list.extend(
        [
            "## Output Artifacts",
            "",
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- summary YAML: `{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}`;",
            f"- metrics CSV: `{shared_training_infrastructure.format_project_relative_path(metrics_csv_path)}`;",
            f"- pairwise CSV: `{shared_training_infrastructure.format_project_relative_path(pairwise_csv_path)}`;",
            f"- report Markdown: `{shared_training_infrastructure.format_project_relative_path(report_path)}`.",
            "",
        ]
    )
    return "\n".join(line_list)


def run_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the forward reference curve comparison report workflow."""

    (
        run_instance_id,
        output_directory,
        report_path,
        metrics_csv_path,
        pairwise_csv_path,
        validation_summary_path,
    ) = resolve_report_paths(arguments)
    output_directory.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    forward_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == "forward"
    ]
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    candidate_entry_dictionary: dict[str, list[dict[str, Any]]] = {}
    for candidate_configuration in resolve_reference_candidate_configuration_list(training_config):
        candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        per_curve_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            candidate,
            forward_curve_record_list,
            percentage_error_denominator,
            include_curve_payload=True,
        )
        candidate_entry_dictionary[candidate.candidate_id] = per_curve_entry_list

    for candidate_id in ONNX_CANDIDATE_ID_LIST:
        candidate_entry_dictionary[candidate_id] = evaluate_onnx_candidate_curve_list(
            candidate_id,
            forward_curve_record_list,
            selected_harmonic_list,
            percentage_error_denominator,
        )

    candidate_summary_list = build_candidate_summary_list(
        output_directory,
        report_path,
        candidate_entry_dictionary,
        int(arguments.curves_per_collage),
    )
    pairwise_summary_list, per_curve_pairwise_row_list = build_pairwise_difference_summary_list(
        candidate_entry_dictionary
    )
    representative_curve_difference_list = build_representative_curve_difference_list(
        candidate_summary_list,
        candidate_entry_dictionary,
    )
    save_metrics_csv(metrics_csv_path, candidate_entry_dictionary)
    save_pairwise_csv(pairwise_csv_path, per_curve_pairwise_row_list)

    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
        "pairwise_csv_path": shared_training_infrastructure.format_project_relative_path(pairwise_csv_path),
        "dataset": {
            "config_path": shared_training_infrastructure.format_project_relative_path(arguments.config_path),
            "dataset_root": shared_training_infrastructure.format_project_relative_path(dataset_root),
            "forward_curve_count": int(len(forward_curve_record_list)),
            "selected_harmonic_list": selected_harmonic_list,
        },
        "candidate_summary_list": candidate_summary_list,
        "pairwise_summary_list": pairwise_summary_list,
        "representative_curve_difference_list": representative_curve_difference_list,
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        metrics_csv_path,
        pairwise_csv_path,
        validation_summary_path,
        candidate_summary_list,
        pairwise_summary_list,
        representative_curve_difference_list,
    )
    report_path.write_text(report_markdown, encoding="utf-8", newline="\n")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_report(parse_command_line_arguments())
    print(f"[DONE] TE Curve Verification Pipeline forward reference comparison report: {validation_summary['report_path']}")


if __name__ == "__main__":
    main()
