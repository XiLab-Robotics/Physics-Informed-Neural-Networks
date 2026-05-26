# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_sequence_remote_Fw`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution_fw\2026-05-25-16-10-13__te_periodic_temporal_convolution_sequence_remote_fw\checkpoints\periodic_temporal_convolution-epoch=017-val_mae=0.00332097.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033050`
- val_mae: `0.003321`
- val_rmse: `0.003913`

## Test Metrics

- test_loss: `0.029617`
- test_mae: `0.003337`
- test_rmse: `0.003830`

## Interpretation

The held-out val error stayed finite with MAE=0.003321 deg and RMSE=0.003913 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003337 deg and RMSE=0.003830 deg, which indicates a numerically stable baseline run.
