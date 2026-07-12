# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints`
- Generated At: `2026-07-12T11:21:56`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-09-42-30_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_se`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_001_001_wave3_3_full_curve_composite_global.yaml` | `te_wave3_3_full_curve_composite_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:40:00` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_002_002_wave3_3_full_curve_composite_fw.yaml` | `te_wave3_3_full_curve_composite_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:51` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_003_003_wave3_3_full_curve_composite_bw.yaml` | `te_wave3_3_full_curve_composite_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:26:34` |

## Run Details

### te_wave3_3_full_curve_composite_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_001_001_wave3_3_full_curve_composite_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/queue/001_wave3_3_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T09:42:30`
- End Time: `2026-07-12T10:22:30`
- Duration: `00:40:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=139-val_mae=0.00205804.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-09-42-30_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_se/logs/001_te_wave3_3_full_curve_composite_global__polished.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_002_002_wave3_3_full_curve_composite_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/queue/002_wave3_3_full_curve_composite_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T10:22:30`
- End Time: `2026-07-12T10:55:22`
- Duration: `00:32:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=107-val_mae=0.00203018.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-09-42-30_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_se/logs/002_te_wave3_3_full_curve_composite_fw__polished_set.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/completed/2026-07-12-09-42-30_003_003_wave3_3_full_curve_composite_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints/queue/003_wave3_3_full_curve_composite_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T10:55:22`
- End Time: `2026-07-12T11:21:55`
- Duration: `00:26:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=078-val_mae=0.00203714.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-55-22__te_wave3_3_full_curve_composite_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-09-42-30_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_se/logs/003_te_wave3_3_full_curve_composite_bw__polished_set.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
