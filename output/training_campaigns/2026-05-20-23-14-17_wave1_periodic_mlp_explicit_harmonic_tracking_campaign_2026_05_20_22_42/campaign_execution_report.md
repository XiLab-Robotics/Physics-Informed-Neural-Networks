# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49`
- Generated At: `2026-05-21T09:38:37`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Completed Runs: `9`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-05-20-23-14-17_001_01_periodic_mlp_global_rcim_sparse.yaml` | `te_periodic_mlp_rcim_sparse_tracking_global` | `periodic_mlp` | `completed` | `07:47:34` |
| `config/training/queue/completed/2026-05-20-23-14-17_002_02_periodic_mlp_global_dense240.yaml` | `te_periodic_mlp_dense240_tracking_global` | `periodic_mlp` | `completed` | `00:20:22` |
| `config/training/queue/completed/2026-05-20-23-14-17_003_03_periodic_mlp_global_dense360.yaml` | `te_periodic_mlp_dense360_tracking_global` | `periodic_mlp` | `completed` | `00:50:45` |
| `config/training/queue/completed/2026-05-20-23-14-17_004_04_periodic_mlp_fw_rcim_sparse.yaml` | `te_periodic_mlp_rcim_sparse_tracking_Fw` | `periodic_mlp` | `completed` | `00:09:28` |
| `config/training/queue/completed/2026-05-20-23-14-17_005_05_periodic_mlp_fw_dense240.yaml` | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | `completed` | `00:13:21` |
| `config/training/queue/completed/2026-05-20-23-14-17_006_06_periodic_mlp_fw_dense360.yaml` | `te_periodic_mlp_dense360_tracking_Fw` | `periodic_mlp` | `completed` | `00:12:15` |
| `config/training/queue/completed/2026-05-20-23-14-17_007_07_periodic_mlp_bw_rcim_sparse.yaml` | `te_periodic_mlp_rcim_sparse_tracking_Bw` | `periodic_mlp` | `completed` | `00:09:57` |
| `config/training/queue/completed/2026-05-20-23-14-17_008_08_periodic_mlp_bw_dense240.yaml` | `te_periodic_mlp_dense240_tracking_Bw` | `periodic_mlp` | `completed` | `00:20:05` |
| `config/training/queue/completed/2026-05-20-23-14-17_009_09_periodic_mlp_bw_dense360.yaml` | `te_periodic_mlp_dense360_tracking_Bw` | `periodic_mlp` | `completed` | `00:20:33` |

## Run Details

### te_periodic_mlp_rcim_sparse_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_001_01_periodic_mlp_global_rcim_sparse.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/01_periodic_mlp_global_rcim_sparse.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-20T23:14:17`
- End Time: `2026-05-21T07:01:51`
- Duration: `07:47:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global\checkpoints\periodic_mlp-epoch=067-val_mae=0.00286316.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-05-20-23-14-17__te_periodic_mlp_rcim_sparse_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/001_te_periodic_mlp_rcim_sparse_tracking_global.log`
- Error Message: `N/A`

### te_periodic_mlp_dense240_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_002_02_periodic_mlp_global_dense240.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/02_periodic_mlp_global_dense240.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-21T07:01:51`
- End Time: `2026-05-21T07:22:12`
- Duration: `00:20:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global\checkpoints\periodic_mlp-epoch=025-val_mae=0.00296227.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-05-21-07-01-51__te_periodic_mlp_dense240_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/002_te_periodic_mlp_dense240_tracking_global.log`
- Error Message: `N/A`

### te_periodic_mlp_dense360_tracking_global

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_003_03_periodic_mlp_global_dense360.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/03_periodic_mlp_global_dense360.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global`
- Queue Status: `completed`
- Start Time: `2026-05-21T07:22:12`
- End Time: `2026-05-21T08:12:57`
- Duration: `00:50:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global\checkpoints\periodic_mlp-epoch=086-val_mae=0.00285943.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-05-21-07-22-12__te_periodic_mlp_dense360_tracking_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/003_te_periodic_mlp_dense360_tracking_global.log`
- Error Message: `N/A`

### te_periodic_mlp_rcim_sparse_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_004_04_periodic_mlp_fw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/04_periodic_mlp_fw_rcim_sparse.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-21T08:12:57`
- End Time: `2026-05-21T08:22:25`
- Duration: `00:09:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_fw/2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_fw/2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw\checkpoints\periodic_mlp-epoch=032-val_mae=0.00251598.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_fw/2026-05-21-08-12-57__te_periodic_mlp_rcim_sparse_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/004_te_periodic_mlp_rcim_sparse_tracking_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_dense240_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_005_05_periodic_mlp_fw_dense240.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/05_periodic_mlp_fw_dense240.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-21T08:22:25`
- End Time: `2026-05-21T08:35:46`
- Duration: `00:13:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw\checkpoints\periodic_mlp-epoch=039-val_mae=0.00254077.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_fw/2026-05-21-08-22-25__te_periodic_mlp_dense240_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/005_te_periodic_mlp_dense240_tracking_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_dense360_tracking_Fw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_006_06_periodic_mlp_fw_dense360.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/06_periodic_mlp_fw_dense360.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw`
- Queue Status: `completed`
- Start Time: `2026-05-21T08:35:46`
- End Time: `2026-05-21T08:48:01`
- Duration: `00:12:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_fw/2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_fw/2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw\checkpoints\periodic_mlp-epoch=017-val_mae=0.00252353.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_fw/2026-05-21-08-35-46__te_periodic_mlp_dense360_tracking_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/006_te_periodic_mlp_dense360_tracking_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_rcim_sparse_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_007_07_periodic_mlp_bw_rcim_sparse.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/07_periodic_mlp_bw_rcim_sparse.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-21T08:48:01`
- End Time: `2026-05-21T08:57:58`
- Duration: `00:09:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_bw/2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_bw/2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw\checkpoints\periodic_mlp-epoch=051-val_mae=0.00301058.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_bw/2026-05-21-08-48-01__te_periodic_mlp_rcim_sparse_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/007_te_periodic_mlp_rcim_sparse_tracking_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_dense240_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_008_08_periodic_mlp_bw_dense240.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/08_periodic_mlp_bw_dense240.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-21T08:57:58`
- End Time: `2026-05-21T09:18:03`
- Duration: `00:20:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_bw/2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_bw/2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw\checkpoints\periodic_mlp-epoch=073-val_mae=0.00304062.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_bw/2026-05-21-08-57-58__te_periodic_mlp_dense240_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/008_te_periodic_mlp_dense240_tracking_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_dense360_tracking_Bw

- Queue Config: `config/training/queue/completed/2026-05-20-23-14-17_009_09_periodic_mlp_bw_dense360.yaml`
- Source Config: `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/09_periodic_mlp_bw_dense360.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw`
- Queue Status: `completed`
- Start Time: `2026-05-21T09:18:03`
- End Time: `2026-05-21T09:38:37`
- Duration: `00:20:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_bw/2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_bw/2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw\checkpoints\periodic_mlp-epoch=056-val_mae=0.00307213.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_bw/2026-05-21-09-18-03__te_periodic_mlp_dense360_tracking_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42/logs/009_te_periodic_mlp_dense360_tracking_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
