# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values`
- Generated At: `2026-07-16T07:23:05`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-16-06-16-41_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_001_001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:23:13` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_002_002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:17:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_003_003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values` | `wave3_harmonic_prior_residual` | `completed` | `00:26:00` |

## Run Details

### te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_001_001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/queue/001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T06:16:41`
- End Time: `2026-07-16T06:39:53`
- Duration: `00:23:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=086-val_mae=0.00190146.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-16-41__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-06-16-41_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/001_te_wave5_1_harmonic_prior_smooth_l1_structured_g.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_002_002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/queue/002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T06:39:53`
- End Time: `2026-07-16T06:57:05`
- Duration: `00:17:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=071-val_mae=0.00193329.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-39-53__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-06-16-41_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/002_te_wave5_1_harmonic_prior_smooth_l1_structured_f.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/completed/2026-07-16-06-16-41_003_003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_actual_values/queue/003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-16T06:57:05`
- End Time: `2026-07-16T07:23:05`
- Duration: `00:26:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values/checkpoints/wave3_harmonic_prior_residual-epoch=101-val_mae=0.00192977.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-06-57-05__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-06-16-41_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/003_te_wave5_1_harmonic_prior_smooth_l1_structured_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
