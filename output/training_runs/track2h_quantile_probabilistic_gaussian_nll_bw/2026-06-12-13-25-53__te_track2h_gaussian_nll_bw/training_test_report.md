# Track2H Quantile Probabilistic Gaussian Nll Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_gaussian_nll_bw`
- Model Family: `track2h_quantile_probabilistic_gaussian_nll_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_bw\2026-06-12-13-25-53__te_track2h_gaussian_nll_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=180-val_mae=0.00329833.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.429147`
- val_mae: `0.003298`
- val_rmse: `0.003914`
- val_pointwise_loss: `-0.429147`
- val_centered_curve_shape_loss: `0.030520`
- val_curve_offset_loss: `0.011234`
- val_curve_amplitude_loss: `0.249691`
- val_sparse_harmonic_shape_loss: `0.000746`
- val_interval_coverage: `0.804365`
- val_interval_width: `0.011019`
- val_mean_sigma: `0.004299`
- val_structured_mae: `0.011947`
- val_structured_rmse: `0.016469`
- val_residual_offset_mean_abs: `0.023138`

## Test Metrics

- test_loss: `-0.515429`
- test_mae: `0.002998`
- test_rmse: `0.003608`
- test_pointwise_loss: `-0.515429`
- test_centered_curve_shape_loss: `0.014507`
- test_curve_offset_loss: `0.014085`
- test_curve_amplitude_loss: `0.105102`
- test_sparse_harmonic_shape_loss: `0.000331`
- test_interval_coverage: `0.757839`
- test_interval_width: `0.008887`
- test_mean_sigma: `0.003467`
- test_structured_mae: `0.011697`
- test_structured_rmse: `0.016532`
- test_residual_offset_mean_abs: `0.024631`

## Interpretation

The held-out val error stayed finite with MAE=0.003298 deg and RMSE=0.003914 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002998 deg and RMSE=0.003608 deg, which indicates a numerically stable baseline run.
