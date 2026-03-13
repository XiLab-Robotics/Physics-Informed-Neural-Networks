# Training Campaign Execution Report

## Overview

- Campaign Name: `mixed_training_campaign_2026_03_12_15_32_28`
- Generated At: `2026-03-12T23:05:53`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Completed Runs: `9`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-03-12-18-52-30_001_01_stride10_long.yaml` | `te_feedforward_stride10_long` | `feedforward` | `completed` | `00:23:46` |
| `config/training/queue/completed/2026-03-12-18-52-30_002_02_stride5_long.yaml` | `te_feedforward_stride5_long` | `feedforward` | `completed` | `00:17:09` |
| `config/training/queue/completed/2026-03-12-18-52-30_003_03_stride1_long.yaml` | `te_feedforward_stride1_long` | `feedforward` | `completed` | `00:37:42` |
| `config/training/queue/completed/2026-03-12-18-52-30_004_04_stride10_long_large_batch.yaml` | `te_feedforward_stride10_long_large_batch` | `feedforward` | `completed` | `00:18:22` |
| `config/training/queue/completed/2026-03-12-18-52-30_005_05_stride5_long_large_batch.yaml` | `te_feedforward_stride5_long_large_batch` | `feedforward` | `completed` | `00:16:50` |
| `config/training/queue/completed/2026-03-12-18-52-30_006_06_stride1_long_large_batch.yaml` | `te_feedforward_stride1_long_large_batch` | `feedforward` | `completed` | `00:29:14` |
| `config/training/queue/completed/2026-03-12-18-52-30_007_07_stride10_long_large_batch_big_model.yaml` | `te_feedforward_stride10_long_large_batch_big_model` | `feedforward` | `completed` | `00:19:50` |
| `config/training/queue/completed/2026-03-12-18-52-30_008_08_stride5_long_large_batch_big_model.yaml` | `te_feedforward_stride5_long_large_batch_big_model` | `feedforward` | `completed` | `00:33:48` |
| `config/training/queue/completed/2026-03-12-18-52-30_009_09_stride1_long_large_batch_big_model.yaml` | `te_feedforward_stride1_long_large_batch_big_model` | `feedforward` | `completed` | `00:56:42` |

## Run Details

### te_feedforward_stride10_long

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_001_01_stride10_long.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/01_stride10_long.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T18:52:30`
- End Time: `2026-03-12T19:16:16`
- Duration: `00:23:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride10_long`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride10_long/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride10_long/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride10_long\checkpoints\feedforward-epoch=107-val_mae=0.00305276.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride10_long/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride10_long/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_001_01_stride10_long.log`
- Error Message: `N/A`

### te_feedforward_stride5_long

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_002_02_stride5_long.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/02_stride5_long.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T19:16:16`
- End Time: `2026-03-12T19:33:26`
- Duration: `00:17:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride5_long`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride5_long/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride5_long/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride5_long\checkpoints\feedforward-epoch=043-val_mae=0.00317790.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride5_long/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride5_long/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_002_02_stride5_long.log`
- Error Message: `N/A`

### te_feedforward_stride1_long

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_003_03_stride1_long.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/03_stride1_long.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T19:33:26`
- End Time: `2026-03-12T20:11:08`
- Duration: `00:37:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride1_long`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride1_long/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride1_long/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride1_long\checkpoints\feedforward-epoch=066-val_mae=0.00312552.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride1_long/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride1_long/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_003_03_stride1_long.log`
- Error Message: `N/A`

### te_feedforward_stride10_long_large_batch

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_004_04_stride10_long_large_batch.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/04_stride10_long_large_batch.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T20:11:08`
- End Time: `2026-03-12T20:29:30`
- Duration: `00:18:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride10_long_large_batch`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride10_long_large_batch/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride10_long_large_batch/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride10_long_large_batch\checkpoints\feedforward-epoch=111-val_mae=0.00306641.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride10_long_large_batch/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride10_long_large_batch/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_004_04_stride10_long_large_batch.log`
- Error Message: `N/A`

### te_feedforward_stride5_long_large_batch

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_005_05_stride5_long_large_batch.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/05_stride5_long_large_batch.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T20:29:30`
- End Time: `2026-03-12T20:46:20`
- Duration: `00:16:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride5_long_large_batch`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride5_long_large_batch/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride5_long_large_batch/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride5_long_large_batch\checkpoints\feedforward-epoch=081-val_mae=0.00310925.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride5_long_large_batch/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride5_long_large_batch/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_005_05_stride5_long_large_batch.log`
- Error Message: `N/A`

### te_feedforward_stride1_long_large_batch

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_006_06_stride1_long_large_batch.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/06_stride1_long_large_batch.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T20:46:20`
- End Time: `2026-03-12T21:15:33`
- Duration: `00:29:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride1_long_large_batch`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride1_long_large_batch/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride1_long_large_batch/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride1_long_large_batch\checkpoints\feedforward-epoch=050-val_mae=0.00310382.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride1_long_large_batch/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride1_long_large_batch/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_006_06_stride1_long_large_batch.log`
- Error Message: `N/A`

### te_feedforward_stride10_long_large_batch_big_model

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_007_07_stride10_long_large_batch_big_model.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/07_stride10_long_large_batch_big_model.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T21:15:33`
- End Time: `2026-03-12T21:35:23`
- Duration: `00:19:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride10_long_large_batch_big_model`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride10_long_large_batch_big_model/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride10_long_large_batch_big_model/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride10_long_large_batch_big_model\checkpoints\feedforward-epoch=067-val_mae=0.00303994.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride10_long_large_batch_big_model/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride10_long_large_batch_big_model/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_007_07_stride10_long_large_batch_big_model.log`
- Error Message: `N/A`

### te_feedforward_stride5_long_large_batch_big_model

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_008_08_stride5_long_large_batch_big_model.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/08_stride5_long_large_batch_big_model.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T21:35:23`
- End Time: `2026-03-12T22:09:11`
- Duration: `00:33:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride5_long_large_batch_big_model`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride5_long_large_batch_big_model/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride5_long_large_batch_big_model/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride5_long_large_batch_big_model\checkpoints\feedforward-epoch=104-val_mae=0.00310436.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride5_long_large_batch_big_model/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride5_long_large_batch_big_model/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_008_08_stride5_long_large_batch_big_model.log`
- Error Message: `N/A`

### te_feedforward_stride1_long_large_batch_big_model

- Queue Config: `config/training/queue/completed/2026-03-12-18-52-30_009_09_stride1_long_large_batch_big_model.yaml`
- Source Config: `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/09_stride1_long_large_batch_big_model.yaml`
- Model Type: `feedforward`
- Queue Status: `completed`
- Start Time: `2026-03-12T22:09:11`
- End Time: `2026-03-12T23:05:53`
- Duration: `00:56:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- Output Directory: `output/feedforward_network/te_feedforward_stride1_long_large_batch_big_model`
- Config Snapshot: `output/feedforward_network/te_feedforward_stride1_long_large_batch_big_model/feedforward_network_training.yaml`
- Best Checkpoint Pointer: `output/feedforward_network/te_feedforward_stride1_long_large_batch_big_model/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride1_long_large_batch_big_model\checkpoints\feedforward-epoch=078-val_mae=0.00308973.ckpt`
- Metrics Snapshot: `output/feedforward_network/te_feedforward_stride1_long_large_batch_big_model/training_test_metrics.yaml`
- Training Report: `output/feedforward_network/te_feedforward_stride1_long_large_batch_big_model/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/logs/2026-03-12-18-52-30_009_09_stride1_long_large_batch_big_model.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `training_test_metrics.yaml` for numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
