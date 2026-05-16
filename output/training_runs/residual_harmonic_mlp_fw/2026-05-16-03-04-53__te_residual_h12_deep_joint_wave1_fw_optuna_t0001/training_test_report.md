# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0001`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-03-04-53__te_residual_h12_deep_joint_wave1_fw_optuna_t0001\checkpoints\residual_harmonic_mlp-epoch=048-val_mae=0.00280620.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024302`
- val_mae: `0.002806`
- val_rmse: `0.003463`
- val_structured_mae: `0.016698`
- val_structured_rmse: `0.019214`

## Test Metrics

- test_loss: `0.029057`
- test_mae: `0.003328`
- test_rmse: `0.003963`
- test_structured_mae: `0.020087`
- test_structured_rmse: `0.022234`

## Interpretation

The held-out val error stayed finite with MAE=0.002806 deg and RMSE=0.003463 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003328 deg and RMSE=0.003963 deg, which indicates a numerically stable baseline run.
