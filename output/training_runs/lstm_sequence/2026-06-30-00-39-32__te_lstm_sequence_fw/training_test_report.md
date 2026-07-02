# Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_fw`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-00-39-32__te_lstm_sequence_fw\checkpoints\lstm_sequence-epoch=085-val_mae=0.00216870.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005797`
- val_mae: `0.002169`
- val_rmse: `0.002697`
- val_pointwise_loss: `0.005797`
- val_centered_curve_shape_loss: `0.005418`
- val_curve_offset_loss: `0.000379`
- val_curve_amplitude_loss: `0.059460`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006628`
- test_mae: `0.002282`
- test_rmse: `0.002920`
- test_pointwise_loss: `0.006628`
- test_centered_curve_shape_loss: `0.006262`
- test_curve_offset_loss: `0.000366`
- test_curve_amplitude_loss: `0.065064`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002169 deg and RMSE=0.002697 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002282 deg and RMSE=0.002920 deg, which indicates a numerically stable baseline run.
