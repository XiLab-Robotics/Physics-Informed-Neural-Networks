# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values`
- Generated At: `2026-07-11T21:32:35`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-19-14-45_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:56:16` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:30:54` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:50:41` |

## Run Details

### te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/queue/001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T19:14:45`
- End Time: `2026-07-11T20:11:00`
- Duration: `00:56:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=210-val_mae=0.00182815.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-19-14-45_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/001_te_wave3_3_raw_centered_shape_curve_aware_global.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/queue/002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T20:11:00`
- End Time: `2026-07-11T20:41:54`
- Duration: `00:30:54`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=095-val_mae=0.00193478.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-19-14-45_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/002_te_wave3_3_raw_centered_shape_curve_aware_fw__po.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/completed/2026-07-11-19-14-45_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values/queue/003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T20:41:54`
- End Time: `2026-07-11T21:32:35`
- Duration: `00:50:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=186-val_mae=0.00185514.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-19-14-45_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/003_te_wave3_3_raw_centered_shape_curve_aware_bw__po.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
