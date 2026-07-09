# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values`
- Generated At: `2026-07-09T01:51:59`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-23-45-29_dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_va`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_001_001_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_global__polished_actual_values` | `periodic_gru_sequence` | `completed` | `00:43:44` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_002_002_periodic_gru_sequence_fw.yaml` | `te_periodic_gru_sequence_fw__polished_actual_values` | `periodic_gru_sequence` | `completed` | `00:40:09` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_003_003_periodic_gru_sequence_bw.yaml` | `te_periodic_gru_sequence_bw__polished_actual_values` | `periodic_gru_sequence` | `completed` | `00:42:38` |

## Run Details

### te_periodic_gru_sequence_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_001_001_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/queue/001_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T23:45:29`
- End Time: `2026-07-09T00:29:12`
- Duration: `00:43:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=259-val_mae=0.00132221.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-23-45-29_dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_va/logs/001_te_periodic_gru_sequence_global__polished_actual.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_002_002_periodic_gru_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/queue/002_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T00:29:12`
- End Time: `2026-07-09T01:09:21`
- Duration: `00:40:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=200-val_mae=0.00150079.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-23-45-29_dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_va/logs/002_te_periodic_gru_sequence_fw__polished_actual_val.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/completed/2026-07-08-23-45-29_003_003_periodic_gru_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values/queue/003_periodic_gru_sequence_bw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T01:09:21`
- End Time: `2026-07-09T01:51:59`
- Duration: `00:42:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=257-val_mae=0.00127934.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-23-45-29_dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_va/logs/003_te_periodic_gru_sequence_bw__polished_actual_val.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
