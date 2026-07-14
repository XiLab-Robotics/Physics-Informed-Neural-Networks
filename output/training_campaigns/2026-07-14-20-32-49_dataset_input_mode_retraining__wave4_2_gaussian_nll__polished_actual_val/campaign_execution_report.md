# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values`
- Generated At: `2026-07-14T22:39:07`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-20-32-49_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_val`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_001_001_wave4_2_gaussian_nll_global.yaml` | `te_wave4_2_gaussian_nll_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:10:10` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_002_002_wave4_2_gaussian_nll_fw.yaml` | `te_wave4_2_gaussian_nll_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:57:47` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_003_003_wave4_2_gaussian_nll_bw.yaml` | `te_wave4_2_gaussian_nll_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:58:20` |

## Run Details

### te_wave4_2_gaussian_nll_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_001_001_wave4_2_gaussian_nll_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/queue/001_wave4_2_gaussian_nll_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T20:32:49`
- End Time: `2026-07-14T20:42:59`
- Duration: `00:10:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.10197201.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-20-32-49_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_val/logs/001_te_wave4_2_gaussian_nll_global__polished_actual.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_002_002_wave4_2_gaussian_nll_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/queue/002_wave4_2_gaussian_nll_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T20:42:59`
- End Time: `2026-07-14T21:40:47`
- Duration: `00:57:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=258-val_mae=0.00181578.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-20-32-49_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_val/logs/002_te_wave4_2_gaussian_nll_fw__polished_actual_valu.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/completed/2026-07-14-20-32-49_003_003_wave4_2_gaussian_nll_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values/queue/003_wave4_2_gaussian_nll_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-14T21:40:47`
- End Time: `2026-07-14T22:39:07`
- Duration: `00:58:20`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=255-val_mae=0.00180572.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-21-40-47__te_wave4_2_gaussian_nll_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-20-32-49_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_val/logs/003_te_wave4_2_gaussian_nll_bw__polished_actual_valu.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
