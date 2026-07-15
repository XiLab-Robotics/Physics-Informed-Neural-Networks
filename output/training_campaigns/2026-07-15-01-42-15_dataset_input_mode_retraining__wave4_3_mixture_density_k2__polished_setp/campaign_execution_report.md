# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints`
- Generated At: `2026-07-15T03:38:52`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-01-42-15_dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setp`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_001_001_wave4_3_mixture_density_k2_global.yaml` | `te_wave4_3_mixture_density_k2_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:37:16` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_002_002_wave4_3_mixture_density_k2_fw.yaml` | `te_wave4_3_mixture_density_k2_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_003_003_wave4_3_mixture_density_k2_bw.yaml` | `te_wave4_3_mixture_density_k2_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:46:56` |

## Run Details

### te_wave4_3_mixture_density_k2_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_001_001_wave4_3_mixture_density_k2_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/queue/001_wave4_3_mixture_density_k2_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T01:42:15`
- End Time: `2026-07-15T02:19:31`
- Duration: `00:37:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00186311.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-01-42-15_dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setp/logs/001_te_wave4_3_mixture_density_k2_global__polished_s.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_002_002_wave4_3_mixture_density_k2_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/queue/002_wave4_3_mixture_density_k2_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T02:19:32`
- End Time: `2026-07-15T02:51:55`
- Duration: `00:32:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00184963.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-01-42-15_dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setp/logs/002_te_wave4_3_mixture_density_k2_fw__polished_setpo.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/completed/2026-07-15-01-42-15_003_003_wave4_3_mixture_density_k2_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints/queue/003_wave4_3_mixture_density_k2_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T02:51:55`
- End Time: `2026-07-15T03:38:52`
- Duration: `00:46:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=173-val_mae=0.00181733.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-01-42-15_dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setp/logs/003_te_wave4_3_mixture_density_k2_bw__polished_setpo.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
