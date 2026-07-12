# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values`
- Generated At: `2026-07-12T13:51:11`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-11-35-23_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_ac`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_001_001_wave3_3_full_curve_composite_global.yaml` | `te_wave3_3_full_curve_composite_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:38:19` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_002_002_wave3_3_full_curve_composite_fw.yaml` | `te_wave3_3_full_curve_composite_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:55:37` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_003_003_wave3_3_full_curve_composite_bw.yaml` | `te_wave3_3_full_curve_composite_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:41:52` |

## Run Details

### te_wave3_3_full_curve_composite_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_001_001_wave3_3_full_curve_composite_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/queue/001_wave3_3_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-12T11:35:23`
- End Time: `2026-07-12T12:13:42`
- Duration: `00:38:19`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=131-val_mae=0.00200797.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-11-35-23_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_ac/logs/001_te_wave3_3_full_curve_composite_global__polished.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_002_002_wave3_3_full_curve_composite_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/queue/002_wave3_3_full_curve_composite_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-12T12:13:42`
- End Time: `2026-07-12T13:09:19`
- Duration: `00:55:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=211-val_mae=0.00198008.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-11-35-23_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_ac/logs/002_te_wave3_3_full_curve_composite_fw__polished_act.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/completed/2026-07-12-11-35-23_003_003_wave3_3_full_curve_composite_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values/queue/003_wave3_3_full_curve_composite_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-12T13:09:19`
- End Time: `2026-07-12T13:51:11`
- Duration: `00:41:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=143-val_mae=0.00194357.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-13-09-19__te_wave3_3_full_curve_composite_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-11-35-23_dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_ac/logs/003_te_wave3_3_full_curve_composite_bw__polished_act.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
