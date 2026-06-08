# Track2F Bis Clean Sequential Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_clean_residual_offset_bw`
- Model Family: `track2f_bis_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_bw\2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw\checkpoints\sequential_residual_offset_probe-epoch=099-val_mae=0.00381964.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.047427`
- val_mae: `0.003820`
- val_rmse: `0.004490`
- val_base_mae: `0.014356`
- val_base_rmse: `0.017048`
- val_residual_offset_mean_abs: `0.013978`

## Test Metrics

- test_loss: `0.034390`
- test_mae: `0.003540`
- test_rmse: `0.004203`
- test_base_mae: `0.014895`
- test_base_rmse: `0.017484`
- test_residual_offset_mean_abs: `0.014364`

## Interpretation

The held-out val error stayed finite with MAE=0.003820 deg and RMSE=0.004490 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003540 deg and RMSE=0.004203 deg, which indicates a numerically stable baseline run.
