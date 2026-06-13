# Track2H Mixture Density Heads Mdn K2 Global Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k2_global`
- Model Family: `track2h_mixture_density_heads_mdn_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k2_global\2026-06-13-11-11-47__te_track2h_mdn_k2_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=034-val_mae=0.00365445.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.916920`
- val_mae: `0.003654`
- val_rmse: `0.004191`
- val_pointwise_loss: `-0.916920`
- val_centered_curve_shape_loss: `0.006713`
- val_curve_offset_loss: `0.004738`
- val_curve_amplitude_loss: `0.048180`
- val_sparse_harmonic_shape_loss: `0.000161`
- val_mixture_weight_entropy: `0.018659`
- val_mixture_effective_components: `1.019340`
- val_mixture_mean_sigma: `0.169468`
- val_mixture_component_separation: `0.060747`
- val_structured_mae: `0.059258`
- val_structured_rmse: `0.076825`
- val_residual_offset_mean_abs: `0.068559`

## Test Metrics

- test_loss: `-0.947190`
- test_mae: `0.003503`
- test_rmse: `0.003938`
- test_pointwise_loss: `-0.947190`
- test_centered_curve_shape_loss: `0.003400`
- test_curve_offset_loss: `0.005567`
- test_curve_amplitude_loss: `0.021626`
- test_sparse_harmonic_shape_loss: `7.517853e-05`
- test_mixture_weight_entropy: `0.015906`
- test_mixture_effective_components: `1.016360`
- test_mixture_mean_sigma: `0.135948`
- test_mixture_component_separation: `0.059065`
- test_structured_mae: `0.060972`
- test_structured_rmse: `0.078114`
- test_residual_offset_mean_abs: `0.068947`

## Interpretation

The held-out val error stayed finite with MAE=0.003654 deg and RMSE=0.004191 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003503 deg and RMSE=0.003938 deg, which indicates a numerically stable baseline run.
