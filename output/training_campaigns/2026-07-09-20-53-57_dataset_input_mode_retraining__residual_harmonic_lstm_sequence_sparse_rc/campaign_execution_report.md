# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values`
- Generated At: `2026-07-09T22:49:53`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-20-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_001_001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:52:27` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_002_002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:50:38` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_003_003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | `completed` | `00:12:50` |

## Run Details

### te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_001_001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/queue/001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T20:53:57`
- End Time: `2026-07-09T21:46:24`
- Duration: `00:52:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=189-val_mae=0.00196022.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-53-57__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-20-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/001_te_residual_harmonic_lstm_sequence_sparse_rcim_g.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_002_002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/queue/002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T21:46:24`
- End Time: `2026-07-09T22:37:02`
- Duration: `00:50:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=219-val_mae=0.00195141.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-20-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/002_te_residual_harmonic_lstm_sequence_sparse_rcim_f.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/completed/2026-07-09-20-53-57_003_003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values/queue/003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values`
- Queue Status: `completed`
- Start Time: `2026-07-09T22:37:02`
- End Time: `2026-07-09T22:49:53`
- Duration: `00:12:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=010-val_mae=0.00215380.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-20-53-57_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/003_te_residual_harmonic_lstm_sequence_sparse_rcim_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
