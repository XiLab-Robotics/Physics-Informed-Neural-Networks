# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints`
- Generated At: `2026-07-12T05:43:54`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-12-04-02-10_dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_001_001_wave3_3_full_curve_composite_global.yaml` | `te_wave3_3_full_curve_composite_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:36:52` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_002_002_wave3_3_full_curve_composite_fw.yaml` | `te_wave3_3_full_curve_composite_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:30:41` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_003_003_wave3_3_full_curve_composite_bw.yaml` | `te_wave3_3_full_curve_composite_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:34:10` |

## Run Details

### te_wave3_3_full_curve_composite_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_001_001_wave3_3_full_curve_composite_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/queue/001_wave3_3_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T04:02:10`
- End Time: `2026-07-12T04:39:03`
- Duration: `00:36:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=172-val_mae=0.00363873.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-04-02-10_dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified/logs/001_te_wave3_3_full_curve_composite_global__simplifi.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_002_002_wave3_3_full_curve_composite_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/queue/002_wave3_3_full_curve_composite_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T04:39:03`
- End Time: `2026-07-12T05:09:44`
- Duration: `00:30:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=137-val_mae=0.00367911.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-04-02-10_dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified/logs/002_te_wave3_3_full_curve_composite_fw__simplified_s.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/completed/2026-07-12-04-02-10_003_003_wave3_3_full_curve_composite_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints/queue/003_wave3_3_full_curve_composite_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-12T05:09:44`
- End Time: `2026-07-12T05:43:54`
- Duration: `00:34:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=140-val_mae=0.00365689.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-12-05-09-44__te_wave3_3_full_curve_composite_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-12-04-02-10_dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified/logs/003_te_wave3_3_full_curve_composite_bw__simplified_s.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
