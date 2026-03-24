# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h08_standard`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-35-54__te_periodic_mlp_h08_standard\checkpoints\periodic_mlp-epoch=027-val_mae=0.00308566.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007572`
- val_mae: `0.003086`
- val_rmse: `0.003641`

## Test Metrics

- test_loss: `0.007985`
- test_mae: `0.003395`
- test_rmse: `0.003951`

## Interpretation

The held-out val error stayed finite with MAE=0.003086 deg and RMSE=0.003641 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003395 deg and RMSE=0.003951 deg, which indicates a numerically stable baseline run.
