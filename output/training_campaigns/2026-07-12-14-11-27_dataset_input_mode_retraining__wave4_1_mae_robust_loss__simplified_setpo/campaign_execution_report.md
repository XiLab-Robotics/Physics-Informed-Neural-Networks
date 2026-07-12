# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints`
- Generated At: `2026-07-12T15:20:40`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-14-11-27_dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpo`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_001_001_wave4_1_mae_robust_loss_global.yaml` | `te_wave4_1_mae_robust_loss_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:29:25` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_002_002_wave4_1_mae_robust_loss_fw.yaml` | `te_wave4_1_mae_robust_loss_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:17:35` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_003_003_wave4_1_mae_robust_loss_bw.yaml` | `te_wave4_1_mae_robust_loss_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:22:13` |

## Run Details

### te_wave4_1_mae_robust_loss_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_001_001_wave4_1_mae_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/queue/001_wave4_1_mae_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T14:11:27`
- End Time: `2026-07-12T14:40:52`
- Duration: `00:29:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=143-val_mae=0.00355510.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-14-11-27_dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpo/logs/001_te_wave4_1_mae_robust_loss_global__simplified_se.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_002_002_wave4_1_mae_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/queue/002_wave4_1_mae_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T14:40:52`
- End Time: `2026-07-12T14:58:27`
- Duration: `00:17:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=085-val_mae=0.00364418.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-14-11-27_dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpo/logs/002_te_wave4_1_mae_robust_loss_fw__simplified_setpoi.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/completed/2026-07-12-14-11-27_003_003_wave4_1_mae_robust_loss_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints/queue/003_wave4_1_mae_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T14:58:28`
- End Time: `2026-07-12T15:20:40`
- Duration: `00:22:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=073-val_mae=0.00358581.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-14-11-27_dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpo/logs/003_te_wave4_1_mae_robust_loss_bw__simplified_setpoi.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
