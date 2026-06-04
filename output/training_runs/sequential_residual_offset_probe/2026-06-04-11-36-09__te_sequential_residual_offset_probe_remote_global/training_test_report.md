# Sequential Residual Offset Probe Training And Testing Report

## Overview

- Run Name: `te_sequential_residual_offset_probe_remote_global`
- Model Family: `sequential_residual_offset_probe`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe\2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global\checkpoints\sequential_residual_offset_probe-epoch=061-val_mae=0.00378313.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012002`
- val_mae: `0.003783`
- val_rmse: `0.004350`
- val_base_mae: `0.017637`
- val_base_rmse: `0.020243`
- val_residual_offset_mean_abs: `0.017044`

## Test Metrics

- test_loss: `0.009143`
- test_mae: `0.003537`
- test_rmse: `0.004005`
- test_base_mae: `0.018909`
- test_base_rmse: `0.021419`
- test_residual_offset_mean_abs: `0.018514`

## Interpretation

The held-out val error stayed finite with MAE=0.003783 deg and RMSE=0.004350 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003537 deg and RMSE=0.004005 deg, which indicates a numerically stable baseline run.
