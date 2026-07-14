# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints`
- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Run Instance Id: `2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002094960305839777`
- Test RMSE: `0.0035193078219890594`
- Validation MAE: `0.001794740674085915`
- Output Directory: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=109-val_mae=0.00179474.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
