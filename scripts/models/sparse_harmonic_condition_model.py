"""Sparse condition laws for explicit harmonic-coefficient prediction."""

from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from typing import Any

# Import Numerical Utilities
import numpy as np


# Define Stable Numerical Constants
MINIMUM_SCALE = 1.0e-12
DEFAULT_MAXIMUM_THRESHOLD_ITERATIONS = 12


@dataclass(frozen=True)
class NamedConditionTerm:
    """Describe one deterministic operating-condition library term."""

    name: str
    expression: str
    parent_name_list: tuple[str, ...]
    library_group: str


@dataclass
class SparseFitResult:
    """Hold one fitted sparse multi-output coefficient law."""

    coefficient_matrix: np.ndarray
    active_mask: np.ndarray
    selection_probability: np.ndarray
    sign_agreement: np.ndarray
    median_normalized_magnitude: np.ndarray
    alpha: float
    threshold: float


@dataclass
class SparseHarmonicConditionModel:
    """Predict explicit harmonic coefficients from operating conditions."""

    term_list: list[NamedConditionTerm]
    feature_mean: np.ndarray
    feature_scale: np.ndarray
    library_scale: np.ndarray
    target_scale: np.ndarray
    coefficient_matrix: np.ndarray
    harmonic_order_list: list[int]

    def predict_coefficients(
        self,
        condition_matrix: np.ndarray,
    ) -> np.ndarray:
        """Predict physical coefficient corrections.

        Args:
            condition_matrix: Torque, speed, and temperature rows.

        Returns:
            Physical coefficient-correction matrix.
        """

        normalized_condition_matrix = normalize_conditions(
            condition_matrix,
            self.feature_mean,
            self.feature_scale,
        )
        library_matrix = evaluate_condition_library(
            normalized_condition_matrix,
            self.term_list,
        )
        normalized_library_matrix = (
            library_matrix / self.library_scale[np.newaxis, :]
        )
        normalized_prediction_matrix = (
            normalized_library_matrix @ self.coefficient_matrix
        )
        return normalized_prediction_matrix * self.target_scale[np.newaxis, :]

    @property
    def active_term_count(self) -> int:
        """Return the number of active term-output coefficient slots."""

        return int(np.count_nonzero(np.abs(self.coefficient_matrix) > 0.0))

    @property
    def maximum_terms_per_output(self) -> int:
        """Return the largest active-term count of one output channel."""

        return int(
            np.max(
                np.count_nonzero(
                    np.abs(self.coefficient_matrix) > 0.0,
                    axis=0,
                )
            )
        )


