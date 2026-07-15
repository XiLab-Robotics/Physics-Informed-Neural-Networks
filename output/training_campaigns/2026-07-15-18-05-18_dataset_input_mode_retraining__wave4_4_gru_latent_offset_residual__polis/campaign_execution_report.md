# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values`
- Generated At: `2026-07-15T19:43:02`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-18-05-18_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_001_001_wave4_4_gru_latent_offset_residual_global.yaml` | `te_wave4_4_gru_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:46:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_002_002_wave4_4_gru_latent_offset_residual_fw.yaml` | `te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:21:49` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_003_003_wave4_4_gru_latent_offset_residual_bw.yaml` | `te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values` | `latent_state_hysteresis_probe` | `completed` | `00:29:49` |

## Run Details

### te_wave4_4_gru_latent_offset_residual_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_001_001_wave4_4_gru_latent_offset_residual_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/queue/001_wave4_4_gru_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T18:05:18`
- End Time: `2026-07-15T18:51:23`
- Duration: `00:46:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=208-val_mae=0.00217281.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-18-05-18_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/001_te_wave4_4_gru_latent_offset_residual_global__po.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_002_002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/queue/002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T18:51:23`
- End Time: `2026-07-15T19:13:13`
- Duration: `00:21:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=113-val_mae=0.00224746.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-18-05-18_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/002_te_wave4_4_gru_latent_offset_residual_fw__polish.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/completed/2026-07-15-18-05-18_003_003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values/queue/003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-15T19:13:13`
- End Time: `2026-07-15T19:43:02`
- Duration: `00:29:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=140-val_mae=0.00222826.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-18-05-18_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/003_te_wave4_4_gru_latent_offset_residual_bw__polish.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
