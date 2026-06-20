"""Build TE curve-verification reports for sparse original ONNX RCIM variants."""

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
import yaml

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
    / "track2_sparse_original_onnx_variants"
)
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "sparse_original_onnx_variants"
)
DEFAULT_FULL_ORIGINAL_ONNX_SUMMARY_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_original_onnx_fw_collage_report"
    / "2026-06-08-12-57-36__track2_original_onnx_fw_collage_report"
    / "track2_original_onnx_fw_collage_summary.yaml"
)
DEFAULT_BEST_MODEL_COLLAGE_SUMMARY_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_best_model_collage_report"
    / "2026-05-28-13-37-39__track2_best_model_collage_report"
    / "track2_best_model_collage_summary.yaml"
)
REPORT_FILENAME = "track2_sparse_original_onnx_variants_report.md"
SUMMARY_FILENAME = "track2_sparse_original_onnx_variants_summary.yaml"
METRICS_FILENAME = "track2_sparse_original_onnx_variants_metrics.csv"
VARIANT_ID_LIST = [
    plot_original_onnx_fw_track2_curves.SPARSE_SIMPLIFIED_ONNX_VARIANT_ID,
    plot_original_onnx_fw_track2_curves.SPARSE_PLC_HGBM_ONNX_VARIANT_ID,
]


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config-path",
        type=Path,
        default=plot_original_onnx_fw_track2_curves.DEFAULT_TRACK2_CONFIG_PATH,
        help="TE Curve Verification Pipeline configuration used to resolve the held-out curve split.",
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
    parser.add_argument(
        "--full-original-onnx-summary-path",
        type=Path,
        default=DEFAULT_FULL_ORIGINAL_ONNX_SUMMARY_PATH,
        help="Existing full original ONNX summary used as a comparison baseline.",
    )
    parser.add_argument(
        "--best-model-collage-summary-path",
        type=Path,
        default=DEFAULT_BEST_MODEL_COLLAGE_SUMMARY_PATH,
        help="Existing best-model collage summary used for paper original and retuned baselines.",
    )
    return parser.parse_args()


