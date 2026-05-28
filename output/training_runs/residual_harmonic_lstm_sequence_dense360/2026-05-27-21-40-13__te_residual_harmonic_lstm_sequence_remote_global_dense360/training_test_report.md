# Residual Harmonic Lstm Sequence Dense360 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_global_dense360`
- Model Family: `residual_harmonic_lstm_sequence_dense360`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-05-27-21-40-13__te_residual_harmonic_lstm_sequence_remote_global_dense360\checkpoints\residual_harmonic_lstm_sequence-epoch=076-val_mae=0.00364759.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011214`
- val_mae: `0.003648`
- val_rmse: `0.004200`
- val_structured_mae: `0.037858`
- val_structured_rmse: `0.038254`

## Test Metrics

- test_loss: `0.008701`
- test_mae: `0.003477`
- test_rmse: `0.003940`
- test_structured_mae: `0.040718`
- test_structured_rmse: `0.041042`

## Interpretation

The held-out val error stayed finite with MAE=0.003648 deg and RMSE=0.004200 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003477 deg and RMSE=0.003940 deg, which indicates a numerically stable baseline run.
