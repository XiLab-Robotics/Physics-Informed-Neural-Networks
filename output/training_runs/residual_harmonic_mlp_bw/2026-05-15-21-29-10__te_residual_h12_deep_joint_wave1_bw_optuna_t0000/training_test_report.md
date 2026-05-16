# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0000`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-21-29-10__te_residual_h12_deep_joint_wave1_bw_optuna_t0000\checkpoints\residual_harmonic_mlp-epoch=095-val_mae=0.00293512.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026922`
- val_mae: `0.002935`
- val_rmse: `0.003422`
- val_structured_mae: `0.017588`
- val_structured_rmse: `0.018904`

## Test Metrics

- test_loss: `0.026708`
- test_mae: `0.003266`
- test_rmse: `0.003727`
- test_structured_mae: `0.021499`
- test_structured_rmse: `0.023022`

## Interpretation

The held-out val error stayed finite with MAE=0.002935 deg and RMSE=0.003422 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003266 deg and RMSE=0.003727 deg, which indicates a numerically stable baseline run.
