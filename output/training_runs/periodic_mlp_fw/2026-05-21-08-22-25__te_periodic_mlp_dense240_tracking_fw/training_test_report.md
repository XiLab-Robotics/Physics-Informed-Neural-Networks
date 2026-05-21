# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense240_tracking_Fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw\checkpoints\periodic_mlp-epoch=039-val_mae=0.00254077.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020885`
- val_mae: `0.002541`
- val_rmse: `0.003049`

## Test Metrics

- test_loss: `0.024324`
- test_mae: `0.003055`
- test_rmse: `0.003537`

## Interpretation

The held-out val error stayed finite with MAE=0.002541 deg and RMSE=0.003049 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003055 deg and RMSE=0.003537 deg, which indicates a numerically stable baseline run.
