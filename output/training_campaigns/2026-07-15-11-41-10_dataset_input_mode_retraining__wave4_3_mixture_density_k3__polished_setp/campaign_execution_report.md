# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints`
- Generated At: `2026-07-15T13:42:30`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-11-41-10_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setp`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_001_001_wave4_3_mixture_density_k3_global.yaml` | `te_wave4_3_mixture_density_k3_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:40:39` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_002_002_wave4_3_mixture_density_k3_fw.yaml` | `te_wave4_3_mixture_density_k3_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_003_003_wave4_3_mixture_density_k3_bw.yaml` | `te_wave4_3_mixture_density_k3_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:46:49` |

## Run Details

### te_wave4_3_mixture_density_k3_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_001_001_wave4_3_mixture_density_k3_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/queue/001_wave4_3_mixture_density_k3_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T11:41:10`
- End Time: `2026-07-15T12:21:48`
- Duration: `00:40:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=177-val_mae=0.00183826.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-11-41-10_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setp/logs/001_te_wave4_3_mixture_density_k3_global__polished_s.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_002_002_wave4_3_mixture_density_k3_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/queue/002_wave4_3_mixture_density_k3_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T12:21:49`
- End Time: `2026-07-15T12:55:40`
- Duration: `00:33:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=140-val_mae=0.00184649.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-11-41-10_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setp/logs/002_te_wave4_3_mixture_density_k3_fw__polished_setpo.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/completed/2026-07-15-11-41-10_003_003_wave4_3_mixture_density_k3_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints/queue/003_wave4_3_mixture_density_k3_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T12:55:40`
- End Time: `2026-07-15T13:42:29`
- Duration: `00:46:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=166-val_mae=0.00183407.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-11-41-10_dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setp/logs/003_te_wave4_3_mixture_density_k3_bw__polished_setpo.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
