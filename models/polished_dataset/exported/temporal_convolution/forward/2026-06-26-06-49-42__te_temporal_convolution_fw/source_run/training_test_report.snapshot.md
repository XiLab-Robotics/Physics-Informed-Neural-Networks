# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_fw`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-06-49-42__te_temporal_convolution_fw\checkpoints\temporal_convolution-epoch=069-val_mae=0.00231121.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006212`
- val_mae: `0.002311`
- val_rmse: `0.002865`
- val_pointwise_loss: `0.006212`
- val_centered_curve_shape_loss: `0.005445`
- val_curve_offset_loss: `0.000768`
- val_curve_amplitude_loss: `0.057183`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006988`
- test_mae: `0.002399`
- test_rmse: `0.003061`
- test_pointwise_loss: `0.006988`
- test_centered_curve_shape_loss: `0.006209`
- test_curve_offset_loss: `0.000779`
- test_curve_amplitude_loss: `0.062581`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002311 deg and RMSE=0.002865 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002399 deg and RMSE=0.003061 deg, which indicates a numerically stable baseline run.
