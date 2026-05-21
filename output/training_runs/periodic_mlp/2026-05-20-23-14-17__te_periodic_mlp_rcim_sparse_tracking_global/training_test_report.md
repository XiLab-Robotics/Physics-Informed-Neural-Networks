# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_rcim_sparse_tracking_global`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global\checkpoints\periodic_mlp-epoch=067-val_mae=0.00286316.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006616`
- val_mae: `0.002863`
- val_rmse: `0.003304`

## Test Metrics

- test_loss: `0.007483`
- test_mae: `0.003275`
- test_rmse: `0.003726`

## Interpretation

The held-out val error stayed finite with MAE=0.002863 deg and RMSE=0.003304 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003275 deg and RMSE=0.003726 deg, which indicates a numerically stable baseline run.
