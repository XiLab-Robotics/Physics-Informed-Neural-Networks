# Actual Values Direction Flag Alignment

## Overview

Before this correction, the dataset input-mode implementation gave
`polished_dataset` actual values a four-feature input contract:

```text
theta, theta_dot, tau_load, T
```

The setpoint paths use a five-feature contract:

```text
angular_position_deg, input_speed_rpm, input_torque_nm, oil_temperature_deg, direction_flag
```

This creates an avoidable mismatch for future common inference and testing
scripts. The requested change is to add `direction_flag` to the
`polished_dataset` actual-values input contract so every retraining version
uses five input features.

## Technical Approach

The loader will keep measured actual values row-by-row, but append the
direction label as a constant fifth column for every row of a directional
curve:

```text
theta, theta_dot, tau_load, T, direction_flag
```

`direction_flag` remains `1.0` for forward curves and `-1.0` for backward
curves. This preserves the actual-values semantics for speed, torque, and
temperature while making the model input width uniform across:

- `simplified_dataset` with setpoints;
- `polished_dataset` with setpoints;
- `polished_dataset` with actual values.

The schema name `polished_point_v1` can remain stable if treated as the
row-level polished actual-values contract, but its `input_feature_name_list`
and `input_feature_dim` will be updated to include `direction_flag`.

## Involved Components

- `scripts/datasets/transmission_error_dataset.py`
  - update the polished actual-values feature name list;
  - append a per-row `direction_flag` column in
    `build_polished_directional_sample`;
  - verify `resolve_dataset_schema("polished_dataset", "actual_values")`
    reports five input features.
- `scripts/training/transmission_error_datamodule.py`
  - no structural change expected, but its schema-derived input dimension must
    reflect the new five-feature contract.
- `scripts/training/shared_training_infrastructure.py`
  - no structural change expected, but smoke checks must confirm `input_size`
    auto-resolution remains correct.
- Existing campaign package and previously exported tree artifacts remain
  historical results. Any future `polished_dataset` actual-values retraining
  must use the new five-feature contract.

## Implementation Steps

1. Update the polished actual-values feature list to include `direction_flag`.
2. Append the constant direction column to actual-values polished feature
   matrices while preserving row-level `theta_dot`, `tau_load`, and `T`.
3. Add or run deterministic loader checks proving:
   - polished actual-values input dimension is `5`;
   - polished actual-values direction column is constant and has the expected
     sign;
   - polished setpoints and simplified setpoints remain five-feature inputs.
4. Run Python compilation checks for the touched dataset/training modules.
5. Run Markdown QA on this technical document and the updated documentation
   index.
