# Training Campaign Execution Report

## Overview

- Campaign Name: `polished_dataset_full_wave_retraining_2026_06_22`
- Generated At: `2026-07-02T01:47:45`
- Queue Root: `config/training/queue/polished_dataset_full_wave_retraining`
- Campaign Output Directory: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Completed Runs: `108`
- Failed Runs: `0`

## Run Summary

| Queue Config | Run Name | Model Type | Status | Duration |
| --- | --- | --- | --- | --- |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_001_001_tree_global.yaml` | `te_tree_global` | `hist_gradient_boosting` | `completed` | `00:02:16` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_002_002_tree_fw.yaml` | `te_tree_fw` | `hist_gradient_boosting` | `completed` | `00:01:53` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_003_003_tree_bw.yaml` | `te_tree_bw` | `hist_gradient_boosting` | `completed` | `00:01:53` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_004_004_residual_harmonic_mlp_global.yaml` | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | `completed` | `00:22:28` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_005_005_residual_harmonic_mlp_fw.yaml` | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | `completed` | `00:19:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_006_006_residual_harmonic_mlp_bw.yaml` | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | `completed` | `00:16:36` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_007_007_feedforward_global.yaml` | `te_feedforward_global` | `feedforward` | `completed` | `00:40:07` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_008_008_feedforward_fw.yaml` | `te_feedforward_fw` | `feedforward` | `completed` | `00:45:44` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_009_009_feedforward_bw.yaml` | `te_feedforward_bw` | `feedforward` | `completed` | `01:02:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_010_010_periodic_mlp_global.yaml` | `te_periodic_mlp_global` | `periodic_mlp` | `completed` | `00:19:36` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_011_011_periodic_mlp_fw.yaml` | `te_periodic_mlp_fw` | `periodic_mlp` | `completed` | `00:15:31` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_012_012_periodic_mlp_bw.yaml` | `te_periodic_mlp_bw` | `periodic_mlp` | `completed` | `00:20:08` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_013_013_harmonic_regression_global.yaml` | `te_harmonic_regression_global` | `harmonic_regression` | `completed` | `00:10:24` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_014_014_harmonic_regression_fw.yaml` | `te_harmonic_regression_fw` | `harmonic_regression` | `completed` | `00:10:07` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_015_015_harmonic_regression_bw.yaml` | `te_harmonic_regression_bw` | `harmonic_regression` | `completed` | `00:11:29` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_016_016_periodic_mlp_harmonic_global.yaml` | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | `completed` | `00:15:47` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_017_017_periodic_mlp_harmonic_fw.yaml` | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | `completed` | `00:17:10` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_018_018_periodic_mlp_harmonic_bw.yaml` | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | `completed` | `00:20:48` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_019_019_temporal_convolution_global.yaml` | `te_temporal_convolution_global` | `temporal_convolution` | `completed` | `00:22:15` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_020_020_temporal_convolution_fw.yaml` | `te_temporal_convolution_fw` | `temporal_convolution` | `completed` | `00:15:07` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_021_021_temporal_convolution_bw.yaml` | `te_temporal_convolution_bw` | `temporal_convolution` | `completed` | `00:25:15` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_022_022_gru_sequence_global.yaml` | `te_gru_sequence_global` | `gru_sequence` | `completed` | `00:15:38` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_023_023_gru_sequence_fw.yaml` | `te_gru_sequence_fw` | `gru_sequence` | `completed` | `00:29:54` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_024_024_gru_sequence_bw.yaml` | `te_gru_sequence_bw` | `gru_sequence` | `completed` | `00:33:29` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_025_025_lstm_sequence_global.yaml` | `te_lstm_sequence_global` | `lstm_sequence` | `completed` | `00:29:43` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_026_026_lstm_sequence_fw.yaml` | `te_lstm_sequence_fw` | `lstm_sequence` | `completed` | `00:22:50` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_027_027_lstm_sequence_bw.yaml` | `te_lstm_sequence_bw` | `lstm_sequence` | `completed` | `00:27:12` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_028_028_periodic_temporal_convolution_global.yaml` | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | `completed` | `00:14:09` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_029_029_periodic_temporal_convolution_fw.yaml` | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | `completed` | `00:15:25` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_030_030_periodic_temporal_convolution_bw.yaml` | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | `completed` | `00:15:34` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_031_031_periodic_gru_sequence_global.yaml` | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | `completed` | `00:41:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_032_032_periodic_gru_sequence_fw.yaml` | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | `completed` | `00:45:23` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_033_033_periodic_gru_sequence_bw.yaml` | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | `completed` | `00:45:02` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_034_034_periodic_lstm_sequence_global.yaml` | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | `completed` | `00:30:40` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_035_035_periodic_lstm_sequence_fw.yaml` | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | `completed` | `00:29:41` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_036_036_periodic_lstm_sequence_bw.yaml` | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | `completed` | `00:46:38` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_037_037_residual_harmonic_gru_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_global` | `residual_harmonic_gru_sequence` | `completed` | `00:22:42` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_038_038_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_fw` | `residual_harmonic_gru_sequence` | `completed` | `00:31:46` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_039_039_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_gru_sequence_sparse_rcim_bw` | `residual_harmonic_gru_sequence` | `completed` | `00:25:11` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_040_040_residual_harmonic_gru_sequence_dense240_global.yaml` | `te_residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence` | `completed` | `00:47:26` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_041_041_residual_harmonic_gru_sequence_dense240_fw.yaml` | `te_residual_harmonic_gru_sequence_dense240_fw` | `residual_harmonic_gru_sequence` | `completed` | `00:25:47` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_042_042_residual_harmonic_gru_sequence_dense240_bw.yaml` | `te_residual_harmonic_gru_sequence_dense240_bw` | `residual_harmonic_gru_sequence` | `completed` | `00:43:06` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_043_043_residual_harmonic_gru_sequence_dense360_global.yaml` | `te_residual_harmonic_gru_sequence_dense360_global` | `residual_harmonic_gru_sequence` | `completed` | `00:30:11` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_044_044_residual_harmonic_gru_sequence_dense360_fw.yaml` | `te_residual_harmonic_gru_sequence_dense360_fw` | `residual_harmonic_gru_sequence` | `completed` | `00:54:52` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_045_045_residual_harmonic_gru_sequence_dense360_bw.yaml` | `te_residual_harmonic_gru_sequence_dense360_bw` | `residual_harmonic_gru_sequence` | `completed` | `00:50:34` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_046_046_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence` | `completed` | `00:32:00` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_047_047_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw` | `residual_harmonic_lstm_sequence` | `completed` | `00:24:30` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_048_048_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml` | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `residual_harmonic_lstm_sequence` | `completed` | `00:20:29` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_049_049_residual_harmonic_lstm_sequence_dense240_global.yaml` | `te_residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence` | `completed` | `00:30:03` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_050_050_residual_harmonic_lstm_sequence_dense240_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense240_fw` | `residual_harmonic_lstm_sequence` | `completed` | `00:21:58` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_051_051_residual_harmonic_lstm_sequence_dense240_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense240_bw` | `residual_harmonic_lstm_sequence` | `completed` | `00:25:51` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_052_052_residual_harmonic_lstm_sequence_dense360_global.yaml` | `te_residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence` | `completed` | `00:27:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_053_053_residual_harmonic_lstm_sequence_dense360_fw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_fw` | `residual_harmonic_lstm_sequence` | `completed` | `00:28:00` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_054_054_residual_harmonic_lstm_sequence_dense360_bw.yaml` | `te_residual_harmonic_lstm_sequence_dense360_bw` | `residual_harmonic_lstm_sequence` | `completed` | `00:46:45` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_055_055_wave3_1_sequential_residual_offset_probe_global.yaml` | `te_wave3_1_sequential_residual_offset_probe_global` | `sequential_residual_offset_probe` | `completed` | `00:23:01` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_056_056_wave3_1_sequential_residual_offset_probe_fw.yaml` | `te_wave3_1_sequential_residual_offset_probe_fw` | `sequential_residual_offset_probe` | `completed` | `00:24:13` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_057_057_wave3_1_sequential_residual_offset_probe_bw.yaml` | `te_wave3_1_sequential_residual_offset_probe_bw` | `sequential_residual_offset_probe` | `completed` | `00:29:05` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_058_058_wave3_2_clean_sequential_residual_offset_global.yaml` | `te_wave3_2_clean_sequential_residual_offset_global` | `sequential_residual_offset_probe` | `completed` | `00:28:06` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_059_059_wave3_2_clean_sequential_residual_offset_fw.yaml` | `te_wave3_2_clean_sequential_residual_offset_fw` | `sequential_residual_offset_probe` | `completed` | `00:26:01` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_060_060_wave3_2_clean_sequential_residual_offset_bw.yaml` | `te_wave3_2_clean_sequential_residual_offset_bw` | `sequential_residual_offset_probe` | `completed` | `00:30:17` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_061_061_wave3_2_harmonic_residual_offset_global.yaml` | `te_wave3_2_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | `completed` | `00:31:20` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_062_062_wave3_2_harmonic_residual_offset_fw.yaml` | `te_wave3_2_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | `completed` | `00:21:25` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_063_063_wave3_2_harmonic_residual_offset_bw.yaml` | `te_wave3_2_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | `completed` | `00:37:24` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_064_064_wave3_3_curve_aware_pointwise_control_global.yaml` | `te_wave3_3_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:27:33` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_065_065_wave3_3_curve_aware_pointwise_control_fw.yaml` | `te_wave3_3_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:40:19` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_066_066_wave3_3_curve_aware_pointwise_control_bw.yaml` | `te_wave3_3_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:36:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_067_067_wave3_3_raw_centered_shape_curve_aware_global.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:33:54` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_068_068_wave3_3_raw_centered_shape_curve_aware_fw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:34:22` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_069_069_wave3_3_raw_centered_shape_curve_aware_bw.yaml` | `te_wave3_3_raw_centered_shape_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:39:41` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_070_070_wave3_3_raw_offset_curve_aware_global.yaml` | `te_wave3_3_raw_offset_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:25:59` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_071_071_wave3_3_raw_offset_curve_aware_fw.yaml` | `te_wave3_3_raw_offset_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:28:03` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_072_072_wave3_3_raw_offset_curve_aware_bw.yaml` | `te_wave3_3_raw_offset_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:49:46` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_073_073_wave3_3_full_curve_composite_global.yaml` | `te_wave3_3_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:34:43` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_074_074_wave3_3_full_curve_composite_fw.yaml` | `te_wave3_3_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:25:54` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_075_075_wave3_3_full_curve_composite_bw.yaml` | `te_wave3_3_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:29:10` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_076_076_wave4_1_mae_robust_loss_global.yaml` | `te_wave4_1_mae_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:50:21` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_077_077_wave4_1_mae_robust_loss_fw.yaml` | `te_wave4_1_mae_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:26:51` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_078_078_wave4_1_mae_robust_loss_bw.yaml` | `te_wave4_1_mae_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:52:16` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_079_079_wave4_1_smooth_l1_robust_loss_global.yaml` | `te_wave4_1_smooth_l1_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:22:21` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_080_080_wave4_1_smooth_l1_robust_loss_fw.yaml` | `te_wave4_1_smooth_l1_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:23:12` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_081_081_wave4_1_smooth_l1_robust_loss_bw.yaml` | `te_wave4_1_smooth_l1_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:24:11` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_082_082_wave4_1_log_cosh_robust_loss_global.yaml` | `te_wave4_1_log_cosh_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:41:02` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_083_083_wave4_1_log_cosh_robust_loss_fw.yaml` | `te_wave4_1_log_cosh_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:40:58` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_084_084_wave4_1_log_cosh_robust_loss_bw.yaml` | `te_wave4_1_log_cosh_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:57:26` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_085_085_wave4_2_quantile_p10_p50_p90_global.yaml` | `te_wave4_2_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:59:14` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_086_086_wave4_2_quantile_p10_p50_p90_fw.yaml` | `te_wave4_2_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:59:28` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_087_087_wave4_2_quantile_p10_p50_p90_bw.yaml` | `te_wave4_2_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:45:41` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_088_088_wave4_2_gaussian_nll_global.yaml` | `te_wave4_2_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:31:45` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_089_089_wave4_2_gaussian_nll_fw.yaml` | `te_wave4_2_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:02:58` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_090_090_wave4_2_gaussian_nll_bw.yaml` | `te_wave4_2_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:49:15` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_091_091_wave4_3_mixture_density_k2_global.yaml` | `te_wave4_3_mixture_density_k2_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:51:39` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_092_092_wave4_3_mixture_density_k2_fw.yaml` | `te_wave4_3_mixture_density_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:13:02` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_093_093_wave4_3_mixture_density_k2_bw.yaml` | `te_wave4_3_mixture_density_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:49:12` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_094_094_wave4_3_mixture_density_k3_global.yaml` | `te_wave4_3_mixture_density_k3_global` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:03:09` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_095_095_wave4_3_mixture_density_k3_fw.yaml` | `te_wave4_3_mixture_density_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `01:12:00` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_096_096_wave4_3_mixture_density_k3_bw.yaml` | `te_wave4_3_mixture_density_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | `completed` | `00:54:20` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_097_097_wave4_4_gru_latent_offset_residual_global.yaml` | `te_wave4_4_gru_latent_offset_residual_global` | `latent_state_hysteresis_probe` | `completed` | `00:36:39` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_098_098_wave4_4_gru_latent_offset_residual_fw.yaml` | `te_wave4_4_gru_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | `completed` | `00:28:49` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_099_099_wave4_4_gru_latent_offset_residual_bw.yaml` | `te_wave4_4_gru_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | `completed` | `00:38:01` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_100_100_wave4_4_causal_tcn_latent_offset_residual_global.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_global` | `latent_state_hysteresis_probe` | `completed` | `00:26:42` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_101_101_wave4_4_causal_tcn_latent_offset_residual_fw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | `completed` | `00:28:28` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_102_102_wave4_4_causal_tcn_latent_offset_residual_bw.yaml` | `te_wave4_4_causal_tcn_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | `completed` | `00:30:27` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_103_103_wave5_1_harmonic_prior_pointwise_control_global.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_global` | `wave3_harmonic_prior_residual` | `completed` | `00:30:00` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_104_104_wave5_1_harmonic_prior_pointwise_control_fw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_fw` | `wave3_harmonic_prior_residual` | `completed` | `00:19:31` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_105_105_wave5_1_harmonic_prior_pointwise_control_bw.yaml` | `te_wave5_1_harmonic_prior_pointwise_control_bw` | `wave3_harmonic_prior_residual` | `completed` | `00:35:57` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_106_106_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | `completed` | `00:29:36` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_107_107_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | `completed` | `00:28:24` |
| `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_108_108_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml` | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | `completed` | `00:25:05` |

