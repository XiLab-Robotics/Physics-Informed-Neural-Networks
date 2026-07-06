# Wave4 3 Mixture Density K3 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_global`
- Model Family: `wave4_3_mixture_density_k3_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=187-val_mae=0.00140729.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-2.052314`
- val_mae: `0.001407`
- val_rmse: `0.001764`
- val_pointwise_loss: `-2.052314`
- val_centered_curve_shape_loss: `0.002092`
- val_curve_offset_loss: `0.000248`
- val_curve_amplitude_loss: `0.011220`
- val_sparse_harmonic_shape_loss: `3.356515e-05`
- val_mixture_weight_entropy: `0.040275`
- val_mixture_effective_components: `1.049762`
- val_mixture_mean_sigma: `0.012326`
- val_mixture_component_separation: `0.026302`
- val_structured_mae: `0.066941`
- val_structured_rmse: `0.091471`
- val_residual_offset_mean_abs: `0.059789`

## Test Metrics

- test_loss: `-2.020453`
- test_mae: `0.001544`
- test_rmse: `0.001992`
- test_pointwise_loss: `-2.020453`
- test_centered_curve_shape_loss: `0.002811`
- test_curve_offset_loss: `0.000301`
- test_curve_amplitude_loss: `0.012604`
- test_sparse_harmonic_shape_loss: `4.141702e-05`
- test_mixture_weight_entropy: `0.065960`
- test_mixture_effective_components: `1.086896`
- test_mixture_mean_sigma: `0.012447`
- test_mixture_component_separation: `0.025464`
- test_structured_mae: `0.066771`
- test_structured_rmse: `0.091207`
- test_residual_offset_mean_abs: `0.058011`

## Interpretation

The held-out val error stayed finite with MAE=0.001407 deg and RMSE=0.001764 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001544 deg and RMSE=0.001992 deg, which indicates a numerically stable baseline run.
