# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Generated At: `2026-05-06T23:14:10`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Completed Runs: `15`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-05-06-16-58-54_001_01_tree_global.yaml` | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | `completed` | `00:02:01` |
| `config/training/queue/completed/2026-05-06-16-58-54_002_02_tree_fw.yaml` | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | `completed` | `00:01:10` |
| `config/training/queue/completed/2026-05-06-16-58-54_003_03_tree_bw.yaml` | `te_hist_gbr_tabular_Bw` | `hist_gradient_boosting` | `completed` | `00:01:12` |
| `config/training/queue/completed/2026-05-06-16-58-54_004_04_residual_harmonic_mlp_global.yaml` | `te_residual_h12_deep_joint_wave1_global` | `residual_harmonic_mlp` | `completed` | `00:20:35` |
| `config/training/queue/completed/2026-05-06-16-58-54_005_05_residual_harmonic_mlp_fw.yaml` | `te_residual_h12_deep_joint_wave1_Fw` | `residual_harmonic_mlp` | `completed` | `00:10:41` |
| `config/training/queue/completed/2026-05-06-16-58-54_006_06_residual_harmonic_mlp_bw.yaml` | `te_residual_h12_deep_joint_wave1_Bw` | `residual_harmonic_mlp` | `completed` | `00:15:03` |
| `config/training/queue/completed/2026-05-06-16-58-54_007_07_feedforward_global.yaml` | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | `completed` | `02:27:05` |
| `config/training/queue/completed/2026-05-06-16-58-54_008_08_feedforward_fw.yaml` | `te_feedforward_stride1_high_compute_long_remote_Fw` | `feedforward` | `completed` | `00:25:08` |
| `config/training/queue/completed/2026-05-06-16-58-54_009_09_feedforward_bw.yaml` | `te_feedforward_stride1_high_compute_long_remote_Bw` | `feedforward` | `completed` | `01:08:06` |
| `config/training/queue/completed/2026-05-06-16-58-54_010_10_periodic_mlp_global.yaml` | `te_periodic_mlp_h04_standard_global` | `periodic_mlp` | `completed` | `00:24:13` |
| `config/training/queue/completed/2026-05-06-16-58-54_011_11_periodic_mlp_fw.yaml` | `te_periodic_mlp_h04_standard_Fw` | `periodic_mlp` | `completed` | `00:11:04` |
| `config/training/queue/completed/2026-05-06-16-58-54_012_12_periodic_mlp_bw.yaml` | `te_periodic_mlp_h04_standard_Bw` | `periodic_mlp` | `completed` | `00:15:06` |
| `config/training/queue/completed/2026-05-06-16-58-54_013_13_harmonic_regression_global.yaml` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | `completed` | `00:14:04` |
| `config/training/queue/completed/2026-05-06-16-58-54_014_14_harmonic_regression_fw.yaml` | `te_harmonic_order12_linear_conditioned_recovery_Fw` | `harmonic_regression` | `completed` | `00:10:50` |
| `config/training/queue/completed/2026-05-06-16-58-54_015_15_harmonic_regression_bw.yaml` | `te_harmonic_order12_linear_conditioned_recovery_Bw` | `harmonic_regression` | `completed` | `00:08:57` |

## Run Details

### te_hist_gbr_tabular_global

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_001_01_tree_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/01_tree_global.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-05-06-16-58-54__te_hist_gbr_tabular_global`
- Queue Status: `completed`
- Start Time: `2026-05-06T16:58:54`
- End Time: `2026-05-06T17:00:56`
- Duration: `00:02:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-05-06-16-58-54__te_hist_gbr_tabular_global`
- Config Snapshot: `output/training_runs/tree/2026-05-06-16-58-54__te_hist_gbr_tabular_global/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-05-06-16-58-54__te_hist_gbr_tabular_global/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-05-06-16-58-54__te_hist_gbr_tabular_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/001_te_hist_gbr_tabular_global.log`
- Error Message: `N/A`

### te_hist_gbr_tabular_Fw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_002_02_tree_fw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/02_tree_fw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-05-06-17-00-56__te_hist_gbr_tabular_fw`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:00:56`
- End Time: `2026-05-06T17:02:06`
- Duration: `00:01:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw`
- Config Snapshot: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/002_te_hist_gbr_tabular_fw.log`
- Error Message: `N/A`

### te_hist_gbr_tabular_Bw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_003_03_tree_bw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/03_tree_bw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-05-06-17-02-06__te_hist_gbr_tabular_bw`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:02:06`
- End Time: `2026-05-06T17:03:18`
- Duration: `00:01:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree_bw/2026-05-06-17-02-06__te_hist_gbr_tabular_bw`
- Config Snapshot: `output/training_runs/tree_bw/2026-05-06-17-02-06__te_hist_gbr_tabular_bw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree_bw/2026-05-06-17-02-06__te_hist_gbr_tabular_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree_bw/2026-05-06-17-02-06__te_hist_gbr_tabular_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/003_te_hist_gbr_tabular_bw.log`
- Error Message: `N/A`

### te_residual_h12_deep_joint_wave1_global

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_004_04_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/04_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:03:18`
- End Time: `2026-05-06T17:23:53`
- Duration: `00:20:35`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global\checkpoints\residual_harmonic_mlp-epoch=038-val_mae=0.00311466.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/004_te_residual_h12_deep_joint_wave1_global.log`
- Error Message: `N/A`

