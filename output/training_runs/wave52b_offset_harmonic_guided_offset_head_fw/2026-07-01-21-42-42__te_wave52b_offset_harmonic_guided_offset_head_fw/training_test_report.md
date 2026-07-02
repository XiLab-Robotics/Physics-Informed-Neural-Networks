# Wave52B Offset Harmonic Guided Offset Head Fw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_head_fw`
- Model Family: `wave52b_offset_harmonic_guided_offset_head_fw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_fw\2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=084-val_mae=0.00225646.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020579`
- val_mae: `0.002256`
- val_rmse: `0.002789`
- val_pointwise_loss: `0.020347`
- val_centered_curve_shape_loss: `0.018799`
- val_curve_offset_loss: `0.001548`
- val_curve_amplitude_loss: `0.193125`
- val_sparse_harmonic_shape_loss: `0.000433`
- val_structured_mae: `0.019635`
- val_structured_rmse: `0.023073`
- val_base_mae: `0.010413`
- val_base_rmse: `0.011688`
- val_residual_offset_mean_abs: `0.010102`

## Test Metrics

- test_loss: `0.013738`
- test_mae: `0.001948`
- test_rmse: `0.002454`
- test_pointwise_loss: `0.013431`
- test_centered_curve_shape_loss: `0.011387`
- test_curve_offset_loss: `0.002044`
- test_curve_amplitude_loss: `0.123976`
- test_sparse_harmonic_shape_loss: `0.000245`
- test_structured_mae: `0.020063`
- test_structured_rmse: `0.023460`
- test_base_mae: `0.010001`
- test_base_rmse: `0.011160`
- test_residual_offset_mean_abs: `0.009982`

## Interpretation

The held-out val error stayed finite with MAE=0.002256 deg and RMSE=0.002789 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001948 deg and RMSE=0.002454 deg, which indicates a numerically stable baseline run.
