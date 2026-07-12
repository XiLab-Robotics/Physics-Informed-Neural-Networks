# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints`
- Generated At: `2026-07-12T23:59:37`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-22-20-41_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_s`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_001_001_wave4_1_smooth_l1_robust_loss_global.yaml` | `te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:39:33` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml` | `te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:26:00` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml` | `te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:23` |

## Run Details

### te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_001_001_wave4_1_smooth_l1_robust_loss_global.yaml`
- Source Config: `N/A`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T22:20:41`
- End Time: `2026-07-12T23:00:14`
- Duration: `00:39:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=143-val_mae=0.00190163.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-22-12-14__te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-22-20-41_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_s/logs/001_te_wave4_1_smooth_l1_robust_loss_global__polishe.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Source Config: `N/A`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T23:00:14`
- End Time: `2026-07-12T23:26:15`
- Duration: `00:26:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=079-val_mae=0.00192933.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-22-20-41_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_s/logs/002_te_wave4_1_smooth_l1_robust_loss_fw__polished_se.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints/completed/2026-07-12-22-12-14_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Source Config: `N/A`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T23:26:15`
- End Time: `2026-07-12T23:59:37`
- Duration: `00:33:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=115-val_mae=0.00193797.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-26-15__te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-22-20-41_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_s/logs/003_te_wave4_1_smooth_l1_robust_loss_bw__polished_se.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
