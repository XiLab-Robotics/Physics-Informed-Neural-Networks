# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01`
- Generated At: `2026-05-20T12:25:49`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Completed Runs: `18`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-05-20-10-11-06_001_01_harmonic_regression_global_rcim_sparse.yaml` | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | `completed` | `00:06:17` |
| `config/training/queue/completed/2026-05-20-10-11-06_002_02_harmonic_regression_global_dense240.yaml` | `te_harmonic_dense240_tracking_global` | `harmonic_regression` | `completed` | `00:06:02` |
| `config/training/queue/completed/2026-05-20-10-11-06_003_03_harmonic_regression_global_dense360.yaml` | `te_harmonic_dense360_tracking_global` | `harmonic_regression` | `completed` | `00:08:57` |
| `config/training/queue/completed/2026-05-20-10-11-06_004_04_harmonic_regression_fw_rcim_sparse.yaml` | `te_harmonic_rcim_sparse_tracking_Fw` | `harmonic_regression` | `completed` | `00:05:05` |
| `config/training/queue/completed/2026-05-20-10-11-06_005_05_harmonic_regression_fw_dense240.yaml` | `te_harmonic_dense240_tracking_Fw` | `harmonic_regression` | `completed` | `00:05:56` |
| `config/training/queue/completed/2026-05-20-10-11-06_006_06_harmonic_regression_fw_dense360.yaml` | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | `completed` | `00:07:00` |
| `config/training/queue/completed/2026-05-20-10-11-06_007_07_harmonic_regression_bw_rcim_sparse.yaml` | `te_harmonic_rcim_sparse_tracking_Bw` | `harmonic_regression` | `completed` | `00:05:56` |
| `config/training/queue/completed/2026-05-20-10-11-06_008_08_harmonic_regression_bw_dense240.yaml` | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | `completed` | `00:05:00` |
| `config/training/queue/completed/2026-05-20-10-11-06_009_09_harmonic_regression_bw_dense360.yaml` | `te_harmonic_dense360_tracking_Bw` | `harmonic_regression` | `completed` | `00:06:43` |
| `config/training/queue/completed/2026-05-20-10-11-06_010_10_residual_harmonic_global_rcim_sparse.yaml` | `te_residual_harmonic_rcim_sparse_tracking_global` | `residual_harmonic_mlp` | `completed` | `00:08:03` |
| `config/training/queue/completed/2026-05-20-10-11-06_011_11_residual_harmonic_global_dense240.yaml` | `te_residual_harmonic_dense240_tracking_global` | `residual_harmonic_mlp` | `completed` | `00:11:07` |
| `config/training/queue/completed/2026-05-20-10-11-06_012_12_residual_harmonic_global_dense360.yaml` | `te_residual_harmonic_dense360_tracking_global` | `residual_harmonic_mlp` | `completed` | `00:13:52` |
| `config/training/queue/completed/2026-05-20-10-11-06_013_13_residual_harmonic_fw_rcim_sparse.yaml` | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | `completed` | `00:04:56` |
| `config/training/queue/completed/2026-05-20-10-11-06_014_14_residual_harmonic_fw_dense240.yaml` | `te_residual_harmonic_dense240_tracking_Fw` | `residual_harmonic_mlp` | `completed` | `00:05:04` |
| `config/training/queue/completed/2026-05-20-10-11-06_015_15_residual_harmonic_fw_dense360.yaml` | `te_residual_harmonic_dense360_tracking_Fw` | `residual_harmonic_mlp` | `completed` | `00:06:12` |
| `config/training/queue/completed/2026-05-20-10-11-06_016_16_residual_harmonic_bw_rcim_sparse.yaml` | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | `completed` | `00:06:07` |
| `config/training/queue/completed/2026-05-20-10-11-06_017_17_residual_harmonic_bw_dense240.yaml` | `te_residual_harmonic_dense240_tracking_Bw` | `residual_harmonic_mlp` | `completed` | `00:08:25` |
| `config/training/queue/completed/2026-05-20-10-11-06_018_18_residual_harmonic_bw_dense360.yaml` | `te_residual_harmonic_dense360_tracking_Bw` | `residual_harmonic_mlp` | `completed` | `00:14:01` |

## Run Details

### te_harmonic_rcim_sparse_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_001_01_harmonic_regression_global_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/01_harmonic_regression_global_rcim_sparse.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:11:06`
- End Time: `2026-05-20T10:17:23`
- Duration: `00:06:17`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global\checkpoints\harmonic_regression-epoch=039-val_mae=0.01699512.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/001_te_harmonic_rcim_sparse_tracking_global.log`
- Error Message: `N/A`

### te_harmonic_dense240_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_002_02_harmonic_regression_global_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/02_harmonic_regression_global_dense240.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-17-23__te_harmonic_dense240_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:17:23`
- End Time: `2026-05-20T10:23:25`
- Duration: `00:06:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-05-20-10-17-23__te_harmonic_dense240_tracking_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-17-23__te_harmonic_dense240_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-05-20-10-17-23__te_harmonic_dense240_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-17-23__te_harmonic_dense240_tracking_global\checkpoints\harmonic_regression-epoch=020-val_mae=0.01698888.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-17-23__te_harmonic_dense240_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-05-20-10-17-23__te_harmonic_dense240_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/002_te_harmonic_dense240_tracking_global.log`
- Error Message: `N/A`

