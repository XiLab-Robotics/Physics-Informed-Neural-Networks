"""Plot Wave 1 family-best TE predictions on held-out test curves."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import random
import sys
from dataclasses import dataclass
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

# Import PyTorch Utilities
import torch

# Import Project Utilities
from scripts.models.model_factory import create_model
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

DEFAULT_FAMILY_LIST = [
    "tree",
    "residual_harmonic_mlp",
    "feedforward",
    "periodic_mlp",
    "harmonic_regression",
]
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave1_best_model_te_curve_prediction"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "wave1_best_model_te_curve_prediction"
DEFAULT_FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
SUMMARY_FILENAME = "validation_summary.yaml"
REPORT_FILENAME = "wave1_best_model_te_curve_prediction_report.md"
PER_CURVE_METRICS_FILENAME = "per_curve_metrics.csv"
TREE_MODEL_TYPE_SET = {"random_forest", "hist_gradient_boosting"}


@dataclass(frozen=True)
class LoadedFamilyModel:

    """Loaded family-best model plus registry and config metadata."""

    family_name: str
    model_type: str
    run_name: str
    run_instance_id: str
    registry_entry: dict[str, Any]
    training_config: dict[str, Any]
    model_object: Any


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Load the current Wave 1 best model for each family, evaluate the "
            "selected held-out test curves, plot TE predictions, and generate "
            "a Markdown comparison report."
        )
    )
    argument_parser.add_argument(
        "--families",
        nargs="+",
        default=DEFAULT_FAMILY_LIST,
        help="Model-family registry names to include.",
    )
    argument_parser.add_argument(
        "--sample-fraction",
        type=float,
        default=0.20,
        help="Fraction of the canonical test-curve split to evaluate.",
    )
    argument_parser.add_argument(
        "--max-curves",
        type=int,
        default=None,
        help="Optional cap used for smoke tests or quick previews.",
    )
    argument_parser.add_argument(
        "--random-seed",
        type=int,
        default=42,
        help="Deterministic seed used to sample test curves.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for machine-readable prediction artifacts and plots.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown analysis report bundle.",
    )
    argument_parser.add_argument(
        "--family-registry-root",
        type=Path,
        default=DEFAULT_FAMILY_REGISTRY_ROOT,
        help="Root containing per-family latest_family_best.yaml files.",
    )
    argument_parser.add_argument(
        "--skip-plots",
        action="store_true",
        help="Evaluate and export CSV/report data without writing PNG plots.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    assert yaml_path.exists(), f"YAML path does not exist | {yaml_path}"
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        yaml_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(yaml_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return yaml_dictionary


def resolve_timestamped_output_paths(output_root: Path, report_topic_root: Path) -> tuple[str, Path, Path]:

    """Resolve the timestamped artifact and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__wave1_best_model_te_curve_prediction"
    )
    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(output_root) / run_instance_id
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root)
        / f"[{current_timestamp.strftime('%Y-%m-%d')}]"
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def load_family_best_entry(family_registry_root: Path, family_name: str) -> dict[str, Any]:

    """Load the current best registry entry for one model family."""

    registry_path = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
        / family_name
        / shared_training_infrastructure.FAMILY_BEST_FILENAME
    )
    registry_dictionary = load_yaml_dictionary(registry_path)
    best_entry = registry_dictionary["best_entry"]
    assert isinstance(best_entry, dict), f"Registry best_entry must be a dictionary | {registry_path}"
    return best_entry


