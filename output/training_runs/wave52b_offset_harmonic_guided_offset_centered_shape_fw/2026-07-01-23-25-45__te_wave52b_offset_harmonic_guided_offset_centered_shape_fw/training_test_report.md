# Wave52B Offset Harmonic Guided Offset Centered Shape Fw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_fw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_fw\2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=155-val_mae=0.00225772.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030796`
- val_mae: `0.002258`
- val_rmse: `0.002787`
- val_pointwise_loss: `0.020321`
- val_centered_curve_shape_loss: `0.018971`
- val_curve_offset_loss: `0.001350`
- val_curve_amplitude_loss: `0.129568`
- val_sparse_harmonic_shape_loss: `0.000436`
- val_structured_mae: `0.019635`
- val_structured_rmse: `0.023073`
- val_base_mae: `0.011242`
- val_base_rmse: `0.012976`
- val_residual_offset_mean_abs: `0.010833`

## Test Metrics

- test_loss: `0.019737`
- test_mae: `0.001931`
- test_rmse: `0.002445`
- test_pointwise_loss: `0.013118`
- test_centered_curve_shape_loss: `0.011570`
- test_curve_offset_loss: `0.001548`
- test_curve_amplitude_loss: `0.081451`
- test_sparse_harmonic_shape_loss: `0.000250`
- test_structured_mae: `0.020063`
- test_structured_rmse: `0.023460`
- test_base_mae: `0.010922`
- test_base_rmse: `0.012659`
- test_residual_offset_mean_abs: `0.010755`

## Interpretation

The held-out val error stayed finite with MAE=0.002258 deg and RMSE=0.002787 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001931 deg and RMSE=0.002445 deg, which indicates a numerically stable baseline run.
