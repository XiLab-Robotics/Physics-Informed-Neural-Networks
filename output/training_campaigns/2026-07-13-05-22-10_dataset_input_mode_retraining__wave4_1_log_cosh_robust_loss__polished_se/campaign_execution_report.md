# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Generated At: `2026-07-13T06:03:01`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-13-05-22-10_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_se`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `1`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/completed/2026-07-13-05-22-10_001_001_wave4_1_log_cosh_robust_loss_global.yaml` | `te_wave4_1_log_cosh_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:39:50` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/failed/2026-07-13-05-22-10_002_002_wave4_1_log_cosh_robust_loss_fw.yaml` | `te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `failed` | `00:01:01` |

## Run Details

### te_wave4_1_log_cosh_robust_loss_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/completed/2026-07-13-05-22-10_001_001_wave4_1_log_cosh_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/queue/001_wave4_1_log_cosh_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-13T05:22:10`
- End Time: `2026-07-13T06:02:00`
- Duration: `00:39:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=155-val_mae=0.00191211.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-13-05-22-10_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_se/logs/001_te_wave4_1_log_cosh_robust_loss_global__polished.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/failed/2026-07-13-05-22-10_002_002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints/queue/002_wave4_1_log_cosh_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-06-02-00__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints`
- Queue Status: `failed`
- Start Time: `2026-07-13T06:02:00`
- End Time: `2026-07-13T06:03:01`
- Duration: `00:01:01`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-06-02-00__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-06-02-00__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-07-13-05-22-10_dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_se/logs/002_te_wave4_1_log_cosh_robust_loss_fw__polished_set.log`
- Error Message: `[Errno 28] No space left on device`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
