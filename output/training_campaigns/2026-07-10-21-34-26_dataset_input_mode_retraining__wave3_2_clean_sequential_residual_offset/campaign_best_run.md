# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values`
- Run Name: `te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Run Instance Id: `2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Model Family: `wave3_2_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.00228761974722147`
- Test RMSE: `0.0033455651719123125`
- Validation MAE: `0.002169393701478839`
- Output Directory: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values\checkpoints\sequential_residual_offset_probe-epoch=153-val_mae=0.00216939.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
