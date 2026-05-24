# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_remote_Fw`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw\checkpoints\gru_sequence-epoch=045-val_mae=0.00340867.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.035350`
- val_mae: `0.003409`
- val_rmse: `0.004010`

## Test Metrics

- test_loss: `0.030127`
- test_mae: `0.003333`
- test_rmse: `0.003881`

## Interpretation

The held-out val error stayed finite with MAE=0.003409 deg and RMSE=0.004010 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003333 deg and RMSE=0.003881 deg, which indicates a numerically stable baseline run.
