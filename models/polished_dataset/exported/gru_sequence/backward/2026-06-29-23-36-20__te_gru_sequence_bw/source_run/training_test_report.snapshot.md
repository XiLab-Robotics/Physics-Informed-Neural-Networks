# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_bw`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-23-36-20__te_gru_sequence_bw\checkpoints\gru_sequence-epoch=148-val_mae=0.00211895.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005666`
- val_mae: `0.002119`
- val_rmse: `0.002629`
- val_pointwise_loss: `0.005666`
- val_centered_curve_shape_loss: `0.005379`
- val_curve_offset_loss: `0.000287`
- val_curve_amplitude_loss: `0.058618`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006462`
- test_mae: `0.002230`
- test_rmse: `0.002860`
- test_pointwise_loss: `0.006462`
- test_centered_curve_shape_loss: `0.006138`
- test_curve_offset_loss: `0.000323`
- test_curve_amplitude_loss: `0.064474`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002119 deg and RMSE=0.002629 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002230 deg and RMSE=0.002860 deg, which indicates a numerically stable baseline run.
