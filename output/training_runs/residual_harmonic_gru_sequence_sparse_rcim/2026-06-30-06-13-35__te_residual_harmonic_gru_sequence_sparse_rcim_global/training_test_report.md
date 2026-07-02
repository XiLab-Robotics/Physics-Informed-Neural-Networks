# Residual Harmonic Gru Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_global`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global\checkpoints\residual_harmonic_gru_sequence-epoch=076-val_mae=0.00197322.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005271`
- val_mae: `0.001973`
- val_rmse: `0.002442`
- val_pointwise_loss: `0.005271`
- val_centered_curve_shape_loss: `0.004943`
- val_curve_offset_loss: `0.000328`
- val_curve_amplitude_loss: `0.039382`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039834`
- val_structured_rmse: `0.042029`

## Test Metrics

- test_loss: `0.006084`
- test_mae: `0.002104`
- test_rmse: `0.002690`
- test_pointwise_loss: `0.006084`
- test_centered_curve_shape_loss: `0.005673`
- test_curve_offset_loss: `0.000411`
- test_curve_amplitude_loss: `0.044323`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037353`
- test_structured_rmse: `0.040288`

## Interpretation

The held-out val error stayed finite with MAE=0.001973 deg and RMSE=0.002442 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002104 deg and RMSE=0.002690 deg, which indicates a numerically stable baseline run.
