# Track2H Mixture Density Heads Mdn K3 Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k3_fw`
- Model Family: `track2h_mixture_density_heads_mdn_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k3_fw\2026-06-13-12-34-37__te_track2h_mdn_k3_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=014-val_mae=0.00325279.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.402530`
- val_mae: `0.003253`
- val_rmse: `0.003740`
- val_pointwise_loss: `-0.402530`
- val_centered_curve_shape_loss: `0.014871`
- val_curve_offset_loss: `0.015770`
- val_curve_amplitude_loss: `0.091060`
- val_sparse_harmonic_shape_loss: `0.000322`
- val_mixture_weight_entropy: `0.019226`
- val_mixture_effective_components: `1.019656`
- val_mixture_mean_sigma: `0.036360`
- val_mixture_component_separation: `0.048765`
- val_structured_mae: `0.029559`
- val_structured_rmse: `0.038711`
- val_residual_offset_mean_abs: `0.039495`

## Test Metrics

- test_loss: `-0.420259`
- test_mae: `0.003235`
- test_rmse: `0.003613`
- test_pointwise_loss: `-0.420259`
- test_centered_curve_shape_loss: `0.007695`
- test_curve_offset_loss: `0.018618`
- test_curve_amplitude_loss: `0.040391`
- test_sparse_harmonic_shape_loss: `0.000142`
- test_mixture_weight_entropy: `0.018505`
- test_mixture_effective_components: `1.018868`
- test_mixture_mean_sigma: `0.030782`
- test_mixture_component_separation: `0.048651`
- test_structured_mae: `0.029761`
- test_structured_rmse: `0.039076`
- test_residual_offset_mean_abs: `0.039050`

## Interpretation

The held-out val error stayed finite with MAE=0.003253 deg and RMSE=0.003740 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003235 deg and RMSE=0.003613 deg, which indicates a numerically stable baseline run.
