# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__feedforward__polished_actual_values`
- Generated At: `2026-07-07T19:39:50`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-18-12-11_dataset_input_mode_retraining__feedforward__polished_actual_values`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_001_001_feedforward_global.yaml` | `te_feedforward_global__polished_actual_values` | `feedforward` | `completed` | `00:30:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_002_002_feedforward_fw.yaml` | `te_feedforward_fw__polished_actual_values` | `feedforward` | `completed` | `00:34:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_003_003_feedforward_bw.yaml` | `te_feedforward_bw__polished_actual_values` | `feedforward` | `completed` | `00:22:41` |

## Run Details

### te_feedforward_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_001_001_feedforward_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_actual_values/queue/001_feedforward_global.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-18-12-11__te_feedforward_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T18:12:11`
- End Time: `2026-07-07T18:43:03`
- Duration: `00:30:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values/checkpoints/feedforward-epoch=118-val_mae=0.00160808.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-18-12-11__te_feedforward_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-18-12-11_dataset_input_mode_retraining__feedforward__polished_actual_values/logs/001_te_feedforward_global__polished_actual_values.log`
- Error Message: `N/A`

### te_feedforward_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_002_002_feedforward_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_actual_values/queue/002_feedforward_fw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T18:43:03`
- End Time: `2026-07-07T19:17:09`
- Duration: `00:34:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/checkpoints/feedforward-epoch=181-val_mae=0.00161552.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-18-12-11_dataset_input_mode_retraining__feedforward__polished_actual_values/logs/002_te_feedforward_fw__polished_actual_values.log`
- Error Message: `N/A`

### te_feedforward_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_actual_values/completed/2026-07-07-18-12-11_003_003_feedforward_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_actual_values/queue/003_feedforward_bw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T19:17:09`
- End Time: `2026-07-07T19:39:50`
- Duration: `00:22:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/checkpoints/feedforward-epoch=074-val_mae=0.00164741.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-18-12-11_dataset_input_mode_retraining__feedforward__polished_actual_values/logs/003_te_feedforward_bw__polished_actual_values.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
