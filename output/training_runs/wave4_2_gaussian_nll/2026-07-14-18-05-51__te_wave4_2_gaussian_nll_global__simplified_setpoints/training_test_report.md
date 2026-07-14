# Wave4 2 Gaussian Nll Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_global__simplified_setpoints`
- Model Family: `wave4_2_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-05-51__te_wave4_2_gaussian_nll_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.11074460.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `107.040710`
- val_mae: `0.110745`
- val_rmse: `0.137478`
- val_pointwise_loss: `107.040710`
- val_centered_curve_shape_loss: `5.373864`
- val_curve_offset_loss: `3.435965`
- val_curve_amplitude_loss: `115.695648`
- val_sparse_harmonic_shape_loss: `0.150493`
- val_interval_coverage: `0.867161`
- val_interval_width: `6.003653`
- val_mean_sigma: `2.342338`
- val_structured_mae: `0.099853`
- val_structured_rmse: `0.123930`
- val_residual_offset_mean_abs: `0.120896`

## Test Metrics

- test_loss: `159.881638`
- test_mae: `0.109411`
- test_rmse: `0.135984`
- test_pointwise_loss: `159.881638`
- test_centered_curve_shape_loss: `4.977563`
- test_curve_offset_loss: `3.593695`
- test_curve_amplitude_loss: `106.896538`
- test_sparse_harmonic_shape_loss: `0.139443`
- test_interval_coverage: `0.874302`
- test_interval_width: `6.178451`
- test_mean_sigma: `2.410536`
- test_structured_mae: `0.099380`
- test_structured_rmse: `0.123230`
- test_residual_offset_mean_abs: `0.121657`

## Interpretation

The held-out val error stayed finite with MAE=0.110745 deg and RMSE=0.137478 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.109411 deg and RMSE=0.135984 deg, which indicates a numerically stable baseline run.
