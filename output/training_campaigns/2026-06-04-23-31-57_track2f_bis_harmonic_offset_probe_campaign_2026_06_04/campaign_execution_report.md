# Training Campaign Execution Report

## Overview

- Campaign Name: `track2f_bis_harmonic_offset_probe_campaign_2026_06_04`
- Generated At: `2026-06-04T23:58:31`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Completed Runs: `3`
- Failed Runs: `3`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-04-23-31-57_001_01_clean_sequential_residual_offset_control_global.yaml` | `te_track2f_bis_clean_residual_offset_global` | `sequential_residual_offset_probe` | `completed` | `00:11:40` |
| `config/training/queue/completed/2026-06-04-23-31-57_002_02_clean_sequential_residual_offset_control_fw.yaml` | `te_track2f_bis_clean_residual_offset_fw` | `sequential_residual_offset_probe` | `completed` | `00:05:16` |
| `config/training/queue/completed/2026-06-04-23-31-57_003_03_clean_sequential_residual_offset_control_bw.yaml` | `te_track2f_bis_clean_residual_offset_bw` | `sequential_residual_offset_probe` | `completed` | `00:09:37` |
| `config/training/queue/failed/2026-06-04-23-31-57_004_04_harmonic_residual_offset_probe_global.yaml` | `te_track2f_bis_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | `failed` | `00:00:00` |
| `config/training/queue/failed/2026-06-04-23-31-57_005_05_harmonic_residual_offset_probe_fw.yaml` | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | `failed` | `00:00:00` |
| `config/training/queue/failed/2026-06-04-23-31-57_006_06_harmonic_residual_offset_probe_bw.yaml` | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | `failed` | `00:00:00` |

## Run Details

### te_track2f_bis_clean_residual_offset_global

- Queue Config: `config/training/queue/completed/2026-06-04-23-31-57_001_01_clean_sequential_residual_offset_control_global.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/01_clean_sequential_residual_offset_control_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global`
- Queue Status: `completed`
- Start Time: `2026-06-04T23:31:57`
- End Time: `2026-06-04T23:43:38`
- Duration: `00:11:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_clean_sequential_residual_offset_global/2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global`
- Config Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_global/2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_clean_sequential_residual_offset_global/2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_global\2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global\checkpoints\sequential_residual_offset_probe-epoch=048-val_mae=0.00371694.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_global/2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_clean_sequential_residual_offset_global/2026-06-04-23-31-57__te_track2f_bis_clean_residual_offset_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/001_te_track2f_bis_clean_residual_offset_global.log`
- Error Message: `N/A`

### te_track2f_bis_clean_residual_offset_fw

- Queue Config: `config/training/queue/completed/2026-06-04-23-31-57_002_02_clean_sequential_residual_offset_control_fw.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/02_clean_sequential_residual_offset_control_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw`
- Queue Status: `completed`
- Start Time: `2026-06-04T23:43:38`
- End Time: `2026-06-04T23:48:53`
- Duration: `00:05:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_clean_sequential_residual_offset_fw/2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw`
- Config Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_fw/2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_clean_sequential_residual_offset_fw/2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_fw\2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw\checkpoints\sequential_residual_offset_probe-epoch=020-val_mae=0.00347412.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_fw/2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_clean_sequential_residual_offset_fw/2026-06-04-23-43-38__te_track2f_bis_clean_residual_offset_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/002_te_track2f_bis_clean_residual_offset_fw.log`
- Error Message: `N/A`

### te_track2f_bis_clean_residual_offset_bw

- Queue Config: `config/training/queue/completed/2026-06-04-23-31-57_003_03_clean_sequential_residual_offset_control_bw.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/03_clean_sequential_residual_offset_control_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw`
- Queue Status: `completed`
- Start Time: `2026-06-04T23:48:53`
- End Time: `2026-06-04T23:58:31`
- Duration: `00:09:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_clean_sequential_residual_offset_bw/2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw`
- Config Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_bw/2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2f_bis_clean_sequential_residual_offset_bw/2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2f_bis_clean_sequential_residual_offset_bw\2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw\checkpoints\sequential_residual_offset_probe-epoch=099-val_mae=0.00381964.ckpt`
- Metrics Snapshot: `output/training_runs/track2f_bis_clean_sequential_residual_offset_bw/2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2f_bis_clean_sequential_residual_offset_bw/2026-06-04-23-48-53__te_track2f_bis_clean_residual_offset_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/003_te_track2f_bis_clean_residual_offset_bw.log`
- Error Message: `N/A`

### te_track2f_bis_harmonic_residual_offset_global

- Queue Config: `config/training/queue/failed/2026-06-04-23-31-57_004_04_harmonic_residual_offset_probe_global.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/04_harmonic_residual_offset_probe_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global`
- Queue Status: `failed`
- Start Time: `2026-06-04T23:58:31`
- End Time: `2026-06-04T23:58:31`
- Duration: `00:00:00`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_global`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/004_te_track2f_bis_harmonic_residual_offset_global.log`
- Error Message: `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

### te_track2f_bis_harmonic_residual_offset_fw

- Queue Config: `config/training/queue/failed/2026-06-04-23-31-57_005_05_harmonic_residual_offset_probe_fw.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/05_harmonic_residual_offset_probe_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Queue Status: `failed`
- Start Time: `2026-06-04T23:58:31`
- End Time: `2026-06-04T23:58:31`
- Duration: `00:00:00`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_fw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_fw`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/005_te_track2f_bis_harmonic_residual_offset_fw.log`
- Error Message: `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

### te_track2f_bis_harmonic_residual_offset_bw

- Queue Config: `config/training/queue/failed/2026-06-04-23-31-57_006_06_harmonic_residual_offset_probe_bw.yaml`
- Source Config: `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/06_harmonic_residual_offset_probe_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw`
- Queue Status: `failed`
- Start Time: `2026-06-04T23:58:31`
- End Time: `2026-06-04T23:58:31`
- Duration: `00:00:00`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2f_bis_harmonic_residual_offset_bw/2026-06-04-23-58-31__te_track2f_bis_harmonic_residual_offset_bw`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/logs/006_te_track2f_bis_harmonic_residual_offset_bw.log`
- Error Message: `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
