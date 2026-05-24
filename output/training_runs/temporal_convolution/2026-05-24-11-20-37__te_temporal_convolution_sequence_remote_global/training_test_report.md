# Temporal Convolution Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_sequence_remote_global`
- Model Family: `temporal_convolution`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-05-24-11-20-37__te_temporal_convolution_sequence_remote_global\checkpoints\temporal_convolution-epoch=055-val_mae=0.00393457.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013080`
- val_mae: `0.003935`
- val_rmse: `0.004532`

## Test Metrics

- test_loss: `0.010646`
- test_mae: `0.003754`
- test_rmse: `0.004266`

## Interpretation

The held-out val error stayed finite with MAE=0.003935 deg and RMSE=0.004532 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003754 deg and RMSE=0.004266 deg, which indicates a numerically stable baseline run.