def load_family_training_config(best_entry: dict[str, Any]) -> dict[str, Any]:

    """Load the immutable training config snapshot for one best entry."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        best_entry["output_directory"]
    )
    training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    return shared_training_infrastructure.load_training_config(training_config_path)


def load_neural_regression_module(
    best_entry: dict[str, Any],
    training_config: dict[str, Any],
) -> TransmissionErrorRegressionModule:

    """Load one family-best Lightning regression checkpoint."""

    datamodule, _, _, normalization_statistics = shared_training_infrastructure.initialize_training_components(
        training_config
    )
    checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        best_entry["best_checkpoint_path"]
    )
    regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=checkpoint_path,
        regression_model=create_model(
            model_type=str(training_config["experiment"]["model_type"]),
            model_configuration=training_config["model"],
        ),
        input_feature_dim=datamodule.get_input_feature_dim(),
        target_feature_dim=datamodule.get_target_feature_dim(),
        normalization_statistics=normalization_statistics,
        map_location=torch.device("cpu"),
    )
    regression_module.to(torch.device("cpu"))
    regression_module.eval()
    return regression_module


def load_wave1_family_best_models(
    family_name_list: list[str],
    family_registry_root: Path,
) -> list[LoadedFamilyModel]:

    """Load the current best model artifact for each requested Wave 1 family."""

    loaded_model_list: list[LoadedFamilyModel] = []
    for raw_family_name in family_name_list:
        family_name = raw_family_name.strip().lower()
        best_entry = load_family_best_entry(family_registry_root, family_name)
        training_config = load_family_training_config(best_entry)
        model_type = str(best_entry["model_type"]).strip().lower()

        if model_type in TREE_MODEL_TYPE_SET:
            model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
                best_entry["best_checkpoint_path"]
            )
            model_object = tree_regression_support.load_tree_model(model_path)
        else:
            model_object = load_neural_regression_module(best_entry, training_config)

        loaded_model_list.append(
            LoadedFamilyModel(
                family_name=family_name,
                model_type=model_type,
                run_name=str(best_entry["run_name"]),
                run_instance_id=str(best_entry["run_instance_id"]),
                registry_entry=best_entry,
                training_config=training_config,
                model_object=model_object,
            )
        )

    assert loaded_model_list, "No family-best models were loaded"
    return loaded_model_list


def build_canonical_test_dataset(reference_training_config: dict[str, Any]):

    """Build the canonical test dataset from the approved Wave 1 split config."""

    datamodule = shared_training_infrastructure.create_datamodule_from_training_config(
        reference_training_config
    )
    datamodule.setup(stage="fit")
    assert datamodule.test_dataset is not None, "Test dataset is not initialized"
    return datamodule.test_dataset, datamodule.get_dataset_split_summary()


def select_curve_indices(
    test_curve_count: int,
    sample_fraction: float,
    max_curves: int | None,
    random_seed: int,
) -> list[int]:

    """Select a deterministic subset of test curves."""

    assert test_curve_count > 0, "Test curve count must be positive"
    assert 0.0 < sample_fraction <= 1.0, f"Sample fraction must be in (0, 1] | {sample_fraction}"
    if max_curves is not None:
        assert max_curves > 0, f"Max curves must be positive | {max_curves}"

    requested_curve_count = max(1, int(round(test_curve_count * sample_fraction)))
    if max_curves is not None:
        requested_curve_count = min(requested_curve_count, max_curves)
    requested_curve_count = min(requested_curve_count, test_curve_count)

    random_generator = random.Random(random_seed)
    selected_index_list = random_generator.sample(range(test_curve_count), requested_curve_count)
    return sorted(selected_index_list)


def predict_curve_with_loaded_model(
    loaded_model: LoadedFamilyModel,
    input_tensor: torch.Tensor,
) -> np.ndarray:

    """Predict one full TE curve with one loaded family-best model."""

    if loaded_model.model_type in TREE_MODEL_TYPE_SET:
        input_feature_matrix = input_tensor.detach().cpu().numpy().astype(np.float32)
        return np.asarray(loaded_model.model_object.predict(input_feature_matrix), dtype=np.float32).reshape(-1)

    regression_module = loaded_model.model_object
    assert isinstance(regression_module, TransmissionErrorRegressionModule), (
        f"Expected TransmissionErrorRegressionModule | {loaded_model.family_name}"
    )
    with torch.no_grad():
        point_input_tensor = input_tensor.float()
        normalized_input_tensor = regression_module.normalize_input_tensor(point_input_tensor)
        normalized_prediction_tensor, _ = regression_module.forward_regression_model(
            point_input_tensor,
            normalized_input_tensor,
        )
        predicted_curve_tensor = regression_module.denormalize_target_tensor(normalized_prediction_tensor)
    return predicted_curve_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)


def compute_curve_metrics(target_curve: np.ndarray, predicted_curve: np.ndarray) -> dict[str, float]:

    """Compute curve-level TE prediction metrics."""

    target_vector = np.asarray(target_curve, dtype=np.float64).reshape(-1)
    predicted_vector = np.asarray(predicted_curve, dtype=np.float64).reshape(-1)
    residual_vector = predicted_vector - target_vector
    mae = float(np.mean(np.abs(residual_vector)))
    rmse = float(np.sqrt(np.mean(np.square(residual_vector))))
    peak_to_peak_denominator = max(float(np.ptp(target_vector)), 1.0e-12)
    mean_percentage_error_pct = float(100.0 * mae / peak_to_peak_denominator)
    return {
        "mae": mae,
        "rmse": rmse,
        "mean_percentage_error_pct": mean_percentage_error_pct,
    }


def summarize_model_metrics(metric_dictionary_list: list[dict[str, float]]) -> dict[str, float]:

    """Average curve metrics for one model."""

    assert metric_dictionary_list, "Metric dictionary list is empty"
    return {
        "mae": float(np.mean([metric["mae"] for metric in metric_dictionary_list])),
        "rmse": float(np.mean([metric["rmse"] for metric in metric_dictionary_list])),
        "mean_percentage_error_pct": float(
            np.mean([metric["mean_percentage_error_pct"] for metric in metric_dictionary_list])
        ),
        "p95_mean_percentage_error_pct": float(
            np.percentile(
                [metric["mean_percentage_error_pct"] for metric in metric_dictionary_list],
                95.0,
            )
        ),
    }


def sanitize_filename_fragment(raw_value: str) -> str:

    """Sanitize one value for use inside generated artifact filenames."""

    normalized_character_list: list[str] = []
    previous_separator = False
    for character in raw_value.strip().lower():
        if character.isalnum():
            normalized_character_list.append(character)
            previous_separator = False
            continue
        if previous_separator:
            continue
        normalized_character_list.append("_")
        previous_separator = True
    return "".join(normalized_character_list).strip("_") or "curve"


def save_prediction_csv(
    prediction_csv_path: Path,
    angular_position_deg: np.ndarray,
    target_curve_deg: np.ndarray,
    prediction_dictionary: dict[str, np.ndarray],
) -> None:

    """Save one per-point prediction table for a TE curve."""

    prediction_csv_path.parent.mkdir(parents=True, exist_ok=True)
    with prediction_csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["angular_position_deg", "measured_te_deg"]
            + [f"{model_name}_prediction_deg" for model_name in prediction_dictionary]
        )
        for point_index, angular_position_value in enumerate(angular_position_deg):
            writer.writerow(
                [
                    f"{float(angular_position_value):.9f}",
                    f"{float(target_curve_deg[point_index]):.9f}",
                ]
                + [
                    f"{float(prediction_curve[point_index]):.9f}"
                    for prediction_curve in prediction_dictionary.values()
                ]
            )


def save_prediction_plot(
    plot_path: Path,
    angular_position_deg: np.ndarray,
    target_curve_deg: np.ndarray,
    prediction_dictionary: dict[str, np.ndarray],
    curve_title: str,
) -> None:

    """Save one TE-curve overlay plot."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plot_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10.0, 5.0))
    axis.plot(angular_position_deg, target_curve_deg, label="Measured TE", linewidth=2.0, color="#111111")

    for model_name, prediction_curve in prediction_dictionary.items():
        axis.plot(angular_position_deg, prediction_curve, label=model_name, linewidth=1.2, alpha=0.88)

    axis.set_xlabel("Angular Position [deg]")
    axis.set_ylabel("Transmission Error [deg]")
    axis.set_title(curve_title)
    axis.grid(True, alpha=0.28)
    axis.legend(loc="best", fontsize=8)
    figure.tight_layout()
    figure.savefig(plot_path, dpi=180)
    plt.close(figure)