def resolve_report_paths(arguments: argparse.Namespace) -> tuple[str, Path, Path, Path, Path]:

    """Resolve output, report, metric, and summary paths."""

    assert int(arguments.curves_per_collage) == 4, "This report expects exactly four curves per collage."
    timestamp_text = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    run_instance_id = f"{timestamp_text}__track2_sparse_original_onnx_variants"
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


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load a YAML dictionary if the source exists."""

    resolved_yaml_path = shared_training_infrastructure.resolve_runtime_project_relative_path(yaml_path)
    if not resolved_yaml_path.exists():
        return {}
    with resolved_yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | {resolved_yaml_path}"
    return loaded_dictionary


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


def evaluate_variant_curve_list(
    candidate_id: str,
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    selected_harmonic_list: list[int],
    percentage_error_denominator: str,
    target_list: list[plot_original_onnx_fw_track2_curves.HardcodedOnnxTarget],
) -> list[dict[str, Any]]:

    """Evaluate one sparse original-ONNX candidate on all forward curves."""

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


def save_metrics_csv(csv_path: Path, variant_summary_list: list[dict[str, Any]]) -> None:

    """Save one row per evaluated sparse-variant curve."""

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
        for variant_summary in variant_summary_list:
            for entry in variant_summary["per_curve_entry_list"]:
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
    target_list: list[Any],
) -> list[str]:

    """Build Markdown rows for loaded target models."""

    row_list = [
        "| Target | Harmonic | Family | Original ONNX Files |",
        "| --- | ---: | --- | --- |",
    ]
    for target in target_list:
        if isinstance(target, dict):
            target_kind = str(target["target_kind"])
            harmonic_order = int(target["harmonic_order"])
            family_name = str(target["family_name"])
            model_path = Path(str(target["model_path"]))
        else:
            target_kind = str(target.target_kind)
            harmonic_order = int(target.harmonic_order)
            family_name = str(target.family_name)
            model_path = Path(target.model_path)

        target_prefix = "A" if target_kind == "amplitude" else "P"
        row_list.append(
            "| "
            f"`{target_kind}` | "
            f"`{target_prefix}{harmonic_order}` | "
            f"`{family_name}` | "
            f"`{model_path.name}` |"
        )
    return row_list


def build_baseline_summary_list(
    full_original_onnx_summary: dict[str, Any],
    best_model_collage_summary: dict[str, Any],
) -> list[dict[str, Any]]:

    """Build comparison baseline rows from existing validated summaries."""

    baseline_summary_list: list[dict[str, Any]] = []
    if full_original_onnx_summary:
        baseline_summary_list.append(
            {
                "candidate_id": str(full_original_onnx_summary["candidate_id"]),
                "source": "full original ONNX report",
                "metrics": full_original_onnx_summary["metric_summary"],
            }
        )

    for candidate_summary in best_model_collage_summary.get("candidate_summary_list", []):
        candidate_id = str(candidate_summary.get("candidate_id", ""))
        if candidate_id in {"paper_original_best_Fw", "paper_retuned_best_Fw"}:
            baseline_summary_list.append(
                {
                    "candidate_id": candidate_id,
                    "source": str(candidate_summary.get("candidate_source_label", "")),
                    "metrics": candidate_summary["metrics"],
                }
            )

    return baseline_summary_list


def append_metric_row(line_list: list[str], candidate_id: str, metric_summary: dict[str, float]) -> None:

    """Append one TE Curve Verification Pipeline metric row."""

    line_list.append(
        "| "
        f"`{candidate_id}` | "
        f"{int(metric_summary.get('curve_count', 97))} | "
        f"{float(metric_summary['mae']):.6f} | "
        f"{float(metric_summary['rmse']):.6f} | "
        f"{float(metric_summary['mean_percentage_error_pct']):.3f} | "
        f"{float(metric_summary['p95_mean_percentage_error_pct']):.3f} |"
    )


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    metrics_csv_path: Path,
    validation_summary_path: Path,
    variant_summary_list: list[dict[str, Any]],
    baseline_summary_list: list[dict[str, Any]],
) -> str:

    """Build the report Markdown body."""

    line_list = [
        "# TE Curve Verification Pipeline Sparse Original ONNX Variant Report",
        "",
        "## Overview",
        "",
        "This report evaluates two sparse forward `TE Curve Verification Pipeline` candidates built",
        "only from the recovered paper-original `ONNX` release under",
        "`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`.",
        "Both variants reconstruct TE curves from harmonics `0`, `1`, `39`,",
        "and `40` only.",
        "",
        "## TE Curve Verification Pipeline Forward Metrics",
        "",
        "| Candidate | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for variant_summary in variant_summary_list:
        metric_summary = dict(variant_summary["metric_summary"])
        metric_summary["curve_count"] = int(variant_summary["curve_count"])
        append_metric_row(line_list, str(variant_summary["candidate_id"]), metric_summary)

    for baseline_summary in baseline_summary_list:
        metric_summary = dict(baseline_summary["metrics"])
        metric_summary["curve_count"] = 97
        append_metric_row(line_list, str(baseline_summary["candidate_id"]), metric_summary)

    for variant_summary in variant_summary_list:
        line_list.extend(
            [
                "",
                f"## {variant_summary['display_name']}",
                "",
                f"- candidate: `{variant_summary['candidate_id']}`;",
                f"- selected harmonics: `{', '.join(str(value) for value in variant_summary['selected_harmonic_list'])}`;",
                f"- loaded original `ONNX` targets: `{variant_summary['target_count']}`.",
                "",
                "### Loaded ONNX Targets",
                "",
                *build_target_table_rows(variant_summary["target_list"]),
                "",
                "### Collage",
                "",
                f"![{variant_summary['candidate_id']} TE Curve Verification Pipeline collage]({variant_summary['collage_markdown_path']})",
                "",
                "### Collaged Curves",
                "",
                "| Curve | Speed [rpm] | Torque [Nm] | Oil [C] | MAE [deg] | Mean Error [%] |",
                "| --- | ---: | ---: | ---: | ---: | ---: |",
            ]
        )

        for curve_index, entry in enumerate(variant_summary["selected_curve_list"], start=1):
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

    """Run the sparse original-ONNX report generation workflow."""

    run_instance_id, output_directory, report_path, metrics_csv_path, validation_summary_path = resolve_report_paths(
        arguments
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output_directory.mkdir(parents=True, exist_ok=True)

    curve_record_list, _, percentage_error_denominator = (
        plot_original_onnx_fw_track2_curves.build_forward_track2_curve_record_list(arguments.config_path)
    )
    variant_summary_list: list[dict[str, Any]] = []
    for variant_id in VARIANT_ID_LIST:
        variant_configuration = plot_original_onnx_fw_track2_curves.resolve_onnx_variant_configuration(variant_id)
        selected_harmonic_list = [
            int(harmonic_order)
            for harmonic_order in variant_configuration["selected_harmonic_list"]
        ]
        target_list = plot_original_onnx_fw_track2_curves.load_hardcoded_onnx_target_list(
            variant_configuration["target_configuration_list"]
        )
        per_curve_entry_list = evaluate_variant_curve_list(
            str(variant_configuration["candidate_id"]),
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
        collage_path = output_directory / "collages" / f"{variant_id}.png"
        report_asset_path = report_path.parent / "assets" / f"{variant_id}.png"
        build_track2_best_model_collage_report.save_candidate_collage(
            collage_path,
            variant_id,
            selected_curve_entry_list,
        )
        report_asset_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(collage_path, report_asset_path)

        variant_summary_list.append(
            {
                "candidate_id": str(variant_configuration["candidate_id"]),
                "display_name": str(variant_configuration["display_name"]),
                "selected_harmonic_list": selected_harmonic_list,
                "target_count": len(target_list),
                "curve_count": len(per_curve_entry_list),
                "metric_summary": metric_summary,
                "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
                "collage_markdown_path": build_relative_markdown_path(report_asset_path, report_path.parent),
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
                "per_curve_entry_list": per_curve_entry_list,
            }
        )

    save_metrics_csv(metrics_csv_path, variant_summary_list)
    baseline_summary_list = build_baseline_summary_list(
        load_yaml_dictionary(arguments.full_original_onnx_summary_path),
        load_yaml_dictionary(arguments.best_model_collage_summary_path),
    )
    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
        "variant_summary_list": [
            {
                key: value
                for key, value in variant_summary.items()
                if key != "per_curve_entry_list"
            }
            for variant_summary in variant_summary_list
        ],
        "baseline_summary_list": baseline_summary_list,
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        metrics_csv_path,
        validation_summary_path,
        variant_summary_list,
        baseline_summary_list,
    )
    report_path.write_text(report_markdown, encoding="utf-8", newline="\n")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_report(parse_command_line_arguments())
    print(f"[DONE] TE Curve Verification Pipeline sparse original ONNX variants report: {validation_summary['report_path']}")


if __name__ == "__main__":
    main()
