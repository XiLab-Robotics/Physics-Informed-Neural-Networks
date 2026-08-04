"""Export the selected Wave 5.2R A02 composition and validate parity."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from datetime import datetime
import hashlib
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import onnx
import onnxruntime as ort
import torch
from torch import nn
import yaml

# Import Project Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_integrated_specialist_model as integrated_campaign,
)


# Define The Frozen A02 Export Contract
CAMPAIGN_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "wave52r_integrated_specialist_model"
    / "campaigns"
    / "2026-08-02_wave52r_integrated_specialist_model"
    / "campaign.yaml"
)
A02_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "integrated_specialist_models"
    / "2026-08-03-17-49-51__a02__seed_314159"
)
A02_CHECKPOINT_PATH = A02_RUN_DIRECTORY / "best_model.pt"
A02_PREDICTION_PATH = A02_RUN_DIRECTORY / "test_predictions.npz"
OUTPUT_ROOT = (
    PROJECT_ROOT
    / "output"
    / "deployment"
    / "wave52r_integrated_specialist_a02"
)
ONNX_OPSET_VERSION = 17
ANGULAR_SAMPLE_COUNT = 2048
RECONSTRUCTION_MAX_ABS_TOLERANCE_DEG = 1.0e-6
ONNX_MAX_ABS_TOLERANCE_DEG = 2.0e-6
PLC_MAX_ABS_TOLERANCE_DEG = 5.0e-6


class A02CompositionOnnxWrapper(nn.Module):
    """Expose the selected A02 curve composition as fixed-shape tensors."""

    def __init__(self, a02_model: nn.Module) -> None:
        """Retain only the trained H08 gate and immutable normalization."""

        super().__init__()
        self.h08_gate_head = a02_model.h08_gate_head
        self.register_buffer(
            "condition_feature_mean",
            a02_model.condition_feature_mean.detach().clone(),
        )
        self.register_buffer(
            "condition_feature_scale",
            a02_model.condition_feature_scale.detach().clone(),
        )
        self.branch_bound_deg = float(a02_model.branch_bound_deg)

    def forward(
        self,
        condition: torch.Tensor,
        k01_prediction_curve: torch.Tensor,
        h08_prediction_curve: torch.Tensor,
        direction_flag: torch.Tensor,
    ) -> tuple[
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
    ]:
        """Return the final curve and every deployment-facing intermediate."""

        normalized_condition = (
            condition - self.condition_feature_mean
        ) / self.condition_feature_scale
        learned_h08_gate = torch.tanh(
            self.h08_gate_head(normalized_condition)
        )
        forward_gate = (direction_flag > 0.0).to(
            k01_prediction_curve.dtype
        )
        k01_mean = torch.mean(
            k01_prediction_curve,
            dim=1,
            keepdim=True,
        )
        h08_mean = torch.mean(
            h08_prediction_curve,
            dim=1,
            keepdim=True,
        )
        k01_centered_curve = k01_prediction_curve - k01_mean
        h08_centered_curve = h08_prediction_curve - h08_mean
        h08_centered_difference = (
            h08_centered_curve - k01_centered_curve
        )
        h08_centered_residual = torch.clamp(
            forward_gate * learned_h08_gate * h08_centered_difference,
            -self.branch_bound_deg,
            self.branch_bound_deg,
        )
        prediction_curve = k01_prediction_curve + h08_centered_residual
        return (
            prediction_curve,
            k01_mean,
            h08_mean,
            k01_centered_curve,
            h08_centered_difference,
            learned_h08_gate,
            forward_gate,
            h08_centered_residual,
        )


def parse_arguments() -> argparse.Namespace:
    """Parse the optional immutable output-directory override."""

    parser = argparse.ArgumentParser(
        description=(
            "Export the selected A02 curve composer and validate exact, "
            "ONNX Runtime, and PLC-reference parity."
        )
    )
    parser.add_argument(
        "--output-directory",
        type=Path,
        help=(
            "Repository-relative output directory. Defaults to one "
            "timestamped run under output/deployment/."
        ),
    )
    return parser.parse_args()


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write one stable CSV table."""

    assert row_list
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        csv_writer = csv.DictWriter(
            output_file,
            fieldnames=list(row_list[0]),
            lineterminator="\n",
        )
        csv_writer.writeheader()
        csv_writer.writerows(row_list)


