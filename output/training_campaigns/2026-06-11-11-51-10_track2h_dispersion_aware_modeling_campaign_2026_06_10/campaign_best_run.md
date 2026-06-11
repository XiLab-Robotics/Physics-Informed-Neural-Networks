# Campaign Best Run

## Overview

- Campaign Name: `track2h_dispersion_aware_modeling_campaign_2026_06_10`
- Run Name: `te_track2h_smooth_l1_robust_bw`
- Run Instance Id: `2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw`
- Model Family: `track2h_dispersion_aware_smooth_l1_robust_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.003073683939874172`
- Test RMSE: `0.0036618902813643217`
- Validation MAE: `0.003372314851731062`
- Output Directory: `output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw`
- Metrics Snapshot: `output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=231-val_mae=0.00337231.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
