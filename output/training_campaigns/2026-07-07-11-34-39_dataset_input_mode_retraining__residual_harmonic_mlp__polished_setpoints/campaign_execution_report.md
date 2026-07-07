# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints`
- Generated At: `2026-07-07T13:03:04`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-11-34-39_dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_001_001_residual_harmonic_mlp_global.yaml` | `te_residual_harmonic_mlp_global__polished_setpoints` | `residual_harmonic_mlp` | `completed` | `00:28:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_002_002_residual_harmonic_mlp_fw.yaml` | `te_residual_harmonic_mlp_fw__polished_setpoints` | `residual_harmonic_mlp` | `completed` | `00:34:12` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_003_003_residual_harmonic_mlp_bw.yaml` | `te_residual_harmonic_mlp_bw__polished_setpoints` | `residual_harmonic_mlp` | `completed` | `00:26:08` |

## Run Details

### te_residual_harmonic_mlp_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_001_001_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/queue/001_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T11:34:39`
- End Time: `2026-07-07T12:02:44`
- Duration: `00:28:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=069-val_mae=0.00158201.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-11-34-39_dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/logs/001_te_residual_harmonic_mlp_global__polished_setpoi.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_002_002_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/queue/002_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T12:02:44`
- End Time: `2026-07-07T12:36:55`
- Duration: `00:34:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=122-val_mae=0.00159866.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-11-34-39_dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/logs/002_te_residual_harmonic_mlp_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/completed/2026-07-07-11-34-39_003_003_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/queue/003_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T12:36:55`
- End Time: `2026-07-07T13:03:04`
- Duration: `00:26:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=093-val_mae=0.00162645.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-11-34-39_dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints/logs/003_te_residual_harmonic_mlp_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
