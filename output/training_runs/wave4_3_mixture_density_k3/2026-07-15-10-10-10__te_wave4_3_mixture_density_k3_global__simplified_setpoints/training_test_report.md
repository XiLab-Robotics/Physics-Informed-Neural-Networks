# Wave4 3 Mixture Density K3 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_global__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k3_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-10-10-10__te_wave4_3_mixture_density_k3_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=103-val_mae=0.00358189.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.988099`
- val_mae: `0.003582`
- val_rmse: `0.004453`
- val_pointwise_loss: `-0.988099`
- val_centered_curve_shape_loss: `0.006555`
- val_curve_offset_loss: `0.004423`
- val_curve_amplitude_loss: `0.049853`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_mixture_weight_entropy: `0.019686`
- val_mixture_effective_components: `1.021178`
- val_mixture_mean_sigma: `0.126497`
- val_mixture_component_separation: `0.096684`
- val_structured_mae: `0.065600`
- val_structured_rmse: `0.083906`
- val_residual_offset_mean_abs: `0.086498`

## Test Metrics

- test_loss: `-0.995534`
- test_mae: `0.003460`
- test_rmse: `0.004301`
- test_pointwise_loss: `-0.995534`
- test_centered_curve_shape_loss: `0.003227`
- test_curve_offset_loss: `0.005598`
- test_curve_amplitude_loss: `0.022032`
- test_sparse_harmonic_shape_loss: `7.038318e-05`
- test_mixture_weight_entropy: `0.015033`
- test_mixture_effective_components: `1.015783`
- test_mixture_mean_sigma: `0.130727`
- test_mixture_component_separation: `0.095291`
- test_structured_mae: `0.066200`
- test_structured_rmse: `0.084419`
- test_residual_offset_mean_abs: `0.087957`

## Interpretation

The held-out val error stayed finite with MAE=0.003582 deg and RMSE=0.004453 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003460 deg and RMSE=0.004301 deg, which indicates a numerically stable baseline run.
