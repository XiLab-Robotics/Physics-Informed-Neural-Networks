# Training Campaign Execution Report

## Overview

- Campaign Name: `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00`
- Generated At: `2026-03-26T20:19:32`
- Queue Root: `config/training/queue`
- Campaign Output Directory: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Completed Runs: `15`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/completed/2026-03-26-15-01-20_001_01_residual_h08_small_frozen.yaml` | `te_residual_h08_small_frozen_wave1` | `residual_harmonic_mlp` | `completed` | `00:18:38` |
| `config/training/queue/completed/2026-03-26-15-01-20_002_02_residual_h08_small_joint.yaml` | `te_residual_h08_small_joint_wave1` | `residual_harmonic_mlp` | `completed` | `00:11:22` |
| `config/training/queue/completed/2026-03-26-15-01-20_003_03_residual_h12_small_frozen.yaml` | `te_residual_h12_small_frozen_wave1` | `residual_harmonic_mlp` | `completed` | `00:23:21` |
| `config/training/queue/completed/2026-03-26-15-01-20_004_04_residual_h12_small_joint_anchor.yaml` | `te_residual_h12_small_joint_anchor_wave1` | `residual_harmonic_mlp` | `completed` | `00:11:20` |
| `config/training/queue/completed/2026-03-26-15-01-20_005_05_residual_h16_small_joint.yaml` | `te_residual_h16_small_joint_wave1` | `residual_harmonic_mlp` | `completed` | `00:20:09` |
| `config/training/queue/completed/2026-03-26-15-01-20_006_06_residual_h12_medium_joint.yaml` | `te_residual_h12_medium_joint_wave1` | `residual_harmonic_mlp` | `completed` | `00:22:14` |
| `config/training/queue/completed/2026-03-26-15-01-20_007_07_residual_h12_wide_joint.yaml` | `te_residual_h12_wide_joint_wave1` | `residual_harmonic_mlp` | `completed` | `00:31:23` |
| `config/training/queue/completed/2026-03-26-15-01-20_008_08_residual_h12_deep_joint.yaml` | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | `completed` | `00:28:48` |
| `config/training/queue/completed/2026-03-26-15-01-20_009_09_residual_h12_small_joint_low_dropout.yaml` | `te_residual_h12_small_joint_low_dropout_wave1` | `residual_harmonic_mlp` | `completed` | `00:21:04` |
| `config/training/queue/completed/2026-03-26-15-01-20_010_10_residual_h12_small_joint_high_dropout.yaml` | `te_residual_h12_small_joint_high_dropout_wave1` | `residual_harmonic_mlp` | `completed` | `00:21:29` |
| `config/training/queue/completed/2026-03-26-15-01-20_011_11_residual_h12_small_joint_no_layer_norm.yaml` | `te_residual_h12_small_joint_no_layer_norm_wave1` | `residual_harmonic_mlp` | `completed` | `00:12:49` |
| `config/training/queue/completed/2026-03-26-15-01-20_012_12_residual_h12_small_joint_low_lr_long.yaml` | `te_residual_h12_small_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | `completed` | `00:27:44` |
| `config/training/queue/completed/2026-03-26-15-01-20_013_13_residual_h12_wide_joint_low_lr_long.yaml` | `te_residual_h12_wide_joint_low_lr_long_wave1` | `residual_harmonic_mlp` | `completed` | `00:22:45` |
| `config/training/queue/completed/2026-03-26-15-01-20_014_14_residual_h12_small_joint_dense.yaml` | `te_residual_h12_small_joint_dense_wave1` | `residual_harmonic_mlp` | `completed` | `00:26:57` |
| `config/training/queue/completed/2026-03-26-15-01-20_015_15_residual_h12_small_joint_medium_dense_large_batch.yaml` | `te_residual_h12_small_joint_medium_dense_large_batch_wave1` | `residual_harmonic_mlp` | `completed` | `00:18:07` |

## Run Details

### te_residual_h08_small_frozen_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_001_01_residual_h08_small_frozen.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/01_residual_h08_small_frozen.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T15:01:20`
- End Time: `2026-03-26T15:19:58`
- Duration: `00:18:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1\checkpoints\residual_harmonic_mlp-epoch=063-val_mae=0.00300655.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/001_te_residual_h08_small_frozen_wave1.log`
- Error Message: `N/A`

