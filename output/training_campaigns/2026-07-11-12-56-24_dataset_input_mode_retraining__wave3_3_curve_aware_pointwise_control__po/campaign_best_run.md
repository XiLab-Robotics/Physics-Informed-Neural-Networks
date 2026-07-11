# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values`
- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Run Instance Id: `2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.001943023526109755`
- Test RMSE: `0.00297743733972311`
- Validation MAE: `0.0018328940495848656`
- Output Directory: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00183289.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

