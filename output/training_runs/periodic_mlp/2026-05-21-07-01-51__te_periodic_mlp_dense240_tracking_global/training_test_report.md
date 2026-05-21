# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense240_tracking_global`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global\checkpoints\periodic_mlp-epoch=025-val_mae=0.00296227.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006999`
- val_mae: `0.002962`
- val_rmse: `0.003501`

## Test Metrics

- test_loss: `0.007503`
- test_mae: `0.003348`
- test_rmse: `0.003862`

## Interpretation

The held-out val error stayed finite with MAE=0.002962 deg and RMSE=0.003501 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003348 deg and RMSE=0.003862 deg, which indicates a numerically stable baseline run.
