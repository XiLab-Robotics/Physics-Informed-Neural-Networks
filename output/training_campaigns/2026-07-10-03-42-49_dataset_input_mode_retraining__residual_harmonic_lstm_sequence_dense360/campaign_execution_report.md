# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints`
- Generated At: `2026-07-10T04:38:28`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-03-42-49_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml` | `te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:21:09` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:19:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:15:25` |

## Run Details

### te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/queue/001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T03:42:49`
- End Time: `2026-07-10T04:03:58`
- Duration: `00:21:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=055-val_mae=0.00360012.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-03-42-49_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/001_te_residual_harmonic_lstm_sequence_dense360_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/queue/002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T04:03:58`
- End Time: `2026-07-10T04:23:03`
- Duration: `00:19:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=047-val_mae=0.00358223.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-03-42-49_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/002_te_residual_harmonic_lstm_sequence_dense360_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/completed/2026-07-10-03-42-49_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints/queue/003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T04:23:03`
- End Time: `2026-07-10T04:38:28`
- Duration: `00:15:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=030-val_mae=0.00360440.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-03-42-49_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/003_te_residual_harmonic_lstm_sequence_dense360_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
