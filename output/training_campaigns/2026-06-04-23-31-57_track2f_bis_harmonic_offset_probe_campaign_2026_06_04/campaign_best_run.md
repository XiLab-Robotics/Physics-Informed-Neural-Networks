# Campaign Best Run

## Overview

- Campaign Name: `track2f_bis_harmonic_offset_probe_campaign_2026_06_04`
- Run Name: `te_track2f_bis_clean_residual_offset_fw`
- Run Instance Id: `2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw`
- Model Family: `track2f_bis_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.0034461263567209244`
- Test RMSE: `0.003971843980252743`
- Validation MAE: `0.003474122378975153`
- Output Directory: `output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw`
- Metrics Snapshot: `output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw\checkpoints\sequential_residual_offset_probe-epoch=020-val_mae=0.00347412.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
