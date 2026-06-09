# Track2G Curve Aware Harmonic Residual Offset Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_full_curve_composite_global`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global\2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00361589.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.018364`
- val_mae: `0.003616`
- val_rmse: `0.004109`
- val_pointwise_loss: `0.011132`
- val_centered_curve_shape_loss: `0.006579`
- val_curve_offset_loss: `0.004553`
- val_curve_amplitude_loss: `0.039699`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_structured_mae: `0.025450`
- val_structured_rmse: `0.026464`
- val_residual_offset_mean_abs: `0.025341`

## Test Metrics

- test_loss: `0.012621`
- test_mae: `0.003345`
- test_rmse: `0.003713`
- test_pointwise_loss: `0.008121`
- test_centered_curve_shape_loss: `0.003278`
- test_curve_offset_loss: `0.004843`
- test_curve_amplitude_loss: `0.019737`
- test_sparse_harmonic_shape_loss: `7.133408e-05`
- test_structured_mae: `0.028460`
- test_structured_rmse: `0.029296`
- test_residual_offset_mean_abs: `0.028476`

## Interpretation

The held-out val error stayed finite with MAE=0.003616 deg and RMSE=0.004109 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003345 deg and RMSE=0.003713 deg, which indicates a numerically stable baseline run.
