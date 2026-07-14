# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints`
- Generated At: `2026-07-15T01:20:08`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-22-56-56_dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_se`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_001_001_wave4_3_mixture_density_k2_global.yaml` | `te_wave4_3_mixture_density_k2_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:49:25` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_002_002_wave4_3_mixture_density_k2_fw.yaml` | `te_wave4_3_mixture_density_k2_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:51:03` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_003_003_wave4_3_mixture_density_k2_bw.yaml` | `te_wave4_3_mixture_density_k2_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:42:44` |

## Run Details

### te_wave4_3_mixture_density_k2_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_001_001_wave4_3_mixture_density_k2_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/queue/001_wave4_3_mixture_density_k2_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T22:56:56`
- End Time: `2026-07-14T23:46:20`
- Duration: `00:49:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=237-val_mae=0.00346790.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-22-56-56_dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_se/logs/001_te_wave4_3_mixture_density_k2_global__simplified.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_002_002_wave4_3_mixture_density_k2_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/queue/002_wave4_3_mixture_density_k2_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T23:46:20`
- End Time: `2026-07-15T00:37:24`
- Duration: `00:51:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=258-val_mae=0.00346706.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-22-56-56_dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_se/logs/002_te_wave4_3_mixture_density_k2_fw__simplified_set.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/completed/2026-07-14-22-56-56_003_003_wave4_3_mixture_density_k2_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints/queue/003_wave4_3_mixture_density_k2_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T00:37:24`
- End Time: `2026-07-15T01:20:08`
- Duration: `00:42:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=185-val_mae=0.00360751.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-22-56-56_dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_se/logs/003_te_wave4_3_mixture_density_k2_bw__simplified_set.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
