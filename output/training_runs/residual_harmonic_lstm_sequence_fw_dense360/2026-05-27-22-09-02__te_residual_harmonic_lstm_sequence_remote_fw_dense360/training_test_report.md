# Residual Harmonic Lstm Sequence Fw Dense360 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_Fw_dense360`
- Model Family: `residual_harmonic_lstm_sequence_fw_dense360`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_fw_dense360\2026-05-27-22-09-02__te_residual_harmonic_lstm_sequence_remote_fw_dense360\checkpoints\residual_harmonic_lstm_sequence-epoch=028-val_mae=0.00330212.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.031660`
- val_mae: `0.003302`
- val_rmse: `0.003814`
- val_structured_mae: `0.017261`
- val_structured_rmse: `0.018807`

## Test Metrics

- test_loss: `0.028611`
- test_mae: `0.003351`
- test_rmse: `0.003774`
- test_structured_mae: `0.017696`
- test_structured_rmse: `0.019552`

## Interpretation

The held-out val error stayed finite with MAE=0.003302 deg and RMSE=0.003814 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003351 deg and RMSE=0.003774 deg, which indicates a numerically stable baseline run.
