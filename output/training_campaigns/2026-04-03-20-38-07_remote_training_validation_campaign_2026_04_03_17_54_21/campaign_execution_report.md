# Training Campaign Execution Report

## Overview

- Campaign Name: `remote_training_validation_campaign_2026_04_03_17_54_21`
- Generated At: `2026-04-03T22:30:26`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Completed Runs: `4`
- Failed Runs: `1`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-04-03-20-38-07_001_01_random_forest_remote_medium.yaml` | `te_random_forest_remote_medium` | `random_forest` | `completed` | `00:39:14` |
| `config/training/queue/failed/2026-04-03-20-38-07_002_02_random_forest_remote_aggressive.yaml` | `te_random_forest_remote_aggressive` | `random_forest` | `failed` | `00:30:50` |
| `config/training/queue/completed/2026-04-03-20-38-07_003_03_hist_gbr_remote_deep.yaml` | `te_hist_gbr_remote_deep` | `hist_gradient_boosting` | `completed` | `00:01:55` |
| `config/training/queue/completed/2026-04-03-20-38-07_004_04_feedforward_high_compute_remote.yaml` | `te_feedforward_high_compute_remote` | `feedforward` | `completed` | `00:10:24` |
| `config/training/queue/completed/2026-04-03-20-38-07_005_05_feedforward_stride1_big_remote.yaml` | `te_feedforward_stride1_big_remote` | `feedforward` | `completed` | `00:29:55` |

## Run Details

### te_random_forest_remote_medium

- Queue Config: `config/training/queue/completed/2026-04-03-20-38-07_001_01_random_forest_remote_medium.yaml`
- Source Config: `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/01_random_forest_remote_medium.yaml`
- Model Type: `random_forest`
- Run Instance Id: `2026-04-03-20-38-07__te_random_forest_remote_medium`
- Queue Status: `completed`
- Start Time: `2026-04-03T20:38:07`
- End Time: `2026-04-03T21:17:21`
- Duration: `00:39:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-04-03-20-38-07__te_random_forest_remote_medium`
- Config Snapshot: `N/A`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21/logs/001_te_random_forest_remote_medium.log`
- Error Message: `N/A`

### te_random_forest_remote_aggressive

- Queue Config: `config/training/queue/failed/2026-04-03-20-38-07_002_02_random_forest_remote_aggressive.yaml`
- Source Config: `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/02_random_forest_remote_aggressive.yaml`
- Model Type: `random_forest`
- Run Instance Id: `2026-04-03-21-17-21__te_random_forest_remote_aggressive`
- Queue Status: `failed`
- Start Time: `2026-04-03T21:17:21`
- End Time: `2026-04-03T21:48:11`
- Duration: `00:30:50`
- Process Return Code: `N/A`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-04-03-21-17-21__te_random_forest_remote_aggressive`
- Config Snapshot: `output/training_runs/tree/2026-04-03-21-17-21__te_random_forest_remote_aggressive/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `N/A`
- Training Report: `N/A`
- Terminal Log: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21/logs/002_te_random_forest_remote_aggressive.log`
- Error Message: `could not allocate 536870912 bytes`

### te_hist_gbr_remote_deep

- Queue Config: `config/training/queue/completed/2026-04-03-20-38-07_003_03_hist_gbr_remote_deep.yaml`
- Source Config: `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/03_hist_gbr_remote_deep.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-04-03-21-48-11__te_hist_gbr_remote_deep`
- Queue Status: `completed`
- Start Time: `2026-04-03T21:48:11`
- End Time: `2026-04-03T21:50:07`
- Duration: `00:01:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep`
- Config Snapshot: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21/logs/003_te_hist_gbr_remote_deep.log`
- Error Message: `N/A`

### te_feedforward_high_compute_remote

- Queue Config: `config/training/queue/completed/2026-04-03-20-38-07_004_04_feedforward_high_compute_remote.yaml`
- Source Config: `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/04_feedforward_high_compute_remote.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-04-03-21-50-07__te_feedforward_high_compute_remote`
- Queue Status: `completed`
- Start Time: `2026-04-03T21:50:07`
- End Time: `2026-04-03T22:00:31`
- Duration: `00:10:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-04-03-21-50-07__te_feedforward_high_compute_remote`
- Config Snapshot: `output/training_runs/feedforward/2026-04-03-21-50-07__te_feedforward_high_compute_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-04-03-21-50-07__te_feedforward_high_compute_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-03-21-50-07__te_feedforward_high_compute_remote\checkpoints\feedforward-epoch=048-val_mae=0.00305896.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-04-03-21-50-07__te_feedforward_high_compute_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-04-03-21-50-07__te_feedforward_high_compute_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21/logs/004_te_feedforward_high_compute_remote.log`
- Error Message: `N/A`

### te_feedforward_stride1_big_remote

- Queue Config: `config/training/queue/completed/2026-04-03-20-38-07_005_05_feedforward_stride1_big_remote.yaml`
- Source Config: `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/05_feedforward_stride1_big_remote.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-04-03-22-00-31__te_feedforward_stride1_big_remote`
- Queue Status: `completed`
- Start Time: `2026-04-03T22:00:31`
- End Time: `2026-04-03T22:30:26`
- Duration: `00:29:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-04-03-22-00-31__te_feedforward_stride1_big_remote`
- Config Snapshot: `output/training_runs/feedforward/2026-04-03-22-00-31__te_feedforward_stride1_big_remote/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-04-03-22-00-31__te_feedforward_stride1_big_remote/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-03-22-00-31__te_feedforward_stride1_big_remote\checkpoints\feedforward-epoch=136-val_mae=0.00301873.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-04-03-22-00-31__te_feedforward_stride1_big_remote/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-04-03-22-00-31__te_feedforward_stride1_big_remote/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-04-03-20-38-07_remote_training_validation_campaign_2026_04_03_17_54_21/logs/005_te_feedforward_stride1_big_remote.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
