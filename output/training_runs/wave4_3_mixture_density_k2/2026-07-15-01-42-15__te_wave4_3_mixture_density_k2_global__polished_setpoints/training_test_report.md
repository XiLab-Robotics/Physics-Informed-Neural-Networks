# Wave4 3 Mixture Density K2 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_3_mixture_density_k2_global__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00186311.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.644341`
- val_mae: `0.001863`
- val_rmse: `0.002665`
- val_pointwise_loss: `-1.644341`
- val_centered_curve_shape_loss: `0.004642`
- val_curve_offset_loss: `0.000521`
- val_curve_amplitude_loss: `0.034633`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_mixture_weight_entropy: `0.025745`
- val_mixture_effective_components: `1.026753`
- val_mixture_mean_sigma: `0.099415`
- val_mixture_component_separation: `0.047569`
- val_structured_mae: `0.062399`
- val_structured_rmse: `0.083942`
- val_residual_offset_mean_abs: `0.065934`

## Test Metrics

- test_loss: `-1.531777`
- test_mae: `0.002221`
- test_rmse: `0.003626`
- test_pointwise_loss: `-1.531777`
- test_centered_curve_shape_loss: `0.005534`
- test_curve_offset_loss: `0.003269`
- test_curve_amplitude_loss: `0.045351`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_mixture_weight_entropy: `0.028693`
- test_mixture_effective_components: `1.029720`
- test_mixture_mean_sigma: `0.099995`
- test_mixture_component_separation: `0.046261`
- test_structured_mae: `0.061002`
- test_structured_rmse: `0.082287`
- test_residual_offset_mean_abs: `0.064721`

## Interpretation

The held-out val error stayed finite with MAE=0.001863 deg and RMSE=0.002665 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002221 deg and RMSE=0.003626 deg, which indicates a numerically stable baseline run.
