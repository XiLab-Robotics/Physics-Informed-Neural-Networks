# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values`
- Generated At: `2026-07-10T23:01:43`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-21-34-26_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_001_001_wave3_2_clean_sequential_residual_offset_global.yaml` | `te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:31:42` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_002_002_wave3_2_clean_sequential_residual_offset_fw.yaml` | `te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:30:55` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_003_003_wave3_2_clean_sequential_residual_offset_bw.yaml` | `te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:24:39` |

## Run Details

### te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_001_001_wave3_2_clean_sequential_residual_offset_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/queue/001_wave3_2_clean_sequential_residual_offset_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T21:34:26`
- End Time: `2026-07-10T22:06:08`
- Duration: `00:31:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=151-val_mae=0.00216362.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-21-34-26_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/001_te_wave3_2_clean_sequential_residual_offset_glob.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_002_002_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/queue/002_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T22:06:08`
- End Time: `2026-07-10T22:37:03`
- Duration: `00:30:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=153-val_mae=0.00216939.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-21-34-26_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/002_te_wave3_2_clean_sequential_residual_offset_fw.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/completed/2026-07-10-21-34-26_003_003_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values/queue/003_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T22:37:04`
- End Time: `2026-07-10T23:01:43`
- Duration: `00:24:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=127-val_mae=0.00219453.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-21-34-26_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/003_te_wave3_2_clean_sequential_residual_offset_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