### te_harmonic_dense360_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_003_03_harmonic_regression_global_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/03_harmonic_regression_global_dense360.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-23-25__te_harmonic_dense360_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:23:25`
- End Time: `2026-05-20T10:32:22`
- Duration: `00:08:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-05-20-10-23-25__te_harmonic_dense360_tracking_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-23-25__te_harmonic_dense360_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-05-20-10-23-25__te_harmonic_dense360_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-23-25__te_harmonic_dense360_tracking_global\checkpoints\harmonic_regression-epoch=030-val_mae=0.01699096.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-05-20-10-23-25__te_harmonic_dense360_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-05-20-10-23-25__te_harmonic_dense360_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/003_te_harmonic_dense360_tracking_global.log`
- Error Message: `N/A`

### te_harmonic_rcim_sparse_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_004_04_harmonic_regression_fw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/04_harmonic_regression_fw_rcim_sparse.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:32:22`
- End Time: `2026-05-20T10:37:26`
- Duration: `00:05:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_fw/2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw`
- Config Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_fw/2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw\checkpoints\harmonic_regression-epoch=028-val_mae=0.00256613.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_fw/2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/004_te_harmonic_rcim_sparse_tracking_fw.log`
- Error Message: `N/A`

### te_harmonic_dense240_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_005_05_harmonic_regression_fw_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/05_harmonic_regression_fw_dense240.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:37:26`
- End Time: `2026-05-20T10:43:22`
- Duration: `00:05:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_fw/2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw`
- Config Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_fw/2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw\checkpoints\harmonic_regression-epoch=040-val_mae=0.00259326.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_fw/2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/005_te_harmonic_dense240_tracking_fw.log`
- Error Message: `N/A`

### te_harmonic_dense360_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_006_06_harmonic_regression_fw_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/06_harmonic_regression_fw_dense360.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:43:22`
- End Time: `2026-05-20T10:50:22`
- Duration: `00:07:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw`
- Config Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw\checkpoints\harmonic_regression-epoch=053-val_mae=0.00261006.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_fw/2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/006_te_harmonic_dense360_tracking_fw.log`
- Error Message: `N/A`

### te_harmonic_rcim_sparse_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_007_07_harmonic_regression_bw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/07_harmonic_regression_bw_rcim_sparse.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:50:22`
- End Time: `2026-05-20T10:56:18`
- Duration: `00:05:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_bw/2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw`
- Config Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_bw/2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw\checkpoints\harmonic_regression-epoch=055-val_mae=0.00357006.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_bw/2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/007_te_harmonic_rcim_sparse_tracking_bw.log`
- Error Message: `N/A`

### te_harmonic_dense240_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_008_08_harmonic_regression_bw_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/08_harmonic_regression_bw_dense240.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T10:56:18`
- End Time: `2026-05-20T11:01:18`
- Duration: `00:05:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_bw/2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw`
- Config Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_bw/2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw\checkpoints\harmonic_regression-epoch=023-val_mae=0.00358755.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_bw/2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/008_te_harmonic_dense240_tracking_bw.log`
- Error Message: `N/A`

### te_harmonic_dense360_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_009_09_harmonic_regression_bw_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/09_harmonic_regression_bw_dense360.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:01:18`
- End Time: `2026-05-20T11:08:01`
- Duration: `00:06:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_bw/2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw`
- Config Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_bw/2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw\checkpoints\harmonic_regression-epoch=033-val_mae=0.00363716.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_bw/2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/009_te_harmonic_dense360_tracking_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_rcim_sparse_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_010_10_residual_harmonic_global_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/10_residual_harmonic_global_rcim_sparse.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:08:01`
- End Time: `2026-05-20T11:16:04`
- Duration: `00:08:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global\checkpoints\residual_harmonic_mlp-epoch=042-val_mae=0.00296875.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/010_te_residual_harmonic_rcim_sparse_tracking_global.log`
- Error Message: `N/A`

### te_residual_harmonic_dense240_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_011_11_residual_harmonic_global_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/11_residual_harmonic_global_dense240.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:16:04`
- End Time: `2026-05-20T11:27:11`
- Duration: `00:11:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global\checkpoints\residual_harmonic_mlp-epoch=070-val_mae=0.00297567.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/011_te_residual_harmonic_dense240_tracking_global.log`
- Error Message: `N/A`

