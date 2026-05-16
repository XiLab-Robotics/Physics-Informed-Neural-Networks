# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0004`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-22-38-08__te_residual_h12_deep_joint_wave1_bw_optuna_t0004\checkpoints\residual_harmonic_mlp-epoch=043-val_mae=0.00305982.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028420`
- val_mae: `0.003060`
- val_rmse: `0.003724`
- val_structured_mae: `0.017694`
- val_structured_rmse: `0.020222`

## Test Metrics

- test_loss: `0.027813`
- test_mae: `0.003296`
- test_rmse: `0.003884`
- test_structured_mae: `0.021713`
- test_structured_rmse: `0.023908`

## Interpretation

The held-out val error stayed finite with MAE=0.003060 deg and RMSE=0.003724 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003296 deg and RMSE=0.003884 deg, which indicates a numerically stable baseline run.
