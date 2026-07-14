# Wave4 3 Mixture Density K2 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_bw__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=185-val_mae=0.00360751.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.942279`
- val_mae: `0.003608`
- val_rmse: `0.004443`
- val_pointwise_loss: `-0.942279`
- val_centered_curve_shape_loss: `0.006510`
- val_curve_offset_loss: `0.004450`
- val_curve_amplitude_loss: `0.047351`
- val_sparse_harmonic_shape_loss: `0.000155`
- val_mixture_weight_entropy: `0.042542`
- val_mixture_effective_components: `1.045813`
- val_mixture_mean_sigma: `0.035517`
- val_mixture_component_separation: `0.024074`
- val_structured_mae: `0.060205`
- val_structured_rmse: `0.076232`
- val_residual_offset_mean_abs: `0.066492`

## Test Metrics

- test_loss: `-0.987315`
- test_mae: `0.003481`
- test_rmse: `0.004230`
- test_pointwise_loss: `-0.987315`
- test_centered_curve_shape_loss: `0.003215`
- test_curve_offset_loss: `0.005358`
- test_curve_amplitude_loss: `0.020056`
- test_sparse_harmonic_shape_loss: `6.984024e-05`
- test_mixture_weight_entropy: `0.036917`
- test_mixture_effective_components: `1.038600`
- test_mixture_mean_sigma: `0.035421`
- test_mixture_component_separation: `0.022760`
- test_structured_mae: `0.060780`
- test_structured_rmse: `0.076685`
- test_residual_offset_mean_abs: `0.067279`

## Interpretation

The held-out val error stayed finite with MAE=0.003608 deg and RMSE=0.004443 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003481 deg and RMSE=0.004230 deg, which indicates a numerically stable baseline run.