## Run Details

### te_tree_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_001_001_tree_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/001_tree_global.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-29-15-54-18__te_tree_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T15:54:18`
- End Time: `2026-06-29T15:56:33`
- Duration: `00:02:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-29-15-54-18__te_tree_global`
- Config Snapshot: `output/training_runs/tree/2026-06-29-15-54-18__te_tree_global/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-29-15-54-18__te_tree_global/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-29-15-54-18__te_tree_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/001_te_tree_global.log`
- Error Message: `N/A`

### te_tree_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_002_002_tree_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/002_tree_fw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-29-15-56-33__te_tree_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T15:56:33`
- End Time: `2026-06-29T15:58:27`
- Duration: `00:01:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-29-15-56-33__te_tree_fw`
- Config Snapshot: `output/training_runs/tree/2026-06-29-15-56-33__te_tree_fw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-29-15-56-33__te_tree_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-29-15-56-33__te_tree_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/002_te_tree_fw.log`
- Error Message: `N/A`

### te_tree_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_003_003_tree_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/003_tree_bw.yaml`
- Model Type: `hist_gradient_boosting`
- Run Instance Id: `2026-06-29-15-58-27__te_tree_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T15:58:27`
- End Time: `2026-06-29T16:00:19`
- Duration: `00:01:53`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/tree/2026-06-29-15-58-27__te_tree_bw`
- Config Snapshot: `output/training_runs/tree/2026-06-29-15-58-27__te_tree_bw/training_config.yaml`
- Best Checkpoint Pointer: `N/A`
- Best Checkpoint Path: `N/A`
- Metrics Snapshot: `output/training_runs/tree/2026-06-29-15-58-27__te_tree_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/tree/2026-06-29-15-58-27__te_tree_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/003_te_tree_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_004_004_residual_harmonic_mlp_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/004_residual_harmonic_mlp_global.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-29-16-00-20__te_residual_harmonic_mlp_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T16:00:20`
- End Time: `2026-06-29T16:22:47`
- Duration: `00:22:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-00-20__te_residual_harmonic_mlp_global`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-00-20__te_residual_harmonic_mlp_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-00-20__te_residual_harmonic_mlp_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-00-20__te_residual_harmonic_mlp_global\checkpoints\residual_harmonic_mlp-epoch=100-val_mae=0.00162131.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-00-20__te_residual_harmonic_mlp_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-00-20__te_residual_harmonic_mlp_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/004_te_residual_harmonic_mlp_global.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_005_005_residual_harmonic_mlp_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/005_residual_harmonic_mlp_fw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-29-16-22-47__te_residual_harmonic_mlp_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T16:22:47`
- End Time: `2026-06-29T16:42:14`
- Duration: `00:19:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-22-47__te_residual_harmonic_mlp_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-22-47__te_residual_harmonic_mlp_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-22-47__te_residual_harmonic_mlp_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-22-47__te_residual_harmonic_mlp_fw\checkpoints\residual_harmonic_mlp-epoch=098-val_mae=0.00163209.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-22-47__te_residual_harmonic_mlp_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-22-47__te_residual_harmonic_mlp_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/005_te_residual_harmonic_mlp_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_mlp_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_006_006_residual_harmonic_mlp_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/006_residual_harmonic_mlp_bw.yaml`
- Model Type: `residual_harmonic_mlp`
- Run Instance Id: `2026-06-29-16-42-14__te_residual_harmonic_mlp_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T16:42:14`
- End Time: `2026-06-29T16:58:51`
- Duration: `00:16:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-42-14__te_residual_harmonic_mlp_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-42-14__te_residual_harmonic_mlp_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-42-14__te_residual_harmonic_mlp_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-42-14__te_residual_harmonic_mlp_bw\checkpoints\residual_harmonic_mlp-epoch=065-val_mae=0.00163724.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-42-14__te_residual_harmonic_mlp_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_mlp/2026-06-29-16-42-14__te_residual_harmonic_mlp_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/006_te_residual_harmonic_mlp_bw.log`
- Error Message: `N/A`

