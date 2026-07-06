# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_fw`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-23-06-26__te_gru_sequence_fw\checkpoints\gru_sequence-epoch=153-val_mae=0.00213020.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005694`
- val_mae: `0.002130`
- val_rmse: `0.002644`
- val_pointwise_loss: `0.005694`
- val_centered_curve_shape_loss: `0.005370`
- val_curve_offset_loss: `0.000323`
- val_curve_amplitude_loss: `0.055913`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006525`
- test_mae: `0.002247`
- test_rmse: `0.002882`
- test_pointwise_loss: `0.006525`
- test_centered_curve_shape_loss: `0.006159`
- test_curve_offset_loss: `0.000365`
- test_curve_amplitude_loss: `0.062078`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002130 deg and RMSE=0.002644 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002247 deg and RMSE=0.002882 deg, which indicates a numerically stable baseline run.
