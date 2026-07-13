# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values`
- Generated At: `2026-07-13T10:57:02`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-13-09-01-50_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_ac`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_001_001_wave4_1_log_cosh_robust_loss_global.yaml` | `te_wave4_1_log_cosh_robust_loss_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:48` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_002_002_wave4_1_log_cosh_robust_loss_fw.yaml` | `te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:49:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_003_003_wave4_1_log_cosh_robust_loss_bw.yaml` | `te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:18` |

## Run Details

### te_wave4_1_log_cosh_robust_loss_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_001_001_wave4_1_log_cosh_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/queue/001_wave4_1_log_cosh_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T09:01:50`
- End Time: `2026-07-13T09:34:38`
- Duration: `00:32:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=110-val_mae=0.00189902.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-09-01-50_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_ac/logs/001_te_wave4_1_log_cosh_robust_loss_global__polished.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_002_002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/queue/002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T09:34:38`
- End Time: `2026-07-13T10:23:44`
- Duration: `00:49:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=193-val_mae=0.00182691.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-09-01-50_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_ac/logs/002_te_wave4_1_log_cosh_robust_loss_fw__polished_act.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/completed/2026-07-13-09-01-50_003_003_wave4_1_log_cosh_robust_loss_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values/queue/003_wave4_1_log_cosh_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-13T10:23:44`
- End Time: `2026-07-13T10:57:02`
- Duration: `00:33:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=127-val_mae=0.00187102.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-09-01-50_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_ac/logs/003_te_wave4_1_log_cosh_robust_loss_bw__polished_act.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
