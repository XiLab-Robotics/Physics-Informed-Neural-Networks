# Wave4 3 Mixture Density K2 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_fw__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=258-val_mae=0.00346706.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.050154`
- val_mae: `0.003467`
- val_rmse: `0.004380`
- val_pointwise_loss: `-1.050154`
- val_centered_curve_shape_loss: `0.006467`
- val_curve_offset_loss: `0.004354`
- val_curve_amplitude_loss: `0.050632`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_mixture_weight_entropy: `0.021496`
- val_mixture_effective_components: `1.024452`
- val_mixture_mean_sigma: `0.020898`
- val_mixture_component_separation: `0.031523`
- val_structured_mae: `0.064652`
- val_structured_rmse: `0.083440`
- val_residual_offset_mean_abs: `0.075704`

## Test Metrics

- test_loss: `-1.089095`
- test_mae: `0.003283`
- test_rmse: `0.004147`
- test_pointwise_loss: `-1.089095`
- test_centered_curve_shape_loss: `0.003241`
- test_curve_offset_loss: `0.005127`
- test_curve_amplitude_loss: `0.022582`
- test_sparse_harmonic_shape_loss: `7.042580e-05`
- test_mixture_weight_entropy: `0.014005`
- test_mixture_effective_components: `1.016785`
- test_mixture_mean_sigma: `0.018888`
- test_mixture_component_separation: `0.030749`
- test_structured_mae: `0.064322`
- test_structured_rmse: `0.081963`
- test_residual_offset_mean_abs: `0.082902`

## Interpretation

The held-out val error stayed finite with MAE=0.003467 deg and RMSE=0.004380 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003283 deg and RMSE=0.004147 deg, which indicates a numerically stable baseline run.
