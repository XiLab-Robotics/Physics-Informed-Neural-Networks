# Track2H Mixture Density Heads Mdn K3 Global Training And Testing Report

## Overview

- Run Name: `te_track2h_mdn_k3_global`
- Model Family: `track2h_mixture_density_heads_mdn_k3_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_mixture_density_heads_mdn_k3_global\2026-06-13-12-14-13__te_track2h_mdn_k3_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=034-val_mae=0.00361697.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.930578`
- val_mae: `0.003617`
- val_rmse: `0.004152`
- val_pointwise_loss: `-0.930578`
- val_centered_curve_shape_loss: `0.006524`
- val_curve_offset_loss: `0.004933`
- val_curve_amplitude_loss: `0.053833`
- val_sparse_harmonic_shape_loss: `0.000155`
- val_mixture_weight_entropy: `0.013205`
- val_mixture_effective_components: `1.013736`
- val_mixture_mean_sigma: `0.079638`
- val_mixture_component_separation: `0.110375`
- val_structured_mae: `0.061553`
- val_structured_rmse: `0.078026`
- val_residual_offset_mean_abs: `0.078678`

## Test Metrics

- test_loss: `-0.929006`
- test_mae: `0.003564`
- test_rmse: `0.003986`
- test_pointwise_loss: `-0.929006`
- test_centered_curve_shape_loss: `0.003252`
- test_curve_offset_loss: `0.005988`
- test_curve_amplitude_loss: `0.025155`
- test_sparse_harmonic_shape_loss: `7.075611e-05`
- test_mixture_weight_entropy: `0.012118`
- test_mixture_effective_components: `1.012586`
- test_mixture_mean_sigma: `0.080886`
- test_mixture_component_separation: `0.107899`
- test_structured_mae: `0.062201`
- test_structured_rmse: `0.078239`
- test_residual_offset_mean_abs: `0.079398`

## Interpretation

The held-out val error stayed finite with MAE=0.003617 deg and RMSE=0.004152 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003564 deg and RMSE=0.003986 deg, which indicates a numerically stable baseline run.
