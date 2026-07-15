# Wave4 3 Mixture Density K2 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_global__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-04-04-29__te_wave4_3_mixture_density_k2_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=252-val_mae=0.00175520.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.950786`
- val_mae: `0.001755`
- val_rmse: `0.002531`
- val_pointwise_loss: `-1.950786`
- val_centered_curve_shape_loss: `0.004600`
- val_curve_offset_loss: `0.000283`
- val_curve_amplitude_loss: `0.037701`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_mixture_weight_entropy: `0.007888`
- val_mixture_effective_components: `1.008026`
- val_mixture_mean_sigma: `0.024428`
- val_mixture_component_separation: `0.035830`
- val_structured_mae: `0.055767`
- val_structured_rmse: `0.076314`
- val_residual_offset_mean_abs: `0.061632`

## Test Metrics

- test_loss: `-1.892673`
- test_mae: `0.001975`
- test_rmse: `0.003299`
- test_pointwise_loss: `-1.892673`
- test_centered_curve_shape_loss: `0.006801`
- test_curve_offset_loss: `0.000626`
- test_curve_amplitude_loss: `0.062806`
- test_sparse_harmonic_shape_loss: `0.000123`
- test_mixture_weight_entropy: `0.011724`
- test_mixture_effective_components: `1.012606`
- test_mixture_mean_sigma: `0.023377`
- test_mixture_component_separation: `0.035376`
- test_structured_mae: `0.054608`
- test_structured_rmse: `0.074858`
- test_residual_offset_mean_abs: `0.061908`

## Interpretation

The held-out val error stayed finite with MAE=0.001755 deg and RMSE=0.002531 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001975 deg and RMSE=0.003299 deg, which indicates a numerically stable baseline run.
