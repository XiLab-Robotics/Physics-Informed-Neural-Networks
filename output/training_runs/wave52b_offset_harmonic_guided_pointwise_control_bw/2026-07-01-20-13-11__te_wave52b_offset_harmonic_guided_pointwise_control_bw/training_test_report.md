# Wave52B Offset Harmonic Guided Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_pointwise_control_bw`
- Model Family: `wave52b_offset_harmonic_guided_pointwise_control_bw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_bw\2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=102-val_mae=0.00259094.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.036997`
- val_mae: `0.002591`
- val_rmse: `0.003201`
- val_pointwise_loss: `0.036997`
- val_centered_curve_shape_loss: `0.035866`
- val_curve_offset_loss: `0.001131`
- val_curve_amplitude_loss: `0.351910`
- val_sparse_harmonic_shape_loss: `0.000889`
- val_structured_mae: `0.019549`
- val_structured_rmse: `0.023002`
- val_base_mae: `0.002591`
- val_base_rmse: `0.003201`
- val_residual_offset_mean_abs: `0.000000e+00`

## Test Metrics

- test_loss: `0.019675`
- test_mae: `0.001979`
- test_rmse: `0.002587`
- test_pointwise_loss: `0.019675`
- test_centered_curve_shape_loss: `0.018730`
- test_curve_offset_loss: `0.000945`
- test_curve_amplitude_loss: `0.166258`
- test_sparse_harmonic_shape_loss: `0.000444`
- test_structured_mae: `0.020345`
- test_structured_rmse: `0.023741`
- test_base_mae: `0.001979`
- test_base_rmse: `0.002587`
- test_residual_offset_mean_abs: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002591 deg and RMSE=0.003201 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001979 deg and RMSE=0.002587 deg, which indicates a numerically stable baseline run.
