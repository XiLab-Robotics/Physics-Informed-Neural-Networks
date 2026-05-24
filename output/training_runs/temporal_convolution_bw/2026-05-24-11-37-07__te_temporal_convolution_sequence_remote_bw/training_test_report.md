# Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_sequence_remote_Bw`
- Model Family: `temporal_convolution_bw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution_bw\2026-05-24-11-37-07__te_temporal_convolution_sequence_remote_bw\checkpoints\temporal_convolution-epoch=089-val_mae=0.00393295.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.049321`
- val_mae: `0.003933`
- val_rmse: `0.004617`

## Test Metrics

- test_loss: `0.036721`
- test_mae: `0.003739`
- test_rmse: `0.004369`

## Interpretation

The held-out val error stayed finite with MAE=0.003933 deg and RMSE=0.004617 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003739 deg and RMSE=0.004369 deg, which indicates a numerically stable baseline run.
