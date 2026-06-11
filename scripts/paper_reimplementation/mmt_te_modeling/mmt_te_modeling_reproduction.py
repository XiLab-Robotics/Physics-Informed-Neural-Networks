"""Reproduce the analytical equation surface from MMT_TEModeling.

The script implements the numbered equation groups from Yang et al.,
``A modelling approach for kinematic equivalent mechanism and rotational
transmission error of RV reducer``. The included command-line entry point runs
a small RV-80E demonstration with transparent equivalent-error values.

The demo is an executable equation-chain check, not a claim of exact figure
reproduction. Exact figure reproduction requires the reducer-specific
cycloidal contact geometry and measured component errors for every sample.
"""

from __future__ import annotations

# Import Standard Libraries
from dataclasses import dataclass
import math

# Import Numerical Libraries
import numpy as np


EPSILON = 1.0e-12
MINIMUM_SAFE_SINE = 5.0e-2
ARCSECOND_PER_RADIAN = 180.0 * 3600.0 / math.pi


@dataclass(frozen=True)
class ReducerParameters:

    """Store fixed reducer geometry for the analytical model.

    Attributes:
        z1: Sun gear tooth count.
        z2: Planetary gear tooth count.
        z4: Cycloidal gear tooth count.
        z5: Pin gear tooth count.
        module_mm: Involute gear module in millimeters.
        pressure_angle_rad: Working pressure angle in radians.
        pin_pitch_radius_mm: Pin gear pitch circle radius.
        crank_eccentricity_mm: Crankshaft eccentricity.
        pin_radius_mm: Pin radius.
    """

    z1: int = 10
    z2: int = 38
    z4: int = 39
    z5: int = 40
    module_mm: float = 1.75
    pressure_angle_rad: float = math.radians(20.0)
    pin_pitch_radius_mm: float = 77.5
    crank_eccentricity_mm: float = 1.5
    pin_radius_mm: float = 4.0

    @property
    def carrier_radius_mm(self) -> float:

        """Return the sun-to-planet-center distance used by the demo."""

        return 0.5 * self.module_mm * (self.z1 + self.z2)

    @property
    def sun_base_radius_mm(self) -> float:

        """Return the sun gear base radius for the equivalent involute link."""

        return 0.5 * self.module_mm * self.z1 * math.cos(self.pressure_angle_rad)

    @property
    def planetary_base_radius_mm(self) -> float:

        """Return the planetary gear base radius for the equivalent link."""

        return 0.5 * self.module_mm * self.z2 * math.cos(self.pressure_angle_rad)

    @property
    def normal_link_length_mm(self) -> float:

        """Return an involute normal-link length used by the demo geometry."""

        center_distance_mm = self.carrier_radius_mm
        base_difference_mm = self.planetary_base_radius_mm - self.sun_base_radius_mm
        return math.sqrt(max(center_distance_mm**2 - base_difference_mm**2, EPSILON))

    @property
    def whole_machine_ratio(self) -> float:

        """Return input angle divided by output angle from Eq. (2)."""

        numerator = self.z2 * self.z5 + self.z1 * (self.z5 - self.z4)
        denominator = self.z1 * (self.z5 - self.z4)
        return numerator / denominator


@dataclass(frozen=True)
class EquivalentErrors:

    """Store equivalent original-error amplitudes for one model evaluation.

    All length values are millimeters and all angles are radians.
    """

    delta_l_b1_mm: float = 0.0
    delta_l_b2_mm: float = 0.005
    delta_l_h_mm: float = 0.004
    delta_l_c_mm: float = 0.005
    delta_l_a_mm: float = 0.003
    delta_l_v_mm: float = 0.0
    delta_l_r_mm: float = 0.005
    accumulative_pitch_error_mm: float = 0.005
    cycloidal_profile_error_mm: float = 0.005
    pin_radius_error_mm: float = 0.002
    delta_theta_b1_rad: float = 0.0
    curvature_radius_positive: bool = True


