# Training Campaign Execution Report

## Overview

- Campaign Name: `track2h_latent_state_hysteresis_campaign_2026_06_16`
- Generated At: `2026-06-16T19:34:05`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Completed Runs: `6`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-06-16-18-06-11_001_01_gru_offset_residual_global.yaml` | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | `completed` | `00:17:28` |
| `config/training/queue/completed/2026-06-16-18-06-11_002_02_gru_offset_residual_fw.yaml` | `te_track2h_l_gru_offset_residual_fw` | `latent_state_hysteresis_probe` | `completed` | `00:10:34` |
| `config/training/queue/completed/2026-06-16-18-06-11_003_03_gru_offset_residual_bw.yaml` | `te_track2h_l_gru_offset_residual_bw` | `latent_state_hysteresis_probe` | `completed` | `00:14:01` |
| `config/training/queue/completed/2026-06-16-18-06-11_004_04_causal_tcn_offset_residual_global.yaml` | `te_track2h_l_causal_tcn_offset_residual_global` | `latent_state_hysteresis_probe` | `completed` | `00:28:35` |
| `config/training/queue/completed/2026-06-16-18-06-11_005_05_causal_tcn_offset_residual_fw.yaml` | `te_track2h_l_causal_tcn_offset_residual_fw` | `latent_state_hysteresis_probe` | `completed` | `00:05:24` |
| `config/training/queue/completed/2026-06-16-18-06-11_006_06_causal_tcn_offset_residual_bw.yaml` | `te_track2h_l_causal_tcn_offset_residual_bw` | `latent_state_hysteresis_probe` | `completed` | `00:11:52` |

## Run Details

### te_track2h_l_gru_offset_residual_global

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_001_01_gru_offset_residual_global.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/01_gru_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global`
- Queue Status: `completed`
- Start Time: `2026-06-16T18:06:11`
- End Time: `2026-06-16T18:23:39`
- Duration: `00:17:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_global\2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=064-val_mae=0.00371717.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/001_te_track2h_l_gru_offset_residual_global.log`
- Error Message: `N/A`

### te_track2h_l_gru_offset_residual_fw

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_002_02_gru_offset_residual_fw.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/02_gru_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw`
- Queue Status: `completed`
- Start Time: `2026-06-16T18:23:39`
- End Time: `2026-06-16T18:34:12`
- Duration: `00:10:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_fw\2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=109-val_mae=0.00346843.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_fw/2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/002_te_track2h_l_gru_offset_residual_fw.log`
- Error Message: `N/A`

### te_track2h_l_gru_offset_residual_bw

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_003_03_gru_offset_residual_bw.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/03_gru_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw`
- Queue Status: `completed`
- Start Time: `2026-06-16T18:34:12`
- End Time: `2026-06-16T18:48:13`
- Duration: `00:14:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_bw\2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=149-val_mae=0.00383662.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_bw/2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/003_te_track2h_l_gru_offset_residual_bw.log`
- Error Message: `N/A`

### te_track2h_l_causal_tcn_offset_residual_global

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_004_04_causal_tcn_offset_residual_global.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/04_causal_tcn_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global`
- Queue Status: `completed`
- Start Time: `2026-06-16T18:48:13`
- End Time: `2026-06-16T19:16:49`
- Duration: `00:28:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_global\2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=152-val_mae=0.00354330.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_global/2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/004_te_track2h_l_causal_tcn_offset_residual_global.log`
- Error Message: `N/A`

### te_track2h_l_causal_tcn_offset_residual_fw

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_005_05_causal_tcn_offset_residual_fw.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/05_causal_tcn_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw`
- Queue Status: `completed`
- Start Time: `2026-06-16T19:16:49`
- End Time: `2026-06-16T19:22:12`
- Duration: `00:05:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw\2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=037-val_mae=0.00356529.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw/2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/005_te_track2h_l_causal_tcn_offset_residual_fw.log`
- Error Message: `N/A`

### te_track2h_l_causal_tcn_offset_residual_bw

- Queue Config: `config/training/queue/completed/2026-06-16-18-06-11_006_06_causal_tcn_offset_residual_bw.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/06_causal_tcn_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw`
- Queue Status: `completed`
- Start Time: `2026-06-16T19:22:13`
- End Time: `2026-06-16T19:34:05`
- Duration: `00:11:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw\2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=100-val_mae=0.00384011.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw/2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/logs/006_te_track2h_l_causal_tcn_offset_residual_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
