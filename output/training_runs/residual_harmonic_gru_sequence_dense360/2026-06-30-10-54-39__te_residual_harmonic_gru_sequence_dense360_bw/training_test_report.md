# Residual Harmonic Gru Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_bw`
- Model Family: `residual_harmonic_gru_sequence_dense360_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw\checkpoints\residual_harmonic_gru_sequence-epoch=138-val_mae=0.00197936.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005272`
- val_mae: `0.001979`
- val_rmse: `0.002468`
- val_pointwise_loss: `0.005272`
- val_centered_curve_shape_loss: `0.004978`
- val_curve_offset_loss: `0.000294`
- val_curve_amplitude_loss: `0.036038`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039868`
- val_structured_rmse: `0.042065`

## Test Metrics

- test_loss: `0.006010`
- test_mae: `0.002103`
- test_rmse: `0.002701`
- test_pointwise_loss: `0.006010`
- test_centered_curve_shape_loss: `0.005664`
- test_curve_offset_loss: `0.000346`
- test_curve_amplitude_loss: `0.040708`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037393`
- test_structured_rmse: `0.040335`

## Interpretation

The held-out val error stayed finite with MAE=0.001979 deg and RMSE=0.002468 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002103 deg and RMSE=0.002701 deg, which indicates a numerically stable baseline run.