### te_feedforward_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_007_007_feedforward_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/007_feedforward_global.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-29-16-58-51__te_feedforward_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T16:58:51`
- End Time: `2026-06-29T17:38:58`
- Duration: `00:40:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-29-16-58-51__te_feedforward_global`
- Config Snapshot: `output/training_runs/feedforward/2026-06-29-16-58-51__te_feedforward_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-29-16-58-51__te_feedforward_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-16-58-51__te_feedforward_global\checkpoints\feedforward-epoch=090-val_mae=0.00167189.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-29-16-58-51__te_feedforward_global/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-29-16-58-51__te_feedforward_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/007_te_feedforward_global.log`
- Error Message: `N/A`

### te_feedforward_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_008_008_feedforward_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/008_feedforward_fw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-29-17-38-58__te_feedforward_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T17:38:58`
- End Time: `2026-06-29T18:24:42`
- Duration: `00:45:44`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-29-17-38-58__te_feedforward_fw`
- Config Snapshot: `output/training_runs/feedforward/2026-06-29-17-38-58__te_feedforward_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-29-17-38-58__te_feedforward_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-17-38-58__te_feedforward_fw\checkpoints\feedforward-epoch=140-val_mae=0.00165413.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-29-17-38-58__te_feedforward_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-29-17-38-58__te_feedforward_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/008_te_feedforward_fw.log`
- Error Message: `N/A`

### te_feedforward_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_009_009_feedforward_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/009_feedforward_bw.yaml`
- Model Type: `feedforward`
- Run Instance Id: `2026-06-29-18-24-42__te_feedforward_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T18:24:42`
- End Time: `2026-06-29T19:27:09`
- Duration: `01:02:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/feedforward/2026-06-29-18-24-42__te_feedforward_bw`
- Config Snapshot: `output/training_runs/feedforward/2026-06-29-18-24-42__te_feedforward_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/feedforward/2026-06-29-18-24-42__te_feedforward_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-18-24-42__te_feedforward_bw\checkpoints\feedforward-epoch=188-val_mae=0.00163049.ckpt`
- Metrics Snapshot: `output/training_runs/feedforward/2026-06-29-18-24-42__te_feedforward_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/feedforward/2026-06-29-18-24-42__te_feedforward_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/009_te_feedforward_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_010_010_periodic_mlp_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/010_periodic_mlp_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-19-27-09__te_periodic_mlp_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T19:27:09`
- End Time: `2026-06-29T19:46:45`
- Duration: `00:19:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-29-19-27-09__te_periodic_mlp_global`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-29-19-27-09__te_periodic_mlp_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-29-19-27-09__te_periodic_mlp_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-19-27-09__te_periodic_mlp_global\checkpoints\periodic_mlp-epoch=113-val_mae=0.00165497.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-29-19-27-09__te_periodic_mlp_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-29-19-27-09__te_periodic_mlp_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/010_te_periodic_mlp_global.log`
- Error Message: `N/A`

### te_periodic_mlp_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_011_011_periodic_mlp_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/011_periodic_mlp_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-19-46-45__te_periodic_mlp_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T19:46:45`
- End Time: `2026-06-29T20:02:16`
- Duration: `00:15:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-29-19-46-45__te_periodic_mlp_fw`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-29-19-46-45__te_periodic_mlp_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-29-19-46-45__te_periodic_mlp_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-19-46-45__te_periodic_mlp_fw\checkpoints\periodic_mlp-epoch=064-val_mae=0.00167050.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-29-19-46-45__te_periodic_mlp_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-29-19-46-45__te_periodic_mlp_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/011_te_periodic_mlp_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_012_012_periodic_mlp_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/012_periodic_mlp_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-20-02-16__te_periodic_mlp_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T20:02:16`
- End Time: `2026-06-29T20:22:24`
- Duration: `00:20:08`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp/2026-06-29-20-02-16__te_periodic_mlp_bw`
- Config Snapshot: `output/training_runs/periodic_mlp/2026-06-29-20-02-16__te_periodic_mlp_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp/2026-06-29-20-02-16__te_periodic_mlp_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-20-02-16__te_periodic_mlp_bw\checkpoints\periodic_mlp-epoch=094-val_mae=0.00165793.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp/2026-06-29-20-02-16__te_periodic_mlp_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp/2026-06-29-20-02-16__te_periodic_mlp_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/012_te_periodic_mlp_bw.log`
- Error Message: `N/A`

### te_harmonic_regression_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_013_013_harmonic_regression_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/013_harmonic_regression_global.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-29-20-22-24__te_harmonic_regression_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T20:22:24`
- End Time: `2026-06-29T20:32:49`
- Duration: `00:10:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-29-20-22-24__te_harmonic_regression_global`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-22-24__te_harmonic_regression_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-29-20-22-24__te_harmonic_regression_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-22-24__te_harmonic_regression_global\checkpoints\harmonic_regression-epoch=054-val_mae=0.00389853.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-22-24__te_harmonic_regression_global/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-29-20-22-24__te_harmonic_regression_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/013_te_harmonic_regression_global.log`
- Error Message: `N/A`

### te_harmonic_regression_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_014_014_harmonic_regression_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/014_harmonic_regression_fw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-29-20-32-49__te_harmonic_regression_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T20:32:49`
- End Time: `2026-06-29T20:42:56`
- Duration: `00:10:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-29-20-32-49__te_harmonic_regression_fw`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-32-49__te_harmonic_regression_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-29-20-32-49__te_harmonic_regression_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-32-49__te_harmonic_regression_fw\checkpoints\harmonic_regression-epoch=042-val_mae=0.00390024.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-32-49__te_harmonic_regression_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-29-20-32-49__te_harmonic_regression_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/014_te_harmonic_regression_fw.log`
- Error Message: `N/A`

### te_harmonic_regression_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_015_015_harmonic_regression_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/015_harmonic_regression_bw.yaml`
- Model Type: `harmonic_regression`
- Run Instance Id: `2026-06-29-20-42-56__te_harmonic_regression_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T20:42:56`
- End Time: `2026-06-29T20:54:24`
- Duration: `00:11:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/harmonic_regression/2026-06-29-20-42-56__te_harmonic_regression_bw`
- Config Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-42-56__te_harmonic_regression_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/harmonic_regression/2026-06-29-20-42-56__te_harmonic_regression_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-42-56__te_harmonic_regression_bw\checkpoints\harmonic_regression-epoch=029-val_mae=0.00389217.ckpt`
- Metrics Snapshot: `output/training_runs/harmonic_regression/2026-06-29-20-42-56__te_harmonic_regression_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/harmonic_regression/2026-06-29-20-42-56__te_harmonic_regression_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/015_te_harmonic_regression_bw.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_016_016_periodic_mlp_harmonic_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/016_periodic_mlp_harmonic_global.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-20-54-24__te_periodic_mlp_harmonic_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T20:54:24`
- End Time: `2026-06-29T21:10:12`
- Duration: `00:15:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-29-20-54-24__te_periodic_mlp_harmonic_global`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-20-54-24__te_periodic_mlp_harmonic_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-29-20-54-24__te_periodic_mlp_harmonic_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-20-54-24__te_periodic_mlp_harmonic_global\checkpoints\periodic_mlp-epoch=061-val_mae=0.00126497.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-20-54-24__te_periodic_mlp_harmonic_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-29-20-54-24__te_periodic_mlp_harmonic_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/016_te_periodic_mlp_harmonic_global.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_017_017_periodic_mlp_harmonic_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/017_periodic_mlp_harmonic_fw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T21:10:12`
- End Time: `2026-06-29T21:27:22`
- Duration: `00:17:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw\checkpoints\periodic_mlp-epoch=071-val_mae=0.00120864.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/017_te_periodic_mlp_harmonic_fw.log`
- Error Message: `N/A`

