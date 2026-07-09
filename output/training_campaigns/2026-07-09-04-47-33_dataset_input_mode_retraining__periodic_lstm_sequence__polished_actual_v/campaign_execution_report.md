# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values`
- Generated At: `2026-07-09T05:28:43`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-04-47-33_dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_v`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_001_001_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_global__polished_actual_values` | `periodic_lstm_sequence` | `completed` | `00:18:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_002_002_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_fw__polished_actual_values` | `periodic_lstm_sequence` | `completed` | `00:10:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_003_003_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_bw__polished_actual_values` | `periodic_lstm_sequence` | `completed` | `00:12:12` |

## Run Details

### te_periodic_lstm_sequence_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_001_001_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/queue/001_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T04:47:33`
- End Time: `2026-07-09T05:06:07`
- Duration: `00:18:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/checkpoints/periodic_lstm_sequence-epoch=103-val_mae=0.00191666.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-04-47-33_dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_v/logs/001_te_periodic_lstm_sequence_global__polished_actua.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_002_002_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/queue/002_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T05:06:07`
- End Time: `2026-07-09T05:16:31`
- Duration: `00:10:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values/checkpoints/periodic_lstm_sequence-epoch=017-val_mae=0.00196587.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-06-07__te_periodic_lstm_sequence_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-04-47-33_dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_v/logs/002_te_periodic_lstm_sequence_fw__polished_actual_va.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/completed/2026-07-09-04-47-33_003_003_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values/queue/003_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T05:16:31`
- End Time: `2026-07-09T05:28:43`
- Duration: `00:12:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/checkpoints/periodic_lstm_sequence-epoch=053-val_mae=0.00197877.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-04-47-33_dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_v/logs/003_te_periodic_lstm_sequence_bw__polished_actual_va.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
