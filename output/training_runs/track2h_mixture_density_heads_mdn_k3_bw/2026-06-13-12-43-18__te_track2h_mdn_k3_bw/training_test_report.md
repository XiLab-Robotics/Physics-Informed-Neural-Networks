# Track2H Mixture Density Heads Mdn K3 Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k3_bw`
- Model Family: `track2h_mixture_density_heads_mdn_k3_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k3_bw\2026-06-13-12-43-18__te_track2h_mdn_k3_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=166-val_mae=0.00277494.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.621051`
- val_mae: `0.002775`
- val_rmse: `0.003308`
- val_pointwise_loss: `-0.621051`
- val_centered_curve_shape_loss: `0.015850`
- val_curve_offset_loss: `0.011295`
- val_curve_amplitude_loss: `0.069136`
- val_sparse_harmonic_shape_loss: `0.000318`
- val_mixture_weight_entropy: `0.061590`
- val_mixture_effective_components: `1.078573`
- val_mixture_mean_sigma: `0.013125`
- val_mixture_component_separation: `0.035133`
- val_structured_mae: `0.031102`
- val_structured_rmse: `0.042972`
- val_residual_offset_mean_abs: `0.054075`

## Test Metrics

- test_loss: `-0.139613`
- test_mae: `0.002721`
- test_rmse: `0.003250`
- test_pointwise_loss: `-0.139613`
- test_centered_curve_shape_loss: `0.007810`
- test_curve_offset_loss: `0.014765`
- test_curve_amplitude_loss: `0.028437`
- test_sparse_harmonic_shape_loss: `0.000138`
- test_mixture_weight_entropy: `0.032689`
- test_mixture_effective_components: `1.040880`
- test_mixture_mean_sigma: `0.012381`
- test_mixture_component_separation: `0.036078`
- test_structured_mae: `0.030789`
- test_structured_rmse: `0.042334`
- test_residual_offset_mean_abs: `0.058767`

## Interpretation

The held-out val error stayed finite with MAE=0.002775 deg and RMSE=0.003308 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002721 deg and RMSE=0.003250 deg, which indicates a numerically stable baseline run.
