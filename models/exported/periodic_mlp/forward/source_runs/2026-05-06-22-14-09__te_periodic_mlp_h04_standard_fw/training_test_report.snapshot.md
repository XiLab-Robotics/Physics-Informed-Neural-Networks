# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw\checkpoints\periodic_mlp-epoch=022-val_mae=0.00284801.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024587`
- val_mae: `0.002848`
- val_rmse: `0.003429`

## Test Metrics

- test_loss: `0.030516`
- test_mae: `0.003432`
- test_rmse: `0.004023`

## Interpretation

The held-out val error stayed finite with MAE=0.002848 deg and RMSE=0.003429 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003432 deg and RMSE=0.004023 deg, which indicates a numerically stable baseline run.
