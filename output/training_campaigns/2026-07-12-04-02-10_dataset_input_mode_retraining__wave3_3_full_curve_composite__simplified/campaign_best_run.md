# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints`
- Run Name: `te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Run Instance Id: `2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Model Family: `wave3_3_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0034191631712019444`
- Test RMSE: `0.004197763744741678`
- Validation MAE: `0.0036387292202562094`
- Output Directory: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_3_full_curve_composite\2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=172-val_mae=0.00363873.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
