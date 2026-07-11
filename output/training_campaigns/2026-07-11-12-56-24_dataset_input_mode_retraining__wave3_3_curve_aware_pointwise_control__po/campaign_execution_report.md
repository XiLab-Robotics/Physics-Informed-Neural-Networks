# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values`
- Generated At: `2026-07-11T15:28:19`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-12-56-24_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__po`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_001_001_wave3_3_curve_aware_pointwise_control_global.yaml` | `te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:50:15` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_002_002_wave3_3_curve_aware_pointwise_control_fw.yaml` | `te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:57:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_003_003_wave3_3_curve_aware_pointwise_control_bw.yaml` | `te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:44:29` |

## Run Details

### te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_001_001_wave3_3_curve_aware_pointwise_control_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/queue/001_wave3_3_curve_aware_pointwise_control_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T12:56:24`
- End Time: `2026-07-11T13:46:39`
- Duration: `00:50:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=199-val_mae=0.00185032.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-12-56-24_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__po/logs/001_te_wave3_3_curve_aware_pointwise_control_global.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_002_002_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/queue/002_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T13:46:39`
- End Time: `2026-07-11T14:43:50`
- Duration: `00:57:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00183289.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-12-56-24_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__po/logs/002_te_wave3_3_curve_aware_pointwise_control_fw__pol.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/completed/2026-07-11-12-56-24_003_003_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values/queue/003_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T14:43:50`
- End Time: `2026-07-11T15:28:19`
- Duration: `00:44:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=175-val_mae=0.00184976.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-12-56-24_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__po/logs/003_te_wave3_3_curve_aware_pointwise_control_bw__pol.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
