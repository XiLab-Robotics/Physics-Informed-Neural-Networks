# Sequential Residual Offset Probe Bw Training And Testing Report

## Overview

- Run Name: `te_sequential_residual_offset_probe_remote_bw`
- Model Family: `sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe_bw\2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw\checkpoints\sequential_residual_offset_probe-epoch=061-val_mae=0.00383996.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.047546`
- val_mae: `0.003840`
- val_rmse: `0.004512`
- val_base_mae: `0.014664`
- val_base_rmse: `0.017457`
- val_residual_offset_mean_abs: `0.014134`

## Test Metrics

- test_loss: `0.035072`
- test_mae: `0.003638`
- test_rmse: `0.004280`
- test_base_mae: `0.015475`
- test_base_rmse: `0.018389`
- test_residual_offset_mean_abs: `0.014940`

## Interpretation

The held-out val error stayed finite with MAE=0.003840 deg and RMSE=0.004512 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003638 deg and RMSE=0.004280 deg, which indicates a numerically stable baseline run.
