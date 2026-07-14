# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Run Instance Id: `2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.003342448500916362`
- Test RMSE: `0.004120647441595793`
- Validation MAE: `0.0035372453276067972`
- Output Directory: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=091-val_mae=0.00353725.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
