# Residual Harmonic Lstm Sequence Fw Dense240 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_Fw_dense240`
- Model Family: `residual_harmonic_lstm_sequence_fw_dense240`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_fw_dense240\2026-05-27-21-22-31__te_residual_harmonic_lstm_sequence_remote_fw_dense240\checkpoints\residual_harmonic_lstm_sequence-epoch=029-val_mae=0.00330691.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.032344`
- val_mae: `0.003307`
- val_rmse: `0.003837`
- val_structured_mae: `0.017248`
- val_structured_rmse: `0.018790`

## Test Metrics

- test_loss: `0.027798`
- test_mae: `0.003262`
- test_rmse: `0.003706`
- test_structured_mae: `0.017723`
- test_structured_rmse: `0.019579`

## Interpretation

The held-out val error stayed finite with MAE=0.003307 deg and RMSE=0.003837 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003262 deg and RMSE=0.003706 deg, which indicates a numerically stable baseline run.
