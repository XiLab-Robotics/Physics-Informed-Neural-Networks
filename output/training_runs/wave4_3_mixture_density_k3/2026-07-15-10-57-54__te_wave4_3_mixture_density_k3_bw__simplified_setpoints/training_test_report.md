# Wave4 3 Mixture Density K3 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_bw__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k3_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-10-57-54__te_wave4_3_mixture_density_k3_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=083-val_mae=0.00361315.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.959602`
- val_mae: `0.003613`
- val_rmse: `0.004501`
- val_pointwise_loss: `-0.959602`
- val_centered_curve_shape_loss: `0.006637`
- val_curve_offset_loss: `0.004562`
- val_curve_amplitude_loss: `0.048047`
- val_sparse_harmonic_shape_loss: `0.000157`
- val_mixture_weight_entropy: `0.023102`
- val_mixture_effective_components: `1.023950`
- val_mixture_mean_sigma: `0.365054`
- val_mixture_component_separation: `0.136767`
- val_structured_mae: `0.075346`
- val_structured_rmse: `0.096067`
- val_residual_offset_mean_abs: `0.066368`

## Test Metrics

- test_loss: `-0.996771`
- test_mae: `0.003521`
- test_rmse: `0.004291`
- test_pointwise_loss: `-0.996771`
- test_centered_curve_shape_loss: `0.003345`
- test_curve_offset_loss: `0.005455`
- test_curve_amplitude_loss: `0.021870`
- test_sparse_harmonic_shape_loss: `7.222650e-05`
- test_mixture_weight_entropy: `0.022596`
- test_mixture_effective_components: `1.023316`
- test_mixture_mean_sigma: `0.320975`
- test_mixture_component_separation: `0.133845`
- test_structured_mae: `0.074081`
- test_structured_rmse: `0.094448`
- test_residual_offset_mean_abs: `0.068324`

## Interpretation

The held-out val error stayed finite with MAE=0.003613 deg and RMSE=0.004501 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003521 deg and RMSE=0.004291 deg, which indicates a numerically stable baseline run.