### te_periodic_mlp_harmonic_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_018_018_periodic_mlp_harmonic_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/018_periodic_mlp_harmonic_bw.yaml`
- Model Type: `periodic_mlp`
- Run Instance Id: `2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T21:27:22`
- End Time: `2026-06-29T21:48:10`
- Duration: `00:20:48`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw`
- Config Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw\checkpoints\periodic_mlp-epoch=126-val_mae=0.00118841.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_mlp_harmonic/2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/018_te_periodic_mlp_harmonic_bw.log`
- Error Message: `N/A`

### te_temporal_convolution_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_019_019_temporal_convolution_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/019_temporal_convolution_global.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-29-21-48-10__te_temporal_convolution_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T21:48:10`
- End Time: `2026-06-29T22:10:25`
- Duration: `00:22:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-29-21-48-10__te_temporal_convolution_global`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-29-21-48-10__te_temporal_convolution_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-29-21-48-10__te_temporal_convolution_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-21-48-10__te_temporal_convolution_global\checkpoints\temporal_convolution-epoch=111-val_mae=0.00229596.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-29-21-48-10__te_temporal_convolution_global/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-29-21-48-10__te_temporal_convolution_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/019_te_temporal_convolution_global.log`
- Error Message: `N/A`

### te_temporal_convolution_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_020_020_temporal_convolution_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/020_temporal_convolution_fw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-29-22-10-26__te_temporal_convolution_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T22:10:26`
- End Time: `2026-06-29T22:25:32`
- Duration: `00:15:07`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-29-22-10-26__te_temporal_convolution_fw`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-29-22-10-26__te_temporal_convolution_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-29-22-10-26__te_temporal_convolution_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-22-10-26__te_temporal_convolution_fw\checkpoints\temporal_convolution-epoch=051-val_mae=0.00233879.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-29-22-10-26__te_temporal_convolution_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-29-22-10-26__te_temporal_convolution_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/020_te_temporal_convolution_fw.log`
- Error Message: `N/A`

### te_temporal_convolution_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_021_021_temporal_convolution_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/021_temporal_convolution_bw.yaml`
- Model Type: `temporal_convolution`
- Run Instance Id: `2026-06-29-22-25-32__te_temporal_convolution_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T22:25:32`
- End Time: `2026-06-29T22:50:48`
- Duration: `00:25:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/temporal_convolution/2026-06-29-22-25-32__te_temporal_convolution_bw`
- Config Snapshot: `output/training_runs/temporal_convolution/2026-06-29-22-25-32__te_temporal_convolution_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/temporal_convolution/2026-06-29-22-25-32__te_temporal_convolution_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-22-25-32__te_temporal_convolution_bw\checkpoints\temporal_convolution-epoch=100-val_mae=0.00223589.ckpt`
- Metrics Snapshot: `output/training_runs/temporal_convolution/2026-06-29-22-25-32__te_temporal_convolution_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/temporal_convolution/2026-06-29-22-25-32__te_temporal_convolution_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/021_te_temporal_convolution_bw.log`
- Error Message: `N/A`

### te_gru_sequence_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_022_022_gru_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/022_gru_sequence_global.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-29-22-50-48__te_gru_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-29T22:50:48`
- End Time: `2026-06-29T23:06:25`
- Duration: `00:15:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-29-22-50-48__te_gru_sequence_global`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-29-22-50-48__te_gru_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-29-22-50-48__te_gru_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-22-50-48__te_gru_sequence_global\checkpoints\gru_sequence-epoch=050-val_mae=0.00220547.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-29-22-50-48__te_gru_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-29-22-50-48__te_gru_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/022_te_gru_sequence_global.log`
- Error Message: `N/A`

### te_gru_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_023_023_gru_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/023_gru_sequence_fw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-29-23-06-26__te_gru_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-29T23:06:26`
- End Time: `2026-06-29T23:36:20`
- Duration: `00:29:54`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-29-23-06-26__te_gru_sequence_fw`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-29-23-06-26__te_gru_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-29-23-06-26__te_gru_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-23-06-26__te_gru_sequence_fw\checkpoints\gru_sequence-epoch=153-val_mae=0.00213020.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-29-23-06-26__te_gru_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-29-23-06-26__te_gru_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/023_te_gru_sequence_fw.log`
- Error Message: `N/A`

### te_gru_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_024_024_gru_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/024_gru_sequence_bw.yaml`
- Model Type: `gru_sequence`
- Run Instance Id: `2026-06-29-23-36-20__te_gru_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-29T23:36:20`
- End Time: `2026-06-30T00:09:49`
- Duration: `00:33:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/gru_sequence/2026-06-29-23-36-20__te_gru_sequence_bw`
- Config Snapshot: `output/training_runs/gru_sequence/2026-06-29-23-36-20__te_gru_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/gru_sequence/2026-06-29-23-36-20__te_gru_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\gru_sequence\2026-06-29-23-36-20__te_gru_sequence_bw\checkpoints\gru_sequence-epoch=148-val_mae=0.00211895.ckpt`
- Metrics Snapshot: `output/training_runs/gru_sequence/2026-06-29-23-36-20__te_gru_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/gru_sequence/2026-06-29-23-36-20__te_gru_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/024_te_gru_sequence_bw.log`
- Error Message: `N/A`

### te_lstm_sequence_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_025_025_lstm_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/025_lstm_sequence_global.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-30-00-09-49__te_lstm_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T00:09:49`
- End Time: `2026-06-30T00:39:32`
- Duration: `00:29:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-30-00-09-49__te_lstm_sequence_global`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-30-00-09-49__te_lstm_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-30-00-09-49__te_lstm_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-00-09-49__te_lstm_sequence_global\checkpoints\lstm_sequence-epoch=145-val_mae=0.00213809.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-30-00-09-49__te_lstm_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-30-00-09-49__te_lstm_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/025_te_lstm_sequence_global.log`
- Error Message: `N/A`

### te_lstm_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_026_026_lstm_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/026_lstm_sequence_fw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-30-00-39-32__te_lstm_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T00:39:32`
- End Time: `2026-06-30T01:02:22`
- Duration: `00:22:50`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-30-00-39-32__te_lstm_sequence_fw`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-30-00-39-32__te_lstm_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-30-00-39-32__te_lstm_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-00-39-32__te_lstm_sequence_fw\checkpoints\lstm_sequence-epoch=085-val_mae=0.00216870.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-30-00-39-32__te_lstm_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-30-00-39-32__te_lstm_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/026_te_lstm_sequence_fw.log`
- Error Message: `N/A`

