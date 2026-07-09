# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints`
- Generated At: `2026-07-09T11:29:46`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-10-32-04_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_001_001_residual_harmonic_gru_sequence_dense240_global.yaml` | `te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:20:12` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_002_002_residual_harmonic_gru_sequence_dense240_fw.yaml` | `te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:19:53` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_003_003_residual_harmonic_gru_sequence_dense240_bw.yaml` | `te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:17:37` |

## Run Details

### te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_001_001_residual_harmonic_gru_sequence_dense240_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/queue/001_residual_harmonic_gru_sequence_dense240_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T10:32:04`
- End Time: `2026-07-09T10:52:16`
- Duration: `00:20:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=081-val_mae=0.00198647.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-32-04__te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-10-32-04_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240/logs/001_te_residual_harmonic_gru_sequence_dense240_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_002_002_residual_harmonic_gru_sequence_dense240_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/queue/002_residual_harmonic_gru_sequence_dense240_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T10:52:16`
- End Time: `2026-07-09T11:12:09`
- Duration: `00:19:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=110-val_mae=0.00198772.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-10-32-04_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240/logs/002_te_residual_harmonic_gru_sequence_dense240_fw__p.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/completed/2026-07-09-10-32-04_003_003_residual_harmonic_gru_sequence_dense240_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints/queue/003_residual_harmonic_gru_sequence_dense240_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T11:12:09`
- End Time: `2026-07-09T11:29:46`
- Duration: `00:17:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=069-val_mae=0.00196095.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-10-32-04_dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240/logs/003_te_residual_harmonic_gru_sequence_dense240_bw__p.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
