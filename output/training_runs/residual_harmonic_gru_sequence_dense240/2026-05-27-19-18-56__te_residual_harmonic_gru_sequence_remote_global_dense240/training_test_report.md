# Residual Harmonic Gru Sequence Dense240 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_global_dense240`
- Model Family: `residual_harmonic_gru_sequence_dense240`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-05-27-19-18-56__te_residual_harmonic_gru_sequence_remote_global_dense240\checkpoints\residual_harmonic_gru_sequence-epoch=020-val_mae=0.00359991.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010984`
- val_mae: `0.003600`
- val_rmse: `0.004167`
- val_structured_mae: `0.037828`
- val_structured_rmse: `0.038360`

## Test Metrics

- test_loss: `0.008883`
- test_mae: `0.003511`
- test_rmse: `0.003983`
- test_structured_mae: `0.040703`
- test_structured_rmse: `0.041094`

## Interpretation

The held-out val error stayed finite with MAE=0.003600 deg and RMSE=0.004167 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003511 deg and RMSE=0.003983 deg, which indicates a numerically stable baseline run.
