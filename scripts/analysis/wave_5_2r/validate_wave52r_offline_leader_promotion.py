"""Validate K01 and H08 for conditional cross-surface promotion."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from datetime import datetime
import hashlib
from pathlib import Path
import sys
import time
from typing import Any, Callable

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import onnx
import onnxruntime as ort
import psutil
import torch
from torch import nn
import yaml

# Import Repository Campaign And Model Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)


# Define Immutable Candidate And Gate Paths
K01_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "temporal_analytical_residual_models"
    / "2026-07-29-19-21-15__stage9_k01"
)
H08_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-15__stage5_h08"
)
VALIDITY_ENVELOPE_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_causal_setpoint_validity_envelope.yaml"
)
OUTPUT_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_offline_leader_promotion"
)

# Define Numerical And Runtime Acceptance Thresholds
CURVE_MAX_ABS_TOLERANCE_DEG = 2.0e-6
COEFFICIENT_MAX_ABS_TOLERANCE_DEG = 1.0e-6
K01_CROSS_DEVICE_REPLAY_MAX_ABS_TOLERANCE_DEG = 5.0e-5
K01_HIDDEN_STATE_MAX_ABS_TOLERANCE = 2.0e-5
K01_CHUNK_EQUIVALENCE_MAX_ABS_TOLERANCE_DEG = 5.0e-5
K01_STATE_CARRY_MINIMUM_EFFECT_DEG = 1.0e-7
K01_EXPORT_CHUNK_LENGTH = 32
ONNX_OPSET_VERSION = 17
BENCHMARK_WARMUP_RUN_COUNT = 10
BENCHMARK_MEASURED_RUN_COUNT = 100
K01_FULL_CURVE_BENCHMARK_RUN_COUNT = 10
TARGET_ML_TASK_PERIOD_MICROSECONDS = 500.0


class H08OnnxWrapper(nn.Module):
    """Expose the H08 inspectable coefficient graph to ONNX."""

    def __init__(self, model_object: nn.Module) -> None:
        """Store the frozen H08 model."""

        super().__init__()
        self.model_object = model_object

    def forward(
        self,
        normalized_condition: torch.Tensor,
        analytical_anchor_coefficients: torch.Tensor,
    ) -> tuple[
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
    ]:
        """Return curve, coefficients, correction, and anchor contribution."""

        output = self.model_object(
            normalized_condition,
            analytical_anchor_coefficients,
        )
        return (
            output["prediction_curve"],
            output["prediction_coefficients"],
            output["coefficient_correction"],
            output["analytical_contribution_curve"],
        )


class K01StatefulOnnxWrapper(nn.Module):
    """Expose one explicit K01 causal state-carry step to ONNX."""

    def __init__(self, model_object: nn.Module) -> None:
        """Store the frozen K01 model."""

        super().__init__()
        self.model_object = model_object

    def forward(
        self,
        angular_position_deg: torch.Tensor,
        condition: torch.Tensor,
        analytical_anchor_curve: torch.Tensor,
        analytical_anchor_coefficients: torch.Tensor,
        hidden_state: torch.Tensor,
    ) -> tuple[
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
    ]:
        """Return causal outputs and the next explicit hidden state."""

        output = self.model_object.forward_sequence(
            angular_position_deg,
            condition,
            analytical_anchor_curve,
            analytical_anchor_coefficients,
            hidden_state,
        )
        return (
            output["prediction_curve"],
            output["residual_curve"],
            output["coefficient_correction"],
            output["predicted_coefficient"],
            output["final_hidden_state"],
        )


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def write_csv(
    output_path: Path,
    row_list: list[dict[str, Any]],
) -> None:
    """Write one stable CSV table."""

    assert row_list
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=list(row_list[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def compute_file_sha256(input_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def build_onnx_cpu_session(onnx_path: Path) -> ort.InferenceSession:
    """Create one deterministic single-thread CPU ONNX Runtime session."""

    session_options = ort.SessionOptions()
    session_options.intra_op_num_threads = 1
    session_options.inter_op_num_threads = 1
    session_options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
    return ort.InferenceSession(
        str(onnx_path),
        sess_options=session_options,
        providers=["CPUExecutionProvider"],
    )


def latency_summary_microseconds(
    latency_array: np.ndarray,
) -> dict[str, float]:
    """Summarize one latency distribution in microseconds."""

    assert latency_array.ndim == 1
    assert latency_array.size > 0
    return {
        "mean_microseconds": float(np.mean(latency_array)),
        "median_microseconds": float(np.median(latency_array)),
        "p95_microseconds": float(np.quantile(latency_array, 0.95)),
        "p99_microseconds": float(np.quantile(latency_array, 0.99)),
        "maximum_microseconds": float(np.max(latency_array)),
    }


def benchmark_callable(
    callable_object: Callable[[], Any],
    warmup_run_count: int,
    measured_run_count: int,
) -> dict[str, float]:
    """Benchmark one callable after an explicit warm-up."""

    for _ in range(warmup_run_count):
        callable_object()
    latency_list = []
    for _ in range(measured_run_count):
        start_time = time.perf_counter_ns()
        callable_object()
        elapsed_nanoseconds = time.perf_counter_ns() - start_time
        latency_list.append(elapsed_nanoseconds / 1000.0)
    return latency_summary_microseconds(
        np.asarray(latency_list, dtype=np.float64)
    )


def parameter_payload(model_object: nn.Module) -> dict[str, int]:
    """Return parameter count and static tensor-byte estimates."""

    parameter_count = sum(
        parameter.numel() for parameter in model_object.parameters()
    )
    parameter_byte_count = sum(
        parameter.numel() * parameter.element_size()
        for parameter in model_object.parameters()
    )
    buffer_byte_count = sum(
        buffer.numel() * buffer.element_size()
        for buffer in model_object.buffers()
    )
    return {
        "parameter_count": int(parameter_count),
        "parameter_byte_count": int(parameter_byte_count),
        "buffer_byte_count": int(buffer_byte_count),
        "static_tensor_byte_count": int(
            parameter_byte_count + buffer_byte_count
        ),
    }


def build_validity_test_payload(
    dataset: stage5.Stage5Dataset,
) -> dict[str, Any]:
    """Exercise finite and training-envelope fallback classification."""

    envelope_payload = read_yaml(VALIDITY_ENVELOPE_PATH)
    axis_bound_dictionary = envelope_payload["axis_bound_dictionary"]
    minimum_array = np.asarray(
        [
            axis_bound_dictionary["signed_setpoint_torque_nm"]["minimum"],
            axis_bound_dictionary["absolute_setpoint_speed_rpm"]["minimum"],
            axis_bound_dictionary["setpoint_temperature_deg_c"]["minimum"],
        ],
        dtype=np.float64,
    )
    maximum_array = np.asarray(
        [
            axis_bound_dictionary["signed_setpoint_torque_nm"]["maximum"],
            axis_bound_dictionary["absolute_setpoint_speed_rpm"]["maximum"],
            axis_bound_dictionary["setpoint_temperature_deg_c"]["maximum"],
        ],
        dtype=np.float64,
    )
    valid_condition = np.asarray(dataset.feature_mean, dtype=np.float64)
    test_condition_matrix = np.vstack(
        [
            valid_condition,
            [np.nan, valid_condition[1], valid_condition[2]],
            [minimum_array[0] - 1.0, valid_condition[1], valid_condition[2]],
            [valid_condition[0], maximum_array[1] + 1.0, valid_condition[2]],
            [valid_condition[0], valid_condition[1], maximum_array[2] + 1.0],
        ]
    )
    finite_mask = np.all(np.isfinite(test_condition_matrix), axis=1)
    inside_axis_mask = np.all(
        (test_condition_matrix >= minimum_array)
        & (test_condition_matrix <= maximum_array),
        axis=1,
    )
    accepted_mask = finite_mask & inside_axis_mask
    expected_mask = np.asarray([True, False, False, False, False])
    assert np.array_equal(accepted_mask, expected_mask)
    return {
        "validity_envelope_path": VALIDITY_ENVELOPE_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "validity_envelope_sha256": compute_file_sha256(
            VALIDITY_ENVELOPE_PATH
        ),
        "test_case_count": int(test_condition_matrix.shape[0]),
        "accepted_case_count": int(np.sum(accepted_mask)),
        "fallback_case_count": int(np.sum(~accepted_mask)),
        "finite_and_axis_bound_classification_passed": True,
        "deployment_rule": (
            "Reject non-finite or outside-axis inputs before model execution "
            "and route them to the incumbent or analytical fallback."
        ),
    }


def load_h08_model(
    dataset: stage5.Stage5Dataset,
) -> tuple[nn.Module, dict[str, Any]]:
    """Reconstruct H08 from its immutable checkpoint."""

    checkpoint_path = H08_RUN_DIRECTORY / "best_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    specification = next(
        candidate
        for candidate in stage5.build_candidate_list()
        if candidate.candidate_id == "H08"
    )
    model_object = stage5.build_model(specification, dataset)
    model_object.load_state_dict(
        checkpoint_payload["state_dict"],
        strict=True,
    )
    model_object.eval()
    assert checkpoint_payload["candidate"]["candidate_id"] == "H08"
    return model_object, checkpoint_payload


def validate_h08(
    dataset: stage5.Stage5Dataset,
    output_directory: Path,
) -> dict[str, Any]:
    """Validate H08 replay, export parity, and local runtime evidence."""

    model_object, checkpoint_payload = load_h08_model(dataset)
    checkpoint_path = H08_RUN_DIRECTORY / "best_model.pt"
    prediction_path = H08_RUN_DIRECTORY / "test_predictions.npz"
    frozen_prediction_payload = np.load(prediction_path)
    test_batch = stage5.tensor_dataset_for_split(
        dataset,
        "data_selected",
        "test",
        torch.device("cpu"),
    )

    # Reconstruct The Complete Frozen Forward Payload
    with torch.inference_mode():
        first_output = model_object(
            test_batch["condition"],
            test_batch["anchor"],
        )
        repeated_output = model_object(
            test_batch["condition"],
            test_batch["anchor"],
        )
    replay_curve_difference = float(
        np.max(
            np.abs(
                first_output["prediction_curve"].numpy()
                - frozen_prediction_payload["predicted_curve"]
            )
        )
    )
    replay_coefficient_difference = float(
        np.max(
            np.abs(
                first_output["prediction_coefficients"].numpy()
                - frozen_prediction_payload["predicted_coefficient"]
            )
        )
    )
    deterministic_difference = float(
        torch.max(
            torch.abs(
                first_output["prediction_curve"]
                - repeated_output["prediction_curve"]
            )
        )
    )
    assert replay_curve_difference <= CURVE_MAX_ABS_TOLERANCE_DEG
    assert (
        replay_coefficient_difference
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )
    assert deterministic_difference == 0.0

    # Export One Inspectable Coefficient And Reconstruction Graph
    model_wrapper = H08OnnxWrapper(model_object)
    model_wrapper.eval()
    onnx_path = output_directory / "h08_banded_coefficient_residual.onnx"
    torch.onnx.export(
        model_wrapper,
        (
            test_batch["condition"][:1],
            test_batch["anchor"][:1],
        ),
        onnx_path,
        input_names=[
            "normalized_condition",
            "analytical_anchor_coefficients",
        ],
        output_names=[
            "prediction_curve",
            "prediction_coefficients",
            "coefficient_correction",
            "analytical_contribution_curve",
        ],
        dynamic_axes={
            "normalized_condition": {0: "batch"},
            "analytical_anchor_coefficients": {0: "batch"},
            "prediction_curve": {0: "batch"},
            "prediction_coefficients": {0: "batch"},
            "coefficient_correction": {0: "batch"},
            "analytical_contribution_curve": {0: "batch"},
        },
        opset_version=ONNX_OPSET_VERSION,
        do_constant_folding=True,
        dynamo=False,
    )
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)

    # Validate ONNX Runtime On All 97 Frozen Test Conditions
    process_object = psutil.Process()
    rss_before_session_bytes = process_object.memory_info().rss
    onnx_session = build_onnx_cpu_session(onnx_path)
    rss_after_session_bytes = process_object.memory_info().rss
    onnx_output_list = onnx_session.run(
        None,
        {
            "normalized_condition": np.ascontiguousarray(
                test_batch["condition"].numpy()
            ),
            "analytical_anchor_coefficients": np.ascontiguousarray(
                test_batch["anchor"].numpy()
            ),
        },
    )
    rss_after_inference_bytes = process_object.memory_info().rss
    python_output_list = [
        first_output["prediction_curve"].numpy(),
        first_output["prediction_coefficients"].numpy(),
        first_output["coefficient_correction"].numpy(),
        first_output["analytical_contribution_curve"].numpy(),
    ]
    output_name_list = [
        "prediction_curve",
        "prediction_coefficients",
        "coefficient_correction",
        "analytical_contribution_curve",
    ]
    parity_dictionary = {}
    for output_name, python_array, onnx_array in zip(
        output_name_list,
        python_output_list,
        onnx_output_list,
        strict=True,
    ):
        assert python_array.shape == onnx_array.shape
        assert np.all(np.isfinite(onnx_array))
        parity_dictionary[output_name] = float(
            np.max(np.abs(python_array - onnx_array))
        )
    assert (
        parity_dictionary["prediction_curve"]
        <= CURVE_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        parity_dictionary["prediction_coefficients"]
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        parity_dictionary["coefficient_correction"]
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )

    # Benchmark One Condition-Level Coefficient And Curve Evaluation
    benchmark_input_dictionary = {
        "normalized_condition": np.ascontiguousarray(
            test_batch["condition"][:1].numpy()
        ),
        "analytical_anchor_coefficients": np.ascontiguousarray(
            test_batch["anchor"][:1].numpy()
        ),
    }
    latency_payload = benchmark_callable(
        lambda: onnx_session.run(None, benchmark_input_dictionary),
        BENCHMARK_WARMUP_RUN_COUNT,
        BENCHMARK_MEASURED_RUN_COUNT,
    )
    status = "passed_local_promotion_gates"
    return {
        "candidate_id": "wave52r_stage5_h08_seed_314159",
        "candidate_family": "banded_coefficient_residual",
        "candidate_lane": "non_temporal",
        "surface": "Fw",
        "status": status,
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "checkpoint_sha256": compute_file_sha256(checkpoint_path),
        "prediction_path": prediction_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "prediction_sha256": compute_file_sha256(prediction_path),
        "split_signature": checkpoint_payload.get(
            "split_signature",
            stage5.SPLIT_SIGNATURE,
        ),
        "condition_count": int(test_batch["condition"].shape[0]),
        "angular_sample_count": int(
            first_output["prediction_curve"].shape[1]
        ),
        "checkpoint_replay": {
            "curve_max_abs_difference_deg": replay_curve_difference,
            "coefficient_max_abs_difference_deg": (
                replay_coefficient_difference
            ),
            "deterministic_repeat_max_abs_difference_deg": (
                deterministic_difference
            ),
            "passed": True,
        },
        "onnx_export": {
            "onnx_path": onnx_path.relative_to(PROJECT_ROOT).as_posix(),
            "onnx_sha256": compute_file_sha256(onnx_path),
            "onnx_size_bytes": int(onnx_path.stat().st_size),
            "opset_version": ONNX_OPSET_VERSION,
            "output_max_abs_difference": parity_dictionary,
            "passed": True,
        },
        "runtime": {
            "scope": (
                "one condition-level coefficient and complete-curve "
                "reconstruction on Windows CPU"
            ),
            **latency_payload,
            "session_rss_delta_bytes": int(
                max(0, rss_after_session_bytes - rss_before_session_bytes)
            ),
            "inference_rss_delta_bytes": int(
                max(0, rss_after_inference_bytes - rss_after_session_bytes)
            ),
            "twincat_runtime_status": "pending",
        },
        "model": parameter_payload(model_object),
        "deployment_contract": {
            "condition_input_order": [
                "signed_setpoint_torque_nm",
                "absolute_setpoint_speed_rpm",
                "setpoint_temperature_deg_c",
            ],
            "inspectable_outputs": [
                "prediction_coefficients",
                "coefficient_correction",
                "analytical_contribution_curve",
                "prediction_curve",
            ],
            "future_information_required": False,
            "target_derived_runtime_input_count": 0,
            "preferred_plc_form": (
                "condition-to-coefficient graph plus explicit pointwise "
                "harmonic reconstruction"
            ),
        },
    }


def load_k01_model(
    dataset: stage5.Stage5Dataset,
) -> tuple[nn.Module, dict[str, Any], stage9.AnchorBundle]:
    """Reconstruct K01 and its frozen H04 anchor bundle."""

    checkpoint_path = K01_RUN_DIRECTORY / "best_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    specification = next(
        candidate
        for candidate in stage9.build_candidate_list()
        if candidate.candidate_id == "K01"
    )
    anchor_bundle = stage9.build_anchor_bundle(dataset)
    model_object = stage9.build_model(specification, dataset)
    model_object.load_state_dict(
        checkpoint_payload["state_dict"],
        strict=True,
    )
    model_object.eval()
    assert checkpoint_payload["candidate"]["candidate_id"] == "K01"
    return model_object, checkpoint_payload, anchor_bundle


def run_k01_onnx_curve(
    onnx_session: ort.InferenceSession,
    angular_position_array: np.ndarray,
    condition_array: np.ndarray,
    anchor_curve_array: np.ndarray,
    anchor_coefficient_array: np.ndarray,
    hidden_size: int,
    num_layers: int,
    reset_each_chunk: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    """Run one complete curve through the fixed-chunk ONNX state contract."""

    assert angular_position_array.shape == (
        stage5.ANGULAR_SAMPLE_COUNT,
    )
    assert stage5.ANGULAR_SAMPLE_COUNT % K01_EXPORT_CHUNK_LENGTH == 0
    hidden_state = np.zeros(
        (num_layers, 1, hidden_size),
        dtype=np.float32,
    )
    prediction_chunk_list = []
    for start_index in range(
        0,
        stage5.ANGULAR_SAMPLE_COUNT,
        K01_EXPORT_CHUNK_LENGTH,
    ):
        end_index = start_index + K01_EXPORT_CHUNK_LENGTH
        if reset_each_chunk:
            hidden_state.fill(0.0)
        output_list = onnx_session.run(
            None,
            {
                "angular_position_deg": np.ascontiguousarray(
                    angular_position_array[None, start_index:end_index]
                ),
                "condition": np.ascontiguousarray(
                    condition_array[None, :]
                ),
                "analytical_anchor_curve": np.ascontiguousarray(
                    anchor_curve_array[None, start_index:end_index]
                ),
                "analytical_anchor_coefficients": np.ascontiguousarray(
                    anchor_coefficient_array[None, :]
                ),
                "hidden_state": np.ascontiguousarray(hidden_state),
            },
        )
        prediction_chunk_list.append(output_list[0])
        hidden_state = output_list[4]
    return np.concatenate(prediction_chunk_list, axis=1), hidden_state


def validate_k01(
    dataset: stage5.Stage5Dataset,
    output_directory: Path,
) -> dict[str, Any]:
    """Validate K01 replay, causality, stateful export, and local runtime."""

    (
        model_object,
        checkpoint_payload,
        anchor_bundle,
    ) = load_k01_model(dataset)
    checkpoint_path = K01_RUN_DIRECTORY / "best_model.pt"
    prediction_path = K01_RUN_DIRECTORY / "test_predictions.npz"
    frozen_prediction_payload = np.load(prediction_path)
    specification = next(
        candidate
        for candidate in stage9.build_candidate_list()
        if candidate.candidate_id == "K01"
    )
    anchor_curve_matrix, anchor_coefficient_matrix = (
        stage9.anchor_arrays_for_candidate(
            specification,
            anchor_bundle,
        )
    )
    assert anchor_coefficient_matrix is not None
    test_batch = stage9.build_split_tensors(
        dataset,
        anchor_curve_matrix,
        anchor_coefficient_matrix,
        "test",
        torch.device("cpu"),
    )
    condition_tensor = test_batch["condition"]
    anchor_curve_tensor = test_batch["anchor"]
    anchor_coefficient_tensor = test_batch["anchor_coefficient"]
    angular_position_tensor = test_batch["angle"]
    assert isinstance(condition_tensor, torch.Tensor)
    assert isinstance(anchor_curve_tensor, torch.Tensor)
    assert isinstance(anchor_coefficient_tensor, torch.Tensor)
    assert isinstance(angular_position_tensor, torch.Tensor)

    # Reproduce The Original Chunk-33 Saved Prediction Contract
    (
        replay_prediction_matrix,
        _,
        recurrent_metric_payload,
    ) = stage9.predict_model(
        model_object,
        condition_tensor,
        anchor_curve_tensor,
        anchor_coefficient_tensor,
        angular_position_tensor,
        stage9.DEFAULT_CHUNK_LENGTH,
    )
    replay_absolute_difference = np.abs(
        replay_prediction_matrix
        - frozen_prediction_payload["predicted_curve"]
    )
    replay_curve_difference = float(
        np.max(replay_absolute_difference)
    )
    replay_curve_mean_difference = float(
        np.mean(replay_absolute_difference)
    )
    replay_curve_p99_difference = float(
        np.quantile(replay_absolute_difference, 0.99)
    )
    assert (
        replay_curve_difference
        <= K01_CROSS_DEVICE_REPLAY_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        recurrent_metric_payload[
            "reset_reproducibility_max_abs_deg"
        ]
        == 0.0
    )
    assert (
        recurrent_metric_payload["chunk_equivalence_max_abs_deg"]
        <= K01_CHUNK_EQUIVALENCE_MAX_ABS_TOLERANCE_DEG
    )

    # Prove Prefix Invariance Against A Mutated Future
    prefix_length = 129
    first_angle = angular_position_tensor[:1]
    first_condition = condition_tensor[:1]
    first_anchor_curve = anchor_curve_tensor[:1]
    first_anchor_coefficient = anchor_coefficient_tensor[:1]
    mutated_angle = first_angle.clone()
    mutated_anchor_curve = first_anchor_curve.clone()
    mutated_angle[:, prefix_length:] = torch.flip(
        mutated_angle[:, prefix_length:],
        dims=[1],
    )
    mutated_anchor_curve[:, prefix_length:] = torch.flip(
        mutated_anchor_curve[:, prefix_length:],
        dims=[1],
    )
    with torch.inference_mode():
        reference_output = model_object.forward_sequence(
            first_angle,
            first_condition,
            first_anchor_curve,
            first_anchor_coefficient,
        )
        mutated_output = model_object.forward_sequence(
            mutated_angle,
            first_condition,
            mutated_anchor_curve,
            first_anchor_coefficient,
        )
    prefix_invariance_difference = float(
        torch.max(
            torch.abs(
                reference_output["prediction_curve"][:, :prefix_length]
                - mutated_output["prediction_curve"][:, :prefix_length]
            )
        )
    )
    assert prefix_invariance_difference == 0.0

    # Export One Fixed-Chunk Stateful Streaming Graph
    model_wrapper = K01StatefulOnnxWrapper(model_object)
    model_wrapper.eval()
    onnx_path = output_directory / "k01_stateful_chunk32.onnx"
    export_hidden_state = model_object.initial_hidden_state(
        1,
        first_angle,
    )
    torch.onnx.export(
        model_wrapper,
        (
            first_angle[:, :K01_EXPORT_CHUNK_LENGTH],
            first_condition,
            first_anchor_curve[:, :K01_EXPORT_CHUNK_LENGTH],
            first_anchor_coefficient,
            export_hidden_state,
        ),
        onnx_path,
        input_names=[
            "angular_position_deg",
            "condition",
            "analytical_anchor_curve",
            "analytical_anchor_coefficients",
            "hidden_state",
        ],
        output_names=[
            "prediction_curve",
            "residual_curve",
            "coefficient_correction",
            "predicted_coefficient",
            "final_hidden_state",
        ],
        opset_version=ONNX_OPSET_VERSION,
        do_constant_folding=True,
        dynamo=False,
    )
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)

    # Compare Stateful PyTorch And ONNX Curves On All 97 Conditions
    process_object = psutil.Process()
    rss_before_session_bytes = process_object.memory_info().rss
    onnx_session = build_onnx_cpu_session(onnx_path)
    rss_after_session_bytes = process_object.memory_info().rss
    with torch.inference_mode():
        pytorch_chunk_output = model_object.forward_in_chunks(
            angular_position_tensor,
            condition_tensor,
            anchor_curve_tensor,
            anchor_coefficient_tensor,
            chunk_length=K01_EXPORT_CHUNK_LENGTH,
        )
    pytorch_prediction_matrix = (
        pytorch_chunk_output["prediction_curve"].numpy()
    )
    onnx_prediction_list = []
    onnx_final_hidden_list = []
    for condition_index in range(condition_tensor.shape[0]):
        onnx_prediction, onnx_final_hidden = run_k01_onnx_curve(
            onnx_session,
            angular_position_tensor[condition_index].numpy(),
            condition_tensor[condition_index].numpy(),
            anchor_curve_tensor[condition_index].numpy(),
            anchor_coefficient_tensor[condition_index].numpy(),
            model_object.hidden_size,
            model_object.num_layers,
        )
        onnx_prediction_list.append(onnx_prediction[0])
        onnx_final_hidden_list.append(onnx_final_hidden[:, 0, :])
    onnx_prediction_matrix = np.vstack(onnx_prediction_list)
    onnx_final_hidden_matrix = np.stack(onnx_final_hidden_list, axis=1)
    rss_after_inference_bytes = process_object.memory_info().rss
    curve_parity_difference = float(
        np.max(
            np.abs(
                pytorch_prediction_matrix
                - onnx_prediction_matrix
            )
        )
    )
    hidden_state_parity_difference = float(
        np.max(
            np.abs(
                pytorch_chunk_output["final_hidden_state"].numpy()
                - onnx_final_hidden_matrix
            )
        )
    )
    assert curve_parity_difference <= CURVE_MAX_ABS_TOLERANCE_DEG
    assert (
        hidden_state_parity_difference
        <= K01_HIDDEN_STATE_MAX_ABS_TOLERANCE
    )

    # Prove That Explicit State Carry Is Functionally Active
    stateful_prediction, _ = run_k01_onnx_curve(
        onnx_session,
        first_angle[0].numpy(),
        first_condition[0].numpy(),
        first_anchor_curve[0].numpy(),
        first_anchor_coefficient[0].numpy(),
        model_object.hidden_size,
        model_object.num_layers,
        reset_each_chunk=False,
    )
    reset_each_chunk_prediction, _ = run_k01_onnx_curve(
        onnx_session,
        first_angle[0].numpy(),
        first_condition[0].numpy(),
        first_anchor_curve[0].numpy(),
        first_anchor_coefficient[0].numpy(),
        model_object.hidden_size,
        model_object.num_layers,
        reset_each_chunk=True,
    )
    state_carry_effect = float(
        np.mean(
            np.abs(
                stateful_prediction
                - reset_each_chunk_prediction
            )
        )
    )
    assert state_carry_effect >= K01_STATE_CARRY_MINIMUM_EFFECT_DEG

    # Benchmark One Chunk And One Complete 2048-Sample Curve
    first_chunk_input_dictionary = {
        "angular_position_deg": np.ascontiguousarray(
            first_angle[:, :K01_EXPORT_CHUNK_LENGTH].numpy()
        ),
        "condition": np.ascontiguousarray(first_condition.numpy()),
        "analytical_anchor_curve": np.ascontiguousarray(
            first_anchor_curve[:, :K01_EXPORT_CHUNK_LENGTH].numpy()
        ),
        "analytical_anchor_coefficients": np.ascontiguousarray(
            first_anchor_coefficient.numpy()
        ),
        "hidden_state": np.zeros(
            (
                model_object.num_layers,
                1,
                model_object.hidden_size,
            ),
            dtype=np.float32,
        ),
    }
    chunk_latency_payload = benchmark_callable(
        lambda: onnx_session.run(
            None,
            first_chunk_input_dictionary,
        ),
        BENCHMARK_WARMUP_RUN_COUNT,
        BENCHMARK_MEASURED_RUN_COUNT,
    )
    full_curve_latency_payload = benchmark_callable(
        lambda: run_k01_onnx_curve(
            onnx_session,
            first_angle[0].numpy(),
            first_condition[0].numpy(),
            first_anchor_curve[0].numpy(),
            first_anchor_coefficient[0].numpy(),
            model_object.hidden_size,
            model_object.num_layers,
        ),
        2,
        K01_FULL_CURVE_BENCHMARK_RUN_COUNT,
    )
    chunk_target_proxy_passed = (
        chunk_latency_payload["p95_microseconds"]
        <= TARGET_ML_TASK_PERIOD_MICROSECONDS
    )
    status = "passed_local_promotion_gates"
    return {
        "candidate_id": "wave52r_stage9_k01",
        "candidate_family": "h04_coefficient_residual_gru",
        "candidate_lane": "temporal",
        "surface": "Fw",
        "status": status,
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "checkpoint_sha256": compute_file_sha256(checkpoint_path),
        "prediction_path": prediction_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "prediction_sha256": compute_file_sha256(prediction_path),
        "split_signature": checkpoint_payload["split_signature"],
        "condition_count": int(condition_tensor.shape[0]),
        "angular_sample_count": int(angular_position_tensor.shape[1]),
        "checkpoint_replay": {
            "curve_max_abs_difference_deg": replay_curve_difference,
            "curve_mean_abs_difference_deg": (
                replay_curve_mean_difference
            ),
            "curve_p99_abs_difference_deg": (
                replay_curve_p99_difference
            ),
            "cross_device_max_abs_tolerance_deg": (
                K01_CROSS_DEVICE_REPLAY_MAX_ABS_TOLERANCE_DEG
            ),
            "reference_payload_device": "cuda",
            "replay_device": "cpu",
            **recurrent_metric_payload,
            "prefix_mutated_future_length": int(prefix_length),
            "prefix_invariance_max_abs_difference_deg": (
                prefix_invariance_difference
            ),
            "passed": True,
        },
        "onnx_export": {
            "onnx_path": onnx_path.relative_to(PROJECT_ROOT).as_posix(),
            "onnx_sha256": compute_file_sha256(onnx_path),
            "onnx_size_bytes": int(onnx_path.stat().st_size),
            "opset_version": ONNX_OPSET_VERSION,
            "fixed_batch_size": 1,
            "fixed_chunk_length": K01_EXPORT_CHUNK_LENGTH,
            "curve_max_abs_difference_deg": curve_parity_difference,
            "hidden_state_max_abs_difference": (
                hidden_state_parity_difference
            ),
            "state_carry_effect_mae_deg": state_carry_effect,
            "passed": True,
        },
        "runtime": {
            "scope": "Windows CPU ONNX Runtime stateful streaming proxy",
            "chunk": chunk_latency_payload,
            "complete_2048_sample_curve": full_curve_latency_payload,
            "target_ml_task_period_microseconds": (
                TARGET_ML_TASK_PERIOD_MICROSECONDS
            ),
            "chunk_p95_within_target_proxy": chunk_target_proxy_passed,
            "session_rss_delta_bytes": int(
                max(0, rss_after_session_bytes - rss_before_session_bytes)
            ),
            "inference_rss_delta_bytes": int(
                max(0, rss_after_inference_bytes - rss_after_session_bytes)
            ),
            "twincat_runtime_status": "pending",
        },
        "model": parameter_payload(model_object),
        "deployment_contract": {
            "condition_input_order": [
                "signed_setpoint_torque_nm",
                "absolute_setpoint_speed_rpm",
                "setpoint_temperature_deg_c",
            ],
            "state_input": (
                f"float32[{model_object.num_layers},1,"
                f"{model_object.hidden_size}]"
            ),
            "state_reset_required_at_curve_start": True,
            "state_carry_required_between_chunks": True,
            "future_information_required": False,
            "target_derived_runtime_input_count": 0,
            "preferred_plc_form": (
                "fixed-chunk causal GRU with explicit hidden-state input "
                "and output"
            ),
        },
    }


def write_summary_report(
    output_directory: Path,
    summary_payload: dict[str, Any],
) -> Path:
    """Write one concise human-readable promotion-gate report."""

    k01_payload = summary_payload["candidate_result_dictionary"]["K01"]
    h08_payload = summary_payload["candidate_result_dictionary"]["H08"]
    report_path = output_directory / "promotion_gate_report.md"
    report_text = f"""# Wave 5.2R Offline Leader Promotion Gate Report

