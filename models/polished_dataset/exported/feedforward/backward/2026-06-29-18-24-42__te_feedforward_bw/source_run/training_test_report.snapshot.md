# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_bw`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-18-24-42__te_feedforward_bw\checkpoints\feedforward-epoch=188-val_mae=0.00163049.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002764`
- val_mae: `0.001630`
- val_rmse: `0.002034`
- val_pointwise_loss: `0.002764`
- val_centered_curve_shape_loss: `0.002460`
- val_curve_offset_loss: `0.000337`
- val_curve_amplitude_loss: `0.037844`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003799`
- test_mae: `0.001686`
- test_rmse: `0.002175`
- test_pointwise_loss: `0.003799`
- test_centered_curve_shape_loss: `0.003522`
- test_curve_offset_loss: `0.000792`
- test_curve_amplitude_loss: `0.053764`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001630 deg and RMSE=0.002034 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001686 deg and RMSE=0.002175 deg, which indicates a numerically stable baseline run.
