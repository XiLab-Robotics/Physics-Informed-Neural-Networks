"""Calibrate causal uncertainty and physics-trust signals for TE curves."""

from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from typing import Any

# Import Numerical And Statistical Utilities
import numpy as np
from scipy.stats import spearmanr
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import average_precision_score
from sklearn.model_selection import KFold


# Define Stable Numerical Constants
MINIMUM_POSITIVE_SCALE = 1.0e-9
DEFAULT_CONFORMAL_LEVEL_LIST = (0.50, 0.80, 0.90, 0.95)
DEFAULT_RIDGE_ALPHA_LIST = (1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1, 1.0, 10.0)


@dataclass(frozen=True)
class IsotonicCalibrationState:
    """Store a portable monotonic calibration map."""

    x_threshold_array: np.ndarray
    y_threshold_array: np.ndarray
    constant_value: float | None


@dataclass(frozen=True)
class CompositeTrustState:
    """Store one validation-fitted nonnegative composite estimator."""

    feature_mean: np.ndarray
    feature_scale: np.ndarray
    coefficient_array: np.ndarray
    intercept: float
    selected_alpha: float
    calibration_state: IsotonicCalibrationState


def calculate_nearest_training_distance(
    condition_matrix: np.ndarray,
    training_condition_matrix: np.ndarray,
    feature_mean: np.ndarray,
    feature_scale: np.ndarray,
) -> np.ndarray:
    """Calculate standardized nearest-training-condition distances.

    Args:
        condition_matrix: Query torque, speed, and temperature rows.
        training_condition_matrix: Training-only operating-condition rows.
        feature_mean: Training-only feature means.
        feature_scale: Training-only feature standard deviations.

    Returns:
        One nonnegative distance per query row.
    """

    query = (
        np.asarray(condition_matrix, dtype=np.float64)
        - np.asarray(feature_mean, dtype=np.float64)
    ) / np.asarray(feature_scale, dtype=np.float64)
    training = (
        np.asarray(training_condition_matrix, dtype=np.float64)
        - np.asarray(feature_mean, dtype=np.float64)
    ) / np.asarray(feature_scale, dtype=np.float64)
    squared_distance_matrix = np.sum(
        (query[:, np.newaxis, :] - training[np.newaxis, :, :]) ** 2,
        axis=2,
    )
    return np.sqrt(np.min(squared_distance_matrix, axis=1))


