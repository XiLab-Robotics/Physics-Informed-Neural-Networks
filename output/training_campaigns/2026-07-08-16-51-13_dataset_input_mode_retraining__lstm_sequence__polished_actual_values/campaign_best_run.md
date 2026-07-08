# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__polished_actual_values`
- Run Name: `te_lstm_sequence_fw__polished_actual_values`
- Run Instance Id: `2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Test MAE: `0.002238660119473934`
- Test RMSE: `0.0033192161936312914`
- Validation MAE: `0.002151240361854434`
- Output Directory: `output\training_runs\lstm_sequence\2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\lstm_sequence\2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\lstm_sequence\2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\lstm_sequence\2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values\checkpoints\lstm_sequence-epoch=210-val_mae=0.00215124.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

