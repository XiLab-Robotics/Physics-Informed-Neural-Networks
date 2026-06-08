# Track2F Bis Harmonic Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_harmonic_residual_offset_fw`
- Model Family: `track2f_bis_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw\checkpoints\harmonic_residual_offset_probe-epoch=175-val_mae=0.00294145.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028723`
- val_mae: `0.002941`
- val_rmse: `0.003457`
- val_structured_mae: `0.004225`
- val_structured_rmse: `0.004766`
- val_residual_offset_mean_abs: `0.002826`

## Test Metrics

- test_loss: `0.024398`
- test_mae: `0.002862`
- test_rmse: `0.003334`
- test_structured_mae: `0.003952`
- test_structured_rmse: `0.004393`
- test_residual_offset_mean_abs: `0.003130`

## Interpretation

The held-out val error stayed finite with MAE=0.002941 deg and RMSE=0.003457 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002862 deg and RMSE=0.003334 deg, which indicates a numerically stable baseline run.
