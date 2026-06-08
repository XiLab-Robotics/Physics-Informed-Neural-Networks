# Track2F Bis Clean Sequential Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_clean_residual_offset_global`
- Model Family: `track2f_bis_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_global\2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global\checkpoints\sequential_residual_offset_probe-epoch=048-val_mae=0.00371694.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011647`
- val_mae: `0.003717`
- val_rmse: `0.004310`
- val_base_mae: `0.018268`
- val_base_rmse: `0.020749`
- val_residual_offset_mean_abs: `0.017542`

## Test Metrics

- test_loss: `0.008944`
- test_mae: `0.003528`
- test_rmse: `0.004010`
- test_base_mae: `0.019842`
- test_base_rmse: `0.022233`
- test_residual_offset_mean_abs: `0.019289`

## Interpretation

The held-out val error stayed finite with MAE=0.003717 deg and RMSE=0.004310 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003528 deg and RMSE=0.004010 deg, which indicates a numerically stable baseline run.
