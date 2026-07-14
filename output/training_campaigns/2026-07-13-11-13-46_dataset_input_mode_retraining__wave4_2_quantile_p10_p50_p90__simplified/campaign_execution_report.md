# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Generated At: `2026-07-13T12:03:07`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-13-11-13-46_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `2`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_001_001_wave4_2_quantile_p10_p50_p90_global.yaml` | `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:22:07` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml` | `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:14` |

## Run Details

### te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_001_001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/queue/001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-13T11:13:46`
- End Time: `2026-07-13T11:35:53`
- Duration: `00:22:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=091-val_mae=0.00353725.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-11-13-46_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/001_te_wave4_2_quantile_p10_p50_p90_global__simplifi.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/queue/002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-13T11:35:53`
- End Time: `2026-07-13T12:03:07`
- Duration: `00:27:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00355780.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-11-13-46_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/002_te_wave4_2_quantile_p10_p50_p90_fw__simplified_s.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
