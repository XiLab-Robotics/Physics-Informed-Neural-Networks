# Wave3 3 Raw Offset Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_global`
- Model Family: `wave3_3_raw_offset_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=058-val_mae=0.00186253.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005189`
- val_mae: `0.001863`
- val_rmse: `0.002293`
- val_pointwise_loss: `0.005015`
- val_centered_curve_shape_loss: `0.004627`
- val_curve_offset_loss: `0.000388`
- val_curve_amplitude_loss: `0.035837`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.021884`
- val_structured_rmse: `0.023678`
- val_residual_offset_mean_abs: `0.021610`

## Test Metrics

- test_loss: `0.006041`
- test_mae: `0.002014`
- test_rmse: `0.002561`
- test_pointwise_loss: `0.005842`
- test_centered_curve_shape_loss: `0.005399`
- test_curve_offset_loss: `0.000443`
- test_curve_amplitude_loss: `0.040266`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.022027`
- test_structured_rmse: `0.024212`
- test_residual_offset_mean_abs: `0.021649`

## Interpretation

The held-out val error stayed finite with MAE=0.001863 deg and RMSE=0.002293 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002014 deg and RMSE=0.002561 deg, which indicates a numerically stable baseline run.
