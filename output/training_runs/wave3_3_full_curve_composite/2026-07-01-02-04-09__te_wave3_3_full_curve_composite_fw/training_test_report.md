# Wave3 3 Full Curve Composite Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_fw`
- Model Family: `wave3_3_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=057-val_mae=0.00189842.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.009022`
- val_mae: `0.001898`
- val_rmse: `0.002338`
- val_pointwise_loss: `0.005004`
- val_centered_curve_shape_loss: `0.004643`
- val_curve_offset_loss: `0.000361`
- val_curve_amplitude_loss: `0.027158`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.008060`
- val_structured_rmse: `0.008486`
- val_residual_offset_mean_abs: `0.007577`

## Test Metrics

- test_loss: `0.010708`
- test_mae: `0.002038`
- test_rmse: `0.002607`
- test_pointwise_loss: `0.005918`
- test_centered_curve_shape_loss: `0.005419`
- test_curve_offset_loss: `0.000499`
- test_curve_amplitude_loss: `0.032442`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.007928`
- test_structured_rmse: `0.008532`
- test_residual_offset_mean_abs: `0.007342`

## Interpretation

The held-out val error stayed finite with MAE=0.001898 deg and RMSE=0.002338 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002038 deg and RMSE=0.002607 deg, which indicates a numerically stable baseline run.
