# Wave4 3 Mixture Density K2 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=237-val_mae=0.00346790.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.061914`
- val_mae: `0.003468`
- val_rmse: `0.004355`
- val_pointwise_loss: `-1.061914`
- val_centered_curve_shape_loss: `0.006561`
- val_curve_offset_loss: `0.004264`
- val_curve_amplitude_loss: `0.051623`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_mixture_weight_entropy: `0.011978`
- val_mixture_effective_components: `1.013829`
- val_mixture_mean_sigma: `0.070007`
- val_mixture_component_separation: `0.059172`
- val_structured_mae: `0.065999`
- val_structured_rmse: `0.085012`
- val_residual_offset_mean_abs: `0.079069`

## Test Metrics

- test_loss: `-1.073983`
- test_mae: `0.003256`
- test_rmse: `0.004035`
- test_pointwise_loss: `-1.073983`
- test_centered_curve_shape_loss: `0.003248`
- test_curve_offset_loss: `0.004679`
- test_curve_amplitude_loss: `0.022598`
- test_sparse_harmonic_shape_loss: `7.064031e-05`
- test_mixture_weight_entropy: `0.008705`
- test_mixture_effective_components: `1.009544`
- test_mixture_mean_sigma: `0.049128`
- test_mixture_component_separation: `0.056619`
- test_structured_mae: `0.066400`
- test_structured_rmse: `0.085058`
- test_residual_offset_mean_abs: `0.080842`

## Interpretation

The held-out val error stayed finite with MAE=0.003468 deg and RMSE=0.004355 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003256 deg and RMSE=0.004035 deg, which indicates a numerically stable baseline run.
