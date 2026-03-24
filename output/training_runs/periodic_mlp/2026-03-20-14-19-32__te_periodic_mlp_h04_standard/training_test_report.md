# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-19-32__te_periodic_mlp_h04_standard\checkpoints\periodic_mlp-epoch=031-val_mae=0.00309735.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007431`
- val_mae: `0.003097`
- val_rmse: `0.003628`

## Test Metrics

- test_loss: `0.007541`
- test_mae: `0.003317`
- test_rmse: `0.003793`

## Interpretation

The held-out val error stayed finite with MAE=0.003097 deg and RMSE=0.003628 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003317 deg and RMSE=0.003793 deg, which indicates a numerically stable baseline run.
