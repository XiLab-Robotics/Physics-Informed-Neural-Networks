# Track2G Curve Aware Harmonic Residual Offset Full Curve Composite Bw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_full_curve_composite_bw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw\2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00380311.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.068685`
- val_mae: `0.003803`
- val_rmse: `0.004454`
- val_pointwise_loss: `0.044555`
- val_centered_curve_shape_loss: `0.029904`
- val_curve_offset_loss: `0.014650`
- val_curve_amplitude_loss: `0.114174`
- val_sparse_harmonic_shape_loss: `0.000726`
- val_structured_mae: `0.013912`
- val_structured_rmse: `0.015745`
- val_residual_offset_mean_abs: `0.013752`

## Test Metrics

- test_loss: `0.046969`
- test_mae: `0.003511`
- test_rmse: `0.004113`
- test_pointwise_loss: `0.032110`
- test_centered_curve_shape_loss: `0.015261`
- test_curve_offset_loss: `0.016850`
- test_curve_amplitude_loss: `0.050938`
- test_sparse_harmonic_shape_loss: `0.000351`
- test_structured_mae: `0.015842`
- test_structured_rmse: `0.017566`
- test_residual_offset_mean_abs: `0.015543`

## Interpretation

The held-out val error stayed finite with MAE=0.003803 deg and RMSE=0.004454 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003511 deg and RMSE=0.004113 deg, which indicates a numerically stable baseline run.
