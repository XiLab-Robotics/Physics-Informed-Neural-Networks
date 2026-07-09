# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints`
- Generated At: `2026-07-09T19:24:40`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-18-39-59_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_001_001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:16:39` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_002_002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:14:14` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_003_003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | `completed` | `00:13:48` |

## Run Details

### te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_001_001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/queue/001_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T18:39:59`
- End Time: `2026-07-09T18:56:39`
- Duration: `00:16:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=050-val_mae=0.00361757.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-18-39-59_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/001_te_residual_harmonic_lstm_sequence_sparse_rcim_g.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_002_002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/queue/002_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T18:56:39`
- End Time: `2026-07-09T19:10:52`
- Duration: `00:14:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=029-val_mae=0.00367824.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-18-39-59_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/002_te_residual_harmonic_lstm_sequence_sparse_rcim_f.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-18-39-59_003_003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints/queue/003_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T19:10:53`
- End Time: `2026-07-09T19:24:40`
- Duration: `00:13:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=027-val_mae=0.00365442.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-18-39-59_dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rc/logs/003_te_residual_harmonic_lstm_sequence_sparse_rcim_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
