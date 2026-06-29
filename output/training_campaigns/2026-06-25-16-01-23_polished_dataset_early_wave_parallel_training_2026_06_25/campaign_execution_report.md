# Training Campaign Execution Report

## Overview

- Campaign Name: `polished_dataset_early_wave_parallel_training_2026_06_25`
- Generated At: `2026-06-26T21:30:03`
- Queue Root: `config/training/queue/polished_dataset_early_wave_parallel_training`
- Campaign Output Directory: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-25-15-28-26_polished_early_wave_parallel_training_campaign_plan_report.md`
- Completed Runs: `36`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_001_001_tree_global.yaml` | `te_tree_global` | `hist_gradient_boosting` | `completed` | `00:03:00` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_002_002_tree_fw.yaml` | `te_tree_fw` | `hist_gradient_boosting` | `completed` | `00:02:29` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_003_003_tree_bw.yaml` | `te_tree_bw` | `hist_gradient_boosting` | `completed` | `00:02:24` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_004_004_residual_harmonic_mlp_global.yaml` | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | `completed` | `00:33:07` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_005_005_residual_harmonic_mlp_fw.yaml` | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | `completed` | `00:24:31` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_006_006_residual_harmonic_mlp_bw.yaml` | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | `completed` | `00:40:41` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_007_007_feedforward_global.yaml` | `te_feedforward_global` | `feedforward` | `completed` | `02:35:35` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_008_008_feedforward_fw.yaml` | `te_feedforward_fw` | `feedforward` | `completed` | `01:44:25` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_009_009_feedforward_bw.yaml` | `te_feedforward_bw` | `feedforward` | `completed` | `03:19:34` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_010_010_periodic_mlp_global.yaml` | `te_periodic_mlp_global` | `periodic_mlp` | `completed` | `00:29:56` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_011_011_periodic_mlp_fw.yaml` | `te_periodic_mlp_fw` | `periodic_mlp` | `completed` | `00:43:55` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_012_012_periodic_mlp_bw.yaml` | `te_periodic_mlp_bw` | `periodic_mlp` | `completed` | `00:40:10` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_013_013_harmonic_regression_global.yaml` | `te_harmonic_regression_global` | `harmonic_regression` | `completed` | `00:23:12` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_014_014_harmonic_regression_fw.yaml` | `te_harmonic_regression_fw` | `harmonic_regression` | `completed` | `00:15:42` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_015_015_harmonic_regression_bw.yaml` | `te_harmonic_regression_bw` | `harmonic_regression` | `completed` | `00:19:57` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_016_016_periodic_mlp_harmonic_global.yaml` | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | `completed` | `00:42:19` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_017_017_periodic_mlp_harmonic_fw.yaml` | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | `completed` | `00:38:01` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_018_018_periodic_mlp_harmonic_bw.yaml` | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | `completed` | `00:39:46` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_019_019_temporal_convolution_global.yaml` | `te_temporal_convolution_global` | `temporal_convolution` | `completed` | `00:29:33` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_020_020_temporal_convolution_fw.yaml` | `te_temporal_convolution_fw` | `temporal_convolution` | `completed` | `00:33:25` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_021_021_temporal_convolution_bw.yaml` | `te_temporal_convolution_bw` | `temporal_convolution` | `completed` | `00:33:57` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_022_022_gru_sequence_global.yaml` | `te_gru_sequence_global` | `gru_sequence` | `completed` | `00:56:28` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_023_023_gru_sequence_fw.yaml` | `te_gru_sequence_fw` | `gru_sequence` | `completed` | `00:35:12` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_024_024_gru_sequence_bw.yaml` | `te_gru_sequence_bw` | `gru_sequence` | `completed` | `00:42:04` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_025_025_lstm_sequence_global.yaml` | `te_lstm_sequence_global` | `lstm_sequence` | `completed` | `00:52:04` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_026_026_lstm_sequence_fw.yaml` | `te_lstm_sequence_fw` | `lstm_sequence` | `completed` | `00:47:50` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_027_027_lstm_sequence_bw.yaml` | `te_lstm_sequence_bw` | `lstm_sequence` | `completed` | `00:50:56` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_028_028_periodic_temporal_convolution_global.yaml` | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | `completed` | `00:22:15` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_029_029_periodic_temporal_convolution_fw.yaml` | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | `completed` | `00:31:41` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_030_030_periodic_temporal_convolution_bw.yaml` | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | `completed` | `00:27:06` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_031_031_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | `completed` | `01:02:53` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_032_032_periodic_gru_sequence_fw.yaml` | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | `completed` | `01:20:41` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_033_033_periodic_gru_sequence_bw.yaml` | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | `completed` | `01:21:37` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_034_034_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | `completed` | `01:27:51` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_035_035_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | `completed` | `00:59:17` |
| `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_036_036_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | `completed` | `01:14:57` |

