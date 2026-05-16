# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0010`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-00-25-13__te_residual_h12_deep_joint_wave1_bw_optuna_t0010\checkpoints\residual_harmonic_mlp-epoch=111-val_mae=0.00295009.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027718`
- val_mae: `0.002950`
- val_rmse: `0.003631`
- val_structured_mae: `0.017543`
- val_structured_rmse: `0.019807`

## Test Metrics

- test_loss: `0.029441`
- test_mae: `0.003366`
- test_rmse: `0.003996`
- test_structured_mae: `0.021517`
- test_structured_rmse: `0.023484`

## Interpretation

The held-out val error stayed finite with MAE=0.002950 deg and RMSE=0.003631 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003366 deg and RMSE=0.003996 deg, which indicates a numerically stable baseline run.
