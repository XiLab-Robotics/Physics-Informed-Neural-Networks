# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Generated At: `2026-07-14T12:24:22`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-10-30-18_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `4`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml` | `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:35:11` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_001_001_wave4_2_quantile_p10_p50_p90_global.yaml` | `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:25:04` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml` | `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:58` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml` | `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:25:51` |

## Run Details

### te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-13-11-13-46_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Source Config: `N/A`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T10:30:18`
- End Time: `2026-07-14T11:05:29`
- Duration: `00:35:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=136-val_mae=0.00353663.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-10-30-18_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/001_te_wave4_2_quantile_p10_p50_p90_bw__simplified_s.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_001_001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/queue/001_wave4_2_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T11:05:29`
- End Time: `2026-07-14T11:30:33`
- Duration: `00:25:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=096-val_mae=0.00351589.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-10-30-18_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/002_te_wave4_2_quantile_p10_p50_p90_global__simplifi.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_002_002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/queue/002_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T11:30:33`
- End Time: `2026-07-14T11:58:31`
- Duration: `00:27:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=098-val_mae=0.00349706.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-10-30-18_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/003_te_wave4_2_quantile_p10_p50_p90_fw__simplified_s.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/completed/2026-07-14-10-30-18_003_003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints/queue/003_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T11:58:31`
- End Time: `2026-07-14T12:24:22`
- Duration: `00:25:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=087-val_mae=0.00355108.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-10-30-18_dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified/logs/004_te_wave4_2_quantile_p10_p50_p90_bw__simplified_s.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
