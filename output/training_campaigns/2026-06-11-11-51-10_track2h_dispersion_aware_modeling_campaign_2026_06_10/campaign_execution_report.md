# Training Campaign Execution Report

## Overview

- Campaign Name: `track2h_dispersion_aware_modeling_campaign_2026_06_10`
- Generated At: `2026-06-11T14:01:57`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Completed Runs: `9`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-11-11-51-10_001_01_mae_robust_global.yaml` | `te_track2h_mae_robust_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:16:33` |
| `config/training/queue/completed/2026-06-11-11-51-10_002_02_mae_robust_fw.yaml` | `te_track2h_mae_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:07:09` |
| `config/training/queue/completed/2026-06-11-11-51-10_003_03_mae_robust_bw.yaml` | `te_track2h_mae_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:18:22` |
| `config/training/queue/completed/2026-06-11-11-51-10_004_04_smooth_l1_robust_global.yaml` | `te_track2h_smooth_l1_robust_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:15:30` |
| `config/training/queue/completed/2026-06-11-11-51-10_005_05_smooth_l1_robust_fw.yaml` | `te_track2h_smooth_l1_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:07:42` |
| `config/training/queue/completed/2026-06-11-11-51-10_006_06_smooth_l1_robust_bw.yaml` | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:28:21` |
| `config/training/queue/completed/2026-06-11-11-51-10_007_07_log_cosh_robust_global.yaml` | `te_track2h_log_cosh_robust_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:18:16` |
| `config/training/queue/completed/2026-06-11-11-51-10_008_08_log_cosh_robust_fw.yaml` | `te_track2h_log_cosh_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:07:56` |
| `config/training/queue/completed/2026-06-11-11-51-10_009_09_log_cosh_robust_bw.yaml` | `te_track2h_log_cosh_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:10:56` |

## Run Details

### te_track2h_mae_robust_global

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_001_01_mae_robust_global.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/01_mae_robust_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-11-51-10__te_track2h_mae_robust_global`
- Queue Status: `completed`
- Start Time: `2026-06-11T11:51:10`
- End Time: `2026-06-11T12:07:43`
- Duration: `00:16:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-51-10__te_track2h_mae_robust_global`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-51-10__te_track2h_mae_robust_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-51-10__te_track2h_mae_robust_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_global\2026-06-11-11-51-10__te_track2h_mae_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=026-val_mae=0.00364502.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-51-10__te_track2h_mae_robust_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-51-10__te_track2h_mae_robust_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/001_te_track2h_mae_robust_global.log`
- Error Message: `N/A`

### te_track2h_mae_robust_fw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_002_02_mae_robust_fw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/02_mae_robust_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-12-07-43__te_track2h_mae_robust_fw`
- Queue Status: `completed`
- Start Time: `2026-06-11T12:07:43`
- End Time: `2026-06-11T12:14:52`
- Duration: `00:07:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_mae_robust_fw/2026-06-11-12-07-43__te_track2h_mae_robust_fw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_fw/2026-06-11-12-07-43__te_track2h_mae_robust_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_mae_robust_fw/2026-06-11-12-07-43__te_track2h_mae_robust_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_fw\2026-06-11-12-07-43__te_track2h_mae_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=012-val_mae=0.00325839.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_fw/2026-06-11-12-07-43__te_track2h_mae_robust_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_mae_robust_fw/2026-06-11-12-07-43__te_track2h_mae_robust_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/002_te_track2h_mae_robust_fw.log`
- Error Message: `N/A`

### te_track2h_mae_robust_bw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_003_03_mae_robust_bw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/03_mae_robust_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-12-14-52__te_track2h_mae_robust_bw`
- Queue Status: `completed`
- Start Time: `2026-06-11T12:14:52`
- End Time: `2026-06-11T12:33:14`
- Duration: `00:18:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_mae_robust_bw/2026-06-11-12-14-52__te_track2h_mae_robust_bw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_bw/2026-06-11-12-14-52__te_track2h_mae_robust_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_mae_robust_bw/2026-06-11-12-14-52__te_track2h_mae_robust_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_bw\2026-06-11-12-14-52__te_track2h_mae_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=145-val_mae=0.00357893.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_mae_robust_bw/2026-06-11-12-14-52__te_track2h_mae_robust_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_mae_robust_bw/2026-06-11-12-14-52__te_track2h_mae_robust_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/003_te_track2h_mae_robust_bw.log`
- Error Message: `N/A`

