# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values`
- Generated At: `2026-07-09T09:31:01`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-07-39-41_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_001_001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:39:39` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_002_002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:35:40` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_003_003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | `completed` | `00:36:01` |

## Run Details

### te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_001_001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/queue/001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T07:39:41`
- End Time: `2026-07-09T08:19:20`
- Duration: `00:39:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=226-val_mae=0.00193782.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-07-39-41_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/001_te_residual_harmonic_gru_sequence_sparse_rcim_gl.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_002_002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/queue/002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T08:19:20`
- End Time: `2026-07-09T08:55:01`
- Duration: `00:35:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=170-val_mae=0.00195142.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-07-39-41_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/002_te_residual_harmonic_gru_sequence_sparse_rcim_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-07-39-41_003_003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values/queue/003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T08:55:01`
- End Time: `2026-07-09T09:31:01`
- Duration: `00:36:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=200-val_mae=0.00195317.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-07-39-41_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/003_te_residual_harmonic_gru_sequence_sparse_rcim_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