def build_named_condition_term_list(
    library_name: str,
) -> list[NamedConditionTerm]:
    """Build one predeclared condition-term library.

    Args:
        library_name: `quadratic`, `extended`, or `symbolic`.

    Returns:
        Stable ordered term list.
    """

    assert library_name in {"quadratic", "extended", "symbolic"}
    quadratic_term_list = [
        NamedConditionTerm("one", "1", (), "quadratic"),
        NamedConditionTerm("torque", "q", (), "quadratic"),
        NamedConditionTerm("speed", "s", (), "quadratic"),
        NamedConditionTerm("temperature", "u", (), "quadratic"),
        NamedConditionTerm("torque_sq", "q^2", ("torque",), "quadratic"),
        NamedConditionTerm("speed_sq", "s^2", ("speed",), "quadratic"),
        NamedConditionTerm(
            "temperature_sq",
            "u^2",
            ("temperature",),
            "quadratic",
        ),
        NamedConditionTerm(
            "torque_speed",
            "q*s",
            ("torque", "speed"),
            "quadratic",
        ),
        NamedConditionTerm(
            "torque_temperature",
            "q*u",
            ("torque", "temperature"),
            "quadratic",
        ),
        NamedConditionTerm(
            "speed_temperature",
            "s*u",
            ("speed", "temperature"),
            "quadratic",
        ),
    ]
    if library_name == "quadratic":
        return quadratic_term_list
    extended_term_list = [
        NamedConditionTerm("torque_cube", "q^3", ("torque",), "extended"),
        NamedConditionTerm("speed_cube", "s^3", ("speed",), "extended"),
        NamedConditionTerm(
            "temperature_cube",
            "u^3",
            ("temperature",),
            "extended",
        ),
        NamedConditionTerm(
            "torque_speed_temperature",
            "q*s*u",
            ("torque", "speed", "temperature"),
            "extended",
        ),
        NamedConditionTerm(
            "torque_sq_speed",
            "q^2*s",
            ("torque_sq", "speed"),
            "extended",
        ),
        NamedConditionTerm(
            "torque_sq_temperature",
            "q^2*u",
            ("torque_sq", "temperature"),
            "extended",
        ),
        NamedConditionTerm(
            "speed_sq_torque",
            "s^2*q",
            ("speed_sq", "torque"),
            "extended",
        ),
        NamedConditionTerm(
            "speed_sq_temperature",
            "s^2*u",
            ("speed_sq", "temperature"),
            "extended",
        ),
        NamedConditionTerm(
            "temperature_sq_torque",
            "u^2*q",
            ("temperature_sq", "torque"),
            "extended",
        ),
        NamedConditionTerm(
            "temperature_sq_speed",
            "u^2*s",
            ("temperature_sq", "speed"),
            "extended",
        ),
        NamedConditionTerm(
            "torque_signed_magnitude",
            "q*abs(q)",
            ("torque",),
            "symbolic",
        ),
        NamedConditionTerm(
            "speed_signed_magnitude",
            "s*abs(s)",
            ("speed",),
            "symbolic",
        ),
        NamedConditionTerm(
            "temperature_signed_magnitude",
            "u*abs(u)",
            ("temperature",),
            "symbolic",
        ),
        NamedConditionTerm(
            "torque_signed_log",
            "sign(q)*log1p(abs(q))",
            ("torque",),
            "symbolic",
        ),
        NamedConditionTerm(
            "speed_signed_log",
            "sign(s)*log1p(abs(s))",
            ("speed",),
            "symbolic",
        ),
        NamedConditionTerm(
            "temperature_signed_log",
            "sign(u)*log1p(abs(u))",
            ("temperature",),
            "symbolic",
        ),
        NamedConditionTerm(
            "torque_bounded",
            "q/(1+abs(q))",
            ("torque",),
            "symbolic",
        ),
        NamedConditionTerm(
            "speed_bounded",
            "s/(1+abs(s))",
            ("speed",),
            "symbolic",
        ),
        NamedConditionTerm(
            "temperature_bounded",
            "u/(1+abs(u))",
            ("temperature",),
            "symbolic",
        ),
    ]
    if library_name == "extended":
        return [*quadratic_term_list, *extended_term_list]
    symbolic_name_set = {
        "one",
        "torque",
        "speed",
        "temperature",
        "torque_speed",
        "torque_temperature",
        "speed_temperature",
        "torque_speed_temperature",
        "torque_signed_magnitude",
        "speed_signed_magnitude",
        "temperature_signed_magnitude",
        "torque_signed_log",
        "speed_signed_log",
        "temperature_signed_log",
        "torque_bounded",
        "speed_bounded",
        "temperature_bounded",
    }
    return [
        term
        for term in [*quadratic_term_list, *extended_term_list]
        if term.name in symbolic_name_set
    ]


def normalize_conditions(
    condition_matrix: np.ndarray,
    feature_mean: np.ndarray,
    feature_scale: np.ndarray,
) -> np.ndarray:
    """Normalize torque, speed, and temperature conditions."""

    condition_array = np.asarray(condition_matrix, dtype=np.float64)
    mean_array = np.asarray(feature_mean, dtype=np.float64)
    scale_array = np.asarray(feature_scale, dtype=np.float64)
    assert condition_array.ndim == 2
    assert condition_array.shape[1] == 3
    assert mean_array.shape == (3,)
    assert scale_array.shape == (3,)
    assert np.all(scale_array > MINIMUM_SCALE)
    normalized_matrix = (
        condition_array - mean_array[np.newaxis, :]
    ) / scale_array[np.newaxis, :]
    assert np.all(np.isfinite(normalized_matrix))
    return normalized_matrix


