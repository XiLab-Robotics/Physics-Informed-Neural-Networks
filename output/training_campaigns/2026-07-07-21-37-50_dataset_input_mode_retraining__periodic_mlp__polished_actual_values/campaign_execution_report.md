# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp__polished_actual_values`
- Generated At: `2026-07-07T22:30:45`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-21-37-50_dataset_input_mode_retraining__periodic_mlp__polished_actual_values`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_001_001_periodic_mlp_global.yaml` | `te_periodic_mlp_global__polished_actual_values` | `periodic_mlp` | `completed` | `00:20:28` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_002_002_periodic_mlp_fw.yaml` | `te_periodic_mlp_fw__polished_actual_values` | `periodic_mlp` | `completed` | `00:14:00` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_003_003_periodic_mlp_bw.yaml` | `te_periodic_mlp_bw__polished_actual_values` | `periodic_mlp` | `completed` | `00:18:27` |

## Run Details

### te_periodic_mlp_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_001_001_periodic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/queue/001_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T21:37:50`
- End Time: `2026-07-07T21:58:17`
- Duration: `00:20:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/checkpoints/periodic_mlp-epoch=094-val_mae=0.00165445.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-21-37-50_dataset_input_mode_retraining__periodic_mlp__polished_actual_values/logs/001_te_periodic_mlp_global__polished_actual_values.log`
- Error Message: `N/A`

### te_periodic_mlp_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_002_002_periodic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/queue/002_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T21:58:17`
- End Time: `2026-07-07T22:12:18`
- Duration: `00:14:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/checkpoints/periodic_mlp-epoch=048-val_mae=0.00168924.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-21-37-50_dataset_input_mode_retraining__periodic_mlp__polished_actual_values/logs/002_te_periodic_mlp_fw__polished_actual_values.log`
- Error Message: `N/A`

### te_periodic_mlp_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/completed/2026-07-07-21-37-50_003_003_periodic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_actual_values/queue/003_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T22:12:18`
- End Time: `2026-07-07T22:30:45`
- Duration: `00:18:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/checkpoints/periodic_mlp-epoch=076-val_mae=0.00167645.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-21-37-50_dataset_input_mode_retraining__periodic_mlp__polished_actual_values/logs/003_te_periodic_mlp_bw__polished_actual_values.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
