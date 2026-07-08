# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints`
- Generated At: `2026-07-08T02:43:23`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-01-46-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_001_001_periodic_mlp_harmonic_global.yaml` | `te_periodic_mlp_harmonic_global__polished_setpoints` | `periodic_mlp` | `completed` | `00:29:32` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_002_002_periodic_mlp_harmonic_fw.yaml` | `te_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | `completed` | `00:13:32` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_003_003_periodic_mlp_harmonic_bw.yaml` | `te_periodic_mlp_harmonic_bw__polished_setpoints` | `periodic_mlp` | `completed` | `00:13:51` |

## Run Details

### te_periodic_mlp_harmonic_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_001_001_periodic_mlp_harmonic_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/queue/001_periodic_mlp_harmonic_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T01:46:27`
- End Time: `2026-07-08T02:15:59`
- Duration: `00:29:32`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/checkpoints/periodic_mlp-epoch=183-val_mae=0.00113740.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-46-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/logs/001_te_periodic_mlp_harmonic_global__polished_setpoi.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_002_002_periodic_mlp_harmonic_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/queue/002_periodic_mlp_harmonic_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T02:15:59`
- End Time: `2026-07-08T02:29:31`
- Duration: `00:13:32`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/checkpoints/periodic_mlp-epoch=051-val_mae=0.00120808.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-46-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/logs/002_te_periodic_mlp_harmonic_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/completed/2026-07-08-01-46-27_003_003_periodic_mlp_harmonic_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/queue/003_periodic_mlp_harmonic_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T02:29:32`
- End Time: `2026-07-08T02:43:23`
- Duration: `00:13:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/checkpoints/periodic_mlp-epoch=081-val_mae=0.00121896.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-46-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints/logs/003_te_periodic_mlp_harmonic_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
