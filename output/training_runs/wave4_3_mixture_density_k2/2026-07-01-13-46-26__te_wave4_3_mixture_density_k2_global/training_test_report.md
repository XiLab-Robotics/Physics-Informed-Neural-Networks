# Wave4 3 Mixture Density K2 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_global`
- Model Family: `wave4_3_mixture_density_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=165-val_mae=0.00154977.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.988213`
- val_mae: `0.001550`
- val_rmse: `0.001938`
- val_pointwise_loss: `-1.988213`
- val_centered_curve_shape_loss: `0.003318`
- val_curve_offset_loss: `0.000275`
- val_curve_amplitude_loss: `0.021297`
- val_sparse_harmonic_shape_loss: `6.672249e-05`
- val_mixture_weight_entropy: `0.041517`
- val_mixture_effective_components: `1.049274`
- val_mixture_mean_sigma: `0.004892`
- val_mixture_component_separation: `0.008239`
- val_structured_mae: `0.059589`
- val_structured_rmse: `0.086380`
- val_residual_offset_mean_abs: `0.050498`

## Test Metrics

- test_loss: `-1.943508`
- test_mae: `0.001743`
- test_rmse: `0.002245`
- test_pointwise_loss: `-1.943508`
- test_centered_curve_shape_loss: `0.004381`
- test_curve_offset_loss: `0.000410`
- test_curve_amplitude_loss: `0.028820`
- test_sparse_harmonic_shape_loss: `8.400306e-05`
- test_mixture_weight_entropy: `0.051068`
- test_mixture_effective_components: `1.060005`
- test_mixture_mean_sigma: `0.005058`
- test_mixture_component_separation: `0.007830`
- test_structured_mae: `0.059635`
- test_structured_rmse: `0.086286`
- test_residual_offset_mean_abs: `0.048625`

## Interpretation

The held-out val error stayed finite with MAE=0.001550 deg and RMSE=0.001938 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001743 deg and RMSE=0.002245 deg, which indicates a numerically stable baseline run.
