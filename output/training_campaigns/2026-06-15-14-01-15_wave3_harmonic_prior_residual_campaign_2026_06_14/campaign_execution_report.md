# Training Campaign Execution Report

## Overview

- Campaign Name: `wave3_harmonic_prior_residual_campaign_2026_06_14`
- Generated At: `2026-06-15T15:30:20`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Completed Runs: `6`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-15-14-01-15_001_01_pointwise_control_global.yaml` | `te_wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual` | `completed` | `00:26:08` |
| `config/training/queue/completed/2026-06-15-14-01-15_002_02_pointwise_control_fw.yaml` | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `wave3_harmonic_prior_residual` | `completed` | `00:07:10` |
| `config/training/queue/completed/2026-06-15-14-01-15_003_03_pointwise_control_bw.yaml` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | `completed` | `00:14:45` |
| `config/training/queue/completed/2026-06-15-14-01-15_004_04_smooth_l1_structured_global.yaml` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | `completed` | `00:19:38` |
| `config/training/queue/completed/2026-06-15-14-01-15_005_05_smooth_l1_structured_fw.yaml` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | `completed` | `00:07:28` |
| `config/training/queue/completed/2026-06-15-14-01-15_006_06_smooth_l1_structured_bw.yaml` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | `completed` | `00:13:56` |

## Run Details

### te_wave3_harmonic_prior_residual_pointwise_control_global

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_001_01_pointwise_control_global.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/01_pointwise_control_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global`
- Queue Status: `completed`
- Start Time: `2026-06-15T14:01:15`
- End Time: `2026-06-15T14:27:23`
- Duration: `00:26:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_global\2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global\checkpoints\wave3_harmonic_prior_residual-epoch=085-val_mae=0.00361072.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_global/2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/001_te_wave3_harmonic_prior_residual_pointwise_contr.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_pointwise_control_fw

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_002_02_pointwise_control_fw.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/02_pointwise_control_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw`
- Queue Status: `completed`
- Start Time: `2026-06-15T14:27:23`
- End Time: `2026-06-15T14:34:34`
- Duration: `00:07:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_fw\2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw\checkpoints\wave3_harmonic_prior_residual-epoch=013-val_mae=0.00331506.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_fw/2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/002_te_wave3_harmonic_prior_residual_pointwise_contr.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_pointwise_control_bw

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_003_03_pointwise_control_bw.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/03_pointwise_control_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw`
- Queue Status: `completed`
- Start Time: `2026-06-15T14:34:34`
- End Time: `2026-06-15T14:49:19`
- Duration: `00:14:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_bw\2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw\checkpoints\wave3_harmonic_prior_residual-epoch=123-val_mae=0.00363415.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_pointwise_control_bw/2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/003_te_wave3_harmonic_prior_residual_pointwise_contr.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_smooth_l1_structured_global

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_004_04_smooth_l1_structured_global.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/04_smooth_l1_structured_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Queue Status: `completed`
- Start Time: `2026-06-15T14:49:19`
- End Time: `2026-06-15T15:08:57`
- Duration: `00:19:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_global\2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=050-val_mae=0.00363290.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/004_te_wave3_harmonic_prior_residual_smooth_l1_struc.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_smooth_l1_structured_fw

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_005_05_smooth_l1_structured_fw.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/05_smooth_l1_structured_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw`
- Queue Status: `completed`
- Start Time: `2026-06-15T15:08:57`
- End Time: `2026-06-15T15:16:24`
- Duration: `00:07:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_fw\2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw\checkpoints\wave3_harmonic_prior_residual-epoch=016-val_mae=0.00331004.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_fw/2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/005_te_wave3_harmonic_prior_residual_smooth_l1_struc.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_smooth_l1_structured_bw

- Queue Config: `config/training/queue/completed/2026-06-15-14-01-15_006_06_smooth_l1_structured_bw.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/06_smooth_l1_structured_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw`
- Queue Status: `completed`
- Start Time: `2026-06-15T15:16:24`
- End Time: `2026-06-15T15:30:20`
- Duration: `00:13:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_bw\2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw\checkpoints\wave3_harmonic_prior_residual-epoch=114-val_mae=0.00364433.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_bw/2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/logs/006_te_wave3_harmonic_prior_residual_smooth_l1_struc.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
