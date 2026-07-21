"""Build Track 2 candidate curve plots from a compact comparison config."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path
from typing import Any

# Import Third-Party Libraries
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
    run_reference_family_vs_feedforward_comparison,
)
from scripts.reports.analysis import track2_circular_plotting
from scripts.training import shared_training_infrastructure


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line parser."""

    argument_parser = argparse.ArgumentParser(
        description="Generate bounded Track 2 truth-vs-prediction plots for configured candidates."
    )
    argument_parser.add_argument("--config-path", required=True, type=Path)
    argument_parser.add_argument("--output-root", required=True, type=Path)
    argument_parser.add_argument("--dataset", default=None)
    argument_parser.add_argument("--surface-scope", default="forward")
    argument_parser.add_argument("--max-plots-per-candidate", type=int, default=4)
    argument_parser.add_argument("--windows", action="store_true")
    return argument_parser


def load_candidate_payloads(
    config_path: Path,
    dataset_name: str | None,
    surface_scope: str,
    max_plots_per_candidate: int,
) -> list[dict[str, Any]]:

    """Evaluate configured candidates with curve payloads retained."""

    training_config = shared_training_infrastructure.apply_dataset_override(
        reference_family_vs_feedforward_support.load_reference_family_comparison_config(config_path),
        dataset_name,
    )
    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    candidate_configuration_list = (
        run_reference_family_vs_feedforward_comparison.filter_candidate_configuration_list_by_dataset_scope(
            candidate_configuration_list,
            str(training_config.get("dataset", {}).get("name", dataset_name or "")),
        )
    )
    candidate_configuration_list = (
        run_reference_family_vs_feedforward_comparison.filter_candidate_configuration_list_by_surface_scope(
            candidate_configuration_list,
            surface_scope,
        )
    )
    selected_harmonic_list = [
        int(harmonic_order)
        for harmonic_order in training_config.get("evaluation", {}).get("selected_harmonics", [])
    ]
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    curve_record_list = run_reference_family_vs_feedforward_comparison.filter_curve_record_list_by_surface_scope(
        curve_record_list,
        surface_scope,
    )
    plot_curve_record_list = curve_record_list[:max_plots_per_candidate]
    assert plot_curve_record_list, f"No curve records available for plotting | surface_scope={surface_scope}"

    payload_list: list[dict[str, Any]] = []
    for candidate_configuration in candidate_configuration_list:
        candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        candidate_payload_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            candidate,
            plot_curve_record_list,
            str(training_config["comparison"].get("percentage_error_denominator", "peak_to_peak_truth")),
            include_curve_payload=True,
        )
        payload_list.extend(candidate_payload_list)
    return payload_list


def save_candidate_curve_plots(
    payload_list: list[dict[str, Any]],
    output_root: Path,
    max_plots_per_candidate: int,
) -> list[str]:

    """Render bounded candidate curve overlays and return repository-relative paths."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    grouped_payload_dictionary: dict[str, list[dict[str, Any]]] = {}
    for payload in payload_list:
        grouped_payload_dictionary.setdefault(str(payload["candidate_id"]), []).append(payload)

    output_root.mkdir(parents=True, exist_ok=True)
    plot_path_list: list[str] = []
    for candidate_id, candidate_payload_list in sorted(grouped_payload_dictionary.items()):
        candidate_output_directory = output_root / candidate_id
        candidate_output_directory.mkdir(parents=True, exist_ok=True)
        for plot_index, payload in enumerate(candidate_payload_list[:max_plots_per_candidate], start=1):
            angular_position_deg, truth_curve_deg, predicted_curve_deg = (
                track2_circular_plotting.prepare_sorted_circular_angle_curve_arrays(
                    payload["angular_position_deg"],
                    payload["truth_curve_deg"],
                    payload["predicted_curve_deg"],
                )
            )
            figure, axis = plt.subplots(figsize=(8.0, 4.0))
            track2_circular_plotting.plot_circular_angle_curve(
                axis,
                angular_position_deg,
                truth_curve_deg,
                label="Truth",
                linewidth=1.5,
            )
            track2_circular_plotting.plot_circular_angle_curve(
                axis,
                angular_position_deg,
                predicted_curve_deg,
                label=candidate_id,
                linewidth=1.1,
            )
            axis.set_title(
                f"{payload['direction_label']} | {float(payload['speed_rpm']):.0f} rpm | "
                f"{float(payload['torque_nm']):.0f} Nm | {float(payload['oil_temperature_deg']):.1f} C"
            )
            axis.set_xlabel("Angular position [deg]")
            axis.set_ylabel("Transmission error [deg]")
            axis.grid(True, alpha=0.25)
            axis.legend(loc="best")
            figure.tight_layout()
            plot_path = candidate_output_directory / f"{plot_index:02d}_{candidate_id}.png"
            figure.savefig(plot_path, dpi=180)
            plt.close(figure)
            plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))
    return plot_path_list


def write_plot_summary(output_root: Path, plot_path_list: list[str]) -> Path:

    """Write a compact YAML summary for generated plots."""

    summary_path = output_root / "track2_candidate_curve_plot_summary.yaml"
    summary_dictionary = {
        "plot_count": len(plot_path_list),
        "plot_path_list": plot_path_list,
    }
    with summary_path.open("w", encoding="utf-8") as summary_file:
        yaml.safe_dump(summary_dictionary, summary_file, sort_keys=False)
    return summary_path


def main() -> None:

    """Run the Track 2 candidate plot builder."""

    parsed_arguments = build_argument_parser().parse_args()
    payload_list = load_candidate_payloads(
        parsed_arguments.config_path,
        parsed_arguments.dataset,
        parsed_arguments.surface_scope,
        parsed_arguments.max_plots_per_candidate,
    )
    output_root = shared_training_infrastructure.resolve_runtime_project_relative_path(parsed_arguments.output_root)
    plot_path_list = save_candidate_curve_plots(
        payload_list,
        output_root,
        parsed_arguments.max_plots_per_candidate,
    )
    summary_path = write_plot_summary(output_root, plot_path_list)
    print(f"[DONE] Track 2 candidate curve plots written | {summary_path}")


if __name__ == "__main__":
    main()
