# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values`
- Generated At: `2026-07-10T12:18:02`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-10-48-41_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_001_001_wave3_1_sequential_residual_offset_probe_global.yaml` | `te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:20:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_002_002_wave3_1_sequential_residual_offset_probe_fw.yaml` | `te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:25:45` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_003_003_wave3_1_sequential_residual_offset_probe_bw.yaml` | `te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values` | `sequential_residual_offset_probe` | `completed` | `00:42:44` |

## Run Details

### te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_001_001_wave3_1_sequential_residual_offset_probe_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/queue/001_wave3_1_sequential_residual_offset_probe_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T10:48:41`
- End Time: `2026-07-10T11:09:33`
- Duration: `00:20:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=077-val_mae=0.00220916.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-10-48-41_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/001_te_wave3_1_sequential_residual_offset_probe_glob.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_002_002_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/queue/002_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T11:09:33`
- End Time: `2026-07-10T11:35:18`
- Duration: `00:25:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=097-val_mae=0.00219045.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-09-33__te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-10-48-41_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/002_te_wave3_1_sequential_residual_offset_probe_fw.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/completed/2026-07-10-10-48-41_003_003_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values/queue/003_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T11:35:18`
- End Time: `2026-07-10T12:18:02`
- Duration: `00:42:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=197-val_mae=0.00215382.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-10-48-41_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/003_te_wave3_1_sequential_residual_offset_probe_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