def evaluate_selected_curves(
    loaded_model_list: list[LoadedFamilyModel],
    test_dataset,
    selected_curve_index_list: list[int],
    output_directory: Path,
    write_plots: bool,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, float]], list[str], list[str]]:

    """Evaluate selected test curves and persist per-curve artifacts."""

    curve_entry_list: list[dict[str, Any]] = []
    model_metric_accumulator: dict[str, list[dict[str, float]]] = {
        loaded_model.family_name: [] for loaded_model in loaded_model_list
    }
    prediction_csv_path_list: list[str] = []
    plot_path_list: list[str] = []

    for curve_order, dataset_index in enumerate(selected_curve_index_list, start=1):
        curve_sample = test_dataset[dataset_index]
        input_tensor = curve_sample["input_tensor"].float()
        angular_position_deg = curve_sample["angular_position_deg"].numpy().reshape(-1).astype(np.float32)
        target_curve_deg = curve_sample["target_tensor"].numpy().reshape(-1).astype(np.float32)
        source_file_path = str(curve_sample["source_file_path"])
        direction_label = str(curve_sample["direction_label"])

        prediction_dictionary: dict[str, np.ndarray] = {}
        metric_dictionary: dict[str, dict[str, float]] = {}
        for loaded_model in loaded_model_list:
            prediction_curve = predict_curve_with_loaded_model(loaded_model, input_tensor)
            assert prediction_curve.shape == target_curve_deg.shape, (
                f"Prediction shape mismatch | {loaded_model.family_name} | "
                f"{prediction_curve.shape} vs {target_curve_deg.shape}"
            )
            prediction_dictionary[loaded_model.family_name] = prediction_curve
            model_metrics = compute_curve_metrics(target_curve_deg, prediction_curve)
            metric_dictionary[loaded_model.family_name] = model_metrics
            model_metric_accumulator[loaded_model.family_name].append(model_metrics)

        filename_stem = (
            f"curve_{curve_order:03d}_dataset_{dataset_index:04d}_"
            f"{sanitize_filename_fragment(direction_label)}_"
            f"{sanitize_filename_fragment(Path(source_file_path).stem)}"
        )
        prediction_csv_path = output_directory / "prediction_tables" / f"{filename_stem}.csv"
        save_prediction_csv(
            prediction_csv_path,
            angular_position_deg,
            target_curve_deg,
            prediction_dictionary,
        )
        prediction_csv_path_list.append(
            shared_training_infrastructure.format_project_relative_path(prediction_csv_path)
        )

        plot_path = output_directory / "plots" / f"{filename_stem}.png"
        if write_plots:
            curve_title = (
                f"Wave 1 Best Models | {float(curve_sample['speed_rpm']):.0f} rpm | "
                f"{float(curve_sample['torque_nm']):.0f} Nm | "
                f"{float(curve_sample['oil_temperature_deg']):.0f} C | {direction_label}"
            )
            save_prediction_plot(
                plot_path,
                angular_position_deg,
                target_curve_deg,
                prediction_dictionary,
                curve_title,
            )
            plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))

        curve_entry_list.append(
            {
                "dataset_index": int(dataset_index),
                "source_file_path": shared_training_infrastructure.format_project_relative_path(source_file_path),
                "direction_label": direction_label,
                "speed_rpm": float(curve_sample["speed_rpm"]),
                "torque_nm": float(curve_sample["torque_nm"]),
                "oil_temperature_deg": float(curve_sample["oil_temperature_deg"]),
                "sequence_length": int(curve_sample["sequence_length"]),
                "prediction_csv_path": shared_training_infrastructure.format_project_relative_path(
                    prediction_csv_path
                ),
                "plot_path": shared_training_infrastructure.format_project_relative_path(plot_path)
                if write_plots
                else "N/A",
                "metrics": metric_dictionary,
            }
        )

    aggregate_metric_dictionary = {
        model_name: summarize_model_metrics(metric_list)
        for model_name, metric_list in model_metric_accumulator.items()
    }
    return curve_entry_list, aggregate_metric_dictionary, prediction_csv_path_list, plot_path_list


