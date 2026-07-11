# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_setpoints`
- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints`
- Run Instance Id: `2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0022390850353986025`
- Test RMSE: `0.003598244395107031`
- Validation MAE: `0.0019147873390465975`
- Output Directory: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_curve_aware_pointwise_control\2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=094-val_mae=0.00191479.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

