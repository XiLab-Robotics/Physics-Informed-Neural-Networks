# Wave52B Offset Harmonic Guided Offset Centered Shape Global Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_global`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_global`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_global\2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global\checkpoints\wave52b_offset_harmonic_guided-epoch=083-val_mae=0.00227055.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.009361`
- val_mae: `0.002271`
- val_rmse: `0.002811`
- val_pointwise_loss: `0.006114`
- val_centered_curve_shape_loss: `0.005532`
- val_curve_offset_loss: `0.000582`
- val_curve_amplitude_loss: `0.041062`
- val_sparse_harmonic_shape_loss: `0.000127`
- val_structured_mae: `0.040232`
- val_structured_rmse: `0.043958`
- val_base_mae: `0.017273`
- val_base_rmse: `0.018961`
- val_residual_offset_mean_abs: `0.017026`

## Test Metrics

- test_loss: `0.013360`
- test_mae: `0.002540`
- test_rmse: `0.003229`
- test_pointwise_loss: `0.009266`
- test_centered_curve_shape_loss: `0.006712`
- test_curve_offset_loss: `0.002554`
- test_curve_amplitude_loss: `0.047381`
- test_sparse_harmonic_shape_loss: `0.000137`
- test_structured_mae: `0.037992`
- test_structured_rmse: `0.042295`
- test_base_mae: `0.016390`
- test_base_rmse: `0.018397`
- test_residual_offset_mean_abs: `0.015960`

## Interpretation

The held-out val error stayed finite with MAE=0.002271 deg and RMSE=0.002811 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002540 deg and RMSE=0.003229 deg, which indicates a numerically stable baseline run.
