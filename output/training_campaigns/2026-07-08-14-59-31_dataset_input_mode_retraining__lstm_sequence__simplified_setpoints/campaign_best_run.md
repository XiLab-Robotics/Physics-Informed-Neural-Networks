# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints`
- Run Name: `te_lstm_sequence_global__simplified_setpoints`
- Run Instance Id: `2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Test MAE: `0.0034460152965039015`
- Test RMSE: `0.004293248988687992`
- Validation MAE: `0.003692096099257469`
- Output Directory: `output\training_runs\lstm_sequence\2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\lstm_sequence\2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\lstm_sequence\2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\lstm_sequence\2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints\checkpoints\lstm_sequence-epoch=115-val_mae=0.00369210.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

