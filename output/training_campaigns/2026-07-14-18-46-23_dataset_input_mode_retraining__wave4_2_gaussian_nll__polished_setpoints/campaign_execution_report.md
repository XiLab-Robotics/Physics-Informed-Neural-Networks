# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints`
- Generated At: `2026-07-14T20:02:53`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-14-18-46-23_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_001_001_wave4_2_gaussian_nll_global.yaml` | `te_wave4_2_gaussian_nll_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:56:32` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_002_002_wave4_2_gaussian_nll_fw.yaml` | `te_wave4_2_gaussian_nll_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:09:59` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_003_003_wave4_2_gaussian_nll_bw.yaml` | `te_wave4_2_gaussian_nll_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:09:58` |

## Run Details

### te_wave4_2_gaussian_nll_global__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_001_001_wave4_2_gaussian_nll_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/queue/001_wave4_2_gaussian_nll_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T18:46:23`
- End Time: `2026-07-14T19:42:55`
- Duration: `00:56:32`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00188169.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-18-46-23_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/logs/001_te_wave4_2_gaussian_nll_global__polished_setpoin.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_fw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_002_002_wave4_2_gaussian_nll_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/queue/002_wave4_2_gaussian_nll_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T19:42:55`
- End Time: `2026-07-14T19:52:54`
- Duration: `00:09:59`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=001-val_mae=0.08819758.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-42-55__te_wave4_2_gaussian_nll_fw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-18-46-23_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/logs/002_te_wave4_2_gaussian_nll_fw__polished_setpoints.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_bw__polished_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/completed/2026-07-14-18-46-23_003_003_wave4_2_gaussian_nll_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/queue/003_wave4_2_gaussian_nll_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-14T19:52:54`
- End Time: `2026-07-14T20:02:53`
- Duration: `00:09:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.08419463.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-14-18-46-23_dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints/logs/003_te_wave4_2_gaussian_nll_bw__polished_setpoints.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