## Outcome

The local forward promotion gates completed with overall status
`{summary_payload["overall_status"]}`.

- K01: `{k01_payload["status"]}`;
- H08: `{h08_payload["status"]}`;
- incumbent periodic GRU and periodic harmonic MLP: preserved unchanged;
- TwinCAT runtime acceptance: pending;
- backward and global promotion: not yet evaluated.

## K01

- checkpoint replay maximum curve difference:
  `{k01_payload["checkpoint_replay"]["curve_max_abs_difference_deg"]:.9g} deg`;
- reset reproducibility maximum difference:
  `{k01_payload["checkpoint_replay"]["reset_reproducibility_max_abs_deg"]:.9g} deg`;
- chunk/full-sequence maximum difference:
  `{k01_payload["checkpoint_replay"]["chunk_equivalence_max_abs_deg"]:.9g} deg`;
- mutated-future prefix difference:
  `{k01_payload["checkpoint_replay"]["prefix_invariance_max_abs_difference_deg"]:.9g} deg`;
- ONNX curve maximum difference:
  `{k01_payload["onnx_export"]["curve_max_abs_difference_deg"]:.9g} deg`;
- ONNX hidden-state maximum difference:
  `{k01_payload["onnx_export"]["hidden_state_max_abs_difference"]:.9g}`;
