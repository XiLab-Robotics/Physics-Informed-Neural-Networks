# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints`
- Generated At: `2026-07-11T23:35:05`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-21-48-20_dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplifie`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_001_001_wave3_3_raw_offset_curve_aware_global.yaml` | `te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:38:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_002_002_wave3_3_raw_offset_curve_aware_fw.yaml` | `te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:23` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_003_003_wave3_3_raw_offset_curve_aware_bw.yaml` | `te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:35:17` |

## Run Details

### te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_001_001_wave3_3_raw_offset_curve_aware_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/queue/001_wave3_3_raw_offset_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T21:48:20`
- End Time: `2026-07-11T22:26:25`
- Duration: `00:38:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=159-val_mae=0.00354446.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-21-48-20_dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplifie/logs/001_te_wave3_3_raw_offset_curve_aware_global__simpli.log`
- Error Message: `N/A`

### te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_002_002_wave3_3_raw_offset_curve_aware_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/queue/002_wave3_3_raw_offset_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T22:26:25`
- End Time: `2026-07-11T22:59:48`
- Duration: `00:33:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=132-val_mae=0.00358121.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-21-48-20_dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplifie/logs/002_te_wave3_3_raw_offset_curve_aware_fw__simplified.log`
- Error Message: `N/A`

### te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/completed/2026-07-11-21-48-20_003_003_wave3_3_raw_offset_curve_aware_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints/queue/003_wave3_3_raw_offset_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T22:59:48`
- End Time: `2026-07-11T23:35:05`
- Duration: `00:35:17`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=145-val_mae=0.00357142.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-21-48-20_dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplifie/logs/003_te_wave3_3_raw_offset_curve_aware_bw__simplified.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
