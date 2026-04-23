"""Support utilities for Track 2 reference-family vs feedforward comparison."""

from __future__ import annotations

# Import Python Utilities
import csv
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import pandas as pd
import yaml

# Import PyTorch Utilities
import torch

# Import Project Utilities
from scripts.models.model_factory import create_model
from scripts.paper_reimplementation.rcim_ml_compensation import harmonic_wise_support
from scripts.training import shared_training_infrastructure
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

COMPARISON_REPORT_ROOT = (
    shared_training_infrastructure.PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "validation_checks"
    / "track2"
)
COMPARISON_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"


@dataclass(frozen=True)
class ReferenceModelEntry:

    """One archived reference target model from the curated family inventory."""

    target_name: str
    target_kind: str
    harmonic_order: int
    python_model_path: Path
    feature_name_list: list[str]


def load_reference_family_comparison_config(config_path: str | Path) -> dict[str, Any]:

    """Load one Track 2 reference-family comparison configuration file."""

    return shared_training_infrastructure.load_training_config(config_path)


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return loaded_dictionary


def build_comparison_report_path(training_config: dict[str, Any]) -> Path:

    """Build the canonical Markdown report path for one comparison run."""

    report_timestamp = datetime.now().strftime(COMPARISON_REPORT_TIMESTAMP_FORMAT)
    run_name = shared_training_infrastructure.sanitize_name(
        shared_training_infrastructure.resolve_output_run_name(training_config)
    )
    return COMPARISON_REPORT_ROOT / f"{report_timestamp}_{run_name}_report.md"


def load_reference_inventory(reference_inventory_path: str | Path) -> dict[str, Any]:

    """Load one curated Track 1 family reference inventory."""

    resolved_inventory_path = shared_training_infrastructure.resolve_runtime_project_relative_path(reference_inventory_path)
    assert resolved_inventory_path.exists(), f"Reference Inventory Path does not exist | {resolved_inventory_path}"
    return load_yaml_dictionary(resolved_inventory_path)


def resolve_selected_harmonic_list(reference_inventory: dict[str, Any]) -> list[int]:

    """Resolve the harmonic orders covered by the curated reference inventory."""

    archive_scope = reference_inventory["archive_scope"]
    amplitude_harmonic_order_list = [int(harmonic_order) for harmonic_order in archive_scope["amplitude_harmonic_order_list"]]
    phase_harmonic_order_list = [int(harmonic_order) for harmonic_order in archive_scope["phase_harmonic_order_list"]]
    selected_harmonic_list = sorted(set(amplitude_harmonic_order_list) | set(phase_harmonic_order_list))
    assert selected_harmonic_list and selected_harmonic_list[0] == 0, "Reference bank must include harmonic 0"
    return selected_harmonic_list


def load_reference_model_entries(reference_inventory: dict[str, Any]) -> list[ReferenceModelEntry]:

    """Load and validate the reference target-model inventory entries."""

    reference_model_entry_list: list[ReferenceModelEntry] = []
    for reference_entry in reference_inventory["reference_models"]:
        python_model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            reference_entry["python_model_path"]
        )
        reference_model_entry_list.append(
            ReferenceModelEntry(
                target_name=str(reference_entry["target_name"]),
                target_kind=str(reference_entry["target_kind"]).strip().lower(),
                harmonic_order=int(reference_entry["harmonic_order"]),
                python_model_path=python_model_path,
                feature_name_list=[str(feature_name) for feature_name in reference_entry["feature_name_list"]],
            )
        )

    assert reference_model_entry_list, "Reference inventory produced no model entries"
    return reference_model_entry_list


def load_reference_model_dictionary(reference_model_entry_list: list[ReferenceModelEntry]) -> dict[str, Any]:

    """Load the archived Python estimators for one curated reference bank."""

    reference_model_dictionary: dict[str, Any] = {}
    for reference_entry in reference_model_entry_list:
        with reference_entry.python_model_path.open("rb") as model_file:
            reference_model_dictionary[reference_entry.target_name] = pickle.load(model_file)
    return reference_model_dictionary


