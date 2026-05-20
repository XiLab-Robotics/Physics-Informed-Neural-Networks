"""Smoke checks for harmonic-basis model configuration."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import PyTorch Utilities
import torch

# Import Project Models
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.model_factory import create_model

RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]

def assert_harmonic_model_shape(model: HarmonicRegression, expected_feature_count: int) -> None:

    """Assert one harmonic-regression configuration has the expected shape.

    Args:
        model: Harmonic regression model instance to inspect.
        expected_feature_count: Expected bias plus sine/cosine feature count.
    """

    # Validate Feature And Parameter Shapes
    assert model.harmonic_feature_count == expected_feature_count, (
        f"Unexpected harmonic feature count | {model.harmonic_feature_count} != {expected_feature_count}"
    )
    assert model.base_coefficient_tensor.shape[0] == expected_feature_count, (
        f"Unexpected coefficient count | {model.base_coefficient_tensor.shape[0]} != {expected_feature_count}"
    )

    # Validate Forward Output Shape
    input_tensor = torch.tensor(
        [
            [0.0, 100.0, 25.0, 30.0, 1.0],
            [90.0, 200.0, 30.0, 35.0, 0.0],
        ],
        dtype=torch.float32,
    )
    prediction_tensor = model.forward_with_input_context(input_tensor, input_tensor)
    assert tuple(prediction_tensor.shape) == (2, 1), f"Unexpected prediction shape | {prediction_tensor.shape}"

def main() -> int:

    """Run harmonic-basis configuration smoke checks."""

    # Validate Backward-Compatible Contiguous Basis
    contiguous_model = HarmonicRegression(input_size=5, harmonic_order=12, coefficient_mode="linear_conditioned")
    assert contiguous_model.harmonic_index_list == list(range(1, 13))
    assert_harmonic_model_shape(contiguous_model, expected_feature_count=25)

    # Validate Sparse RCIM Basis
    sparse_model = HarmonicRegression(
        input_size=5,
        harmonic_order=12,
        coefficient_mode="linear_conditioned",
        harmonic_index_list=RCIM_HARMONIC_INDEX_LIST,
    )
    assert sparse_model.harmonic_index_list == RCIM_HARMONIC_INDEX_LIST
    assert_harmonic_model_shape(sparse_model, expected_feature_count=19)

    # Validate Dense Paper-Maximum And Extended Bases Through The Factory
    dense_240_model = create_model(
        "harmonic_regression",
        {
            "input_size": 5,
            "output_size": 1,
            "harmonic_order": 240,
            "coefficient_mode": "static",
            "harmonic_index_list": list(range(0, 241)),
        },
    )
    assert_harmonic_model_shape(dense_240_model, expected_feature_count=481)

    dense_360_model = create_model(
        "residual_harmonic_mlp",
        {
            "input_size": 5,
            "output_size": 1,
            "harmonic_order": 360,
            "coefficient_mode": "static",
            "harmonic_index_list": list(range(0, 361)),
            "residual_hidden_size": [8, 8],
            "residual_activation_name": "GELU",
            "residual_dropout_probability": 0.0,
            "residual_use_layer_norm": False,
            "freeze_structured_branch": False,
        },
    )
    assert_harmonic_model_shape(dense_360_model.structured_branch, expected_feature_count=721)

    print("[DONE] Harmonic basis configuration smoke checks passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
