# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints`
- Generated At: `2026-07-08T01:27:11`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-01-02-50_dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoin`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_001_001_periodic_mlp_harmonic_global.yaml` | `te_periodic_mlp_harmonic_global__simplified_setpoints` | `periodic_mlp` | `completed` | `00:08:22` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_002_002_periodic_mlp_harmonic_fw.yaml` | `te_periodic_mlp_harmonic_fw__simplified_setpoints` | `periodic_mlp` | `completed` | `00:08:09` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_003_003_periodic_mlp_harmonic_bw.yaml` | `te_periodic_mlp_harmonic_bw__simplified_setpoints` | `periodic_mlp` | `completed` | `00:07:49` |

## Run Details

### te_periodic_mlp_harmonic_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_001_001_periodic_mlp_harmonic_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/queue/001_periodic_mlp_harmonic_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T01:02:50`
- End Time: `2026-07-08T01:11:12`
- Duration: `00:08:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/checkpoints/periodic_mlp-epoch=059-val_mae=0.00284742.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-02-50_dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoin/logs/001_te_periodic_mlp_harmonic_global__simplified_setp.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_002_002_periodic_mlp_harmonic_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/queue/002_periodic_mlp_harmonic_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T01:11:12`
- End Time: `2026-07-08T01:19:22`
- Duration: `00:08:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/checkpoints/periodic_mlp-epoch=055-val_mae=0.00280280.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-02-50_dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoin/logs/002_te_periodic_mlp_harmonic_fw__simplified_setpoint.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/completed/2026-07-08-01-02-50_003_003_periodic_mlp_harmonic_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints/queue/003_periodic_mlp_harmonic_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T01:19:22`
- End Time: `2026-07-08T01:27:11`
- Duration: `00:07:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/checkpoints/periodic_mlp-epoch=053-val_mae=0.00280310.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-01-02-50_dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoin/logs/003_te_periodic_mlp_harmonic_bw__simplified_setpoint.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
