# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values`
- Generated At: `2026-07-16T03:36:03`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-16-02-19-49_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_001_001_wave5_1_harmonic_prior_pointwise_control_global.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:24:43` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_002_002_wave5_1_harmonic_prior_pointwise_control_fw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:23:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_003_003_wave5_1_harmonic_prior_pointwise_control_bw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:27:56` |

## Run Details

### te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_001_001_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/queue/001_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T02:19:49`
- End Time: `2026-07-16T02:44:33`
- Duration: `00:24:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=121-val_mae=0.00194574.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-19-49__te_wave5_1_harmonic_prior_pointwise_control_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-02-19-49_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/001_te_wave5_1_harmonic_prior_pointwise_control_glob.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_002_002_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/queue/002_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T02:44:33`
- End Time: `2026-07-16T03:08:07`
- Duration: `00:23:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=119-val_mae=0.00192899.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-02-44-33__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-02-19-49_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/002_te_wave5_1_harmonic_prior_pointwise_control_fw.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/completed/2026-07-16-02-19-49_003_003_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values/queue/003_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T03:08:07`
- End Time: `2026-07-16T03:36:03`
- Duration: `00:27:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=113-val_mae=0.00189638.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-02-19-49_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/003_te_wave5_1_harmonic_prior_pointwise_control_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
