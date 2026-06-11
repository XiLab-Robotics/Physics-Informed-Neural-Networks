# Track2H Dispersion Aware Smooth L1 Robust Global Training And Testing Report

## Overview

- Run Name: `te_track2h_smooth_l1_robust_global`
- Model Family: `track2h_dispersion_aware_smooth_l1_robust_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_global\2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=057-val_mae=0.00364085.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005536`
- val_mae: `0.003641`
- val_rmse: `0.004143`
- val_pointwise_loss: `0.005536`
- val_centered_curve_shape_loss: `0.006474`
- val_curve_offset_loss: `0.004597`
- val_curve_amplitude_loss: `0.052009`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_structured_mae: `0.026382`
- val_structured_rmse: `0.027720`
- val_residual_offset_mean_abs: `0.026369`

## Test Metrics

- test_loss: `0.004184`
- test_mae: `0.003422`
- test_rmse: `0.003810`
- test_pointwise_loss: `0.004184`
- test_centered_curve_shape_loss: `0.003208`
- test_curve_offset_loss: `0.005161`
- test_curve_amplitude_loss: `0.023321`
- test_sparse_harmonic_shape_loss: `6.943590e-05`
- test_structured_mae: `0.029865`
- test_structured_rmse: `0.030888`
- test_residual_offset_mean_abs: `0.030098`

## Interpretation

The held-out val error stayed finite with MAE=0.003641 deg and RMSE=0.004143 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003422 deg and RMSE=0.003810 deg, which indicates a numerically stable baseline run.
