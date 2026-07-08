# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints`
- Generated At: `2026-07-08T15:36:15`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-14-59-31_dataset_input_mode_retraining__lstm_sequence__simplified_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_001_001_lstm_sequence_global.yaml` | `te_lstm_sequence_global__simplified_setpoints` | `lstm_sequence` | `completed` | `00:14:41` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_002_002_lstm_sequence_fw.yaml` | `te_lstm_sequence_fw__simplified_setpoints` | `lstm_sequence` | `completed` | `00:09:50` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_003_003_lstm_sequence_bw.yaml` | `te_lstm_sequence_bw__simplified_setpoints` | `lstm_sequence` | `completed` | `00:12:12` |

## Run Details

### te_lstm_sequence_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_001_001_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/queue/001_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T14:59:31`
- End Time: `2026-07-08T15:14:13`
- Duration: `00:14:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/checkpoints/lstm_sequence-epoch=115-val_mae=0.00369210.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-14-59-31_dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/logs/001_te_lstm_sequence_global__simplified_setpoints.log`
- Error Message: `N/A`

### te_lstm_sequence_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_002_002_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/queue/002_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T15:14:13`
- End Time: `2026-07-08T15:24:03`
- Duration: `00:09:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/checkpoints/lstm_sequence-epoch=092-val_mae=0.00370236.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-14-59-31_dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/logs/002_te_lstm_sequence_fw__simplified_setpoints.log`
- Error Message: `N/A`

### te_lstm_sequence_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/completed/2026-07-08-14-59-31_003_003_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/queue/003_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T15:24:03`
- End Time: `2026-07-08T15:36:15`
- Duration: `00:12:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/checkpoints/lstm_sequence-epoch=091-val_mae=0.00367749.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-14-59-31_dataset_input_mode_retraining__lstm_sequence__simplified_setpoints/logs/003_te_lstm_sequence_bw__simplified_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