## Run Details

### te_tree_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_001_001_tree_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/001_tree_global.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-25-16-01-23__te_tree_global`
- Queue Status: `completed`
- Start Time: `2026-06-25T16:01:23`
- End Time: `2026-06-25T16:04:23`
- Duration: `00:03:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-25-16-01-23__te_tree_global`
- Config Snapshot: `output/training_runs/tree/2026-06-25-16-01-23__te_tree_global/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-25-16-01-23__te_tree_global/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-25-16-01-23__te_tree_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/001_te_tree_global.log`
- Error Message: `N/A`

### te_tree_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_002_002_tree_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/002_tree_fw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-25-16-04-23__te_tree_fw`
- Queue Status: `completed`
- Start Time: `2026-06-25T16:04:23`
- End Time: `2026-06-25T16:06:52`
- Duration: `00:02:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-25-16-04-23__te_tree_fw`
- Config Snapshot: `output/training_runs/tree/2026-06-25-16-04-23__te_tree_fw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-25-16-04-23__te_tree_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-25-16-04-23__te_tree_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/002_te_tree_fw.log`
- Error Message: `N/A`

### te_tree_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_003_003_tree_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/003_tree_bw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-25-16-06-52__te_tree_bw`
- Queue Status: `completed`
- Start Time: `2026-06-25T16:06:52`
- End Time: `2026-06-25T16:09:16`
- Duration: `00:02:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-25-16-06-52__te_tree_bw`
- Config Snapshot: `output/training_runs/tree/2026-06-25-16-06-52__te_tree_bw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-25-16-06-52__te_tree_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-25-16-06-52__te_tree_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/003_te_tree_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_004_004_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/004_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-25-16-09-16__te_residual_harmonic_mlp_global`
- Queue Status: `completed`
- Start Time: `2026-06-25T16:09:16`
- End Time: `2026-06-25T16:42:24`
- Duration: `00:33:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-09-16__te_residual_harmonic_mlp_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-09-16__te_residual_harmonic_mlp_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-09-16__te_residual_harmonic_mlp_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-16-09-16__te_residual_harmonic_mlp_global\checkpoints\residual_harmonic_mlp-epoch=112-val_mae=0.00165991.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-09-16__te_residual_harmonic_mlp_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-09-16__te_residual_harmonic_mlp_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/004_te_residual_harmonic_mlp_global.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_005_005_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/005_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-25-16-42-24__te_residual_harmonic_mlp_fw`
- Queue Status: `completed`
- Start Time: `2026-06-25T16:42:24`
- End Time: `2026-06-25T17:06:54`
- Duration: `00:24:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-42-24__te_residual_harmonic_mlp_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-42-24__te_residual_harmonic_mlp_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-42-24__te_residual_harmonic_mlp_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-16-42-24__te_residual_harmonic_mlp_fw\checkpoints\residual_harmonic_mlp-epoch=075-val_mae=0.00164699.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-42-24__te_residual_harmonic_mlp_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-25-16-42-24__te_residual_harmonic_mlp_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/005_te_residual_harmonic_mlp_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_006_006_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/006_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-25-17-06-54__te_residual_harmonic_mlp_bw`
- Queue Status: `completed`
- Start Time: `2026-06-25T17:06:54`
- End Time: `2026-06-25T17:47:36`
- Duration: `00:40:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-25-17-06-54__te_residual_harmonic_mlp_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-17-06-54__te_residual_harmonic_mlp_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-25-17-06-54__te_residual_harmonic_mlp_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-17-06-54__te_residual_harmonic_mlp_bw\checkpoints\residual_harmonic_mlp-epoch=131-val_mae=0.00160855.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-25-17-06-54__te_residual_harmonic_mlp_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-25-17-06-54__te_residual_harmonic_mlp_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/006_te_residual_harmonic_mlp_bw.log`
- Error Message: `N/A`

