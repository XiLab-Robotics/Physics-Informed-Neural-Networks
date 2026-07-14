# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Run Instance Id: `2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0033780643716454506`
- Test RMSE: `0.004183328244835138`
- Validation MAE: `0.0035158887039870024`
- Output Directory: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=096-val_mae=0.00351589.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
