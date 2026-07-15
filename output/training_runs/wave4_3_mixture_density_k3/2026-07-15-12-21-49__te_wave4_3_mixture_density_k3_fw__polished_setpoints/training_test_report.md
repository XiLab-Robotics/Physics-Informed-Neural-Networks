# Wave4 3 Mixture Density K3 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k3_fw__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=140-val_mae=0.00184649.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.669362`
- val_mae: `0.001846`
- val_rmse: `0.002644`
- val_pointwise_loss: `-1.669362`
- val_centered_curve_shape_loss: `0.004661`
- val_curve_offset_loss: `0.000454`
- val_curve_amplitude_loss: `0.036526`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_mixture_weight_entropy: `0.029806`
- val_mixture_effective_components: `1.031675`
- val_mixture_mean_sigma: `0.064250`
- val_mixture_component_separation: `0.090876`
- val_structured_mae: `0.066584`
- val_structured_rmse: `0.084631`
- val_residual_offset_mean_abs: `0.081298`

## Test Metrics

- test_loss: `-1.580816`
- test_mae: `0.002151`
- test_rmse: `0.003566`
- test_pointwise_loss: `-1.580816`
- test_centered_curve_shape_loss: `0.005603`
- test_curve_offset_loss: `0.002933`
- test_curve_amplitude_loss: `0.047701`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_mixture_weight_entropy: `0.040872`
- test_mixture_effective_components: `1.044343`
- test_mixture_mean_sigma: `0.062935`
- test_mixture_component_separation: `0.088846`
- test_structured_mae: `0.065273`
- test_structured_rmse: `0.083448`
- test_residual_offset_mean_abs: `0.079591`

## Interpretation

The held-out val error stayed finite with MAE=0.001846 deg and RMSE=0.002644 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002151 deg and RMSE=0.003566 deg, which indicates a numerically stable baseline run.
