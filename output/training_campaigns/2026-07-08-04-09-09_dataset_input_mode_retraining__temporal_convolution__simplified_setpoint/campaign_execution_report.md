# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__temporal_convolution__simplified_setpoints`
- Generated At: `2026-07-08T04:29:51`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-04-09-09_dataset_input_mode_retraining__temporal_convolution__simplified_setpoint`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_001_001_temporal_convolution_global.yaml` | `te_temporal_convolution_global__simplified_setpoints` | `temporal_convolution` | `completed` | `00:05:29` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_002_002_temporal_convolution_fw.yaml` | `te_temporal_convolution_fw__simplified_setpoints` | `temporal_convolution` | `completed` | `00:06:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_003_003_temporal_convolution_bw.yaml` | `te_temporal_convolution_bw__simplified_setpoints` | `temporal_convolution` | `completed` | `00:08:39` |

## Run Details

### te_temporal_convolution_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_001_001_temporal_convolution_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/queue/001_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T04:09:09`
- End Time: `2026-07-08T04:14:38`
- Duration: `00:05:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/checkpoints/temporal_convolution-epoch=016-val_mae=0.00380497.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-04-09-09_dataset_input_mode_retraining__temporal_convolution__simplified_setpoint/logs/001_te_temporal_convolution_global__simplified_setpo.log`
- Error Message: `N/A`

### te_temporal_convolution_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_002_002_temporal_convolution_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/queue/002_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T04:14:38`
- End Time: `2026-07-08T04:21:12`
- Duration: `00:06:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/checkpoints/temporal_convolution-epoch=031-val_mae=0.00377881.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-04-09-09_dataset_input_mode_retraining__temporal_convolution__simplified_setpoint/logs/002_te_temporal_convolution_fw__simplified_setpoints.log`
- Error Message: `N/A`

### te_temporal_convolution_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/completed/2026-07-08-04-09-09_003_003_temporal_convolution_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__simplified_setpoints/queue/003_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T04:21:12`
- End Time: `2026-07-08T04:29:51`
- Duration: `00:08:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/checkpoints/temporal_convolution-epoch=091-val_mae=0.00381312.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-04-09-09_dataset_input_mode_retraining__temporal_convolution__simplified_setpoint/logs/003_te_temporal_convolution_bw__simplified_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
