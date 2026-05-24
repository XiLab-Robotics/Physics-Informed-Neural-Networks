# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_remote_Bw`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence_bw\2026-05-24-12-00-05__te_gru_sequence_remote_bw\checkpoints\gru_sequence-epoch=058-val_mae=0.00386744.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.047938`
- val_mae: `0.003867`
- val_rmse: `0.004567`

## Test Metrics

- test_loss: `0.035018`
- test_mae: `0.003631`
- test_rmse: `0.004297`

## Interpretation

The held-out val error stayed finite with MAE=0.003867 deg and RMSE=0.004567 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003631 deg and RMSE=0.004297 deg, which indicates a numerically stable baseline run.