def safe_sin(angle_rad: np.ndarray | float) -> np.ndarray:

    """Return sine values with tiny denominators guarded."""

    sine_value = np.sin(angle_rad)
    return np.where(np.abs(sine_value) < MINIMUM_SAFE_SINE, np.sign(sine_value + EPSILON) * MINIMUM_SAFE_SINE, sine_value)


def angle_difference(theta_x_rad: np.ndarray | float, theta_y_rad: np.ndarray | float) -> np.ndarray:

    """Implement the paper shorthand theta_x,y = theta_x - theta_y."""

    return np.asarray(theta_x_rad, dtype=float) - np.asarray(theta_y_rad, dtype=float)


def output_and_crank_angles(theta_1_rad: np.ndarray, parameters: ReducerParameters) -> tuple[np.ndarray, np.ndarray]:

    """Implement Eq. (2) for output and crankshaft angles."""

    theta_1_rad = np.asarray(theta_1_rad, dtype=float)
    denominator = parameters.z2 * parameters.z5 + parameters.z1 * (parameters.z5 - parameters.z4)
    theta_h_rad = parameters.z1 * (parameters.z5 - parameters.z4) / denominator * theta_1_rad
    theta_3_rad = -parameters.z4 / (parameters.z5 - parameters.z4) * theta_h_rad
    return theta_h_rad, theta_3_rad


