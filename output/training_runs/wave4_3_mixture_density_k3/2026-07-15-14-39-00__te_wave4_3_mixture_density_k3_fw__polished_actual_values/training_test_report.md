# Wave4 3 Mixture Density K3 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_fw__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00161545.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.976351`
- val_mae: `0.001615`
- val_rmse: `0.002403`
- val_pointwise_loss: `-1.976351`
- val_centered_curve_shape_loss: `0.003805`
- val_curve_offset_loss: `0.000287`
- val_curve_amplitude_loss: `0.019877`
- val_sparse_harmonic_shape_loss: `7.963139e-05`
- val_mixture_weight_entropy: `0.131468`
- val_mixture_effective_components: `1.167730`
- val_mixture_mean_sigma: `0.027134`
- val_mixture_component_separation: `0.045562`
- val_structured_mae: `0.050060`
- val_structured_rmse: `0.068680`
- val_residual_offset_mean_abs: `0.076893`

## Test Metrics

- test_loss: `-1.937587`
- test_mae: `0.001803`
- test_rmse: `0.003007`
- test_pointwise_loss: `-1.937587`
- test_centered_curve_shape_loss: `0.004803`
- test_curve_offset_loss: `0.000973`
- test_curve_amplitude_loss: `0.020171`
- test_sparse_harmonic_shape_loss: `8.893468e-05`
- test_mixture_weight_entropy: `0.158617`
- test_mixture_effective_components: `1.204627`
- test_mixture_mean_sigma: `0.025842`
- test_mixture_component_separation: `0.044977`
- test_structured_mae: `0.049815`
- test_structured_rmse: `0.068103`
- test_residual_offset_mean_abs: `0.075907`

## Interpretation

The held-out val error stayed finite with MAE=0.001615 deg and RMSE=0.002403 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001803 deg and RMSE=0.003007 deg, which indicates a numerically stable baseline run.
