# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0003`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-14-04-22__te_residual_h12_deep_joint_wave1_global_optuna_t0003\checkpoints\residual_harmonic_mlp-epoch=032-val_mae=0.00304033.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007517`
- val_mae: `0.003040`
- val_rmse: `0.003443`
- val_structured_mae: `0.040592`
- val_structured_rmse: `0.040851`

## Test Metrics

- test_loss: `0.007929`
- test_mae: `0.003371`
- test_rmse: `0.003740`
- test_structured_mae: `0.039434`
- test_structured_rmse: `0.039785`

## Interpretation

The held-out val error stayed finite with MAE=0.003040 deg and RMSE=0.003443 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003371 deg and RMSE=0.003740 deg, which indicates a numerically stable baseline run.
