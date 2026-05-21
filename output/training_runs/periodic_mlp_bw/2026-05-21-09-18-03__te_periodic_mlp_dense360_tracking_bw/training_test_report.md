# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense360_tracking_Bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw\checkpoints\periodic_mlp-epoch=056-val_mae=0.00307213.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028366`
- val_mae: `0.003072`
- val_rmse: `0.003717`

## Test Metrics

- test_loss: `0.029762`
- test_mae: `0.003424`
- test_rmse: `0.004006`

## Interpretation

The held-out val error stayed finite with MAE=0.003072 deg and RMSE=0.003717 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003424 deg and RMSE=0.004006 deg, which indicates a numerically stable baseline run.
