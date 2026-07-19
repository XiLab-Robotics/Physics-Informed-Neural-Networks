# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_bw__polished_setpoints`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/checkpoints/gru_sequence-epoch=088-val_mae=0.00218293.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005814`
- val_mae: `0.002183`
- val_rmse: `0.003013`
- val_pointwise_loss: `0.005814`
- val_centered_curve_shape_loss: `0.005383`
- val_curve_offset_loss: `0.000431`
- val_curve_amplitude_loss: `0.059720`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009311`
- test_mae: `0.002467`
- test_rmse: `0.003849`
- test_pointwise_loss: `0.009311`
- test_centered_curve_shape_loss: `0.006291`
- test_curve_offset_loss: `0.003020`
- test_curve_amplitude_loss: `0.072577`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002183 deg and RMSE=0.003013 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002467 deg and RMSE=0.003849 deg, which indicates a numerically stable baseline run.
