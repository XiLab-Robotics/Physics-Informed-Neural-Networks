# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__harmonic_regression__polished_setpoints`
- Generated At: `2026-07-07T23:49:55`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-23-18-16_dataset_input_mode_retraining__harmonic_regression__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_001_001_harmonic_regression_global.yaml` | `te_harmonic_regression_global__polished_setpoints` | `harmonic_regression` | `completed` | `00:10:51` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_002_002_harmonic_regression_fw.yaml` | `te_harmonic_regression_fw__polished_setpoints` | `harmonic_regression` | `completed` | `00:10:33` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_003_003_harmonic_regression_bw.yaml` | `te_harmonic_regression_bw__polished_setpoints` | `harmonic_regression` | `completed` | `00:10:14` |

## Run Details

### te_harmonic_regression_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_001_001_harmonic_regression_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/queue/001_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T23:18:16`
- End Time: `2026-07-07T23:29:07`
- Duration: `00:10:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/checkpoints/harmonic_regression-epoch=038-val_mae=0.01714113.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-23-18-16_dataset_input_mode_retraining__harmonic_regression__polished_setpoints/logs/001_te_harmonic_regression_global__polished_setpoint.log`
- Error Message: `N/A`

### te_harmonic_regression_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_002_002_harmonic_regression_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/queue/002_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T23:29:07`
- End Time: `2026-07-07T23:39:40`
- Duration: `00:10:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/checkpoints/harmonic_regression-epoch=032-val_mae=0.01714993.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-23-18-16_dataset_input_mode_retraining__harmonic_regression__polished_setpoints/logs/002_te_harmonic_regression_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_harmonic_regression_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/completed/2026-07-07-23-18-16_003_003_harmonic_regression_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_setpoints/queue/003_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T23:39:40`
- End Time: `2026-07-07T23:49:55`
- Duration: `00:10:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/checkpoints/harmonic_regression-epoch=044-val_mae=0.01715066.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-23-18-16_dataset_input_mode_retraining__harmonic_regression__polished_setpoints/logs/003_te_harmonic_regression_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
