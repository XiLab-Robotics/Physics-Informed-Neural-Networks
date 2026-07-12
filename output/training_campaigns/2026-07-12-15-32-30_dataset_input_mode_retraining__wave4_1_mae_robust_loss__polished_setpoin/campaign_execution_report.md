# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints`
- Generated At: `2026-07-12T17:19:03`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-15-32-30_dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoin`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_001_001_wave4_1_mae_robust_loss_global.yaml` | `te_wave4_1_mae_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:47:04` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_002_002_wave4_1_mae_robust_loss_fw.yaml` | `te_wave4_1_mae_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:31:29` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_003_003_wave4_1_mae_robust_loss_bw.yaml` | `te_wave4_1_mae_robust_loss_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:59` |

## Run Details

### te_wave4_1_mae_robust_loss_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_001_001_wave4_1_mae_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/queue/001_wave4_1_mae_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T15:32:30`
- End Time: `2026-07-12T16:19:34`
- Duration: `00:47:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=178-val_mae=0.00178795.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-15-32-30_dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoin/logs/001_te_wave4_1_mae_robust_loss_global__polished_setp.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_002_002_wave4_1_mae_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/queue/002_wave4_1_mae_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T16:19:34`
- End Time: `2026-07-12T16:51:03`
- Duration: `00:31:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00179190.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-15-32-30_dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoin/logs/002_te_wave4_1_mae_robust_loss_fw__polished_setpoint.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/completed/2026-07-12-15-32-30_003_003_wave4_1_mae_robust_loss_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints/queue/003_wave4_1_mae_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T16:51:03`
- End Time: `2026-07-12T17:19:03`
- Duration: `00:27:59`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=088-val_mae=0.00183184.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-15-32-30_dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoin/logs/003_te_wave4_1_mae_robust_loss_bw__polished_setpoint.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
