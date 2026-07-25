"""Inspectable Polynomial-Fourier model primitives for the Phase 1 benchmark."""

from __future__ import annotations

import hashlib
import re
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import onnxruntime as ort


@dataclass(frozen=True)
class QuadraticCoefficientSurface:
    """Complete quadratic multi-output coefficient surface."""

    feature_mean: np.ndarray
    feature_scale: np.ndarray
    coefficient_matrix: np.ndarray
    harmonic_order_list: tuple[int, ...]
    design_condition_number: float

    def predict(self, operating_feature_matrix: np.ndarray) -> np.ndarray:
        """Predict offset and sine/cosine coefficients."""

        standardized_feature_matrix = (
            operating_feature_matrix - self.feature_mean
        ) / self.feature_scale
        design_matrix = build_complete_quadratic_design(
            standardized_feature_matrix
        )
        return design_matrix @ self.coefficient_matrix


@dataclass(frozen=True)
class PlcPolynomialFourierParameters:
    """Parsed active PLC Polynomial-Fourier parameters."""

    gear_factor: float
    polynomial_degree: int
    harmonic_order_array: np.ndarray
    positive_offset_coefficients: np.ndarray
    positive_amplitude_coefficients: np.ndarray
    positive_phase_coefficients: np.ndarray
    negative_offset_coefficients: np.ndarray
    negative_amplitude_coefficients: np.ndarray
    negative_phase_coefficients: np.ndarray
    source_sha256: str


class RecoveredMatlabOnnxPredictor:
    """Run the seven ONNX coefficient models used by the recovered MATLAB path."""

    def __init__(
        self,
        model_path_map: dict[str, Path],
        provider_list: list[str],
    ) -> None:
        """Create explicit CPU sessions and validate their scalar contracts."""

        required_model_name_set = {
            "A0",
            "A1",
            "phi1",
            "A39",
            "phi39",
            "A40",
            "phi40",
        }
        assert set(model_path_map) == required_model_name_set, (
            "Recovered MATLAB ONNX model map is incomplete"
        )
        self.session_map: dict[str, ort.InferenceSession] = {}
        self.model_sha256_map: dict[str, str] = {}
        for model_name, model_path in model_path_map.items():
            assert model_path.is_file(), f"ONNX model does not exist | {model_path}"
            session_options = ort.SessionOptions()
            session_options.intra_op_num_threads = 1
            session_options.inter_op_num_threads = 1
            session = ort.InferenceSession(
                str(model_path),
                sess_options=session_options,
                providers=provider_list,
            )
            session.disable_fallback()
            assert session.get_providers() == provider_list, (
                f"Unexpected ONNX provider resolution | {model_path}"
            )
            assert len(session.get_inputs()) == 1, (
                f"Expected one ONNX input | {model_path}"
            )
            assert len(session.get_outputs()) == 1, (
                f"Expected one ONNX output | {model_path}"
            )
            assert session.get_inputs()[0].shape == [None, 3], (
                f"Unexpected ONNX input shape | {model_path}"
            )
            self.session_map[model_name] = session
            self.model_sha256_map[model_name] = compute_file_sha256(model_path)

    def predict_coefficients(
        self,
        nominal_input_matrix: np.ndarray,
    ) -> dict[str, np.ndarray]:
        """Predict the MATLAB coefficient set for a float32 input batch."""

        input_matrix = np.asarray(nominal_input_matrix, dtype=np.float32)
        assert input_matrix.ndim == 2 and input_matrix.shape[1] == 3, (
            "ONNX input must have shape [batch, 3]"
        )
        prediction_map: dict[str, np.ndarray] = {}
        for model_name, session in self.session_map.items():
            input_name = session.get_inputs()[0].name
            output_name = session.get_outputs()[0].name
            prediction = session.run(
                [output_name],
                {input_name: input_matrix},
            )[0]
            prediction_map[model_name] = np.asarray(
                prediction,
                dtype=np.float64,
            ).reshape(-1)
        return prediction_map

    @staticmethod
    def reconstruct(
        theta_rad: np.ndarray,
        coefficient_map: dict[str, float],
    ) -> np.ndarray:
        """Reconstruct the exact sparse cosine law used by MATLAB."""

        return (
            coefficient_map["A0"]
            + coefficient_map["A1"]
            * np.cos(theta_rad + coefficient_map["phi1"])
            + coefficient_map["A39"]
            * np.cos(39.0 * theta_rad + coefficient_map["phi39"])
            + coefficient_map["A40"]
            * np.cos(40.0 * theta_rad + coefficient_map["phi40"])
        )


