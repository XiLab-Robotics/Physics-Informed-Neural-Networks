# Campaign Best Run

## Overview

- Campaign Name: `track2f_bis_harmonic_offset_probe_repair_2026_06_05`
- Run Name: `te_track2f_bis_harmonic_residual_offset_fw`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Model Family: `track2f_bis_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Test MAE: `0.0028616469353437424`
- Test RMSE: `0.0033336810301989317`
- Validation MAE: `0.0029414519667625427`
- Output Directory: `output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Metrics Snapshot: `output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw\checkpoints\harmonic_residual_offset_probe-epoch=175-val_mae=0.00294145.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
