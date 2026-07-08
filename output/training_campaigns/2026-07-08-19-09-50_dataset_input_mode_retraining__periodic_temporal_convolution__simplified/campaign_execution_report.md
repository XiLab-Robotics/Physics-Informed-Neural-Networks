# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints`
- Generated At: `2026-07-08T19:35:07`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-19-09-50_dataset_input_mode_retraining__periodic_temporal_convolution__simplified`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_001_001_periodic_temporal_convolution_global.yaml` | `te_periodic_temporal_convolution_global__simplified_setpoints` | `periodic_temporal_convolution` | `completed` | `00:09:38` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_002_002_periodic_temporal_convolution_fw.yaml` | `te_periodic_temporal_convolution_fw__simplified_setpoints` | `periodic_temporal_convolution` | `completed` | `00:05:56` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_003_003_periodic_temporal_convolution_bw.yaml` | `te_periodic_temporal_convolution_bw__simplified_setpoints` | `periodic_temporal_convolution` | `completed` | `00:09:43` |

## Run Details

### te_periodic_temporal_convolution_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_001_001_periodic_temporal_convolution_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/queue/001_periodic_temporal_convolution_global.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T19:09:50`
- End Time: `2026-07-08T19:19:28`
- Duration: `00:09:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=095-val_mae=0.00360046.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-09-50_dataset_input_mode_retraining__periodic_temporal_convolution__simplified/logs/001_te_periodic_temporal_convolution_global__simplif.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_002_002_periodic_temporal_convolution_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/queue/002_periodic_temporal_convolution_fw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T19:19:28`
- End Time: `2026-07-08T19:25:24`
- Duration: `00:05:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=050-val_mae=0.00364466.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-09-50_dataset_input_mode_retraining__periodic_temporal_convolution__simplified/logs/002_te_periodic_temporal_convolution_fw__simplified.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/completed/2026-07-08-19-09-50_003_003_periodic_temporal_convolution_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints/queue/003_periodic_temporal_convolution_bw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T19:25:24`
- End Time: `2026-07-08T19:35:07`
- Duration: `00:09:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=066-val_mae=0.00355314.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-09-50_dataset_input_mode_retraining__periodic_temporal_convolution__simplified/logs/003_te_periodic_temporal_convolution_bw__simplified.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
