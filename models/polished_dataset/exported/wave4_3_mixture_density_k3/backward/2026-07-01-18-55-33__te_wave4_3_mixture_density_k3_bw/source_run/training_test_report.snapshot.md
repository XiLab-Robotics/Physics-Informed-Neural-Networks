# Wave4 3 Mixture Density K3 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_bw`
- Model Family: `wave4_3_mixture_density_k3_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=150-val_mae=0.00151947.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-2.030062`
- val_mae: `0.001519`
- val_rmse: `0.001904`
- val_pointwise_loss: `-2.030062`
- val_centered_curve_shape_loss: `0.003291`
- val_curve_offset_loss: `0.000249`
- val_curve_amplitude_loss: `0.024431`
- val_sparse_harmonic_shape_loss: `6.621720e-05`
- val_mixture_weight_entropy: `0.033658`
- val_mixture_effective_components: `1.038359`
- val_mixture_mean_sigma: `0.022398`
- val_mixture_component_separation: `0.041248`
- val_structured_mae: `0.073583`
- val_structured_rmse: `0.104649`
- val_residual_offset_mean_abs: `0.063228`

## Test Metrics

- test_loss: `-1.985637`
- test_mae: `0.001704`
- test_rmse: `0.002205`
- test_pointwise_loss: `-1.985637`
- test_centered_curve_shape_loss: `0.004335`
- test_curve_offset_loss: `0.000303`
- test_curve_amplitude_loss: `0.028592`
- test_sparse_harmonic_shape_loss: `8.269564e-05`
- test_mixture_weight_entropy: `0.046152`
- test_mixture_effective_components: `1.054338`
- test_mixture_mean_sigma: `0.021516`
- test_mixture_component_separation: `0.040160`
- test_structured_mae: `0.073926`
- test_structured_rmse: `0.105082`
- test_residual_offset_mean_abs: `0.061191`

## Interpretation

The held-out val error stayed finite with MAE=0.001519 deg and RMSE=0.001904 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001704 deg and RMSE=0.002205 deg, which indicates a numerically stable baseline run.