def _term_value_map(
    normalized_condition_matrix: np.ndarray,
) -> dict[str, np.ndarray]:
    """Evaluate every supported named condition term."""

    torque = normalized_condition_matrix[:, 0]
    speed = normalized_condition_matrix[:, 1]
    temperature = normalized_condition_matrix[:, 2]
    return {
        "one": np.ones(normalized_condition_matrix.shape[0]),
        "torque": torque,
        "speed": speed,
        "temperature": temperature,
        "torque_sq": torque**2,
        "speed_sq": speed**2,
        "temperature_sq": temperature**2,
        "torque_speed": torque * speed,
        "torque_temperature": torque * temperature,
        "speed_temperature": speed * temperature,
        "torque_cube": torque**3,
        "speed_cube": speed**3,
        "temperature_cube": temperature**3,
        "torque_speed_temperature": torque * speed * temperature,
        "torque_sq_speed": torque**2 * speed,
        "torque_sq_temperature": torque**2 * temperature,
        "speed_sq_torque": speed**2 * torque,
        "speed_sq_temperature": speed**2 * temperature,
        "temperature_sq_torque": temperature**2 * torque,
        "temperature_sq_speed": temperature**2 * speed,
        "torque_signed_magnitude": torque * np.abs(torque),
        "speed_signed_magnitude": speed * np.abs(speed),
        "temperature_signed_magnitude": temperature * np.abs(temperature),
        "torque_signed_log": np.sign(torque) * np.log1p(np.abs(torque)),
        "speed_signed_log": np.sign(speed) * np.log1p(np.abs(speed)),
        "temperature_signed_log": (
            np.sign(temperature) * np.log1p(np.abs(temperature))
        ),
        "torque_bounded": torque / (1.0 + np.abs(torque)),
        "speed_bounded": speed / (1.0 + np.abs(speed)),
        "temperature_bounded": temperature / (
            1.0 + np.abs(temperature)
        ),
    }


def evaluate_condition_library(
    normalized_condition_matrix: np.ndarray,
    term_list: list[NamedConditionTerm],
) -> np.ndarray:
    """Evaluate one named term library."""

    value_map = _term_value_map(
        np.asarray(normalized_condition_matrix, dtype=np.float64)
    )
    assert len({term.name for term in term_list}) == len(term_list)
    library_matrix = np.column_stack(
        [value_map[term.name] for term in term_list]
    )
    assert library_matrix.shape == (
        normalized_condition_matrix.shape[0],
        len(term_list),
    )
    assert np.all(np.isfinite(library_matrix))
    return library_matrix


def compute_library_scale(
    training_library_matrix: np.ndarray,
) -> np.ndarray:
    """Compute stable train-only column scales while preserving the intercept."""

    library_matrix = np.asarray(training_library_matrix, dtype=np.float64)
    scale_array = np.sqrt(np.mean(library_matrix**2, axis=0))
    scale_array = np.maximum(scale_array, MINIMUM_SCALE)
    scale_array[0] = 1.0
    return scale_array


def fit_ridge_coefficients(
    normalized_library_matrix: np.ndarray,
    normalized_target_matrix: np.ndarray,
    alpha: float,
    active_mask: np.ndarray | None = None,
) -> np.ndarray:
    """Fit deterministic multi-output ridge coefficients."""

    library_matrix = np.asarray(
        normalized_library_matrix,
        dtype=np.float64,
    )
    target_matrix = np.asarray(normalized_target_matrix, dtype=np.float64)
    assert library_matrix.ndim == 2
    assert target_matrix.ndim == 2
    assert library_matrix.shape[0] == target_matrix.shape[0]
    assert alpha >= 0.0
    term_count = library_matrix.shape[1]
    output_count = target_matrix.shape[1]
    if active_mask is None:
        active_mask = np.ones((term_count, output_count), dtype=bool)
    assert active_mask.shape == (term_count, output_count)
    coefficient_matrix = np.zeros((term_count, output_count), dtype=np.float64)
    for output_index in range(output_count):
        selected_index_array = np.flatnonzero(active_mask[:, output_index])
        if selected_index_array.size == 0:
            selected_index_array = np.asarray([0], dtype=np.int64)
        selected_library_matrix = library_matrix[:, selected_index_array]
        gram_matrix = selected_library_matrix.T @ selected_library_matrix
        regularization_matrix = alpha * np.eye(
            selected_index_array.size,
            dtype=np.float64,
        )
        intercept_position_array = np.flatnonzero(
            selected_index_array == 0
        )
        regularization_matrix[
            intercept_position_array,
            intercept_position_array,
        ] = 0.0
        right_hand_side = (
            selected_library_matrix.T @ target_matrix[:, output_index]
        )
        try:
            selected_coefficient_array = np.linalg.solve(
                gram_matrix + regularization_matrix,
                right_hand_side,
            )
        except np.linalg.LinAlgError:
            selected_coefficient_array = np.linalg.lstsq(
                gram_matrix + regularization_matrix,
                right_hand_side,
                rcond=None,
            )[0]
        coefficient_matrix[
            selected_index_array,
            output_index,
        ] = selected_coefficient_array
    assert np.all(np.isfinite(coefficient_matrix))
    return coefficient_matrix


