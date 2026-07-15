# Wave4 3 Mixture Density K2 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_fw__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00172453.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.915686`
- val_mae: `0.001725`
- val_rmse: `0.002464`
- val_pointwise_loss: `-1.915686`
- val_centered_curve_shape_loss: `0.004409`
- val_curve_offset_loss: `0.000260`
- val_curve_amplitude_loss: `0.024677`
- val_sparse_harmonic_shape_loss: `9.858198e-05`
- val_mixture_weight_entropy: `0.053390`
- val_mixture_effective_components: `1.063061`
- val_mixture_mean_sigma: `0.007833`
- val_mixture_component_separation: `0.011857`
- val_structured_mae: `0.053584`
- val_structured_rmse: `0.074353`
- val_residual_offset_mean_abs: `0.066065`

## Test Metrics

- test_loss: `-1.888555`
- test_mae: `0.001936`
- test_rmse: `0.003224`
- test_pointwise_loss: `-1.888555`
- test_centered_curve_shape_loss: `0.005190`
- test_curve_offset_loss: `0.001898`
- test_curve_amplitude_loss: `0.026198`
- test_sparse_harmonic_shape_loss: `0.000105`
- test_mixture_weight_entropy: `0.068848`
- test_mixture_effective_components: `1.082603`
- test_mixture_mean_sigma: `0.008188`
- test_mixture_component_separation: `0.011477`
- test_structured_mae: `0.053547`
- test_structured_rmse: `0.073911`
- test_residual_offset_mean_abs: `0.064661`

## Interpretation

The held-out val error stayed finite with MAE=0.001725 deg and RMSE=0.002464 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001936 deg and RMSE=0.003224 deg, which indicates a numerically stable baseline run.
