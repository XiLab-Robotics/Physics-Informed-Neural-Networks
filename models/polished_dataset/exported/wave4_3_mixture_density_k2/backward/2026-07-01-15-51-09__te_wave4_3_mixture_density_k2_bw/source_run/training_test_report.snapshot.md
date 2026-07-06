# Wave4 3 Mixture Density K2 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_bw`
- Model Family: `wave4_3_mixture_density_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=133-val_mae=0.00152756.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-2.022157`
- val_mae: `0.001528`
- val_rmse: `0.001909`
- val_pointwise_loss: `-2.022157`
- val_centered_curve_shape_loss: `0.003284`
- val_curve_offset_loss: `0.000267`
- val_curve_amplitude_loss: `0.024777`
- val_sparse_harmonic_shape_loss: `6.585591e-05`
- val_mixture_weight_entropy: `0.046031`
- val_mixture_effective_components: `1.054224`
- val_mixture_mean_sigma: `0.004310`
- val_mixture_component_separation: `0.006524`
- val_structured_mae: `0.062240`
- val_structured_rmse: `0.086573`
- val_residual_offset_mean_abs: `0.040403`

## Test Metrics

- test_loss: `-1.968559`
- test_mae: `0.001725`
- test_rmse: `0.002226`
- test_pointwise_loss: `-1.968559`
- test_centered_curve_shape_loss: `0.004510`
- test_curve_offset_loss: `0.000302`
- test_curve_amplitude_loss: `0.031809`
- test_sparse_harmonic_shape_loss: `8.418670e-05`
- test_mixture_weight_entropy: `0.057647`
- test_mixture_effective_components: `1.067532`
- test_mixture_mean_sigma: `0.004465`
- test_mixture_component_separation: `0.006353`
- test_structured_mae: `0.062075`
- test_structured_rmse: `0.086155`
- test_residual_offset_mean_abs: `0.038814`

## Interpretation

The held-out val error stayed finite with MAE=0.001528 deg and RMSE=0.001909 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001725 deg and RMSE=0.002226 deg, which indicates a numerically stable baseline run.
