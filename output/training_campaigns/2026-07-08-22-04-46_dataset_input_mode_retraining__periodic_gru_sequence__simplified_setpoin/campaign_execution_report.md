# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints`
- Generated At: `2026-07-08T22:33:24`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-22-04-46_dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoin`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_001_001_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_global__simplified_setpoints` | `periodic_gru_sequence` | `completed` | `00:09:35` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_002_002_periodic_gru_sequence_fw.yaml` | `te_periodic_gru_sequence_fw__simplified_setpoints` | `periodic_gru_sequence` | `completed` | `00:09:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_003_003_periodic_gru_sequence_bw.yaml` | `te_periodic_gru_sequence_bw__simplified_setpoints` | `periodic_gru_sequence` | `completed` | `00:09:58` |

## Run Details

### te_periodic_gru_sequence_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_001_001_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/queue/001_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T22:04:46`
- End Time: `2026-07-08T22:14:21`
- Duration: `00:09:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=060-val_mae=0.00347740.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-22-04-46_dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoin/logs/001_te_periodic_gru_sequence_global__simplified_setp.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_002_002_periodic_gru_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/queue/002_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T22:14:21`
- End Time: `2026-07-08T22:23:26`
- Duration: `00:09:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=056-val_mae=0.00353205.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-22-04-46_dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoin/logs/002_te_periodic_gru_sequence_fw__simplified_setpoint.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/completed/2026-07-08-22-04-46_003_003_periodic_gru_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints/queue/003_periodic_gru_sequence_bw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T22:23:27`
- End Time: `2026-07-08T22:33:24`
- Duration: `00:09:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=081-val_mae=0.00349987.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-22-04-46_dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoin/logs/003_te_periodic_gru_sequence_bw__simplified_setpoint.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
