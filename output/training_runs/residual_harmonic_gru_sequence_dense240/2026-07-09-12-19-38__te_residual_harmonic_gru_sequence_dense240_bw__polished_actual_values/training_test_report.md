# Residual Harmonic Gru Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_bw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_dense240_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-12-19-38__te_residual_harmonic_gru_sequence_dense240_bw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=180-val_mae=0.00194153.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005161`
- val_mae: `0.001942`
- val_rmse: `0.002719`
- val_pointwise_loss: `0.005161`
- val_centered_curve_shape_loss: `0.004872`
- val_curve_offset_loss: `0.000289`
- val_curve_amplitude_loss: `0.032068`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039745`
- val_structured_rmse: `0.044222`

## Test Metrics

- test_loss: `0.005880`
- test_mae: `0.002049`
- test_rmse: `0.003081`
- test_pointwise_loss: `0.005880`
- test_centered_curve_shape_loss: `0.005603`
- test_curve_offset_loss: `0.000277`
- test_curve_amplitude_loss: `0.036596`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037353`
- test_structured_rmse: `0.042258`

## Interpretation

The held-out val error stayed finite with MAE=0.001942 deg and RMSE=0.002719 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002049 deg and RMSE=0.003081 deg, which indicates a numerically stable baseline run.
