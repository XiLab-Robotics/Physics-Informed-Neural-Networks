# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints`
- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Run Instance Id: `2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002270868280902505`
- Test RMSE: `0.003605000441893935`
- Validation MAE: `0.0019514970481395721`
- Output Directory: `output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=112-val_mae=0.00195150.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

