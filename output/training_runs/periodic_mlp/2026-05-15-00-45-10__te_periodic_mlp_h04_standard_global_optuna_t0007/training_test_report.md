# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0007`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-00-45-10__te_periodic_mlp_h04_standard_global_optuna_t0007\checkpoints\periodic_mlp-epoch=041-val_mae=0.00304861.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007125`
- val_mae: `0.003049`
- val_rmse: `0.003577`

## Test Metrics

- test_loss: `0.007598`
- test_mae: `0.003339`
- test_rmse: `0.003858`

## Interpretation

The held-out val error stayed finite with MAE=0.003049 deg and RMSE=0.003577 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003339 deg and RMSE=0.003858 deg, which indicates a numerically stable baseline run.