def compute_file_sha256(file_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def resolve_output_directory(argument: Path | None) -> Path:
    """Resolve one immutable output directory."""

    if argument is not None:
        output_directory = (
            argument
            if argument.is_absolute()
            else PROJECT_ROOT / argument
        )
    else:
        timestamp = datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")
        output_directory = OUTPUT_ROOT / f"{timestamp}__a02_export_parity"
    if output_directory.exists():
        raise FileExistsError(output_directory)
    output_directory.mkdir(parents=True)
    return output_directory


def build_frozen_test_payload(
    campaign_configuration: dict[str, Any],
) -> dict[str, np.ndarray | Any]:
    """Replay exact K01/H08 ingredients on the official 194 test curves."""

    dataset_dictionary = integrated_campaign.load_all_dataset_dictionary()
    global_dataset = dataset_dictionary["global"]
    forward_dataset = dataset_dictionary["Fw"]
    global_test_index = np.flatnonzero(global_dataset.split_array == "test")
    forward_test_index = np.flatnonzero(forward_dataset.split_array == "test")
    assert global_test_index.size == 194
    assert forward_test_index.size == 97

    checkpoint_contract = campaign_configuration[
        "frozen_checkpoint_contract"
    ]
    global_k01_curve, _ = integrated_campaign.predict_k01(
        global_dataset,
        PROJECT_ROOT / checkpoint_contract["global_h04"],
        PROJECT_ROOT / checkpoint_contract["global_k01"],
        global_test_index,
    )
    forward_h08_curve = integrated_campaign.predict_h08(
        forward_dataset,
        PROJECT_ROOT / checkpoint_contract["fw_h08"],
        forward_test_index,
    )

    forward_h08_by_condition_id = {
        f"{forward_dataset.condition_id_list[index]}__Fw": curve
        for index, curve in zip(
            forward_test_index.tolist(),
            forward_h08_curve,
            strict=True,
        )
    }
    global_test_condition_id = np.asarray(
        [global_dataset.condition_id_list[index] for index in global_test_index],
        dtype=str,
    )
    aligned_h08_curve = np.zeros_like(global_k01_curve, dtype=np.float32)
    for global_index, condition_id in enumerate(
        global_test_condition_id.tolist()
    ):
        if condition_id.endswith("__Fw"):
            aligned_h08_curve[global_index] = (
                forward_h08_by_condition_id[condition_id]
            )

    condition_matrix = global_dataset.condition_matrix[
        global_test_index
    ].astype(np.float32)
    direction_flag = condition_matrix[:, 3:4].astype(np.float32)
    assert np.all(np.isin(direction_flag, [-1.0, 1.0]))
    return {
        "dataset": global_dataset,
        "condition_id": global_test_condition_id,
        "condition": condition_matrix,
        "direction_flag": direction_flag,
        "k01_prediction_curve": global_k01_curve.astype(np.float32),
        "h08_prediction_curve": aligned_h08_curve,
        "measured_curve": global_dataset.curve_matrix[
            global_test_index
        ].astype(np.float64),
    }


def build_selected_a02_model(dataset: Any) -> nn.Module:
    """Load the exact selected A02 checkpoint with strict key matching."""

    a02_model = integrated_campaign.build_model(dataset, "A02")
    checkpoint = torch.load(
        A02_CHECKPOINT_PATH,
        map_location="cpu",
        weights_only=False,
    )
    assert checkpoint["ablation_id"] == "A02"
    assert int(checkpoint["random_seed"]) == 314159
    a02_model.load_state_dict(checkpoint["state_dict"], strict=True)
    a02_model.eval()
    return a02_model


def run_onnx_session(
    onnx_path: Path,
    payload: dict[str, np.ndarray | Any],
) -> list[np.ndarray]:
    """Run the fixed-batch ONNX graph over every official test condition."""

    session_options = ort.SessionOptions()
    session_options.intra_op_num_threads = 1
    session_options.inter_op_num_threads = 1
    onnx_session = ort.InferenceSession(
        str(onnx_path),
        sess_options=session_options,
        providers=["CPUExecutionProvider"],
    )
    output_batch_list: list[list[np.ndarray]] = []
    for condition_index in range(len(payload["condition_id"])):
        output_batch_list.append(
            onnx_session.run(
                None,
                {
                    "condition": payload["condition"][
                        condition_index : condition_index + 1
                    ],
                    "k01_prediction_curve": payload[
                        "k01_prediction_curve"
                    ][condition_index : condition_index + 1],
                    "h08_prediction_curve": payload[
                        "h08_prediction_curve"
                    ][condition_index : condition_index + 1],
                    "direction_flag": payload["direction_flag"][
                        condition_index : condition_index + 1
                    ],
                },
            )
        )
    return [
        np.concatenate(
            [batch_output[output_index] for batch_output in output_batch_list],
            axis=0,
        )
        for output_index in range(len(output_batch_list[0]))
    ]


def linear_float32(
    input_matrix: np.ndarray,
    weight_matrix: np.ndarray,
    bias_array: np.ndarray,
) -> np.ndarray:
    """Apply one explicit PLC-like REAL dense layer."""

    input_array = np.asarray(input_matrix, dtype=np.float32)
    weight_array = np.asarray(weight_matrix, dtype=np.float32)
    resolved_bias = np.asarray(bias_array, dtype=np.float32)
    output_matrix = np.empty(
        (input_array.shape[0], weight_array.shape[0]),
        dtype=np.float32,
    )
    for sample_index in range(input_array.shape[0]):
        for output_index in range(weight_array.shape[0]):
            accumulator = np.float32(resolved_bias[output_index])
            for input_index in range(weight_array.shape[1]):
                accumulator = np.float32(
                    accumulator
                    + np.float32(
                        input_array[sample_index, input_index]
                        * weight_array[output_index, input_index]
                    )
                )
            output_matrix[sample_index, output_index] = accumulator
    return output_matrix


def mean_float32(curve_matrix: np.ndarray) -> np.ndarray:
    """Compute a deterministic sequential REAL mean for each full curve."""

    curve_array = np.asarray(curve_matrix, dtype=np.float32)
    mean_array = np.empty((curve_array.shape[0], 1), dtype=np.float32)
    divisor = np.float32(curve_array.shape[1])
    for curve_index in range(curve_array.shape[0]):
        accumulator = np.float32(0.0)
        for sample_value in curve_array[curve_index]:
            accumulator = np.float32(accumulator + sample_value)
        mean_array[curve_index, 0] = np.float32(accumulator / divisor)
    return mean_array


def run_plc_reference(
    wrapper: A02CompositionOnnxWrapper,
    payload: dict[str, np.ndarray | Any],
) -> list[np.ndarray]:
    """Evaluate A02 with independent IEC REAL-like float32 arithmetic."""

    state_dictionary = wrapper.state_dict()
    condition = np.asarray(payload["condition"], dtype=np.float32)
    normalized_condition = np.asarray(
        (
            condition
            - state_dictionary["condition_feature_mean"].cpu().numpy()
        )
        / state_dictionary["condition_feature_scale"].cpu().numpy(),
        dtype=np.float32,
    )
    hidden = np.tanh(
        linear_float32(
            normalized_condition,
            state_dictionary["h08_gate_head.0.weight"].cpu().numpy(),
            state_dictionary["h08_gate_head.0.bias"].cpu().numpy(),
        )
    ).astype(np.float32)
    learned_h08_gate = np.tanh(
        linear_float32(
            hidden,
            state_dictionary["h08_gate_head.2.weight"].cpu().numpy(),
            state_dictionary["h08_gate_head.2.bias"].cpu().numpy(),
        )
    ).astype(np.float32)
    direction_flag = np.asarray(payload["direction_flag"], dtype=np.float32)
    forward_gate = (direction_flag > 0.0).astype(np.float32)
    k01_curve = np.asarray(
        payload["k01_prediction_curve"],
        dtype=np.float32,
    )
    h08_curve = np.asarray(
        payload["h08_prediction_curve"],
        dtype=np.float32,
    )
    k01_mean = mean_float32(k01_curve)
    h08_mean = mean_float32(h08_curve)
    k01_centered = np.asarray(k01_curve - k01_mean, dtype=np.float32)
    h08_centered = np.asarray(h08_curve - h08_mean, dtype=np.float32)
    h08_difference = np.asarray(
        h08_centered - k01_centered,
        dtype=np.float32,
    )
    residual = np.asarray(
        forward_gate * learned_h08_gate * h08_difference,
        dtype=np.float32,
    )
    residual = np.clip(
        residual,
        np.float32(-wrapper.branch_bound_deg),
        np.float32(wrapper.branch_bound_deg),
    ).astype(np.float32)
    prediction = np.asarray(k01_curve + residual, dtype=np.float32)
    return [
        prediction,
        k01_mean,
        h08_mean,
        k01_centered,
        h08_difference,
        learned_h08_gate,
        forward_gate,
        residual,
    ]


def build_parameter_st(wrapper: A02CompositionOnnxWrapper) -> str:
    """Render the trained A02 gate constants as inspectable Structured Text."""

    state_dictionary = wrapper.state_dict()

    def real_literal(value: float) -> str:
        return f"{float(np.float32(value)):.9e}"

    def real_array(name: str, value_array: np.ndarray) -> str:
        flattened = np.asarray(value_array, dtype=np.float32).reshape(-1)
        values = ", ".join(real_literal(value) for value in flattened)
        return (
            f"    {name} : ARRAY[0..{flattened.size - 1}] OF REAL := "
            f"[{values}];"
        )

    declaration_list = [
        "{attribute 'qualified_only'}",
        "VAR_GLOBAL CONSTANT",
        real_array(
            "A02_CONDITION_MEAN",
            state_dictionary["condition_feature_mean"].cpu().numpy(),
        ),
        real_array(
            "A02_CONDITION_SCALE",
            state_dictionary["condition_feature_scale"].cpu().numpy(),
        ),
        real_array(
            "A02_GATE_LAYER_0_WEIGHT",
            state_dictionary["h08_gate_head.0.weight"].cpu().numpy(),
        ),
        real_array(
            "A02_GATE_LAYER_0_BIAS",
            state_dictionary["h08_gate_head.0.bias"].cpu().numpy(),
        ),
        real_array(
            "A02_GATE_LAYER_2_WEIGHT",
            state_dictionary["h08_gate_head.2.weight"].cpu().numpy(),
        ),
        real_array(
            "A02_GATE_LAYER_2_BIAS",
            state_dictionary["h08_gate_head.2.bias"].cpu().numpy(),
        ),
        f"    A02_BRANCH_BOUND_DEG : REAL := {real_literal(wrapper.branch_bound_deg)};",
        "END_VAR",
    ]
    return "\n".join(declaration_list) + "\n"


def build_composer_st() -> str:
    """Render the fixed-curve A02 PLC reference function block."""

    return """FUNCTION_BLOCK FB_Wave52rA02CurveComposer
VAR_INPUT
    aCondition : ARRAY[0..3] OF REAL;
    aK01PredictionCurve : ARRAY[0..2047] OF REAL;
    aH08PredictionCurve : ARRAY[0..2047] OF REAL;
    fDirectionFlag : REAL;
    bExecute : BOOL;
END_VAR
VAR_OUTPUT
    aPredictionCurve : ARRAY[0..2047] OF REAL;
    aH08CenteredResidual : ARRAY[0..2047] OF REAL;
    fK01Mean : REAL;
    fH08Mean : REAL;
    fLearnedH08Gate : REAL;
    fForwardGate : REAL;
    bValid : BOOL;
END_VAR
VAR
    aNormalizedCondition : ARRAY[0..3] OF REAL;
    aHidden : ARRAY[0..11] OF REAL;
    fAccumulator : REAL;
    fCenteredDifference : REAL;
    fResidual : REAL;
    nInputIndex : INT;
    nOutputIndex : INT;
    nCurveIndex : INT;
END_VAR

bValid := FALSE;
IF bExecute THEN
    fK01Mean := 0.0;
    fH08Mean := 0.0;
    FOR nCurveIndex := 0 TO 2047 DO
        fK01Mean := fK01Mean + aK01PredictionCurve[nCurveIndex];
        fH08Mean := fH08Mean + aH08PredictionCurve[nCurveIndex];
    END_FOR
    fK01Mean := fK01Mean / 2048.0;
    fH08Mean := fH08Mean / 2048.0;

    FOR nInputIndex := 0 TO 3 DO
        aNormalizedCondition[nInputIndex] :=
            (aCondition[nInputIndex]
            - GVL_Wave52rA02Parameters.A02_CONDITION_MEAN[nInputIndex])
            / GVL_Wave52rA02Parameters.A02_CONDITION_SCALE[nInputIndex];
    END_FOR
    FOR nOutputIndex := 0 TO 11 DO
        fAccumulator :=
            GVL_Wave52rA02Parameters.A02_GATE_LAYER_0_BIAS[nOutputIndex];
        FOR nInputIndex := 0 TO 3 DO
            fAccumulator := fAccumulator
                + aNormalizedCondition[nInputIndex]
                * GVL_Wave52rA02Parameters.A02_GATE_LAYER_0_WEIGHT[
                    nOutputIndex * 4 + nInputIndex
                ];
        END_FOR
        aHidden[nOutputIndex] := TANH(fAccumulator);
    END_FOR
    fAccumulator := GVL_Wave52rA02Parameters.A02_GATE_LAYER_2_BIAS[0];
    FOR nInputIndex := 0 TO 11 DO
        fAccumulator := fAccumulator
            + aHidden[nInputIndex]
            * GVL_Wave52rA02Parameters.A02_GATE_LAYER_2_WEIGHT[nInputIndex];
    END_FOR
    fLearnedH08Gate := TANH(fAccumulator);
    IF fDirectionFlag > 0.0 THEN fForwardGate := 1.0; ELSE fForwardGate := 0.0; END_IF

    FOR nCurveIndex := 0 TO 2047 DO
        fCenteredDifference :=
            (aH08PredictionCurve[nCurveIndex] - fH08Mean)
            - (aK01PredictionCurve[nCurveIndex] - fK01Mean);
        fResidual := fForwardGate * fLearnedH08Gate * fCenteredDifference;
        fResidual := LIMIT(
            -GVL_Wave52rA02Parameters.A02_BRANCH_BOUND_DEG,
            fResidual,
            GVL_Wave52rA02Parameters.A02_BRANCH_BOUND_DEG
        );
        aH08CenteredResidual[nCurveIndex] := fResidual;
        aPredictionCurve[nCurveIndex] :=
            aK01PredictionCurve[nCurveIndex] + fResidual;
    END_FOR
    bValid := TRUE;
END_IF
"""


def run_export_and_validation(output_directory: Path) -> dict[str, Any]:
    """Build the A02 package and prove all host-side parity layers."""

    campaign_configuration = read_yaml(CAMPAIGN_CONFIG_PATH)
    payload = build_frozen_test_payload(campaign_configuration)
    a02_model = build_selected_a02_model(payload["dataset"])
    wrapper = A02CompositionOnnxWrapper(a02_model)
    wrapper.eval()

    torch_input_tuple = (
        torch.as_tensor(payload["condition"], dtype=torch.float32),
        torch.as_tensor(
            payload["k01_prediction_curve"],
            dtype=torch.float32,
        ),
        torch.as_tensor(
            payload["h08_prediction_curve"],
            dtype=torch.float32,
        ),
        torch.as_tensor(payload["direction_flag"], dtype=torch.float32),
    )
    with torch.inference_mode():
        python_output_tuple = wrapper(*torch_input_tuple)
    python_output_list = [
        output.detach().cpu().numpy() for output in python_output_tuple
    ]

    with np.load(A02_PREDICTION_PATH) as campaign_prediction:
        campaign_prediction_curve = campaign_prediction[
            "prediction_curve"
        ].astype(np.float32)
        campaign_measured_curve = campaign_prediction[
            "measured_curve"
        ].astype(np.float64)
        campaign_k01_curve = campaign_prediction[
            "k01_baseline_curve"
        ].astype(np.float32)
        campaign_residual = campaign_prediction[
            "h08_centered_residual"
        ].astype(np.float32)
    assert campaign_prediction_curve.shape == (194, ANGULAR_SAMPLE_COUNT)
    measured_alignment_max_abs_deg = float(
        np.max(
            np.abs(
                campaign_measured_curve
                - np.asarray(payload["measured_curve"], dtype=np.float64)
            )
        )
    )
    k01_replay_max_abs_deg = float(
        np.max(
            np.abs(
                campaign_k01_curve
                - np.asarray(payload["k01_prediction_curve"])
            )
        )
    )
    reconstruction_max_abs_deg = float(
        np.max(np.abs(campaign_prediction_curve - python_output_list[0]))
    )
    residual_reconstruction_max_abs_deg = float(
        np.max(np.abs(campaign_residual - python_output_list[7]))
    )
    assert measured_alignment_max_abs_deg == 0.0
    assert k01_replay_max_abs_deg <= RECONSTRUCTION_MAX_ABS_TOLERANCE_DEG
    assert reconstruction_max_abs_deg <= RECONSTRUCTION_MAX_ABS_TOLERANCE_DEG
    assert (
        residual_reconstruction_max_abs_deg
        <= RECONSTRUCTION_MAX_ABS_TOLERANCE_DEG
    )

    # Export One Fixed-Batch Composition Graph For TF3820 Compatibility
    onnx_path = output_directory / "wave52r_integrated_a02_curve_composer.onnx"
    torch.onnx.export(
        wrapper,
        tuple(value[:1] for value in torch_input_tuple),
        onnx_path,
        input_names=[
            "condition",
            "k01_prediction_curve",
            "h08_prediction_curve",
            "direction_flag",
        ],
        output_names=[
            "prediction_curve",
            "k01_mean",
            "h08_mean",
            "k01_centered_curve",
            "h08_centered_difference",
            "learned_h08_gate",
            "forward_gate",
            "h08_centered_residual",
        ],
        opset_version=ONNX_OPSET_VERSION,
        dynamo=False,
    )
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    onnx_output_list = run_onnx_session(onnx_path, payload)
    plc_output_list = run_plc_reference(wrapper, payload)

    output_name_list = [
        "prediction_curve",
        "k01_mean",
        "h08_mean",
        "k01_centered_curve",
        "h08_centered_difference",
        "learned_h08_gate",
        "forward_gate",
        "h08_centered_residual",
    ]
    onnx_max_abs_by_output = {}
    plc_max_abs_by_output = {}
    for output_name, python_output, onnx_output, plc_output in zip(
        output_name_list,
        python_output_list,
        onnx_output_list,
        plc_output_list,
        strict=True,
    ):
        assert python_output.shape == onnx_output.shape == plc_output.shape
        assert np.all(np.isfinite(onnx_output))
        assert np.all(np.isfinite(plc_output))
        onnx_max_abs_by_output[output_name] = float(
            np.max(np.abs(python_output - onnx_output))
        )
        plc_max_abs_by_output[output_name] = float(
            np.max(np.abs(python_output - plc_output))
        )
    assert max(onnx_max_abs_by_output.values()) <= ONNX_MAX_ABS_TOLERANCE_DEG
    assert max(plc_max_abs_by_output.values()) <= PLC_MAX_ABS_TOLERANCE_DEG

    backward_mask = np.asarray(payload["direction_flag"])[:, 0] < 0.0
    backward_residual_abs_max_deg = float(
        np.max(np.abs(python_output_list[7][backward_mask]))
    )
    backward_prediction_k01_abs_max_deg = float(
        np.max(
            np.abs(
                python_output_list[0][backward_mask]
                - np.asarray(payload["k01_prediction_curve"])[backward_mask]
            )
        )
    )
    assert backward_residual_abs_max_deg == 0.0
    assert backward_prediction_k01_abs_max_deg == 0.0

    # Persist Reproducible Test Vectors And PLC Reference Sources
    input_payload_path = output_directory / "a02_export_test_vectors.npz"
    np.savez_compressed(
        input_payload_path,
        condition_id=np.asarray(payload["condition_id"]),
        condition=np.asarray(payload["condition"]),
        direction_flag=np.asarray(payload["direction_flag"]),
        k01_prediction_curve=np.asarray(payload["k01_prediction_curve"]),
        h08_prediction_curve=np.asarray(payload["h08_prediction_curve"]),
        expected_prediction_curve=python_output_list[0],
        expected_h08_centered_residual=python_output_list[7],
        expected_learned_h08_gate=python_output_list[5],
    )
    gate_parameter_path = output_directory / "a02_gate_parameters.npz"
    np.savez_compressed(
        gate_parameter_path,
        **{
            state_name.replace(".", "__"): state_tensor.cpu().numpy()
            for state_name, state_tensor in wrapper.state_dict().items()
        },
        branch_bound_deg=np.asarray(
            [wrapper.branch_bound_deg],
            dtype=np.float32,
        ),
    )
    parameter_st_path = output_directory / "GVL_Wave52rA02Parameters.st"
    parameter_st_path.write_text(
        build_parameter_st(wrapper),
        encoding="utf-8",
        newline="\n",
    )
    composer_st_path = output_directory / "FB_Wave52rA02CurveComposer.st"
    composer_st_path.write_text(
        build_composer_st(),
        encoding="utf-8",
        newline="\n",
    )

    per_condition_row_list = []
    for condition_index, condition_id in enumerate(
        np.asarray(payload["condition_id"]).tolist()
    ):
        per_condition_row_list.append(
            {
                "condition_id": condition_id,
                "surface": (
                    "Fw" if payload["direction_flag"][condition_index, 0] > 0
                    else "Bw"
                ),
                "learned_h08_gate": float(
                    python_output_list[5][condition_index, 0]
                ),
                "residual_abs_max_deg": float(
                    np.max(np.abs(python_output_list[7][condition_index]))
                ),
                "reconstruction_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            campaign_prediction_curve[condition_index]
                            - python_output_list[0][condition_index]
                        )
                    )
                ),
                "onnx_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_output_list[0][condition_index]
                            - onnx_output_list[0][condition_index]
                        )
                    )
                ),
                "plc_reference_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_output_list[0][condition_index]
                            - plc_output_list[0][condition_index]
                        )
                    )
                ),
            }
        )
    per_condition_path = output_directory / "a02_parity_per_condition.csv"
    write_csv(per_condition_path, per_condition_row_list)

    source_checkpoint_dictionary = {
        "a02": A02_CHECKPOINT_PATH,
        "global_k01": PROJECT_ROOT
        / campaign_configuration["frozen_checkpoint_contract"]["global_k01"],
        "global_h04_anchor": PROJECT_ROOT
        / campaign_configuration["frozen_checkpoint_contract"]["global_h04"],
        "forward_h08": PROJECT_ROOT
        / campaign_configuration["frozen_checkpoint_contract"]["fw_h08"],
    }
    summary = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "status": "passed",
        "candidate_id": "wave52r_integrated_a02_seed_314159",
        "export_topology": "explicit_k01_h08_a02_curve_composition",
        "surface_contract": {
            "Fw": "global_k01_plus_forward_centered_h08_residual",
            "Bw": "global_k01_exact_replay",
            "global": "direction_routed_Fw_and_Bw_contract",
        },
        "condition_count": int(len(payload["condition_id"])),
        "forward_condition_count": int(np.sum(~backward_mask)),
        "backward_condition_count": int(np.sum(backward_mask)),
        "angular_sample_count": ANGULAR_SAMPLE_COUNT,
        "input_shape": {
            "condition": [1, 4],
            "k01_prediction_curve": [1, ANGULAR_SAMPLE_COUNT],
            "h08_prediction_curve": [1, ANGULAR_SAMPLE_COUNT],
            "direction_flag": [1, 1],
        },
        "onnx_opset_version": ONNX_OPSET_VERSION,
        "checkpoint_sha256": {
            name: compute_file_sha256(path)
            for name, path in source_checkpoint_dictionary.items()
        },
        "artifact_path": {
            "onnx": onnx_path.relative_to(PROJECT_ROOT).as_posix(),
            "test_vectors": input_payload_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "gate_parameters": gate_parameter_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "parameter_st": parameter_st_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "composer_st": composer_st_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "per_condition_parity": per_condition_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
        },
        "artifact_sha256": {
            path_name: compute_file_sha256(path)
            for path_name, path in {
                "onnx": onnx_path,
                "test_vectors": input_payload_path,
                "gate_parameters": gate_parameter_path,
                "parameter_st": parameter_st_path,
                "composer_st": composer_st_path,
                "per_condition_parity": per_condition_path,
            }.items()
        },
        "parity": {
            "measured_alignment_max_abs_deg": measured_alignment_max_abs_deg,
            "k01_replay_max_abs_deg": k01_replay_max_abs_deg,
            "campaign_reconstruction_max_abs_deg": reconstruction_max_abs_deg,
            "campaign_residual_reconstruction_max_abs_deg": (
                residual_reconstruction_max_abs_deg
            ),
            "onnx_max_abs_by_output": onnx_max_abs_by_output,
            "plc_reference_max_abs_by_output": plc_max_abs_by_output,
            "backward_residual_abs_max_deg": backward_residual_abs_max_deg,
            "backward_prediction_k01_abs_max_deg": (
                backward_prediction_k01_abs_max_deg
            ),
        },
        "tolerance_deg": {
            "campaign_reconstruction": RECONSTRUCTION_MAX_ABS_TOLERANCE_DEG,
            "onnx": ONNX_MAX_ABS_TOLERANCE_DEG,
            "plc_reference": PLC_MAX_ABS_TOLERANCE_DEG,
        },
        "qualification": {
            "campaign_reconstruction_parity": "passed",
            "onnx_runtime_parity": "passed",
            "plc_float32_reference_parity": "passed",
            "backward_zero_residual": "passed",
            "twincat_static_integration": "pending",
            "twincat_xae_build": "pending",
            "activated_target_runtime": "pending",
            "commissioned_testrig_compensation": "pending",
        },
        "deployment_claim": (
            "Export-prepared fixed-grid full-curve composition only; no "
            "TwinCAT build, target, latency, or commissioned-runtime claim."
        ),
    }
    summary_path = output_directory / "a02_export_parity_summary.yaml"
    write_yaml(summary_path, summary)
    return summary


def main() -> None:
    """Run the selected A02 export and parity workflow."""

    arguments = parse_arguments()
    output_directory = resolve_output_directory(arguments.output_directory)
    summary = run_export_and_validation(output_directory)
    print(
        "[PASS] Wave 5.2R A02 export parity | "
        f"conditions={summary['condition_count']} | "
        "campaign_max_abs_deg="
        f"{summary['parity']['campaign_reconstruction_max_abs_deg']:.3e} | "
        "onnx_max_abs_deg="
        f"{max(summary['parity']['onnx_max_abs_by_output'].values()):.3e} | "
        "plc_max_abs_deg="
        f"{max(summary['parity']['plc_reference_max_abs_by_output'].values()):.3e}",
        flush=True,
    )


if __name__ == "__main__":
    main()
