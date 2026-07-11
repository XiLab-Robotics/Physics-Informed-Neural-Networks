# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints`
- Generated At: `2026-07-11T19:01:38`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-17-26-29_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:34:33` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:24:21` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:36:15` |

## Run Details

### te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_001_001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/queue/001_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T17:26:29`
- End Time: `2026-07-11T18:01:02`
- Duration: `00:34:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=112-val_mae=0.00195150.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-17-26-29_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/001_te_wave3_3_raw_centered_shape_curve_aware_global.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_002_002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/queue/002_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T18:01:02`
- End Time: `2026-07-11T18:25:23`
- Duration: `00:24:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=068-val_mae=0.00194145.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-17-26-29_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/002_te_wave3_3_raw_centered_shape_curve_aware_fw__po.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/completed/2026-07-11-17-26-29_003_003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints/queue/003_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T18:25:23`
- End Time: `2026-07-11T19:01:38`
- Duration: `00:36:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=121-val_mae=0.00193931.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-17-26-29_dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__p/logs/003_te_wave3_3_raw_centered_shape_curve_aware_bw__po.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
