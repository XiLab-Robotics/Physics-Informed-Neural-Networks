# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Generated At: `2026-07-13T08:09:09`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-13-07-40-29_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_se`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `1`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/completed/2026-07-13-07-40-29_001_002_wave4_1_log_cosh_robust_loss_fw.yaml` | `te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:28:41` |

## Run Details

### te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/completed/2026-07-13-07-40-29_001_002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/queue/002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-13T07:40:29`
- End Time: `2026-07-13T08:09:09`
- Duration: `00:28:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=089-val_mae=0.00196005.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-07-40-29_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_se/logs/001_te_wave4_1_log_cosh_robust_loss_fw__polished_set.log.gz`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
