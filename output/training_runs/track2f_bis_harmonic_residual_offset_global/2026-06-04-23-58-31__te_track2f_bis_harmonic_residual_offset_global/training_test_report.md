# Track2F Bis Harmonic Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_harmonic_residual_offset_global`
- Model Family: `track2f_bis_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_global\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global\checkpoints\harmonic_residual_offset_probe-epoch=050-val_mae=0.00365893.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010985`
- val_mae: `0.003659`
- val_rmse: `0.004153`
- val_structured_mae: `0.020530`
- val_structured_rmse: `0.022122`
- val_residual_offset_mean_abs: `0.020259`

## Test Metrics

- test_loss: `0.008575`
- test_mae: `0.003538`
- test_rmse: `0.003932`
- test_structured_mae: `0.023224`
- test_structured_rmse: `0.024931`
- test_residual_offset_mean_abs: `0.022970`

## Interpretation

The held-out val error stayed finite with MAE=0.003659 deg and RMSE=0.004153 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003538 deg and RMSE=0.003932 deg, which indicates a numerically stable baseline run.
