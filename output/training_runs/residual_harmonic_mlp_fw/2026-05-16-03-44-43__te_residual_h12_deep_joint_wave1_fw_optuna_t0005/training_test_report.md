# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-03-44-43__te_residual_h12_deep_joint_wave1_fw_optuna_t0005\checkpoints\residual_harmonic_mlp-epoch=063-val_mae=0.00286965.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025019`
- val_mae: `0.002870`
- val_rmse: `0.003529`
- val_structured_mae: `0.016569`
- val_structured_rmse: `0.019018`

## Test Metrics

- test_loss: `0.027811`
- test_mae: `0.003168`
- test_rmse: `0.003871`
- test_structured_mae: `0.020014`
- test_structured_rmse: `0.022064`

## Interpretation

The held-out val error stayed finite with MAE=0.002870 deg and RMSE=0.003529 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003168 deg and RMSE=0.003871 deg, which indicates a numerically stable baseline run.
