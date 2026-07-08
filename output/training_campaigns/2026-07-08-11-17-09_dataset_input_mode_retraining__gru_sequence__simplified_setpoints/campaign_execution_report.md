# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__simplified_setpoints`
- Generated At: `2026-07-08T11:47:31`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-11-17-09_dataset_input_mode_retraining__gru_sequence__simplified_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_001_001_gru_sequence_global.yaml` | `te_gru_sequence_global__simplified_setpoints` | `gru_sequence` | `completed` | `00:06:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_002_002_gru_sequence_fw.yaml` | `te_gru_sequence_fw__simplified_setpoints` | `gru_sequence` | `completed` | `00:07:50` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_003_003_gru_sequence_bw.yaml` | `te_gru_sequence_bw__simplified_setpoints` | `gru_sequence` | `completed` | `00:15:40` |

## Run Details

### te_gru_sequence_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_001_001_gru_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/queue/001_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T11:17:09`
- End Time: `2026-07-08T11:24:01`
- Duration: `00:06:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/checkpoints/gru_sequence-epoch=036-val_mae=0.00377716.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-17-09_dataset_input_mode_retraining__gru_sequence__simplified_setpoints/logs/001_te_gru_sequence_global__simplified_setpoints.log`
- Error Message: `N/A`

### te_gru_sequence_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_002_002_gru_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/queue/002_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T11:24:01`
- End Time: `2026-07-08T11:31:51`
- Duration: `00:07:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/checkpoints/gru_sequence-epoch=043-val_mae=0.00375895.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-17-09_dataset_input_mode_retraining__gru_sequence__simplified_setpoints/logs/002_te_gru_sequence_fw__simplified_setpoints.log`
- Error Message: `N/A`

### te_gru_sequence_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/completed/2026-07-08-11-17-09_003_003_gru_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__simplified_setpoints/queue/003_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T11:31:51`
- End Time: `2026-07-08T11:47:31`
- Duration: `00:15:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/checkpoints/gru_sequence-epoch=132-val_mae=0.00366119.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-17-09_dataset_input_mode_retraining__gru_sequence__simplified_setpoints/logs/003_te_gru_sequence_bw__simplified_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
