# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints`
- Generated At: `2026-07-16T01:57:35`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-16-00-50-35_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_001_001_wave5_1_harmonic_prior_pointwise_control_global.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:28:36` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_002_002_wave5_1_harmonic_prior_pointwise_control_fw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:20:43` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_003_003_wave5_1_harmonic_prior_pointwise_control_bw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:17:41` |

## Run Details

### te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_001_001_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/queue/001_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T00:50:35`
- End Time: `2026-07-16T01:19:11`
- Duration: `00:28:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=131-val_mae=0.00190080.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-00-50-35_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/001_te_wave5_1_harmonic_prior_pointwise_control_glob.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_002_002_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/queue/002_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T01:19:11`
- End Time: `2026-07-16T01:39:54`
- Duration: `00:20:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=084-val_mae=0.00195891.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-19-11__te_wave5_1_harmonic_prior_pointwise_control_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-00-50-35_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/002_te_wave5_1_harmonic_prior_pointwise_control_fw.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/completed/2026-07-16-00-50-35_003_003_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints/queue/003_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T01:39:54`
- End Time: `2026-07-16T01:57:35`
- Duration: `00:17:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=074-val_mae=0.00194037.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-01-39-54__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-00-50-35_dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control/logs/003_te_wave5_1_harmonic_prior_pointwise_control_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
