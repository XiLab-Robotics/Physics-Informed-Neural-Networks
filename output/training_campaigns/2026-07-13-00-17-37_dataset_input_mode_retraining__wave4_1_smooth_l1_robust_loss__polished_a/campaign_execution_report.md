# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values`
- Generated At: `2026-07-13T02:22:44`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-13-00-17-37_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_a`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_001_001_wave4_1_smooth_l1_robust_loss_global.yaml` | `te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:36:44` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml` | `te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:56:18` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml` | `te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:04` |

## Run Details

### te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_001_001_wave4_1_smooth_l1_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/queue/001_wave4_1_smooth_l1_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T00:17:37`
- End Time: `2026-07-13T00:54:21`
- Duration: `00:36:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=151-val_mae=0.00188208.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-00-17-37_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_a/logs/001_te_wave4_1_smooth_l1_robust_loss_global__polishe.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/queue/002_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T00:54:21`
- End Time: `2026-07-13T01:50:39`
- Duration: `00:56:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=218-val_mae=0.00183482.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-00-17-37_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_a/logs/002_te_wave4_1_smooth_l1_robust_loss_fw__polished_ac.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/completed/2026-07-13-00-17-37_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values/queue/003_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T01:50:39`
- End Time: `2026-07-13T02:22:44`
- Duration: `00:32:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=128-val_mae=0.00189374.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-00-17-37_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_a/logs/003_te_wave4_1_smooth_l1_robust_loss_bw__polished_ac.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
