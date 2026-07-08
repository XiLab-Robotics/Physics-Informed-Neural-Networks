# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__polished_setpoints`
- Generated At: `2026-07-08T16:38:40`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-15-45-54_dataset_input_mode_retraining__lstm_sequence__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_001_001_lstm_sequence_global.yaml` | `te_lstm_sequence_global__polished_setpoints` | `lstm_sequence` | `completed` | `00:20:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_002_002_lstm_sequence_fw.yaml` | `te_lstm_sequence_fw__polished_setpoints` | `lstm_sequence` | `completed` | `00:15:04` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_003_003_lstm_sequence_bw.yaml` | `te_lstm_sequence_bw__polished_setpoints` | `lstm_sequence` | `completed` | `00:17:36` |

## Run Details

### te_lstm_sequence_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_001_001_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/queue/001_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T15:45:54`
- End Time: `2026-07-08T16:05:59`
- Duration: `00:20:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/checkpoints/lstm_sequence-epoch=118-val_mae=0.00218648.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-15-45-54_dataset_input_mode_retraining__lstm_sequence__polished_setpoints/logs/001_te_lstm_sequence_global__polished_setpoints.log`
- Error Message: `N/A`

### te_lstm_sequence_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_002_002_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/queue/002_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T16:05:59`
- End Time: `2026-07-08T16:21:04`
- Duration: `00:15:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/checkpoints/lstm_sequence-epoch=078-val_mae=0.00219094.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-15-45-54_dataset_input_mode_retraining__lstm_sequence__polished_setpoints/logs/002_te_lstm_sequence_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_lstm_sequence_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/completed/2026-07-08-15-45-54_003_003_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_setpoints/queue/003_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T16:21:04`
- End Time: `2026-07-08T16:38:40`
- Duration: `00:17:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/checkpoints/lstm_sequence-epoch=070-val_mae=0.00219971.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-15-45-54_dataset_input_mode_retraining__lstm_sequence__polished_setpoints/logs/003_te_lstm_sequence_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
