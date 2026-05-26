# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_sequence_remote_Bw`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution_bw\2026-05-25-16-18-28__te_periodic_temporal_convolution_sequence_remote_bw\checkpoints\periodic_temporal_convolution-epoch=018-val_mae=0.00388991.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.044737`
- val_mae: `0.003890`
- val_rmse: `0.004504`

## Test Metrics

- test_loss: `0.032647`
- test_mae: `0.003614`
- test_rmse: `0.004163`

## Interpretation

The held-out val error stayed finite with MAE=0.003890 deg and RMSE=0.004504 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003614 deg and RMSE=0.004163 deg, which indicates a numerically stable baseline run.
