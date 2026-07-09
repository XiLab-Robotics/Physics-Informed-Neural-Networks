# Residual Harmonic Gru Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_fw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-09-59-06__te_residual_harmonic_gru_sequence_dense240_fw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=065-val_mae=0.00358712.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010757`
- val_mae: `0.003587`
- val_rmse: `0.004434`
- val_pointwise_loss: `0.010757`
- val_centered_curve_shape_loss: `0.006610`
- val_curve_offset_loss: `0.004147`
- val_curve_amplitude_loss: `0.040856`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037828`
- val_structured_rmse: `0.042765`

## Test Metrics

- test_loss: `0.008162`
- test_mae: `0.003365`
- test_rmse: `0.004129`
- test_pointwise_loss: `0.008162`
- test_centered_curve_shape_loss: `0.003436`
- test_curve_offset_loss: `0.004726`
- test_curve_amplitude_loss: `0.017953`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040701`
- test_structured_rmse: `0.045485`

## Interpretation

The held-out val error stayed finite with MAE=0.003587 deg and RMSE=0.004434 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003365 deg and RMSE=0.004129 deg, which indicates a numerically stable baseline run.