### te_feedforward_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_007_007_feedforward_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/007_feedforward_global.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-25-17-47-36__te_feedforward_global`
- Queue Status: `completed`
- Start Time: `2026-06-25T17:47:36`
- End Time: `2026-06-25T20:23:10`
- Duration: `02:35:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-25-17-47-36__te_feedforward_global`
- Config Snapshot: `output/training_runs/feedforward/2026-06-25-17-47-36__te_feedforward_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-25-17-47-36__te_feedforward_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-06-25-17-47-36__te_feedforward_global\checkpoints\feedforward-epoch=123-val_mae=0.00163670.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-25-17-47-36__te_feedforward_global/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-25-17-47-36__te_feedforward_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/007_te_feedforward_global.log`
- Error Message: `N/A`

### te_feedforward_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_008_008_feedforward_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/008_feedforward_fw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-25-20-23-10__te_feedforward_fw`
- Queue Status: `completed`
- Start Time: `2026-06-25T20:23:10`
- End Time: `2026-06-25T22:07:36`
- Duration: `01:44:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-25-20-23-10__te_feedforward_fw`
- Config Snapshot: `output/training_runs/feedforward/2026-06-25-20-23-10__te_feedforward_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-25-20-23-10__te_feedforward_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-06-25-20-23-10__te_feedforward_fw\checkpoints\feedforward-epoch=092-val_mae=0.00162825.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-25-20-23-10__te_feedforward_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-25-20-23-10__te_feedforward_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/008_te_feedforward_fw.log`
- Error Message: `N/A`

### te_feedforward_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_009_009_feedforward_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/009_feedforward_bw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-25-22-07-36__te_feedforward_bw`
- Queue Status: `completed`
- Start Time: `2026-06-25T22:07:36`
- End Time: `2026-06-26T01:27:11`
- Duration: `03:19:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-25-22-07-36__te_feedforward_bw`
- Config Snapshot: `output/training_runs/feedforward/2026-06-25-22-07-36__te_feedforward_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-25-22-07-36__te_feedforward_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-06-25-22-07-36__te_feedforward_bw\checkpoints\feedforward-epoch=200-val_mae=0.00160556.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-25-22-07-36__te_feedforward_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-25-22-07-36__te_feedforward_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/009_te_feedforward_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_010_010_periodic_mlp_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/010_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-01-27-11__te_periodic_mlp_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T01:27:11`
- End Time: `2026-06-26T01:57:07`
- Duration: `00:29:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-26-01-27-11__te_periodic_mlp_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-26-01-27-11__te_periodic_mlp_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-26-01-27-11__te_periodic_mlp_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-01-27-11__te_periodic_mlp_global\checkpoints\periodic_mlp-epoch=082-val_mae=0.00163440.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-26-01-27-11__te_periodic_mlp_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-26-01-27-11__te_periodic_mlp_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/010_te_periodic_mlp_global.log`
- Error Message: `N/A`

