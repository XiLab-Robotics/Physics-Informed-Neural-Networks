# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values`
- Generated At: `2026-07-14T17:40:46`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-15-32-15_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_ac`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_001_001_wave4_2_quantile_p10_p50_p90_global.yaml` | `te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:42:47` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml` | `te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:56:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml` | `te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:29:32` |

## Run Details

### te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_001_001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/queue/001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T15:32:15`
- End Time: `2026-07-14T16:15:03`
- Duration: `00:42:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=180-val_mae=0.00177392.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-15-32-15_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_ac/logs/001_te_wave4_2_quantile_p10_p50_p90_global__polished.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/queue/002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T16:15:03`
- End Time: `2026-07-14T17:11:13`
- Duration: `00:56:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=250-val_mae=0.00176755.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-15-32-15_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_ac/logs/002_te_wave4_2_quantile_p10_p50_p90_fw__polished_act.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/completed/2026-07-14-15-32-15_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values/queue/003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T17:11:13`
- End Time: `2026-07-14T17:40:45`
- Duration: `00:29:32`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=123-val_mae=0.00178818.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-15-32-15_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_ac/logs/003_te_wave4_2_quantile_p10_p50_p90_bw__polished_act.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
