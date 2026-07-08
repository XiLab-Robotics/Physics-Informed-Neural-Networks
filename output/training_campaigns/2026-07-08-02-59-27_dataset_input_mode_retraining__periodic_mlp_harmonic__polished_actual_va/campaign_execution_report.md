# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values`
- Generated At: `2026-07-08T03:56:02`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-08-02-59-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_va`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_001_001_periodic_mlp_harmonic_global.yaml` | `te_periodic_mlp_harmonic_global__polished_actual_values` | `periodic_mlp` | `completed` | `00:18:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_002_002_periodic_mlp_harmonic_fw.yaml` | `te_periodic_mlp_harmonic_fw__polished_actual_values` | `periodic_mlp` | `completed` | `00:13:24` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_003_003_periodic_mlp_harmonic_bw.yaml` | `te_periodic_mlp_harmonic_bw__polished_actual_values` | `periodic_mlp` | `completed` | `00:25:00` |

## Run Details

### te_periodic_mlp_harmonic_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_001_001_periodic_mlp_harmonic_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/queue/001_periodic_mlp_harmonic_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T02:59:27`
- End Time: `2026-07-08T03:17:38`
- Duration: `00:18:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/checkpoints/periodic_mlp-epoch=074-val_mae=0.00123779.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-02-59-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_va/logs/001_te_periodic_mlp_harmonic_global__polished_actual.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_002_002_periodic_mlp_harmonic_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/queue/002_periodic_mlp_harmonic_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T03:17:38`
- End Time: `2026-07-08T03:31:01`
- Duration: `00:13:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/checkpoints/periodic_mlp-epoch=045-val_mae=0.00131065.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-02-59-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_va/logs/002_te_periodic_mlp_harmonic_fw__polished_actual_val.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/completed/2026-07-08-02-59-27_003_003_periodic_mlp_harmonic_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values/queue/003_periodic_mlp_harmonic_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-08T03:31:01`
- End Time: `2026-07-08T03:56:01`
- Duration: `00:25:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/checkpoints/periodic_mlp-epoch=128-val_mae=0.00117146.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-08-02-59-27_dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_va/logs/003_te_periodic_mlp_harmonic_bw__polished_actual_val.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
