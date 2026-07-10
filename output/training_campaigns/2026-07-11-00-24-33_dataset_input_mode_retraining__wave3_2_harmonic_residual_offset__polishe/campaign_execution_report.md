# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints`
- Generated At: `2026-07-11T01:42:05`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-11-00-24-33_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_001_001_wave3_2_harmonic_residual_offset_global.yaml` | `te_wave3_2_harmonic_residual_offset_global__polished_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:28:26` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_002_002_wave3_2_harmonic_residual_offset_fw.yaml` | `te_wave3_2_harmonic_residual_offset_fw__polished_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:21:43` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_003_003_wave3_2_harmonic_residual_offset_bw.yaml` | `te_wave3_2_harmonic_residual_offset_bw__polished_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:27:23` |

## Run Details

### te_wave3_2_harmonic_residual_offset_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_001_001_wave3_2_harmonic_residual_offset_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/queue/001_wave3_2_harmonic_residual_offset_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T00:24:33`
- End Time: `2026-07-11T00:52:59`
- Duration: `00:28:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=124-val_mae=0.00190522.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-00-24-33_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/001_te_wave3_2_harmonic_residual_offset_global__poli.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_002_002_wave3_2_harmonic_residual_offset_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/queue/002_wave3_2_harmonic_residual_offset_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T00:52:59`
- End Time: `2026-07-11T01:14:42`
- Duration: `00:21:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=085-val_mae=0.00188607.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-00-24-33_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/002_te_wave3_2_harmonic_residual_offset_fw__polished.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/completed/2026-07-11-00-24-33_003_003_wave3_2_harmonic_residual_offset_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints/queue/003_wave3_2_harmonic_residual_offset_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-11T01:14:42`
- End Time: `2026-07-11T01:42:05`
- Duration: `00:27:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=120-val_mae=0.00193287.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-11-00-24-33_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polishe/logs/003_te_wave3_2_harmonic_residual_offset_bw__polished.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