def resolve_feedforward_best_entry(feedforward_leaderboard_path: str | Path) -> dict[str, Any]:

    """Resolve the current canonical best feedforward registry entry."""

    leaderboard_dictionary = load_yaml_dictionary(
        shared_training_infrastructure.resolve_runtime_project_relative_path(feedforward_leaderboard_path)
    )
    entry_list = leaderboard_dictionary["entry_list"]
    assert isinstance(entry_list, list) and entry_list, "Feedforward leaderboard entry_list is empty"
    best_entry = entry_list[0]
    assert str(best_entry["model_family"]).strip().lower() == "feedforward", "Unexpected best-entry family"
    return best_entry


def load_feedforward_regression_module(feedforward_best_entry: dict[str, Any]) -> tuple[TransmissionErrorRegressionModule, dict[str, Any]]:

    """Load the canonical best feedforward checkpoint plus its config snapshot."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        feedforward_best_entry["output_directory"]
    )
    training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    datamodule, _, _, normalization_statistics = shared_training_infrastructure.initialize_training_components(training_config)
    datamodule.setup(stage="fit")
    best_checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        feedforward_best_entry["best_checkpoint_path"]
    )
    regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=best_checkpoint_path,
        regression_model=create_model(
            model_type=str(training_config["experiment"]["model_type"]),
            model_configuration=training_config["model"],
        ),
        input_feature_dim=datamodule.get_input_feature_dim(),
        target_feature_dim=datamodule.get_target_feature_dim(),
        normalization_statistics=normalization_statistics,
    )
    regression_module.to(torch.device("cpu"))
    regression_module.eval()
    return regression_module, training_config


def build_curve_record_list(
    training_config: dict[str, Any],
    selected_harmonic_list: list[int],
) -> tuple[list[harmonic_wise_support.HarmonicCurveRecord], dict[str, int], dict[str, int], Path]:

    """Build the held-out TE-curve record list used by the comparison."""

    split_record_bundle, directional_count_dictionary, file_count_dictionary, dataset_root = (
        harmonic_wise_support.build_split_record_bundle(training_config)
    )
    return split_record_bundle["test"], directional_count_dictionary, file_count_dictionary, dataset_root


def build_reference_feature_matrix(curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord]) -> pd.DataFrame:

    """Build the reference-bank feature matrix aligned with the archived models."""

    return pd.DataFrame(
        data=[
            {
                "rpm": float(curve_record.speed_rpm),
                "deg": float(curve_record.oil_temperature_deg),
                "tor": float(curve_record.torque_nm),
            }
            for curve_record in curve_record_list
        ],
        columns=["rpm", "deg", "tor"],
    )


def predict_reference_bank_target_dictionary(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_model_entry_list: list[ReferenceModelEntry],
    reference_model_dictionary: dict[str, Any],
) -> dict[str, np.ndarray]:

    """Predict all archived amplitude and phase targets for the held-out curves."""

    reference_feature_matrix = build_reference_feature_matrix(curve_record_list)
    predicted_target_dictionary: dict[str, np.ndarray] = {}
    for reference_entry in reference_model_entry_list:
        assert reference_entry.feature_name_list == ["rpm", "deg", "tor"], (
            "Unexpected reference feature schema | "
            f"{reference_entry.feature_name_list}"
        )
        predicted_target_dictionary[reference_entry.target_name] = np.asarray(
            reference_model_dictionary[reference_entry.target_name].predict(reference_feature_matrix),
            dtype=np.float32,
        ).reshape(-1)
    return predicted_target_dictionary


def build_reference_coefficient_dictionary(
    predicted_target_dictionary: dict[str, np.ndarray],
    sample_index: int,
    selected_harmonic_list: list[int],
) -> tuple[dict[str, float], dict[str, float]]:

    """Convert one amplitude/phase prediction set into harmonic coefficients."""

    coefficient_dictionary: dict[str, float] = {}
    amplitude_phase_dictionary: dict[str, float] = {}

    for harmonic_order in selected_harmonic_list:
        amplitude_target_name = f"fft_y_Fw_filtered_ampl_{harmonic_order}"
        predicted_amplitude = float(predicted_target_dictionary[amplitude_target_name][sample_index])

        if harmonic_order == 0:
            coefficient_dictionary["coefficient_cos_h0"] = predicted_amplitude
            amplitude_phase_dictionary["amplitude_h0"] = abs(predicted_amplitude)
            amplitude_phase_dictionary["phase_rad_h0"] = 0.0
            continue

        phase_target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
        predicted_phase = float(predicted_target_dictionary[phase_target_name][sample_index])
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(predicted_amplitude * np.cos(predicted_phase))
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(-predicted_amplitude * np.sin(predicted_phase))
        amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = float(predicted_amplitude)
        amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = float(predicted_phase)

    return coefficient_dictionary, amplitude_phase_dictionary


def build_reference_target_metric_dictionary(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    predicted_target_dictionary: dict[str, np.ndarray],
    selected_harmonic_list: list[int],
) -> dict[str, float]:

    """Build compact amplitude and phase diagnostics for the archived bank."""

    amplitude_error_list: list[float] = []
    phase_error_list: list[float] = []

    for sample_index, curve_record in enumerate(curve_record_list):
        for harmonic_order in selected_harmonic_list:
            amplitude_target_name = f"fft_y_Fw_filtered_ampl_{harmonic_order}"
            truth_amplitude = float(curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"])
            predicted_amplitude = float(predicted_target_dictionary[amplitude_target_name][sample_index])
            amplitude_error_list.append(abs(predicted_amplitude - truth_amplitude))

            if harmonic_order == 0:
                continue

            phase_target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
            truth_phase = float(curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"])
            predicted_phase = float(predicted_target_dictionary[phase_target_name][sample_index])
            wrapped_phase_error = abs(harmonic_wise_support.wrap_phase_difference_radians(predicted_phase - truth_phase))
            phase_error_list.append(float(wrapped_phase_error))

    return {
        "amplitude_mae": float(np.mean(amplitude_error_list)),
        "amplitude_rmse": float(np.sqrt(np.mean(np.square(amplitude_error_list)))),
        "phase_mae_rad": float(np.mean(phase_error_list)) if phase_error_list else 0.0,
        "phase_rmse_rad": float(np.sqrt(np.mean(np.square(phase_error_list)))) if phase_error_list else 0.0,
    }


def build_feedforward_input_tensor(curve_record: harmonic_wise_support.HarmonicCurveRecord) -> torch.Tensor:

    """Build the pointwise feedforward input tensor for one curve record."""

    sequence_length = int(curve_record.angular_position_deg.shape[0])
    input_feature_matrix = np.column_stack(
        [
            curve_record.angular_position_deg.astype(np.float32),
            np.full(sequence_length, curve_record.speed_rpm, dtype=np.float32),
            np.full(sequence_length, curve_record.torque_nm, dtype=np.float32),
            np.full(sequence_length, curve_record.oil_temperature_deg, dtype=np.float32),
            np.full(sequence_length, curve_record.direction_flag, dtype=np.float32),
        ]
    ).astype(np.float32)
    return torch.from_numpy(input_feature_matrix)


def predict_feedforward_curve(
    regression_module: TransmissionErrorRegressionModule,
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
) -> np.ndarray:

    """Predict one TE curve with the canonical feedforward checkpoint."""

    input_tensor = build_feedforward_input_tensor(curve_record).float()
    with torch.no_grad():
        normalized_input_tensor = regression_module.normalize_input_tensor(input_tensor)
        normalized_prediction_tensor, _ = regression_module.forward_regression_model(
            input_tensor,
            normalized_input_tensor,
        )
        predicted_curve_tensor = regression_module.denormalize_target_tensor(normalized_prediction_tensor)
    return predicted_curve_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)


def summarize_metric_dictionary(metric_dictionary_list: list[dict[str, float]]) -> dict[str, float]:

    """Average one metric-dictionary list and add a `p95` percentage statistic."""

    mean_metric_dictionary = harmonic_wise_support.average_metric_dictionary(metric_dictionary_list)
    percentage_error_list = [metric_dictionary["mean_percentage_error_pct"] for metric_dictionary in metric_dictionary_list]
    mean_metric_dictionary["p95_mean_percentage_error_pct"] = float(np.percentile(percentage_error_list, 95.0))
    return mean_metric_dictionary


def build_group_metric_summary(
    per_sample_entry_list: list[dict[str, Any]],
    group_key_name: str,
) -> dict[str, dict[str, dict[str, float]]]:

    """Aggregate per-model metrics by one chosen grouping key."""

    grouped_metric_accumulator: dict[str, dict[str, list[dict[str, float]]]] = {}
    for per_sample_entry in per_sample_entry_list:
        group_key = str(per_sample_entry[group_key_name])
        grouped_metric_accumulator.setdefault(group_key, {})
        for model_name in ["lgbm19_reference_bank", "feedforward_best", "oracle_harmonic_truncation"]:
            metric_dictionary = per_sample_entry[f"{model_name}_metrics"]
            grouped_metric_accumulator[group_key].setdefault(model_name, []).append(metric_dictionary)

    return {
        group_key: {
            model_name: summarize_metric_dictionary(metric_dictionary_list)
            for model_name, metric_dictionary_list in model_metric_dictionary.items()
        }
        for group_key, model_metric_dictionary in grouped_metric_accumulator.items()
    }


def save_per_condition_metrics_csv(output_directory: Path, per_sample_entry_list: list[dict[str, Any]]) -> Path:

    """Save one per-condition comparison table for downstream inspection."""

    csv_path = output_directory / "per_condition_metrics.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "model_name",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
            ]
        )
        for per_sample_entry in per_sample_entry_list:
            for model_name in ["lgbm19_reference_bank", "feedforward_best", "oracle_harmonic_truncation"]:
                metric_dictionary = per_sample_entry[f"{model_name}_metrics"]
                writer.writerow(
                    [
                        per_sample_entry["source_file_path"],
                        per_sample_entry["direction_label"],
                        per_sample_entry["speed_rpm"],
                        per_sample_entry["torque_nm"],
                        per_sample_entry["oil_temperature_deg"],
                        model_name,
                        metric_dictionary["mae"],
                        metric_dictionary["rmse"],
                        metric_dictionary["mean_percentage_error_pct"],
                    ]
                )
    return csv_path


def maybe_generate_preview_plots(
    output_directory: Path,
    per_sample_entry_list: list[dict[str, Any]],
    preview_curve_count: int,
) -> list[str]:

    """Generate a few representative overlay plots when matplotlib is available."""

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return []

    preview_directory = output_directory / "preview_curves"
    preview_directory.mkdir(parents=True, exist_ok=True)
    preview_plot_path_list: list[str] = []

    for preview_index, per_sample_entry in enumerate(per_sample_entry_list[:preview_curve_count]):
        figure, axis = plt.subplots(figsize=(8.0, 4.0))
        angular_position_deg = np.asarray(per_sample_entry["angular_position_deg"], dtype=np.float32)
        axis.plot(angular_position_deg, per_sample_entry["truth_curve_deg"], label="Truth", linewidth=1.5)
        axis.plot(angular_position_deg, per_sample_entry["lgbm19_curve_deg"], label="LGBM-19", linewidth=1.1)
        axis.plot(angular_position_deg, per_sample_entry["feedforward_curve_deg"], label="Feedforward", linewidth=1.1)
        axis.set_xlabel("Angular Position [deg]")
        axis.set_ylabel("Transmission Error [deg]")
        axis.set_title(
            f"Preview {preview_index + 1} | "
            f"{per_sample_entry['speed_rpm']:.0f} rpm | "
            f"{per_sample_entry['torque_nm']:.0f} Nm | "
            f"{per_sample_entry['oil_temperature_deg']:.0f} C | "
            f"{per_sample_entry['direction_label']}"
        )
        axis.grid(True, alpha=0.3)
        axis.legend(loc="best")
        plot_path = preview_directory / f"preview_{preview_index + 1:02d}.png"
        figure.tight_layout()
        figure.savefig(plot_path, dpi=180)
        plt.close(figure)
        preview_plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))

    return preview_plot_path_list


def build_comparison_summary(
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    reference_inventory: dict[str, Any],
    feedforward_best_entry: dict[str, Any],
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_target_metric_dictionary: dict[str, float],
    aggregate_metric_dictionary: dict[str, dict[str, float]],
    per_sample_entry_list: list[dict[str, Any]],
    direction_metric_summary: dict[str, dict[str, dict[str, float]]],
    temperature_metric_summary: dict[str, dict[str, dict[str, float]]],
    preview_plot_path_list: list[str],
    per_condition_metrics_csv_path: Path,
    selected_harmonic_list: list[int],
) -> dict[str, Any]:

    """Build the machine-readable comparison summary."""

    comparison_configuration = training_config["comparison"]
    return {
        "config_path": shared_training_infrastructure.format_project_relative_path(resolved_config_path),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "comparison_scope": {
            "reference_family_name": str(reference_inventory["paper_family_name"]),
            "reference_bank_model_count": int(len(reference_inventory["reference_models"])),
            "selected_harmonic_list": list(selected_harmonic_list),
            "percentage_error_denominator": str(comparison_configuration["percentage_error_denominator"]),
            "curve_count": int(len(curve_record_list)),
        },
        "feedforward_reference": {
            "run_instance_id": str(feedforward_best_entry["run_instance_id"]),
            "run_name": str(feedforward_best_entry["run_name"]),
            "best_checkpoint_path": str(feedforward_best_entry["best_checkpoint_path"]),
            "registry_test_mae": float(feedforward_best_entry["test_mae"]),
            "registry_test_rmse": float(feedforward_best_entry["test_rmse"]),
        },
        "reference_bank": {
            "reference_inventory_path": shared_training_infrastructure.format_project_relative_path(
                shared_training_infrastructure.resolve_runtime_project_relative_path(
                    training_config["paths"]["reference_inventory_path"]
                )
            ),
            "paper_family_name": str(reference_inventory["paper_family_name"]),
            "target_metric_summary": reference_target_metric_dictionary,
        },
        "aggregate_metrics": aggregate_metric_dictionary,
        "direction_breakdown": direction_metric_summary,
        "temperature_breakdown": temperature_metric_summary,
        "preview_plot_path_list": preview_plot_path_list,
        "per_condition_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(
            per_condition_metrics_csv_path
        ),
        "sample_preview_list": [
            {
                "source_file_path": per_sample_entry["source_file_path"],
                "direction_label": per_sample_entry["direction_label"],
                "speed_rpm": per_sample_entry["speed_rpm"],
                "torque_nm": per_sample_entry["torque_nm"],
                "oil_temperature_deg": per_sample_entry["oil_temperature_deg"],
                "lgbm19_mean_percentage_error_pct": per_sample_entry["lgbm19_reference_bank_metrics"]["mean_percentage_error_pct"],
                "feedforward_mean_percentage_error_pct": per_sample_entry["feedforward_best_metrics"]["mean_percentage_error_pct"],
                "oracle_mean_percentage_error_pct": per_sample_entry["oracle_harmonic_truncation_metrics"]["mean_percentage_error_pct"],
            }
            for per_sample_entry in per_sample_entry_list[:3]
        ],
    }


def build_reference_family_vs_feedforward_report_markdown(comparison_summary: dict[str, Any]) -> str:

    """Build the Markdown comparison report."""

    comparison_scope = comparison_summary["comparison_scope"]
    feedforward_reference = comparison_summary["feedforward_reference"]
    reference_bank = comparison_summary["reference_bank"]
    aggregate_metrics = comparison_summary["aggregate_metrics"]

    report_line_list = [
        "# Track 2 LGBM19 Vs Feedforward Comparison Report",
        "",
        "## Overview",
        "",
        "This report compares the curated paper-faithful `LGBM-19` harmonic bank",
        "against the canonical best direct-TE `feedforward` baseline on the",
        "repository held-out TE-curve test split.",
        "",
        "## Scope",
        "",
        f"- reference family: `{reference_bank['paper_family_name']}`;",
        f"- reference bank size: `{comparison_scope['reference_bank_model_count']}` archived target models;",
        f"- selected harmonics: `{', '.join(str(harmonic_order) for harmonic_order in comparison_scope['selected_harmonic_list'])}`;",
        f"- held-out curve count: `{comparison_scope['curve_count']}`;",
        f"- percentage-error denominator: `{comparison_scope['percentage_error_denominator']}`;",
        f"- canonical feedforward run: `{feedforward_reference['run_instance_id']}`;",
        "",
        "## Aggregate Comparison",
        "",
        "| Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
        "| --- | ---: | ---: | ---: | ---: |",
        (
            f"| `LGBM-19 reference bank` | "
            f"{aggregate_metrics['lgbm19_reference_bank']['mae']:.6f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['rmse']:.6f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        (
            f"| `feedforward best` | "
            f"{aggregate_metrics['feedforward_best']['mae']:.6f} | "
            f"{aggregate_metrics['feedforward_best']['rmse']:.6f} | "
            f"{aggregate_metrics['feedforward_best']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['feedforward_best']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        (
            f"| `oracle harmonic truncation` | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['mae']:.6f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['rmse']:.6f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        "",
        "## Reference Bank Diagnostics",
        "",
        f"- amplitude MAE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['amplitude_mae']:.6f}`.",
        f"- amplitude RMSE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['amplitude_rmse']:.6f}`.",
        f"- phase MAE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['phase_mae_rad']:.6f} rad`.",
        f"- phase RMSE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['phase_rmse_rad']:.6f} rad`.",
        "",
        "## Direction Breakdown",
        "",
        "| Direction | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |",
        "| --- | --- | ---: | ---: | ---: |",
    ]

    for direction_label, direction_entry in comparison_summary["direction_breakdown"].items():
        for model_name, metric_dictionary in direction_entry.items():
            report_line_list.append(
                f"| `{direction_label}` | `{model_name}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
            )

    report_line_list.extend(
        [
            "",
            "## Temperature Breakdown",
            "",
            "| Temperature [C] | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )

    for temperature_label, temperature_entry in comparison_summary["temperature_breakdown"].items():
        for model_name, metric_dictionary in temperature_entry.items():
            report_line_list.append(
                f"| `{temperature_label}` | `{model_name}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
            )

    report_line_list.extend(
        [
            "",
            "## Sample Preview",
            "",
        ]
    )

    for preview_entry in comparison_summary["sample_preview_list"]:
        report_line_list.append(
            (
                f"- `{preview_entry['source_file_path']}` | `{preview_entry['direction_label']}` | "
                f"`{preview_entry['speed_rpm']:.0f} rpm` | "
                f"`{preview_entry['torque_nm']:.0f} Nm` | "
                f"`{preview_entry['oil_temperature_deg']:.0f} C` | "
                f"`LGBM={preview_entry['lgbm19_mean_percentage_error_pct']:.3f}%` | "
                f"`feedforward={preview_entry['feedforward_mean_percentage_error_pct']:.3f}%` | "
                f"`oracle={preview_entry['oracle_mean_percentage_error_pct']:.3f}%`"
            )
        )

    report_line_list.extend(
        [
            "",
            "## Output Artifacts",
            "",
            f"- summary YAML: `{comparison_summary['output_directory']}/validation_summary.yaml`;",
            f"- per-condition CSV: `{comparison_summary['per_condition_metrics_csv_path']}`;",
        ]
    )

    for preview_plot_path in comparison_summary["preview_plot_path_list"]:
        report_line_list.append(f"- preview plot: `{preview_plot_path}`;")

    return "\n".join(report_line_list) + "\n"
