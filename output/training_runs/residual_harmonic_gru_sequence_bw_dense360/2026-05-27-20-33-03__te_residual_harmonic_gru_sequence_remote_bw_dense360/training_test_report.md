# Residual Harmonic Gru Sequence Bw Dense360 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_Bw_dense360`
- Model Family: `residual_harmonic_gru_sequence_bw_dense360`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_bw_dense360\2026-05-27-20-33-03__te_residual_harmonic_gru_sequence_remote_bw_dense360\checkpoints\residual_harmonic_gru_sequence-epoch=056-val_mae=0.00377293.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.043175`
- val_mae: `0.003773`
- val_rmse: `0.004379`
- val_structured_mae: `0.017632`
- val_structured_rmse: `0.019306`

## Test Metrics

- test_loss: `0.031753`
- test_mae: `0.003468`
- test_rmse: `0.004050`
- test_structured_mae: `0.018800`
- test_structured_rmse: `0.020724`

## Interpretation

The held-out val error stayed finite with MAE=0.003773 deg and RMSE=0.004379 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003468 deg and RMSE=0.004050 deg, which indicates a numerically stable baseline run.
