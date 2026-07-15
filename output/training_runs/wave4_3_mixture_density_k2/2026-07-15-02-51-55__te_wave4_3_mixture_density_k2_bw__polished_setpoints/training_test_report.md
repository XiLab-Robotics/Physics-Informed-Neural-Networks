# Wave4 3 Mixture Density K2 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_bw__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=173-val_mae=0.00181733.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.757601`
- val_mae: `0.001817`
- val_rmse: `0.002610`
- val_pointwise_loss: `-1.757601`
- val_centered_curve_shape_loss: `0.004621`
- val_curve_offset_loss: `0.000459`
- val_curve_amplitude_loss: `0.036829`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_mixture_weight_entropy: `0.021023`
- val_mixture_effective_components: `1.023325`
- val_mixture_mean_sigma: `0.017813`
- val_mixture_component_separation: `0.030605`
- val_structured_mae: `0.060221`
- val_structured_rmse: `0.078952`
- val_residual_offset_mean_abs: `0.089492`

## Test Metrics

- test_loss: `-1.600482`
- test_mae: `0.002160`
- test_rmse: `0.003580`
- test_pointwise_loss: `-1.600482`
- test_centered_curve_shape_loss: `0.005572`
- test_curve_offset_loss: `0.002936`
- test_curve_amplitude_loss: `0.047192`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_mixture_weight_entropy: `0.031725`
- test_mixture_effective_components: `1.037053`
- test_mixture_mean_sigma: `0.018028`
- test_mixture_component_separation: `0.030242`
- test_structured_mae: `0.058453`
- test_structured_rmse: `0.077032`
- test_residual_offset_mean_abs: `0.086328`

## Interpretation

The held-out val error stayed finite with MAE=0.001817 deg and RMSE=0.002610 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002160 deg and RMSE=0.003580 deg, which indicates a numerically stable baseline run.
