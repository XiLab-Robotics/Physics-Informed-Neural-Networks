# Residual Harmonic Gru Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense360_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=081-val_mae=0.00358186.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010731`
- val_mae: `0.003582`
- val_rmse: `0.004425`
- val_pointwise_loss: `0.010731`
- val_centered_curve_shape_loss: `0.006571`
- val_curve_offset_loss: `0.004160`
- val_curve_amplitude_loss: `0.043964`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037825`
- val_structured_rmse: `0.042693`

## Test Metrics

- test_loss: `0.008343`
- test_mae: `0.003407`
- test_rmse: `0.004178`
- test_pointwise_loss: `0.008343`
- test_centered_curve_shape_loss: `0.003429`
- test_curve_offset_loss: `0.004913`
- test_curve_amplitude_loss: `0.020025`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040700`
- test_structured_rmse: `0.045431`

## Interpretation

The held-out val error stayed finite with MAE=0.003582 deg and RMSE=0.004425 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003407 deg and RMSE=0.004178 deg, which indicates a numerically stable baseline run.