### te_residual_harmonic_dense360_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_012_12_residual_harmonic_global_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/12_residual_harmonic_global_dense360.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:27:11`
- End Time: `2026-05-20T11:41:03`
- Duration: `00:13:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global\checkpoints\residual_harmonic_mlp-epoch=047-val_mae=0.00294320.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/012_te_residual_harmonic_dense360_tracking_global.log`
- Error Message: `N/A`

### te_residual_harmonic_rcim_sparse_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_013_13_residual_harmonic_fw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/13_residual_harmonic_fw_rcim_sparse.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:41:03`
- End Time: `2026-05-20T11:45:59`
- Duration: `00:04:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=029-val_mae=0.00270433.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/013_te_residual_harmonic_rcim_sparse_tracking_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_dense240_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_014_14_residual_harmonic_fw_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/14_residual_harmonic_fw_dense240.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:46:00`
- End Time: `2026-05-20T11:51:03`
- Duration: `00:05:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=019-val_mae=0.00264874.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/014_te_residual_harmonic_dense240_tracking_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_dense360_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_015_15_residual_harmonic_fw_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/15_residual_harmonic_fw_dense360.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:51:03`
- End Time: `2026-05-20T11:57:15`
- Duration: `00:06:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=022-val_mae=0.00259842.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_fw/2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/015_te_residual_harmonic_dense360_tracking_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_rcim_sparse_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_016_16_residual_harmonic_bw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/16_residual_harmonic_bw_rcim_sparse.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T11:57:15`
- End Time: `2026-05-20T12:03:22`
- Duration: `00:06:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=060-val_mae=0.00295293.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-11-57-15__te_residual_harmonic_rcim_sparse_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/016_te_residual_harmonic_rcim_sparse_tracking_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_dense240_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_017_17_residual_harmonic_bw_dense240.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/17_residual_harmonic_bw_dense240.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T12:03:22`
- End Time: `2026-05-20T12:11:48`
- Duration: `00:08:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=077-val_mae=0.00286149.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/017_te_residual_harmonic_dense240_tracking_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_dense360_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-10-11-06_018_18_residual_harmonic_bw_dense360.yaml`
- Source Config: `config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign/queue/18_residual_harmonic_bw_dense360.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-20T12:11:48`
- End Time: `2026-05-20T12:25:49`
- Duration: `00:14:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=122-val_mae=0.00282637.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_bw/2026-05-20-12-11-48__te_residual_harmonic_dense360_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-10-11-06_wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01/logs/018_te_residual_harmonic_dense360_tracking_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
