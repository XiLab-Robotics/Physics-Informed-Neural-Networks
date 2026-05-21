# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense360_tracking_Fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw\checkpoints\periodic_mlp-epoch=017-val_mae=0.00252353.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021502`
- val_mae: `0.002524`
- val_rmse: `0.003062`

## Test Metrics

- test_loss: `0.026510`
- test_mae: `0.003155`
- test_rmse: `0.003680`

## Interpretation

The held-out val error stayed finite with MAE=0.002524 deg and RMSE=0.003062 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003155 deg and RMSE=0.003680 deg, which indicates a numerically stable baseline run.
