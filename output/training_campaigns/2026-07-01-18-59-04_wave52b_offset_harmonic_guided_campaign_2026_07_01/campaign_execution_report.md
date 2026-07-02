# Training Campaign Execution Report

## Overview

- Campaign Name: `wave52b_offset_harmonic_guided_campaign_2026_07_01`
- Generated At: `2026-07-02T02:27:12`
- Queue Root: `config/training/queue/wave52b_offset_harmonic_guided`
- Campaign Output Directory: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Completed Runs: `12`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_001_001_pointwise_control_global.yaml` | `te_wave52b_offset_harmonic_guided_pointwise_control_global` | `wave52b_offset_harmonic_guided` | `completed` | `00:55:18` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_002_002_pointwise_control_fw.yaml` | `te_wave52b_offset_harmonic_guided_pointwise_control_fw` | `wave52b_offset_harmonic_guided` | `completed` | `00:18:48` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_003_003_pointwise_control_bw.yaml` | `te_wave52b_offset_harmonic_guided_pointwise_control_bw` | `wave52b_offset_harmonic_guided` | `completed` | `00:29:15` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_004_004_offset_head_global.yaml` | `te_wave52b_offset_harmonic_guided_offset_head_global` | `wave52b_offset_harmonic_guided` | `completed` | `01:00:16` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_005_005_offset_head_fw.yaml` | `te_wave52b_offset_harmonic_guided_offset_head_fw` | `wave52b_offset_harmonic_guided` | `completed` | `00:21:45` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_006_006_offset_head_bw.yaml` | `te_wave52b_offset_harmonic_guided_offset_head_bw` | `wave52b_offset_harmonic_guided` | `completed` | `00:32:03` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_007_007_offset_centered_shape_global.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_global` | `wave52b_offset_harmonic_guided` | `completed` | `00:49:14` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_008_008_offset_centered_shape_fw.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `wave52b_offset_harmonic_guided` | `completed` | `00:36:47` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_009_009_offset_centered_shape_bw.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw` | `wave52b_offset_harmonic_guided` | `completed` | `00:35:50` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_010_010_offset_centered_shape_harmonic_global.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` | `completed` | `00:46:25` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_011_011_offset_centered_shape_harmonic_fw.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided` | `completed` | `00:32:31` |
| `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_012_012_offset_centered_shape_harmonic_bw.yaml` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided` | `completed` | `00:29:54` |

## Run Details

### te_wave52b_offset_harmonic_guided_pointwise_control_global

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_001_001_pointwise_control_global.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/001_pointwise_control_global.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T18:59:04`
- End Time: `2026-07-01T19:54:22`
- Duration: `00:55:18`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_global/2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_global/2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_global/2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_global\2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global\checkpoints\wave52b_offset_harmonic_guided-epoch=112-val_mae=0.00221041.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_global/2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_global/2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/001_te_wave52b_offset_harmonic_guided_pointwise_cont.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_pointwise_control_fw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_002_002_pointwise_control_fw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/002_pointwise_control_fw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T19:54:22`
- End Time: `2026-07-01T20:13:11`
- Duration: `00:18:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_fw/2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_fw/2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_fw/2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_fw\2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=062-val_mae=0.00234381.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_fw/2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_fw/2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/002_te_wave52b_offset_harmonic_guided_pointwise_cont.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_pointwise_control_bw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_003_003_pointwise_control_bw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/003_pointwise_control_bw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T20:13:11`
- End Time: `2026-07-01T20:42:26`
- Duration: `00:29:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_bw/2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_bw/2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_bw/2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_bw\2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=102-val_mae=0.00259094.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_bw/2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_pointwise_control_bw/2026-07-01-20-13-11__te_wave52b_offset_harmonic_guided_pointwise_control_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/003_te_wave52b_offset_harmonic_guided_pointwise_cont.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_head_global

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_004_004_offset_head_global.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/004_offset_head_global.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T20:42:26`
- End Time: `2026-07-01T21:42:42`
- Duration: `01:00:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_global/2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_global/2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_global/2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_global\2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global\checkpoints\wave52b_offset_harmonic_guided-epoch=092-val_mae=0.00224943.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_global/2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_global/2026-07-01-20-42-26__te_wave52b_offset_harmonic_guided_offset_head_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/004_te_wave52b_offset_harmonic_guided_offset_head_gl.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_head_fw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_005_005_offset_head_fw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/005_offset_head_fw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T21:42:42`
- End Time: `2026-07-01T22:04:27`
- Duration: `00:21:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_fw/2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_fw/2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_fw/2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_fw\2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=084-val_mae=0.00225646.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_fw/2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_fw/2026-07-01-21-42-42__te_wave52b_offset_harmonic_guided_offset_head_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/005_te_wave52b_offset_harmonic_guided_offset_head_fw.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_head_bw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_006_006_offset_head_bw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/006_offset_head_bw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T22:04:27`
- End Time: `2026-07-01T22:36:30`
- Duration: `00:32:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_bw/2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_bw/2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_bw/2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_bw\2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=098-val_mae=0.00259676.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_bw/2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_head_bw/2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/006_te_wave52b_offset_harmonic_guided_offset_head_bw.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_global

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_007_007_offset_centered_shape_global.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/007_offset_centered_shape_global.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T22:36:31`
- End Time: `2026-07-01T23:25:44`
- Duration: `00:49:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_global/2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_global/2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_global/2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_global\2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global\checkpoints\wave52b_offset_harmonic_guided-epoch=083-val_mae=0.00227055.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_global/2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_global/2026-07-01-22-36-30__te_wave52b_offset_harmonic_guided_offset_centered_shape_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/007_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_fw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_008_008_offset_centered_shape_fw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/008_offset_centered_shape_fw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T23:25:45`
- End Time: `2026-07-02T00:02:31`
- Duration: `00:36:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_fw/2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_fw/2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_fw/2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_fw\2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=155-val_mae=0.00225772.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_fw/2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_fw/2026-07-01-23-25-45__te_wave52b_offset_harmonic_guided_offset_centered_shape_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/008_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_bw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_009_009_offset_centered_shape_bw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/009_offset_centered_shape_bw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw`
- Queue Status: `completed`
- Start Time: `2026-07-02T00:02:32`
- End Time: `2026-07-02T00:38:22`
- Duration: `00:35:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_bw/2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_bw/2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_bw/2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_bw\2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=122-val_mae=0.00260437.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_bw/2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_bw/2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/009_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_010_010_offset_centered_shape_harmonic_global.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/010_offset_centered_shape_harmonic_global.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- Queue Status: `completed`
- Start Time: `2026-07-02T00:38:22`
- End Time: `2026-07-02T01:24:47`
- Duration: `00:46:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global\2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global\checkpoints\wave52b_offset_harmonic_guided-epoch=056-val_mae=0.00188588.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/2026-07-02-00-38-22__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/010_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_011_011_offset_centered_shape_harmonic_fw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/011_offset_centered_shape_harmonic_fw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- Queue Status: `completed`
- Start Time: `2026-07-02T01:24:47`
- End Time: `2026-07-02T01:57:18`
- Duration: `00:32:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=116-val_mae=0.00180918.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/011_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

### te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw

- Queue Config: `config/training/queue/wave52b_offset_harmonic_guided/completed/2026-07-01-18-59-04_012_012_offset_centered_shape_harmonic_bw.yaml`
- Source Config: `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue/012_offset_centered_shape_harmonic_bw.yaml`
- Model Type: `wave52b_offset_harmonic_guided`
- Run Instance Id: `2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`
- Queue Status: `completed`
- Start Time: `2026-07-02T01:57:18`
- End Time: `2026-07-02T02:27:12`
- Duration: `00:29:54`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`
- Config Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw\2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=082-val_mae=0.00231961.ckpt`
- Metrics Snapshot: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/2026-07-02-01-57-18__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/logs/012_te_wave52b_offset_harmonic_guided_offset_centere.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