### te_lstm_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_027_027_lstm_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/027_lstm_sequence_bw.yaml`
- Model Type: `lstm_sequence`
- Run Instance Id: `2026-06-30-01-02-22__te_lstm_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T01:02:22`
- End Time: `2026-06-30T01:29:35`
- Duration: `00:27:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/lstm_sequence/2026-06-30-01-02-22__te_lstm_sequence_bw`
- Config Snapshot: `output/training_runs/lstm_sequence/2026-06-30-01-02-22__te_lstm_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/lstm_sequence/2026-06-30-01-02-22__te_lstm_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-01-02-22__te_lstm_sequence_bw\checkpoints\lstm_sequence-epoch=138-val_mae=0.00214675.ckpt`
- Metrics Snapshot: `output/training_runs/lstm_sequence/2026-06-30-01-02-22__te_lstm_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/lstm_sequence/2026-06-30-01-02-22__te_lstm_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/027_te_lstm_sequence_bw.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_028_028_periodic_temporal_convolution_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/028_periodic_temporal_convolution_global.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-30-01-29-35__te_periodic_temporal_convolution_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T01:29:35`
- End Time: `2026-06-30T01:43:44`
- Duration: `00:14:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-29-35__te_periodic_temporal_convolution_global`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-29-35__te_periodic_temporal_convolution_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-29-35__te_periodic_temporal_convolution_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-29-35__te_periodic_temporal_convolution_global\checkpoints\periodic_temporal_convolution-epoch=030-val_mae=0.00215997.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-29-35__te_periodic_temporal_convolution_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-29-35__te_periodic_temporal_convolution_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/028_te_periodic_temporal_convolution_global.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_029_029_periodic_temporal_convolution_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/029_periodic_temporal_convolution_fw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-30-01-43-44__te_periodic_temporal_convolution_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T01:43:44`
- End Time: `2026-06-30T01:59:09`
- Duration: `00:15:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-43-44__te_periodic_temporal_convolution_fw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-43-44__te_periodic_temporal_convolution_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-43-44__te_periodic_temporal_convolution_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-43-44__te_periodic_temporal_convolution_fw\checkpoints\periodic_temporal_convolution-epoch=076-val_mae=0.00220865.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-43-44__te_periodic_temporal_convolution_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-43-44__te_periodic_temporal_convolution_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/029_te_periodic_temporal_convolution_fw.log`
- Error Message: `N/A`

### te_periodic_temporal_convolution_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_030_030_periodic_temporal_convolution_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/030_periodic_temporal_convolution_bw.yaml`
- Model Type: `periodic_temporal_convolution`
- Run Instance Id: `2026-06-30-01-59-09__te_periodic_temporal_convolution_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T01:59:09`
- End Time: `2026-06-30T02:14:43`
- Duration: `00:15:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-59-09__te_periodic_temporal_convolution_bw`
- Config Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-59-09__te_periodic_temporal_convolution_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-59-09__te_periodic_temporal_convolution_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-59-09__te_periodic_temporal_convolution_bw\checkpoints\periodic_temporal_convolution-epoch=064-val_mae=0.00207692.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-59-09__te_periodic_temporal_convolution_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_temporal_convolution/2026-06-30-01-59-09__te_periodic_temporal_convolution_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/030_te_periodic_temporal_convolution_bw.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_031_031_periodic_gru_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/031_periodic_gru_sequence_global.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-30-02-14-43__te_periodic_gru_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T02:14:43`
- End Time: `2026-06-30T02:56:10`
- Duration: `00:41:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-30-02-14-43__te_periodic_gru_sequence_global`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-02-14-43__te_periodic_gru_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-30-02-14-43__te_periodic_gru_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-02-14-43__te_periodic_gru_sequence_global\checkpoints\periodic_gru_sequence-epoch=236-val_mae=0.00113201.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-02-14-43__te_periodic_gru_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-30-02-14-43__te_periodic_gru_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/031_te_periodic_gru_sequence_global.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_032_032_periodic_gru_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/032_periodic_gru_sequence_fw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-30-02-56-10__te_periodic_gru_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T02:56:10`
- End Time: `2026-06-30T03:41:33`
- Duration: `00:45:23`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-30-02-56-10__te_periodic_gru_sequence_fw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-02-56-10__te_periodic_gru_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-30-02-56-10__te_periodic_gru_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-02-56-10__te_periodic_gru_sequence_fw\checkpoints\periodic_gru_sequence-epoch=235-val_mae=0.00108406.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-02-56-10__te_periodic_gru_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-30-02-56-10__te_periodic_gru_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/032_te_periodic_gru_sequence_fw.log`
- Error Message: `N/A`

### te_periodic_gru_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_033_033_periodic_gru_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/033_periodic_gru_sequence_bw.yaml`
- Model Type: `periodic_gru_sequence`
- Run Instance Id: `2026-06-30-03-41-33__te_periodic_gru_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T03:41:33`
- End Time: `2026-06-30T04:26:36`
- Duration: `00:45:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_gru_sequence/2026-06-30-03-41-33__te_periodic_gru_sequence_bw`
- Config Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-03-41-33__te_periodic_gru_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_gru_sequence/2026-06-30-03-41-33__te_periodic_gru_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-03-41-33__te_periodic_gru_sequence_bw\checkpoints\periodic_gru_sequence-epoch=242-val_mae=0.00115776.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_gru_sequence/2026-06-30-03-41-33__te_periodic_gru_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_gru_sequence/2026-06-30-03-41-33__te_periodic_gru_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/033_te_periodic_gru_sequence_bw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_034_034_periodic_lstm_sequence_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/034_periodic_lstm_sequence_global.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-30-04-26-36__te_periodic_lstm_sequence_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T04:26:36`
- End Time: `2026-06-30T04:57:16`
- Duration: `00:30:40`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-26-36__te_periodic_lstm_sequence_global`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-26-36__te_periodic_lstm_sequence_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-26-36__te_periodic_lstm_sequence_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-04-26-36__te_periodic_lstm_sequence_global\checkpoints\periodic_lstm_sequence-epoch=124-val_mae=0.00153599.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-26-36__te_periodic_lstm_sequence_global/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-26-36__te_periodic_lstm_sequence_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/034_te_periodic_lstm_sequence_global.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_035_035_periodic_lstm_sequence_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/035_periodic_lstm_sequence_fw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-30-04-57-16__te_periodic_lstm_sequence_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T04:57:16`
- End Time: `2026-06-30T05:26:57`
- Duration: `00:29:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-57-16__te_periodic_lstm_sequence_fw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-57-16__te_periodic_lstm_sequence_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-57-16__te_periodic_lstm_sequence_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-04-57-16__te_periodic_lstm_sequence_fw\checkpoints\periodic_lstm_sequence-epoch=118-val_mae=0.00151323.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-57-16__te_periodic_lstm_sequence_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-30-04-57-16__te_periodic_lstm_sequence_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/035_te_periodic_lstm_sequence_fw.log`
- Error Message: `N/A`

### te_periodic_lstm_sequence_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_036_036_periodic_lstm_sequence_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/036_periodic_lstm_sequence_bw.yaml`
- Model Type: `periodic_lstm_sequence`
- Run Instance Id: `2026-06-30-05-26-57__te_periodic_lstm_sequence_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T05:26:57`
- End Time: `2026-06-30T06:13:35`
- Duration: `00:46:38`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/periodic_lstm_sequence/2026-06-30-05-26-57__te_periodic_lstm_sequence_bw`
- Config Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-05-26-57__te_periodic_lstm_sequence_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/periodic_lstm_sequence/2026-06-30-05-26-57__te_periodic_lstm_sequence_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-05-26-57__te_periodic_lstm_sequence_bw\checkpoints\periodic_lstm_sequence-epoch=250-val_mae=0.00122970.ckpt`
- Metrics Snapshot: `output/training_runs/periodic_lstm_sequence/2026-06-30-05-26-57__te_periodic_lstm_sequence_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/periodic_lstm_sequence/2026-06-30-05-26-57__te_periodic_lstm_sequence_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/036_te_periodic_lstm_sequence_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_037_037_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/037_residual_harmonic_gru_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T06:13:35`
- End Time: `2026-06-30T06:36:17`
- Duration: `00:22:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global\checkpoints\residual_harmonic_gru_sequence-epoch=076-val_mae=0.00197322.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-13-35__te_residual_harmonic_gru_sequence_sparse_rcim_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/037_te_residual_harmonic_gru_sequence_sparse_rcim_gl.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_038_038_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/038_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T06:36:17`
- End Time: `2026-06-30T07:08:04`
- Duration: `00:31:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw\checkpoints\residual_harmonic_gru_sequence-epoch=130-val_mae=0.00194226.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-06-36-17__te_residual_harmonic_gru_sequence_sparse_rcim_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/038_te_residual_harmonic_gru_sequence_sparse_rcim_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_sparse_rcim_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_039_039_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/039_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T07:08:04`
- End Time: `2026-06-30T07:33:14`
- Duration: `00:25:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_sparse_rcim\2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw\checkpoints\residual_harmonic_gru_sequence-epoch=109-val_mae=0.00195543.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-06-30-07-08-04__te_residual_harmonic_gru_sequence_sparse_rcim_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/039_te_residual_harmonic_gru_sequence_sparse_rcim_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense240_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_040_040_residual_harmonic_gru_sequence_dense240_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/040_residual_harmonic_gru_sequence_dense240_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T07:33:15`
- End Time: `2026-06-30T08:20:41`
- Duration: `00:47:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global\checkpoints\residual_harmonic_gru_sequence-epoch=136-val_mae=0.00196656.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/040_te_residual_harmonic_gru_sequence_dense240_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense240_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_041_041_residual_harmonic_gru_sequence_dense240_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/041_residual_harmonic_gru_sequence_dense240_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T08:20:41`
- End Time: `2026-06-30T08:46:28`
- Duration: `00:25:47`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw\checkpoints\residual_harmonic_gru_sequence-epoch=068-val_mae=0.00202486.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/041_te_residual_harmonic_gru_sequence_dense240_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense240_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_042_042_residual_harmonic_gru_sequence_dense240_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/042_residual_harmonic_gru_sequence_dense240_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T08:46:29`
- End Time: `2026-06-30T09:29:35`
- Duration: `00:43:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw\checkpoints\residual_harmonic_gru_sequence-epoch=119-val_mae=0.00198404.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense240/2026-06-30-08-46-29__te_residual_harmonic_gru_sequence_dense240_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/042_te_residual_harmonic_gru_sequence_dense240_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_043_043_residual_harmonic_gru_sequence_dense360_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/043_residual_harmonic_gru_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T09:29:35`
- End Time: `2026-06-30T09:59:47`
- Duration: `00:30:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global\checkpoints\residual_harmonic_gru_sequence-epoch=050-val_mae=0.00202033.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/043_te_residual_harmonic_gru_sequence_dense360_globa.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_044_044_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/044_residual_harmonic_gru_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T09:59:47`
- End Time: `2026-06-30T10:54:39`
- Duration: `00:54:52`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw\checkpoints\residual_harmonic_gru_sequence-epoch=133-val_mae=0.00196756.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/044_te_residual_harmonic_gru_sequence_dense360_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_gru_sequence_dense360_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_045_045_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/045_residual_harmonic_gru_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_gru_sequence`
- Run Instance Id: `2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T10:54:39`
- End Time: `2026-06-30T11:45:13`
- Duration: `00:50:34`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw\checkpoints\residual_harmonic_gru_sequence-epoch=138-val_mae=0.00197936.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_gru_sequence_dense360/2026-06-30-10-54-39__te_residual_harmonic_gru_sequence_dense360_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/045_te_residual_harmonic_gru_sequence_dense360_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_046_046_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/046_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T11:45:14`
- End Time: `2026-06-30T12:17:13`
- Duration: `00:32:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global\checkpoints\residual_harmonic_lstm_sequence-epoch=126-val_mae=0.00195406.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/046_te_residual_harmonic_lstm_sequence_sparse_rcim_g.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_047_047_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/047_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T12:17:14`
- End Time: `2026-06-30T12:41:44`
- Duration: `00:24:30`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=082-val_mae=0.00197149.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/047_te_residual_harmonic_lstm_sequence_sparse_rcim_f.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_sparse_rcim_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_048_048_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/048_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T12:41:44`
- End Time: `2026-06-30T13:02:13`
- Duration: `00:20:29`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=091-val_mae=0.00199396.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/048_te_residual_harmonic_lstm_sequence_sparse_rcim_b.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense240_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_049_049_residual_harmonic_lstm_sequence_dense240_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/049_residual_harmonic_lstm_sequence_dense240_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T13:02:13`
- End Time: `2026-06-30T13:32:16`
- Duration: `00:30:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global\checkpoints\residual_harmonic_lstm_sequence-epoch=061-val_mae=0.00203116.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/049_te_residual_harmonic_lstm_sequence_dense240_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense240_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_050_050_residual_harmonic_lstm_sequence_dense240_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/050_residual_harmonic_lstm_sequence_dense240_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T13:32:17`
- End Time: `2026-06-30T13:54:14`
- Duration: `00:21:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=032-val_mae=0.00204432.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/050_te_residual_harmonic_lstm_sequence_dense240_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense240_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_051_051_residual_harmonic_lstm_sequence_dense240_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/051_residual_harmonic_lstm_sequence_dense240_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T13:54:15`
- End Time: `2026-06-30T14:20:06`
- Duration: `00:25:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=047-val_mae=0.00204037.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/051_te_residual_harmonic_lstm_sequence_dense240_bw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_052_052_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/052_residual_harmonic_lstm_sequence_dense360_global.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T14:20:06`
- End Time: `2026-06-30T14:47:33`
- Duration: `00:27:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global\checkpoints\residual_harmonic_lstm_sequence-epoch=037-val_mae=0.00207083.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/052_te_residual_harmonic_lstm_sequence_dense360_glob.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_053_053_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/053_residual_harmonic_lstm_sequence_dense360_fw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T14:47:34`
- End Time: `2026-06-30T15:15:33`
- Duration: `00:28:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=065-val_mae=0.00206567.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/053_te_residual_harmonic_lstm_sequence_dense360_fw.log`
- Error Message: `N/A`

### te_residual_harmonic_lstm_sequence_dense360_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_054_054_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/054_residual_harmonic_lstm_sequence_dense360_bw.yaml`
- Model Type: `residual_harmonic_lstm_sequence`
- Run Instance Id: `2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T15:15:34`
- End Time: `2026-06-30T16:02:19`
- Duration: `00:46:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw`
- Config Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=100-val_mae=0.00200719.ckpt`
- Metrics Snapshot: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/054_te_residual_harmonic_lstm_sequence_dense360_bw.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_055_055_wave3_1_sequential_residual_offset_probe_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/055_wave3_1_sequential_residual_offset_probe_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T16:02:20`
- End Time: `2026-06-30T16:25:21`
- Duration: `00:23:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global\checkpoints\sequential_residual_offset_probe-epoch=101-val_mae=0.00214720.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/055_te_wave3_1_sequential_residual_offset_probe_glob.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_056_056_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/056_wave3_1_sequential_residual_offset_probe_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T16:25:21`
- End Time: `2026-06-30T16:49:34`
- Duration: `00:24:13`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw\checkpoints\sequential_residual_offset_probe-epoch=110-val_mae=0.00215428.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/056_te_wave3_1_sequential_residual_offset_probe_fw.log`
- Error Message: `N/A`

### te_wave3_1_sequential_residual_offset_probe_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_057_057_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/057_wave3_1_sequential_residual_offset_probe_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T16:49:34`
- End Time: `2026-06-30T17:18:40`
- Duration: `00:29:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw`
- Config Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw\checkpoints\sequential_residual_offset_probe-epoch=152-val_mae=0.00214684.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_1_sequential_residual_offset_probe/2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/057_te_wave3_1_sequential_residual_offset_probe_bw.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_058_058_wave3_2_clean_sequential_residual_offset_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/058_wave3_2_clean_sequential_residual_offset_global.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T17:18:40`
- End Time: `2026-06-30T17:46:46`
- Duration: `00:28:06`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global\checkpoints\sequential_residual_offset_probe-epoch=133-val_mae=0.00215807.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/058_te_wave3_2_clean_sequential_residual_offset_glob.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_059_059_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/059_wave3_2_clean_sequential_residual_offset_fw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T17:46:46`
- End Time: `2026-06-30T18:12:47`
- Duration: `00:26:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw\checkpoints\sequential_residual_offset_probe-epoch=127-val_mae=0.00215929.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/059_te_wave3_2_clean_sequential_residual_offset_fw.log`
- Error Message: `N/A`

