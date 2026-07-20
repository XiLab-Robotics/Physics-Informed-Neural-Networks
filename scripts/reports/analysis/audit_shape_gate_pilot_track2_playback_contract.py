"""Audit sequence playback contracts for one Track 2 registry candidate."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import sys
from pathlib import Path
from typing import Any

# Import Third-Party Libraries
import numpy as np
import torch
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
    run_reference_family_vs_feedforward_comparison,
)
from scripts.training import shared_training_infrastructure
from scripts.training.transmission_error_datamodule import TransmissionErrorDataModule
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line parser."""

    argument_parser = argparse.ArgumentParser(
        description="Audit Track 2 full-curve playback against training-like sequence windows."
    )
    argument_parser.add_argument("--config-path", required=True, type=Path)
    argument_parser.add_argument("--output-root", required=True, type=Path)
    argument_parser.add_argument("--dataset", default=None)
    argument_parser.add_argument("--surface-scope", default="forward")
    argument_parser.add_argument("--max-curves", type=int, default=0)
    return argument_parser


def write_csv_row_list(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries as a CSV table."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not row_list:
        output_path.write_text("", encoding="utf-8")
        return

    field_name_list = list(row_list[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_name_list)
        writer.writeheader()
        writer.writerows(row_list)


def build_training_like_target_index_array(
    point_count: int,
    sequence_length: int,
    sequence_stride: int,
    sequence_target_position: str,
    maximum_sequences_per_curve: int | None,
) -> np.ndarray:

    """Build the target indices used by the training sequence collate path."""

    assert point_count >= sequence_length, f"Point count is shorter than sequence length | {point_count}"
    normalized_target_position = sequence_target_position.strip().lower()
    assert normalized_target_position in {"center", "last"}, (
        f"Unsupported sequence target position | {sequence_target_position}"
    )
    target_offset = sequence_length // 2 if normalized_target_position == "center" else sequence_length - 1
    start_index_array = np.arange(0, point_count - sequence_length + 1, sequence_stride, dtype=np.int64)
    if maximum_sequences_per_curve is not None and len(start_index_array) > maximum_sequences_per_curve:
        reduced_position_array = np.linspace(
            0,
            len(start_index_array) - 1,
            num=maximum_sequences_per_curve,
            dtype=np.float32,
        ).round().astype(np.int64)
        start_index_array = start_index_array[reduced_position_array]
    return start_index_array + target_offset


def predict_training_like_sequence_targets(
    model_object: TransmissionErrorRegressionModule,
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    training_config: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray]:

    """Predict only the non-padded sequence windows used by the training collate path."""

    expected_input_feature_dim = reference_family_vs_feedforward_support.resolve_expected_input_feature_dim(
        training_config,
        model_object,
    )
    point_input_tensor = reference_family_vs_feedforward_support.build_feedforward_input_tensor(
        curve_record,
        training_config,
        expected_input_feature_dim,
    ).float().to(model_object.input_feature_mean.device)
    dataset_configuration = training_config.get("dataset", {})
    sequence_length = int(dataset_configuration.get("sequence_length", 1))
    sequence_stride = int(dataset_configuration.get("sequence_stride", 1))
    sequence_target_position = str(dataset_configuration.get("sequence_target_position", "center"))
    maximum_sequences_per_curve = dataset_configuration.get("maximum_sequences_per_curve")
    if maximum_sequences_per_curve is not None:
        maximum_sequences_per_curve = int(maximum_sequences_per_curve)

    target_index_array = build_training_like_target_index_array(
        int(point_input_tensor.shape[0]),
        sequence_length,
        sequence_stride,
        sequence_target_position,
        maximum_sequences_per_curve,
    )
    sequence_window_tensor_list = [
        point_input_tensor[int(target_index) - sequence_length // 2:int(target_index) - sequence_length // 2 + sequence_length]
        if sequence_target_position.strip().lower() == "center"
        else point_input_tensor[int(target_index) - sequence_length + 1:int(target_index) + 1]
        for target_index in target_index_array.tolist()
    ]
    input_tensor = torch.stack(sequence_window_tensor_list, dim=0)
    with torch.no_grad():
        normalized_input_tensor = model_object.normalize_input_tensor(input_tensor)
        normalized_prediction_tensor, _ = model_object.forward_regression_model(
            input_tensor,
            normalized_input_tensor,
        )
        deterministic_prediction_tensor = model_object.extract_deterministic_prediction_tensor(
            normalized_prediction_tensor
        )
        predicted_target_tensor = model_object.denormalize_target_tensor(deterministic_prediction_tensor)
    return target_index_array, predicted_target_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)


def compute_basic_metric_dictionary(
    truth_array: np.ndarray,
    prediction_array: np.ndarray,
) -> dict[str, float]:

    """Compute compact raw and centered error metrics."""

    error_array = prediction_array.astype(np.float64) - truth_array.astype(np.float64)
    centered_prediction_array = prediction_array - float(np.mean(prediction_array))
    centered_truth_array = truth_array - float(np.mean(truth_array))
    centered_error_array = centered_prediction_array.astype(np.float64) - centered_truth_array.astype(np.float64)
    return {
        "mae_deg": float(np.mean(np.abs(error_array))),
        "rmse_deg": float(np.sqrt(np.mean(np.square(error_array)))),
        "mean_error_deg": float(np.mean(error_array)),
        "absolute_offset_error_deg": float(abs(np.mean(error_array))),
        "centered_mae_deg": float(np.mean(np.abs(centered_error_array))),
        "truth_mean_deg": float(np.mean(truth_array)),
        "prediction_mean_deg": float(np.mean(prediction_array)),
    }


def build_audit_row(
    candidate_id: str,
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    full_prediction_array: np.ndarray,
    training_like_target_index_array: np.ndarray,
    training_like_prediction_array: np.ndarray,
) -> dict[str, Any]:

    """Build one per-curve audit row."""

    truth_array = curve_record.transmission_error_deg.astype(np.float32)
    full_metric_dictionary = compute_basic_metric_dictionary(truth_array, full_prediction_array)
    sampled_truth_array = truth_array[training_like_target_index_array]
    sampled_full_prediction_array = full_prediction_array[training_like_target_index_array]
    sampled_full_metric_dictionary = compute_basic_metric_dictionary(
        sampled_truth_array,
        sampled_full_prediction_array,
    )
    training_like_metric_dictionary = compute_basic_metric_dictionary(
        sampled_truth_array,
        training_like_prediction_array,
    )

    return {
        "candidate_id": candidate_id,
        "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
        "direction_label": curve_record.direction_label,
        "speed_rpm": float(curve_record.speed_rpm),
        "torque_nm": float(curve_record.torque_nm),
        "oil_temperature_deg": float(curve_record.oil_temperature_deg),
        "point_count": int(len(truth_array)),
        "training_like_sequence_count": int(len(training_like_target_index_array)),
        "full_mae_deg": full_metric_dictionary["mae_deg"],
        "full_offset_error_deg": full_metric_dictionary["absolute_offset_error_deg"],
        "full_centered_mae_deg": full_metric_dictionary["centered_mae_deg"],
        "sampled_full_mae_deg": sampled_full_metric_dictionary["mae_deg"],
        "sampled_full_offset_error_deg": sampled_full_metric_dictionary["absolute_offset_error_deg"],
        "sampled_full_centered_mae_deg": sampled_full_metric_dictionary["centered_mae_deg"],
        "training_like_mae_deg": training_like_metric_dictionary["mae_deg"],
        "training_like_offset_error_deg": training_like_metric_dictionary["absolute_offset_error_deg"],
        "training_like_centered_mae_deg": training_like_metric_dictionary["centered_mae_deg"],
        "truth_mean_deg": full_metric_dictionary["truth_mean_deg"],
        "full_prediction_mean_deg": full_metric_dictionary["prediction_mean_deg"],
        "training_like_prediction_mean_deg": training_like_metric_dictionary["prediction_mean_deg"],
    }


def summarize_row_list(row_list: list[dict[str, Any]]) -> dict[str, Any]:

    """Summarize numeric audit columns."""

    numeric_key_list = [
        "full_mae_deg",
        "full_offset_error_deg",
        "full_centered_mae_deg",
        "sampled_full_mae_deg",
        "sampled_full_offset_error_deg",
        "sampled_full_centered_mae_deg",
        "training_like_mae_deg",
        "training_like_offset_error_deg",
        "training_like_centered_mae_deg",
    ]
    summary_dictionary: dict[str, Any] = {"curve_count": len(row_list)}
    for numeric_key in numeric_key_list:
        value_array = np.asarray([float(row[numeric_key]) for row in row_list], dtype=np.float64)
        summary_dictionary[f"mean_{numeric_key}"] = float(np.mean(value_array))
        summary_dictionary[f"p95_{numeric_key}"] = float(np.percentile(value_array, 95))
    return summary_dictionary


def compute_datamodule_loader_metric_dictionary(
    model_object: TransmissionErrorRegressionModule,
    datamodule: TransmissionErrorDataModule,
) -> dict[str, Any]:

    """Evaluate the loaded checkpoint on the saved training-config test loader."""

    datamodule.setup("test")
    metric_sum_dictionary = {
        "absolute_error_sum": 0.0,
        "squared_error_sum": 0.0,
        "sample_count": 0,
    }
    direction_count_dictionary: dict[str, int] = {}
    source_path_list: list[str] = []
    inference_device = model_object.input_feature_mean.device
    with torch.no_grad():
        for batch_dictionary in datamodule.test_dataloader():
            input_tensor = batch_dictionary["input_tensor"].float().to(inference_device)
            target_tensor = batch_dictionary["target_tensor"].float().to(inference_device)
            normalized_input_tensor = model_object.normalize_input_tensor(input_tensor)
            normalized_prediction_tensor, _ = model_object.forward_regression_model(
                input_tensor,
                normalized_input_tensor,
            )
            deterministic_prediction_tensor = model_object.extract_deterministic_prediction_tensor(
                normalized_prediction_tensor
            )
            prediction_tensor = model_object.denormalize_target_tensor(deterministic_prediction_tensor)
            error_tensor = prediction_tensor - target_tensor
            metric_sum_dictionary["absolute_error_sum"] += float(torch.sum(torch.abs(error_tensor)).detach().cpu())
            metric_sum_dictionary["squared_error_sum"] += float(torch.sum(torch.square(error_tensor)).detach().cpu())
            metric_sum_dictionary["sample_count"] += int(error_tensor.numel())
            for direction_label in batch_dictionary.get("direction_label", []):
                direction_count_dictionary[str(direction_label)] = direction_count_dictionary.get(str(direction_label), 0) + 1
            for source_file_path in batch_dictionary.get("source_file_path", []):
                if len(source_path_list) < 12:
                    source_path_list.append(str(source_file_path))

    sample_count = int(metric_sum_dictionary["sample_count"])
    assert sample_count > 0, "Datamodule test loader produced no samples"
    return {
        "datamodule_test_sample_count": sample_count,
        "datamodule_test_mae_deg": metric_sum_dictionary["absolute_error_sum"] / sample_count,
        "datamodule_test_rmse_deg": float(np.sqrt(metric_sum_dictionary["squared_error_sum"] / sample_count)),
        "datamodule_test_direction_curve_count": direction_count_dictionary,
        "datamodule_test_source_path_preview": source_path_list,
        "datamodule_train_curve_count": len(datamodule.train_dataset or []),
        "datamodule_validation_curve_count": len(datamodule.validation_dataset or []),
        "datamodule_test_curve_count": len(datamodule.test_dataset or []),
    }


def build_report_markdown(
    output_directory: Path,
    config_path: Path,
    summary_dictionary: dict[str, Any],
    csv_path: Path,
) -> str:

    """Build the Markdown audit report."""

    return "\n".join(
        [
            "# Shape-Gate Pilot Track 2 Playback Contract Audit",
            "",
            "## Overview",
            "",
            "This diagnostic compares the existing Track 2 full-curve sequence",
            "playback against a training-like sequence-window playback for the",
            "`shape_gate_loss_pilot_periodic_gru_sequence_Fw` checkpoint.",
            "",
            "## Scope",
            "",
            f"- config: `{shared_training_infrastructure.format_project_relative_path(config_path)}`;",
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- per-curve CSV: `{shared_training_infrastructure.format_project_relative_path(csv_path)}`;",
            f"- curve count: `{summary_dictionary['curve_count']}`;",
            f"- datamodule test curve count: `{summary_dictionary['datamodule_test_curve_count']}`;",
            f"- datamodule test sample count: `{summary_dictionary['datamodule_test_sample_count']}`;",
            "",
            "## Mean Metrics",
            "",
            "| Playback | MAE [deg] | Offset Error [deg] | Centered MAE [deg] |",
            "| --- | ---: | ---: | ---: |",
            (
                f"| Saved-config datamodule test-loader | {summary_dictionary['datamodule_test_mae_deg']:.6f} | "
                "N/A | N/A |"
            ),
            (
                f"| Track 2 full curve | {summary_dictionary['mean_full_mae_deg']:.6f} | "
                f"{summary_dictionary['mean_full_offset_error_deg']:.6f} | "
                f"{summary_dictionary['mean_full_centered_mae_deg']:.6f} |"
            ),
            (
                f"| Track 2 sampled at training targets | {summary_dictionary['mean_sampled_full_mae_deg']:.6f} | "
                f"{summary_dictionary['mean_sampled_full_offset_error_deg']:.6f} | "
                f"{summary_dictionary['mean_sampled_full_centered_mae_deg']:.6f} |"
            ),
            (
                f"| Training-like valid windows | {summary_dictionary['mean_training_like_mae_deg']:.6f} | "
                f"{summary_dictionary['mean_training_like_offset_error_deg']:.6f} | "
                f"{summary_dictionary['mean_training_like_centered_mae_deg']:.6f} |"
            ),
            "",
            "## Interpretation",
            "",
            "- If the training-like row remains close to the full-curve row, the",
            "  checkpoint itself has an offset-dominated failure.",
            "- If the training-like row drops close to the training/test-loader MAE,",
            "  the Track 2 full-curve reconstruction path is not comparable to the",
            "  training evaluation contract and must be fixed or separately labeled.",
            "",
        ]
    )


def main() -> None:

    """Run the playback-contract audit."""

    arguments = build_argument_parser().parse_args()
    training_config = shared_training_infrastructure.apply_dataset_override(
        reference_family_vs_feedforward_support.load_reference_family_comparison_config(arguments.config_path),
        arguments.dataset,
    )
    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    candidate_configuration_list = (
        run_reference_family_vs_feedforward_comparison.filter_candidate_configuration_list_by_surface_scope(
            candidate_configuration_list,
            arguments.surface_scope,
        )
    )
    assert len(candidate_configuration_list) == 1, (
        f"Expected exactly one candidate for this audit | {len(candidate_configuration_list)}"
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
        arguments.surface_scope,
    )
    if arguments.max_curves > 0:
        curve_record_list = curve_record_list[:arguments.max_curves]

    candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration_list[0])
    assert isinstance(candidate.model_object, TransmissionErrorRegressionModule), (
        f"Expected Lightning registry candidate | {candidate.candidate_kind}"
    )

    row_list: list[dict[str, Any]] = []
    for curve_record in curve_record_list:
        full_prediction_array = reference_family_vs_feedforward_support.predict_wave1_registry_curve(
            candidate.model_object,
            candidate.training_config,
            curve_record,
        )
        training_like_target_index_array, training_like_prediction_array = predict_training_like_sequence_targets(
            candidate.model_object,
            curve_record,
            candidate.training_config,
        )
        row_list.append(
            build_audit_row(
                candidate.candidate_id,
                curve_record,
                full_prediction_array,
                training_like_target_index_array,
                training_like_prediction_array,
            )
        )

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.output_root)
    output_directory.mkdir(parents=True, exist_ok=True)
    csv_path = output_directory / "shape_gate_pilot_track2_playback_contract_audit.csv"
    summary_path = output_directory / "shape_gate_pilot_track2_playback_contract_audit.yaml"
    report_path = output_directory / "shape_gate_pilot_track2_playback_contract_audit.md"
    write_csv_row_list(csv_path, row_list)
    summary_dictionary = summarize_row_list(row_list)
    datamodule = shared_training_infrastructure.create_datamodule_from_training_config(candidate.training_config)
    summary_dictionary.update(
        compute_datamodule_loader_metric_dictionary(
            candidate.model_object,
            datamodule,
        )
    )
    summary_dictionary.update(
        {
            "config_path": shared_training_infrastructure.format_project_relative_path(arguments.config_path),
            "surface_scope": arguments.surface_scope,
            "csv_path": shared_training_infrastructure.format_project_relative_path(csv_path),
        }
    )
    with summary_path.open("w", encoding="utf-8", newline="\n") as summary_file:
        yaml.safe_dump(summary_dictionary, summary_file, sort_keys=False)
    report_path.write_text(
        build_report_markdown(output_directory, arguments.config_path, summary_dictionary, csv_path),
        encoding="utf-8",
        newline="\n",
    )
    print(f"[DONE] Playback contract audit written | {report_path}")


if __name__ == "__main__":
    main()
