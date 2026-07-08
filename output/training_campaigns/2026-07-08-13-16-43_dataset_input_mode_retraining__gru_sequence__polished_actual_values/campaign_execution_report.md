# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__polished_actual_values`
- Generated At: `2026-07-08T14:46:08`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-13-16-43_dataset_input_mode_retraining__gru_sequence__polished_actual_values`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_001_001_gru_sequence_global.yaml` | `te_gru_sequence_global__polished_actual_values` | `gru_sequence` | `completed` | `00:27:43` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_002_002_gru_sequence_fw.yaml` | `te_gru_sequence_fw__polished_actual_values` | `gru_sequence` | `completed` | `00:26:08` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_003_003_gru_sequence_bw.yaml` | `te_gru_sequence_bw__polished_actual_values` | `gru_sequence` | `completed` | `00:35:34` |

## Run Details

### te_gru_sequence_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_001_001_gru_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_actual_values/queue/001_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T13:16:43`
- End Time: `2026-07-08T13:44:26`
- Duration: `00:27:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/checkpoints/gru_sequence-epoch=141-val_mae=0.00217238.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-13-16-43_dataset_input_mode_retraining__gru_sequence__polished_actual_values/logs/001_te_gru_sequence_global__polished_actual_values.log`
- Error Message: `N/A`

### te_gru_sequence_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_002_002_gru_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_actual_values/queue/002_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T13:44:26`
- End Time: `2026-07-08T14:10:34`
- Duration: `00:26:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/checkpoints/gru_sequence-epoch=149-val_mae=0.00216525.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-13-16-43_dataset_input_mode_retraining__gru_sequence__polished_actual_values/logs/002_te_gru_sequence_fw__polished_actual_values.log`
- Error Message: `N/A`

### te_gru_sequence_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_actual_values/completed/2026-07-08-13-16-43_003_003_gru_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_actual_values/queue/003_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T14:10:34`
- End Time: `2026-07-08T14:46:08`
- Duration: `00:35:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/checkpoints/gru_sequence-epoch=172-val_mae=0.00214390.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-13-16-43_dataset_input_mode_retraining__gru_sequence__polished_actual_values/logs/003_te_gru_sequence_bw__polished_actual_values.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
