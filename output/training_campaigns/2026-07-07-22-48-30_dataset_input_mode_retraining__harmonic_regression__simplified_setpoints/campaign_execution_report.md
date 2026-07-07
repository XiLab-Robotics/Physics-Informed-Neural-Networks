# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__harmonic_regression__simplified_setpoints`
- Generated At: `2026-07-07T23:07:36`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-22-48-30_dataset_input_mode_retraining__harmonic_regression__simplified_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_001_001_harmonic_regression_global.yaml` | `te_harmonic_regression_global__simplified_setpoints` | `harmonic_regression` | `completed` | `00:06:29` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_002_002_harmonic_regression_fw.yaml` | `te_harmonic_regression_fw__simplified_setpoints` | `harmonic_regression` | `completed` | `00:06:09` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_003_003_harmonic_regression_bw.yaml` | `te_harmonic_regression_bw__simplified_setpoints` | `harmonic_regression` | `completed` | `00:06:28` |

## Run Details

### te_harmonic_regression_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_001_001_harmonic_regression_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/queue/001_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T22:48:30`
- End Time: `2026-07-07T22:54:59`
- Duration: `00:06:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/checkpoints/harmonic_regression-epoch=063-val_mae=0.01699328.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-22-48-30_dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/logs/001_te_harmonic_regression_global__simplified_setpoi.log`
- Error Message: `N/A`

### te_harmonic_regression_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_002_002_harmonic_regression_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/queue/002_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T22:54:59`
- End Time: `2026-07-07T23:01:08`
- Duration: `00:06:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints/checkpoints/harmonic_regression-epoch=033-val_mae=0.01699562.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-22-54-59__te_harmonic_regression_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-22-48-30_dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/logs/002_te_harmonic_regression_fw__simplified_setpoints.log`
- Error Message: `N/A`

### te_harmonic_regression_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/completed/2026-07-07-22-48-30_003_003_harmonic_regression_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/queue/003_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T23:01:08`
- End Time: `2026-07-07T23:07:36`
- Duration: `00:06:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/checkpoints/harmonic_regression-epoch=060-val_mae=0.01698885.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-22-48-30_dataset_input_mode_retraining__harmonic_regression__simplified_setpoints/logs/003_te_harmonic_regression_bw__simplified_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
