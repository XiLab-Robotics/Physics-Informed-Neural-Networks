# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_rcim_sparse_tracking_Bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw\checkpoints\periodic_mlp-epoch=051-val_mae=0.00301058.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024986`
- val_mae: `0.003011`
- val_rmse: `0.003506`

## Test Metrics

- test_loss: `0.027251`
- test_mae: `0.003398`
- test_rmse: `0.003922`

## Interpretation

The held-out val error stayed finite with MAE=0.003011 deg and RMSE=0.003506 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003398 deg and RMSE=0.003922 deg, which indicates a numerically stable baseline run.
