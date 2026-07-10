# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints`
- Generated At: `2026-07-10T06:25:15`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-04-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml` | `te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:33:55` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:23:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:33:59` |

## Run Details

### te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_001_001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/queue/001_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T04:53:57`
- End Time: `2026-07-10T05:27:52`
- Duration: `00:33:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=101-val_mae=0.00197679.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-04-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/001_te_residual_harmonic_lstm_sequence_dense360_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_002_002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/queue/002_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T05:27:52`
- End Time: `2026-07-10T05:51:16`
- Duration: `00:23:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=089-val_mae=0.00201259.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-27-52__te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-04-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/002_te_residual_harmonic_lstm_sequence_dense360_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/completed/2026-07-10-04-53-57_003_003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints/queue/003_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T05:51:16`
- End Time: `2026-07-10T06:25:15`
- Duration: `00:33:59`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=102-val_mae=0.00199077.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-04-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360/logs/003_te_residual_harmonic_lstm_sequence_dense360_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
