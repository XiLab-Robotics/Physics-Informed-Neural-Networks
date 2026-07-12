# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints`
- Run Name: `te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Run Instance Id: `2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Model Family: `wave3_3_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0023530113976448774`
- Test RMSE: `0.0037150071002542973`
- Validation MAE: `0.002030177740380168`
- Output Directory: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=107-val_mae=0.00203018.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