- state-carry functional effect:
  `{k01_payload["onnx_export"]["state_carry_effect_mae_deg"]:.9g} deg`;
- ONNX chunk P95:
  `{k01_payload["runtime"]["chunk"]["p95_microseconds"]:.3f} us`;
- local `500 us` proxy:
  `{k01_payload["runtime"]["chunk_p95_within_target_proxy"]}`.

K01 is locally export-qualified with an explicit stateful causal interface.
This is not yet a TwinCAT runtime pass.

## H08

- checkpoint replay maximum curve difference:
  `{h08_payload["checkpoint_replay"]["curve_max_abs_difference_deg"]:.9g} deg`;
- checkpoint replay maximum coefficient difference:
  `{h08_payload["checkpoint_replay"]["coefficient_max_abs_difference_deg"]:.9g} deg`;
- deterministic repeated-run difference:
  `{h08_payload["checkpoint_replay"]["deterministic_repeat_max_abs_difference_deg"]:.9g} deg`;
- ONNX curve maximum difference:
  `{h08_payload["onnx_export"]["output_max_abs_difference"]["prediction_curve"]:.9g} deg`;
- ONNX coefficient maximum difference:
  `{h08_payload["onnx_export"]["output_max_abs_difference"]["prediction_coefficients"]:.9g} deg`;
