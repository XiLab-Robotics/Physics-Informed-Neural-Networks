# Wave4 2 Gaussian Nll Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_fw__polished_setpoints`
- Model Family: `wave4_2_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=001-val_mae=0.08819758.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `18.869482`
- val_mae: `0.088198`
- val_rmse: `0.110128`
- val_pointwise_loss: `18.869482`
- val_centered_curve_shape_loss: `4.917747`
- val_curve_offset_loss: `0.814578`
- val_curve_amplitude_loss: `107.441437`
- val_sparse_harmonic_shape_loss: `0.138091`
- val_interval_coverage: `0.878651`
- val_interval_width: `5.395155`
- val_mean_sigma: `2.104931`
- val_structured_mae: `0.089818`
- val_structured_rmse: `0.111867`
- val_residual_offset_mean_abs: `0.079136`

## Test Metrics

- test_loss: `19.925508`
- test_mae: `0.087134`
- test_rmse: `0.109389`
- test_pointwise_loss: `19.925508`
- test_centered_curve_shape_loss: `4.873450`
- test_curve_offset_loss: `0.716126`
- test_curve_amplitude_loss: `106.200020`
- test_sparse_harmonic_shape_loss: `0.136852`
- test_interval_coverage: `0.889202`
- test_interval_width: `5.502139`
- test_mean_sigma: `2.146671`
- test_structured_mae: `0.088407`
- test_structured_rmse: `0.110586`
- test_residual_offset_mean_abs: `0.081405`

## Interpretation

The held-out val error stayed finite with MAE=0.088198 deg and RMSE=0.110128 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.087134 deg and RMSE=0.109389 deg, which indicates a numerically stable baseline run.