### te_periodic_mlp_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_011_011_periodic_mlp_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/011_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-01-57-07__te_periodic_mlp_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T01:57:07`
- End Time: `2026-06-26T02:41:02`
- Duration: `00:43:55`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-26-01-57-07__te_periodic_mlp_fw`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-26-01-57-07__te_periodic_mlp_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-26-01-57-07__te_periodic_mlp_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-01-57-07__te_periodic_mlp_fw\checkpoints\periodic_mlp-epoch=144-val_mae=0.00159747.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-26-01-57-07__te_periodic_mlp_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-26-01-57-07__te_periodic_mlp_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/011_te_periodic_mlp_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_012_012_periodic_mlp_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/012_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-02-41-02__te_periodic_mlp_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T02:41:02`
- End Time: `2026-06-26T03:21:12`
- Duration: `00:40:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-26-02-41-02__te_periodic_mlp_bw`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-26-02-41-02__te_periodic_mlp_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-26-02-41-02__te_periodic_mlp_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-02-41-02__te_periodic_mlp_bw\checkpoints\periodic_mlp-epoch=128-val_mae=0.00161062.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-26-02-41-02__te_periodic_mlp_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-26-02-41-02__te_periodic_mlp_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/012_te_periodic_mlp_bw.log`
- Error Message: `N/A`

### te_harmonic_regression_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_013_013_harmonic_regression_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/013_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-26-03-21-12__te_harmonic_regression_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T03:21:12`
- End Time: `2026-06-26T03:44:24`
- Duration: `00:23:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-26-03-21-12__te_harmonic_regression_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-26-03-21-12__te_harmonic_regression_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-26-03-21-12__te_harmonic_regression_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-03-21-12__te_harmonic_regression_global\checkpoints\harmonic_regression-epoch=055-val_mae=0.00387866.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-26-03-21-12__te_harmonic_regression_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-26-03-21-12__te_harmonic_regression_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/013_te_harmonic_regression_global.log`
- Error Message: `N/A`