- ONNX condition-level P95:
  `{h08_payload["runtime"]["p95_microseconds"]:.3f} us`.

H08 is locally export-qualified with inspectable harmonic coefficients and
explicit reconstruction outputs. This is not yet a TwinCAT runtime pass.

## Validity And Fallback

The shared input-envelope test classified
`{summary_payload["validity_and_fallback"]["test_case_count"]}` cases and
routed all non-finite or out-of-envelope inputs to fallback. The incumbent
models remain the required operational fallback until the new candidates pass
the remaining gates.

## Decision

Local Gates A through C are sufficient only to decide whether a candidate may
enter the conditional `Fw`, `Bw`, and `global` campaign. They do not authorize
global leadership by themselves.

The next allowed step is to prepare the approved cross-surface campaign package
for every candidate with status `passed_local_promotion_gates`, keeping the
periodic GRU and periodic harmonic MLP as frozen controls.
"""
    with report_path.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        output_file.write(report_text)
    return report_path


def validate_offline_leader_promotion(
    run_instance_id: str,
) -> dict[str, Any]:
    """Run all local promotion gates and persist their evidence."""

    output_directory = OUTPUT_ROOT_DIRECTORY / run_instance_id
    output_directory.mkdir(parents=True, exist_ok=False)
    torch.manual_seed(314159)
    torch.use_deterministic_algorithms(True, warn_only=True)
    torch.set_num_threads(1)

    # Rebuild The Frozen Dataset And Validate Shared Fallback Semantics
    dataset = stage5.build_stage5_dataset()
    validity_payload = build_validity_test_payload(dataset)

    # Validate Both New Offline Leaders Independently
    h08_payload = validate_h08(dataset, output_directory)
    k01_payload = validate_k01(dataset, output_directory)
    both_candidate_gate_passed = all(
        candidate_payload["status"] == "passed_local_promotion_gates"
        for candidate_payload in (k01_payload, h08_payload)
    )
    overall_status = (
        "qualified_for_conditional_cross_surface_campaign"
        if both_candidate_gate_passed
        else "one_or_more_local_promotion_gates_failed"
    )
    summary_payload = {
        "schema_version": 1,
        "generated_at": now_iso(),
        "run_instance_id": run_instance_id,
        "overall_status": overall_status,
        "scope": {
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "condition_count": 97,
            "angular_sample_count": stage5.ANGULAR_SAMPLE_COUNT,
            "split_signature": stage5.SPLIT_SIGNATURE,
        },
        "candidate_result_dictionary": {
            "K01": k01_payload,
            "H08": h08_payload,
        },
        "validity_and_fallback": validity_payload,
        "incumbent_preservation": {
            "temporal_incumbent": "periodic_gru_sequence",
            "non_temporal_incumbent": "periodic_mlp_harmonic",
            "artifact_or_registry_replacement_performed": False,
            "required_operational_fallback": True,
        },
        "promotion_boundary": {
            "forward_local_export_gate_completed": (
                both_candidate_gate_passed
            ),
            "twincat_runtime_completed": False,
            "backward_evaluated": False,
            "global_evaluated": False,
            "global_leader_promotion_allowed": False,
            "conditional_cross_surface_campaign_preparation_allowed": (
                both_candidate_gate_passed
            ),
        },
    }
    summary_path = output_directory / "promotion_gate_summary.yaml"
    write_yaml(summary_path, summary_payload)
    report_path = write_summary_report(
        output_directory,
        summary_payload,
    )
    artifact_row_list = [
        {
            "artifact_role": artifact_path.stem,
            "relative_path": artifact_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "size_bytes": artifact_path.stat().st_size,
            "sha256": compute_file_sha256(artifact_path),
        }
        for artifact_path in sorted(output_directory.iterdir())
        if artifact_path.is_file()
    ]
    write_csv(
        output_directory / "artifact_inventory.csv",
        artifact_row_list,
    )
    print(
        "[PASS] Wave 5.2R offline leader local promotion gates | "
        f"status={overall_status} | "
        f"output={output_directory.relative_to(PROJECT_ROOT).as_posix()}",
        flush=True,
    )
    print(
        report_path.relative_to(PROJECT_ROOT).as_posix(),
        flush=True,
    )
    return summary_payload


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Validate K01 and H08 replay, causality, ONNX parity, and "
            "local runtime evidence."
        )
    )
    parser.add_argument(
        "--run-instance-id",
        default="",
        help=(
            "Immutable output directory name. Defaults to a current "
            "timestamp plus the validation suffix."
        ),
    )
    return parser.parse_args()


def main() -> None:
    """Run the approved local promotion validation suite."""

    arguments = parse_arguments()
    run_instance_id = (
        arguments.run_instance_id.strip()
        or f"{now_timestamp()}__wave52r_offline_leader_promotion"
    )
    validate_offline_leader_promotion(run_instance_id)


if __name__ == "__main__":
    main()
