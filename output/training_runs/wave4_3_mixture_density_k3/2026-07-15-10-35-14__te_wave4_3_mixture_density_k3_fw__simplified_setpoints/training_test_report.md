# Wave4 3 Mixture Density K3 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_fw__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=077-val_mae=0.00357399.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.991212`
- val_mae: `0.003574`
- val_rmse: `0.004417`
- val_pointwise_loss: `-0.991212`
- val_centered_curve_shape_loss: `0.006450`
- val_curve_offset_loss: `0.004296`
- val_curve_amplitude_loss: `0.050635`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_mixture_weight_entropy: `0.026361`
- val_mixture_effective_components: `1.027796`
- val_mixture_mean_sigma: `0.060586`
- val_mixture_component_separation: `0.097912`
- val_structured_mae: `0.064138`
- val_structured_rmse: `0.081965`
- val_residual_offset_mean_abs: `0.078762`

## Test Metrics

- test_loss: `-1.038730`
- test_mae: `0.003333`
- test_rmse: `0.004103`
- test_pointwise_loss: `-1.038730`
- test_centered_curve_shape_loss: `0.003176`
- test_curve_offset_loss: `0.004910`
- test_curve_amplitude_loss: `0.022287`
- test_sparse_harmonic_shape_loss: `6.889912e-05`
- test_mixture_weight_entropy: `0.022097`
- test_mixture_effective_components: `1.023002`
- test_mixture_mean_sigma: `0.052970`
- test_mixture_component_separation: `0.096930`
- test_structured_mae: `0.064675`
- test_structured_rmse: `0.082318`
- test_residual_offset_mean_abs: `0.080341`

## Interpretation

The held-out val error stayed finite with MAE=0.003574 deg and RMSE=0.004417 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003333 deg and RMSE=0.004103 deg, which indicates a numerically stable baseline run.
