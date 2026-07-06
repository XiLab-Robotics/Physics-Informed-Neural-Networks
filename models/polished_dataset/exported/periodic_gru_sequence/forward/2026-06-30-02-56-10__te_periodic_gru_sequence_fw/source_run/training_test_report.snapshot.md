# Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_fw`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw\checkpoints\periodic_gru_sequence-epoch=235-val_mae=0.00108406.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001118`
- val_mae: `0.001084`
- val_rmse: `0.001347`
- val_pointwise_loss: `0.001118`
- val_centered_curve_shape_loss: `0.000763`
- val_curve_offset_loss: `0.000355`
- val_curve_amplitude_loss: `0.002312`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001318`
- test_mae: `0.001121`
- test_rmse: `0.001444`
- test_pointwise_loss: `0.001318`
- test_centered_curve_shape_loss: `0.000974`
- test_curve_offset_loss: `0.000344`
- test_curve_amplitude_loss: `0.002778`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001084 deg and RMSE=0.001347 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001121 deg and RMSE=0.001444 deg, which indicates a numerically stable baseline run.
