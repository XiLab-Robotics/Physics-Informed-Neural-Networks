# Causal Offset Mean Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_causal_offset_mean_gru_sequence_fw__polished_setpoints`
- Model Family: `causal_offset_mean_gru_sequence_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\causal_offset_mean_calibration\2026-07-22-18-09-27__te_causal_offset_mean_gru_sequence_fw__polished_setpoints\checkpoints\sequential_residual_offset_probe-epoch=012-val_mae=0.00242843.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028714`
- val_mae: `0.002428`
- val_rmse: `0.002972`
- val_pointwise_loss: `0.021806`
- val_centered_curve_shape_loss: `0.019289`
- val_curve_offset_loss: `0.002517`
- val_curve_amplitude_loss: `0.106397`
- val_sparse_harmonic_shape_loss: `0.000443`
- val_base_mae: `0.013305`
- val_base_rmse: `0.015572`
- val_residual_offset_mean_abs: `0.013476`

## Test Metrics

- test_loss: `0.018611`
- test_mae: `0.002100`
- test_rmse: `0.002610`
- test_pointwise_loss: `0.014675`
- test_centered_curve_shape_loss: `0.011694`
- test_curve_offset_loss: `0.002981`
- test_curve_amplitude_loss: `0.053888`
- test_sparse_harmonic_shape_loss: `0.000250`
- test_base_mae: `0.013640`
- test_base_rmse: `0.015809`
- test_residual_offset_mean_abs: `0.014143`

## Interpretation

The held-out val error stayed finite with MAE=0.002428 deg and RMSE=0.002972 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002100 deg and RMSE=0.002610 deg, which indicates a numerically stable baseline run.