### te_track2h_smooth_l1_robust_global

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_004_04_smooth_l1_robust_global.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/04_smooth_l1_robust_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global`
- Queue Status: `completed`
- Start Time: `2026-06-11T12:33:14`
- End Time: `2026-06-11T12:48:44`
- Duration: `00:15:30`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_global/2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_global/2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_global/2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_global\2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=057-val_mae=0.00364085.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_global/2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_global/2026-06-11-12-33-14__te_track2h_smooth_l1_robust_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/004_te_track2h_smooth_l1_robust_global.log`
- Error Message: `N/A`

### te_track2h_smooth_l1_robust_fw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_005_05_smooth_l1_robust_fw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/05_smooth_l1_robust_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw`
- Queue Status: `completed`
- Start Time: `2026-06-11T12:48:44`
- End Time: `2026-06-11T12:56:26`
- Duration: `00:07:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_fw/2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_fw/2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_fw/2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_fw\2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=014-val_mae=0.00323536.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_fw/2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_fw/2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/005_te_track2h_smooth_l1_robust_fw.log`
- Error Message: `N/A`

### te_track2h_smooth_l1_robust_bw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_006_06_smooth_l1_robust_bw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/06_smooth_l1_robust_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw`
- Queue Status: `completed`
- Start Time: `2026-06-11T12:56:26`
- End Time: `2026-06-11T13:24:47`
- Duration: `00:28:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_bw/2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_bw/2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_bw/2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=231-val_mae=0.00337231.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_bw/2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_smooth_l1_robust_bw/2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/006_te_track2h_smooth_l1_robust_bw.log`
- Error Message: `N/A`

### te_track2h_log_cosh_robust_global

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_007_07_log_cosh_robust_global.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/07_log_cosh_robust_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-13-24-47__te_track2h_log_cosh_robust_global`
- Queue Status: `completed`
- Start Time: `2026-06-11T13:24:47`
- End Time: `2026-06-11T13:43:04`
- Duration: `00:18:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_global/2026-06-11-13-24-47__te_track2h_log_cosh_robust_global`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_global/2026-06-11-13-24-47__te_track2h_log_cosh_robust_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_global/2026-06-11-13-24-47__te_track2h_log_cosh_robust_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_global\2026-06-11-13-24-47__te_track2h_log_cosh_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=037-val_mae=0.00364458.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_global/2026-06-11-13-24-47__te_track2h_log_cosh_robust_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_global/2026-06-11-13-24-47__te_track2h_log_cosh_robust_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/007_te_track2h_log_cosh_robust_global.log`
- Error Message: `N/A`

### te_track2h_log_cosh_robust_fw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_008_08_log_cosh_robust_fw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/08_log_cosh_robust_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw`
- Queue Status: `completed`
- Start Time: `2026-06-11T13:43:04`
- End Time: `2026-06-11T13:51:00`
- Duration: `00:07:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_fw/2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_fw/2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_fw/2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_fw\2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=016-val_mae=0.00327980.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_fw/2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_fw/2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/008_te_track2h_log_cosh_robust_fw.log`
- Error Message: `N/A`

### te_track2h_log_cosh_robust_bw

- Queue Config: `config/training/queue/completed/2026-06-11-11-51-10_009_09_log_cosh_robust_bw.yaml`
- Source Config: `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/09_log_cosh_robust_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw`
- Queue Status: `completed`
- Start Time: `2026-06-11T13:51:00`
- End Time: `2026-06-11T14:01:57`
- Duration: `00:10:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_bw/2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw`
- Config Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_bw/2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_bw/2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_bw\2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=046-val_mae=0.00377404.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_bw/2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_dispersion_aware_log_cosh_robust_bw/2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/logs/009_te_track2h_log_cosh_robust_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
