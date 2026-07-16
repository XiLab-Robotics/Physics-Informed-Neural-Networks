# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints`
- Generated At: `2026-07-16T04:41:37`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-16-04-00-48_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_001_001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:16:42` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_002_002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:13:36` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_003_003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints` | `wave3_harmonic_prior_residual` | `completed` | `00:10:31` |

## Run Details

### te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_001_001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/queue/001_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T04:00:48`
- End Time: `2026-07-16T04:17:30`
- Duration: `00:16:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=098-val_mae=0.00363558.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-00-48__te_wave5_1_harmonic_prior_smooth_l1_structured_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-04-00-48_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/001_te_wave5_1_harmonic_prior_smooth_l1_structured_g.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_002_002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/queue/002_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T04:17:30`
- End Time: `2026-07-16T04:31:07`
- Duration: `00:13:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=070-val_mae=0.00364754.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-04-00-48_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/002_te_wave5_1_harmonic_prior_smooth_l1_structured_f.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/completed/2026-07-16-04-00-48_003_003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints/queue/003_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-16T04:31:07`
- End Time: `2026-07-16T04:41:37`
- Duration: `00:10:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=044-val_mae=0.00364993.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-16-04-31-07__te_wave5_1_harmonic_prior_smooth_l1_structured_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-16-04-00-48_dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structur/logs/003_te_wave5_1_harmonic_prior_smooth_l1_structured_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
