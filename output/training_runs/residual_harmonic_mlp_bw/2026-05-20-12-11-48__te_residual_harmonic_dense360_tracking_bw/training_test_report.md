# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense360_tracking_Bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=122-val_mae=0.00282637.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024217`
- val_mae: `0.002826`
- val_rmse: `0.003383`
- val_structured_mae: `0.017474`
- val_structured_rmse: `0.019694`

## Test Metrics

- test_loss: `0.023596`
- test_mae: `0.003068`
- test_rmse: `0.003545`
- test_structured_mae: `0.021549`
- test_structured_rmse: `0.023471`

## Interpretation

The held-out val error stayed finite with MAE=0.002826 deg and RMSE=0.003383 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003068 deg and RMSE=0.003545 deg, which indicates a numerically stable baseline run.
