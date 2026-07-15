# Wave4 3 Mixture Density K3 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_global__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k3_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=177-val_mae=0.00183826.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.785186`
- val_mae: `0.001838`
- val_rmse: `0.002622`
- val_pointwise_loss: `-1.785186`
- val_centered_curve_shape_loss: `0.004658`
- val_curve_offset_loss: `0.000447`
- val_curve_amplitude_loss: `0.035695`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_mixture_weight_entropy: `0.017305`
- val_mixture_effective_components: `1.020533`
- val_mixture_mean_sigma: `0.093285`
- val_mixture_component_separation: `0.094621`
- val_structured_mae: `0.064591`
- val_structured_rmse: `0.084109`
- val_residual_offset_mean_abs: `0.086938`

## Test Metrics

- test_loss: `-1.676559`
- test_mae: `0.002163`
- test_rmse: `0.003572`
- test_pointwise_loss: `-1.676559`
- test_centered_curve_shape_loss: `0.005650`
- test_curve_offset_loss: `0.002747`
- test_curve_amplitude_loss: `0.046453`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_mixture_weight_entropy: `0.027793`
- test_mixture_effective_components: `1.033875`
- test_mixture_mean_sigma: `0.091890`
- test_mixture_component_separation: `0.093823`
- test_structured_mae: `0.064280`
- test_structured_rmse: `0.083857`
- test_residual_offset_mean_abs: `0.083653`

## Interpretation

The held-out val error stayed finite with MAE=0.001838 deg and RMSE=0.002622 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002163 deg and RMSE=0.003572 deg, which indicates a numerically stable baseline run.
