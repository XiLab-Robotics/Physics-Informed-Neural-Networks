# Wave52B Offset Harmonic Guided Offset Head Global Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_head_global`
- Model Family: `wave52b_offset_harmonic_guided_offset_head_global`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_global\2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global\checkpoints\wave52b_offset_harmonic_guided-epoch=092-val_mae=0.00224943.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006092`
- val_mae: `0.002249`
- val_rmse: `0.002787`
- val_pointwise_loss: `0.006011`
- val_centered_curve_shape_loss: `0.005474`
- val_curve_offset_loss: `0.000537`
- val_curve_amplitude_loss: `0.054807`
- val_sparse_harmonic_shape_loss: `0.000126`
- val_structured_mae: `0.040232`
- val_structured_rmse: `0.043958`
- val_base_mae: `0.015494`
- val_base_rmse: `0.017283`
- val_residual_offset_mean_abs: `0.015246`

## Test Metrics

- test_loss: `0.009171`
- test_mae: `0.002483`
- test_rmse: `0.003166`
- test_pointwise_loss: `0.008814`
- test_centered_curve_shape_loss: `0.006436`
- test_curve_offset_loss: `0.002378`
- test_curve_amplitude_loss: `0.064028`
- test_sparse_harmonic_shape_loss: `0.000135`
- test_structured_mae: `0.037992`
- test_structured_rmse: `0.042295`
- test_base_mae: `0.014873`
- test_base_rmse: `0.016886`
- test_residual_offset_mean_abs: `0.014478`

## Interpretation

The held-out val error stayed finite with MAE=0.002249 deg and RMSE=0.002787 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002483 deg and RMSE=0.003166 deg, which indicates a numerically stable baseline run.
