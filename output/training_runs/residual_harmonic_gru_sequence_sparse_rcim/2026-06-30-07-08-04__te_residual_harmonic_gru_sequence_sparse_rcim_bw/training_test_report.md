# Residual Harmonic Gru Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_bw`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw\checkpoints\residual_harmonic_gru_sequence-epoch=109-val_mae=0.00195543.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005253`
- val_mae: `0.001955`
- val_rmse: `0.002422`
- val_pointwise_loss: `0.005253`
- val_centered_curve_shape_loss: `0.004929`
- val_curve_offset_loss: `0.000324`
- val_curve_amplitude_loss: `0.041605`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039769`
- val_structured_rmse: `0.041965`

## Test Metrics

- test_loss: `0.006044`
- test_mae: `0.002083`
- test_rmse: `0.002664`
- test_pointwise_loss: `0.006044`
- test_centered_curve_shape_loss: `0.005698`
- test_curve_offset_loss: `0.000346`
- test_curve_amplitude_loss: `0.046907`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037333`
- test_structured_rmse: `0.040258`

## Interpretation

The held-out val error stayed finite with MAE=0.001955 deg and RMSE=0.002422 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002083 deg and RMSE=0.002664 deg, which indicates a numerically stable baseline run.
