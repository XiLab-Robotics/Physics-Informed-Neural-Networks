# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0011`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-04-52-44__te_residual_h12_deep_joint_wave1_fw_optuna_t0011\checkpoints\residual_harmonic_mlp-epoch=018-val_mae=0.00275861.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024032`
- val_mae: `0.002759`
- val_rmse: `0.003441`
- val_structured_mae: `0.018353`
- val_structured_rmse: `0.021743`

## Test Metrics

- test_loss: `0.029312`
- test_mae: `0.003354`
- test_rmse: `0.003995`
- test_structured_mae: `0.021286`
- test_structured_rmse: `0.024447`

## Interpretation

The held-out val error stayed finite with MAE=0.002759 deg and RMSE=0.003441 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003354 deg and RMSE=0.003995 deg, which indicates a numerically stable baseline run.
