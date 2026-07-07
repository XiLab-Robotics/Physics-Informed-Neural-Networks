# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp__polished_setpoints`
- Generated At: `2026-07-07T21:25:45`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-20-38-26_dataset_input_mode_retraining__periodic_mlp__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_001_001_periodic_mlp_global.yaml` | `te_periodic_mlp_global__polished_setpoints` | `periodic_mlp` | `completed` | `00:14:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_002_002_periodic_mlp_fw.yaml` | `te_periodic_mlp_fw__polished_setpoints` | `periodic_mlp` | `completed` | `00:19:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_003_003_periodic_mlp_bw.yaml` | `te_periodic_mlp_bw__polished_setpoints` | `periodic_mlp` | `completed` | `00:14:06` |

## Run Details

### te_periodic_mlp_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_001_001_periodic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/queue/001_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T20:38:26`
- End Time: `2026-07-07T20:52:32`
- Duration: `00:14:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/checkpoints/periodic_mlp-epoch=080-val_mae=0.00165354.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-38-26_dataset_input_mode_retraining__periodic_mlp__polished_setpoints/logs/001_te_periodic_mlp_global__polished_setpoints.log`
- Error Message: `N/A`

### te_periodic_mlp_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_002_002_periodic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/queue/002_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T20:52:32`
- End Time: `2026-07-07T21:11:38`
- Duration: `00:19:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/checkpoints/periodic_mlp-epoch=089-val_mae=0.00162401.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-38-26_dataset_input_mode_retraining__periodic_mlp__polished_setpoints/logs/002_te_periodic_mlp_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_periodic_mlp_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/completed/2026-07-07-20-38-26_003_003_periodic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp__polished_setpoints/queue/003_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T21:11:38`
- End Time: `2026-07-07T21:25:45`
- Duration: `00:14:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints/checkpoints/periodic_mlp-epoch=055-val_mae=0.00165461.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-07-07-21-11-38__te_periodic_mlp_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-20-38-26_dataset_input_mode_retraining__periodic_mlp__polished_setpoints/logs/003_te_periodic_mlp_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
