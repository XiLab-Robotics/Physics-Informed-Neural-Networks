# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints`
- Generated At: `2026-07-08T20:25:10`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-19-44-50_dataset_input_mode_retraining__periodic_temporal_convolution__polished_s`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_001_001_periodic_temporal_convolution_global.yaml` | `te_periodic_temporal_convolution_global__polished_setpoints` | `periodic_temporal_convolution` | `completed` | `00:14:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_002_002_periodic_temporal_convolution_fw.yaml` | `te_periodic_temporal_convolution_fw__polished_setpoints` | `periodic_temporal_convolution` | `completed` | `00:12:56` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_003_003_periodic_temporal_convolution_bw.yaml` | `te_periodic_temporal_convolution_bw__polished_setpoints` | `periodic_temporal_convolution` | `completed` | `00:13:01` |

## Run Details

### te_periodic_temporal_convolution_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_001_001_periodic_temporal_convolution_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/queue/001_periodic_temporal_convolution_global.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T19:44:50`
- End Time: `2026-07-08T19:59:14`
- Duration: `00:14:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=050-val_mae=0.00196079.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-44-50_dataset_input_mode_retraining__periodic_temporal_convolution__polished_s/logs/001_te_periodic_temporal_convolution_global__polishe.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_002_002_periodic_temporal_convolution_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/queue/002_periodic_temporal_convolution_fw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T19:59:14`
- End Time: `2026-07-08T20:12:10`
- Duration: `00:12:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=040-val_mae=0.00194544.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-44-50_dataset_input_mode_retraining__periodic_temporal_convolution__polished_s/logs/002_te_periodic_temporal_convolution_fw__polished_se.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/completed/2026-07-08-19-44-50_003_003_periodic_temporal_convolution_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints/queue/003_periodic_temporal_convolution_bw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-08T20:12:10`
- End Time: `2026-07-08T20:25:10`
- Duration: `00:13:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=048-val_mae=0.00196877.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-19-44-50_dataset_input_mode_retraining__periodic_temporal_convolution__polished_s/logs/003_te_periodic_temporal_convolution_bw__polished_se.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
