# Campaign Best Run

## Overview

- Campaign Name: `polished_dataset_full_wave_retraining_2026_06_22`
- Run Name: `te_periodic_gru_sequence_fw`
- Run Instance Id: `2026-06-30-02-56-10__te_periodic_gru_sequence_fw`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.001120887347497046`
- Test RMSE: `0.0014436584897339344`
- Validation MAE: `0.0010840588947758079`
- Output Directory: `output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw`
- Metrics Snapshot: `output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw\checkpoints\periodic_gru_sequence-epoch=235-val_mae=0.00108406.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