def periodic_resample_curve(
    theta_deg: np.ndarray,
    transmission_error_deg: np.ndarray,
    sample_count: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Resample one directional curve to a uniform output revolution."""

    finite_row_mask = np.isfinite(theta_deg) & np.isfinite(
        transmission_error_deg
    )
    finite_theta_deg = theta_deg[finite_row_mask]
    finite_te_deg = transmission_error_deg[finite_row_mask]
    assert finite_theta_deg.size >= sample_count, (
        "Source curve has fewer finite samples than the target grid"
    )
    sort_index_array = np.argsort(finite_theta_deg)
    sorted_theta_deg = finite_theta_deg[sort_index_array]
    sorted_te_deg = finite_te_deg[sort_index_array]
    unique_theta_deg, unique_index_array = np.unique(
        sorted_theta_deg,
        return_index=True,
    )
    unique_te_deg = sorted_te_deg[unique_index_array]
    assert unique_theta_deg.size >= sample_count, (
        "Source curve has fewer unique angular samples than the target grid"
    )

    extended_theta_deg = np.concatenate(
        (
            unique_theta_deg[-1:] - 360.0,
            unique_theta_deg,
            unique_theta_deg[:1] + 360.0,
        )
    )
    extended_te_deg = np.concatenate(
        (
            unique_te_deg[-1:],
            unique_te_deg,
            unique_te_deg[:1],
        )
    )
    uniform_theta_deg = np.linspace(
        0.0,
        360.0,
        sample_count,
        endpoint=False,
    )
    uniform_te_deg = np.interp(
        uniform_theta_deg,
        extended_theta_deg,
        extended_te_deg,
    )
    return uniform_theta_deg, uniform_te_deg


def project_fourier_coefficients(
    transmission_error_deg: np.ndarray,
    harmonic_order_list: list[int] | tuple[int, ...],
) -> np.ndarray:
    """Project a periodic curve into offset and sine/cosine coefficients."""

    sample_count = transmission_error_deg.size
    theta_rad = np.linspace(0.0, 2.0 * np.pi, sample_count, endpoint=False)
    coefficient_list = [float(np.mean(transmission_error_deg))]
    for harmonic_order in harmonic_order_list:
        coefficient_list.append(
            float(
                2.0
                * np.dot(
                    transmission_error_deg,
                    np.sin(harmonic_order * theta_rad),
                )
                / sample_count
            )
        )
        coefficient_list.append(
            float(
                2.0
                * np.dot(
                    transmission_error_deg,
                    np.cos(harmonic_order * theta_rad),
                )
                / sample_count
            )
        )
    return np.asarray(coefficient_list, dtype=np.float64)


def reconstruct_from_projected_coefficients(
    theta_rad: np.ndarray,
    coefficient_array: np.ndarray,
    harmonic_order_list: list[int] | tuple[int, ...],
) -> np.ndarray:
    """Reconstruct a curve from offset and ordered sine/cosine coefficients."""

    expected_coefficient_count = 1 + (2 * len(harmonic_order_list))
    assert coefficient_array.size == expected_coefficient_count, (
        "Fourier coefficient count does not match the harmonic order set"
    )
    reconstructed_curve = np.full_like(
        theta_rad,
        coefficient_array[0],
        dtype=np.float64,
    )
    for harmonic_index, harmonic_order in enumerate(harmonic_order_list):
        sine_coefficient = coefficient_array[1 + (2 * harmonic_index)]
        cosine_coefficient = coefficient_array[2 + (2 * harmonic_index)]
        reconstructed_curve += (
            sine_coefficient * np.sin(harmonic_order * theta_rad)
            + cosine_coefficient * np.cos(harmonic_order * theta_rad)
        )
    return reconstructed_curve


def reconstruct_direct_rfft_oracle(
    transmission_error_deg: np.ndarray,
    maximum_harmonic_order: int,
) -> np.ndarray:
    """Reconstruct a target-leaking direct Fourier oracle up to one order."""

    spectrum = np.fft.rfft(transmission_error_deg)
    truncated_spectrum = np.zeros_like(spectrum)
    retained_bin_count = min(maximum_harmonic_order + 1, spectrum.size)
    truncated_spectrum[:retained_bin_count] = spectrum[:retained_bin_count]
    return np.fft.irfft(
        truncated_spectrum,
        n=transmission_error_deg.size,
    )


def build_complete_quadratic_design(
    standardized_feature_matrix: np.ndarray,
) -> np.ndarray:
    """Build the Bauer complete quadratic basis in three variables."""

    feature_matrix = np.asarray(standardized_feature_matrix, dtype=np.float64)
    assert feature_matrix.ndim == 2 and feature_matrix.shape[1] == 3, (
        "Complete quadratic design requires exactly three operating variables"
    )
    torque = feature_matrix[:, 0]
    speed = feature_matrix[:, 1]
    temperature = feature_matrix[:, 2]
    return np.column_stack(
        (
            torque**2,
            speed**2,
            temperature**2,
            torque * speed,
            torque * temperature,
            speed * temperature,
            torque,
            speed,
            temperature,
            np.ones(feature_matrix.shape[0], dtype=np.float64),
        )
    )


def fit_quadratic_coefficient_surface(
    operating_feature_matrix: np.ndarray,
    target_coefficient_matrix: np.ndarray,
    harmonic_order_list: list[int],
) -> QuadraticCoefficientSurface:
    """Fit a standardized complete quadratic multi-output surface."""

    feature_mean = np.mean(operating_feature_matrix, axis=0)
    feature_scale = np.std(operating_feature_matrix, axis=0)
    assert np.all(feature_scale > 0.0), "Operating feature scale is zero"
    standardized_feature_matrix = (
        operating_feature_matrix - feature_mean
    ) / feature_scale
    design_matrix = build_complete_quadratic_design(
        standardized_feature_matrix
    )
    coefficient_matrix, _, matrix_rank, singular_value_array = np.linalg.lstsq(
        design_matrix,
        target_coefficient_matrix,
        rcond=None,
    )
    assert matrix_rank == design_matrix.shape[1], (
        "Complete quadratic design is rank deficient"
    )
    design_condition_number = float(
        singular_value_array[0] / singular_value_array[-1]
    )
    return QuadraticCoefficientSurface(
        feature_mean=feature_mean,
        feature_scale=feature_scale,
        coefficient_matrix=coefficient_matrix,
        harmonic_order_list=tuple(harmonic_order_list),
        design_condition_number=design_condition_number,
    )


def bauer_preprocessing_audit(
    transmission_error_deg: np.ndarray,
    zero_padding_factor: int,
) -> dict[str, Any]:
    """Reproduce detrending, Hamming, zero padding, and spectrum normalization."""

    sample_count = transmission_error_deg.size
    normalized_index = np.linspace(-1.0, 1.0, sample_count)
    trend_design = np.column_stack(
        (normalized_index, np.ones(sample_count, dtype=np.float64))
    )
    trend_coefficient_array = np.linalg.lstsq(
        trend_design,
        transmission_error_deg,
        rcond=None,
    )[0]
    detrended_curve = (
        transmission_error_deg - trend_design @ trend_coefficient_array
    )
    hamming_window = np.hamming(sample_count)
    coherent_gain = float(np.mean(hamming_window))
    windowed_curve = detrended_curve * hamming_window
    zero_padded_sample_count = int(
        zero_padding_factor * (2 ** int(np.ceil(np.log2(sample_count))))
    )
    assert zero_padded_sample_count > 10 * sample_count, (
        "Bauer zero padding must exceed ten times the base sample count"
    )
    spectrum = np.fft.rfft(windowed_curve, n=zero_padded_sample_count)
    single_sided_amplitude = (
        2.0 * np.abs(spectrum) / (sample_count * coherent_gain)
    )
    harmonic_axis = np.fft.rfftfreq(
        zero_padded_sample_count,
        d=1.0 / sample_count,
    )
    integer_order_amplitude_array = np.interp(
        np.arange(1, min(400, sample_count // 2) + 1),
        harmonic_axis,
        single_sided_amplitude,
    )
    dominant_order_array = (
        np.argsort(integer_order_amplitude_array)[-10:] + 1
    )
    return {
        "linear_trend_slope_deg_per_normalized_revolution": float(
            trend_coefficient_array[0]
        ),
        "hamming_coherent_gain": coherent_gain,
        "zero_padded_sample_count": zero_padded_sample_count,
        "dominant_order_list": [
            int(order) for order in dominant_order_array[::-1]
        ],
        "maximum_single_sided_amplitude_deg": float(
            np.max(integer_order_amplitude_array)
        ),
    }


def build_plc_polynomial_basis(
    torque_nm: float,
    velocity_rad_s: float,
    temperature_deg_c: float,
) -> np.ndarray:
    """Build the exact 35-term PLC polynomial basis."""

    basis_value_list = [
        torque_nm**2,
        velocity_rad_s**2,
        temperature_deg_c**2,
        torque_nm * velocity_rad_s,
        torque_nm * temperature_deg_c,
        velocity_rad_s * temperature_deg_c,
        torque_nm,
        velocity_rad_s,
        temperature_deg_c,
        1.0,
        torque_nm**3,
        velocity_rad_s**3,
        temperature_deg_c**3,
        torque_nm * velocity_rad_s * temperature_deg_c,
    ]
    for polynomial_degree in range(4, 11):
        basis_value_list.extend(
            (
                torque_nm**polynomial_degree,
                velocity_rad_s**polynomial_degree,
                temperature_deg_c**polynomial_degree,
            )
        )
    basis_array = np.asarray(basis_value_list, dtype=np.float64)
    assert basis_array.size == 35, "PLC polynomial basis must contain 35 terms"
    return basis_array


def evaluate_plc_order10_polynomial(
    coefficient_array: np.ndarray,
    torque_nm: float,
    velocity_rad_s: float,
    temperature_deg_c: float,
) -> float:
    """Evaluate the exact PLC polynomial through an explicit basis dot product."""

    assert coefficient_array.size == 35, (
        "PLC polynomial coefficient array must contain 35 values"
    )
    return float(
        np.dot(
            coefficient_array,
            build_plc_polynomial_basis(
                torque_nm,
                velocity_rad_s,
                temperature_deg_c,
            ),
        )
    )


def reconstruct_plc_curve(
    theta_output_rad: np.ndarray,
    direction_name: str,
    measured_torque_nm: float,
    measured_speed_rpm: float,
    measured_temperature_deg_c: float,
    plc_parameters: PlcPolynomialFourierParameters,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Reconstruct the active direction-specific PLC curve and intermediates."""

    assert direction_name in {"Fw", "Bw"}, f"Unknown direction | {direction_name}"
    velocity_rad_s = abs(measured_speed_rpm) * np.pi / 30.0
    if direction_name == "Fw":
        offset_coefficients = plc_parameters.positive_offset_coefficients
        amplitude_coefficient_matrix = (
            plc_parameters.positive_amplitude_coefficients
        )
        phase_coefficient_matrix = plc_parameters.positive_phase_coefficients
    else:
        offset_coefficients = plc_parameters.negative_offset_coefficients
        amplitude_coefficient_matrix = (
            plc_parameters.negative_amplitude_coefficients
        )
        phase_coefficient_matrix = plc_parameters.negative_phase_coefficients

    offset_rad = evaluate_plc_order10_polynomial(
        offset_coefficients,
        measured_torque_nm,
        velocity_rad_s,
        measured_temperature_deg_c,
    )
    amplitude_rad_array = np.asarray(
        [
            evaluate_plc_order10_polynomial(
                amplitude_coefficient_matrix[harmonic_index],
                measured_torque_nm,
                velocity_rad_s,
                measured_temperature_deg_c,
            )
            for harmonic_index in range(
                plc_parameters.harmonic_order_array.size
            )
        ],
        dtype=np.float64,
    )
    phase_rad_array = np.asarray(
        [
            evaluate_plc_order10_polynomial(
                phase_coefficient_matrix[harmonic_index],
                measured_torque_nm,
                velocity_rad_s,
                measured_temperature_deg_c,
            )
            for harmonic_index in range(
                plc_parameters.harmonic_order_array.size
            )
        ],
        dtype=np.float64,
    )

    predicted_te_rad = np.full_like(theta_output_rad, offset_rad)
    for harmonic_index, harmonic_order in enumerate(
        plc_parameters.harmonic_order_array
    ):
        predicted_te_rad += amplitude_rad_array[harmonic_index] * np.sin(
            harmonic_order * theta_output_rad
            + phase_rad_array[harmonic_index]
        )
    return np.rad2deg(predicted_te_rad), {
        "offset_rad": offset_rad,
        "amplitude_rad_array": amplitude_rad_array,
        "phase_rad_array": phase_rad_array,
        "velocity_rad_s": velocity_rad_s,
    }


def parse_plc_parameters(plc_model_source_path: Path) -> PlcPolynomialFourierParameters:
    """Parse the active degree-10 coefficient tables from the TwinCAT XML."""

    xml_root = ElementTree.parse(plc_model_source_path).getroot()
    declaration_element = xml_root.find(".//Declaration")
    assert declaration_element is not None and declaration_element.text, (
        "PLC model declaration is missing"
    )
    declaration_text = declaration_element.text

    gear_factor_match = re.search(
        r"gear_factor\s*:=\s*(?P<value>[-+0-9.Ee]+)",
        declaration_text,
    )
    polynomial_degree_match = re.search(
        r"polynomial_degree\s*:=\s*(?P<value>[-+0-9.Ee]+)",
        declaration_text,
    )
    harmonic_order_match = re.search(
        r"f_k\s*:=\s*\[(?P<values>[^\]]+)\]",
        declaration_text,
    )
    assert gear_factor_match and polynomial_degree_match and harmonic_order_match

    harmonic_order_array = _parse_numeric_array(
        harmonic_order_match.group("values")
    )
    positive_entry_list = _parse_plc_direction_entries(
        _extract_named_bracket_content(declaration_text, "pos")
    )
    negative_entry_list = _parse_plc_direction_entries(
        _extract_named_bracket_content(declaration_text, "neg")
    )
    polynomial_degree = int(float(polynomial_degree_match.group("value")))
    assert polynomial_degree == 10, "Expected active PLC polynomial degree 10"
    assert len(positive_entry_list) == polynomial_degree
    assert len(negative_entry_list) == polynomial_degree

    positive_active_entry = positive_entry_list[polynomial_degree - 1]
    negative_active_entry = negative_entry_list[polynomial_degree - 1]
    return PlcPolynomialFourierParameters(
        gear_factor=float(gear_factor_match.group("value")),
        polynomial_degree=polynomial_degree,
        harmonic_order_array=harmonic_order_array,
        positive_offset_coefficients=positive_active_entry["a_0"],
        positive_amplitude_coefficients=positive_active_entry["amp"]
        .reshape(35, harmonic_order_array.size)
        .T,
        positive_phase_coefficients=positive_active_entry["phase"]
        .reshape(35, harmonic_order_array.size)
        .T,
        negative_offset_coefficients=negative_active_entry["a_0"],
        negative_amplitude_coefficients=negative_active_entry["amp"]
        .reshape(35, harmonic_order_array.size)
        .T,
        negative_phase_coefficients=negative_active_entry["phase"]
        .reshape(35, harmonic_order_array.size)
        .T,
        source_sha256=compute_file_sha256(plc_model_source_path),
    )


def _extract_named_bracket_content(source_text: str, field_name: str) -> str:
    """Extract one named top-level square-bracket payload."""

    field_match = re.search(rf"\b{re.escape(field_name)}\s*:=\s*\[", source_text)
    assert field_match is not None, f"Unable to find PLC field | {field_name}"
    opening_bracket_index = field_match.end() - 1
    bracket_depth = 0
    for character_index in range(opening_bracket_index, len(source_text)):
        character = source_text[character_index]
        if character == "[":
            bracket_depth += 1
        elif character == "]":
            bracket_depth -= 1
            if bracket_depth == 0:
                return source_text[opening_bracket_index + 1 : character_index]
    raise AssertionError(f"Unclosed PLC bracket field | {field_name}")


def _parse_plc_direction_entries(
    direction_payload: str,
) -> list[dict[str, np.ndarray]]:
    """Parse ten parenthesized direction entries from the PLC declaration."""

    entry_text_list: list[str] = []
    parenthesis_depth = 0
    entry_start_index: int | None = None
    for character_index, character in enumerate(direction_payload):
        if character == "(":
            if parenthesis_depth == 0:
                entry_start_index = character_index
            parenthesis_depth += 1
        elif character == ")":
            parenthesis_depth -= 1
            if parenthesis_depth == 0 and entry_start_index is not None:
                entry_text_list.append(
                    direction_payload[entry_start_index + 1 : character_index]
                )
                entry_start_index = None
    assert parenthesis_depth == 0, "Unbalanced PLC direction parentheses"

    parsed_entry_list: list[dict[str, np.ndarray]] = []
    entry_pattern = re.compile(
        r"a_0\s*:=\s*\[(?P<a0>.*?)\]\s*,\s*"
        r"amp\s*:=\s*\[(?P<amp>.*?)\]\s*,\s*"
        r"phase\s*:=\s*\[(?P<phase>.*?)\]",
        flags=re.DOTALL,
    )
    for entry_text in entry_text_list:
        entry_match = entry_pattern.search(entry_text)
        assert entry_match is not None, "Unable to parse PLC direction entry"
        parsed_entry = {
            "a_0": _parse_numeric_array(entry_match.group("a0")),
            "amp": _parse_numeric_array(entry_match.group("amp")),
            "phase": _parse_numeric_array(entry_match.group("phase")),
        }
        assert parsed_entry["a_0"].size == 35
        assert parsed_entry["amp"].size == 315
        assert parsed_entry["phase"].size == 315
        parsed_entry_list.append(parsed_entry)
    return parsed_entry_list


def _parse_numeric_array(array_text: str) -> np.ndarray:
    """Parse a comma-separated TwinCAT numeric array."""

    return np.asarray(
        [
            float(value_text.strip())
            for value_text in array_text.split(",")
            if value_text.strip()
        ],
        dtype=np.float64,
    )


def compute_file_sha256(file_path: Path) -> str:
    """Compute a file SHA-256 incrementally."""

    digest = hashlib.sha256()
    with file_path.open("rb") as source_file:
        for file_chunk in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(file_chunk)
    return digest.hexdigest()
