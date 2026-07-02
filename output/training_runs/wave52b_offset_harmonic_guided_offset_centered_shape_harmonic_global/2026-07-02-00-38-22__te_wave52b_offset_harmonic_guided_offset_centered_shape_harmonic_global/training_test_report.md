# Wave52B Offset Harmonic Guided Offset Centered Shape Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global\2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global\checkpoints\wave52b_offset_harmonic_guided-epoch=056-val_mae=0.00188588.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007469`
- val_mae: `0.001886`
- val_rmse: `0.002317`
- val_pointwise_loss: `0.005041`
- val_centered_curve_shape_loss: `0.004628`
- val_curve_offset_loss: `0.000413`
- val_curve_amplitude_loss: `0.028607`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.007150`
- val_structured_rmse: `0.007583`
- val_base_mae: `0.039109`
- val_base_rmse: `0.042833`
- val_residual_offset_mean_abs: `0.007036`

## Test Metrics

- test_loss: `0.011876`
- test_mae: `0.002215`
- test_rmse: `0.002799`
- test_pointwise_loss: `0.008429`
- test_centered_curve_shape_loss: `0.005609`
- test_curve_offset_loss: `0.002820`
- test_curve_amplitude_loss: `0.037840`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.007120`
- test_structured_rmse: `0.007757`
- test_base_mae: `0.036658`
- test_base_rmse: `0.040982`
- test_residual_offset_mean_abs: `0.006872`

## Interpretation

The held-out val error stayed finite with MAE=0.001886 deg and RMSE=0.002317 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002215 deg and RMSE=0.002799 deg, which indicates a numerically stable baseline run.
