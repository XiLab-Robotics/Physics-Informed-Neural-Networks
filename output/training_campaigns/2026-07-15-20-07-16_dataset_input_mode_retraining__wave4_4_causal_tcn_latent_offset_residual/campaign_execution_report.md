# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints`
- Generated At: `2026-07-15T20:52:03`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-15-20-07-16_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_001_001_wave4_4_causal_tcn_latent_offset_residual_global.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:07:10` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_002_002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:24:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_003_003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints` | `latent_state_hysteresis_probe` | `completed` | `00:13:13` |

## Run Details

### te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_001_001_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/queue/001_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T20:07:16`
- End Time: `2026-07-15T20:14:26`
- Duration: `00:07:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=055-val_mae=0.00376625.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-20-07-16_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/001_te_wave4_4_causal_tcn_latent_offset_residual_glo.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_002_002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/queue/002_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T20:14:26`
- End Time: `2026-07-15T20:38:50`
- Duration: `00:24:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=236-val_mae=0.00349844.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-20-07-16_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/002_te_wave4_4_causal_tcn_latent_offset_residual_fw.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/completed/2026-07-15-20-07-16_003_003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints/queue/003_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-15T20:38:50`
- End Time: `2026-07-15T20:52:03`
- Duration: `00:13:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=105-val_mae=0.00370934.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-15-20-07-16_dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual/logs/003_te_wave4_4_causal_tcn_latent_offset_residual_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
