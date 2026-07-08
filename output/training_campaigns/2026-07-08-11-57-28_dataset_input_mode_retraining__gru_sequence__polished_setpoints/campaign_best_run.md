# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__polished_setpoints`
- Run Name: `te_gru_sequence_fw__polished_setpoints`
- Run Instance Id: `2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Test MAE: `0.0024306881241500378`
- Test RMSE: `0.0038106588181108236`
- Validation MAE: `0.0021622295025736094`
- Output Directory: `output\training_runs\gru_sequence\2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\gru_sequence\2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\gru_sequence\2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\gru_sequence\2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints\checkpoints\gru_sequence-epoch=152-val_mae=0.00216223.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

