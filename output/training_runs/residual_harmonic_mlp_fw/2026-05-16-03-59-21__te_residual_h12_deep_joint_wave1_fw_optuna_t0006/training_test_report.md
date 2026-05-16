# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0006`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-03-59-21__te_residual_h12_deep_joint_wave1_fw_optuna_t0006\checkpoints\residual_harmonic_mlp-epoch=043-val_mae=0.00282685.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023376`
- val_mae: `0.002827`
- val_rmse: `0.003447`
- val_structured_mae: `0.016596`
- val_structured_rmse: `0.019053`

## Test Metrics

- test_loss: `0.026703`
- test_mae: `0.003194`
- test_rmse: `0.003809`
- test_structured_mae: `0.020026`
- test_structured_rmse: `0.022094`

## Interpretation

The held-out val error stayed finite with MAE=0.002827 deg and RMSE=0.003447 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003194 deg and RMSE=0.003809 deg, which indicates a numerically stable baseline run.
