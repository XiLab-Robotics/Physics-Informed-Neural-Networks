# Wave4 3 Mixture Density K3 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_global__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k3_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=164-val_mae=0.00178681.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.822902`
- val_mae: `0.001787`
- val_rmse: `0.002542`
- val_pointwise_loss: `-1.822902`
- val_centered_curve_shape_loss: `0.004499`
- val_curve_offset_loss: `0.000272`
- val_curve_amplitude_loss: `0.032859`
- val_sparse_harmonic_shape_loss: `9.857834e-05`
- val_mixture_weight_entropy: `0.108020`
- val_mixture_effective_components: `1.128816`
- val_mixture_mean_sigma: `0.013498`
- val_mixture_component_separation: `0.043722`
- val_structured_mae: `0.054410`
- val_structured_rmse: `0.074487`
- val_residual_offset_mean_abs: `0.069220`

## Test Metrics

- test_loss: `-1.782015`
- test_mae: `0.001980`
- test_rmse: `0.003276`
- test_pointwise_loss: `-1.782015`
- test_centered_curve_shape_loss: `0.006570`
- test_curve_offset_loss: `0.000571`
- test_curve_amplitude_loss: `0.066581`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_mixture_weight_entropy: `0.112815`
- test_mixture_effective_components: `1.134051`
- test_mixture_mean_sigma: `0.013213`
- test_mixture_component_separation: `0.042570`
- test_structured_mae: `0.053467`
- test_structured_rmse: `0.073288`
- test_residual_offset_mean_abs: `0.067559`

## Interpretation

The held-out val error stayed finite with MAE=0.001787 deg and RMSE=0.002542 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001980 deg and RMSE=0.003276 deg, which indicates a numerically stable baseline run.
