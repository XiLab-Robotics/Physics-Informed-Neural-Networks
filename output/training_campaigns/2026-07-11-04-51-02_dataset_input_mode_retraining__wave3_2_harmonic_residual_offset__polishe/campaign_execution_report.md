# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values`
- Generated At: `2026-07-11T06:57:20`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-04-51-02_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_001_001_wave3_2_harmonic_residual_offset_global.yaml` | `te_wave3_2_harmonic_residual_offset_global__polished_actual_values` | `harmonic_residual_offset_probe` | `completed` | `00:38:50` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_002_002_wave3_2_harmonic_residual_offset_fw.yaml` | `te_wave3_2_harmonic_residual_offset_fw__polished_actual_values` | `harmonic_residual_offset_probe` | `completed` | `00:43:48` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_003_003_wave3_2_harmonic_residual_offset_bw.yaml` | `te_wave3_2_harmonic_residual_offset_bw__polished_actual_values` | `harmonic_residual_offset_probe` | `completed` | `00:43:40` |

## Run Details

### te_wave3_2_harmonic_residual_offset_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_001_001_wave3_2_harmonic_residual_offset_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/queue/001_wave3_2_harmonic_residual_offset_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T04:51:02`
- End Time: `2026-07-11T05:29:51`
- Duration: `00:38:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=201-val_mae=0.00183635.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-04-51-02_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/001_te_wave3_2_harmonic_residual_offset_global__poli.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_002_002_wave3_2_harmonic_residual_offset_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/queue/002_wave3_2_harmonic_residual_offset_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T05:29:51`
- End Time: `2026-07-11T06:13:40`
- Duration: `00:43:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=205-val_mae=0.00184965.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-04-51-02_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/002_te_wave3_2_harmonic_residual_offset_fw__polished.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/completed/2026-07-11-04-51-02_003_003_wave3_2_harmonic_residual_offset_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values/queue/003_wave3_2_harmonic_residual_offset_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-11T06:13:40`
- End Time: `2026-07-11T06:57:20`
- Duration: `00:43:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=205-val_mae=0.00185299.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-04-51-02_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/003_te_wave3_2_harmonic_residual_offset_bw__polished.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
