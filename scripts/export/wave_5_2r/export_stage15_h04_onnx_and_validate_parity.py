"""Export the Stage 15 H04 graph to ONNX and validate numerical parity."""

from __future__ import annotations

# Import Python Utilities
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
from scripts.analysis.wave_5_2r.validate_stage15_official_forward_verification_package import (
    build_frozen_curve_record,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)


# Define The Frozen Export Contract
CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_stage15_official_forward_verification_matrix.yaml"
)
FROZEN_PREDICTION_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
    / "test_predictions.npz"
)
OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_stage15_deployment_parity"
)
ONNX_PATH = OUTPUT_DIRECTORY / "h04_bounded_coefficient_residual.onnx"
INPUT_PAYLOAD_PATH = OUTPUT_DIRECTORY / "stage15_parity_input_payload.npz"
PARITY_CSV_PATH = OUTPUT_DIRECTORY / "stage15_onnx_parity_per_condition.csv"
SUMMARY_PATH = OUTPUT_DIRECTORY / "stage15_onnx_parity_summary.yaml"
COEFFICIENT_MAX_ABS_TOLERANCE_DEG = 1.0e-6
CURVE_MAX_ABS_TOLERANCE_DEG = 2.0e-6
ONNX_OPSET_VERSION = 17


class Stage15H04OnnxWrapper(nn.Module):
    """Expose H04 outputs as an ordered ONNX-friendly tensor tuple."""

    def __init__(self, model_object: nn.Module) -> None:
        """Store the frozen coefficient-residual model."""

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
        """Return reconstructed curve and inspectable coefficient tensors."""

        model_output = self.model_object(
            normalized_condition,
            analytical_anchor_coefficients,
        )
        return (
            model_output["prediction_curve"],
            model_output["prediction_coefficients"],
            model_output["coefficient_correction"],
            model_output["analytical_contribution_curve"],
        )


