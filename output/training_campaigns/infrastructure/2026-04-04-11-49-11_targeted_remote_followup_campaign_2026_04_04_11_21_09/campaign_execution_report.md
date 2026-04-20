# Training Campaign Execution Report

## Overview

- Campaign Name: `targeted_remote_followup_campaign_2026_04_04_11_21_09`
- Generated At: `2026-04-04T13:03:55`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Completed Runs: `5`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-04-04-11-49-11_001_01_residual_h12_deep_long_remote.yaml` | `te_residual_h12_deep_long_remote` | `residual_harmonic_mlp` | `completed` | `00:15:58` |
| `config/training/queue/completed/2026-04-04-11-49-11_002_02_residual_h12_deep_dense_remote.yaml` | `te_residual_h12_deep_dense_remote` | `residual_harmonic_mlp` | `completed` | `00:13:28` |
| `config/training/queue/completed/2026-04-04-11-49-11_003_03_feedforward_high_compute_long_remote.yaml` | `te_feedforward_high_compute_long_remote` | `feedforward` | `completed` | `00:13:24` |
| `config/training/queue/completed/2026-04-04-11-49-11_004_04_feedforward_stride1_high_compute_long_remote.yaml` | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` | `completed` | `00:30:09` |
| `config/training/queue/completed/2026-04-04-11-49-11_005_05_hist_gbr_remote_refined.yaml` | `te_hist_gbr_remote_refined` | `hist_gradient_boosting` | `completed` | `00:01:46` |

## Run Details

### te_residual_h12_deep_long_remote

- Queue Config: `config/training/queue/completed/2026-04-04-11-49-11_001_01_residual_h12_deep_long_remote.yaml`
- Source Config: `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/01_residual_h12_deep_long_remote.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-04-04-11-49-11__te_residual_h12_deep_long_remote`
- Queue Status: `completed`
- Start Time: `2026-04-04T11:49:11`
- End Time: `2026-04-04T12:05:09`
- Duration: `00:15:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-04-04-11-49-11__te_residual_h12_deep_long_remote\checkpoints\residual_harmonic_mlp-epoch=080-val_mae=0.00297334.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-04-04-11-49-11__te_residual_h12_deep_long_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/logs/001_te_residual_h12_deep_long_remote.log`
- Error Message: `N/A`

### te_residual_h12_deep_dense_remote

- Queue Config: `config/training/queue/completed/2026-04-04-11-49-11_002_02_residual_h12_deep_dense_remote.yaml`
- Source Config: `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/02_residual_h12_deep_dense_remote.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-04-04-12-05-09__te_residual_h12_deep_dense_remote`
- Queue Status: `completed`
- Start Time: `2026-04-04T12:05:09`
- End Time: `2026-04-04T12:18:37`
- Duration: `00:13:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-04-04-12-05-09__te_residual_h12_deep_dense_remote\checkpoints\residual_harmonic_mlp-epoch=069-val_mae=0.00301834.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-04-04-12-05-09__te_residual_h12_deep_dense_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/logs/002_te_residual_h12_deep_dense_remote.log`
- Error Message: `N/A`

### te_feedforward_high_compute_long_remote

- Queue Config: `config/training/queue/completed/2026-04-04-11-49-11_003_03_feedforward_high_compute_long_remote.yaml`
- Source Config: `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/03_feedforward_high_compute_long_remote.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-04-04-12-18-37__te_feedforward_high_compute_long_remote`
- Queue Status: `completed`
- Start Time: `2026-04-04T12:18:37`
- End Time: `2026-04-04T12:32:00`
- Duration: `00:13:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote`
- Config Snapshot: `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-04-12-18-37__te_feedforward_high_compute_long_remote\checkpoints\feedforward-epoch=097-val_mae=0.00305764.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-04-04-12-18-37__te_feedforward_high_compute_long_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/logs/003_te_feedforward_high_compute_long_remote.log`
- Error Message: `N/A`

### te_feedforward_stride1_high_compute_long_remote

- Queue Config: `config/training/queue/completed/2026-04-04-11-49-11_004_04_feedforward_stride1_high_compute_long_remote.yaml`
- Source Config: `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/04_feedforward_stride1_high_compute_long_remote.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote`
- Queue Status: `completed`
- Start Time: `2026-04-04T12:32:00`
- End Time: `2026-04-04T13:02:09`
- Duration: `00:30:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote`
- Config Snapshot: `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote\checkpoints\feedforward-epoch=095-val_mae=0.00304393.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/logs/004_te_feedforward_stride1_high_compute_long_remote.log`
- Error Message: `N/A`

### te_hist_gbr_remote_refined

- Queue Config: `config/training/queue/completed/2026-04-04-11-49-11_005_05_hist_gbr_remote_refined.yaml`
- Source Config: `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/05_hist_gbr_remote_refined.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-04-04-13-02-09__te_hist_gbr_remote_refined`
- Queue Status: `completed`
- Start Time: `2026-04-04T13:02:09`
- End Time: `2026-04-04T13:03:55`
- Duration: `00:01:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-04-04-13-02-09__te_hist_gbr_remote_refined`
- Config Snapshot: `output/training_runs/tree/2026-04-04-13-02-09__te_hist_gbr_remote_refined/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-04-04-13-02-09__te_hist_gbr_remote_refined/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-04-04-13-02-09__te_hist_gbr_remote_refined/training_test_report.md`
- Terminal Log: `output/training_campaigns/infrastructure/2026-04-04-11-49-11_targeted_remote_followup_campaign_2026_04_04_11_21_09/logs/005_te_hist_gbr_remote_refined.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
