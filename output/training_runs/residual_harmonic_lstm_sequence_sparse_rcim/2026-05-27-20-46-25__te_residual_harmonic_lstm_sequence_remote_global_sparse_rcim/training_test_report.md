# Residual Harmonic Lstm Sequence Sparse Rcim Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-05-27-20-46-25__te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim\checkpoints\residual_harmonic_lstm_sequence-epoch=035-val_mae=0.00363187.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011094`
- val_mae: `0.003632`
- val_rmse: `0.004159`
- val_structured_mae: `0.037835`
- val_structured_rmse: `0.038259`

## Test Metrics

- test_loss: `0.008283`
- test_mae: `0.003368`
- test_rmse: `0.003808`
- test_structured_mae: `0.040706`
- test_structured_rmse: `0.041024`

## Interpretation

The held-out val error stayed finite with MAE=0.003632 deg and RMSE=0.004159 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003368 deg and RMSE=0.003808 deg, which indicates a numerically stable baseline run.