### te_residual_h08_small_joint_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_002_02_residual_h08_small_joint.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/02_residual_h08_small_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-15-19-58__te_residual_h08_small_joint_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T15:19:58`
- End Time: `2026-03-26T15:31:20`
- Duration: `00:11:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-19-58__te_residual_h08_small_joint_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-19-58__te_residual_h08_small_joint_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-19-58__te_residual_h08_small_joint_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-19-58__te_residual_h08_small_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=020-val_mae=0.00303040.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-19-58__te_residual_h08_small_joint_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-19-58__te_residual_h08_small_joint_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/002_te_residual_h08_small_joint_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_frozen_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_003_03_residual_h12_small_frozen.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/03_residual_h12_small_frozen.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T15:31:20`
- End Time: `2026-03-26T15:54:41`
- Duration: `00:23:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1\checkpoints\residual_harmonic_mlp-epoch=091-val_mae=0.00303609.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-31-20__te_residual_h12_small_frozen_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/003_te_residual_h12_small_frozen_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_anchor_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_004_04_residual_h12_small_joint_anchor.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/04_residual_h12_small_joint_anchor.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T15:54:41`
- End Time: `2026-03-26T16:06:01`
- Duration: `00:11:20`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1\checkpoints\residual_harmonic_mlp-epoch=017-val_mae=0.00308991.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/004_te_residual_h12_small_joint_anchor_wave1.log`
- Error Message: `N/A`

### te_residual_h16_small_joint_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_005_05_residual_h16_small_joint.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/05_residual_h16_small_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-16-06-02__te_residual_h16_small_joint_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T16:06:02`
- End Time: `2026-03-26T16:26:11`
- Duration: `00:20:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-06-02__te_residual_h16_small_joint_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-06-02__te_residual_h16_small_joint_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-06-02__te_residual_h16_small_joint_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-06-02__te_residual_h16_small_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=074-val_mae=0.00302049.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-06-02__te_residual_h16_small_joint_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-06-02__te_residual_h16_small_joint_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/005_te_residual_h16_small_joint_wave1.log`
- Error Message: `N/A`

### te_residual_h12_medium_joint_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_006_06_residual_h12_medium_joint.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/06_residual_h12_medium_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T16:26:11`
- End Time: `2026-03-26T16:48:24`
- Duration: `00:22:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=082-val_mae=0.00296847.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/006_te_residual_h12_medium_joint_wave1.log`
- Error Message: `N/A`

### te_residual_h12_wide_joint_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_007_07_residual_h12_wide_joint.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/07_residual_h12_wide_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T16:48:24`
- End Time: `2026-03-26T17:19:48`
- Duration: `00:31:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=097-val_mae=0.00288380.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/007_te_residual_h12_wide_joint_wave1.log`
- Error Message: `N/A`

### te_residual_h12_deep_joint_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_008_08_residual_h12_deep_joint.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/08_residual_h12_deep_joint.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T17:19:48`
- End Time: `2026-03-26T17:48:36`
- Duration: `00:28:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=077-val_mae=0.00302384.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/008_te_residual_h12_deep_joint_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_low_dropout_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_009_09_residual_h12_small_joint_low_dropout.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/09_residual_h12_small_joint_low_dropout.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T17:48:36`
- End Time: `2026-03-26T18:09:40`
- Duration: `00:21:04`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1\checkpoints\residual_harmonic_mlp-epoch=076-val_mae=0.00302673.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/009_te_residual_h12_small_joint_low_dropout_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_high_dropout_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_010_10_residual_h12_small_joint_high_dropout.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/10_residual_h12_small_joint_high_dropout.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T18:09:40`
- End Time: `2026-03-26T18:31:09`
- Duration: `00:21:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1\checkpoints\residual_harmonic_mlp-epoch=094-val_mae=0.00300110.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/010_te_residual_h12_small_joint_high_dropout_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_no_layer_norm_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_011_11_residual_h12_small_joint_no_layer_norm.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/11_residual_h12_small_joint_no_layer_norm.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T18:31:09`
- End Time: `2026-03-26T18:43:58`
- Duration: `00:12:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1\checkpoints\residual_harmonic_mlp-epoch=044-val_mae=0.00308930.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/011_te_residual_h12_small_joint_no_layer_norm_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_low_lr_long_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_012_12_residual_h12_small_joint_low_lr_long.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/12_residual_h12_small_joint_low_lr_long.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T18:43:58`
- End Time: `2026-03-26T19:11:43`
- Duration: `00:27:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1\checkpoints\residual_harmonic_mlp-epoch=134-val_mae=0.00298742.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/012_te_residual_h12_small_joint_low_lr_long_wave1.log`
- Error Message: `N/A`

### te_residual_h12_wide_joint_low_lr_long_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_013_13_residual_h12_wide_joint_low_lr_long.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/13_residual_h12_wide_joint_low_lr_long.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T19:11:43`
- End Time: `2026-03-26T19:34:27`
- Duration: `00:22:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1\checkpoints\residual_harmonic_mlp-epoch=124-val_mae=0.00292449.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/013_te_residual_h12_wide_joint_low_lr_long_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_dense_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_014_14_residual_h12_small_joint_dense.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/14_residual_h12_small_joint_dense.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T19:34:28`
- End Time: `2026-03-26T20:01:25`
- Duration: `00:26:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1\checkpoints\residual_harmonic_mlp-epoch=038-val_mae=0.00296185.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/014_te_residual_h12_small_joint_dense_wave1.log`
- Error Message: `N/A`

### te_residual_h12_small_joint_medium_dense_large_batch_wave1

- Queue Config: `config/training/queue/completed/2026-03-26-15-01-20_015_15_residual_h12_small_joint_medium_dense_large_batch.yaml`
- Source Config: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/15_residual_h12_small_joint_medium_dense_large_batch.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1`
- Queue Status: `completed`
- Start Time: `2026-03-26T20:01:25`
- End Time: `2026-03-26T20:19:32`
- Duration: `00:18:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1\checkpoints\residual_harmonic_mlp-epoch=087-val_mae=0.00293487.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1/training_test_report.md`
- Terminal Log: `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/logs/015_te_residual_h12_small_joint_medium_dense_large_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
