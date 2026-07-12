# Wave3 3 Full Curve Composite Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_bw__polished_actual_values`
- Model Family: `wave3_3_full_curve_composite_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=143-val_mae=0.00194357.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008189`
- val_mae: `0.001944`
- val_rmse: `0.002730`
- val_pointwise_loss: `0.005156`
- val_centered_curve_shape_loss: `0.004817`
- val_curve_offset_loss: `0.000339`
- val_curve_amplitude_loss: `0.016942`
- val_sparse_harmonic_shape_loss: `0.000106`
- val_structured_mae: `0.007997`
- val_structured_rmse: `0.009700`
- val_residual_offset_mean_abs: `0.007603`

## Test Metrics

- test_loss: `0.009545`
- test_mae: `0.002070`
- test_rmse: `0.003119`
- test_pointwise_loss: `0.006010`
- test_centered_curve_shape_loss: `0.005574`
- test_curve_offset_loss: `0.000435`
- test_curve_amplitude_loss: `0.019723`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.007865`
- test_structured_rmse: `0.009792`
- test_residual_offset_mean_abs: `0.007383`

## Interpretation

The held-out val error stayed finite with MAE=0.001944 deg and RMSE=0.002730 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002070 deg and RMSE=0.003119 deg, which indicates a numerically stable baseline run.
