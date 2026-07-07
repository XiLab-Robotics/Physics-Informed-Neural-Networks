# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints`
- Generated At: `2026-07-07T11:21:45`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-10-46-08_dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoin`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_001_001_residual_harmonic_mlp_global.yaml` | `te_residual_harmonic_mlp_global__simplified_setpoints` | `residual_harmonic_mlp` | `completed` | `00:08:18` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_002_002_residual_harmonic_mlp_fw.yaml` | `te_residual_harmonic_mlp_fw__simplified_setpoints` | `residual_harmonic_mlp` | `completed` | `00:15:23` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_003_003_residual_harmonic_mlp_bw.yaml` | `te_residual_harmonic_mlp_bw__simplified_setpoints` | `residual_harmonic_mlp` | `completed` | `00:11:55` |

## Run Details

### te_residual_harmonic_mlp_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_001_001_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/queue/001_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T10:46:08`
- End Time: `2026-07-07T10:54:26`
- Duration: `00:08:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=010-val_mae=0.00315844.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-10-46-08_dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoin/logs/001_te_residual_harmonic_mlp_global__simplified_setp.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_002_002_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/queue/002_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T10:54:26`
- End Time: `2026-07-07T11:09:49`
- Duration: `00:15:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=079-val_mae=0.00306417.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-10-46-08_dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoin/logs/002_te_residual_harmonic_mlp_fw__simplified_setpoint.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/completed/2026-07-07-10-46-08_003_003_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints/queue/003_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T11:09:49`
- End Time: `2026-07-07T11:21:45`
- Duration: `00:11:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=032-val_mae=0.00306476.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-10-46-08_dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoin/logs/003_te_residual_harmonic_mlp_bw__simplified_setpoint.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
