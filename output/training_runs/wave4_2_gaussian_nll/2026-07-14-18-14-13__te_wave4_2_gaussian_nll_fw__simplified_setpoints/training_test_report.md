# Wave4 2 Gaussian Nll Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_fw__simplified_setpoints`
- Model Family: `wave4_2_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.09172054.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `54.851116`
- val_mae: `0.091721`
- val_rmse: `0.114133`
- val_pointwise_loss: `54.851116`
- val_centered_curve_shape_loss: `5.006527`
- val_curve_offset_loss: `1.189841`
- val_curve_amplitude_loss: `96.509102`
- val_sparse_harmonic_shape_loss: `0.140681`
- val_interval_coverage: `0.799989`
- val_interval_width: `3.943827`
- val_mean_sigma: `1.538692`
- val_structured_mae: `0.092329`
- val_structured_rmse: `0.115444`
- val_residual_offset_mean_abs: `0.084607`

## Test Metrics

- test_loss: `91.409485`
- test_mae: `0.092190`
- test_rmse: `0.115726`
- test_pointwise_loss: `91.409485`
- test_centered_curve_shape_loss: `4.952099`
- test_curve_offset_loss: `1.322259`
- test_curve_amplitude_loss: `98.113380`
- test_sparse_harmonic_shape_loss: `0.138897`
- test_interval_coverage: `0.802701`
- test_interval_width: `3.791764`
- test_mean_sigma: `1.479364`
- test_structured_mae: `0.092834`
- test_structured_rmse: `0.116423`
- test_residual_offset_mean_abs: `0.084183`

## Interpretation

The held-out val error stayed finite with MAE=0.091721 deg and RMSE=0.114133 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.092190 deg and RMSE=0.115726 deg, which indicates a numerically stable baseline run.
