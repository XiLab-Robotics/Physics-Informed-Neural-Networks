# Track2F Bis Clean Sequential Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_clean_residual_offset_fw`
- Model Family: `track2f_bis_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw\checkpoints\sequential_residual_offset_probe-epoch=020-val_mae=0.00347412.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.035699`
- val_mae: `0.003474`
- val_rmse: `0.004082`
- val_base_mae: `0.013466`
- val_base_rmse: `0.015956`
- val_residual_offset_mean_abs: `0.013094`

## Test Metrics

- test_loss: `0.031117`
- test_mae: `0.003446`
- test_rmse: `0.003972`
- test_base_mae: `0.013347`
- test_base_rmse: `0.015736`
- test_residual_offset_mean_abs: `0.013429`

## Interpretation

The held-out val error stayed finite with MAE=0.003474 deg and RMSE=0.004082 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003446 deg and RMSE=0.003972 deg, which indicates a numerically stable baseline run.
