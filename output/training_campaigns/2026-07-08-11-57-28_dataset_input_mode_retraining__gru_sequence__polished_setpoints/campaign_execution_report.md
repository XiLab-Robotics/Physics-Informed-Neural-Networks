# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__polished_setpoints`
- Generated At: `2026-07-08T13:03:44`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-11-57-28_dataset_input_mode_retraining__gru_sequence__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_001_001_gru_sequence_global.yaml` | `te_gru_sequence_global__polished_setpoints` | `gru_sequence` | `completed` | `00:20:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_002_002_gru_sequence_fw.yaml` | `te_gru_sequence_fw__polished_setpoints` | `gru_sequence` | `completed` | `00:29:18` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_003_003_gru_sequence_bw.yaml` | `te_gru_sequence_bw__polished_setpoints` | `gru_sequence` | `completed` | `00:16:24` |

## Run Details

### te_gru_sequence_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_001_001_gru_sequence_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_setpoints/queue/001_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T11:57:28`
- End Time: `2026-07-08T12:18:02`
- Duration: `00:20:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints/checkpoints/gru_sequence-epoch=091-val_mae=0.00217360.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-11-57-28__te_gru_sequence_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-57-28_dataset_input_mode_retraining__gru_sequence__polished_setpoints/logs/001_te_gru_sequence_global__polished_setpoints.log`
- Error Message: `N/A`

### te_gru_sequence_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_002_002_gru_sequence_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_setpoints/queue/002_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T12:18:02`
- End Time: `2026-07-08T12:47:20`
- Duration: `00:29:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/checkpoints/gru_sequence-epoch=152-val_mae=0.00216223.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-57-28_dataset_input_mode_retraining__gru_sequence__polished_setpoints/logs/002_te_gru_sequence_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_gru_sequence_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__gru_sequence__polished_setpoints/completed/2026-07-08-11-57-28_003_003_gru_sequence_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__gru_sequence__polished_setpoints/queue/003_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T12:47:20`
- End Time: `2026-07-08T13:03:44`
- Duration: `00:16:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/checkpoints/gru_sequence-epoch=088-val_mae=0.00218293.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-07-08-12-47-20__te_gru_sequence_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-11-57-28_dataset_input_mode_retraining__gru_sequence__polished_setpoints/logs/003_te_gru_sequence_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
