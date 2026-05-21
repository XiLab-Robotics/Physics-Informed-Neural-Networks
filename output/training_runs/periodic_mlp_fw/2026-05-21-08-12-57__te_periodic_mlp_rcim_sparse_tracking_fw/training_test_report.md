# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_rcim_sparse_tracking_Fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw\checkpoints\periodic_mlp-epoch=032-val_mae=0.00251598.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020233`
- val_mae: `0.002516`
- val_rmse: `0.002985`

## Test Metrics

- test_loss: `0.025059`
- test_mae: `0.003131`
- test_rmse: `0.003578`

## Interpretation

The held-out val error stayed finite with MAE=0.002516 deg and RMSE=0.002985 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003131 deg and RMSE=0.003578 deg, which indicates a numerically stable baseline run.
