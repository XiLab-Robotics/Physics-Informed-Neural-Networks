# Training Campaign Execution Report

## Overview

- Campaign Name: `track2g_curve_aware_training_campaign_2026_06_08`
- Generated At: `2026-06-08T22:05:10`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Completed Runs: `12`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-08-18-36-30_001_01_pointwise_control_global.yaml` | `te_track2g_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:20:29` |
| `config/training/queue/completed/2026-06-08-18-36-30_002_02_pointwise_control_fw.yaml` | `te_track2g_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:11:40` |
| `config/training/queue/completed/2026-06-08-18-36-30_003_03_pointwise_control_bw.yaml` | `te_track2g_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:14:29` |
| `config/training/queue/completed/2026-06-08-18-36-30_004_04_raw_centered_shape_global.yaml` | `te_track2g_curve_aware_raw_centered_shape_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:22:08` |
| `config/training/queue/completed/2026-06-08-18-36-30_005_05_raw_centered_shape_fw.yaml` | `te_track2g_curve_aware_raw_centered_shape_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:10:48` |
| `config/training/queue/completed/2026-06-08-18-36-30_006_06_raw_centered_shape_bw.yaml` | `te_track2g_curve_aware_raw_centered_shape_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:15:37` |
| `config/training/queue/completed/2026-06-08-18-36-30_007_07_raw_offset_global.yaml` | `te_track2g_curve_aware_raw_offset_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:11` |
| `config/training/queue/completed/2026-06-08-18-36-30_008_08_raw_offset_fw.yaml` | `te_track2g_curve_aware_raw_offset_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:07:42` |
| `config/training/queue/completed/2026-06-08-18-36-30_009_09_raw_offset_bw.yaml` | `te_track2g_curve_aware_raw_offset_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:15:22` |
| `config/training/queue/completed/2026-06-08-18-36-30_010_10_full_curve_composite_global.yaml` | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:32:15` |
| `config/training/queue/completed/2026-06-08-18-36-30_011_11_full_curve_composite_fw.yaml` | `te_track2g_curve_aware_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:10:35` |
| `config/training/queue/completed/2026-06-08-18-36-30_012_12_full_curve_composite_bw.yaml` | `te_track2g_curve_aware_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:15:23` |

## Run Details

### te_track2g_curve_aware_pointwise_control_global

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_001_01_pointwise_control_global.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/01_pointwise_control_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global`
- Queue Status: `completed`
- Start Time: `2026-06-08T18:36:30`
- End Time: `2026-06-08T18:56:59`
- Duration: `00:20:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_global\2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=038-val_mae=0.00360750.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/001_te_track2g_curve_aware_pointwise_control_global.log`
- Error Message: `N/A`

### te_track2g_curve_aware_pointwise_control_fw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_002_02_pointwise_control_fw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/02_pointwise_control_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw`
- Queue Status: `completed`
- Start Time: `2026-06-08T18:56:59`
- End Time: `2026-06-08T19:08:39`
- Duration: `00:11:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw/2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw/2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw/2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw\2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=043-val_mae=0.00329125.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw/2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw/2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/002_te_track2g_curve_aware_pointwise_control_fw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_pointwise_control_bw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_003_03_pointwise_control_bw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/03_pointwise_control_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw`
- Queue Status: `completed`
- Start Time: `2026-06-08T19:08:39`
- End Time: `2026-06-08T19:23:08`
- Duration: `00:14:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw/2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw/2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw/2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw\2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=106-val_mae=0.00374939.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw/2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw/2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/003_te_track2g_curve_aware_pointwise_control_bw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_centered_shape_global

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_004_04_raw_centered_shape_global.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/04_raw_centered_shape_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global`
- Queue Status: `completed`
- Start Time: `2026-06-08T19:23:08`
- End Time: `2026-06-08T19:45:16`
- Duration: `00:22:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global/2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global/2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global/2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global\2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=086-val_mae=0.00363586.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global/2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global/2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/004_te_track2g_curve_aware_raw_centered_shape_global.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_centered_shape_fw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_005_05_raw_centered_shape_fw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/05_raw_centered_shape_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw`
- Queue Status: `completed`
- Start Time: `2026-06-08T19:45:16`
- End Time: `2026-06-08T19:56:04`
- Duration: `00:10:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw/2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw/2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw/2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=036-val_mae=0.00325058.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw/2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw/2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/005_te_track2g_curve_aware_raw_centered_shape_fw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_centered_shape_bw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_006_06_raw_centered_shape_bw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/06_raw_centered_shape_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw`
- Queue Status: `completed`
- Start Time: `2026-06-08T19:56:04`
- End Time: `2026-06-08T20:11:41`
- Duration: `00:15:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw/2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw/2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw/2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw\2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=078-val_mae=0.00373978.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw/2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw/2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/006_te_track2g_curve_aware_raw_centered_shape_bw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_offset_global

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_007_07_raw_offset_global.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/07_raw_offset_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global`
- Queue Status: `completed`
- Start Time: `2026-06-08T20:11:41`
- End Time: `2026-06-08T20:43:53`
- Duration: `00:32:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_global/2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_global/2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_global/2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_global\2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=091-val_mae=0.00356422.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_global/2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_global/2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/007_te_track2g_curve_aware_raw_offset_global.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_offset_fw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_008_08_raw_offset_fw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/08_raw_offset_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw`
- Queue Status: `completed`
- Start Time: `2026-06-08T20:43:53`
- End Time: `2026-06-08T20:51:34`
- Duration: `00:07:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_fw/2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_fw/2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_fw/2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_fw\2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=009-val_mae=0.00332750.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_fw/2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_fw/2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/008_te_track2g_curve_aware_raw_offset_fw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_raw_offset_bw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_009_09_raw_offset_bw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/09_raw_offset_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw`
- Queue Status: `completed`
- Start Time: `2026-06-08T20:51:35`
- End Time: `2026-06-08T21:06:56`
- Duration: `00:15:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_bw/2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_bw/2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_bw/2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_bw\2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00375122.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_bw/2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_raw_offset_bw/2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/009_te_track2g_curve_aware_raw_offset_bw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_full_curve_composite_global

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_010_10_full_curve_composite_global.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/10_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global`
- Queue Status: `completed`
- Start Time: `2026-06-08T21:06:56`
- End Time: `2026-06-08T21:39:11`
- Duration: `00:32:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global\2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00361589.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-08-21-06-56__te_track2g_curve_aware_full_curve_composite_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/010_te_track2g_curve_aware_full_curve_composite_glob.log`
- Error Message: `N/A`

### te_track2g_curve_aware_full_curve_composite_fw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_011_11_full_curve_composite_fw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/11_full_curve_composite_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw`
- Queue Status: `completed`
- Start Time: `2026-06-08T21:39:11`
- End Time: `2026-06-08T21:49:46`
- Duration: `00:10:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw/2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw/2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw/2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw\2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=034-val_mae=0.00332007.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw/2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw/2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/011_te_track2g_curve_aware_full_curve_composite_fw.log`
- Error Message: `N/A`

### te_track2g_curve_aware_full_curve_composite_bw

- Queue Config: `config/training/queue/completed/2026-06-08-18-36-30_012_12_full_curve_composite_bw.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/12_full_curve_composite_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw`
- Queue Status: `completed`
- Start Time: `2026-06-08T21:49:46`
- End Time: `2026-06-08T22:05:10`
- Duration: `00:15:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw/2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw/2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw/2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw\2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00380311.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw/2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw/2026-06-08-21-49-46__te_track2g_curve_aware_full_curve_composite_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/logs/012_te_track2g_curve_aware_full_curve_composite_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
