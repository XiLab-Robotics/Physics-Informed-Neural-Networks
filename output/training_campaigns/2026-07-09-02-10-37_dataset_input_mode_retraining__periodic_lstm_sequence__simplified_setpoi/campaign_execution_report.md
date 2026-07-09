# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints`
- Generated At: `2026-07-09T02:43:23`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-02-10-37_dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoi`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_001_001_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_global__simplified_setpoints` | `periodic_lstm_sequence` | `completed` | `00:09:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_002_002_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_fw__simplified_setpoints` | `periodic_lstm_sequence` | `completed` | `00:12:42` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_003_003_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_bw__simplified_setpoints` | `periodic_lstm_sequence` | `completed` | `00:10:59` |

## Run Details

### te_periodic_lstm_sequence_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_001_001_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/queue/001_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T02:10:37`
- End Time: `2026-07-09T02:19:42`
- Duration: `00:09:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=088-val_mae=0.00353329.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-02-10-37_dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoi/logs/001_te_periodic_lstm_sequence_global__simplified_set.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_002_002_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/queue/002_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T02:19:42`
- End Time: `2026-07-09T02:32:24`
- Duration: `00:12:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=095-val_mae=0.00348296.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-02-10-37_dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoi/logs/002_te_periodic_lstm_sequence_fw__simplified_setpoin.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/completed/2026-07-09-02-10-37_003_003_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints/queue/003_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T02:32:24`
- End Time: `2026-07-09T02:43:23`
- Duration: `00:10:59`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=074-val_mae=0.00352408.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-02-10-37_dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoi/logs/003_te_periodic_lstm_sequence_bw__simplified_setpoin.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
