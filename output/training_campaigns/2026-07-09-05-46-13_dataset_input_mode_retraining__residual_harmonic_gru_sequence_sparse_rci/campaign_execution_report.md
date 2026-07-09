# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints`
- Generated At: `2026-07-09T06:17:11`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-09-05-46-13_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_001_001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:10:22` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_002_002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:10:51` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_003_003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints` | `residual_harmonic_gru_sequence` | `completed` | `00:09:46` |

## Run Details

### te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_001_001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/queue/001_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T05:46:13`
- End Time: `2026-07-09T05:56:34`
- Duration: `00:10:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=106-val_mae=0.00358149.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-05-46-13_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/001_te_residual_harmonic_gru_sequence_sparse_rcim_gl.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_002_002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/queue/002_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T05:56:34`
- End Time: `2026-07-09T06:07:25`
- Duration: `00:10:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=070-val_mae=0.00360244.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-05-46-13_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/002_te_residual_harmonic_gru_sequence_sparse_rcim_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/completed/2026-07-09-05-46-13_003_003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints/queue/003_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-09T06:07:25`
- End Time: `2026-07-09T06:17:11`
- Duration: `00:09:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=061-val_mae=0.00359811.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-09-05-46-13_dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rci/logs/003_te_residual_harmonic_gru_sequence_sparse_rcim_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
