# Training Campaign Execution Report

## Overview

- Campaign Name: `track2f_offset_aware_probe_campaign_2026_06_03`
- Generated At: `2026-06-04T12:04:47`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-04-11-36-09_001_01_sequential_residual_offset_probe_global.yaml` | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | `completed` | `00:09:22` |
| `config/training/queue/completed/2026-06-04-11-36-09_002_02_sequential_residual_offset_probe_fw.yaml` | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe` | `completed` | `00:12:09` |
| `config/training/queue/completed/2026-06-04-11-36-09_003_03_sequential_residual_offset_probe_bw.yaml` | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe` | `completed` | `00:07:07` |

## Run Details

### te_sequential_residual_offset_probe_remote_global

- Queue Config: `config/training/queue/completed/2026-06-04-11-36-09_001_01_sequential_residual_offset_probe_global.yaml`
- Source Config: `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/01_sequential_residual_offset_probe_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global`
- Queue Status: `completed`
- Start Time: `2026-06-04T11:36:09`
- End Time: `2026-06-04T11:45:31`
- Duration: `00:09:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/sequential_residual_offset_probe/2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global`
- Config Snapshot: `output/training_runs/sequential_residual_offset_probe/2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/sequential_residual_offset_probe/2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe\2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global\checkpoints\sequential_residual_offset_probe-epoch=061-val_mae=0.00378313.ckpt`
- Metrics Snapshot: `output/training_runs/sequential_residual_offset_probe/2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/sequential_residual_offset_probe/2026-06-04-11-36-09__te_sequential_residual_offset_probe_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/logs/001_te_sequential_residual_offset_probe_remote_globa.log`
- Error Message: `N/A`

### te_sequential_residual_offset_probe_remote_fw

- Queue Config: `config/training/queue/completed/2026-06-04-11-36-09_002_02_sequential_residual_offset_probe_fw.yaml`
- Source Config: `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/02_sequential_residual_offset_probe_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-06-04T11:45:31`
- End Time: `2026-06-04T11:57:40`
- Duration: `00:12:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/sequential_residual_offset_probe_fw/2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw`
- Config Snapshot: `output/training_runs/sequential_residual_offset_probe_fw/2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/sequential_residual_offset_probe_fw/2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe_fw\2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw\checkpoints\sequential_residual_offset_probe-epoch=168-val_mae=0.00338001.ckpt`
- Metrics Snapshot: `output/training_runs/sequential_residual_offset_probe_fw/2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/sequential_residual_offset_probe_fw/2026-06-04-11-45-31__te_sequential_residual_offset_probe_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/logs/002_te_sequential_residual_offset_probe_remote_fw.log`
- Error Message: `N/A`

### te_sequential_residual_offset_probe_remote_bw

- Queue Config: `config/training/queue/completed/2026-06-04-11-36-09_003_03_sequential_residual_offset_probe_bw.yaml`
- Source Config: `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/03_sequential_residual_offset_probe_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-06-04T11:57:40`
- End Time: `2026-06-04T12:04:47`
- Duration: `00:07:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/sequential_residual_offset_probe_bw/2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw`
- Config Snapshot: `output/training_runs/sequential_residual_offset_probe_bw/2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/sequential_residual_offset_probe_bw/2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\sequential_residual_offset_probe_bw\2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw\checkpoints\sequential_residual_offset_probe-epoch=061-val_mae=0.00383996.ckpt`
- Metrics Snapshot: `output/training_runs/sequential_residual_offset_probe_bw/2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/sequential_residual_offset_probe_bw/2026-06-04-11-57-40__te_sequential_residual_offset_probe_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/logs/003_te_sequential_residual_offset_probe_remote_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
