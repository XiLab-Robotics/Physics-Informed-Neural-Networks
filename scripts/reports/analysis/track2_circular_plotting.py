"""Shared circular-angle plotting helpers for Track 2 visual reports."""

from __future__ import annotations

# Import Python Utilities
from typing import Any

# Import Scientific Python Utilities
import numpy as np


DEFAULT_CIRCULAR_PERIOD_DEG = 360.0
DEFAULT_WRAP_THRESHOLD_DEG = 180.0


def split_circular_angle_curve_segments(
    angular_position_deg: np.ndarray,
    curve_value_deg: np.ndarray,
    wrap_threshold_deg: float = DEFAULT_WRAP_THRESHOLD_DEG,
) -> list[tuple[np.ndarray, np.ndarray]]:

    """Split one angular curve into visually continuous circular segments.

    Args:
        angular_position_deg: Ordered angular positions in degrees.
        curve_value_deg: Curve values aligned with `angular_position_deg`.
        wrap_threshold_deg: Absolute angular jump that marks a circular wrap.

    Returns:
        List of `(angular_segment, curve_segment)` arrays safe to plot without
        drawing a nonphysical line across the circular boundary.
    """

    # Normalize Inputs
    angle_array = np.asarray(angular_position_deg, dtype=np.float64).reshape(-1)
    curve_array = np.asarray(curve_value_deg, dtype=np.float64).reshape(-1)
    assert angle_array.shape == curve_array.shape, (
        "Angular and curve arrays must have the same shape | "
        f"{angle_array.shape} vs {curve_array.shape}"
    )

    if angle_array.size <= 1:
        return [(angle_array, curve_array)]

    # Detect Circular Wraps
    angle_delta_array = np.diff(angle_array)
    split_index_array = np.flatnonzero(np.abs(angle_delta_array) > float(wrap_threshold_deg)) + 1
    if split_index_array.size == 0:
        return [(angle_array, curve_array)]

    split_index_list = [int(index_value) for index_value in split_index_array]
    angle_segment_list = np.split(angle_array, split_index_list)
    curve_segment_list = np.split(curve_array, split_index_list)
    return list(zip(angle_segment_list, curve_segment_list))


def plot_circular_angle_curve(
    axis: Any,
    angular_position_deg: np.ndarray,
    curve_value_deg: np.ndarray,
    **plot_keyword_arguments: Any,
) -> list[Any]:

    """Plot a circular angular curve without connecting across wrap boundaries.

    Args:
        axis: Matplotlib axis object.
        angular_position_deg: Ordered angular positions in degrees.
        curve_value_deg: Curve values aligned with `angular_position_deg`.
        **plot_keyword_arguments: Keyword arguments passed to `axis.plot`.

    Returns:
        List of Matplotlib line objects returned by the segment plot calls.
    """

    line_list: list[Any] = []
    segment_list = split_circular_angle_curve_segments(angular_position_deg, curve_value_deg)

    for segment_index, (angle_segment, curve_segment) in enumerate(segment_list):
        segment_plot_arguments = dict(plot_keyword_arguments)
        if segment_index > 0 and "label" in segment_plot_arguments:
            segment_plot_arguments["label"] = "_nolegend_"
        line_list.extend(axis.plot(angle_segment, curve_segment, **segment_plot_arguments))

    return line_list
