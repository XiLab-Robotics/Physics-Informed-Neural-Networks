# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_actual_values`
- Run Name: `te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values`
- Run Instance Id: `2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0019749989733099937`
- Test RMSE: `0.0030151286628097296`
- Validation MAE: `0.0018499749712646008`
- Output Directory: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=199-val_mae=0.00184997.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

