# Training Campaign Execution Report

## Overview

- Campaign Name: `polished_dataset_stage1_smoke_2026_06_21`
- Generated At: `2026-06-22T16:00:39`
- Queue Root: `config/training/queue/polished_dataset_stage1_smoke`
- Campaign Output Directory: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md`
- Completed Runs: `8`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_001_trial.yaml` | `te_feedforward_trial` | `feedforward` | `completed` | `00:03:27` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_002_01_tree_global.yaml` | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | `completed` | `00:01:53` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_003_13_harmonic_regression_global.yaml` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | `completed` | `00:11:27` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_004_04_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | `completed` | `00:40:03` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_005_01_residual_harmonic_gru_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | `completed` | `00:24:21` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_006_10_full_curve_composite_global.yaml` | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:44:57` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_007_04_smooth_l1_structured_global.yaml` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | `completed` | `00:21:31` |
| `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_008_01_gru_offset_residual_global.yaml` | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | `completed` | `00:23:03` |

## Run Details

### te_feedforward_trial

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_001_trial.yaml`
- Source Config: `config/training/feedforward/presets/trial.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-22-13-09-57__te_feedforward_trial`
- Queue Status: `completed`
- Start Time: `2026-06-22T13:09:57`
- End Time: `2026-06-22T13:13:25`
- Duration: `00:03:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-22-13-09-57__te_feedforward_trial`
- Config Snapshot: `output/training_runs/feedforward/2026-06-22-13-09-57__te_feedforward_trial/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-22-13-09-57__te_feedforward_trial/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-22-13-09-57__te_feedforward_trial\checkpoints\feedforward-epoch=002-val_mae=0.00272463.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-22-13-09-57__te_feedforward_trial/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-22-13-09-57__te_feedforward_trial/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/001_te_feedforward_trial.log`
- Error Message: `N/A`

### te_hist_gbr_tabular_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_002_01_tree_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/01_tree_global.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-22-13-13-25__te_hist_gbr_tabular_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T13:13:25`
- End Time: `2026-06-22T13:15:18`
- Duration: `00:01:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-22-13-13-25__te_hist_gbr_tabular_global`
- Config Snapshot: `output/training_runs/tree/2026-06-22-13-13-25__te_hist_gbr_tabular_global/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-22-13-13-25__te_hist_gbr_tabular_global/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-22-13-13-25__te_hist_gbr_tabular_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/002_te_hist_gbr_tabular_global.log`
- Error Message: `N/A`

### te_harmonic_order12_linear_conditioned_recovery_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_003_13_harmonic_regression_global.yaml`
- Source Config: `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/13_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T13:15:18`
- End Time: `2026-06-22T13:26:44`
- Duration: `00:11:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global\checkpoints\harmonic_regression-epoch=030-val_mae=0.00390380.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/003_te_harmonic_order12_linear_conditioned_recovery.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_remote_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_004_04_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/04_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T13:26:44`
- End Time: `2026-06-22T14:06:48`
- Duration: `00:40:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global\checkpoints\periodic_gru_sequence-epoch=190-val_mae=0.00127364.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/004_te_periodic_gru_sequence_remote_global.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_remote_global_sparse_rcim

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_005_01_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign/queue/01_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Queue Status: `completed`
- Start Time: `2026-06-22T14:06:48`
- End Time: `2026-06-22T14:31:08`
- Duration: `00:24:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim\checkpoints\residual_harmonic_gru_sequence-epoch=081-val_mae=0.00197803.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-22-14-06-48__te_residual_harmonic_gru_sequence_remote_global_sparse_rcim/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/005_te_residual_harmonic_gru_sequence_remote_global.log`
- Error Message: `N/A`

### te_track2g_curve_aware_full_curve_composite_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_006_10_full_curve_composite_global.yaml`
- Source Config: `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/10_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T14:31:08`
- End Time: `2026-06-22T15:16:05`
- Duration: `00:44:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track_2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global`
- Config Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global\2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=136-val_mae=0.00187186.ckpt`
- Metrics Snapshot: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global/2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/006_te_track2g_curve_aware_full_curve_composite_glob.log`
- Error Message: `N/A`

### te_wave3_harmonic_prior_residual_smooth_l1_structured_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_007_04_smooth_l1_structured_global.yaml`
- Source Config: `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue/04_smooth_l1_structured_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T15:16:05`
- End Time: `2026-06-22T15:37:36`
- Duration: `00:21:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Config Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_global\2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=043-val_mae=0.00188941.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_harmonic_prior_residual_smooth_l1_structured_global/2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/007_te_wave3_harmonic_prior_residual_smooth_l1_struc.log`
- Error Message: `N/A`

### te_track2h_l_gru_offset_residual_global

- Queue Config: `config/training/queue/polished_dataset_stage1_smoke/completed/2026-06-22-13-09-57_008_01_gru_offset_residual_global.yaml`
- Source Config: `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign/queue/01_gru_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global`
- Queue Status: `completed`
- Start Time: `2026-06-22T15:37:37`
- End Time: `2026-06-22T16:00:39`
- Duration: `00:23:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
- Output Directory: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global`
- Config Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_global\2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=101-val_mae=0.00223219.ckpt`
- Metrics Snapshot: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global/metrics_summary.yaml`
- Training Report: `output/training_runs/track2h_latent_state_hysteresis_gru_offset_residual_global/2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/logs/008_te_track2h_l_gru_offset_residual_global.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
