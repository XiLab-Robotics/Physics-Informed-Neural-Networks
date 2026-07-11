# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_setpoints`
- Run Name: `te_wave3_3_raw_offset_curve_aware_global__polished_setpoints`
- Run Instance Id: `2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002202904550358653`
- Test RMSE: `0.0035599174443632364`
- Validation MAE: `0.0018951412057504058`
- Output Directory: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00189514.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

