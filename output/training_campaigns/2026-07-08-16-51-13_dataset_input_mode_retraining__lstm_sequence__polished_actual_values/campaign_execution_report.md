# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__polished_actual_values`
- Generated At: `2026-07-08T18:46:16`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-16-51-13_dataset_input_mode_retraining__lstm_sequence__polished_actual_values`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_001_001_lstm_sequence_global.yaml` | `te_lstm_sequence_global__polished_actual_values` | `lstm_sequence` | `completed` | `00:29:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_002_002_lstm_sequence_fw.yaml` | `te_lstm_sequence_fw__polished_actual_values` | `lstm_sequence` | `completed` | `00:42:07` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_003_003_lstm_sequence_bw.yaml` | `te_lstm_sequence_bw__polished_actual_values` | `lstm_sequence` | `completed` | `00:43:50` |

## Run Details

### te_lstm_sequence_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_001_001_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/queue/001_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T16:51:13`
- End Time: `2026-07-08T17:20:19`
- Duration: `00:29:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/checkpoints/lstm_sequence-epoch=160-val_mae=0.00218895.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-16-51-13_dataset_input_mode_retraining__lstm_sequence__polished_actual_values/logs/001_te_lstm_sequence_global__polished_actual_values.log`
- Error Message: `N/A`

### te_lstm_sequence_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_002_002_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/queue/002_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T17:20:19`
- End Time: `2026-07-08T18:02:26`
- Duration: `00:42:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/checkpoints/lstm_sequence-epoch=210-val_mae=0.00215124.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-16-51-13_dataset_input_mode_retraining__lstm_sequence__polished_actual_values/logs/002_te_lstm_sequence_fw__polished_actual_values.log`
- Error Message: `N/A`

### te_lstm_sequence_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/completed/2026-07-08-16-51-13_003_003_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__polished_actual_values/queue/003_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T18:02:26`
- End Time: `2026-07-08T18:46:16`
- Duration: `00:43:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/checkpoints/lstm_sequence-epoch=240-val_mae=0.00214547.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-16-51-13_dataset_input_mode_retraining__lstm_sequence__polished_actual_values/logs/003_te_lstm_sequence_bw__polished_actual_values.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
