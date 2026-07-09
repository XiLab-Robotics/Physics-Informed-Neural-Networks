# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints`
- Generated At: `2026-07-09T14:03:54`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-13-30-19_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_001_001_residual_harmonic_gru_sequence_dense360_global.yaml` | `te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:10:28` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml` | `te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:11:42` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml` | `te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:11:25` |

## Run Details

### te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_001_001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/queue/001_residual_harmonic_gru_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T13:30:19`
- End Time: `2026-07-09T13:40:47`
- Duration: `00:10:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=090-val_mae=0.00360722.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-13-30-19_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/001_te_residual_harmonic_gru_sequence_dense360_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_002_002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/queue/002_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T13:40:47`
- End Time: `2026-07-09T13:52:29`
- Duration: `00:11:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=081-val_mae=0.00358186.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-40-47__te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-13-30-19_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/002_te_residual_harmonic_gru_sequence_dense360_fw__s.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/completed/2026-07-09-13-30-19_003_003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints/queue/003_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T13:52:29`
- End Time: `2026-07-09T14:03:54`
- Duration: `00:11:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=077-val_mae=0.00358806.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-13-30-19_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360/logs/003_te_residual_harmonic_gru_sequence_dense360_bw__s.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
