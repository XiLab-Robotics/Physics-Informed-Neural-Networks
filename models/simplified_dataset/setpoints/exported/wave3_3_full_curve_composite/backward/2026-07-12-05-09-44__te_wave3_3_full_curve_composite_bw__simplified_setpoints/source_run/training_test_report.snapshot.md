# Wave3 3 Full Curve Composite Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_bw__simplified_setpoints`
- Model Family: `wave3_3_full_curve_composite_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=140-val_mae=0.00365689.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.017043`
- val_mae: `0.003657`
- val_rmse: `0.004518`
- val_pointwise_loss: `0.011068`
- val_centered_curve_shape_loss: `0.006589`
- val_curve_offset_loss: `0.004478`
- val_curve_amplitude_loss: `0.027371`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_structured_mae: `0.027867`
- val_structured_rmse: `0.033991`
- val_residual_offset_mean_abs: `0.027541`

## Test Metrics

- test_loss: `0.012811`
- test_mae: `0.003553`
- test_rmse: `0.004307`
- test_pointwise_loss: `0.008874`
- test_centered_curve_shape_loss: `0.003386`
- test_curve_offset_loss: `0.005488`
- test_curve_amplitude_loss: `0.011591`
- test_sparse_harmonic_shape_loss: `7.337892e-05`
- test_structured_mae: `0.030061`
- test_structured_rmse: `0.037111`
- test_residual_offset_mean_abs: `0.029809`

## Interpretation

The held-out val error stayed finite with MAE=0.003657 deg and RMSE=0.004518 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003553 deg and RMSE=0.004307 deg, which indicates a numerically stable baseline run.
