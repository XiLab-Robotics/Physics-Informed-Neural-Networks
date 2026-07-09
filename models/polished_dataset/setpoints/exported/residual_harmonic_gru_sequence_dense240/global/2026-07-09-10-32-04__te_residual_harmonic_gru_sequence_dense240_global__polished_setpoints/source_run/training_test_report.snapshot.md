# Residual Harmonic Gru Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=081-val_mae=0.00198647.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005224`
- val_mae: `0.001986`
- val_rmse: `0.002762`
- val_pointwise_loss: `0.005224`
- val_centered_curve_shape_loss: `0.004846`
- val_curve_offset_loss: `0.000378`
- val_curve_amplitude_loss: `0.034147`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039648`
- val_structured_rmse: `0.044128`

## Test Metrics

- test_loss: `0.008578`
- test_mae: `0.002278`
- test_rmse: `0.003633`
- test_pointwise_loss: `0.008578`
- test_centered_curve_shape_loss: `0.005707`
- test_curve_offset_loss: `0.002871`
- test_curve_amplitude_loss: `0.044017`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037309`
- test_structured_rmse: `0.042195`

## Interpretation

The held-out val error stayed finite with MAE=0.001986 deg and RMSE=0.002762 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002278 deg and RMSE=0.003633 deg, which indicates a numerically stable baseline run.
