# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values`
- Generated At: `2026-07-09T18:18:10`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-16-52-22_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_001_001_residual_harmonic_gru_sequence_dense360_global.yaml` | `te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:26:15` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml` | `te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:30:31` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml` | `te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:29:02` |

## Run Details

### te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_001_001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/queue/001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T16:52:22`
- End Time: `2026-07-09T17:18:37`
- Duration: `00:26:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=134-val_mae=0.00196008.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-52-22__te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-16-52-22_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/001_te_residual_harmonic_gru_sequence_dense360_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/queue/002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T17:18:37`
- End Time: `2026-07-09T17:49:07`
- Duration: `00:30:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=156-val_mae=0.00195537.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-16-52-22_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/002_te_residual_harmonic_gru_sequence_dense360_fw__p.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/completed/2026-07-09-16-52-22_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values/queue/003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T17:49:07`
- End Time: `2026-07-09T18:18:10`
- Duration: `00:29:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=116-val_mae=0.00195966.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-16-52-22_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/003_te_residual_harmonic_gru_sequence_dense360_bw__p.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
