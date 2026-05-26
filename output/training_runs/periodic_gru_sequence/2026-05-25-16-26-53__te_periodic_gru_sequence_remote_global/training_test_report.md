# Periodic Gru Sequence Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_remote_global`
- Model Family: `periodic_gru_sequence`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-05-25-16-26-53__te_periodic_gru_sequence_remote_global\checkpoints\periodic_gru_sequence-epoch=251-val_mae=0.00250715.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004826`
- val_mae: `0.002507`
- val_rmse: `0.002819`

## Test Metrics

- test_loss: `0.005144`
- test_mae: `0.002681`
- test_rmse: `0.002971`

## Interpretation

The held-out val error stayed finite with MAE=0.002507 deg and RMSE=0.002819 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002681 deg and RMSE=0.002971 deg, which indicates a numerically stable baseline run.
