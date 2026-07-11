# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints`
- Run Name: `te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Run Instance Id: `2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0034000342711806297`
- Test RMSE: `0.004186728037893772`
- Validation MAE: `0.003571423003450036`
- Output Directory: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=145-val_mae=0.00357142.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

