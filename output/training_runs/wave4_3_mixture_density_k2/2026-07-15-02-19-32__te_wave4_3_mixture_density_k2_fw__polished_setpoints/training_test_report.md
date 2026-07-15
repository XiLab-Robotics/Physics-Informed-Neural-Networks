# Wave4 3 Mixture Density K2 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00184963.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.665008`
- val_mae: `0.001850`
- val_rmse: `0.002626`
- val_pointwise_loss: `-1.665008`
- val_centered_curve_shape_loss: `0.004657`
- val_curve_offset_loss: `0.000386`
- val_curve_amplitude_loss: `0.035871`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_mixture_weight_entropy: `0.022601`
- val_mixture_effective_components: `1.023510`
- val_mixture_mean_sigma: `0.108853`
- val_mixture_component_separation: `0.044486`
- val_structured_mae: `0.062494`
- val_structured_rmse: `0.081398`
- val_residual_offset_mean_abs: `0.069009`

## Test Metrics

- test_loss: `-1.558616`
- test_mae: `0.002155`
- test_rmse: `0.003552`
- test_pointwise_loss: `-1.558616`
- test_centered_curve_shape_loss: `0.005605`
- test_curve_offset_loss: `0.002980`
- test_curve_amplitude_loss: `0.047076`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_mixture_weight_entropy: `0.025588`
- test_mixture_effective_components: `1.026547`
- test_mixture_mean_sigma: `0.107363`
- test_mixture_component_separation: `0.044113`
- test_structured_mae: `0.061295`
- test_structured_rmse: `0.080224`
- test_residual_offset_mean_abs: `0.067539`

## Interpretation

The held-out val error stayed finite with MAE=0.001850 deg and RMSE=0.002626 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002155 deg and RMSE=0.003552 deg, which indicates a numerically stable baseline run.
