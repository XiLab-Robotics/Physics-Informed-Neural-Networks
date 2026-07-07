# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__feedforward__polished_setpoints`
- Generated At: `2026-07-07T17:59:36`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-17-10-53_dataset_input_mode_retraining__feedforward__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_001_001_feedforward_global.yaml` | `te_feedforward_global__polished_setpoints` | `feedforward` | `completed` | `00:15:04` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_002_002_feedforward_fw.yaml` | `te_feedforward_fw__polished_setpoints` | `feedforward` | `completed` | `00:15:36` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_003_003_feedforward_bw.yaml` | `te_feedforward_bw__polished_setpoints` | `feedforward` | `completed` | `00:18:02` |

## Run Details

### te_feedforward_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_001_001_feedforward_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_setpoints/queue/001_feedforward_global.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-17-10-53__te_feedforward_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T17:10:53`
- End Time: `2026-07-07T17:25:57`
- Duration: `00:15:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/checkpoints/feedforward-epoch=038-val_mae=0.00169107.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-17-10-53_dataset_input_mode_retraining__feedforward__polished_setpoints/logs/001_te_feedforward_global__polished_setpoints.log`
- Error Message: `N/A`

### te_feedforward_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_002_002_feedforward_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_setpoints/queue/002_feedforward_fw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T17:25:58`
- End Time: `2026-07-07T17:41:33`
- Duration: `00:15:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/checkpoints/feedforward-epoch=042-val_mae=0.00168289.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-17-10-53_dataset_input_mode_retraining__feedforward__polished_setpoints/logs/002_te_feedforward_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_feedforward_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__feedforward__polished_setpoints/completed/2026-07-07-17-10-53_003_003_feedforward_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__feedforward__polished_setpoints/queue/003_feedforward_bw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-07T17:41:34`
- End Time: `2026-07-07T17:59:36`
- Duration: `00:18:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/checkpoints/feedforward-epoch=057-val_mae=0.00164066.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-17-10-53_dataset_input_mode_retraining__feedforward__polished_setpoints/logs/003_te_feedforward_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
