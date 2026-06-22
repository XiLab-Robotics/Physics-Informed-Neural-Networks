# Residual Harmonic Gru Sequence Sparse Rcim Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim\checkpoints\residual_harmonic_gru_sequence-epoch=081-val_mae=0.00197803.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005351`
- val_mae: `0.001978`
- val_rmse: `0.002450`
- val_pointwise_loss: `0.005351`
- val_centered_curve_shape_loss: `0.004929`
- val_curve_offset_loss: `0.000422`
- val_curve_amplitude_loss: `0.041663`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039850`
- val_structured_rmse: `0.042043`

## Test Metrics

- test_loss: `0.006209`
- test_mae: `0.002112`
- test_rmse: `0.002699`
- test_pointwise_loss: `0.006209`
- test_centered_curve_shape_loss: `0.005705`
- test_curve_offset_loss: `0.000503`
- test_curve_amplitude_loss: `0.046876`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037358`
- test_structured_rmse: `0.040296`

## Interpretation

The held-out val error stayed finite with MAE=0.001978 deg and RMSE=0.002450 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002112 deg and RMSE=0.002699 deg, which indicates a numerically stable baseline run.
