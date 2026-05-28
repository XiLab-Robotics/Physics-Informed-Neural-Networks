# Residual Harmonic Lstm Sequence Fw Sparse Rcim Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim`
- Model Family: `residual_harmonic_lstm_sequence_fw_sparse_rcim`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_fw_sparse_rcim\2026-05-27-20-55-58__te_residual_harmonic_lstm_sequence_remote_fw_sparse_rcim\checkpoints\residual_harmonic_lstm_sequence-epoch=013-val_mae=0.00334394.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033118`
- val_mae: `0.003344`
- val_rmse: `0.003872`
- val_structured_mae: `0.017876`
- val_structured_rmse: `0.020086`

## Test Metrics

- test_loss: `0.027594`
- test_mae: `0.003234`
- test_rmse: `0.003679`
- test_structured_mae: `0.018373`
- test_structured_rmse: `0.020718`

## Interpretation

The held-out val error stayed finite with MAE=0.003344 deg and RMSE=0.003872 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003234 deg and RMSE=0.003679 deg, which indicates a numerically stable baseline run.
