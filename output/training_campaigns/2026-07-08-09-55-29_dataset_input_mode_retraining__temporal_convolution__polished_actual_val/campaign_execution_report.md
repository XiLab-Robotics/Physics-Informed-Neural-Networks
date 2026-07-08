# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__temporal_convolution__polished_actual_values`
- Generated At: `2026-07-08T11:01:13`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-09-55-29_dataset_input_mode_retraining__temporal_convolution__polished_actual_val`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_001_001_temporal_convolution_global.yaml` | `te_temporal_convolution_global__polished_actual_values` | `temporal_convolution` | `completed` | `00:24:33` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_002_002_temporal_convolution_fw.yaml` | `te_temporal_convolution_fw__polished_actual_values` | `temporal_convolution` | `completed` | `00:14:07` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_003_003_temporal_convolution_bw.yaml` | `te_temporal_convolution_bw__polished_actual_values` | `temporal_convolution` | `completed` | `00:27:04` |

## Run Details

### te_temporal_convolution_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_001_001_temporal_convolution_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/queue/001_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T09:55:29`
- End Time: `2026-07-08T10:20:02`
- Duration: `00:24:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/checkpoints/temporal_convolution-epoch=106-val_mae=0.00219077.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-09-55-29_dataset_input_mode_retraining__temporal_convolution__polished_actual_val/logs/001_te_temporal_convolution_global__polished_actual.log`
- Error Message: `N/A`

### te_temporal_convolution_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_002_002_temporal_convolution_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/queue/002_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T10:20:02`
- End Time: `2026-07-08T10:34:09`
- Duration: `00:14:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/checkpoints/temporal_convolution-epoch=064-val_mae=0.00227215.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-09-55-29_dataset_input_mode_retraining__temporal_convolution__polished_actual_val/logs/002_te_temporal_convolution_fw__polished_actual_valu.log`
- Error Message: `N/A`

### te_temporal_convolution_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/completed/2026-07-08-09-55-29_003_003_temporal_convolution_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__temporal_convolution__polished_actual_values/queue/003_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T10:34:09`
- End Time: `2026-07-08T11:01:13`
- Duration: `00:27:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values/checkpoints/temporal_convolution-epoch=123-val_mae=0.00219843.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-07-08-10-34-09__te_temporal_convolution_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-09-55-29_dataset_input_mode_retraining__temporal_convolution__polished_actual_val/logs/003_te_temporal_convolution_bw__polished_actual_valu.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
