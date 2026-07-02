# Wave3 3 Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_global`
- Model Family: `wave3_3_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=095-val_mae=0.00189366.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008217`
- val_mae: `0.001894`
- val_rmse: `0.002340`
- val_pointwise_loss: `0.005159`
- val_centered_curve_shape_loss: `0.004831`
- val_curve_offset_loss: `0.000328`
- val_curve_amplitude_loss: `0.017200`
- val_sparse_harmonic_shape_loss: `0.000106`
- val_structured_mae: `0.007062`
- val_structured_rmse: `0.007566`
- val_residual_offset_mean_abs: `0.006601`

## Test Metrics

- test_loss: `0.009443`
- test_mae: `0.002023`
- test_rmse: `0.002587`
- test_pointwise_loss: `0.005966`
- test_centered_curve_shape_loss: `0.005637`
- test_curve_offset_loss: `0.000330`
- test_curve_amplitude_loss: `0.019350`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_structured_mae: `0.006803`
- test_structured_rmse: `0.007503`
- test_residual_offset_mean_abs: `0.006312`

## Interpretation

The held-out val error stayed finite with MAE=0.001894 deg and RMSE=0.002340 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002023 deg and RMSE=0.002587 deg, which indicates a numerically stable baseline run.
