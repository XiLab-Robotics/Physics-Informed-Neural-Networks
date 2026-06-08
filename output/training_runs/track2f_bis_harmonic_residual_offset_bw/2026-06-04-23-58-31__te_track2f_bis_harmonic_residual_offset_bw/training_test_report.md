# Track2F Bis Harmonic Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_track2f_bis_harmonic_residual_offset_bw`
- Model Family: `track2f_bis_harmonic_residual_offset_bw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_bw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw\checkpoints\harmonic_residual_offset_probe-epoch=171-val_mae=0.00355501.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.042214`
- val_mae: `0.003555`
- val_rmse: `0.004222`
- val_structured_mae: `0.012217`
- val_structured_rmse: `0.013334`
- val_residual_offset_mean_abs: `0.011272`

## Test Metrics

- test_loss: `0.031048`
- test_mae: `0.003336`
- test_rmse: `0.003935`
- test_structured_mae: `0.012058`
- test_structured_rmse: `0.013553`
- test_residual_offset_mean_abs: `0.011024`

## Interpretation

The held-out val error stayed finite with MAE=0.003555 deg and RMSE=0.004222 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003336 deg and RMSE=0.003935 deg, which indicates a numerically stable baseline run.
