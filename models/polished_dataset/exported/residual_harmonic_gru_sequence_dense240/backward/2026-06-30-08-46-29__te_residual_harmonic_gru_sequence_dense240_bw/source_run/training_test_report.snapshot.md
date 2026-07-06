# Residual Harmonic Gru Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_bw`
- Model Family: `residual_harmonic_gru_sequence_dense240_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw\checkpoints\residual_harmonic_gru_sequence-epoch=119-val_mae=0.00198404.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005316`
- val_mae: `0.001984`
- val_rmse: `0.002466`
- val_pointwise_loss: `0.005316`
- val_centered_curve_shape_loss: `0.005001`
- val_curve_offset_loss: `0.000316`
- val_curve_amplitude_loss: `0.035933`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039843`
- val_structured_rmse: `0.042039`

## Test Metrics

- test_loss: `0.006090`
- test_mae: `0.002101`
- test_rmse: `0.002698`
- test_pointwise_loss: `0.006090`
- test_centered_curve_shape_loss: `0.005722`
- test_curve_offset_loss: `0.000367`
- test_curve_amplitude_loss: `0.040729`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037376`
- test_structured_rmse: `0.040321`

## Interpretation

The held-out val error stayed finite with MAE=0.001984 deg and RMSE=0.002466 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002101 deg and RMSE=0.002698 deg, which indicates a numerically stable baseline run.
