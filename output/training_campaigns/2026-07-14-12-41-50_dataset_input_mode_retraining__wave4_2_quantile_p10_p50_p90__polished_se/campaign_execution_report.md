# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints`
- Generated At: `2026-07-14T14:18:57`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-12-41-50_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_se`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_001_001_wave4_2_quantile_p10_p50_p90_global.yaml` | `te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:37` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml` | `te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:39:27` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml` | `te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:24:02` |

## Run Details

### te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_001_001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/queue/001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T12:41:50`
- End Time: `2026-07-14T13:15:27`
- Duration: `00:33:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=109-val_mae=0.00179474.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-12-41-50_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_se/logs/001_te_wave4_2_quantile_p10_p50_p90_global__polished.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/queue/002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T13:15:27`
- End Time: `2026-07-14T13:54:54`
- Duration: `00:39:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=157-val_mae=0.00180121.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-12-41-50_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_se/logs/002_te_wave4_2_quantile_p10_p50_p90_fw__polished_set.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/completed/2026-07-14-12-41-50_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints/queue/003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T13:54:54`
- End Time: `2026-07-14T14:18:57`
- Duration: `00:24:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=063-val_mae=0.00181729.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-12-41-50_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_se/logs/003_te_wave4_2_quantile_p10_p50_p90_bw__polished_set.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
