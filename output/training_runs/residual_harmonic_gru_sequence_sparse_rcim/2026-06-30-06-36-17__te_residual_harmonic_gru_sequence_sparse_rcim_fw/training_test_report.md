# Residual Harmonic Gru Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_fw`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw\checkpoints\residual_harmonic_gru_sequence-epoch=130-val_mae=0.00194226.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005221`
- val_mae: `0.001942`
- val_rmse: `0.002406`
- val_pointwise_loss: `0.005221`
- val_centered_curve_shape_loss: `0.004915`
- val_curve_offset_loss: `0.000306`
- val_curve_amplitude_loss: `0.039696`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039722`
- val_structured_rmse: `0.041918`

## Test Metrics

- test_loss: `0.005978`
- test_mae: `0.002056`
- test_rmse: `0.002645`
- test_pointwise_loss: `0.005978`
- test_centered_curve_shape_loss: `0.005675`
- test_curve_offset_loss: `0.000303`
- test_curve_amplitude_loss: `0.044753`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037322`
- test_structured_rmse: `0.040235`

## Interpretation

The held-out val error stayed finite with MAE=0.001942 deg and RMSE=0.002406 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002056 deg and RMSE=0.002645 deg, which indicates a numerically stable baseline run.
