"""Generate before/after Track 2 circular-angle plotting diagnostics."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import build_track2_best_model_collage_report
from scripts.reports.analysis import track2_circular_plotting
from scripts.training import shared_training_infrastructure

DEFAULT_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_circular_angle_plot_diagnostic"
    / "2026-07-03-16-07-27__harmonic_regression_global"
)
DEFAULT_CANDIDATE_ID = "harmonic_regression_global"


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Generate direct-line and circular-segmented Track 2 plot diagnostics."
    )
    argument_parser.add_argument(
        "--output-directory",
        type=Path,
        default=DEFAULT_OUTPUT_DIRECTORY,
        help="Directory where the diagnostic PNG files are written.",
    )
    argument_parser.add_argument(
        "--candidate-id",
        default=DEFAULT_CANDIDATE_ID,
        help="Candidate ID to plot. Defaults to harmonic_regression_global.",
    )
    return argument_parser.parse_args()


def build_curve_key(entry_dictionary: dict[str, object]) -> tuple[str, str]:

    """Build the stable source/direction key used by Track 2 report builders."""

    return (
        str(entry_dictionary["source_file_path"]),
        str(entry_dictionary["direction_label"]),
    )


def load_selected_payload_entries(
    candidate_id: str,
    output_directory: Path,
) -> tuple[list[dict[str, object]], Path]:

    """Load the same four selected curve payloads used by the collage report."""

    training_config = shared_training_infrastructure.load_training_config(
        build_track2_best_model_collage_report.DEFAULT_CONFIG_PATH
    )
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    candidate_configuration_list = build_track2_best_model_collage_report.resolve_report_candidate_configuration_list(
        training_config,
        build_track2_best_model_collage_report.DEFAULT_FAMILY_REGISTRY_ROOT,
        build_track2_best_model_collage_report.DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH,
        output_directory,
    )
    candidate_configuration = next(
        candidate_configuration
        for candidate_configuration in candidate_configuration_list
        if str(candidate_configuration["candidate_id"]).lower() == candidate_id.lower()
    )
    candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)

    candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
        candidate,
        curve_record_list,
        percentage_error_denominator,
        include_curve_payload=False,
    )
    selected_entry_list = build_track2_best_model_collage_report.select_candidate_collage_entries(
        candidate_entry_list,
        "mixed" if str(candidate.candidate_surface).lower() == "global" else str(candidate.allowed_direction_list[0]),
        4,
    )

    curve_record_lookup = {
        (
            shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
            str(curve_record.direction_label),
        ): curve_record
        for curve_record in curve_record_list
    }
    selected_curve_record_list = [
        curve_record_lookup[build_curve_key(selected_entry)]
        for selected_entry in selected_entry_list
    ]
    selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
        candidate,
        selected_curve_record_list,
        percentage_error_denominator,
        include_curve_payload=True,
    )
    selected_payload_lookup = {
        build_curve_key(selected_payload_entry): selected_payload_entry
        for selected_payload_entry in selected_payload_entry_list
    }
    ordered_payload_entry_list = [
        selected_payload_lookup[build_curve_key(selected_entry)]
        for selected_entry in selected_entry_list
    ]
    return ordered_payload_entry_list, Path(dataset_root)


def save_diagnostic_collage(
    output_path: Path,
    candidate_id: str,
    selected_payload_entry_list: list[dict[str, object]],
    use_circular_segmentation: bool,
) -> None:

    """Save one four-curve diagnostic collage."""

    figure, axis_array = plt.subplots(2, 2, figsize=(12.0, 7.0), sharex=False, sharey=False)
    flattened_axis_list = list(axis_array.reshape(-1))

    for axis, per_candidate_entry in zip(flattened_axis_list, selected_payload_entry_list):
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float64)
        truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float64)
        predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float64)
        wrap_count = int(np.count_nonzero(np.abs(np.diff(angular_position_deg)) > 180.0))

        if use_circular_segmentation:
            track2_circular_plotting.plot_circular_angle_curve(
                axis,
                angular_position_deg,
                truth_curve_deg,
                label="Measured TE",
                linewidth=1.2,
                color="#4a4a4a",
            )
            track2_circular_plotting.plot_circular_angle_curve(
                axis,
                angular_position_deg,
                predicted_curve_deg,
                label=candidate_id,
                linewidth=1.2,
                color="#1f77b4",
            )
        else:
            axis.plot(angular_position_deg, truth_curve_deg, label="Measured TE", linewidth=1.2, color="#4a4a4a")
            axis.plot(angular_position_deg, predicted_curve_deg, label=candidate_id, linewidth=1.2, color="#1f77b4")

        axis.set_title(
            (
                f"{per_candidate_entry['direction_label']} | "
                f"{float(per_candidate_entry['speed_rpm']):.0f} rpm | "
                f"{float(per_candidate_entry['torque_nm']):.0f} Nm | "
                f"{float(per_candidate_entry['oil_temperature_deg']):.0f} C | "
                f"wraps={wrap_count}"
            ),
            fontsize=9,
        )
        axis.set_xlabel("Angular Position [deg]", fontsize=8)
        axis.set_ylabel("TE [deg]", fontsize=8)
        axis.grid(True, alpha=0.28)
        axis.tick_params(labelsize=8)

    flattened_axis_list[0].legend(loc="best", fontsize=8)
    plot_mode = "circular segmented" if use_circular_segmentation else "direct line"
    figure.suptitle(f"{candidate_id} | {plot_mode}", fontsize=13)
    figure.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def run_diagnostic(arguments: argparse.Namespace) -> dict[str, object]:

    """Run the circular-angle plot diagnostic."""

    output_directory = arguments.output_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)

    selected_payload_entry_list, dataset_root = load_selected_payload_entries(
        str(arguments.candidate_id),
        output_directory,
    )
    direct_line_path = output_directory / f"{arguments.candidate_id}_direct_line.png"
    circular_segmented_path = output_directory / f"{arguments.candidate_id}_circular_segmented.png"

    save_diagnostic_collage(
        direct_line_path,
        str(arguments.candidate_id),
        selected_payload_entry_list,
        use_circular_segmentation=False,
    )
    save_diagnostic_collage(
        circular_segmented_path,
        str(arguments.candidate_id),
        selected_payload_entry_list,
        use_circular_segmentation=True,
    )

    selected_curve_summary_list: list[dict[str, object]] = []
    for per_candidate_entry in selected_payload_entry_list:
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float64)
        wrap_index_array = np.flatnonzero(np.abs(np.diff(angular_position_deg)) > 180.0) + 1
        selected_curve_summary_list.append(
            {
                "direction_label": str(per_candidate_entry["direction_label"]),
                "source_file_path": str(per_candidate_entry["source_file_path"]),
                "point_count": int(angular_position_deg.size),
                "angle_min_deg": float(np.min(angular_position_deg)),
                "angle_max_deg": float(np.max(angular_position_deg)),
                "wrap_count": int(wrap_index_array.size),
            }
        )

    return {
        "dataset_root": str(dataset_root),
        "direct_line_path": str(direct_line_path),
        "circular_segmented_path": str(circular_segmented_path),
        "selected_curve_count": len(selected_payload_entry_list),
        "selected_curve_summary_list": selected_curve_summary_list,
    }


if __name__ == "__main__":
    diagnostic_summary = run_diagnostic(parse_command_line_arguments())
    for key, value in diagnostic_summary.items():
        if key == "selected_curve_summary_list":
            print("selected_curve_summary_list:")
            for curve_summary in value:
                print(f"  - {curve_summary}")
            continue
        print(f"{key}: {value}")
