# Wave4 3 Mixture Density K2 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_bw__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-06-02-16__te_wave4_3_mixture_density_k2_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=129-val_mae=0.00180093.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.766358`
- val_mae: `0.001801`
- val_rmse: `0.002574`
- val_pointwise_loss: `-1.766358`
- val_centered_curve_shape_loss: `0.004597`
- val_curve_offset_loss: `0.000333`
- val_curve_amplitude_loss: `0.030130`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_mixture_weight_entropy: `0.019050`
- val_mixture_effective_components: `1.020036`
- val_mixture_mean_sigma: `0.085255`
- val_mixture_component_separation: `0.051193`
- val_structured_mae: `0.057960`
- val_structured_rmse: `0.079466`
- val_residual_offset_mean_abs: `0.071445`

## Test Metrics

- test_loss: `-1.678490`
- test_mae: `0.002086`
- test_rmse: `0.003379`
- test_pointwise_loss: `-1.678490`
- test_centered_curve_shape_loss: `0.005420`
- test_curve_offset_loss: `0.002247`
- test_curve_amplitude_loss: `0.037677`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_mixture_weight_entropy: `0.019992`
- test_mixture_effective_components: `1.020911`
- test_mixture_mean_sigma: `0.092836`
- test_mixture_component_separation: `0.050944`
- test_structured_mae: `0.057728`
- test_structured_rmse: `0.079410`
- test_residual_offset_mean_abs: `0.070458`

## Interpretation

The held-out val error stayed finite with MAE=0.001801 deg and RMSE=0.002574 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002086 deg and RMSE=0.003379 deg, which indicates a numerically stable baseline run.
