# Periodic Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_global`
- Model Family: `periodic_gru_sequence_global`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-02-14-43__te_periodic_gru_sequence_global\checkpoints\periodic_gru_sequence-epoch=236-val_mae=0.00113201.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001205`
- val_mae: `0.001132`
- val_rmse: `0.001391`
- val_pointwise_loss: `0.001205`
- val_centered_curve_shape_loss: `0.000815`
- val_curve_offset_loss: `0.000390`
- val_curve_amplitude_loss: `0.002624`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001399`
- test_mae: `0.001159`
- test_rmse: `0.001465`
- test_pointwise_loss: `0.001399`
- test_centered_curve_shape_loss: `0.001018`
- test_curve_offset_loss: `0.000381`
- test_curve_amplitude_loss: `0.003019`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001132 deg and RMSE=0.001391 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001159 deg and RMSE=0.001465 deg, which indicates a numerically stable baseline run.
