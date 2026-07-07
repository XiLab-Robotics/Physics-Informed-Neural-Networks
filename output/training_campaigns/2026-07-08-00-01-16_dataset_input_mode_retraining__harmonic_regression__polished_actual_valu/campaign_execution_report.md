# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__harmonic_regression__polished_actual_values`
- Generated At: `2026-07-08T00:46:14`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-00-01-16_dataset_input_mode_retraining__harmonic_regression__polished_actual_valu`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_001_001_harmonic_regression_global.yaml` | `te_harmonic_regression_global__polished_actual_values` | `harmonic_regression` | `completed` | `00:13:58` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_002_002_harmonic_regression_fw.yaml` | `te_harmonic_regression_fw__polished_actual_values` | `harmonic_regression` | `completed` | `00:17:07` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_003_003_harmonic_regression_bw.yaml` | `te_harmonic_regression_bw__polished_actual_values` | `harmonic_regression` | `completed` | `00:13:53` |

## Run Details

### te_harmonic_regression_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_001_001_harmonic_regression_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/queue/001_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T00:01:16`
- End Time: `2026-07-08T00:15:14`
- Duration: `00:13:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/checkpoints/harmonic_regression-epoch=053-val_mae=0.00182331.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-00-01-16_dataset_input_mode_retraining__harmonic_regression__polished_actual_valu/logs/001_te_harmonic_regression_global__polished_actual_v.log`
- Error Message: `N/A`

### te_harmonic_regression_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_002_002_harmonic_regression_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/queue/002_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T00:15:14`
- End Time: `2026-07-08T00:32:21`
- Duration: `00:17:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/checkpoints/harmonic_regression-epoch=073-val_mae=0.00182314.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-00-01-16_dataset_input_mode_retraining__harmonic_regression__polished_actual_valu/logs/002_te_harmonic_regression_fw__polished_actual_value.log`
- Error Message: `N/A`

### te_harmonic_regression_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/completed/2026-07-08-00-01-16_003_003_harmonic_regression_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__harmonic_regression__polished_actual_values/queue/003_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T00:32:21`
- End Time: `2026-07-08T00:46:14`
- Duration: `00:13:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/checkpoints/harmonic_regression-epoch=054-val_mae=0.00182643.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-00-01-16_dataset_input_mode_retraining__harmonic_regression__polished_actual_valu/logs/003_te_harmonic_regression_bw__polished_actual_value.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
