# Track2H Dispersion Aware Mae Robust Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_mae_robust_fw`
- Model Family: `track2h_dispersion_aware_mae_robust_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_fw\2026-06-11-12-07-43__te_track2h_mae_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=012-val_mae=0.00325839.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.137858`
- val_mae: `0.003258`
- val_rmse: `0.003757`
- val_pointwise_loss: `0.137858`
- val_centered_curve_shape_loss: `0.015476`
- val_curve_offset_loss: `0.016588`
- val_curve_amplitude_loss: `0.099315`
- val_sparse_harmonic_shape_loss: `0.000339`
- val_structured_mae: `0.019903`
- val_structured_rmse: `0.021854`
- val_residual_offset_mean_abs: `0.019567`

## Test Metrics

- test_loss: `0.133085`
- test_mae: `0.003146`
- test_rmse: `0.003527`
- test_pointwise_loss: `0.133085`
- test_centered_curve_shape_loss: `0.007740`
- test_curve_offset_loss: `0.018586`
- test_curve_amplitude_loss: `0.045415`
- test_sparse_harmonic_shape_loss: `0.000144`
- test_structured_mae: `0.022560`
- test_structured_rmse: `0.024634`
- test_residual_offset_mean_abs: `0.022771`

## Interpretation

The held-out val error stayed finite with MAE=0.003258 deg and RMSE=0.003757 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003146 deg and RMSE=0.003527 deg, which indicates a numerically stable baseline run.
