# Wave4 2 Gaussian Nll Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_bw__polished_actual_values`
- Model Family: `wave4_2_gaussian_nll_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=255-val_mae=0.00180572.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.743965`
- val_mae: `0.001806`
- val_rmse: `0.002581`
- val_pointwise_loss: `-1.743965`
- val_centered_curve_shape_loss: `0.004578`
- val_curve_offset_loss: `0.000351`
- val_curve_amplitude_loss: `0.037074`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_interval_coverage: `0.879322`
- val_interval_width: `0.007501`
- val_mean_sigma: `0.002927`
- val_structured_mae: `0.034415`
- val_structured_rmse: `0.045585`
- val_residual_offset_mean_abs: `0.069343`

## Test Metrics

- test_loss: `-1.669624`
- test_mae: `0.002032`
- test_rmse: `0.003297`
- test_pointwise_loss: `-1.669624`
- test_centered_curve_shape_loss: `0.005472`
- test_curve_offset_loss: `0.001742`
- test_curve_amplitude_loss: `0.042185`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_interval_coverage: `0.876316`
- test_interval_width: `0.007849`
- test_mean_sigma: `0.003062`
- test_structured_mae: `0.033861`
- test_structured_rmse: `0.044180`
- test_residual_offset_mean_abs: `0.067918`

## Interpretation

The held-out val error stayed finite with MAE=0.001806 deg and RMSE=0.002581 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002032 deg and RMSE=0.003297 deg, which indicates a numerically stable baseline run.
