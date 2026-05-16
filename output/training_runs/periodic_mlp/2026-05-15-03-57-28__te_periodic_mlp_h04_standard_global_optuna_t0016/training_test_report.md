# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0016`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-03-57-28__te_periodic_mlp_h04_standard_global_optuna_t0016\checkpoints\periodic_mlp-epoch=036-val_mae=0.00311079.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007674`
- val_mae: `0.003111`
- val_rmse: `0.003669`

## Test Metrics

- test_loss: `0.008461`
- test_mae: `0.003517`
- test_rmse: `0.004068`

## Interpretation

The held-out val error stayed finite with MAE=0.003111 deg and RMSE=0.003669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003517 deg and RMSE=0.004068 deg, which indicates a numerically stable baseline run.
