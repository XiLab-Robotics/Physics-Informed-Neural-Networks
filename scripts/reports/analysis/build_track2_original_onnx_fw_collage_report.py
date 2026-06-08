"""Build a simple Track 2 collage report for original ONNX paper-best Fw."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
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
)
from scripts.reports.analysis import build_track2_best_model_collage_report
from scripts.training import shared_training_infrastructure

DEFAULT_OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_original_onnx_fw_collage_report"
)
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "original_onnx_fw_collage_report"
)
REPORT_FILENAME = "track2_original_onnx_fw_collage_report.md"
SUMMARY_FILENAME = "track2_original_onnx_fw_collage_summary.yaml"
METRICS_FILENAME = "track2_original_onnx_fw_collage_metrics.csv"
CANDIDATE_ID = "paper_original_best_Fw_original_onnx_release"
CANDIDATE_DISPLAY_NAME = "paper_original_best_Fw ONNX"


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config-path",
        type=Path,
        default=plot_original_onnx_fw_track2_curves.DEFAULT_TRACK2_CONFIG_PATH,
        help="Track 2 configuration used to resolve the held-out curve split.",
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
        help="Number of deterministic representative curves in the collage.",
    )
    return parser.parse_args()


def resolve_report_paths(arguments: argparse.Namespace) -> tuple[str, Path, Path, Path, Path]:

    """Resolve output, report, metric, and summary paths."""

    assert int(arguments.curves_per_collage) == 4, "This report expects exactly four curves per collage."
    timestamp_text = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    run_instance_id = f"{timestamp_text}__track2_original_onnx_fw_collage_report"
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
    validation_summary_path = output_directory / SUMMARY_FILENAME
    return run_instance_id, output_directory, report_path, metrics_csv_path, validation_summary_path


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def evaluate_forward_curve_list(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    selected_harmonic_list: list[int],
    percentage_error_denominator: str,
    target_list: list[plot_original_onnx_fw_track2_curves.HardcodedOnnxTarget],
) -> list[dict[str, Any]]:

    """Evaluate the original ONNX composite target bank on all forward curves."""

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
                "candidate_id": CANDIDATE_ID,
                "direction_label": curve_record.direction_label,
                "source_file_path": shared_training_infrastructure.format_project_relative_path(
                    curve_record.source_file_path
                ),
                "speed_rpm": float(curve_record.speed_rpm),
                "torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "angular_position_deg": curve_record.angular_position_deg,
                "truth_curve_deg": curve_record.transmission_error_deg,
                "predicted_curve_deg": predicted_curve_deg,
                "metrics": metric_dictionary,
            }
        )

    return per_curve_entry_list


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


def save_metrics_csv(csv_path: Path, per_curve_entry_list: list[dict[str, Any]]) -> None:

    """Save one row per evaluated forward curve."""

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
        for entry in per_curve_entry_list:
            writer.writerow(
                [
                    entry["candidate_id"],
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


def build_target_table_rows(
    target_list: list[plot_original_onnx_fw_track2_curves.HardcodedOnnxTarget],
) -> list[str]:

    """Build Markdown rows for the 19 loaded target models."""

    row_list = [
        "| Target | Harmonic | Family | Original ONNX Files |",
        "| --- | ---: | --- | --- |",
    ]
    for target in target_list:
        target_prefix = "A" if target.target_kind == "amplitude" else "P"
        row_list.append(
            "| "
            f"`{target.target_kind}` | "
            f"`{target_prefix}{target.harmonic_order}` | "
            f"`{target.family_name}` | "
            f"`{target.model_path.name}` |"
        )
    return row_list


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    metrics_csv_path: Path,
    validation_summary_path: Path,
    collage_markdown_path: str,
    metric_summary: dict[str, float],
    target_list: list[plot_original_onnx_fw_track2_curves.HardcodedOnnxTarget],
    selected_curve_entry_list: list[dict[str, Any]],
    curve_count: int,
) -> str:

    """Build the report Markdown body."""

    line_list = [
        "# Track 2 Original ONNX Forward Collage Report",
        "",
        "## Overview",
        "",
        "This report evaluates only the recovered paper-original forward `ONNX`",
        "model bank for `paper_original_best_Fw`. The curve prediction is rebuilt",
        "directly from the `19` original target models under",
        "`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`.",
        "",
        "## Loaded ONNX Targets",
        "",
        "The table lists the original release filenames loaded for the `19`",
        "paper-best forward targets. Full original `ONNX` paths are kept in",
        "the validation summary YAML.",
        "",
        *build_target_table_rows(target_list),
        "",
        "## Track 2 Forward Metrics",
        "",
        "| Candidate | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| `{CANDIDATE_DISPLAY_NAME}` | {curve_count} | "
            f"{metric_summary['mae']:.6f} | "
            f"{metric_summary['rmse']:.6f} | "
            f"{metric_summary['mean_percentage_error_pct']:.3f} | "
            f"{metric_summary['p95_mean_percentage_error_pct']:.3f} |"
        ),
        "",
        "## Collage",
        "",
        "The collage shows four deterministic held-out forward `Track 2` curves",
        "spread across the sorted forward evaluation set.",
        "",
        f"![{CANDIDATE_ID} Track 2 collage]({collage_markdown_path})",
        "",
        "## Collaged Curves",
        "",
        "| Curve | Speed [rpm] | Torque [Nm] | Oil [C] | MAE [deg] | Mean Error [%] |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for curve_index, entry in enumerate(selected_curve_entry_list, start=1):
        line_list.append(
            f"| `Curve {curve_index}` | "
            f"{float(entry['speed_rpm']):.0f} | "
            f"{float(entry['torque_nm']):.0f} | "
            f"{float(entry['oil_temperature_deg']):.0f} | "
            f"{float(entry['metrics']['mae']):.6f} | "
            f"{float(entry['metrics']['mean_percentage_error_pct']):.3f} |"
        )

    line_list.extend(
        [
            "",
            "## Output Artifacts",
            "",
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- summary YAML: `{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}`;",
            f"- metrics CSV: `{shared_training_infrastructure.format_project_relative_path(metrics_csv_path)}`;",
            f"- report Markdown: `{shared_training_infrastructure.format_project_relative_path(report_path)}`.",
            "",
        ]
    )
    return "\n".join(line_list)


def run_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the report generation workflow."""

    run_instance_id, output_directory, report_path, metrics_csv_path, validation_summary_path = resolve_report_paths(
        arguments
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output_directory.mkdir(parents=True, exist_ok=True)

    target_list = plot_original_onnx_fw_track2_curves.load_hardcoded_onnx_target_list()
    curve_record_list, selected_harmonic_list, percentage_error_denominator = (
        plot_original_onnx_fw_track2_curves.build_forward_track2_curve_record_list(arguments.config_path)
    )
    per_curve_entry_list = evaluate_forward_curve_list(
        curve_record_list,
        selected_harmonic_list,
        percentage_error_denominator,
        target_list,
    )
    metric_summary = summarize_curve_metrics(per_curve_entry_list)
    selected_curve_entry_list = build_track2_best_model_collage_report.select_candidate_collage_entries(
        per_curve_entry_list,
        "forward",
        int(arguments.curves_per_collage),
    )

    collage_path = output_directory / "collages" / "paper_original_best_fw_original_onnx_release.png"
    report_asset_path = report_path.parent / "assets" / "paper_original_best_fw_original_onnx_release.png"
    build_track2_best_model_collage_report.save_candidate_collage(
        collage_path,
        CANDIDATE_ID,
        selected_curve_entry_list,
    )
    report_asset_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(collage_path, report_asset_path)
    collage_markdown_path = build_relative_markdown_path(report_asset_path, report_path.parent)

    save_metrics_csv(metrics_csv_path, per_curve_entry_list)
    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "candidate_id": CANDIDATE_ID,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
        "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
        "target_count": len(target_list),
        "curve_count": len(per_curve_entry_list),
        "selected_harmonic_list": selected_harmonic_list,
        "metric_summary": metric_summary,
        "target_list": [
            {
                "target_kind": target.target_kind,
                "harmonic_order": int(target.harmonic_order),
                "family_name": target.family_name,
                "model_path": shared_training_infrastructure.format_project_relative_path(target.model_path),
            }
            for target in target_list
        ],
        "selected_curve_list": [
            {
                "source_file_path": entry["source_file_path"],
                "speed_rpm": float(entry["speed_rpm"]),
                "torque_nm": float(entry["torque_nm"]),
                "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                "metrics": entry["metrics"],
            }
            for entry in selected_curve_entry_list
        ],
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        metrics_csv_path,
        validation_summary_path,
        collage_markdown_path,
        metric_summary,
        target_list,
        selected_curve_entry_list,
        len(per_curve_entry_list),
    )
    report_path.write_text(report_markdown, encoding="utf-8", newline="\n")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_report(parse_command_line_arguments())
    print(f"[DONE] Track 2 original ONNX Fw collage report: {validation_summary['report_path']}")


if __name__ == "__main__":
    main()