def compute_file_sha256(file_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


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
    """Write one stable CSV table with a normal final newline."""

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


def build_export_input_payload(
    adapter_config: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build raw, normalized, and analytical inputs for all 97 conditions."""

    frozen_payload = np.load(FROZEN_PREDICTION_PATH)
    condition_id_array = frozen_payload["condition_id"].astype(str)
    raw_condition_row_list = []
    for condition_id in condition_id_array.tolist():
        curve_record = build_frozen_curve_record(
            condition_id,
            angular_sample_count=2048,
        )
        raw_condition_row_list.append(
            [
                -abs(float(curve_record.torque_nm)),
                abs(float(curve_record.speed_rpm)),
                float(curve_record.oil_temperature_deg),
            ]
        )
    raw_condition_matrix = np.asarray(
        raw_condition_row_list,
        dtype=np.float64,
    )
    normalized_condition_matrix = (
        raw_condition_matrix.astype(np.float32)
        - adapter_config["feature_mean"]
    ) / adapter_config["feature_scale"]
    analytical_anchor_matrix = adapter_config[
        "analytical_surface"
    ].predict(raw_condition_matrix).astype(np.float32)
    return (
        condition_id_array,
        normalized_condition_matrix.astype(np.float32),
        analytical_anchor_matrix,
    )


def run_export_and_parity() -> dict[str, Any]:
    """Export H04 and prove Python/ONNX parity on the frozen payload."""

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    comparison_config = (
        reference_family_vs_feedforward_support
        .load_reference_family_comparison_config(CONFIG_PATH)
    )
    candidate_configuration_list = (
        reference_family_vs_feedforward_support
        .resolve_track2_candidate_configuration_list(comparison_config)
    )
    h04_candidate = (
        reference_family_vs_feedforward_support.load_track2_candidate(
            candidate_configuration_list[0]
        )
    )
    assert h04_candidate.training_config is not None
    model_wrapper = Stage15H04OnnxWrapper(
        h04_candidate.model_object
    )
    model_wrapper.eval()

    (
        condition_id_array,
        normalized_condition_matrix,
        analytical_anchor_matrix,
    ) = build_export_input_payload(h04_candidate.training_config)
    normalized_condition_tensor = torch.as_tensor(
        normalized_condition_matrix,
        dtype=torch.float32,
    )
    analytical_anchor_tensor = torch.as_tensor(
        analytical_anchor_matrix,
        dtype=torch.float32,
    )

    # Export The Explicit Multi-Output Inference Graph
    torch.onnx.export(
        model_wrapper,
        (
            normalized_condition_tensor[:1],
            analytical_anchor_tensor[:1],
        ),
        ONNX_PATH,
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
    onnx_model = onnx.load(ONNX_PATH)
    onnx.checker.check_model(onnx_model)

    # Compare Python And ONNX For The Complete Frozen Forward Surface
    with torch.inference_mode():
        python_output_tuple = model_wrapper(
            normalized_condition_tensor,
            analytical_anchor_tensor,
        )
    python_output_array_list = [
        output_tensor.detach().cpu().numpy()
        for output_tensor in python_output_tuple
    ]
    session_options = ort.SessionOptions()
    session_options.intra_op_num_threads = 1
    session_options.inter_op_num_threads = 1
    onnx_session = ort.InferenceSession(
        str(ONNX_PATH),
        sess_options=session_options,
        providers=["CPUExecutionProvider"],
    )
    onnx_output_array_list = onnx_session.run(
        None,
        {
            "normalized_condition": normalized_condition_matrix,
            "analytical_anchor_coefficients": analytical_anchor_matrix,
        },
    )
    assert len(onnx_output_array_list) == 4

    output_name_list = [
        "prediction_curve",
        "prediction_coefficients",
        "coefficient_correction",
        "analytical_contribution_curve",
    ]
    maximum_difference_by_output = {}
    for output_name, python_array, onnx_array in zip(
        output_name_list,
        python_output_array_list,
        onnx_output_array_list,
        strict=True,
    ):
        assert python_array.shape == onnx_array.shape
        assert np.all(np.isfinite(onnx_array))
        maximum_difference_by_output[output_name] = float(
            np.max(np.abs(python_array - onnx_array))
        )

    assert (
        maximum_difference_by_output["prediction_coefficients"]
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        maximum_difference_by_output["coefficient_correction"]
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        maximum_difference_by_output["prediction_curve"]
        <= CURVE_MAX_ABS_TOLERANCE_DEG
    )

    per_condition_row_list = []
    for condition_index, condition_id in enumerate(
        condition_id_array.tolist()
    ):
        per_condition_row_list.append(
            {
                "condition_id": condition_id,
                "prediction_curve_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_output_array_list[0][condition_index]
                            - onnx_output_array_list[0][condition_index]
                        )
                    )
                ),
                "prediction_coefficient_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_output_array_list[1][condition_index]
                            - onnx_output_array_list[1][condition_index]
                        )
                    )
                ),
                "coefficient_correction_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_output_array_list[2][condition_index]
                            - onnx_output_array_list[2][condition_index]
                        )
                    )
                ),
            }
        )
    write_csv(PARITY_CSV_PATH, per_condition_row_list)
    np.savez_compressed(
        INPUT_PAYLOAD_PATH,
        condition_id=condition_id_array,
        normalized_condition=normalized_condition_matrix,
        analytical_anchor_coefficients=analytical_anchor_matrix,
        python_prediction_curve=python_output_array_list[0],
        python_prediction_coefficients=python_output_array_list[1],
        python_coefficient_correction=python_output_array_list[2],
        python_analytical_contribution_curve=python_output_array_list[3],
    )

    summary = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "status": "passed",
        "candidate_id": h04_candidate.candidate_id,
        "condition_count": int(condition_id_array.size),
        "angular_sample_count": int(
            python_output_array_list[0].shape[1]
        ),
        "onnx_opset_version": ONNX_OPSET_VERSION,
        "onnx_path": ONNX_PATH.relative_to(PROJECT_ROOT).as_posix(),
        "onnx_sha256": compute_file_sha256(ONNX_PATH),
        "input_payload_path": INPUT_PAYLOAD_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "input_payload_sha256": compute_file_sha256(INPUT_PAYLOAD_PATH),
        "maximum_absolute_difference_deg_by_output": (
            maximum_difference_by_output
        ),
        "coefficient_max_abs_tolerance_deg": (
            COEFFICIENT_MAX_ABS_TOLERANCE_DEG
        ),
        "curve_max_abs_tolerance_deg": CURVE_MAX_ABS_TOLERANCE_DEG,
        "python_onnx_parity_passed": True,
        "plc_parity_status": "pending",
        "deployment_acceptance_status": (
            "pending_official_curve_verification_and_plc_parity"
        ),
    }
    write_yaml(SUMMARY_PATH, summary)
    return summary


def main() -> None:
    """Run the Stage 15 export and parity validation."""

    summary = run_export_and_parity()
    maximum_difference = summary[
        "maximum_absolute_difference_deg_by_output"
    ]["prediction_curve"]
    print(
        "[PASS] Stage 15 H04 Python/ONNX parity | "
        f"conditions={summary['condition_count']} | "
        f"curve_max_abs_difference_deg={maximum_difference:.3e}",
        flush=True,
    )


if __name__ == "__main__":
    main()