def calculate_support_boundary_score(
    condition_matrix: np.ndarray,
    training_condition_matrix: np.ndarray,
    feature_mean: np.ndarray,
    feature_scale: np.ndarray,
    density_threshold: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Build a support-aware score and machine-readable tier labels."""

    condition_array = np.asarray(condition_matrix, dtype=np.float64)
    training_array = np.asarray(
        training_condition_matrix,
        dtype=np.float64,
    )
    normalized_condition = (
        condition_array - np.asarray(feature_mean, dtype=np.float64)
    ) / np.asarray(feature_scale, dtype=np.float64)
    normalized_training = (
        training_array - np.asarray(feature_mean, dtype=np.float64)
    ) / np.asarray(feature_scale, dtype=np.float64)
    normalized_minimum = np.min(normalized_training, axis=0)
    normalized_maximum = np.max(normalized_training, axis=0)
    nearest_distance = calculate_nearest_training_distance(
        condition_array,
        training_array,
        feature_mean,
        feature_scale,
    )

    lower_excess = np.maximum(
        normalized_minimum[np.newaxis, :] - normalized_condition,
        0.0,
    )
    upper_excess = np.maximum(
        normalized_condition - normalized_maximum[np.newaxis, :],
        0.0,
    )
    outside_distance = np.linalg.vector_norm(
        lower_excess + upper_excess,
        axis=1,
    )
    lower_margin = normalized_condition - normalized_minimum[np.newaxis, :]
    upper_margin = normalized_maximum[np.newaxis, :] - normalized_condition
    inside_margin = np.min(
        np.minimum(lower_margin, upper_margin),
        axis=1,
    )
    boundary_proximity = 1.0 / np.maximum(inside_margin + 0.25, 0.05)
    density_ratio = nearest_distance / max(
        float(density_threshold),
        MINIMUM_POSITIVE_SCALE,
    )
    score = (
        density_ratio
        + 2.0 * outside_distance
        + 0.10 * boundary_proximity
    )

    outside_mask = np.any(
        (normalized_condition < normalized_minimum[np.newaxis, :])
        | (normalized_condition > normalized_maximum[np.newaxis, :]),
        axis=1,
    )
    sparse_mask = (
        ~outside_mask
        & (nearest_distance > float(density_threshold))
    )
    tier_array = np.full(
        condition_array.shape[0],
        "supported_core",
        dtype=object,
    )
    tier_array[sparse_mask] = "supported_sparse_or_corner"
    tier_array[outside_mask] = "unsupported_extrapolation"
    return score, tier_array.astype(str)


def calculate_curve_disagreement(
    first_curve_matrix: np.ndarray,
    second_curve_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Calculate curvewise and pointwise absolute model disagreement."""

    pointwise = np.abs(
        np.asarray(first_curve_matrix, dtype=np.float64)
        - np.asarray(second_curve_matrix, dtype=np.float64)
    )
    assert pointwise.ndim == 2
    return np.mean(pointwise, axis=1), pointwise


def calculate_ensemble_spread(
    prediction_tensor: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Calculate curvewise and pointwise seed-ensemble standard deviation."""

    prediction_array = np.asarray(prediction_tensor, dtype=np.float64)
    assert prediction_array.ndim == 3
    assert prediction_array.shape[0] >= 2
    pointwise_spread = np.std(prediction_array, axis=0, ddof=1)
    curve_spread = np.mean(pointwise_spread, axis=1)
    return curve_spread, pointwise_spread


def fit_isotonic_error_calibrator(
    raw_score_array: np.ndarray,
    curve_error_array: np.ndarray,
) -> IsotonicCalibrationState:
    """Fit a monotonic validation-only error scale."""

    raw_score = np.asarray(raw_score_array, dtype=np.float64).reshape(-1)
    curve_error = np.asarray(curve_error_array, dtype=np.float64).reshape(-1)
    assert raw_score.shape == curve_error.shape
    assert np.all(np.isfinite(raw_score))
    assert np.all(np.isfinite(curve_error))
    if np.ptp(raw_score) <= MINIMUM_POSITIVE_SCALE:
        return IsotonicCalibrationState(
            x_threshold_array=np.asarray([], dtype=np.float64),
            y_threshold_array=np.asarray([], dtype=np.float64),
            constant_value=float(np.mean(curve_error)),
        )
    model = IsotonicRegression(
        y_min=MINIMUM_POSITIVE_SCALE,
        increasing=True,
        out_of_bounds="clip",
    )
    model.fit(raw_score, curve_error)
    return IsotonicCalibrationState(
        x_threshold_array=np.asarray(
            model.X_thresholds_,
            dtype=np.float64,
        ),
        y_threshold_array=np.asarray(
            model.y_thresholds_,
            dtype=np.float64,
        ),
        constant_value=None,
    )


def apply_isotonic_error_calibrator(
    state: IsotonicCalibrationState,
    raw_score_array: np.ndarray,
) -> np.ndarray:
    """Apply a portable isotonic calibration map."""

    raw_score = np.asarray(raw_score_array, dtype=np.float64).reshape(-1)
    if state.constant_value is not None:
        return np.full(
            raw_score.shape,
            max(state.constant_value, MINIMUM_POSITIVE_SCALE),
            dtype=np.float64,
        )
    assert state.x_threshold_array.size >= 2
    calibrated = np.interp(
        raw_score,
        state.x_threshold_array,
        state.y_threshold_array,
        left=state.y_threshold_array[0],
        right=state.y_threshold_array[-1],
    )
    return np.maximum(calibrated, MINIMUM_POSITIVE_SCALE)


def _standardize_composite_features(
    feature_matrix: np.ndarray,
    feature_mean: np.ndarray,
    feature_scale: np.ndarray,
) -> np.ndarray:
    """Apply one stable composite-feature standardization."""

    return (
        np.asarray(feature_matrix, dtype=np.float64)
        - np.asarray(feature_mean, dtype=np.float64)
    ) / np.asarray(feature_scale, dtype=np.float64)


def fit_composite_trust_estimator(
    validation_feature_matrix: np.ndarray,
    validation_curve_error_array: np.ndarray,
    random_seed: int,
    alpha_list: tuple[float, ...] = DEFAULT_RIDGE_ALPHA_LIST,
) -> CompositeTrustState:
    """Fit a nonnegative ridge estimator with deterministic inner CV."""

    feature_matrix = np.asarray(
        validation_feature_matrix,
        dtype=np.float64,
    )
    curve_error = np.asarray(
        validation_curve_error_array,
        dtype=np.float64,
    ).reshape(-1)
    assert feature_matrix.ndim == 2
    assert feature_matrix.shape[0] == curve_error.size
    feature_mean = np.mean(feature_matrix, axis=0)
    feature_scale = np.maximum(
        np.std(feature_matrix, axis=0),
        MINIMUM_POSITIVE_SCALE,
    )
    standardized = _standardize_composite_features(
        feature_matrix,
        feature_mean,
        feature_scale,
    )
    fold_splitter = KFold(
        n_splits=5,
        shuffle=True,
        random_state=random_seed,
    )
    scored_alpha_list: list[tuple[float, float]] = []
    for alpha in alpha_list:
        fold_error_list: list[float] = []
        for training_index, evaluation_index in fold_splitter.split(
            standardized
        ):
            model = Ridge(
                alpha=alpha,
                fit_intercept=True,
                positive=True,
                solver="lbfgs",
                max_iter=15000,
                tol=1.0e-8,
            )
            model.fit(
                standardized[training_index],
                curve_error[training_index],
            )
            prediction = model.predict(standardized[evaluation_index])
            fold_error_list.append(
                float(
                    np.mean(
                        np.abs(
                            prediction - curve_error[evaluation_index]
                        )
                    )
                )
            )
        scored_alpha_list.append((float(np.mean(fold_error_list)), alpha))
    _, selected_alpha = min(scored_alpha_list)
    final_model = Ridge(
        alpha=selected_alpha,
        fit_intercept=True,
        positive=True,
        solver="lbfgs",
        max_iter=15000,
        tol=1.0e-8,
    )
    final_model.fit(standardized, curve_error)
    raw_validation_prediction = final_model.predict(standardized)
    calibration_state = fit_isotonic_error_calibrator(
        raw_validation_prediction,
        curve_error,
    )
    return CompositeTrustState(
        feature_mean=feature_mean,
        feature_scale=feature_scale,
        coefficient_array=np.asarray(
            final_model.coef_,
            dtype=np.float64,
        ),
        intercept=float(final_model.intercept_),
        selected_alpha=float(selected_alpha),
        calibration_state=calibration_state,
    )


def apply_composite_trust_estimator(
    state: CompositeTrustState,
    feature_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Apply the raw and calibrated composite trust estimator."""

    standardized = _standardize_composite_features(
        feature_matrix,
        state.feature_mean,
        state.feature_scale,
    )
    raw_prediction = (
        standardized @ state.coefficient_array + state.intercept
    )
    calibrated_prediction = apply_isotonic_error_calibrator(
        state.calibration_state,
        raw_prediction,
    )
    return raw_prediction, calibrated_prediction


def calculate_curve_error(
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
) -> np.ndarray:
    """Calculate one mean absolute error per complete curve."""

    return np.mean(
        np.abs(
            np.asarray(measured_curve_matrix, dtype=np.float64)
            - np.asarray(predicted_curve_matrix, dtype=np.float64)
        ),
        axis=1,
    )


def calculate_risk_coverage_curve(
    uncertainty_score_array: np.ndarray,
    curve_error_array: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Calculate selective risk after retaining low-uncertainty curves."""

    score = np.asarray(
        uncertainty_score_array,
        dtype=np.float64,
    ).reshape(-1)
    curve_error = np.asarray(
        curve_error_array,
        dtype=np.float64,
    ).reshape(-1)
    order = np.argsort(score, kind="mergesort")
    ordered_error = curve_error[order]
    retained_count = np.arange(1, ordered_error.size + 1)
    coverage = retained_count / ordered_error.size
    risk = np.cumsum(ordered_error) / retained_count
    return coverage, risk


def _risk_at_coverage(
    coverage_array: np.ndarray,
    risk_array: np.ndarray,
    requested_coverage: float,
) -> float:
    """Return risk at the largest retained set within requested coverage."""

    index = int(
        np.clip(
            np.searchsorted(
                coverage_array,
                requested_coverage,
                side="right",
            )
            - 1,
            0,
            coverage_array.size - 1,
        )
    )
    return float(risk_array[index])


def evaluate_localization_metrics(
    uncertainty_score_array: np.ndarray,
    curve_error_array: np.ndarray,
) -> dict[str, float]:
    """Evaluate rank, high-error capture, and selective-risk metrics."""

    score = np.asarray(
        uncertainty_score_array,
        dtype=np.float64,
    ).reshape(-1)
    curve_error = np.asarray(
        curve_error_array,
        dtype=np.float64,
    ).reshape(-1)
    assert score.shape == curve_error.shape
    high_error_threshold = float(
        np.quantile(curve_error, 0.80, method="higher")
    )
    high_error_label = curve_error >= high_error_threshold
    high_error_prevalence = float(np.mean(high_error_label))
    if np.ptp(score) <= MINIMUM_POSITIVE_SCALE:
        unfiltered_curve_mae = float(np.mean(curve_error))
        return {
            "spearman_correlation": 0.0,
            "spearman_pvalue": 1.0,
            "high_error_threshold_deg": high_error_threshold,
            "top_quintile_average_precision": high_error_prevalence,
            "top_20_percent_error_capture_rate": 0.20,
            "normalized_area_under_risk_coverage": 1.0,
            "unfiltered_curve_mae_deg": unfiltered_curve_mae,
            "selective_curve_mae_95_percent_deg": unfiltered_curve_mae,
            "selective_curve_mae_90_percent_deg": unfiltered_curve_mae,
            "selective_curve_mae_80_percent_deg": unfiltered_curve_mae,
            "selective_curve_mae_60_percent_deg": unfiltered_curve_mae,
        }
    result = spearmanr(score, curve_error)
    spearman_correlation = float(result.statistic)
    spearman_pvalue = float(result.pvalue)

    selected_count = max(1, int(np.ceil(0.20 * curve_error.size)))
    selected_index = np.argsort(score, kind="mergesort")[-selected_count:]
    high_error_count = int(np.sum(high_error_label))
    capture_rate = float(
        np.sum(high_error_label[selected_index]) / max(high_error_count, 1)
    )
    average_precision = float(
        average_precision_score(high_error_label.astype(int), score)
    )
    coverage, risk = calculate_risk_coverage_curve(score, curve_error)
    normalized_aurc = float(
        np.trapezoid(risk, coverage)
        / max(float(np.mean(curve_error)), MINIMUM_POSITIVE_SCALE)
    )
    return {
        "spearman_correlation": spearman_correlation,
        "spearman_pvalue": spearman_pvalue,
        "high_error_threshold_deg": high_error_threshold,
        "top_quintile_average_precision": average_precision,
        "top_20_percent_error_capture_rate": capture_rate,
        "normalized_area_under_risk_coverage": normalized_aurc,
        "unfiltered_curve_mae_deg": float(np.mean(curve_error)),
        "selective_curve_mae_95_percent_deg": _risk_at_coverage(
            coverage,
            risk,
            0.95,
        ),
        "selective_curve_mae_90_percent_deg": _risk_at_coverage(
            coverage,
            risk,
            0.90,
        ),
        "selective_curve_mae_80_percent_deg": _risk_at_coverage(
            coverage,
            risk,
            0.80,
        ),
        "selective_curve_mae_60_percent_deg": _risk_at_coverage(
            coverage,
            risk,
            0.60,
        ),
    }


def finite_sample_quantile(
    value_array: np.ndarray,
    coverage_level: float,
) -> float:
    """Return a conservative split-conformal finite-sample quantile."""

    value = np.asarray(value_array, dtype=np.float64).reshape(-1)
    assert value.size > 0
    assert 0.0 < coverage_level < 1.0
    adjusted_level = min(
        1.0,
        np.ceil((value.size + 1) * coverage_level) / value.size,
    )
    return float(np.quantile(value, adjusted_level, method="higher"))


def fit_conformal_quantiles(
    calibration_residual_matrix: np.ndarray,
    calibration_curve_scale_array: np.ndarray,
    level_list: tuple[float, ...] = DEFAULT_CONFORMAL_LEVEL_LIST,
) -> dict[str, Any]:
    """Fit normalized marginal and simultaneous conformal quantiles."""

    residual = np.abs(
        np.asarray(calibration_residual_matrix, dtype=np.float64)
    )
    curve_scale = np.maximum(
        np.asarray(
            calibration_curve_scale_array,
            dtype=np.float64,
        ).reshape(-1),
        MINIMUM_POSITIVE_SCALE,
    )
    assert residual.shape[0] == curve_scale.size
    normalized_residual = residual / curve_scale[:, np.newaxis]
    marginal_quantile_map = {
        f"{int(round(level * 100))}": finite_sample_quantile(
            normalized_residual.reshape(-1),
            level,
        )
        for level in level_list
    }
    simultaneous_score = np.max(normalized_residual, axis=1)
    simultaneous_quantile = finite_sample_quantile(
        simultaneous_score,
        0.90,
    )
    return {
        "marginal_quantile_map": marginal_quantile_map,
        "simultaneous_90_quantile": simultaneous_quantile,
    }


def evaluate_conformal_intervals(
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
    curve_scale_array: np.ndarray,
    conformal_payload: dict[str, Any],
) -> dict[str, float]:
    """Evaluate marginal and complete-curve conformal coverage."""

    measured = np.asarray(measured_curve_matrix, dtype=np.float64)
    predicted = np.asarray(predicted_curve_matrix, dtype=np.float64)
    curve_scale = np.maximum(
        np.asarray(curve_scale_array, dtype=np.float64).reshape(-1),
        MINIMUM_POSITIVE_SCALE,
    )
    assert measured.shape == predicted.shape
    assert measured.shape[0] == curve_scale.size
    absolute_residual = np.abs(measured - predicted)
    metric_payload: dict[str, float] = {}
    marginal_quantile_map = conformal_payload["marginal_quantile_map"]
    for level_name, quantile in marginal_quantile_map.items():
        half_width = curve_scale[:, np.newaxis] * float(quantile)
        metric_payload[
            f"marginal_{level_name}_coverage"
        ] = float(np.mean(absolute_residual <= half_width))
        metric_payload[
            f"marginal_{level_name}_mean_width_deg"
        ] = float(2.0 * np.mean(half_width))
    simultaneous_half_width = (
        curve_scale[:, np.newaxis]
        * float(conformal_payload["simultaneous_90_quantile"])
    )
    metric_payload["simultaneous_90_curve_coverage"] = float(
        np.mean(
            np.all(
                absolute_residual <= simultaneous_half_width,
                axis=1,
            )
        )
    )
    metric_payload["simultaneous_90_mean_width_deg"] = float(
        2.0 * np.mean(simultaneous_half_width)
    )
    return metric_payload


def evaluate_group_metrics(
    group_array: np.ndarray,
    uncertainty_score_array: np.ndarray,
    curve_error_array: np.ndarray,
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
    curve_scale_array: np.ndarray,
    conformal_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """Evaluate localization and interval evidence by declared subgroup."""

    group = np.asarray(group_array).astype(str)
    row_list: list[dict[str, Any]] = []
    marginal_90_quantile = float(
        conformal_payload["marginal_quantile_map"]["90"]
    )
    absolute_residual = np.abs(
        np.asarray(measured_curve_matrix, dtype=np.float64)
        - np.asarray(predicted_curve_matrix, dtype=np.float64)
    )
    curve_scale = np.asarray(
        curve_scale_array,
        dtype=np.float64,
    ).reshape(-1)
    for group_name in sorted(set(group.tolist())):
        mask = group == group_name
        count = int(np.sum(mask))
        score = np.asarray(
            uncertainty_score_array,
            dtype=np.float64,
        )[mask]
        error = np.asarray(curve_error_array, dtype=np.float64)[mask]
        if count >= 3 and np.ptp(score) > MINIMUM_POSITIVE_SCALE:
            rank_result = spearmanr(score, error)
            rank_correlation = float(rank_result.statistic)
        else:
            rank_correlation = 0.0
        half_width = (
            curve_scale[mask, np.newaxis] * marginal_90_quantile
        )
        row_list.append(
            {
                "group": group_name,
                "curve_count": count,
                "curve_mae_deg": float(np.mean(error)),
                "mean_uncertainty_score": float(np.mean(score)),
                "spearman_correlation": rank_correlation,
                "marginal_90_coverage": float(
                    np.mean(absolute_residual[mask] <= half_width)
                ),
                "marginal_90_mean_width_deg": float(
                    2.0 * np.mean(half_width)
                ),
            }
        )
    return row_list


def serialize_isotonic_state(
    state: IsotonicCalibrationState,
) -> dict[str, Any]:
    """Serialize one portable isotonic calibration state."""

    return {
        "x_threshold_list": state.x_threshold_array.tolist(),
        "y_threshold_list": state.y_threshold_array.tolist(),
        "constant_value": state.constant_value,
    }


def serialize_composite_state(
    state: CompositeTrustState,
) -> dict[str, Any]:
    """Serialize one portable composite estimator state."""

    return {
        "feature_mean_list": state.feature_mean.tolist(),
        "feature_scale_list": state.feature_scale.tolist(),
        "coefficient_list": state.coefficient_array.tolist(),
        "intercept": state.intercept,
        "selected_alpha": state.selected_alpha,
        "calibration": serialize_isotonic_state(
            state.calibration_state
        ),
    }
