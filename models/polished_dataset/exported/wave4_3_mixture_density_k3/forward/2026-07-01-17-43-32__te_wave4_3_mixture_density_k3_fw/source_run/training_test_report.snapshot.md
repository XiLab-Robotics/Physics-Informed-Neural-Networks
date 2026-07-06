# Wave4 3 Mixture Density K3 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_fw`
- Model Family: `wave4_3_mixture_density_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00150091.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-2.060978`
- val_mae: `0.001501`
- val_rmse: `0.001886`
- val_pointwise_loss: `-2.060978`
- val_centered_curve_shape_loss: `0.003286`
- val_curve_offset_loss: `0.000226`
- val_curve_amplitude_loss: `0.023370`
- val_sparse_harmonic_shape_loss: `6.643296e-05`
- val_mixture_weight_entropy: `0.027000`
- val_mixture_effective_components: `1.032594`
- val_mixture_mean_sigma: `0.010648`
- val_mixture_component_separation: `0.038323`
- val_structured_mae: `0.087522`
- val_structured_rmse: `0.127397`
- val_residual_offset_mean_abs: `0.050623`

## Test Metrics

- test_loss: `-2.004821`
- test_mae: `0.001671`
- test_rmse: `0.002181`
- test_pointwise_loss: `-2.004821`
- test_centered_curve_shape_loss: `0.004282`
- test_curve_offset_loss: `0.000243`
- test_curve_amplitude_loss: `0.026848`
- test_sparse_harmonic_shape_loss: `8.146473e-05`
- test_mixture_weight_entropy: `0.044018`
- test_mixture_effective_components: `1.054659`
- test_mixture_mean_sigma: `0.010633`
- test_mixture_component_separation: `0.037930`
- test_structured_mae: `0.087199`
- test_structured_rmse: `0.126647`
- test_residual_offset_mean_abs: `0.049403`

## Interpretation

The held-out val error stayed finite with MAE=0.001501 deg and RMSE=0.001886 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001671 deg and RMSE=0.002181 deg, which indicates a numerically stable baseline run.
