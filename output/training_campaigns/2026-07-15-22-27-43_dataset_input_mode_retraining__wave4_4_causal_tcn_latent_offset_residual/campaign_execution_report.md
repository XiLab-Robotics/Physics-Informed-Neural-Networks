# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values`
- Generated At: `2026-07-15T23:09:39`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-22-27-43_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_001_001_wave4_4_causal_tcn_latent_offset_residual_global.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:12:34` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_002_002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:14:07` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_003_003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:15:16` |

## Run Details

### te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_001_001_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/queue/001_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T22:27:43`
- End Time: `2026-07-15T22:40:16`
- Duration: `00:12:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=041-val_mae=0.00230429.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-22-27-43_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/001_te_wave4_4_causal_tcn_latent_offset_residual_glo.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_002_002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/queue/002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T22:40:16`
- End Time: `2026-07-15T22:54:23`
- Duration: `00:14:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=038-val_mae=0.00225416.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-22-27-43_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/002_te_wave4_4_causal_tcn_latent_offset_residual_fw.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/completed/2026-07-15-22-27-43_003_003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values/queue/003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T22:54:23`
- End Time: `2026-07-15T23:09:39`
- Duration: `00:15:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=078-val_mae=0.00222665.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-22-27-43_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/003_te_wave4_4_causal_tcn_latent_offset_residual_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
