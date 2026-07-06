# Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_bw`
- Model Family: `lstm_sequence_bw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-01-02-22__te_lstm_sequence_bw\checkpoints\lstm_sequence-epoch=138-val_mae=0.00214675.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005761`
- val_mae: `0.002147`
- val_rmse: `0.002675`
- val_pointwise_loss: `0.005761`
- val_centered_curve_shape_loss: `0.005435`
- val_curve_offset_loss: `0.000326`
- val_curve_amplitude_loss: `0.062836`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006605`
- test_mae: `0.002259`
- test_rmse: `0.002907`
- test_pointwise_loss: `0.006605`
- test_centered_curve_shape_loss: `0.006192`
- test_curve_offset_loss: `0.000413`
- test_curve_amplitude_loss: `0.068599`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002147 deg and RMSE=0.002675 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002259 deg and RMSE=0.002907 deg, which indicates a numerically stable baseline run.
