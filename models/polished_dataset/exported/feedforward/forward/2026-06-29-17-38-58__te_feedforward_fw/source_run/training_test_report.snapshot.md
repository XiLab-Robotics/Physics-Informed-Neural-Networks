# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_fw`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-17-38-58__te_feedforward_fw\checkpoints\feedforward-epoch=140-val_mae=0.00165413.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002799`
- val_mae: `0.001654`
- val_rmse: `0.002060`
- val_pointwise_loss: `0.002799`
- val_centered_curve_shape_loss: `0.002473`
- val_curve_offset_loss: `0.000366`
- val_curve_amplitude_loss: `0.036476`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004031`
- test_mae: `0.001766`
- test_rmse: `0.002254`
- test_pointwise_loss: `0.004031`
- test_centered_curve_shape_loss: `0.003575`
- test_curve_offset_loss: `0.000999`
- test_curve_amplitude_loss: `0.051544`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001654 deg and RMSE=0.002060 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001766 deg and RMSE=0.002254 deg, which indicates a numerically stable baseline run.
