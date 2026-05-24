# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_sequence_remote_Fw`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution_fw\2026-05-24-11-30-23__te_temporal_convolution_sequence_remote_fw\checkpoints\temporal_convolution-epoch=059-val_mae=0.00349000.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.036765`
- val_mae: `0.003490`
- val_rmse: `0.004105`

## Test Metrics

- test_loss: `0.034974`
- test_mae: `0.003611`
- test_rmse: `0.004183`

## Interpretation

The held-out val error stayed finite with MAE=0.003490 deg and RMSE=0.004105 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003611 deg and RMSE=0.004183 deg, which indicates a numerically stable baseline run.
