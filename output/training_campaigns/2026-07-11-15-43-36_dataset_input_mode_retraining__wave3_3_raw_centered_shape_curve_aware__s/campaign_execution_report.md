# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints`
- Generated At: `2026-07-11T17:14:11`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-15-43-36_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__s`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:29:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:29:49` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:31:35` |

## Run Details

### te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/queue/001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T15:43:36`
- End Time: `2026-07-11T16:12:47`
- Duration: `00:29:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=114-val_mae=0.00357026.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-15-43-36_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__s/logs/001_te_wave3_3_raw_centered_shape_curve_aware_global.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/queue/002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T16:12:47`
- End Time: `2026-07-11T16:42:36`
- Duration: `00:29:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=119-val_mae=0.00356710.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-15-43-36_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__s/logs/002_te_wave3_3_raw_centered_shape_curve_aware_fw__si.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/completed/2026-07-11-15-43-36_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints/queue/003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T16:42:36`
- End Time: `2026-07-11T17:14:11`
- Duration: `00:31:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00357800.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-15-43-36_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__s/logs/003_te_wave3_3_raw_centered_shape_curve_aware_bw__si.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