### te_wave3_2_clean_sequential_residual_offset_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_060_060_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/060_wave3_2_clean_sequential_residual_offset_bw.yaml`
- Model Type: `sequential_residual_offset_probe`
- Run Instance Id: `2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T18:12:48`
- End Time: `2026-06-30T18:43:05`
- Duration: `00:30:17`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw`
- Config Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw\checkpoints\sequential_residual_offset_probe-epoch=155-val_mae=0.00214982.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_clean_sequential_residual_offset/2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/060_te_wave3_2_clean_sequential_residual_offset_bw.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_061_061_wave3_2_harmonic_residual_offset_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/061_wave3_2_harmonic_residual_offset_global.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T18:43:05`
- End Time: `2026-06-30T19:14:25`
- Duration: `00:31:20`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global\checkpoints\harmonic_residual_offset_probe-epoch=124-val_mae=0.00178297.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/061_te_wave3_2_harmonic_residual_offset_global.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_062_062_wave3_2_harmonic_residual_offset_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/062_wave3_2_harmonic_residual_offset_fw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T19:14:26`
- End Time: `2026-06-30T19:35:51`
- Duration: `00:21:25`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw\checkpoints\harmonic_residual_offset_probe-epoch=066-val_mae=0.00180926.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/062_te_wave3_2_harmonic_residual_offset_fw.log`
- Error Message: `N/A`

