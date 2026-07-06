# Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_global`
- Model Family: `gru_sequence_global`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-22-50-48__te_gru_sequence_global\checkpoints\gru_sequence-epoch=050-val_mae=0.00220547.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005866`
- val_mae: `0.002205`
- val_rmse: `0.002726`
- val_pointwise_loss: `0.005866`
- val_centered_curve_shape_loss: `0.005406`
- val_curve_offset_loss: `0.000460`
- val_curve_amplitude_loss: `0.053421`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006697`
- test_mae: `0.002311`
- test_rmse: `0.002954`
- test_pointwise_loss: `0.006697`
- test_centered_curve_shape_loss: `0.006203`
- test_curve_offset_loss: `0.000494`
- test_curve_amplitude_loss: `0.058753`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002205 deg and RMSE=0.002726 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002311 deg and RMSE=0.002954 deg, which indicates a numerically stable baseline run.
