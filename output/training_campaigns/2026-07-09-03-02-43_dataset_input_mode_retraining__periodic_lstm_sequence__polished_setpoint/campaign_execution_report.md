# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints`
- Generated At: `2026-07-09T04:34:07`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-03-02-43_dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoint`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_001_001_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_global__polished_setpoints` | `periodic_lstm_sequence` | `completed` | `00:39:46` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_002_002_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_fw__polished_setpoints` | `periodic_lstm_sequence` | `completed` | `00:13:51` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_003_003_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_bw__polished_setpoints` | `periodic_lstm_sequence` | `completed` | `00:37:47` |

## Run Details

### te_periodic_lstm_sequence_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_001_001_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/queue/001_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T03:02:43`
- End Time: `2026-07-09T03:42:29`
- Duration: `00:39:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/checkpoints/periodic_lstm_sequence-epoch=245-val_mae=0.00137071.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-03-02-43_dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoint/logs/001_te_periodic_lstm_sequence_global__polished_setpo.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_002_002_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/queue/002_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T03:42:29`
- End Time: `2026-07-09T03:56:20`
- Duration: `00:13:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/checkpoints/periodic_lstm_sequence-epoch=047-val_mae=0.00186699.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-03-02-43_dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoint/logs/002_te_periodic_lstm_sequence_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/completed/2026-07-09-03-02-43_003_003_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints/queue/003_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T03:56:20`
- End Time: `2026-07-09T04:34:07`
- Duration: `00:37:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints/checkpoints/periodic_lstm_sequence-epoch=208-val_mae=0.00138862.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-03-56-20__te_periodic_lstm_sequence_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-03-02-43_dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoint/logs/003_te_periodic_lstm_sequence_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
