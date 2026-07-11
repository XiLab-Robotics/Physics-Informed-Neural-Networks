# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints`
- Generated At: `2026-07-11T08:50:56`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-07-21-26_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__si`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_001_001_wave3_3_curve_aware_pointwise_control_global.yaml` | `te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:35:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_002_002_wave3_3_curve_aware_pointwise_control_fw.yaml` | `te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:26:58` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_003_003_wave3_3_curve_aware_pointwise_control_bw.yaml` | `te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:25` |

## Run Details

### te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_001_001_wave3_3_curve_aware_pointwise_control_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/queue/001_wave3_3_curve_aware_pointwise_control_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T07:21:26`
- End Time: `2026-07-11T07:56:33`
- Duration: `00:35:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=139-val_mae=0.00358483.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-07-21-26_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__si/logs/001_te_wave3_3_curve_aware_pointwise_control_global.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_002_002_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/queue/002_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T07:56:33`
- End Time: `2026-07-11T08:23:30`
- Duration: `00:26:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=099-val_mae=0.00361775.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-07-21-26_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__si/logs/002_te_wave3_3_curve_aware_pointwise_control_fw__sim.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/completed/2026-07-11-07-21-26_003_003_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints/queue/003_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T08:23:30`
- End Time: `2026-07-11T08:50:55`
- Duration: `00:27:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00363045.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-07-21-26_dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__si/logs/003_te_wave3_3_curve_aware_pointwise_control_bw__sim.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
