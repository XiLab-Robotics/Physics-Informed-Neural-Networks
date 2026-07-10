# Training Campaign Execution Report

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints`
- Generated At: `2026-07-11T00:08:13`
- Queue Root: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints`
- Campaign Output Directory: `output/training_campaigns/2026-07-10-23-18-29_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplif`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_001_001_wave3_2_harmonic_residual_offset_global.yaml` | `te_wave3_2_harmonic_residual_offset_global__simplified_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:18:23` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_002_002_wave3_2_harmonic_residual_offset_fw.yaml` | `te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:15:10` |
| `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_003_003_wave3_2_harmonic_residual_offset_bw.yaml` | `te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints` | `harmonic_residual_offset_probe` | `completed` | `00:16:11` |

## Run Details

### te_wave3_2_harmonic_residual_offset_global__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_001_001_wave3_2_harmonic_residual_offset_global.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/queue/001_wave3_2_harmonic_residual_offset_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T23:18:29`
- End Time: `2026-07-10T23:36:51`
- Duration: `00:18:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=138-val_mae=0.00362371.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-23-18-29_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplif/logs/001_te_wave3_2_harmonic_residual_offset_global__simp.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_002_002_wave3_2_harmonic_residual_offset_fw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/queue/002_wave3_2_harmonic_residual_offset_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T23:36:51`
- End Time: `2026-07-10T23:52:02`
- Duration: `00:15:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=121-val_mae=0.00362257.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-23-18-29_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplif/logs/002_te_wave3_2_harmonic_residual_offset_fw__simplifi.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints

- Queue Config: `config/training/queue/dataset_input_mode_retraining/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/completed/2026-07-10-23-18-29_003_003_wave3_2_harmonic_residual_offset_bw.yaml`
- Source Config: `config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints/queue/003_wave3_2_harmonic_residual_offset_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints`
- Queue Status: `completed`
- Start Time: `2026-07-10T23:52:02`
- End Time: `2026-07-11T00:08:13`
- Duration: `00:16:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/input_modes/2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/best_checkpoint_path.txt`
- Best Checkpoint Path: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=091-val_mae=0.00361216.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-10-23-18-29_dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplif/logs/003_te_wave3_2_harmonic_residual_offset_bw__simplifi.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
