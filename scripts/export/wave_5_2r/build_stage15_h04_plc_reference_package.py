"""Build a PLC-friendly H04 parameter package and static parity evidence."""

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
import torch
import yaml

# Import Project Utilities
from scripts.export.wave_5_2r.export_stage15_h04_onnx_and_validate_parity import (
    CONFIG_PATH,
    FROZEN_PREDICTION_PATH,
    OUTPUT_DIRECTORY,
    build_export_input_payload,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)


# Define The Static PLC Reference Contract
PARAMETER_ARCHIVE_PATH = (
    OUTPUT_DIRECTORY / "stage15_h04_plc_parameter_archive.npz"
)
GLOBAL_PARAMETER_ST_PATH = (
    OUTPUT_DIRECTORY / "GVL_Stage15H04Parameters.st"
)
FUNCTION_BLOCK_ST_PATH = (
    OUTPUT_DIRECTORY / "FB_Stage15H04CoefficientResidual.st"
)
PARITY_CSV_PATH = (
    OUTPUT_DIRECTORY / "stage15_plc_static_parity_per_condition.csv"
)
SUMMARY_PATH = (
    OUTPUT_DIRECTORY / "stage15_plc_static_parity_summary.yaml"
)
COEFFICIENT_MAX_ABS_TOLERANCE_DEG = 1.0e-6
CURVE_MAX_ABS_TOLERANCE_DEG = 2.0e-6


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


def linear_float32(
    input_matrix: np.ndarray,
    weight_matrix: np.ndarray,
    bias_array: np.ndarray,
) -> np.ndarray:
    """Apply one explicit PLC-like float32 dense layer."""

    input_array = np.asarray(input_matrix, dtype=np.float32)
    weight_array = np.asarray(weight_matrix, dtype=np.float32)
    resolved_bias_array = np.asarray(bias_array, dtype=np.float32)
    output_matrix = np.empty(
        (input_array.shape[0], weight_array.shape[0]),
        dtype=np.float32,
    )
    for sample_index in range(input_array.shape[0]):
        for output_index in range(weight_array.shape[0]):
            accumulator = np.float32(resolved_bias_array[output_index])
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


def quadratic_surface_float32(
    raw_condition_matrix: np.ndarray,
    surface_object: Any,
) -> np.ndarray:
    """Evaluate the frozen PF-A surface with PLC-like float32 operations."""

    raw_condition_array = np.asarray(
        raw_condition_matrix,
        dtype=np.float32,
    )
    feature_mean = np.asarray(
        surface_object.feature_mean,
        dtype=np.float32,
    )
    feature_scale = np.asarray(
        surface_object.feature_scale,
        dtype=np.float32,
    )
    standardized_feature_matrix = np.asarray(
        (raw_condition_array - feature_mean) / feature_scale,
        dtype=np.float32,
    )
    torque = standardized_feature_matrix[:, 0]
    speed = standardized_feature_matrix[:, 1]
    temperature = standardized_feature_matrix[:, 2]
    design_matrix = np.column_stack(
        [
            torque * torque,
            speed * speed,
            temperature * temperature,
            torque * speed,
            torque * temperature,
            speed * temperature,
            torque,
            speed,
            temperature,
            np.ones_like(torque, dtype=np.float32),
        ]
    ).astype(np.float32)
    return linear_float32(
        design_matrix,
        np.asarray(
            surface_object.coefficient_matrix,
            dtype=np.float32,
        ).T,
        np.zeros(19, dtype=np.float32),
    )


