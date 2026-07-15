# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints`
- Generated At: `2026-07-15T17:49:02`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-16-39-39_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_001_001_wave4_4_gru_latent_offset_residual_global.yaml` | `te_wave4_4_gru_latent_offset_residual_global__polished_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:24:09` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_002_002_wave4_4_gru_latent_offset_residual_fw.yaml` | `te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:31:06` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_003_003_wave4_4_gru_latent_offset_residual_bw.yaml` | `te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:14:07` |

## Run Details

### te_wave4_4_gru_latent_offset_residual_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_001_001_wave4_4_gru_latent_offset_residual_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/queue/001_wave4_4_gru_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T16:39:40`
- End Time: `2026-07-15T17:03:49`
- Duration: `00:24:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=100-val_mae=0.00222289.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-16-39-39_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/001_te_wave4_4_gru_latent_offset_residual_global__po.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_002_002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/queue/002_wave4_4_gru_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T17:03:49`
- End Time: `2026-07-15T17:34:55`
- Duration: `00:31:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=164-val_mae=0.00221821.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-16-39-39_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/002_te_wave4_4_gru_latent_offset_residual_fw__polish.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/completed/2026-07-15-16-39-39_003_003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints/queue/003_wave4_4_gru_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T17:34:55`
- End Time: `2026-07-15T17:49:02`
- Duration: `00:14:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=036-val_mae=0.00226526.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-16-39-39_dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polis/logs/003_te_wave4_4_gru_latent_offset_residual_bw__polish.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
