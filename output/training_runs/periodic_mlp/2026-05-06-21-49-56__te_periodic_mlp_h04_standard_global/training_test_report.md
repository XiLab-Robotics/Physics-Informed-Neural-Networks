# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global\checkpoints\periodic_mlp-epoch=041-val_mae=0.00298461.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007188`
- val_mae: `0.002985`
- val_rmse: `0.003521`

## Test Metrics

- test_loss: `0.007939`
- test_mae: `0.003349`
- test_rmse: `0.003916`

## Interpretation

The held-out val error stayed finite with MAE=0.002985 deg and RMSE=0.003521 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003349 deg and RMSE=0.003916 deg, which indicates a numerically stable baseline run.