### te_residual_h12_deep_joint_wave1_Fw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_005_05_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/05_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:23:53`
- End Time: `2026-05-06T17:34:34`
- Duration: `00:10:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_fw/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_fw/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp_fw\2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw\checkpoints\residual_harmonic_mlp-epoch=018-val_mae=0.00285191.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_fw/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_fw/2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/005_te_residual_h12_deep_joint_wave1_fw.log`
- Error Message: `N/A`

### te_residual_h12_deep_joint_wave1_Bw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_006_06_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/06_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:34:34`
- End Time: `2026-05-06T17:49:37`
- Duration: `00:15:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp_bw/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp_bw/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp_bw\2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw\checkpoints\residual_harmonic_mlp-epoch=037-val_mae=0.00310962.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp_bw/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp_bw/2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/006_te_residual_h12_deep_joint_wave1_bw.log`
- Error Message: `N/A`

### te_feedforward_stride1_high_compute_long_remote_global

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_007_07_feedforward_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/07_feedforward_global.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global`
- Queue Status: `completed`
- Start Time: `2026-05-06T17:49:37`
- End Time: `2026-05-06T20:16:42`
- Duration: `02:27:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global`
- Config Snapshot: `output/training_runs/feedforward/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global\checkpoints\feedforward-epoch=180-val_mae=0.00305586.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/007_te_feedforward_stride1_high_compute_long_remote.log`
- Error Message: `N/A`

### te_feedforward_stride1_high_compute_long_remote_Fw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_008_08_feedforward_fw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/08_feedforward_fw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw`
- Queue Status: `completed`
- Start Time: `2026-05-06T20:16:42`
- End Time: `2026-05-06T20:41:50`
- Duration: `00:25:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward_fw/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw`
- Config Snapshot: `output/training_runs/feedforward_fw/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward_fw/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_fw\2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw\checkpoints\feedforward-epoch=033-val_mae=0.00291539.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward_fw/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward_fw/2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/008_te_feedforward_stride1_high_compute_long_remote.log`
- Error Message: `N/A`

### te_feedforward_stride1_high_compute_long_remote_Bw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_009_09_feedforward_bw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/09_feedforward_bw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw`
- Queue Status: `completed`
- Start Time: `2026-05-06T20:41:50`
- End Time: `2026-05-06T21:49:56`
- Duration: `01:08:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward_bw/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw`
- Config Snapshot: `output/training_runs/feedforward_bw/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward_bw/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_bw\2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw\checkpoints\feedforward-epoch=093-val_mae=0.00304864.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward_bw/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward_bw/2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/009_te_feedforward_stride1_high_compute_long_remote.log`
- Error Message: `N/A`

### te_periodic_mlp_h04_standard_global

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_010_10_periodic_mlp_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/10_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global`
- Queue Status: `completed`
- Start Time: `2026-05-06T21:49:56`
- End Time: `2026-05-06T22:14:09`
- Duration: `00:24:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global\checkpoints\periodic_mlp-epoch=041-val_mae=0.00298461.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-05-06-21-49-56__te_periodic_mlp_h04_standard_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/010_te_periodic_mlp_h04_standard_global.log`
- Error Message: `N/A`

### te_periodic_mlp_h04_standard_Fw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_011_11_periodic_mlp_fw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/11_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw`
- Queue Status: `completed`
- Start Time: `2026-05-06T22:14:09`
- End Time: `2026-05-06T22:25:13`
- Duration: `00:11:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_fw/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_fw/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_fw\2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw\checkpoints\periodic_mlp-epoch=022-val_mae=0.00284801.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_fw/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_fw/2026-05-06-22-14-09__te_periodic_mlp_h04_standard_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/011_te_periodic_mlp_h04_standard_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_h04_standard_Bw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_012_12_periodic_mlp_bw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/12_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw`
- Queue Status: `completed`
- Start Time: `2026-05-06T22:25:13`
- End Time: `2026-05-06T22:40:20`
- Duration: `00:15:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_bw/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_bw/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw\checkpoints\periodic_mlp-epoch=049-val_mae=0.00315372.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_bw/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_bw/2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/012_te_periodic_mlp_h04_standard_bw.log`
- Error Message: `N/A`

### te_harmonic_order12_linear_conditioned_recovery_global

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_013_13_harmonic_regression_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/13_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global`
- Queue Status: `completed`
- Start Time: `2026-05-06T22:40:20`
- End Time: `2026-05-06T22:54:24`
- Duration: `00:14:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global\checkpoints\harmonic_regression-epoch=018-val_mae=0.01701703.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/013_te_harmonic_order12_linear_conditioned_recovery.log`
- Error Message: `N/A`

### te_harmonic_order12_linear_conditioned_recovery_Fw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_014_14_harmonic_regression_fw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/14_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw`
- Queue Status: `completed`
- Start Time: `2026-05-06T22:54:24`
- End Time: `2026-05-06T23:05:13`
- Duration: `00:10:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_fw/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw`
- Config Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_fw/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw\checkpoints\harmonic_regression-epoch=068-val_mae=0.00281060.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_fw/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_fw/2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/014_te_harmonic_order12_linear_conditioned_recovery.log`
- Error Message: `N/A`

### te_harmonic_order12_linear_conditioned_recovery_Bw

- Queue Config: `config/training/queue/completed/2026-05-06-16-58-54_015_15_harmonic_regression_bw.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/15_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw`
- Queue Status: `completed`
- Start Time: `2026-05-06T23:05:13`
- End Time: `2026-05-06T23:14:10`
- Duration: `00:08:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression_bw/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw`
- Config Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression_bw/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw\checkpoints\harmonic_regression-epoch=019-val_mae=0.00370070.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression_bw/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression_bw/2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/logs/015_te_harmonic_order12_linear_conditioned_recovery.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
