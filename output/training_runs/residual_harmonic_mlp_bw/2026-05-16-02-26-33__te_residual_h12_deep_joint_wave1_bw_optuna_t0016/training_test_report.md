# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0016`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-02-26-33__te_residual_h12_deep_joint_wave1_bw_optuna_t0016\checkpoints\residual_harmonic_mlp-epoch=043-val_mae=0.00309127.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028062`
- val_mae: `0.003091`
- val_rmse: `0.003596`
- val_structured_mae: `0.017510`
- val_structured_rmse: `0.018862`

## Test Metrics

- test_loss: `0.028525`
- test_mae: `0.003442`
- test_rmse: `0.003857`
- test_structured_mae: `0.021534`
- test_structured_rmse: `0.023002`

## Interpretation

The held-out val error stayed finite with MAE=0.003091 deg and RMSE=0.003596 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003442 deg and RMSE=0.003857 deg, which indicates a numerically stable baseline run.
