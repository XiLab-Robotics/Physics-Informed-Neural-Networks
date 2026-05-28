# Residual Harmonic Gru Sequence Sparse Rcim Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-05-27-18-55-47__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim\checkpoints\residual_harmonic_gru_sequence-epoch=089-val_mae=0.00360653.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011216`
- val_mae: `0.003607`
- val_rmse: `0.004120`
- val_structured_mae: `0.037842`
- val_structured_rmse: `0.038251`

## Test Metrics

- test_loss: `0.008591`
- test_mae: `0.003440`
- test_rmse: `0.003848`
- test_structured_mae: `0.040710`
- test_structured_rmse: `0.041024`

## Interpretation

The held-out val error stayed finite with MAE=0.003607 deg and RMSE=0.004120 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003440 deg and RMSE=0.003848 deg, which indicates a numerically stable baseline run.