def run_plc_static_emulator(
    raw_condition_matrix: np.ndarray,
    state_dictionary: dict[str, torch.Tensor],
    surface_object: Any,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Run the independent REAL-valued PLC reference implementation."""

    feature_mean = np.asarray(
        surface_object.feature_mean,
        dtype=np.float32,
    )
    feature_scale = np.asarray(
        surface_object.feature_scale,
        dtype=np.float32,
    )
    normalized_condition_matrix = np.asarray(
        (
            np.asarray(raw_condition_matrix, dtype=np.float32)
            - feature_mean
        )
        / feature_scale,
        dtype=np.float32,
    )
    activation_matrix = normalized_condition_matrix
    for layer_index in (0, 2, 4):
        activation_matrix = np.tanh(
            linear_float32(
                activation_matrix,
                state_dictionary[
                    f"condition_network.{layer_index}.weight"
                ].detach().cpu().numpy(),
                state_dictionary[
                    f"condition_network.{layer_index}.bias"
                ].detach().cpu().numpy(),
            )
        ).astype(np.float32)
    raw_correction_matrix = linear_float32(
        activation_matrix,
        state_dictionary[
            "condition_network.6.weight"
        ].detach().cpu().numpy(),
        state_dictionary[
            "condition_network.6.bias"
        ].detach().cpu().numpy(),
    )
    correction_bound = (
        state_dictionary["coefficient_correction_bound"]
        .detach()
        .cpu()
        .numpy()
        .astype(np.float32)
    )
    correction_matrix = np.asarray(
        correction_bound
        * np.tanh(raw_correction_matrix).astype(np.float32),
        dtype=np.float32,
    )
    analytical_anchor_matrix = quadratic_surface_float32(
        raw_condition_matrix,
        surface_object,
    )
    prediction_coefficient_matrix = np.asarray(
        analytical_anchor_matrix + correction_matrix,
        dtype=np.float32,
    )
    reconstruction_matrix = (
        state_dictionary["reconstruction_matrix"]
        .detach()
        .cpu()
        .numpy()
        .astype(np.float32)
    )
    prediction_curve_matrix = linear_float32(
        prediction_coefficient_matrix,
        reconstruction_matrix.T,
        np.zeros(reconstruction_matrix.shape[1], dtype=np.float32),
    )
    return (
        prediction_curve_matrix,
        prediction_coefficient_matrix,
        correction_matrix,
    )


def format_st_real_array(value_array: np.ndarray) -> str:
    """Format one flattened REAL initializer for TwinCAT Structured Text."""

    flattened_value_array = np.asarray(
        value_array,
        dtype=np.float32,
    ).reshape(-1)
    return ", ".join(
        f"{float(value):.9e}"
        for value in flattened_value_array
    )


def build_global_parameter_st(
    state_dictionary: dict[str, torch.Tensor],
    surface_object: Any,
) -> str:
    """Build the generated TwinCAT global parameter declaration."""

    parameter_entry_list = [
        (
            "H04_FEATURE_MEAN",
            np.asarray(surface_object.feature_mean, dtype=np.float32),
        ),
        (
            "H04_FEATURE_SCALE",
            np.asarray(surface_object.feature_scale, dtype=np.float32),
        ),
        (
            "H04_PFA_COEFFICIENT_MATRIX",
            np.asarray(
                surface_object.coefficient_matrix,
                dtype=np.float32,
            ),
        ),
        (
            "H04_CORRECTION_BOUND",
            state_dictionary["coefficient_correction_bound"]
            .detach()
            .cpu()
            .numpy(),
        ),
    ]
    for layer_index in (0, 2, 4, 6):
        parameter_entry_list.extend(
            [
                (
                    f"H04_LAYER_{layer_index}_WEIGHT",
                    state_dictionary[
                        f"condition_network.{layer_index}.weight"
                    ]
                    .detach()
                    .cpu()
                    .numpy(),
                ),
                (
                    f"H04_LAYER_{layer_index}_BIAS",
                    state_dictionary[
                        f"condition_network.{layer_index}.bias"
                    ]
                    .detach()
                    .cpu()
                    .numpy(),
                ),
            ]
        )

    line_list = [
        "(* Auto-generated Stage 15 H04 parameters. Do not edit by hand. *)",
        "{attribute 'qualified_only'}",
        "VAR_GLOBAL CONSTANT",
    ]
    for parameter_name, parameter_array in parameter_entry_list:
        flattened_size = int(np.asarray(parameter_array).size)
        line_list.extend(
            [
                (
                    f"    {parameter_name} : ARRAY[0.."
                    f"{flattened_size - 1}] OF REAL := ["
                ),
                f"        {format_st_real_array(parameter_array)}",
                "    ];",
            ]
        )
    line_list.extend(["END_VAR", ""])
    return "\n".join(line_list)


def build_function_block_st() -> str:
    """Build the inspectable H04 TwinCAT inference function block."""

    return """(* Stage 15 H04 PLC reference. Runtime build and timing remain pending. *)
FUNCTION_BLOCK FB_Stage15H04CoefficientResidual
VAR_INPUT
    Enable : BOOL;
    SignedTorqueNm : REAL;
    AbsoluteSpeedRpm : REAL;
    OilTemperatureDegC : REAL;
    OutputAngleRad : REAL;
END_VAR
VAR_OUTPUT
    Valid : BOOL;
    AnalyticalTeDeg : REAL;
    CorrectionTeDeg : REAL;
    PredictedTeDeg : REAL;
    AnalyticalCoefficient : ARRAY[0..18] OF REAL;
    CoefficientCorrection : ARRAY[0..18] OF REAL;
    PredictedCoefficient : ARRAY[0..18] OF REAL;
END_VAR
VAR
    NormalizedCondition : ARRAY[0..2] OF REAL;
    QuadraticBasis : ARRAY[0..9] OF REAL;
    Hidden0 : ARRAY[0..63] OF REAL;
    Hidden1 : ARRAY[0..63] OF REAL;
    Hidden2 : ARRAY[0..31] OF REAL;
    RawCorrection : ARRAY[0..18] OF REAL;
    HarmonicOrder : ARRAY[0..8] OF DINT := [1, 3, 39, 40, 78, 81, 156, 162, 240];
    InputValue : ARRAY[0..2] OF REAL;
    Accumulator : REAL;
    HarmonicIndex : DINT;
    InputIndex : DINT;
    OutputIndex : DINT;
END_VAR

Valid := FALSE;
IF NOT Enable THEN
    PredictedTeDeg := 0.0;
    RETURN;
END_IF

InputValue[0] := SignedTorqueNm;
InputValue[1] := AbsoluteSpeedRpm;
InputValue[2] := OilTemperatureDegC;
FOR InputIndex := 0 TO 2 DO
    NormalizedCondition[InputIndex] :=
        (InputValue[InputIndex] - GVL_Stage15H04Parameters.H04_FEATURE_MEAN[InputIndex])
        / GVL_Stage15H04Parameters.H04_FEATURE_SCALE[InputIndex];
END_FOR

QuadraticBasis[0] := NormalizedCondition[0] * NormalizedCondition[0];
QuadraticBasis[1] := NormalizedCondition[1] * NormalizedCondition[1];
QuadraticBasis[2] := NormalizedCondition[2] * NormalizedCondition[2];
QuadraticBasis[3] := NormalizedCondition[0] * NormalizedCondition[1];
QuadraticBasis[4] := NormalizedCondition[0] * NormalizedCondition[2];
QuadraticBasis[5] := NormalizedCondition[1] * NormalizedCondition[2];
QuadraticBasis[6] := NormalizedCondition[0];
QuadraticBasis[7] := NormalizedCondition[1];
QuadraticBasis[8] := NormalizedCondition[2];
QuadraticBasis[9] := 1.0;

FOR OutputIndex := 0 TO 18 DO
    Accumulator := 0.0;
    FOR InputIndex := 0 TO 9 DO
        Accumulator := Accumulator
            + QuadraticBasis[InputIndex]
            * GVL_Stage15H04Parameters.H04_PFA_COEFFICIENT_MATRIX[
                InputIndex * 19 + OutputIndex
            ];
    END_FOR
    AnalyticalCoefficient[OutputIndex] := Accumulator;
END_FOR

FOR OutputIndex := 0 TO 63 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_0_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 2 DO
        Accumulator := Accumulator
            + NormalizedCondition[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_0_WEIGHT[
                OutputIndex * 3 + InputIndex
            ];
    END_FOR
    Hidden0[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 63 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_2_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 63 DO
        Accumulator := Accumulator
            + Hidden0[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_2_WEIGHT[
                OutputIndex * 64 + InputIndex
            ];
    END_FOR
    Hidden1[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 31 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_4_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 63 DO
        Accumulator := Accumulator
            + Hidden1[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_4_WEIGHT[
                OutputIndex * 64 + InputIndex
            ];
    END_FOR
    Hidden2[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 18 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_6_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 31 DO
        Accumulator := Accumulator
            + Hidden2[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_6_WEIGHT[
                OutputIndex * 32 + InputIndex
            ];
    END_FOR
    RawCorrection[OutputIndex] := Accumulator;
    CoefficientCorrection[OutputIndex] :=
        GVL_Stage15H04Parameters.H04_CORRECTION_BOUND[OutputIndex]
        * TANH(RawCorrection[OutputIndex]);
    PredictedCoefficient[OutputIndex] :=
        AnalyticalCoefficient[OutputIndex] + CoefficientCorrection[OutputIndex];
END_FOR

AnalyticalTeDeg := AnalyticalCoefficient[0];
CorrectionTeDeg := CoefficientCorrection[0];
FOR HarmonicIndex := 0 TO 8 DO
    AnalyticalTeDeg := AnalyticalTeDeg
        + AnalyticalCoefficient[1 + 2 * HarmonicIndex]
        * SIN(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad)
        + AnalyticalCoefficient[2 + 2 * HarmonicIndex]
        * COS(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad);
    CorrectionTeDeg := CorrectionTeDeg
        + CoefficientCorrection[1 + 2 * HarmonicIndex]
        * SIN(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad)
        + CoefficientCorrection[2 + 2 * HarmonicIndex]
        * COS(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad);
END_FOR
PredictedTeDeg := AnalyticalTeDeg + CorrectionTeDeg;
Valid := TRUE;
"""


def run_package_builder() -> dict[str, Any]:
    """Generate parameters, ST source, and independent static parity evidence."""

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
    state_dictionary = h04_candidate.model_object.state_dict()
    surface_object = h04_candidate.training_config[
        "analytical_surface"
    ]
    assert np.allclose(
        h04_candidate.training_config["feature_mean"],
        np.asarray(surface_object.feature_mean, dtype=np.float32),
        rtol=0.0,
        atol=1.0e-6,
    )
    assert np.allclose(
        h04_candidate.training_config["feature_scale"],
        np.asarray(surface_object.feature_scale, dtype=np.float32),
        rtol=0.0,
        atol=1.0e-6,
    )

    frozen_payload = np.load(FROZEN_PREDICTION_PATH)
    condition_id_array = frozen_payload["condition_id"].astype(str)
    (
        _,
        normalized_condition_matrix,
        analytical_anchor_matrix,
    ) = build_export_input_payload(h04_candidate.training_config)
    raw_condition_matrix = (
        normalized_condition_matrix
        * h04_candidate.training_config["feature_scale"]
        + h04_candidate.training_config["feature_mean"]
    ).astype(np.float32)
    with torch.inference_mode():
        python_output = h04_candidate.model_object(
            torch.as_tensor(
                normalized_condition_matrix,
                dtype=torch.float32,
            ),
            torch.as_tensor(
                analytical_anchor_matrix,
                dtype=torch.float32,
            ),
        )
    python_curve_matrix = (
        python_output["prediction_curve"].detach().cpu().numpy()
    )
    python_coefficient_matrix = (
        python_output["prediction_coefficients"].detach().cpu().numpy()
    )
    python_correction_matrix = (
        python_output["coefficient_correction"].detach().cpu().numpy()
    )
    (
        plc_curve_matrix,
        plc_coefficient_matrix,
        plc_correction_matrix,
    ) = run_plc_static_emulator(
        raw_condition_matrix,
        state_dictionary,
        surface_object,
    )

    curve_max_abs_difference_deg = float(
        np.max(np.abs(python_curve_matrix - plc_curve_matrix))
    )
    coefficient_max_abs_difference_deg = float(
        np.max(
            np.abs(
                python_coefficient_matrix - plc_coefficient_matrix
            )
        )
    )
    correction_max_abs_difference_deg = float(
        np.max(
            np.abs(python_correction_matrix - plc_correction_matrix)
        )
    )
    assert (
        curve_max_abs_difference_deg
        <= CURVE_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        coefficient_max_abs_difference_deg
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )
    assert (
        correction_max_abs_difference_deg
        <= COEFFICIENT_MAX_ABS_TOLERANCE_DEG
    )

    parameter_payload = {
        "feature_mean": np.asarray(
            surface_object.feature_mean,
            dtype=np.float32,
        ),
        "feature_scale": np.asarray(
            surface_object.feature_scale,
            dtype=np.float32,
        ),
        "pf_a_coefficient_matrix": np.asarray(
            surface_object.coefficient_matrix,
            dtype=np.float32,
        ),
        "harmonic_order": np.asarray(
            surface_object.harmonic_order_list,
            dtype=np.int32,
        ),
    }
    for state_name, state_tensor in state_dictionary.items():
        parameter_payload[state_name.replace(".", "__")] = (
            state_tensor.detach().cpu().numpy()
        )
    np.savez_compressed(PARAMETER_ARCHIVE_PATH, **parameter_payload)
    GLOBAL_PARAMETER_ST_PATH.write_text(
        build_global_parameter_st(state_dictionary, surface_object),
        encoding="utf-8",
        newline="\n",
    )
    FUNCTION_BLOCK_ST_PATH.write_text(
        build_function_block_st(),
        encoding="utf-8",
        newline="\n",
    )

    parity_row_list = []
    for condition_index, condition_id in enumerate(
        condition_id_array.tolist()
    ):
        parity_row_list.append(
            {
                "condition_id": condition_id,
                "prediction_curve_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_curve_matrix[condition_index]
                            - plc_curve_matrix[condition_index]
                        )
                    )
                ),
                "prediction_coefficient_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_coefficient_matrix[condition_index]
                            - plc_coefficient_matrix[condition_index]
                        )
                    )
                ),
                "coefficient_correction_max_abs_difference_deg": float(
                    np.max(
                        np.abs(
                            python_correction_matrix[condition_index]
                            - plc_correction_matrix[condition_index]
                        )
                    )
                ),
            }
        )
    write_csv(PARITY_CSV_PATH, parity_row_list)

    summary = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "status": "passed",
        "condition_count": int(condition_id_array.size),
        "numeric_type": "IEC_61131_3_REAL_float32_reference",
        "parameter_archive_path": PARAMETER_ARCHIVE_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "parameter_archive_sha256": compute_file_sha256(
            PARAMETER_ARCHIVE_PATH
        ),
        "global_parameter_st_path": GLOBAL_PARAMETER_ST_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "global_parameter_st_sha256": compute_file_sha256(
            GLOBAL_PARAMETER_ST_PATH
        ),
        "function_block_st_path": FUNCTION_BLOCK_ST_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "function_block_st_sha256": compute_file_sha256(
            FUNCTION_BLOCK_ST_PATH
        ),
        "curve_max_abs_difference_deg": (
            curve_max_abs_difference_deg
        ),
        "coefficient_max_abs_difference_deg": (
            coefficient_max_abs_difference_deg
        ),
        "correction_max_abs_difference_deg": (
            correction_max_abs_difference_deg
        ),
        "curve_max_abs_tolerance_deg": CURVE_MAX_ABS_TOLERANCE_DEG,
        "coefficient_max_abs_tolerance_deg": (
            COEFFICIENT_MAX_ABS_TOLERANCE_DEG
        ),
        "static_plc_reference_parity_passed": True,
        "twincat_compile_status": "pending",
        "twincat_runtime_status": "pending",
        "deployment_claim": (
            "PLC-friendly reference package only; no TwinCAT runtime claim"
        ),
    }
    write_yaml(SUMMARY_PATH, summary)
    return summary


def main() -> None:
    """Run the PLC reference package builder."""

    summary = run_package_builder()
    print(
        "[PASS] Stage 15 PLC static reference parity | "
        f"conditions={summary['condition_count']} | "
        "curve_max_abs_difference_deg="
        f"{summary['curve_max_abs_difference_deg']:.3e}",
        flush=True,
    )


if __name__ == "__main__":
    main()
