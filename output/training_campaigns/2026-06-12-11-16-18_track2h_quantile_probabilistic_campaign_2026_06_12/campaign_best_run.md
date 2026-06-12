# Campaign Best Run

## Overview

- Campaign Name: `track2h_quantile_probabilistic_campaign_2026_06_12`
- Run Name: `te_track2h_quantile_p10_p50_p90_bw`
- Run Instance Id: `2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw`
- Model Family: `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0029270444065332413`
- Test RMSE: `0.003519478952512145`
- Validation MAE: `0.0034355325624346733`
- Output Directory: `output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw`
- Metrics Snapshot: `output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=206-val_mae=0.00343553.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