def parallelogram_angles(theta_h_rad: np.ndarray, theta_3_rad: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    """Implement Eq. (3) for the three parallelogram loops."""

    theta_h_rad = np.asarray(theta_h_rad, dtype=float)
    theta_a_rad = 2.0 * math.pi - np.asarray(theta_3_rad, dtype=float)
    loop_offsets_rad = np.asarray([0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0], dtype=float)
    theta_hi_rad = theta_h_rad[:, None] + math.pi / 2.0 + loop_offsets_rad[None, :]
    theta_ai_rad = np.repeat(theta_a_rad[:, None], 3, axis=1)
    return theta_ai_rad, theta_hi_rad


def involute_linkage_angles(theta_h1_rad: np.ndarray, pressure_angle_rad: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    """Implement Eq. (4) for equivalent involute link angles."""

    theta_b1_rad = theta_h1_rad - pressure_angle_rad
    theta_n_rad = theta_h1_rad - pressure_angle_rad + math.pi / 2.0
    theta_b2_rad = theta_h1_rad - pressure_angle_rad + math.pi
    return theta_b1_rad, theta_n_rad, theta_b2_rad


def pin_angle(pin_index: np.ndarray, pin_count: int) -> np.ndarray:

    """Implement Eq. (7) for pin angular positions."""

    return (np.asarray(pin_index, dtype=float) - 1.0) * 2.0 * math.pi / pin_count


def pin_and_cycloid_centers(theta_p_rad: np.ndarray, theta_a_rad: np.ndarray, parameters: ReducerParameters) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

    """Implement Eq. (6) for pin and cycloidal-gear center coordinates."""

    x_k_mm = parameters.pin_pitch_radius_mm * np.cos(theta_p_rad)
    y_k_mm = parameters.pin_pitch_radius_mm * np.sin(theta_p_rad)
    x_o4_mm = parameters.crank_eccentricity_mm * np.cos(theta_a_rad)
    y_o4_mm = parameters.crank_eccentricity_mm * np.sin(theta_a_rad)
    return x_k_mm, y_k_mm, x_o4_mm, y_o4_mm


def contact_linkage_angles(x_c_mm: np.ndarray, y_c_mm: np.ndarray, x_k_mm: np.ndarray, y_k_mm: np.ndarray, x_o4_mm: np.ndarray, y_o4_mm: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    """Implement Eq. (5) with quadrant-safe arctangent."""

    theta_rho_rad = np.arctan2(y_k_mm - y_c_mm, x_k_mm - x_c_mm)
    theta_k_rad = np.arctan2(y_c_mm - y_o4_mm, x_c_mm - x_o4_mm)
    return theta_rho_rad, theta_k_rad


def velocity_transfer_ratios(parameters: ReducerParameters) -> tuple[float, float, float, float]:

    """Implement Eqs. (19)-(22) in their tooth-count form."""

    g1 = -(parameters.z1 + parameters.z2) / parameters.z2
    g2 = 1.0
    g3 = -(parameters.z5 - parameters.z4) / parameters.z4
    g4 = 1.0
    return g1, g2, g3, g4


def cycloid_profile_pin_radius_errors(theta_k_rho_rad: np.ndarray, errors: EquivalentErrors) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    """Implement Eqs. (35)-(36) for profile and pin-radius errors."""

    denominator = safe_sin(theta_k_rho_rad)
    combined_error_mm = errors.cycloidal_profile_error_mm + errors.pin_radius_error_mm
    curvature_exponent = 0 if errors.curvature_radius_positive else 1
    delta_theta_c_rad = combined_error_mm / denominator
    delta_l_k_mm = ((-1.0) ** curvature_exponent) * combined_error_mm / (denominator**2) * np.cos(theta_k_rho_rad)
    delta_l_rho_mm = ((-1.0) ** (curvature_exponent + 1)) * combined_error_mm / (denominator**2)
    return delta_theta_c_rad, delta_l_k_mm, delta_l_rho_mm


def output_disc_assembly_errors(output_disc_error_mm: float, output_disc_error_angle_rad: float, theta_h_rad: np.ndarray, theta_v_rad: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    """Implement Eq. (37) for output-disc assembly error."""

    delta_l_h_mm = -output_disc_error_mm * np.cos(output_disc_error_angle_rad - theta_h_rad)
    delta_l_v_mm = -output_disc_error_mm * np.cos(output_disc_error_angle_rad - theta_v_rad)
    return delta_l_h_mm, delta_l_v_mm


def measured_rte(theta_h_rad: np.ndarray, theta_1_rad: np.ndarray, speed_ratio: float) -> np.ndarray:

    """Implement Eq. (38) for test-bench RTE."""

    return np.asarray(theta_h_rad, dtype=float) - np.asarray(theta_1_rad, dtype=float) / speed_ratio


def compute_subsystem_errors(parameters: ReducerParameters, errors: EquivalentErrors, theta_b1_rad: np.ndarray, theta_n_rad: np.ndarray, theta_b2_rad: np.ndarray, theta_h1_rad: np.ndarray, theta_hi_rad: np.ndarray, theta_ai_rad: np.ndarray, theta_v_rad: np.ndarray, theta_ci_rad: np.ndarray, theta_k_rad: np.ndarray, theta_rho_rad: np.ndarray, theta_p_rad: np.ndarray, delta_l_k_mm: np.ndarray, delta_l_rho_mm: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

    """Implement Eqs. (31)-(34) for subsystem error terms."""

    # Resolve Shared Geometry
    l_b1_mm = parameters.sun_base_radius_mm
    l_b2_mm = parameters.planetary_base_radius_mm
    l_h_mm = parameters.carrier_radius_mm
    l_v_mm = parameters.crank_eccentricity_mm
    l_k_mm = max(parameters.pin_radius_mm, EPSILON)

    # Compute Involute Error Contribution
    theta_b1_n_rad = angle_difference(theta_b1_rad, theta_n_rad)
    theta_h1_n_rad = angle_difference(theta_h1_rad, theta_n_rad)
    theta_b2_n_rad = angle_difference(theta_b2_rad, theta_n_rad)
    delta_l_n_mm = (
        errors.delta_l_b1_mm * np.cos(theta_b1_rad - theta_n_rad)
        + errors.delta_l_b2_mm * np.cos(theta_b2_rad - theta_n_rad)
    )
    f1 = (
        -errors.delta_l_b1_mm / l_b2_mm * np.cos(theta_b1_n_rad)
        + l_b1_mm / l_b2_mm * errors.delta_theta_b1_rad * np.sin(theta_b1_n_rad)
        - delta_l_n_mm / l_b2_mm
        + errors.delta_l_h_mm / l_b2_mm * np.cos(theta_h1_n_rad)
        + errors.delta_l_b2_mm / l_b2_mm * np.cos(theta_b2_n_rad)
    ) / safe_sin(theta_b2_n_rad)

    # Compute Crankshaft Input-Path Contribution
    theta_v_ci_rad = angle_difference(theta_v_rad[:, None], theta_ci_rad)
    theta_hi_ci_rad = angle_difference(theta_hi_rad, theta_ci_rad)
    theta_ai_ci_rad = angle_difference(theta_ai_rad, theta_ci_rad)
    f2i = (
        -errors.delta_l_h_mm / l_v_mm * np.cos(theta_hi_ci_rad)
        - errors.delta_l_a_mm / l_v_mm * np.cos(theta_ai_ci_rad)
        + errors.delta_l_v_mm / l_v_mm * np.cos(theta_v_ci_rad)
        + errors.delta_l_c_mm / l_v_mm
    ) / safe_sin(theta_v_ci_rad)

    # Compute Cycloid-Pin Contribution
    theta_v_rho_rad = angle_difference(theta_v_rad, theta_rho_rad)
    theta_k_rho_rad = angle_difference(theta_k_rad, theta_rho_rad)
    theta_p_rho_rad = angle_difference(theta_p_rad, theta_rho_rad)
    delta_theta_p_rad = errors.accumulative_pitch_error_mm * np.sin(theta_p_rad) / parameters.pin_pitch_radius_mm
    f3 = (
        errors.delta_l_v_mm / l_k_mm * np.cos(theta_v_rho_rad)
        + delta_l_k_mm / l_k_mm * np.cos(theta_k_rho_rad)
        + delta_l_rho_mm / l_k_mm
        - errors.delta_l_r_mm / l_k_mm * np.cos(theta_p_rho_rad)
        + parameters.pin_pitch_radius_mm / l_k_mm * delta_theta_p_rad * np.sin(theta_p_rho_rad)
    ) / safe_sin(theta_k_rho_rad)

    # Compute Crankshaft Output-Path Contribution
    theta_hi_ai_rad = angle_difference(theta_hi_rad, theta_ai_rad)
    theta_v_ai_rad = angle_difference(theta_v_rad[:, None], theta_ai_rad)
    theta_ci_ai_rad = angle_difference(theta_ci_rad, theta_ai_rad)
    f4i = (
        errors.delta_l_h_mm / l_h_mm * np.cos(theta_hi_ai_rad)
        + errors.delta_l_a_mm / l_h_mm
        - errors.delta_l_v_mm / l_h_mm * np.cos(theta_v_ai_rad)
        - errors.delta_l_c_mm / l_h_mm * np.cos(theta_ci_ai_rad)
    ) / safe_sin(theta_hi_ai_rad)

    return f1, f2i, f3, f4i


def whole_machine_rte_universal(f1: np.ndarray, f2i: np.ndarray, f3: np.ndarray, f4i: np.ndarray, parameters: ReducerParameters) -> np.ndarray:

    """Implement Eq. (29), the universal transfer-coefficient expression."""

    g1, g2, g3, g4 = velocity_transfer_ratios(parameters)
    denominator = 1.0 + g1 * g2 * g3 * g4
    return (
        g2 * g3 * g4 / denominator * f1
        + g3 * g4 / denominator * np.mean(f2i, axis=1)
        + g4 / denominator * f3
        + 1.0 / denominator * np.mean(f4i, axis=1)
    )


def whole_machine_rte_one_tooth(f1: np.ndarray, f2i: np.ndarray, f3: np.ndarray, f4i: np.ndarray, parameters: ReducerParameters) -> np.ndarray:

    """Implement Eq. (30), the one-tooth-difference RV expression."""

    numerator = (
        -1.0 / parameters.z4 * f1
        -1.0 / (3.0 * parameters.z4) * np.sum(f2i, axis=1)
        + f3
        + 1.0 / 3.0 * np.sum(f4i, axis=1)
    )
    denominator = 1.0 + (parameters.z1 + parameters.z2) / (parameters.z2 * parameters.z4)
    return numerator / denominator


def run_rv80e_demo(sample_count: int = 11440) -> tuple[np.ndarray, np.ndarray]:

    """Run an executable RV-80E equation-chain demonstration."""

    # Build Kinematic State
    parameters = ReducerParameters()
    errors = EquivalentErrors()
    theta_h_rad = np.linspace(0.0, 2.0 * math.pi, sample_count, endpoint=False)
    theta_1_rad = theta_h_rad * parameters.whole_machine_ratio
    theta_h_from_input_rad, theta_3_rad = output_and_crank_angles(theta_1_rad, parameters)
    theta_ai_rad, theta_hi_rad = parallelogram_angles(theta_h_from_input_rad, theta_3_rad)
    theta_b1_rad, theta_n_rad, theta_b2_rad = involute_linkage_angles(theta_hi_rad[:, 0], parameters.pressure_angle_rad)

    # Build Demonstration Contact Geometry
    pin_indices = np.mod(np.arange(sample_count), parameters.z5) + 1
    theta_p_rad = pin_angle(pin_indices, parameters.z5)
    theta_v_rad = theta_ai_rad[:, 0]
    theta_ci_rad = theta_hi_rad + math.pi / 5.0
    _ = pin_and_cycloid_centers(theta_p_rad, theta_v_rad, parameters)
    theta_rho_rad = theta_p_rad - math.pi / 5.0
    theta_k_rad = theta_p_rad + math.pi / 5.0

    # Propagate Equivalent Errors
    theta_k_rho_rad = angle_difference(theta_k_rad, theta_rho_rad)
    _, delta_l_k_mm, delta_l_rho_mm = cycloid_profile_pin_radius_errors(theta_k_rho_rad, errors)
    f1, f2i, f3, f4i = compute_subsystem_errors(
        parameters,
        errors,
        theta_b1_rad,
        theta_n_rad,
        theta_b2_rad,
        theta_hi_rad[:, 0],
        theta_hi_rad,
        theta_ai_rad,
        theta_v_rad,
        theta_ci_rad,
        theta_k_rad,
        theta_rho_rad,
        theta_p_rad,
        delta_l_k_mm,
        delta_l_rho_mm,
    )
    rte_rad = whole_machine_rte_one_tooth(f1, f2i, f3, f4i, parameters)
    return theta_h_rad, rte_rad


def print_demo_summary(theta_h_rad: np.ndarray, rte_rad: np.ndarray) -> None:

    """Print a compact numerical summary for the demonstration run."""

    # Compute Time-Domain Summary
    rte_arcsec = rte_rad * ARCSECOND_PER_RADIAN
    print("MMT_TEModeling analytical equation-chain demo")
    print(f"Samples: {rte_arcsec.size}")
    print(f"RTE arcsec min/max: {np.min(rte_arcsec):.6f} / {np.max(rte_arcsec):.6f}")
    print(f"RTE arcsec peak-to-peak: {np.ptp(rte_arcsec):.6f}")

    # Compute Harmonic Summary
    centered_rte_arcsec = rte_arcsec - np.mean(rte_arcsec)
    spectrum = np.fft.rfft(centered_rte_arcsec)
    harmonic_bins = np.fft.rfftfreq(centered_rte_arcsec.size, d=1.0 / centered_rte_arcsec.size)
    amplitude = 2.0 * np.abs(spectrum) / centered_rte_arcsec.size
    dominant_indices = np.argsort(amplitude[1:])[-8:][::-1] + 1
    print("Dominant demonstration harmonic bins:")
    for harmonic_index in dominant_indices:
        print(f"  h={harmonic_bins[harmonic_index]:.0f} amplitude_arcsec={amplitude[harmonic_index]:.6f}")


def main() -> None:

    """Run the script demonstration entry point."""

    theta_h_rad, rte_rad = run_rv80e_demo()
    print_demo_summary(theta_h_rad, rte_rad)


if __name__ == "__main__":
    main()
