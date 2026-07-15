# Wave4 3 Mixture Density K3 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_bw__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k3_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00181385.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.767635`
- val_mae: `0.001814`
- val_rmse: `0.002588`
- val_pointwise_loss: `-1.767635`
- val_centered_curve_shape_loss: `0.004638`
- val_curve_offset_loss: `0.000339`
- val_curve_amplitude_loss: `0.036962`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_mixture_weight_entropy: `0.030901`
- val_mixture_effective_components: `1.032015`
- val_mixture_mean_sigma: `0.177405`
- val_mixture_component_separation: `0.099927`
- val_structured_mae: `0.066157`
- val_structured_rmse: `0.086945`
- val_residual_offset_mean_abs: `0.062349`

## Test Metrics

- test_loss: `-1.697160`
- test_mae: `0.002095`
- test_rmse: `0.003487`
- test_pointwise_loss: `-1.697160`
- test_centered_curve_shape_loss: `0.005785`
- test_curve_offset_loss: `0.002854`
- test_curve_amplitude_loss: `0.045481`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_mixture_weight_entropy: `0.033003`
- test_mixture_effective_components: `1.034198`
- test_mixture_mean_sigma: `0.182990`
- test_mixture_component_separation: `0.099948`
- test_structured_mae: `0.065804`
- test_structured_rmse: `0.086529`
- test_residual_offset_mean_abs: `0.061393`

## Interpretation

The held-out val error stayed finite with MAE=0.001814 deg and RMSE=0.002588 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002095 deg and RMSE=0.003487 deg, which indicates a numerically stable baseline run.
