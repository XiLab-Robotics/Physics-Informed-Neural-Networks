# Campaign Best Run

## Overview

- Campaign Name: `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25`
- Run Name: `te_periodic_gru_sequence_remote_Bw`
- Run Instance Id: `2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.0023438564967364073`
- Test RMSE: `0.002746675396338105`
- Validation MAE: `0.0025232085026800632`
- Output Directory: `output\training_runs\periodic_gru_sequence_bw\2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw`
- Metrics Snapshot: `output\training_runs\periodic_gru_sequence_bw\2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_gru_sequence_bw\2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_gru_sequence_bw\2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw\checkpoints\periodic_gru_sequence-epoch=252-val_mae=0.00252321.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