def fit_sequential_thresholded_ridge(
    normalized_library_matrix: np.ndarray,
    normalized_target_matrix: np.ndarray,
    alpha: float,
    threshold: float,
    maximum_iteration_count: int = DEFAULT_MAXIMUM_THRESHOLD_ITERATIONS,
) -> SparseFitResult:
    """Fit one sequential thresholded-ridge multi-output law."""

    assert threshold >= 0.0
    term_count = normalized_library_matrix.shape[1]
    output_count = normalized_target_matrix.shape[1]
    active_mask = np.ones((term_count, output_count), dtype=bool)
    active_mask[0, :] = True
    coefficient_matrix = np.zeros_like(active_mask, dtype=np.float64)
    for _ in range(maximum_iteration_count):
        coefficient_matrix = fit_ridge_coefficients(
            normalized_library_matrix,
            normalized_target_matrix,
            alpha,
            active_mask,
        )
        next_active_mask = np.abs(coefficient_matrix) >= threshold
        next_active_mask[0, :] = True
        empty_output_mask = np.sum(next_active_mask, axis=0) == 0
        next_active_mask[0, empty_output_mask] = True
        if np.array_equal(next_active_mask, active_mask):
            break
        active_mask = next_active_mask
    coefficient_matrix = fit_ridge_coefficients(
        normalized_library_matrix,
        normalized_target_matrix,
        alpha,
        active_mask,
    )
    selected_mask = np.abs(coefficient_matrix) > 0.0
    return SparseFitResult(
        coefficient_matrix=coefficient_matrix,
        active_mask=selected_mask,
        selection_probability=selected_mask.astype(np.float64),
        sign_agreement=np.ones_like(coefficient_matrix),
        median_normalized_magnitude=np.abs(coefficient_matrix),
        alpha=alpha,
        threshold=threshold,
    )


def run_bootstrap_stability_selection(
    normalized_library_matrix: np.ndarray,
    normalized_target_matrix: np.ndarray,
    alpha: float,
    threshold: float,
    bootstrap_count: int,
    random_seed: int,
) -> SparseFitResult:
    """Run deterministic row-bootstrap sparse stability selection."""

    assert bootstrap_count > 1
    generator = np.random.default_rng(random_seed)
    row_count = normalized_library_matrix.shape[0]
    bootstrap_coefficient_list: list[np.ndarray] = []
    for _ in range(bootstrap_count):
        bootstrap_index_array = generator.choice(
            row_count,
            size=row_count,
            replace=True,
        )
        bootstrap_result = fit_sequential_thresholded_ridge(
            normalized_library_matrix[bootstrap_index_array],
            normalized_target_matrix[bootstrap_index_array],
            alpha,
            threshold,
        )
        bootstrap_coefficient_list.append(
            bootstrap_result.coefficient_matrix
        )
    bootstrap_coefficient_tensor = np.stack(
        bootstrap_coefficient_list,
        axis=0,
    )
    selected_tensor = np.abs(bootstrap_coefficient_tensor) > 0.0
    selection_probability = np.mean(selected_tensor, axis=0)
    median_coefficient_matrix = np.median(
        bootstrap_coefficient_tensor,
        axis=0,
    )
    median_sign_matrix = np.sign(median_coefficient_matrix)
    matching_sign_tensor = (
        np.sign(bootstrap_coefficient_tensor)
        == median_sign_matrix[np.newaxis, :, :]
    ) & selected_tensor
    selected_count_matrix = np.sum(selected_tensor, axis=0)
    sign_agreement = np.divide(
        np.sum(matching_sign_tensor, axis=0),
        np.maximum(selected_count_matrix, 1),
    )
    median_normalized_magnitude = np.median(
        np.abs(bootstrap_coefficient_tensor),
        axis=0,
    )
    return SparseFitResult(
        coefficient_matrix=median_coefficient_matrix,
        active_mask=selected_count_matrix > 0,
        selection_probability=selection_probability,
        sign_agreement=sign_agreement,
        median_normalized_magnitude=median_normalized_magnitude,
        alpha=alpha,
        threshold=threshold,
    )


