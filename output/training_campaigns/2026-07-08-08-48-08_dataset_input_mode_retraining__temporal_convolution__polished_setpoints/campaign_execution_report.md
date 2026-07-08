# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__temporal_convolution__polished_setpoints`
- Generated At: `2026-07-08T09:39:25`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-08-48-08_dataset_input_mode_retraining__temporal_convolution__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_001_001_temporal_convolution_global.yaml` | `te_temporal_convolution_global__polished_setpoints` | `temporal_convolution` | `completed` | `00:13:19` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_002_002_temporal_convolution_fw.yaml` | `te_temporal_convolution_fw__polished_setpoints` | `temporal_convolution` | `completed` | `00:12:51` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_003_003_temporal_convolution_bw.yaml` | `te_temporal_convolution_bw__polished_setpoints` | `temporal_convolution` | `completed` | `00:25:06` |

## Run Details

### te_temporal_convolution_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_001_001_temporal_convolution_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/queue/001_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T08:48:08`
- End Time: `2026-07-08T09:01:27`
- Duration: `00:13:19`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/checkpoints/temporal_convolution-epoch=074-val_mae=0.00225012.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-08-48-08_dataset_input_mode_retraining__temporal_convolution__polished_setpoints/logs/001_te_temporal_convolution_global__polished_setpoin.log`
- Error Message: `N/A`

### te_temporal_convolution_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_002_002_temporal_convolution_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/queue/002_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T09:01:27`
- End Time: `2026-07-08T09:14:19`
- Duration: `00:12:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/checkpoints/temporal_convolution-epoch=042-val_mae=0.00225272.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-08-48-08_dataset_input_mode_retraining__temporal_convolution__polished_setpoints/logs/002_te_temporal_convolution_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_temporal_convolution_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/completed/2026-07-08-08-48-08_003_003_temporal_convolution_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_setpoints/queue/003_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T09:14:19`
- End Time: `2026-07-08T09:39:25`
- Duration: `00:25:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/checkpoints/temporal_convolution-epoch=125-val_mae=0.00222200.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-08-48-08_dataset_input_mode_retraining__temporal_convolution__polished_setpoints/logs/003_te_temporal_convolution_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
