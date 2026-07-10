# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints`
- Generated At: `2026-07-10T14:57:16`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-13-46-46_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_001_001_wave3_2_clean_sequential_residual_offset_global.yaml` | `te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:25:58` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_002_002_wave3_2_clean_sequential_residual_offset_fw.yaml` | `te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:22:26` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_003_003_wave3_2_clean_sequential_residual_offset_bw.yaml` | `te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints` | `sequential_residual_offset_probe` | `completed` | `00:22:06` |

## Run Details

### te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_001_001_wave3_2_clean_sequential_residual_offset_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/queue/001_wave3_2_clean_sequential_residual_offset_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T13:46:46`
- End Time: `2026-07-10T14:12:44`
- Duration: `00:25:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=128-val_mae=0.00217355.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-13-46-46_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/001_te_wave3_2_clean_sequential_residual_offset_glob.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_002_002_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/queue/002_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T14:12:44`
- End Time: `2026-07-10T14:35:10`
- Duration: `00:22:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=092-val_mae=0.00219799.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-13-46-46_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/002_te_wave3_2_clean_sequential_residual_offset_fw.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/completed/2026-07-10-13-46-46_003_003_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints/queue/003_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T14:35:10`
- End Time: `2026-07-10T14:57:16`
- Duration: `00:22:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=089-val_mae=0.00218161.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-13-46-46_dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset/logs/003_te_wave3_2_clean_sequential_residual_offset_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
