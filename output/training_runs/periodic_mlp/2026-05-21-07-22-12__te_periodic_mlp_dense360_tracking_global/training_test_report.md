# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense360_tracking_global`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global\checkpoints\periodic_mlp-epoch=086-val_mae=0.00285943.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007419`
- val_mae: `0.002859`
- val_rmse: `0.003335`

## Test Metrics

- test_loss: `0.008601`
- test_mae: `0.003401`
- test_rmse: `0.003831`

## Interpretation

The held-out val error stayed finite with MAE=0.002859 deg and RMSE=0.003335 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003401 deg and RMSE=0.003831 deg, which indicates a numerically stable baseline run.
