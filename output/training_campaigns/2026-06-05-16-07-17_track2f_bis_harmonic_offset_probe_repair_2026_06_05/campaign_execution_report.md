# Training Campaign Execution Report

## Overview

- Campaign Name: `track2f_bis_harmonic_offset_probe_repair_2026_06_05`
- Generated At: `2026-06-05T16:44:49`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-05-16-07-17_001_2026_06_04_23_31_57_004_04_harmonic_residual_offset_probe_global.yaml` | `te_track2f_bis_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | `completed` | `00:12:05` |
| `config/training/queue/completed/2026-06-05-16-07-17_002_2026_06_04_23_31_57_005_05_harmonic_residual_offset_probe_fw.yaml` | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | `completed` | `00:13:16` |
| `config/training/queue/completed/2026-06-05-16-07-17_003_2026_06_04_23_31_57_006_06_harmonic_residual_offset_probe_bw.yaml` | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | `completed` | `00:12:11` |

## Run Details

### te_track2f_bis_harmonic_residual_offset_global

- Queue Config: `config/training/queue/completed/2026-06-05-16-07-17_001_2026_06_04_23_31_57_004_04_harmonic_residual_offset_probe_global.yaml`
- Source Config: `config/training/queue/failed/2026-06-04-23-31-57_004_04_harmonic_residual_offset_probe_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global`
- Queue Status: `completed`
- Start Time: `2026-06-05T16:07:17`
- End Time: `2026-06-05T16:19:21`
- Duration: `00:12:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global`
- Config Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_global\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global\checkpoints\harmonic_residual_offset_probe-epoch=050-val_mae=0.00365893.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05/logs/001_te_track2f_bis_harmonic_residual_offset_global.log`
- Error Message: `N/A`

### te_track2f_bis_harmonic_residual_offset_fw

- Queue Config: `config/training/queue/completed/2026-06-05-16-07-17_002_2026_06_04_23_31_57_005_05_harmonic_residual_offset_probe_fw.yaml`
- Source Config: `config/training/queue/failed/2026-06-04-23-31-57_005_05_harmonic_residual_offset_probe_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Queue Status: `completed`
- Start Time: `2026-06-05T16:19:21`
- End Time: `2026-06-05T16:32:38`
- Duration: `00:13:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Config Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_fw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw\checkpoints\harmonic_residual_offset_probe-epoch=175-val_mae=0.00294145.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05/logs/002_te_track2f_bis_harmonic_residual_offset_fw.log`
- Error Message: `N/A`

### te_track2f_bis_harmonic_residual_offset_bw

- Queue Config: `config/training/queue/completed/2026-06-05-16-07-17_003_2026_06_04_23_31_57_006_06_harmonic_residual_offset_probe_bw.yaml`
- Source Config: `config/training/queue/failed/2026-06-04-23-31-57_006_06_harmonic_residual_offset_probe_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw`
- Queue Status: `completed`
- Start Time: `2026-06-05T16:32:38`
- End Time: `2026-06-05T16:44:49`
- Duration: `00:12:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw`
- Config Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_harmonic_residual_offset_bw\2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw\checkpoints\harmonic_residual_offset_probe-epoch=171-val_mae=0.00355501.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-05-16-07-17_track2f_bis_harmonic_offset_probe_repair_2026_06_05/logs/003_te_track2f_bis_harmonic_residual_offset_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