### te_wave3_2_harmonic_residual_offset_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_063_063_wave3_2_harmonic_residual_offset_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/063_wave3_2_harmonic_residual_offset_bw.yaml`
- Model Type: `harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T19:35:52`
- End Time: `2026-06-30T20:13:16`
- Duration: `00:37:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw`
- Config Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw\checkpoints\harmonic_residual_offset_probe-epoch=192-val_mae=0.00179089.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_2_harmonic_residual_offset/2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/063_te_wave3_2_harmonic_residual_offset_bw.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_064_064_wave3_3_curve_aware_pointwise_control_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/064_wave3_3_curve_aware_pointwise_control_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T20:13:16`
- End Time: `2026-06-30T20:40:49`
- Duration: `00:27:33`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=064-val_mae=0.00183684.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/064_te_wave3_3_curve_aware_pointwise_control_global.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_065_065_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/065_wave3_3_curve_aware_pointwise_control_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T20:40:49`
- End Time: `2026-06-30T21:21:08`
- Duration: `00:40:19`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=119-val_mae=0.00179175.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/065_te_wave3_3_curve_aware_pointwise_control_fw.log`
- Error Message: `N/A`

### te_wave3_3_curve_aware_pointwise_control_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_066_066_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/066_wave3_3_curve_aware_pointwise_control_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T21:21:09`
- End Time: `2026-06-30T21:57:36`
- Duration: `00:36:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw`
- Config Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=103-val_mae=0.00181463.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_curve_aware_pointwise_control/2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/066_te_wave3_3_curve_aware_pointwise_control_bw.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_067_067_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/067_wave3_3_raw_centered_shape_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T21:57:37`
- End Time: `2026-06-30T22:31:31`
- Duration: `00:33:54`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=092-val_mae=0.00179701.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/067_te_wave3_3_raw_centered_shape_curve_aware_global.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_068_068_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/068_wave3_3_raw_centered_shape_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw`
- Queue Status: `completed`
- Start Time: `2026-06-30T22:31:32`
- End Time: `2026-06-30T23:05:54`
- Duration: `00:34:22`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=094-val_mae=0.00178919.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/068_te_wave3_3_raw_centered_shape_curve_aware_fw.log`
- Error Message: `N/A`

### te_wave3_3_raw_centered_shape_curve_aware_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_069_069_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/069_wave3_3_raw_centered_shape_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw`
- Queue Status: `completed`
- Start Time: `2026-06-30T23:05:54`
- End Time: `2026-06-30T23:45:36`
- Duration: `00:39:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw`
- Config Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=117-val_mae=0.00180437.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/069_te_wave3_3_raw_centered_shape_curve_aware_bw.log`
- Error Message: `N/A`

### te_wave3_3_raw_offset_curve_aware_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_070_070_wave3_3_raw_offset_curve_aware_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/070_wave3_3_raw_offset_curve_aware_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global`
- Queue Status: `completed`
- Start Time: `2026-06-30T23:45:36`
- End Time: `2026-07-01T00:11:35`
- Duration: `00:25:59`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=058-val_mae=0.00186253.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-06-30-23-45-36__te_wave3_3_raw_offset_curve_aware_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/070_te_wave3_3_raw_offset_curve_aware_global.log`
- Error Message: `N/A`

### te_wave3_3_raw_offset_curve_aware_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_071_071_wave3_3_raw_offset_curve_aware_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/071_wave3_3_raw_offset_curve_aware_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T00:11:36`
- End Time: `2026-07-01T00:39:38`
- Duration: `00:28:03`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=092-val_mae=0.00183328.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/071_te_wave3_3_raw_offset_curve_aware_fw.log`
- Error Message: `N/A`

### te_wave3_3_raw_offset_curve_aware_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_072_072_wave3_3_raw_offset_curve_aware_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/072_wave3_3_raw_offset_curve_aware_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T00:39:39`
- End Time: `2026-07-01T01:29:25`
- Duration: `00:49:46`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw`
- Config Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=160-val_mae=0.00176783.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/072_te_wave3_3_raw_offset_curve_aware_bw.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_073_073_wave3_3_full_curve_composite_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/073_wave3_3_full_curve_composite_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T01:29:25`
- End Time: `2026-07-01T02:04:09`
- Duration: `00:34:43`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=095-val_mae=0.00189366.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-01-29-25__te_wave3_3_full_curve_composite_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/073_te_wave3_3_full_curve_composite_global.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_074_074_wave3_3_full_curve_composite_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/074_wave3_3_full_curve_composite_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T02:04:09`
- End Time: `2026-07-01T02:30:04`
- Duration: `00:25:54`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=057-val_mae=0.00189842.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-04-09__te_wave3_3_full_curve_composite_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/074_te_wave3_3_full_curve_composite_fw.log`
- Error Message: `N/A`

### te_wave3_3_full_curve_composite_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_075_075_wave3_3_full_curve_composite_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/075_wave3_3_full_curve_composite_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T02:30:04`
- End Time: `2026-07-01T02:59:14`
- Duration: `00:29:10`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw`
- Config Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=071-val_mae=0.00191986.ckpt`
- Metrics Snapshot: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave3_3_full_curve_composite/2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/075_te_wave3_3_full_curve_composite_bw.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_076_076_wave4_1_mae_robust_loss_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/076_wave4_1_mae_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T02:59:15`
- End Time: `2026-07-01T03:49:35`
- Duration: `00:50:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=196-val_mae=0.00175450.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/076_te_wave4_1_mae_robust_loss_global.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_077_077_wave4_1_mae_robust_loss_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/077_wave4_1_mae_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T03:49:36`
- End Time: `2026-07-01T04:16:27`
- Duration: `00:26:51`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=061-val_mae=0.00180646.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/077_te_wave4_1_mae_robust_loss_fw.log`
- Error Message: `N/A`

### te_wave4_1_mae_robust_loss_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_078_078_wave4_1_mae_robust_loss_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/078_wave4_1_mae_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T04:16:28`
- End Time: `2026-07-01T05:08:43`
- Duration: `00:52:16`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw`
- Config Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=170-val_mae=0.00175748.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_mae_robust_loss/2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/078_te_wave4_1_mae_robust_loss_bw.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_079_079_wave4_1_smooth_l1_robust_loss_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/079_wave4_1_smooth_l1_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T05:08:44`
- End Time: `2026-07-01T05:31:05`
- Duration: `00:22:21`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=080-val_mae=0.00186636.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/079_te_wave4_1_smooth_l1_robust_loss_global.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_080_080_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/080_wave4_1_smooth_l1_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T05:31:06`
- End Time: `2026-07-01T05:54:18`
- Duration: `00:23:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=082-val_mae=0.00184069.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/080_te_wave4_1_smooth_l1_robust_loss_fw.log`
- Error Message: `N/A`

### te_wave4_1_smooth_l1_robust_loss_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_081_081_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/081_wave4_1_smooth_l1_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T05:54:19`
- End Time: `2026-07-01T06:18:29`
- Duration: `00:24:11`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw`
- Config Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=083-val_mae=0.00185081.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/081_te_wave4_1_smooth_l1_robust_loss_bw.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_082_082_wave4_1_log_cosh_robust_loss_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/082_wave4_1_log_cosh_robust_loss_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T06:18:30`
- End Time: `2026-07-01T06:59:33`
- Duration: `00:41:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=154-val_mae=0.00177642.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/082_te_wave4_1_log_cosh_robust_loss_global.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_083_083_wave4_1_log_cosh_robust_loss_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/083_wave4_1_log_cosh_robust_loss_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T06:59:33`
- End Time: `2026-07-01T07:40:32`
- Duration: `00:40:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=121-val_mae=0.00180694.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/083_te_wave4_1_log_cosh_robust_loss_fw.log`
- Error Message: `N/A`

### te_wave4_1_log_cosh_robust_loss_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_084_084_wave4_1_log_cosh_robust_loss_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/084_wave4_1_log_cosh_robust_loss_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T07:40:32`
- End Time: `2026-07-01T08:37:58`
- Duration: `00:57:26`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw`
- Config Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=191-val_mae=0.00176554.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/084_te_wave4_1_log_cosh_robust_loss_bw.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_085_085_wave4_2_quantile_p10_p50_p90_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/085_wave4_2_quantile_p10_p50_p90_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T08:37:59`
- End Time: `2026-07-01T09:37:13`
- Duration: `00:59:14`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=220-val_mae=0.00172811.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/085_te_wave4_2_quantile_p10_p50_p90_global.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_086_086_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/086_wave4_2_quantile_p10_p50_p90_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T09:37:14`
- End Time: `2026-07-01T10:36:42`
- Duration: `00:59:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=202-val_mae=0.00173095.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/086_te_wave4_2_quantile_p10_p50_p90_fw.log`
- Error Message: `N/A`

### te_wave4_2_quantile_p10_p50_p90_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_087_087_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/087_wave4_2_quantile_p10_p50_p90_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T10:36:43`
- End Time: `2026-07-01T11:22:24`
- Duration: `00:45:41`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw`
- Config Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=163-val_mae=0.00174118.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/087_te_wave4_2_quantile_p10_p50_p90_bw.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_088_088_wave4_2_gaussian_nll_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/088_wave4_2_gaussian_nll_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T11:22:25`
- End Time: `2026-07-01T11:54:10`
- Duration: `00:31:45`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=108-val_mae=0.00182486.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/088_te_wave4_2_gaussian_nll_global.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_089_089_wave4_2_gaussian_nll_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/089_wave4_2_gaussian_nll_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T11:54:11`
- End Time: `2026-07-01T12:57:09`
- Duration: `01:02:58`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=204-val_mae=0.00173884.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/089_te_wave4_2_gaussian_nll_fw.log`
- Error Message: `N/A`

