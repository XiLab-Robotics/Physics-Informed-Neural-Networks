# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_dense240_tracking_Bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw\checkpoints\periodic_mlp-epoch=073-val_mae=0.00304062.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027331`
- val_mae: `0.003041`
- val_rmse: `0.003628`

## Test Metrics

- test_loss: `0.029682`
- test_mae: `0.003417`
- test_rmse: `0.004005`

## Interpretation

The held-out val error stayed finite with MAE=0.003041 deg and RMSE=0.003628 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003417 deg and RMSE=0.004005 deg, which indicates a numerically stable baseline run.
