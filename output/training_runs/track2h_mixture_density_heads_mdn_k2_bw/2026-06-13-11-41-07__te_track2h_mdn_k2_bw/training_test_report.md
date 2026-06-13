# Track2H Mixture Density Heads Mdn K2 Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k2_bw`
- Model Family: `track2h_mixture_density_heads_mdn_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k2_bw\2026-06-13-11-41-07__te_track2h_mdn_k2_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=236-val_mae=0.00291440.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.161834`
- val_mae: `0.002914`
- val_rmse: `0.003465`
- val_pointwise_loss: `-0.161834`
- val_centered_curve_shape_loss: `0.016528`
- val_curve_offset_loss: `0.012582`
- val_curve_amplitude_loss: `0.061737`
- val_sparse_harmonic_shape_loss: `0.000335`
- val_mixture_weight_entropy: `0.049039`
- val_mixture_effective_components: `1.061455`
- val_mixture_mean_sigma: `0.005778`
- val_mixture_component_separation: `0.013067`
- val_structured_mae: `0.030098`
- val_structured_rmse: `0.043597`
- val_residual_offset_mean_abs: `0.036672`

## Test Metrics

- test_loss: `-0.246045`
- test_mae: `0.002658`
- test_rmse: `0.003198`
- test_pointwise_loss: `-0.246045`
- test_centered_curve_shape_loss: `0.008120`
- test_curve_offset_loss: `0.013678`
- test_curve_amplitude_loss: `0.022596`
- test_sparse_harmonic_shape_loss: `0.000146`
- test_mixture_weight_entropy: `0.032067`
- test_mixture_effective_components: `1.040371`
- test_mixture_mean_sigma: `0.005300`
- test_mixture_component_separation: `0.012931`
- test_structured_mae: `0.030378`
- test_structured_rmse: `0.043304`
- test_residual_offset_mean_abs: `0.037627`

## Interpretation

The held-out val error stayed finite with MAE=0.002914 deg and RMSE=0.003465 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002658 deg and RMSE=0.003198 deg, which indicates a numerically stable baseline run.
