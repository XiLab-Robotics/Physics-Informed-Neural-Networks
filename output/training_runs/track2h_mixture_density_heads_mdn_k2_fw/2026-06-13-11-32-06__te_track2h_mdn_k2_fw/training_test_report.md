# Track2H Mixture Density Heads Mdn K2 Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k2_fw`
- Model Family: `track2h_mixture_density_heads_mdn_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k2_fw\2026-06-13-11-32-06__te_track2h_mdn_k2_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=017-val_mae=0.00328504.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.294832`
- val_mae: `0.003285`
- val_rmse: `0.003799`
- val_pointwise_loss: `-0.294832`
- val_centered_curve_shape_loss: `0.015262`
- val_curve_offset_loss: `0.017112`
- val_curve_amplitude_loss: `0.103274`
- val_sparse_harmonic_shape_loss: `0.000331`
- val_mixture_weight_entropy: `0.026796`
- val_mixture_effective_components: `1.027505`
- val_mixture_mean_sigma: `0.182282`
- val_mixture_component_separation: `0.040015`
- val_structured_mae: `0.034511`
- val_structured_rmse: `0.044957`
- val_residual_offset_mean_abs: `0.031286`

## Test Metrics

- test_loss: `-0.322628`
- test_mae: `0.003339`
- test_rmse: `0.003721`
- test_pointwise_loss: `-0.322628`
- test_centered_curve_shape_loss: `0.007866`
- test_curve_offset_loss: `0.020561`
- test_curve_amplitude_loss: `0.046555`
- test_sparse_harmonic_shape_loss: `0.000145`
- test_mixture_weight_entropy: `0.024810`
- test_mixture_effective_components: `1.025501`
- test_mixture_mean_sigma: `0.140972`
- test_mixture_component_separation: `0.039158`
- test_structured_mae: `0.033704`
- test_structured_rmse: `0.044468`
- test_residual_offset_mean_abs: `0.032396`

## Interpretation

The held-out val error stayed finite with MAE=0.003285 deg and RMSE=0.003799 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003339 deg and RMSE=0.003721 deg, which indicates a numerically stable baseline run.
