# Sequential Residual Offset Probe Fw Training And Testing Report

## Overview

- Run Name: `te_sequential_residual_offset_probe_remote_fw`
- Model Family: `sequential_residual_offset_probe_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe_fw\2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw\checkpoints\sequential_residual_offset_probe-epoch=168-val_mae=0.00338001.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.034903`
- val_mae: `0.003380`
- val_rmse: `0.003985`
- val_base_mae: `0.014171`
- val_base_rmse: `0.017061`
- val_residual_offset_mean_abs: `0.013697`

## Test Metrics

- test_loss: `0.030740`
- test_mae: `0.003385`
- test_rmse: `0.003931`
- test_base_mae: `0.014037`
- test_base_rmse: `0.016928`
- test_residual_offset_mean_abs: `0.013951`

## Interpretation

The held-out val error stayed finite with MAE=0.003380 deg and RMSE=0.003985 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003385 deg and RMSE=0.003931 deg, which indicates a numerically stable baseline run.
