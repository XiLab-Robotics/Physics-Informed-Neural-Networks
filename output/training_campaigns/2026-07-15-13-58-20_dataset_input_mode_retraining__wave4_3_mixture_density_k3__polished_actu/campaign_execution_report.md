# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values`
- Generated At: `2026-07-15T16:07:33`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-13-58-20_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actu`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_001_001_wave4_3_mixture_density_k3_global.yaml` | `te_wave4_3_mixture_density_k3_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:40:40` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_002_002_wave4_3_mixture_density_k3_fw.yaml` | `te_wave4_3_mixture_density_k3_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:00:36` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_003_003_wave4_3_mixture_density_k3_bw.yaml` | `te_wave4_3_mixture_density_k3_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:57` |

## Run Details

### te_wave4_3_mixture_density_k3_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_001_001_wave4_3_mixture_density_k3_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/queue/001_wave4_3_mixture_density_k3_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T13:58:20`
- End Time: `2026-07-15T14:39:00`
- Duration: `00:40:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=164-val_mae=0.00178681.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-13-58-20_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actu/logs/001_te_wave4_3_mixture_density_k3_global__polished_a.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_002_002_wave4_3_mixture_density_k3_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/queue/002_wave4_3_mixture_density_k3_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T14:39:00`
- End Time: `2026-07-15T15:39:35`
- Duration: `01:00:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00161545.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-13-58-20_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actu/logs/002_te_wave4_3_mixture_density_k3_fw__polished_actua.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/completed/2026-07-15-13-58-20_003_003_wave4_3_mixture_density_k3_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values/queue/003_wave4_3_mixture_density_k3_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T15:39:35`
- End Time: `2026-07-15T16:07:33`
- Duration: `00:27:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00181385.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-13-58-20_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actu/logs/003_te_wave4_3_mixture_density_k3_bw__polished_actua.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
