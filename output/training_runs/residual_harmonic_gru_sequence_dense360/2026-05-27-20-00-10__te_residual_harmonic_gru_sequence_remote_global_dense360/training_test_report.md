# Residual Harmonic Gru Sequence Dense360 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_global_dense360`
- Model Family: `residual_harmonic_gru_sequence_dense360`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-05-27-20-00-10__te_residual_harmonic_gru_sequence_remote_global_dense360\checkpoints\residual_harmonic_gru_sequence-epoch=045-val_mae=0.00362817.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011198`
- val_mae: `0.003628`
- val_rmse: `0.004180`
- val_structured_mae: `0.037831`
- val_structured_rmse: `0.038253`

## Test Metrics

- test_loss: `0.009091`
- test_mae: `0.003535`
- test_rmse: `0.003999`
- test_structured_mae: `0.040704`
- test_structured_rmse: `0.041022`

## Interpretation

The held-out val error stayed finite with MAE=0.003628 deg and RMSE=0.004180 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003535 deg and RMSE=0.003999 deg, which indicates a numerically stable baseline run.
