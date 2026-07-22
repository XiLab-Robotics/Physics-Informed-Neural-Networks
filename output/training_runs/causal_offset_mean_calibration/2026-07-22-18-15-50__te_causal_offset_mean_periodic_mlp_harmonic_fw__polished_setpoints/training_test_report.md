# Causal Offset Mean Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `causal_offset_mean_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=020-val_mae=0.00146895.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015965`
- val_mae: `0.001469`
- val_rmse: `0.001901`
- val_pointwise_loss: `0.008758`
- val_centered_curve_shape_loss: `0.007616`
- val_curve_offset_loss: `0.002398`
- val_curve_amplitude_loss: `0.098801`
- val_sparse_harmonic_shape_loss: `0.000134`

## Test Metrics

- test_loss: `0.011486`
- test_mae: `0.001277`
- test_rmse: `0.001739`
- test_pointwise_loss: `0.006205`
- test_centered_curve_shape_loss: `0.005440`
- test_curve_offset_loss: `0.002524`
- test_curve_amplitude_loss: `0.070889`
- test_sparse_harmonic_shape_loss: `9.364144e-05`

## Interpretation

The held-out val error stayed finite with MAE=0.001469 deg and RMSE=0.001901 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001277 deg and RMSE=0.001739 deg, which indicates a numerically stable baseline run.
