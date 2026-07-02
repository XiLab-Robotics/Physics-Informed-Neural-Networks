# Wave52B Offset Harmonic Guided Offset Centered Shape Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw\2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=082-val_mae=0.00231961.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.047446`
- val_mae: `0.002320`
- val_rmse: `0.002848`
- val_pointwise_loss: `0.031496`
- val_centered_curve_shape_loss: `0.030386`
- val_curve_offset_loss: `0.001110`
- val_curve_amplitude_loss: `0.192667`
- val_sparse_harmonic_shape_loss: `0.000737`
- val_structured_mae: `0.003750`
- val_structured_rmse: `0.004385`
- val_base_mae: `0.019651`
- val_base_rmse: `0.023090`
- val_residual_offset_mean_abs: `0.001538`

## Test Metrics

- test_loss: `0.022929`
- test_mae: `0.001677`
- test_rmse: `0.002151`
- test_pointwise_loss: `0.015762`
- test_centered_curve_shape_loss: `0.014802`
- test_curve_offset_loss: `0.000960`
- test_curve_amplitude_loss: `0.080579`
- test_sparse_harmonic_shape_loss: `0.000335`
- test_structured_mae: `0.003210`
- test_structured_rmse: `0.003793`
- test_base_mae: `0.019971`
- test_base_rmse: `0.023261`
- test_residual_offset_mean_abs: `0.001656`

## Interpretation

The held-out val error stayed finite with MAE=0.002320 deg and RMSE=0.002848 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001677 deg and RMSE=0.002151 deg, which indicates a numerically stable baseline run.
