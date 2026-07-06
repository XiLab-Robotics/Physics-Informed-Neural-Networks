# Periodic Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_bw`
- Model Family: `periodic_lstm_sequence_bw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-05-26-57__te_periodic_lstm_sequence_bw\checkpoints\periodic_lstm_sequence-epoch=250-val_mae=0.00122970.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001494`
- val_mae: `0.001230`
- val_rmse: `0.001520`
- val_pointwise_loss: `0.001494`
- val_centered_curve_shape_loss: `0.001073`
- val_curve_offset_loss: `0.000421`
- val_curve_amplitude_loss: `0.003342`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001604`
- test_mae: `0.001226`
- test_rmse: `0.001558`
- test_pointwise_loss: `0.001604`
- test_centered_curve_shape_loss: `0.001187`
- test_curve_offset_loss: `0.000417`
- test_curve_amplitude_loss: `0.003060`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001230 deg and RMSE=0.001520 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001226 deg and RMSE=0.001558 deg, which indicates a numerically stable baseline run.