def save_per_curve_metrics_csv(output_directory: Path, curve_entry_list: list[dict[str, Any]]) -> Path:

    """Save one compact per-curve metrics table."""

    csv_path = output_directory / PER_CURVE_METRICS_FILENAME
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "dataset_index",
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "model_family",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
                "prediction_csv_path",
                "plot_path",
            ]
        )
        for curve_entry in curve_entry_list:
            for model_family, metric_dictionary in curve_entry["metrics"].items():
                writer.writerow(
                    [
                        curve_entry["dataset_index"],
                        curve_entry["source_file_path"],
                        curve_entry["direction_label"],
                        f"{curve_entry['speed_rpm']:.9f}",
                        f"{curve_entry['torque_nm']:.9f}",
                        f"{curve_entry['oil_temperature_deg']:.9f}",
                        model_family,
                        f"{metric_dictionary['mae']:.9f}",
                        f"{metric_dictionary['rmse']:.9f}",
                        f"{metric_dictionary['mean_percentage_error_pct']:.9f}",
                        curve_entry["prediction_csv_path"],
                        curve_entry["plot_path"],
                    ]
                )
    return csv_path


def build_validation_summary(
    run_instance_id: str,
    output_directory: Path,
    report_path: Path,
    loaded_model_list: list[LoadedFamilyModel],
    dataset_split_summary,
    selected_curve_index_list: list[int],
    sample_fraction: float,
    random_seed: int,
    aggregate_metric_dictionary: dict[str, dict[str, float]],
    curve_entry_list: list[dict[str, Any]],
    per_curve_metrics_csv_path: Path,
    plot_path_list: list[str],
) -> dict[str, Any]:

    """Build the machine-readable validation summary."""

    return {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "selection": {
            "sample_fraction": float(sample_fraction),
            "random_seed": int(random_seed),
            "test_curve_count": int(dataset_split_summary.test_curve_count),
            "selected_curve_count": int(len(selected_curve_index_list)),
            "selected_curve_index_list": [int(index_value) for index_value in selected_curve_index_list],
        },
        "dataset_split": {
            "train_curve_count": int(dataset_split_summary.train_curve_count),
            "validation_curve_count": int(dataset_split_summary.validation_curve_count),
            "test_curve_count": int(dataset_split_summary.test_curve_count),
        },
        "models": [
            {
                "family_name": loaded_model.family_name,
                "model_type": loaded_model.model_type,
                "run_name": loaded_model.run_name,
                "run_instance_id": loaded_model.run_instance_id,
                "best_checkpoint_path": loaded_model.registry_entry["best_checkpoint_path"],
                "registry_test_mae": float(loaded_model.registry_entry["test_mae"]),
                "registry_test_rmse": float(loaded_model.registry_entry["test_rmse"]),
            }
            for loaded_model in loaded_model_list
        ],
        "aggregate_metrics": aggregate_metric_dictionary,
        "per_curve_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(
            per_curve_metrics_csv_path
        ),
        "plot_path_list": plot_path_list,
        "curve_entry_list": curve_entry_list,
    }


