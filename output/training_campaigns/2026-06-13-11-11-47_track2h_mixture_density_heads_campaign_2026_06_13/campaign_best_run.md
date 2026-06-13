# Campaign Best Run

## Overview

- Campaign Name: `track2h_mixture_density_heads_campaign_2026_06_13`
- Run Name: `te_track2h_mdn_k2_bw`
- Run Instance Id: `2026-06-13-11-41-07__te_track2h_mdn_k2_bw`
- Model Family: `track2h_mixture_density_heads_mdn_k2_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002658107550814748`
- Test RMSE: `0.0031979118939489126`
- Validation MAE: `0.0029144026339054108`
- Output Directory: `output\training_runs\track2h_mixture_density_heads_mdn_k2_bw\2026-06-13-11-41-07__te_track2h_mdn_k2_bw`
- Metrics Snapshot: `output\training_runs\track2h_mixture_density_heads_mdn_k2_bw\2026-06-13-11-41-07__te_track2h_mdn_k2_bw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2h_mixture_density_heads_mdn_k2_bw\2026-06-13-11-41-07__te_track2h_mdn_k2_bw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2h_mixture_density_heads_mdn_k2_bw\2026-06-13-11-41-07__te_track2h_mdn_k2_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=236-val_mae=0.00291440.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

