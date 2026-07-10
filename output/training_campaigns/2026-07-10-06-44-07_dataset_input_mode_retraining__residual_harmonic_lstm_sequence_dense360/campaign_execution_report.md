# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values`
- Generated At: `2026-07-10T07:56:39`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-06-44-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml` | `te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:15:32` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:25:12` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:31:48` |

## Run Details

### te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/queue/001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T06:44:07`
- End Time: `2026-07-10T06:59:39`
- Duration: `00:15:32`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=018-val_mae=0.00209241.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-06-44-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/001_te_residual_harmonic_lstm_sequence_dense360_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/queue/002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T06:59:39`
- End Time: `2026-07-10T07:24:50`
- Duration: `00:25:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=062-val_mae=0.00203211.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-06-44-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/002_te_residual_harmonic_lstm_sequence_dense360_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/completed/2026-07-10-06-44-07_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values/queue/003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-10T07:24:50`
- End Time: `2026-07-10T07:56:39`
- Duration: `00:31:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=105-val_mae=0.00199856.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-06-44-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/003_te_residual_harmonic_lstm_sequence_dense360_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
