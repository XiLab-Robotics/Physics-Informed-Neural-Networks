# Residual Harmonic Gru Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-39-47__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=116-val_mae=0.00198454.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005326`
- val_mae: `0.001985`
- val_rmse: `0.002780`
- val_pointwise_loss: `0.005326`
- val_centered_curve_shape_loss: `0.004901`
- val_curve_offset_loss: `0.000425`
- val_curve_amplitude_loss: `0.040595`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039828`
- val_structured_rmse: `0.044281`

## Test Metrics

- test_loss: `0.008700`
- test_mae: `0.002279`
- test_rmse: `0.003659`
- test_pointwise_loss: `0.008700`
- test_centered_curve_shape_loss: `0.005804`
- test_curve_offset_loss: `0.002896`
- test_curve_amplitude_loss: `0.051401`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037353`
- test_structured_rmse: `0.042247`

## Interpretation

The held-out val error stayed finite with MAE=0.001985 deg and RMSE=0.002780 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002279 deg and RMSE=0.003659 deg, which indicates a numerically stable baseline run.
