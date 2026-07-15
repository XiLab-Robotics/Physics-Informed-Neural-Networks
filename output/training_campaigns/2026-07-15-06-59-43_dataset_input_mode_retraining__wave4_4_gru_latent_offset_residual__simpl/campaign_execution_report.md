# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints`
- Generated At: `2026-07-15T07:39:05`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-06-59-43_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simpl`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_001_001_wave4_4_gru_latent_offset_residual_global.yaml` | `te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:12:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_002_002_wave4_4_gru_latent_offset_residual_fw.yaml` | `te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:14:49` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_003_003_wave4_4_gru_latent_offset_residual_bw.yaml` | `te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:12:27` |

## Run Details

### te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_001_001_wave4_4_gru_latent_offset_residual_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/queue/001_wave4_4_gru_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T06:59:43`
- End Time: `2026-07-15T07:11:49`
- Duration: `00:12:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=065-val_mae=0.00375664.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-06-59-43_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simpl/logs/001_te_wave4_4_gru_latent_offset_residual_global__si.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_002_002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/queue/002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T07:11:49`
- End Time: `2026-07-15T07:26:38`
- Duration: `00:14:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=081-val_mae=0.00371922.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-06-59-43_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simpl/logs/002_te_wave4_4_gru_latent_offset_residual_fw__simpli.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/completed/2026-07-15-06-59-43_003_003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints/queue/003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T07:26:38`
- End Time: `2026-07-15T07:39:05`
- Duration: `00:12:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=072-val_mae=0.00377245.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-06-59-43_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simpl/logs/003_te_wave4_4_gru_latent_offset_residual_bw__simpli.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