def build_stable_active_mask(
    stability_result: SparseFitResult,
    minimum_selection_probability: float,
    minimum_sign_agreement: float,
    minimum_median_magnitude: float,
) -> np.ndarray:
    """Build the stable term-output mask from frozen thresholds."""

    active_mask = (
        (
            stability_result.selection_probability
            >= minimum_selection_probability
        )
        & (stability_result.sign_agreement >= minimum_sign_agreement)
        & (
            stability_result.median_normalized_magnitude
            >= minimum_median_magnitude
        )
    )
    active_mask[0, :] = True
    return active_mask


def enforce_strong_hierarchy(
    active_mask: np.ndarray,
    term_list: list[NamedConditionTerm],
) -> np.ndarray:
    """Add all parent terms required by selected interactions."""

    hierarchical_mask = np.asarray(active_mask, dtype=bool).copy()
    term_index_map = {
        term.name: term_index
        for term_index, term in enumerate(term_list)
    }
    changed = True
    while changed:
        changed = False
        for term_index, term in enumerate(term_list):
            selected_output_index_array = np.flatnonzero(
                hierarchical_mask[term_index]
            )
            if selected_output_index_array.size == 0:
                continue
            for parent_name in term.parent_name_list:
                parent_index = term_index_map.get(parent_name)
                if parent_index is None:
                    continue
                previous_mask = hierarchical_mask[
                    parent_index,
                    selected_output_index_array,
                ].copy()
                hierarchical_mask[
                    parent_index,
                    selected_output_index_array,
                ] = True
                if not np.all(previous_mask):
                    changed = True
    hierarchical_mask[0, :] = True
    return hierarchical_mask


def reconstruct_curve_matrix(
    coefficient_matrix: np.ndarray,
    harmonic_order_list: list[int],
    angular_sample_count: int,
) -> np.ndarray:
    """Reconstruct periodic curves from offset/cosine/sine coefficients."""

    coefficient_array = np.asarray(coefficient_matrix, dtype=np.float64)
    expected_coefficient_count = 1 + 2 * len(harmonic_order_list)
    assert coefficient_array.ndim == 2
    assert coefficient_array.shape[1] == expected_coefficient_count
    angle_array = np.linspace(
        0.0,
        2.0 * np.pi,
        angular_sample_count,
        endpoint=False,
    )
    curve_matrix = np.repeat(
        coefficient_array[:, 0:1],
        angular_sample_count,
        axis=1,
    )
    for order_index, harmonic_order in enumerate(harmonic_order_list):
        sine_coefficient = coefficient_array[:, 1 + 2 * order_index]
        cosine_coefficient = coefficient_array[:, 2 + 2 * order_index]
        curve_matrix += (
            sine_coefficient[:, np.newaxis]
            * np.sin(harmonic_order * angle_array)[np.newaxis, :]
        )
        curve_matrix += (
            cosine_coefficient[:, np.newaxis]
            * np.cos(harmonic_order * angle_array)[np.newaxis, :]
        )
    assert np.all(np.isfinite(curve_matrix))
    return curve_matrix


def serialize_term_list(
    term_list: list[NamedConditionTerm],
) -> list[dict[str, Any]]:
    """Serialize named terms for immutable campaign artifacts."""

    return [
        {
            "name": term.name,
            "expression": term.expression,
            "parent_name_list": list(term.parent_name_list),
            "library_group": term.library_group,
        }
        for term in term_list
    ]