def build_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the Markdown comparison report."""

    selection_dictionary = validation_summary["selection"]
    aggregate_metric_dictionary = validation_summary["aggregate_metrics"]
    report_line_list = [
        "# Wave 1 Best Model TE Curve Prediction Report",
        "",
        "## Overview",
        "",
        "This report compares the current best model from each completed Wave 1",
        "family on a deterministic subset of the canonical held-out TE test",
        "curves. It is an offline inference and visualization pass only; no",
        "model is trained or promoted by this report.",
        "",
        "## Scope",
        "",
        f"- test-curve count: `{selection_dictionary['test_curve_count']}`;",
        f"- selected curve count: `{selection_dictionary['selected_curve_count']}`;",
        f"- requested sample fraction: `{selection_dictionary['sample_fraction']:.3f}`;",
        f"- random seed: `{selection_dictionary['random_seed']}`;",
        f"- output directory: `{validation_summary['output_directory']}`;",
        "",
        "## Loaded Family Best Models",
        "",
        "| Family | Model Type | Best Run | Registry Test MAE [deg] | Registry Test RMSE [deg] |",
        "| --- | --- | --- | ---: | ---: |",
    ]

    for model_entry in validation_summary["models"]:
        report_line_list.append(
            f"| `{model_entry['family_name']}` | `{model_entry['model_type']}` | "
            f"`{model_entry['run_name']}` | "
            f"{model_entry['registry_test_mae']:.6f} | "
            f"{model_entry['registry_test_rmse']:.6f} |"
        )

    report_line_list.extend(
        [
            "",
            "## Aggregate Curve Metrics",
            "",
            "| Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )

    for family_name, metric_dictionary in aggregate_metric_dictionary.items():
        report_line_list.append(
            f"| `{family_name}` | "
            f"{metric_dictionary['mae']:.6f} | "
            f"{metric_dictionary['rmse']:.6f} | "
            f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
            f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
        )

    report_line_list.extend(
        [
            "",
            "## Selected Curves",
            "",
            "| Index | Direction | Speed [rpm] | Torque [Nm] | Oil Temp [C] | Source |",
            "| ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )

    for curve_entry in validation_summary["curve_entry_list"]:
        report_line_list.append(
            f"| `{curve_entry['dataset_index']}` | `{curve_entry['direction_label']}` | "
            f"{curve_entry['speed_rpm']:.0f} | {curve_entry['torque_nm']:.0f} | "
            f"{curve_entry['oil_temperature_deg']:.0f} | `{curve_entry['source_file_path']}` |"
        )

    report_line_list.extend(
        [
            "",
            "## Output Artifacts",
            "",
            f"- validation summary: `{validation_summary['output_directory']}/{SUMMARY_FILENAME}`;",
            f"- per-curve metrics CSV: `{validation_summary['per_curve_metrics_csv_path']}`;",
        ]
    )

    for plot_path in validation_summary["plot_path_list"][:10]:
        report_line_list.append(f"- plot: `{plot_path}`;")
    if len(validation_summary["plot_path_list"]) > 10:
        remaining_plot_count = len(validation_summary["plot_path_list"]) - 10
        report_line_list.append(f"- additional plots omitted from this list: `{remaining_plot_count}`.")

    return "\n".join(report_line_list) + "\n"


def run_wave1_best_model_te_curve_prediction(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the full Wave 1 family-best TE-curve prediction comparison."""

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
    )
    report_path = report_directory / REPORT_FILENAME

    loaded_model_list = load_wave1_family_best_models(
        family_name_list=[str(family_name) for family_name in arguments.families],
        family_registry_root=arguments.family_registry_root,
    )
    reference_training_config = loaded_model_list[0].training_config
    test_dataset, dataset_split_summary = build_canonical_test_dataset(reference_training_config)
    selected_curve_index_list = select_curve_indices(
        test_curve_count=len(test_dataset),
        sample_fraction=float(arguments.sample_fraction),
        max_curves=arguments.max_curves,
        random_seed=int(arguments.random_seed),
    )

    curve_entry_list, aggregate_metric_dictionary, _, plot_path_list = evaluate_selected_curves(
        loaded_model_list=loaded_model_list,
        test_dataset=test_dataset,
        selected_curve_index_list=selected_curve_index_list,
        output_directory=output_directory,
        write_plots=not bool(arguments.skip_plots),
    )
    per_curve_metrics_csv_path = save_per_curve_metrics_csv(output_directory, curve_entry_list)

    validation_summary = build_validation_summary(
        run_instance_id=run_instance_id,
        output_directory=output_directory,
        report_path=report_path,
        loaded_model_list=loaded_model_list,
        dataset_split_summary=dataset_split_summary,
        selected_curve_index_list=selected_curve_index_list,
        sample_fraction=float(arguments.sample_fraction),
        random_seed=int(arguments.random_seed),
        aggregate_metric_dictionary=aggregate_metric_dictionary,
        curve_entry_list=curve_entry_list,
        per_curve_metrics_csv_path=per_curve_metrics_csv_path,
        plot_path_list=plot_path_list,
    )

    shared_training_infrastructure.save_yaml_snapshot(
        validation_summary,
        output_directory / SUMMARY_FILENAME,
    )
    report_path.write_text(build_report_markdown(validation_summary), encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the CLI entry point."""

    validation_summary = run_wave1_best_model_te_curve_prediction(parse_command_line_arguments())
    print(f"[DONE] Wave 1 TE-curve prediction report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
