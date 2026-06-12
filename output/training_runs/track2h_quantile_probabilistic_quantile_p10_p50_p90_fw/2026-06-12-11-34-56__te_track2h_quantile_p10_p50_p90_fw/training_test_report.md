# Track2H Quantile Probabilistic Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_quantile_p10_p50_p90_fw`
- Model Family: `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_fw\2026-06-12-11-34-56__te_track2h_quantile_p10_p50_p90_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=019-val_mae=0.00326876.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.042195`
- val_mae: `0.003269`
- val_rmse: `0.003793`
- val_pointwise_loss: `0.042195`
- val_centered_curve_shape_loss: `0.015343`
- val_curve_offset_loss: `0.016540`
- val_curve_amplitude_loss: `0.096066`
- val_sparse_harmonic_shape_loss: `0.000334`
- val_interval_coverage: `0.865416`
- val_interval_width: `0.010915`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.017411`
- val_structured_rmse: `0.020220`
- val_residual_offset_mean_abs: `0.016674`

## Test Metrics

- test_loss: `0.040618`
- test_mae: `0.003285`
- test_rmse: `0.003668`
- test_pointwise_loss: `0.040618`
- test_centered_curve_shape_loss: `0.007928`
- test_curve_offset_loss: `0.019785`
- test_curve_amplitude_loss: `0.041911`
- test_sparse_harmonic_shape_loss: `0.000147`
- test_interval_coverage: `0.848636`
- test_interval_width: `0.010536`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.018459`
- test_structured_rmse: `0.021440`
- test_residual_offset_mean_abs: `0.018466`

## Interpretation

The held-out val error stayed finite with MAE=0.003269 deg and RMSE=0.003793 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003285 deg and RMSE=0.003668 deg, which indicates a numerically stable baseline run.
