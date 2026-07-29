"""Analytical utilities for the Stage 13 synthetic weak-form oracle lane."""

from __future__ import annotations

# Import Numerical Utilities
import numpy as np


MINIMUM_NORMALIZATION_SCALE = 1.0e-15


def build_periodic_angle_array(sample_count: int) -> np.ndarray:
    """Build a uniform endpoint-exclusive angular grid."""

    assert sample_count >= 16
    return np.linspace(0.0, 2.0 * np.pi, sample_count, endpoint=False)


def build_fourier_design_matrix(
    theta_array: np.ndarray,
    harmonic_order_list: list[int],
) -> np.ndarray:
    """Build a mean-plus-sine/cosine Fourier design matrix."""

    assert theta_array.ndim == 1
    column_list = [np.ones_like(theta_array)]
    for harmonic_order in harmonic_order_list:
        assert harmonic_order > 0
        column_list.append(np.sin(harmonic_order * theta_array))
        column_list.append(np.cos(harmonic_order * theta_array))
    return np.column_stack(column_list)


def reconstruct_fourier_curve(
    coefficient_array: np.ndarray,
    harmonic_order_list: list[int],
    theta_array: np.ndarray,
) -> np.ndarray:
    """Reconstruct one Fourier curve from explicit coefficients."""

    design_matrix = build_fourier_design_matrix(
        theta_array,
        harmonic_order_list,
    )
    assert coefficient_array.shape == (design_matrix.shape[1],)
    return design_matrix @ coefficient_array


def project_fourier_coefficients(
    curve_array: np.ndarray,
    harmonic_order_list: list[int],
    theta_array: np.ndarray,
) -> np.ndarray:
    """Recover Fourier coefficients by deterministic least squares."""

    assert curve_array.shape == theta_array.shape
    design_matrix = build_fourier_design_matrix(
        theta_array,
        harmonic_order_list,
    )
    coefficient_array, _, _, _ = np.linalg.lstsq(
        design_matrix,
        curve_array,
        rcond=None,
    )
    return coefficient_array


def normalized_root_mean_square_error(
    estimated_array: np.ndarray,
    truth_array: np.ndarray,
) -> float:
    """Return RMSE normalized by the truth RMS."""

    assert estimated_array.shape == truth_array.shape
    error_rms = float(np.sqrt(np.mean(np.square(estimated_array - truth_array))))
    truth_rms = float(np.sqrt(np.mean(np.square(truth_array))))
    return error_rms / max(truth_rms, MINIMUM_NORMALIZATION_SCALE)


def pointwise_oscillator_residual(
    signal_array: np.ndarray,
    theta_array: np.ndarray,
    harmonic_order: int,
) -> float:
    """Measure the normalized finite-difference oscillator residual."""

    assert signal_array.shape == theta_array.shape
    assert harmonic_order > 0
    angular_spacing = float(2.0 * np.pi / signal_array.size)
    second_derivative = (
        np.roll(signal_array, -1)
        - (2.0 * signal_array)
        + np.roll(signal_array, 1)
    ) / (angular_spacing**2)
    residual_array = second_derivative + (
        float(harmonic_order**2) * signal_array
    )
    residual_rms = float(np.sqrt(np.mean(np.square(residual_array))))
    signal_rms = float(np.sqrt(np.mean(np.square(signal_array))))
    return residual_rms / max(
        float(harmonic_order**2) * signal_rms,
        MINIMUM_NORMALIZATION_SCALE,
    )


def _build_periodic_test_function(
    theta_array: np.ndarray,
    center: float,
    concentration: float,
    carrier_order: int,
    carrier_phase: float,
) -> np.ndarray:
    """Build one smooth localized periodic test function."""

    envelope = np.exp(
        concentration * (np.cos(theta_array - center) - 1.0)
    )
    carrier = np.cos(
        (carrier_order * theta_array) + carrier_phase
    )
    return envelope * carrier


def weak_oscillator_residual(
    signal_array: np.ndarray,
    theta_array: np.ndarray,
    harmonic_order: int,
    test_function_count: int = 24,
) -> float:
    """Measure an integrated oscillator residual without differentiating data."""

    assert signal_array.shape == theta_array.shape
    assert harmonic_order > 0
    assert test_function_count >= 8
    angular_spacing = float(2.0 * np.pi / signal_array.size)
    signal_rms = float(np.sqrt(np.mean(np.square(signal_array))))
    normalized_residual_list: list[float] = []

    # Differentiate only the known smooth test functions.
    for test_index in range(test_function_count):
        center = 2.0 * np.pi * test_index / test_function_count
        concentration = 2.0 + float(test_index % 4)
        carrier_order = 1 + (test_index % 5)
        carrier_phase = 0.5 * np.pi * (test_index % 2)
        test_function = _build_periodic_test_function(
            theta_array,
            center,
            concentration,
            carrier_order,
            carrier_phase,
        )
        test_second_derivative = (
            np.roll(test_function, -1)
            - (2.0 * test_function)
            + np.roll(test_function, 1)
        ) / (angular_spacing**2)
        weak_operator = test_second_derivative + (
            float(harmonic_order**2) * test_function
        )
        weak_integral = float(np.mean(signal_array * weak_operator))
        test_rms = float(np.sqrt(np.mean(np.square(test_function))))
        normalization = max(
            float(harmonic_order**2) * signal_rms * test_rms,
            MINIMUM_NORMALIZATION_SCALE,
        )
        normalized_residual_list.append(weak_integral / normalization)

    return float(
        np.sqrt(np.mean(np.square(normalized_residual_list)))
    )


def add_normalized_gaussian_noise(
    signal_array: np.ndarray,
    normalized_noise_level: float,
    random_generator: np.random.Generator,
) -> np.ndarray:
    """Add deterministic Gaussian noise relative to signal RMS."""

    assert normalized_noise_level >= 0.0
    signal_rms = float(np.sqrt(np.mean(np.square(signal_array))))
    return signal_array + random_generator.normal(
        loc=0.0,
        scale=normalized_noise_level * signal_rms,
        size=signal_array.shape,
    )


def fit_linear_parameter_model(
    design_matrix: np.ndarray,
    target_array: np.ndarray,
) -> np.ndarray:
    """Fit one deterministic linear parameter model."""

    assert design_matrix.ndim == 2
    assert target_array.ndim == 1
    assert design_matrix.shape[0] == target_array.size
    parameter_array, _, _, _ = np.linalg.lstsq(
        design_matrix,
        target_array,
        rcond=None,
    )
    return parameter_array
