# Residual Harmonic Gru Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-04-00__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=058-val_mae=0.00205854.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005460`
- val_mae: `0.002059`
- val_rmse: `0.002854`
- val_pointwise_loss: `0.005460`
- val_centered_curve_shape_loss: `0.004923`
- val_curve_offset_loss: `0.000537`
- val_curve_amplitude_loss: `0.039300`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039783`
- val_structured_rmse: `0.044479`

## Test Metrics

- test_loss: `0.008905`
- test_mae: `0.002369`
- test_rmse: `0.003732`
- test_pointwise_loss: `0.008905`
- test_centered_curve_shape_loss: `0.005827`
- test_curve_offset_loss: `0.003077`
- test_curve_amplitude_loss: `0.050037`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037421`
- test_structured_rmse: `0.042500`

## Interpretation

The held-out val error stayed finite with MAE=0.002059 deg and RMSE=0.002854 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002369 deg and RMSE=0.003732 deg, which indicates a numerically stable baseline run.
