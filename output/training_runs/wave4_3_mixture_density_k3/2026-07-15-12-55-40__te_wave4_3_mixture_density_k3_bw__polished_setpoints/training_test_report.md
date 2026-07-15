# Wave4 3 Mixture Density K3 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_bw__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k3_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=166-val_mae=0.00183407.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.731690`
- val_mae: `0.001834`
- val_rmse: `0.002631`
- val_pointwise_loss: `-1.731690`
- val_centered_curve_shape_loss: `0.004608`
- val_curve_offset_loss: `0.000478`
- val_curve_amplitude_loss: `0.035651`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_mixture_weight_entropy: `0.024070`
- val_mixture_effective_components: `1.028319`
- val_mixture_mean_sigma: `0.055522`
- val_mixture_component_separation: `0.073921`
- val_structured_mae: `0.058182`
- val_structured_rmse: `0.075020`
- val_residual_offset_mean_abs: `0.091757`

## Test Metrics

- test_loss: `-1.645552`
- test_mae: `0.002176`
- test_rmse: `0.003600`
- test_pointwise_loss: `-1.645552`
- test_centered_curve_shape_loss: `0.005504`
- test_curve_offset_loss: `0.003106`
- test_curve_amplitude_loss: `0.045296`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_mixture_weight_entropy: `0.040323`
- test_mixture_effective_components: `1.048801`
- test_mixture_mean_sigma: `0.053673`
- test_mixture_component_separation: `0.074025`
- test_structured_mae: `0.057195`
- test_structured_rmse: `0.074043`
- test_residual_offset_mean_abs: `0.089027`

## Interpretation

The held-out val error stayed finite with MAE=0.001834 deg and RMSE=0.002631 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002176 deg and RMSE=0.003600 deg, which indicates a numerically stable baseline run.