### te_wave4_2_gaussian_nll_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_090_090_wave4_2_gaussian_nll_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/090_wave4_2_gaussian_nll_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T12:57:10`
- End Time: `2026-07-01T13:46:25`
- Duration: `00:49:15`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw`
- Config Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=168-val_mae=0.00177847.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_2_gaussian_nll/2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/090_te_wave4_2_gaussian_nll_bw.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_091_091_wave4_3_mixture_density_k2_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/091_wave4_3_mixture_density_k2_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T13:46:26`
- End Time: `2026-07-01T14:38:05`
- Duration: `00:51:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=165-val_mae=0.00154977.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-13-46-26__te_wave4_3_mixture_density_k2_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/091_te_wave4_3_mixture_density_k2_global.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_092_092_wave4_3_mixture_density_k2_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/092_wave4_3_mixture_density_k2_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T14:38:06`
- End Time: `2026-07-01T15:51:08`
- Duration: `01:13:02`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=255-val_mae=0.00149336.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-14-38-06__te_wave4_3_mixture_density_k2_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/092_te_wave4_3_mixture_density_k2_fw.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k2_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_093_093_wave4_3_mixture_density_k2_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/093_wave4_3_mixture_density_k2_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T15:51:09`
- End Time: `2026-07-01T16:40:21`
- Duration: `00:49:12`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k2\2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=133-val_mae=0.00152756.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k2/2026-07-01-15-51-09__te_wave4_3_mixture_density_k2_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/093_te_wave4_3_mixture_density_k2_bw.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_094_094_wave4_3_mixture_density_k3_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/094_wave4_3_mixture_density_k3_global.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T16:40:22`
- End Time: `2026-07-01T17:43:31`
- Duration: `01:03:09`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=187-val_mae=0.00140729.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-16-40-22__te_wave4_3_mixture_density_k3_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/094_te_wave4_3_mixture_density_k3_global.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_095_095_wave4_3_mixture_density_k3_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/095_wave4_3_mixture_density_k3_fw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T17:43:32`
- End Time: `2026-07-01T18:55:32`
- Duration: `01:12:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00150091.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-17-43-32__te_wave4_3_mixture_density_k3_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/095_te_wave4_3_mixture_density_k3_fw.log`
- Error Message: `N/A`

### te_wave4_3_mixture_density_k3_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_096_096_wave4_3_mixture_density_k3_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/096_wave4_3_mixture_density_k3_bw.yaml`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Run Instance Id: `2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T18:55:33`
- End Time: `2026-07-01T19:49:53`
- Duration: `00:54:20`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw`
- Config Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_3_mixture_density_k3\2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=150-val_mae=0.00151947.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_3_mixture_density_k3/2026-07-01-18-55-33__te_wave4_3_mixture_density_k3_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/096_te_wave4_3_mixture_density_k3_bw.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_097_097_wave4_4_gru_latent_offset_residual_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/097_wave4_4_gru_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T19:49:54`
- End Time: `2026-07-01T20:26:33`
- Duration: `00:36:39`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=171-val_mae=0.00219533.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/097_te_wave4_4_gru_latent_offset_residual_global.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_098_098_wave4_4_gru_latent_offset_residual_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/098_wave4_4_gru_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T20:26:34`
- End Time: `2026-07-01T20:55:24`
- Duration: `00:28:49`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=128-val_mae=0.00220084.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/098_te_wave4_4_gru_latent_offset_residual_fw.log`
- Error Message: `N/A`

### te_wave4_4_gru_latent_offset_residual_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_099_099_wave4_4_gru_latent_offset_residual_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/099_wave4_4_gru_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T20:55:24`
- End Time: `2026-07-01T21:33:26`
- Duration: `00:38:01`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw`
- Config Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=173-val_mae=0.00219051.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/099_te_wave4_4_gru_latent_offset_residual_bw.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_100_100_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/100_wave4_4_causal_tcn_latent_offset_residual_global.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T21:33:27`
- End Time: `2026-07-01T22:00:09`
- Duration: `00:26:42`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=135-val_mae=0.00221664.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/100_te_wave4_4_causal_tcn_latent_offset_residual_glo.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_101_101_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/101_wave4_4_causal_tcn_latent_offset_residual_fw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T22:00:10`
- End Time: `2026-07-01T22:28:38`
- Duration: `00:28:28`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=105-val_mae=0.00222384.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/101_te_wave4_4_causal_tcn_latent_offset_residual_fw.log`
- Error Message: `N/A`

### te_wave4_4_causal_tcn_latent_offset_residual_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_102_102_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/102_wave4_4_causal_tcn_latent_offset_residual_bw.yaml`
- Model Type: `latent_state_hysteresis_probe`
- Run Instance Id: `2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T22:28:39`
- End Time: `2026-07-01T22:59:07`
- Duration: `00:30:27`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw`
- Config Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=154-val_mae=0.00220405.ckpt`
- Metrics Snapshot: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/102_te_wave4_4_causal_tcn_latent_offset_residual_bw.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_103_103_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/103_wave5_1_harmonic_prior_pointwise_control_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global`
- Queue Status: `completed`
- Start Time: `2026-07-01T22:59:08`
- End Time: `2026-07-01T23:29:07`
- Duration: `00:30:00`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global\checkpoints\wave3_harmonic_prior_residual-epoch=080-val_mae=0.00189408.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/103_te_wave5_1_harmonic_prior_pointwise_control_glob.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_104_104_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/104_wave5_1_harmonic_prior_pointwise_control_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw`
- Queue Status: `completed`
- Start Time: `2026-07-01T23:29:08`
- End Time: `2026-07-01T23:48:39`
- Duration: `00:19:31`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw\checkpoints\wave3_harmonic_prior_residual-epoch=058-val_mae=0.00191340.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/104_te_wave5_1_harmonic_prior_pointwise_control_fw.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_pointwise_control_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_105_105_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/105_wave5_1_harmonic_prior_pointwise_control_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw`
- Queue Status: `completed`
- Start Time: `2026-07-01T23:48:40`
- End Time: `2026-07-02T00:24:37`
- Duration: `00:35:57`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw\checkpoints\wave3_harmonic_prior_residual-epoch=106-val_mae=0.00189325.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/105_te_wave5_1_harmonic_prior_pointwise_control_bw.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_global

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_106_106_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/106_wave5_1_harmonic_prior_smooth_l1_structured_global.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global`
- Queue Status: `completed`
- Start Time: `2026-07-02T00:24:38`
- End Time: `2026-07-02T00:54:14`
- Duration: `00:29:36`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=077-val_mae=0.00187023.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/106_te_wave5_1_harmonic_prior_smooth_l1_structured_g.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_fw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_107_107_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/107_wave5_1_harmonic_prior_smooth_l1_structured_fw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw`
- Queue Status: `completed`
- Start Time: `2026-07-02T00:54:15`
- End Time: `2026-07-02T01:22:38`
- Duration: `00:28:24`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw\checkpoints\wave3_harmonic_prior_residual-epoch=073-val_mae=0.00191209.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/107_te_wave5_1_harmonic_prior_smooth_l1_structured_f.log`
- Error Message: `N/A`

### te_wave5_1_harmonic_prior_smooth_l1_structured_bw

- Queue Config: `config/training/queue/polished_dataset_full_wave_retraining/completed/2026-06-29-15-54-17_108_108_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Source Config: `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/108_wave5_1_harmonic_prior_smooth_l1_structured_bw.yaml`
- Model Type: `wave3_harmonic_prior_residual`
- Run Instance Id: `2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw`
- Queue Status: `completed`
- Start Time: `2026-07-02T01:22:39`
- End Time: `2026-07-02T01:47:45`
- Duration: `00:25:05`
- Process Return Code: `0`
- Planning Report Path: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md`
- Output Directory: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw`
- Config Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw/training_config.yaml`
- Best Checkpoint Pointer: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw/best_checkpoint_path.txt`
- Best Checkpoint Path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw\checkpoints\wave3_harmonic_prior_residual-epoch=080-val_mae=0.00192112.ckpt`
- Metrics Snapshot: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw/metrics_summary.yaml`
- Training Report: `output/training_runs/wave5_1_harmonic_prior_smooth_l1_structured/2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw/training_test_report.md`
- Terminal Log: `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/logs/108_te_wave5_1_harmonic_prior_smooth_l1_structured_b.log`
- Error Message: `N/A`

## Post-Training Reporting Notes

Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.

Recommended references for the final report:

- `metrics_summary.yaml` for the common numeric comparison tables.
- `training_test_report.md` for per-run interpretation notes.
- `best_checkpoint_path.txt` for checkpoint traceability.
- `logs/*.log` for terminal-level diagnostics and failure analysis.
