# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints`
- Generated At: `2026-07-09T16:29:19`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-15-18-00_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_001_001_residual_harmonic_gru_sequence_dense360_global.yaml` | `te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:27:26` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml` | `te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:25:17` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml` | `te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:18:35` |

## Run Details

### te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_001_001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/queue/001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T15:18:00`
- End Time: `2026-07-09T15:45:26`
- Duration: `00:27:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=111-val_mae=0.00197378.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-15-18-00_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/001_te_residual_harmonic_gru_sequence_dense360_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/queue/002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T15:45:26`
- End Time: `2026-07-09T16:10:44`
- Duration: `00:25:17`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=120-val_mae=0.00200154.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-45-26__te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-15-18-00_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/002_te_residual_harmonic_gru_sequence_dense360_fw__p.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/completed/2026-07-09-15-18-00_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints/queue/003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T16:10:44`
- End Time: `2026-07-09T16:29:19`
- Duration: `00:18:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=064-val_mae=0.00200024.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-15-18-00_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/003_te_residual_harmonic_gru_sequence_dense360_bw__p.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
