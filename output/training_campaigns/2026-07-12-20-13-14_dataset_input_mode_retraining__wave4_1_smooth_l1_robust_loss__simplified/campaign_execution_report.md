# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints`
- Generated At: `2026-07-12T21:30:59`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-20-13-14_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_001_001_wave4_1_smooth_l1_robust_loss_global.yaml` | `te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:24:55` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml` | `te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:24:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml` | `te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:28:15` |

## Run Details

### te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_001_001_wave4_1_smooth_l1_robust_loss_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/queue/001_wave4_1_smooth_l1_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T20:13:14`
- End Time: `2026-07-12T20:38:09`
- Duration: `00:24:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=087-val_mae=0.00364010.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-20-13-14_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified/logs/001_te_wave4_1_smooth_l1_robust_loss_global__simplif.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_002_002_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/queue/002_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T20:38:09`
- End Time: `2026-07-12T21:02:43`
- Duration: `00:24:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=086-val_mae=0.00353570.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-20-13-14_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified/logs/002_te_wave4_1_smooth_l1_robust_loss_fw__simplified.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/completed/2026-07-12-20-13-14_003_003_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints/queue/003_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T21:02:43`
- End Time: `2026-07-12T21:30:59`
- Duration: `00:28:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=142-val_mae=0.00357827.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-20-13-14_dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified/logs/003_te_wave4_1_smooth_l1_robust_loss_bw__simplified.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
