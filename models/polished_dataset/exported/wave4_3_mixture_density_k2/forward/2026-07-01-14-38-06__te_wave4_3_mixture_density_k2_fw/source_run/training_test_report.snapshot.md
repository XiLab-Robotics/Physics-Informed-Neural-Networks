# Wave4 3 Mixture Density K2 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_fw`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=255-val_mae=0.00149336.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-2.055228`
- val_mae: `0.001493`
- val_rmse: `0.001880`
- val_pointwise_loss: `-2.055228`
- val_centered_curve_shape_loss: `0.003201`
- val_curve_offset_loss: `0.000201`
- val_curve_amplitude_loss: `0.021287`
- val_sparse_harmonic_shape_loss: `6.318298e-05`
- val_mixture_weight_entropy: `0.027704`
- val_mixture_effective_components: `1.033051`
- val_mixture_mean_sigma: `0.003652`
- val_mixture_component_separation: `0.006828`
- val_structured_mae: `0.071445`
- val_structured_rmse: `0.100771`
- val_residual_offset_mean_abs: `0.048495`

## Test Metrics

- test_loss: `-1.967681`
- test_mae: `0.001698`
- test_rmse: `0.002196`
- test_pointwise_loss: `-1.967681`
- test_centered_curve_shape_loss: `0.004260`
- test_curve_offset_loss: `0.000262`
- test_curve_amplitude_loss: `0.026401`
- test_sparse_harmonic_shape_loss: `7.996053e-05`
- test_mixture_weight_entropy: `0.039398`
- test_mixture_effective_components: `1.048125`
- test_mixture_mean_sigma: `0.003881`
- test_mixture_component_separation: `0.006570`
- test_structured_mae: `0.071498`
- test_structured_rmse: `0.100964`
- test_residual_offset_mean_abs: `0.047772`

## Interpretation

The held-out val error stayed finite with MAE=0.001493 deg and RMSE=0.001880 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001698 deg and RMSE=0.002196 deg, which indicates a numerically stable baseline run.
