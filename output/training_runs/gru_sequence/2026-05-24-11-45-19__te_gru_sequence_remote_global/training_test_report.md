# Gru Sequence Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_remote_global`
- Model Family: `gru_sequence`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-05-24-11-45-19__te_gru_sequence_remote_global\checkpoints\gru_sequence-epoch=056-val_mae=0.00370743.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011943`
- val_mae: `0.003707`
- val_rmse: `0.004308`

## Test Metrics

- test_loss: `0.009529`
- test_mae: `0.003591`
- test_rmse: `0.004110`

## Interpretation

The held-out val error stayed finite with MAE=0.003707 deg and RMSE=0.004308 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003591 deg and RMSE=0.004110 deg, which indicates a numerically stable baseline run.
