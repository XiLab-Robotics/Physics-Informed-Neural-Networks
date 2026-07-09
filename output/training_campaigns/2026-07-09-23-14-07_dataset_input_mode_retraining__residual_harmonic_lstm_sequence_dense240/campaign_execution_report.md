# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints`
- Generated At: `2026-07-10T00:20:55`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-23-14-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_001_001_residual_harmonic_lstm_sequence_dense240_global.yaml` | `te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:17:53` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_002_002_residual_harmonic_lstm_sequence_dense240_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:21:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_003_003_residual_harmonic_lstm_sequence_dense240_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:27:02` |

## Run Details

### te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_001_001_residual_harmonic_lstm_sequence_dense240_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/queue/001_residual_harmonic_lstm_sequence_dense240_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T23:14:07`
- End Time: `2026-07-09T23:32:01`
- Duration: `00:17:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=042-val_mae=0.00360357.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-23-14-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240/logs/001_te_residual_harmonic_lstm_sequence_dense240_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_002_002_residual_harmonic_lstm_sequence_dense240_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/queue/002_residual_harmonic_lstm_sequence_dense240_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T23:32:01`
- End Time: `2026-07-09T23:53:53`
- Duration: `00:21:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=061-val_mae=0.00356071.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-23-14-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240/logs/002_te_residual_harmonic_lstm_sequence_dense240_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/completed/2026-07-09-23-14-07_003_003_residual_harmonic_lstm_sequence_dense240_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints/queue/003_residual_harmonic_lstm_sequence_dense240_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T23:53:53`
- End Time: `2026-07-10T00:20:55`
- Duration: `00:27:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=087-val_mae=0.00358639.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-23-14-07_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240/logs/003_te_residual_harmonic_lstm_sequence_dense240_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