### te_harmonic_regression_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_014_014_harmonic_regression_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/014_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-26-03-44-24__te_harmonic_regression_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T03:44:24`
- End Time: `2026-06-26T04:00:06`
- Duration: `00:15:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-26-03-44-24__te_harmonic_regression_fw`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-26-03-44-24__te_harmonic_regression_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-26-03-44-24__te_harmonic_regression_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-03-44-24__te_harmonic_regression_fw\checkpoints\harmonic_regression-epoch=050-val_mae=0.00388663.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-26-03-44-24__te_harmonic_regression_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-26-03-44-24__te_harmonic_regression_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/014_te_harmonic_regression_fw.log`
- Error Message: `N/A`

### te_harmonic_regression_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_015_015_harmonic_regression_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/015_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-26-04-00-06__te_harmonic_regression_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T04:00:06`
- End Time: `2026-06-26T04:20:03`
- Duration: `00:19:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-26-04-00-06__te_harmonic_regression_bw`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-26-04-00-06__te_harmonic_regression_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-26-04-00-06__te_harmonic_regression_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-04-00-06__te_harmonic_regression_bw\checkpoints\harmonic_regression-epoch=039-val_mae=0.00388820.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-26-04-00-06__te_harmonic_regression_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-26-04-00-06__te_harmonic_regression_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/015_te_harmonic_regression_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_016_016_periodic_mlp_harmonic_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/016_periodic_mlp_harmonic_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-04-20-03__te_periodic_mlp_harmonic_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T04:20:03`
- End Time: `2026-06-26T05:02:22`
- Duration: `00:42:19`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-26-04-20-03__te_periodic_mlp_harmonic_global`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-04-20-03__te_periodic_mlp_harmonic_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-26-04-20-03__te_periodic_mlp_harmonic_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-04-20-03__te_periodic_mlp_harmonic_global\checkpoints\periodic_mlp-epoch=138-val_mae=0.00119613.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-04-20-03__te_periodic_mlp_harmonic_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-26-04-20-03__te_periodic_mlp_harmonic_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/016_te_periodic_mlp_harmonic_global.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_017_017_periodic_mlp_harmonic_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/017_periodic_mlp_harmonic_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T05:02:22`
- End Time: `2026-06-26T05:40:23`
- Duration: `00:38:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw\checkpoints\periodic_mlp-epoch=117-val_mae=0.00114445.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/017_te_periodic_mlp_harmonic_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_018_018_periodic_mlp_harmonic_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/018_periodic_mlp_harmonic_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T05:40:23`
- End Time: `2026-06-26T06:20:09`
- Duration: `00:39:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw\checkpoints\periodic_mlp-epoch=126-val_mae=0.00110253.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/018_te_periodic_mlp_harmonic_bw.log`
- Error Message: `N/A`

### te_temporal_convolution_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_019_019_temporal_convolution_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/019_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-26-06-20-09__te_temporal_convolution_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T06:20:09`
- End Time: `2026-06-26T06:49:42`
- Duration: `00:29:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-26-06-20-09__te_temporal_convolution_global`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-26-06-20-09__te_temporal_convolution_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-26-06-20-09__te_temporal_convolution_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-06-20-09__te_temporal_convolution_global\checkpoints\temporal_convolution-epoch=080-val_mae=0.00230806.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-26-06-20-09__te_temporal_convolution_global/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-26-06-20-09__te_temporal_convolution_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/019_te_temporal_convolution_global.log`
- Error Message: `N/A`

### te_temporal_convolution_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_020_020_temporal_convolution_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/020_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-26-06-49-42__te_temporal_convolution_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T06:49:42`
- End Time: `2026-06-26T07:23:08`
- Duration: `00:33:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-26-06-49-42__te_temporal_convolution_fw`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-26-06-49-42__te_temporal_convolution_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-26-06-49-42__te_temporal_convolution_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-06-49-42__te_temporal_convolution_fw\checkpoints\temporal_convolution-epoch=069-val_mae=0.00231121.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-26-06-49-42__te_temporal_convolution_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-26-06-49-42__te_temporal_convolution_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/020_te_temporal_convolution_fw.log`
- Error Message: `N/A`

### te_temporal_convolution_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_021_021_temporal_convolution_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/021_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-26-07-23-08__te_temporal_convolution_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T07:23:08`
- End Time: `2026-06-26T07:57:05`
- Duration: `00:33:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-26-07-23-08__te_temporal_convolution_bw`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-26-07-23-08__te_temporal_convolution_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-26-07-23-08__te_temporal_convolution_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-07-23-08__te_temporal_convolution_bw\checkpoints\temporal_convolution-epoch=071-val_mae=0.00230252.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-26-07-23-08__te_temporal_convolution_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-26-07-23-08__te_temporal_convolution_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/021_te_temporal_convolution_bw.log`
- Error Message: `N/A`

### te_gru_sequence_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_022_022_gru_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/022_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-26-07-57-05__te_gru_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T07:57:05`
- End Time: `2026-06-26T08:53:33`
- Duration: `00:56:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-26-07-57-05__te_gru_sequence_global`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-26-07-57-05__te_gru_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-26-07-57-05__te_gru_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-07-57-05__te_gru_sequence_global\checkpoints\gru_sequence-epoch=182-val_mae=0.00212575.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-26-07-57-05__te_gru_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-26-07-57-05__te_gru_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/022_te_gru_sequence_global.log`
- Error Message: `N/A`

### te_gru_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_023_023_gru_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/023_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-26-08-53-33__te_gru_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T08:53:33`
- End Time: `2026-06-26T09:28:46`
- Duration: `00:35:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-26-08-53-33__te_gru_sequence_fw`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-26-08-53-33__te_gru_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-26-08-53-33__te_gru_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-08-53-33__te_gru_sequence_fw\checkpoints\gru_sequence-epoch=083-val_mae=0.00215611.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-26-08-53-33__te_gru_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-26-08-53-33__te_gru_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/023_te_gru_sequence_fw.log`
- Error Message: `N/A`

### te_gru_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_024_024_gru_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/024_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-26-09-28-46__te_gru_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T09:28:46`
- End Time: `2026-06-26T10:10:50`
- Duration: `00:42:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-26-09-28-46__te_gru_sequence_bw`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-26-09-28-46__te_gru_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-26-09-28-46__te_gru_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-09-28-46__te_gru_sequence_bw\checkpoints\gru_sequence-epoch=094-val_mae=0.00214655.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-26-09-28-46__te_gru_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-26-09-28-46__te_gru_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/024_te_gru_sequence_bw.log`
- Error Message: `N/A`

### te_lstm_sequence_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_025_025_lstm_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/025_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-26-10-10-51__te_lstm_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T10:10:51`
- End Time: `2026-06-26T11:02:54`
- Duration: `00:52:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-26-10-10-51__te_lstm_sequence_global`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-26-10-10-51__te_lstm_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-26-10-10-51__te_lstm_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-10-10-51__te_lstm_sequence_global\checkpoints\lstm_sequence-epoch=120-val_mae=0.00215068.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-26-10-10-51__te_lstm_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-26-10-10-51__te_lstm_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/025_te_lstm_sequence_global.log`
- Error Message: `N/A`

### te_lstm_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_026_026_lstm_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/026_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-26-11-02-55__te_lstm_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T11:02:55`
- End Time: `2026-06-26T11:50:45`
- Duration: `00:47:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-26-11-02-55__te_lstm_sequence_fw`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-26-11-02-55__te_lstm_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-26-11-02-55__te_lstm_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-11-02-55__te_lstm_sequence_fw\checkpoints\lstm_sequence-epoch=098-val_mae=0.00215097.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-26-11-02-55__te_lstm_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-26-11-02-55__te_lstm_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/026_te_lstm_sequence_fw.log`
- Error Message: `N/A`

### te_lstm_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_027_027_lstm_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/027_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-26-11-50-45__te_lstm_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T11:50:45`
- End Time: `2026-06-26T12:41:41`
- Duration: `00:50:56`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-26-11-50-45__te_lstm_sequence_bw`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-26-11-50-45__te_lstm_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-26-11-50-45__te_lstm_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-11-50-45__te_lstm_sequence_bw\checkpoints\lstm_sequence-epoch=142-val_mae=0.00215130.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-26-11-50-45__te_lstm_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-26-11-50-45__te_lstm_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/027_te_lstm_sequence_bw.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_028_028_periodic_temporal_convolution_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/028_periodic_temporal_convolution_global.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-26-12-41-42__te_periodic_temporal_convolution_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T12:41:42`
- End Time: `2026-06-26T13:03:57`
- Duration: `00:22:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-26-12-41-42__te_periodic_temporal_convolution_global`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-12-41-42__te_periodic_temporal_convolution_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-26-12-41-42__te_periodic_temporal_convolution_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-12-41-42__te_periodic_temporal_convolution_global\checkpoints\periodic_temporal_convolution-epoch=025-val_mae=0.00220180.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-12-41-42__te_periodic_temporal_convolution_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-26-12-41-42__te_periodic_temporal_convolution_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/028_te_periodic_temporal_convolution_global.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_029_029_periodic_temporal_convolution_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/029_periodic_temporal_convolution_fw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-26-13-03-57__te_periodic_temporal_convolution_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T13:03:57`
- End Time: `2026-06-26T13:35:38`
- Duration: `00:31:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-03-57__te_periodic_temporal_convolution_fw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-03-57__te_periodic_temporal_convolution_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-03-57__te_periodic_temporal_convolution_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-13-03-57__te_periodic_temporal_convolution_fw\checkpoints\periodic_temporal_convolution-epoch=055-val_mae=0.00206541.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-03-57__te_periodic_temporal_convolution_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-03-57__te_periodic_temporal_convolution_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/029_te_periodic_temporal_convolution_fw.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_030_030_periodic_temporal_convolution_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/030_periodic_temporal_convolution_bw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-26-13-35-38__te_periodic_temporal_convolution_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T13:35:38`
- End Time: `2026-06-26T14:02:44`
- Duration: `00:27:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-35-38__te_periodic_temporal_convolution_bw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-35-38__te_periodic_temporal_convolution_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-35-38__te_periodic_temporal_convolution_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-13-35-38__te_periodic_temporal_convolution_bw\checkpoints\periodic_temporal_convolution-epoch=043-val_mae=0.00216132.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-35-38__te_periodic_temporal_convolution_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-26-13-35-38__te_periodic_temporal_convolution_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/030_te_periodic_temporal_convolution_bw.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_031_031_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/031_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-26-14-02-44__te_periodic_gru_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T14:02:44`
- End Time: `2026-06-26T15:05:37`
- Duration: `01:02:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-26-14-02-44__te_periodic_gru_sequence_global`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-14-02-44__te_periodic_gru_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-26-14-02-44__te_periodic_gru_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-14-02-44__te_periodic_gru_sequence_global\checkpoints\periodic_gru_sequence-epoch=157-val_mae=0.00125208.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-14-02-44__te_periodic_gru_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-26-14-02-44__te_periodic_gru_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/031_te_periodic_gru_sequence_global.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_032_032_periodic_gru_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/032_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-26-15-05-38__te_periodic_gru_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T15:05:38`
- End Time: `2026-06-26T16:26:19`
- Duration: `01:20:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-26-15-05-38__te_periodic_gru_sequence_fw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-15-05-38__te_periodic_gru_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-26-15-05-38__te_periodic_gru_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-15-05-38__te_periodic_gru_sequence_fw\checkpoints\periodic_gru_sequence-epoch=249-val_mae=0.00109946.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-15-05-38__te_periodic_gru_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-26-15-05-38__te_periodic_gru_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/032_te_periodic_gru_sequence_fw.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_033_033_periodic_gru_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/033_periodic_gru_sequence_bw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-26-16-26-19__te_periodic_gru_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T16:26:19`
- End Time: `2026-06-26T17:47:56`
- Duration: `01:21:37`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-26-16-26-19__te_periodic_gru_sequence_bw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-16-26-19__te_periodic_gru_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-26-16-26-19__te_periodic_gru_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-16-26-19__te_periodic_gru_sequence_bw\checkpoints\periodic_gru_sequence-epoch=258-val_mae=0.00108795.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-26-16-26-19__te_periodic_gru_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-26-16-26-19__te_periodic_gru_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/033_te_periodic_gru_sequence_bw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_global

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_034_034_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/034_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-26-17-47-56__te_periodic_lstm_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-26T17:47:56`
- End Time: `2026-06-26T19:15:48`
- Duration: `01:27:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-26-17-47-56__te_periodic_lstm_sequence_global`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-17-47-56__te_periodic_lstm_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-26-17-47-56__te_periodic_lstm_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-17-47-56__te_periodic_lstm_sequence_global\checkpoints\periodic_lstm_sequence-epoch=256-val_mae=0.00118477.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-17-47-56__te_periodic_lstm_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-26-17-47-56__te_periodic_lstm_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/034_te_periodic_lstm_sequence_global.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_035_035_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/035_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-26-19-15-48__te_periodic_lstm_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-26T19:15:48`
- End Time: `2026-06-26T20:15:05`
- Duration: `00:59:17`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-26-19-15-48__te_periodic_lstm_sequence_fw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-19-15-48__te_periodic_lstm_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-26-19-15-48__te_periodic_lstm_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-19-15-48__te_periodic_lstm_sequence_fw\checkpoints\periodic_lstm_sequence-epoch=167-val_mae=0.00149466.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-19-15-48__te_periodic_lstm_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-26-19-15-48__te_periodic_lstm_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/035_te_periodic_lstm_sequence_fw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_early_wave_parallel_training/completed/2026-06-25-16-01-22_036_036_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/036_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-26-20-15-06__te_periodic_lstm_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-26T20:15:06`
- End Time: `2026-06-26T21:30:02`
- Duration: `01:14:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-26-20-15-06__te_periodic_lstm_sequence_bw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-20-15-06__te_periodic_lstm_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-26-20-15-06__te_periodic_lstm_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-20-15-06__te_periodic_lstm_sequence_bw\checkpoints\periodic_lstm_sequence-epoch=182-val_mae=0.00123087.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-26-20-15-06__te_periodic_lstm_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-26-20-15-06__te_periodic_lstm_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/logs/036_te_periodic_lstm_sequence_bw.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
