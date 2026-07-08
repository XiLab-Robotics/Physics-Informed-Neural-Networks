# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__polished_setpoints`
- Run Name: `te_lstm_sequence_fw__polished_setpoints`
- Run Instance Id: `2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Test MAE: `0.002464499557390809`
- Test RMSE: `0.003858801443129778`
- Validation MAE: `0.0021909361239522696`
- Output Directory: `output\training_runs\lstm_sequence\2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\lstm_sequence\2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\lstm_sequence\2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\lstm_sequence\2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints\checkpoints\lstm_sequence-epoch=078-val_mae=0.00219094.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

