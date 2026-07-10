# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints`
- Generated At: `2026-07-10T08:58:58`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-08-11-44_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_001_001_wave3_1_sequential_residual_offset_probe_global.yaml` | `te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:13:12` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_002_002_wave3_1_sequential_residual_offset_probe_fw.yaml` | `te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:21:27` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_003_003_wave3_1_sequential_residual_offset_probe_bw.yaml` | `te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:12:34` |

## Run Details

### te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_001_001_wave3_1_sequential_residual_offset_probe_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/queue/001_wave3_1_sequential_residual_offset_probe_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T08:11:44`
- End Time: `2026-07-10T08:24:57`
- Duration: `00:13:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=095-val_mae=0.00372731.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-08-11-44_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/001_te_wave3_1_sequential_residual_offset_probe_glob.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_002_002_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/queue/002_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T08:24:57`
- End Time: `2026-07-10T08:46:24`
- Duration: `00:21:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=138-val_mae=0.00365466.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-08-11-44_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/002_te_wave3_1_sequential_residual_offset_probe_fw.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/completed/2026-07-10-08-11-44_003_003_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints/queue/003_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T08:46:24`
- End Time: `2026-07-10T08:58:58`
- Duration: `00:12:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=098-val_mae=0.00372763.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-08-11-44_dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe/logs/003_te_wave3_1_sequential_residual_offset_probe_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
