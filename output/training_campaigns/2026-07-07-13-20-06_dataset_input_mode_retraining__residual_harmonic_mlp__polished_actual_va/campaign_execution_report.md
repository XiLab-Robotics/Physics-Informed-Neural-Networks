# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values`
- Generated At: `2026-07-07T14:47:50`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-07-13-20-06_dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_va`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_001_001_residual_harmonic_mlp_global.yaml` | `te_residual_harmonic_mlp_global__polished_actual_values` | `residual_harmonic_mlp` | `completed` | `00:30:13` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_002_002_residual_harmonic_mlp_fw.yaml` | `te_residual_harmonic_mlp_fw__polished_actual_values` | `residual_harmonic_mlp` | `completed` | `00:25:05` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_003_003_residual_harmonic_mlp_bw.yaml` | `te_residual_harmonic_mlp_bw__polished_actual_values` | `residual_harmonic_mlp` | `completed` | `00:32:26` |

## Run Details

### te_residual_harmonic_mlp_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_001_001_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/queue/001_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T13:20:06`
- End Time: `2026-07-07T13:50:19`
- Duration: `00:30:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=077-val_mae=0.00160259.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-13-20-06_dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_va/logs/001_te_residual_harmonic_mlp_global__polished_actual.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_002_002_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/queue/002_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T13:50:19`
- End Time: `2026-07-07T14:15:24`
- Duration: `00:25:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=052-val_mae=0.00163893.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-13-20-06_dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_va/logs/002_te_residual_harmonic_mlp_fw__polished_actual_val.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/completed/2026-07-07-13-20-06_003_003_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values/queue/003_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-07T14:15:24`
- End Time: `2026-07-07T14:47:50`
- Duration: `00:32:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=075-val_mae=0.00160615.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-07-13-20-06_dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_va/logs/003_te_residual_harmonic_mlp_bw__polished_actual_val.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
