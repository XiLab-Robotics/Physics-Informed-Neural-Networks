# Residual Harmonic Gru Sequence Fw Dense360 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_Fw_dense360`
- Model Family: `residual_harmonic_gru_sequence_fw_dense360`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_fw_dense360\2026-05-27-20-21-50__te_residual_harmonic_gru_sequence_remote_fw_dense360\checkpoints\residual_harmonic_gru_sequence-epoch=037-val_mae=0.00326484.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.031012`
- val_mae: `0.003265`
- val_rmse: `0.003797`
- val_structured_mae: `0.017312`
- val_structured_rmse: `0.018869`

## Test Metrics

- test_loss: `0.027079`
- test_mae: `0.003241`
- test_rmse: `0.003677`
- test_structured_mae: `0.017573`
- test_structured_rmse: `0.019433`

## Interpretation

The held-out val error stayed finite with MAE=0.003265 deg and RMSE=0.003797 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003241 deg and RMSE=0.003677 deg, which indicates a numerically stable baseline run.
