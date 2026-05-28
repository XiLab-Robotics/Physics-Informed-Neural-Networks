# Residual Harmonic Lstm Sequence Dense240 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_remote_global_dense240`
- Model Family: `residual_harmonic_lstm_sequence_dense240`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-05-27-21-08-36__te_residual_harmonic_lstm_sequence_remote_global_dense240\checkpoints\residual_harmonic_lstm_sequence-epoch=022-val_mae=0.00362421.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011106`
- val_mae: `0.003624`
- val_rmse: `0.004190`
- val_structured_mae: `0.037827`
- val_structured_rmse: `0.038339`

## Test Metrics

- test_loss: `0.008647`
- test_mae: `0.003473`
- test_rmse: `0.003925`
- test_structured_mae: `0.040701`
- test_structured_rmse: `0.041075`

## Interpretation

The held-out val error stayed finite with MAE=0.003624 deg and RMSE=0.004190 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003473 deg and RMSE=0.003925 deg, which indicates a numerically stable baseline run.
