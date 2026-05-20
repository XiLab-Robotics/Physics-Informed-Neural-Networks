# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_rcim_sparse_tracking_Bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=060-val_mae=0.00295293.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025537`
- val_mae: `0.002953`
- val_rmse: `0.003530`
- val_structured_mae: `0.017464`
- val_structured_rmse: `0.019692`

## Test Metrics

- test_loss: `0.023253`
- test_mae: `0.003042`
- test_rmse: `0.003548`
- test_structured_mae: `0.021561`
- test_structured_rmse: `0.023490`

## Interpretation

The held-out val error stayed finite with MAE=0.002953 deg and RMSE=0.003530 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003042 deg and RMSE=0.003548 deg, which indicates a numerically stable baseline run.
