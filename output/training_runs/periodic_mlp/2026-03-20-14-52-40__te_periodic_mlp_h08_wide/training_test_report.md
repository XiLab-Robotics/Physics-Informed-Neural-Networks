# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h08_wide`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-03-20-14-52-40__te_periodic_mlp_h08_wide\checkpoints\periodic_mlp-epoch=046-val_mae=0.00308864.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007857`
- val_mae: `0.003089`
- val_rmse: `0.003653`

## Test Metrics

- test_loss: `0.009058`
- test_mae: `0.003590`
- test_rmse: `0.004143`

## Interpretation

The held-out val error stayed finite with MAE=0.003089 deg and RMSE=0.003653 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003590 deg and RMSE=0.004143 deg, which indicates a numerically stable baseline run.
