# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\simplified_dataset`;
- comparison mode: `full_directional_candidate_matrix`;
- candidate count: `168`;
- held-out curve count before candidate filtering: `194`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;
- `global` candidates are evaluated on both directions and reported with
  direction-separated metrics.

## Candidate Inventory

| Candidate | Family | Source | Kind | Surface | Valid Directions | Model Source |
| --- | --- | --- | --- | --- | --- | --- |
| `SVM19_Fw` | `SVM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\svm_reference_models\reference_inventory.yaml` |
| `SVM19_Bw` | `SVM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\svm_reference_models\reference_inventory.yaml` |
| `MLP19_Fw` | `MLP` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\mlp_reference_models\reference_inventory.yaml` |
| `MLP19_Bw` | `MLP` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\reference_inventory.yaml` |
| `RF19_Fw` | `RF` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\rf_reference_models\reference_inventory.yaml` |
| `RF19_Bw` | `RF` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\rf_reference_models\reference_inventory.yaml` |
| `DT19_Fw` | `DT` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\dt_reference_models\reference_inventory.yaml` |
| `DT19_Bw` | `DT` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\dt_reference_models\reference_inventory.yaml` |
| `ET19_Fw` | `ET` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\et_reference_models\reference_inventory.yaml` |
| `ET19_Bw` | `ET` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\et_reference_models\reference_inventory.yaml` |
| `ERT19_Fw` | `ERT` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\ert_reference_models\reference_inventory.yaml` |
| `ERT19_Bw` | `ERT` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\ert_reference_models\reference_inventory.yaml` |
| `GBM19_Fw` | `GBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\gbm_reference_models\reference_inventory.yaml` |
| `GBM19_Bw` | `GBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\reference_inventory.yaml` |
| `HGBM19_Fw` | `HGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\hgbm_reference_models\reference_inventory.yaml` |
| `HGBM19_Bw` | `HGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\reference_inventory.yaml` |
| `XGBM19_Fw` | `XGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\xgbm_reference_models\reference_inventory.yaml` |
| `XGBM19_Bw` | `XGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\reference_inventory.yaml` |
| `LGBM19_Fw` | `LGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\lgbm_reference_models\reference_inventory.yaml` |
| `LGBM19_Bw` | `LGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\reference_inventory.yaml` |
| `ELM19_Fw` | `ELM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\elm_reference_models\reference_inventory.yaml` |
| `ELM19_Bw` | `ELM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\elm_reference_models\reference_inventory.yaml` |
| `rcim_original_SVM19_Fw` | `SVM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\svm_reference_models\reference_inventory.yaml` |
| `rcim_original_MLP19_Fw` | `MLP` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_original_RF19_Fw` | `RF` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\rf_reference_models\reference_inventory.yaml` |
| `rcim_original_DT19_Fw` | `DT` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\dt_reference_models\reference_inventory.yaml` |
| `rcim_original_ET19_Fw` | `ET` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\et_reference_models\reference_inventory.yaml` |
| `rcim_original_ERT19_Fw` | `ERT` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\ert_reference_models\reference_inventory.yaml` |
| `rcim_original_GBM19_Fw` | `GBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_original_HGBM19_Fw` | `HGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_XGBM19_Fw` | `XGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_LGBM19_Fw` | `LGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_ELM19_Fw` | `ELM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\elm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_SVM19_Fw` | `SVM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\svm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_MLP19_Fw` | `MLP` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_retuned_RF19_Fw` | `RF` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\rf_reference_models\reference_inventory.yaml` |
| `rcim_retuned_DT19_Fw` | `DT` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\dt_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ET19_Fw` | `ET` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\et_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ERT19_Fw` | `ERT` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\ert_reference_models\reference_inventory.yaml` |
| `rcim_retuned_GBM19_Fw` | `GBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_HGBM19_Fw` | `HGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_XGBM19_Fw` | `XGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_LGBM19_Fw` | `LGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ELM19_Fw` | `ELM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\elm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_SVM19_Bw` | `SVM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\svm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_MLP19_Bw` | `MLP` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_retuned_RF19_Bw` | `RF` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\rf_reference_models\reference_inventory.yaml` |
| `rcim_retuned_DT19_Bw` | `DT` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\dt_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ET19_Bw` | `ET` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\et_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ERT19_Bw` | `ERT` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\ert_reference_models\reference_inventory.yaml` |
| `rcim_retuned_GBM19_Bw` | `GBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_HGBM19_Bw` | `HGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_XGBM19_Bw` | `XGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_LGBM19_Bw` | `LGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ELM19_Bw` | `ELM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\elm_reference_models\reference_inventory.yaml` |
| `temporal_convolution_global` | `temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\temporal_convolution\latest_family_best.yaml` |
| `temporal_convolution_Fw` | `temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\temporal_convolution_fw\latest_family_best.yaml` |
| `temporal_convolution_Bw` | `temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\temporal_convolution_bw\latest_family_best.yaml` |
| `gru_sequence_global` | `gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\gru_sequence\latest_family_best.yaml` |
| `gru_sequence_Fw` | `gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\gru_sequence_fw\latest_family_best.yaml` |
| `gru_sequence_Bw` | `gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\gru_sequence_bw\latest_family_best.yaml` |
| `lstm_sequence_global` | `lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\lstm_sequence\latest_family_best.yaml` |
| `lstm_sequence_Fw` | `lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\lstm_sequence_fw\latest_family_best.yaml` |
| `lstm_sequence_Bw` | `lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\lstm_sequence_bw\latest_family_best.yaml` |
| `feedforward_global` | `feedforward` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\feedforward\global\python\feedforward-epoch=198-val_mae=0.00295772.ckpt` |
| `feedforward_Fw` | `feedforward` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\feedforward\forward\python\feedforward-epoch=086-val_mae=0.00274640.ckpt` |
| `feedforward_Bw` | `feedforward` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\feedforward\backward\python\feedforward-epoch=209-val_mae=0.00287506.ckpt` |
| `harmonic_regression_global` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\harmonic_regression\global\python\harmonic_regression-epoch=040-val_mae=0.01702522.ckpt` |
| `harmonic_regression_Fw` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\harmonic_regression\forward\python\harmonic_regression-epoch=043-val_mae=0.00284796.ckpt` |
| `harmonic_regression_Bw` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\harmonic_regression\backward\python\harmonic_regression-epoch=047-val_mae=0.00363757.ckpt` |
| `periodic_mlp_global` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\periodic_mlp\global\python\periodic_mlp-epoch=075-val_mae=0.00296443.ckpt` |
| `periodic_mlp_Fw` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\periodic_mlp\forward\python\periodic_mlp-epoch=023-val_mae=0.00275063.ckpt` |
| `periodic_mlp_Bw` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\periodic_mlp\backward\python\periodic_mlp-epoch=112-val_mae=0.00290718.ckpt` |
| `residual_harmonic_mlp_global` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\residual_harmonic_mlp\global\python\residual_harmonic_mlp-epoch=200-val_mae=0.00286835.ckpt` |
| `residual_harmonic_mlp_Fw` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\residual_harmonic_mlp\forward\python\residual_harmonic_mlp-epoch=018-val_mae=0.00275861.ckpt` |
| `residual_harmonic_mlp_Bw` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\residual_harmonic_mlp\backward\python\residual_harmonic_mlp-epoch=115-val_mae=0.00292969.ckpt` |
| `tree_global` | `tree` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\tree\global\python\tree_model.pkl` |
| `tree_Fw` | `tree` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\tree\forward\python\tree_model.pkl` |
| `tree_Bw` | `tree` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\tree\backward\python\tree_model.pkl` |
| `paper_original_best_Fw` | `best_composite` | `rcim_original` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward` |
| `paper_retuned_best_Fw` | `best_composite` | `rcim_retuned` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward` |
| `track1_best_Fw` | `best_composite` | `rcim_track1` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward` |
| `paper_retuned_best_Bw` | `best_composite` | `rcim_retuned` | `composite_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward` |
| `track1_best_Bw` | `best_composite` | `rcim_track1` | `composite_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward` |
| `periodic_temporal_convolution_global` | `periodic_temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\periodic_temporal_convolution\latest_family_best.yaml` |
| `periodic_temporal_convolution_Fw` | `periodic_temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\periodic_temporal_convolution_fw\latest_family_best.yaml` |
| `periodic_temporal_convolution_Bw` | `periodic_temporal_convolution` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\periodic_temporal_convolution_bw\latest_family_best.yaml` |
| `periodic_gru_sequence_global` | `periodic_gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\periodic_gru_sequence\latest_family_best.yaml` |
| `periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\periodic_gru_sequence_fw\latest_family_best.yaml` |
| `periodic_gru_sequence_Bw` | `periodic_gru_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\periodic_gru_sequence_bw\latest_family_best.yaml` |
| `periodic_lstm_sequence_global` | `periodic_lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\periodic_lstm_sequence\latest_family_best.yaml` |
| `periodic_lstm_sequence_Fw` | `periodic_lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\periodic_lstm_sequence_fw\latest_family_best.yaml` |
| `periodic_lstm_sequence_Bw` | `periodic_lstm_sequence` | `wave2_temporal_entry_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\periodic_lstm_sequence_bw\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `residual_harmonic_gru_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_gru_sequence_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `residual_harmonic_gru_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_gru_sequence_fw_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `residual_harmonic_gru_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_gru_sequence_bw_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_gru_sequence_dense240\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense240_Fw` | `residual_harmonic_gru_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_gru_sequence_fw_dense240\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense240_Bw` | `residual_harmonic_gru_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_gru_sequence_bw_dense240\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense360_global` | `residual_harmonic_gru_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_gru_sequence_dense360\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense360_Fw` | `residual_harmonic_gru_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_gru_sequence_fw_dense360\latest_family_best.yaml` |
| `residual_harmonic_gru_sequence_dense360_Bw` | `residual_harmonic_gru_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_gru_sequence_bw_dense360\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_lstm_sequence_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `residual_harmonic_lstm_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_lstm_sequence_fw_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `residual_harmonic_lstm_sequence_sparse_rcim` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_lstm_sequence_bw_sparse_rcim\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_lstm_sequence_dense240\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `residual_harmonic_lstm_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_lstm_sequence_fw_dense240\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `residual_harmonic_lstm_sequence_dense240` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_lstm_sequence_bw_dense240\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\residual_harmonic_lstm_sequence_dense360\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `residual_harmonic_lstm_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\residual_harmonic_lstm_sequence_fw_dense360\latest_family_best.yaml` |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `residual_harmonic_lstm_sequence_dense360` | `wave2c_residual_harmonic_temporal_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\residual_harmonic_lstm_sequence_bw_dense360\latest_family_best.yaml` |
| `sequential_residual_offset_probe_global` | `sequential_residual_offset_probe` | `track2f_offset_aware_probe_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\sequential_residual_offset_probe\latest_family_best.yaml` |
| `sequential_residual_offset_probe_Fw` | `sequential_residual_offset_probe` | `track2f_offset_aware_probe_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\sequential_residual_offset_probe_fw\latest_family_best.yaml` |
| `sequential_residual_offset_probe_Bw` | `sequential_residual_offset_probe` | `track2f_offset_aware_probe_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\sequential_residual_offset_probe_bw\latest_family_best.yaml` |
| `track2f_bis_clean_sequential_residual_offset_global` | `track2f_bis_clean_sequential_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2f_bis_clean_sequential_residual_offset_global\latest_family_best.yaml` |
| `track2f_bis_clean_sequential_residual_offset_Fw` | `track2f_bis_clean_sequential_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2f_bis_clean_sequential_residual_offset_fw\latest_family_best.yaml` |
| `track2f_bis_clean_sequential_residual_offset_Bw` | `track2f_bis_clean_sequential_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2f_bis_clean_sequential_residual_offset_bw\latest_family_best.yaml` |
| `track2f_bis_harmonic_residual_offset_global` | `track2f_bis_harmonic_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2f_bis_harmonic_residual_offset_global\latest_family_best.yaml` |
| `track2f_bis_harmonic_residual_offset_Fw` | `track2f_bis_harmonic_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2f_bis_harmonic_residual_offset_fw\latest_family_best.yaml` |
| `track2f_bis_harmonic_residual_offset_Bw` | `track2f_bis_harmonic_residual_offset` | `track2f_bis_harmonic_offset_probe_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2f_bis_harmonic_residual_offset_bw\latest_family_best.yaml` |
| `track2g_curve_aware_pointwise_control_global` | `track2g_curve_aware_pointwise_control` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_pointwise_control_global\latest_family_best.yaml` |
| `track2g_curve_aware_pointwise_control_Fw` | `track2g_curve_aware_pointwise_control` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw\latest_family_best.yaml` |
| `track2g_curve_aware_pointwise_control_Bw` | `track2g_curve_aware_pointwise_control` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw\latest_family_best.yaml` |
| `track2g_curve_aware_raw_centered_shape_global` | `track2g_curve_aware_raw_centered_shape` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global\latest_family_best.yaml` |
| `track2g_curve_aware_raw_centered_shape_Fw` | `track2g_curve_aware_raw_centered_shape` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\latest_family_best.yaml` |
| `track2g_curve_aware_raw_centered_shape_Bw` | `track2g_curve_aware_raw_centered_shape` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw\latest_family_best.yaml` |
| `track2g_curve_aware_raw_offset_global` | `track2g_curve_aware_raw_offset` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_offset_global\latest_family_best.yaml` |
| `track2g_curve_aware_raw_offset_Fw` | `track2g_curve_aware_raw_offset` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_offset_fw\latest_family_best.yaml` |
| `track2g_curve_aware_raw_offset_Bw` | `track2g_curve_aware_raw_offset` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_raw_offset_bw\latest_family_best.yaml` |
| `track2g_curve_aware_full_curve_composite_global` | `track2g_curve_aware_full_curve_composite` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global\latest_family_best.yaml` |
| `track2g_curve_aware_full_curve_composite_Fw` | `track2g_curve_aware_full_curve_composite` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw\latest_family_best.yaml` |
| `track2g_curve_aware_full_curve_composite_Bw` | `track2g_curve_aware_full_curve_composite` | `track2g_curve_aware_training_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw\latest_family_best.yaml` |
| `track2h_mae_robust_global` | `track2h_mae_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_dispersion_aware_mae_robust_global\latest_family_best.yaml` |
| `track2h_mae_robust_Fw` | `track2h_mae_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_dispersion_aware_mae_robust_fw\latest_family_best.yaml` |
| `track2h_mae_robust_Bw` | `track2h_mae_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_dispersion_aware_mae_robust_bw\latest_family_best.yaml` |
| `track2h_smooth_l1_robust_global` | `track2h_smooth_l1_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_dispersion_aware_smooth_l1_robust_global\latest_family_best.yaml` |
| `track2h_smooth_l1_robust_Fw` | `track2h_smooth_l1_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_dispersion_aware_smooth_l1_robust_fw\latest_family_best.yaml` |
| `track2h_smooth_l1_robust_Bw` | `track2h_smooth_l1_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_dispersion_aware_smooth_l1_robust_bw\latest_family_best.yaml` |
| `track2h_log_cosh_robust_global` | `track2h_log_cosh_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_dispersion_aware_log_cosh_robust_global\latest_family_best.yaml` |
| `track2h_log_cosh_robust_Fw` | `track2h_log_cosh_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_dispersion_aware_log_cosh_robust_fw\latest_family_best.yaml` |
| `track2h_log_cosh_robust_Bw` | `track2h_log_cosh_robust` | `track2h_dispersion_aware_modeling_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_dispersion_aware_log_cosh_robust_bw\latest_family_best.yaml` |
| `track2h_quantile_p10_p50_p90_global` | `track2h_quantile_p10_p50_p90` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_quantile_probabilistic_quantile_p10_p50_p90_global\latest_family_best.yaml` |
| `track2h_quantile_p10_p50_p90_Fw` | `track2h_quantile_p10_p50_p90` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_quantile_probabilistic_quantile_p10_p50_p90_fw\latest_family_best.yaml` |
| `track2h_quantile_p10_p50_p90_Bw` | `track2h_quantile_p10_p50_p90` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\latest_family_best.yaml` |
| `track2h_gaussian_nll_global` | `track2h_gaussian_nll` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_quantile_probabilistic_gaussian_nll_global\latest_family_best.yaml` |
| `track2h_gaussian_nll_Fw` | `track2h_gaussian_nll` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_quantile_probabilistic_gaussian_nll_fw\latest_family_best.yaml` |
| `track2h_gaussian_nll_Bw` | `track2h_gaussian_nll` | `track2h_quantile_probabilistic_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_quantile_probabilistic_gaussian_nll_bw\latest_family_best.yaml` |
| `track2h_mdn_k2_global` | `track2h_mdn_k2` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_mixture_density_heads_mdn_k2_global\latest_family_best.yaml` |
| `track2h_mdn_k2_Fw` | `track2h_mdn_k2` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_mixture_density_heads_mdn_k2_fw\latest_family_best.yaml` |
| `track2h_mdn_k2_Bw` | `track2h_mdn_k2` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_mixture_density_heads_mdn_k2_bw\latest_family_best.yaml` |
| `track2h_mdn_k3_global` | `track2h_mdn_k3` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_mixture_density_heads_mdn_k3_global\latest_family_best.yaml` |
| `track2h_mdn_k3_Fw` | `track2h_mdn_k3` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_mixture_density_heads_mdn_k3_fw\latest_family_best.yaml` |
| `track2h_mdn_k3_Bw` | `track2h_mdn_k3` | `track2h_mixture_density_heads_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_mixture_density_heads_mdn_k3_bw\latest_family_best.yaml` |
| `track2h_l_gru_offset_residual_global` | `track2h_l_gru_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_latent_state_hysteresis_gru_offset_residual_global\latest_family_best.yaml` |
| `track2h_l_gru_offset_residual_Fw` | `track2h_l_gru_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_latent_state_hysteresis_gru_offset_residual_fw\latest_family_best.yaml` |
| `track2h_l_gru_offset_residual_Bw` | `track2h_l_gru_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_latent_state_hysteresis_gru_offset_residual_bw\latest_family_best.yaml` |
| `track2h_l_causal_tcn_offset_residual_global` | `track2h_l_causal_tcn_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\track2h_latent_state_hysteresis_causal_tcn_offset_residual_global\latest_family_best.yaml` |
| `track2h_l_causal_tcn_offset_residual_Fw` | `track2h_l_causal_tcn_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw\latest_family_best.yaml` |
| `track2h_l_causal_tcn_offset_residual_Bw` | `track2h_l_causal_tcn_offset_residual` | `track2h_latent_state_hysteresis_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual_pointwise_control` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\wave3_harmonic_prior_residual_pointwise_control_global\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_pointwise_control_Fw` | `wave3_harmonic_prior_residual_pointwise_control` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\wave3_harmonic_prior_residual_pointwise_control_fw\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_pointwise_control_Bw` | `wave3_harmonic_prior_residual_pointwise_control` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\wave3_harmonic_prior_residual_pointwise_control_bw\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual_smooth_l1_structured` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\wave3_harmonic_prior_residual_smooth_l1_structured_global\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_Fw` | `wave3_harmonic_prior_residual_smooth_l1_structured` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\wave3_harmonic_prior_residual_smooth_l1_structured_fw\latest_family_best.yaml` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_Bw` | `wave3_harmonic_prior_residual_smooth_l1_structured` | `wave3_harmonic_prior_residual_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\wave3_harmonic_prior_residual_smooth_l1_structured_bw\latest_family_best.yaml` |
| `wave52b_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` | `wave52b_offset_harmonic_guided_registry` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global\latest_family_best.yaml` |
| `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided` | `wave52b_offset_harmonic_guided_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\latest_family_best.yaml` |
| `wave52b_offset_centered_shape_harmonic_Bw` | `wave52b_offset_harmonic_guided` | `wave52b_offset_harmonic_guided_registry` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw\latest_family_best.yaml` |

## Best Composite Reference Models

These candidates combine the approved best harmonic-wise cells into
one TE Curve Verification Pipeline curve-reconstruction candidate. They are also repeated
inside the source-group tables below, but this section keeps the
composed models explicit.

| Candidate | Source | Surface | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| `paper_original_best_Fw` | `rcim_original` | `Fw` | `forward` | 0.002769 | 0.002951 | 6.250 | 13.827 |
| `paper_retuned_best_Fw` | `rcim_retuned` | `Fw` | `forward` | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `track1_best_Fw` | `rcim_track1` | `Fw` | `forward` | 0.003014 | 0.003204 | 6.819 | 11.638 |
| `paper_retuned_best_Bw` | `rcim_retuned` | `Bw` | `backward` | 0.003675 | 0.004284 | 7.572 | 15.645 |
| `track1_best_Bw` | `rcim_track1` | `Bw` | `backward` | 0.005027 | 0.005212 | 11.860 | 48.106 |

## Forward Comparison

### Original Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_original_ERT19_Fw` | 0.001471 | 0.001677 | 3.253 | 6.145 |
| `rcim_original_RF19_Fw` | 0.001767 | 0.001971 | 3.940 | 6.872 |
| `rcim_original_LGBM19_Fw` | 0.001801 | 0.002004 | 4.017 | 10.054 |
| `rcim_original_DT19_Fw` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_original_GBM19_Fw` | 0.001921 | 0.002122 | 4.312 | 8.193 |
| `rcim_original_HGBM19_Fw` | 0.002011 | 0.002217 | 4.493 | 10.617 |
| `rcim_original_ET19_Fw` | 0.002232 | 0.002432 | 4.985 | 11.357 |
| `rcim_original_XGBM19_Fw` | 0.002594 | 0.002814 | 5.805 | 10.574 |
| `paper_original_best_Fw` | 0.002769 | 0.002951 | 6.250 | 13.827 |
| `rcim_original_SVM19_Fw` | 0.003052 | 0.003324 | 6.767 | 13.827 |
| `rcim_original_ELM19_Fw` | 0.005423 | 0.005731 | 12.130 | 28.721 |
| `rcim_original_MLP19_Fw` | 0.018754 | 0.022589 | 42.943 | 107.515 |

### Retuned Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| `rcim_retuned_RF19_Fw` | 0.001487 | 0.001699 | 3.292 | 5.998 |
| `rcim_retuned_ERT19_Fw` | 0.001807 | 0.002010 | 4.039 | 7.599 |
| `paper_retuned_best_Fw` | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `rcim_retuned_HGBM19_Fw` | 0.001851 | 0.002056 | 4.126 | 9.401 |
| `rcim_retuned_LGBM19_Fw` | 0.001851 | 0.002055 | 4.135 | 9.866 |
| `rcim_retuned_DT19_Fw` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_retuned_ET19_Fw` | 0.002001 | 0.002196 | 4.426 | 9.533 |
| `rcim_retuned_XGBM19_Fw` | 0.002054 | 0.002264 | 4.588 | 10.488 |
| `rcim_retuned_SVM19_Fw` | 0.003167 | 0.003428 | 7.035 | 12.971 |
| `rcim_retuned_ELM19_Fw` | 0.007182 | 0.007463 | 16.181 | 40.024 |
| `rcim_retuned_MLP19_Fw` | 0.016647 | 0.020154 | 38.510 | 86.197 |

### RCIM Model-Bank Reproduction Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `RF19_Fw` | 0.002164 | 0.002371 | 4.841 | 11.061 |
| `ERT19_Fw` | 0.002295 | 0.002491 | 5.163 | 13.141 |
| `GBM19_Fw` | 0.002779 | 0.002981 | 6.238 | 12.995 |
| `track1_best_Fw` | 0.003014 | 0.003204 | 6.819 | 11.638 |
| `DT19_Fw` | 0.003122 | 0.003313 | 7.011 | 13.928 |
| `SVM19_Fw` | 0.003236 | 0.003487 | 7.185 | 11.841 |
| `HGBM19_Fw` | 0.003251 | 0.003464 | 7.315 | 13.802 |
| `ET19_Fw` | 0.003267 | 0.003467 | 7.339 | 14.670 |
| `XGBM19_Fw` | 0.004190 | 0.004396 | 9.407 | 22.660 |
| `LGBM19_Fw` | 0.006812 | 0.007009 | 15.415 | 30.398 |
| `ELM19_Fw` | 0.007281 | 0.007573 | 16.352 | 36.326 |
| `MLP19_Fw` | 0.038690 | 0.047157 | 89.567 | 201.437 |

### Wave 1 Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `tree_Fw` | 0.003053 | 0.003395 | 6.731 | 11.995 |
| `periodic_mlp_Fw` | 0.003366 | 0.003794 | 7.467 | 12.904 |
| `periodic_mlp_global` | 0.003380 | 0.003791 | 7.493 | 14.349 |
| `harmonic_regression_Fw` | 0.003394 | 0.003807 | 7.534 | 11.391 |
| `residual_harmonic_mlp_Fw` | 0.003434 | 0.003876 | 7.618 | 13.617 |
| `feedforward_Fw` | 0.003466 | 0.003904 | 7.685 | 13.132 |
| `feedforward_global` | 0.003550 | 0.003979 | 7.916 | 16.195 |
| `residual_harmonic_mlp_global` | 0.003649 | 0.004051 | 8.123 | 14.713 |
| `harmonic_regression_global` | 0.018314 | 0.018547 | 41.749 | 79.404 |

### Wave 2.1 Temporal Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `periodic_lstm_sequence_global` | 0.002726 | 0.002959 | 6.142 | 14.092 |
| `periodic_gru_sequence_global` | 0.002777 | 0.003023 | 6.267 | 13.580 |
| `periodic_gru_sequence_Fw` | 0.003186 | 0.003438 | 7.077 | 11.974 |
| `periodic_lstm_sequence_Fw` | 0.003266 | 0.003550 | 7.258 | 11.961 |
| `gru_sequence_Fw` | 0.003330 | 0.003762 | 7.378 | 13.029 |
| `periodic_temporal_convolution_Fw` | 0.003335 | 0.003708 | 7.404 | 12.518 |
| `lstm_sequence_Fw` | 0.003366 | 0.003800 | 7.450 | 11.807 |
| `periodic_temporal_convolution_global` | 0.003407 | 0.003724 | 7.581 | 14.480 |
| `lstm_sequence_global` | 0.003445 | 0.003863 | 7.642 | 12.032 |
| `temporal_convolution_global` | 0.003508 | 0.003928 | 7.792 | 14.045 |
| `gru_sequence_global` | 0.003546 | 0.003975 | 7.869 | 14.344 |
| `temporal_convolution_Fw` | 0.003603 | 0.004031 | 8.028 | 14.674 |

### Wave 2.3 Residual Harmonic Temporal Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | 0.003194 | 0.003499 | 7.083 | 13.041 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | 0.003229 | 0.003533 | 7.164 | 12.682 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | 0.003245 | 0.003562 | 7.192 | 12.555 |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | 0.003287 | 0.003611 | 7.282 | 12.461 |
| `residual_harmonic_lstm_sequence_dense240_global` | 0.006247 | 0.008597 | 14.061 | 20.066 |
| `residual_harmonic_gru_sequence_dense240_global` | 0.006534 | 0.008959 | 14.732 | 20.898 |
| `residual_harmonic_gru_sequence_dense240_Fw` | 0.006983 | 0.009275 | 15.722 | 19.139 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | 0.007042 | 0.009370 | 15.868 | 19.358 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | 0.007731 | 0.010235 | 17.430 | 21.285 |
| `residual_harmonic_gru_sequence_dense360_global` | 0.007844 | 0.011211 | 17.679 | 22.520 |
| `residual_harmonic_gru_sequence_dense360_Fw` | 0.007869 | 0.010574 | 17.740 | 20.918 |
| `residual_harmonic_lstm_sequence_dense360_global` | 0.008760 | 0.012992 | 19.759 | 24.068 |

### Wave 3.1 Offset-Aware Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `sequential_residual_offset_probe_global` | 0.011772 | 0.013373 | 25.070 | 64.043 |
| `sequential_residual_offset_probe_Fw` | 0.036294 | 0.036467 | 77.932 | 160.083 |

### Wave 3.2 Harmonic-Offset Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2f_bis_clean_sequential_residual_offset_global` | 0.014946 | 0.015784 | 31.986 | 76.955 |
| `track2f_bis_harmonic_residual_offset_global` | 0.039482 | 0.039637 | 84.805 | 170.090 |
| `track2f_bis_clean_sequential_residual_offset_Fw` | 0.045185 | 0.045455 | 97.083 | 194.081 |
| `track2f_bis_harmonic_residual_offset_Fw` | 0.059869 | 0.059969 | 127.873 | 267.479 |

### Wave 3.3 Curve-Aware Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2g_curve_aware_full_curve_composite_global` | 0.001798 | 0.002176 | 3.621 | 8.564 |
| `track2g_curve_aware_raw_centered_shape_global` | 0.008354 | 0.008849 | 18.524 | 30.195 |
| `track2g_curve_aware_raw_offset_global` | 0.009768 | 0.010154 | 20.971 | 56.927 |
| `track2g_curve_aware_pointwise_control_global` | 0.015865 | 0.016241 | 34.752 | 79.981 |
| `track2g_curve_aware_raw_centered_shape_Fw` | 0.037030 | 0.037237 | 79.717 | 153.051 |
| `track2g_curve_aware_pointwise_control_Fw` | 0.044577 | 0.044713 | 95.253 | 186.415 |
| `track2g_curve_aware_full_curve_composite_Fw` | 0.050091 | 0.050255 | 107.778 | 216.693 |
| `track2g_curve_aware_raw_offset_Fw` | 0.058349 | 0.058552 | 124.991 | 247.137 |

### Wave 5.2 series Robust-Loss Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_log_cosh_robust_global` | 0.006651 | 0.007133 | 14.636 | 27.123 |
| `track2h_mae_robust_global` | 0.007132 | 0.007593 | 15.736 | 28.173 |
| `track2h_smooth_l1_robust_global` | 0.034438 | 0.034618 | 74.024 | 167.540 |
| `track2h_mae_robust_Fw` | 0.049061 | 0.049181 | 105.141 | 200.455 |
| `track2h_log_cosh_robust_Fw` | 0.054964 | 0.055089 | 117.915 | 225.075 |
| `track2h_smooth_l1_robust_Fw` | 0.058171 | 0.058283 | 124.441 | 247.002 |

### Wave 5.2 series Quantile Probabilistic Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_gaussian_nll_global` | 0.016491 | 0.016807 | 35.270 | 86.670 |
| `track2h_quantile_p10_p50_p90_global` | 0.034013 | 0.034165 | 72.887 | 153.467 |
| `track2h_quantile_p10_p50_p90_Fw` | 0.050281 | 0.050425 | 107.720 | 203.214 |
| `track2h_gaussian_nll_Fw` | 0.054985 | 0.055109 | 117.675 | 233.102 |

### Wave 5.2 series Mixture Density Heads Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_mdn_k3_global` | 0.008047 | 0.008537 | 17.449 | 50.984 |
| `track2h_mdn_k2_global` | 0.014253 | 0.014687 | 30.002 | 96.021 |
| `track2h_mdn_k2_Fw` | 0.047438 | 0.047677 | 102.227 | 196.592 |
| `track2h_mdn_k3_Fw` | 0.057840 | 0.057965 | 124.009 | 250.657 |

### Wave 4.4 Latent-State Hysteresis Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_l_gru_offset_residual_global` | 0.002172 | 0.002635 | 4.462 | 8.584 |
| `track2h_l_causal_tcn_offset_residual_global` | 0.021679 | 0.022716 | 46.237 | 109.161 |
| `track2h_l_gru_offset_residual_Fw` | 0.024419 | 0.025009 | 52.319 | 115.442 |
| `track2h_l_causal_tcn_offset_residual_Fw` | 0.028476 | 0.028960 | 61.107 | 131.014 |

### Wave 5.2B Offset And Harmonic Guided Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | 0.001695 | 0.002045 | 3.391 | 8.270 |
| `wave52b_offset_centered_shape_harmonic_global` | 0.001929 | 0.002295 | 3.959 | 9.602 |

## Backward Comparison

### Retuned Backward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Bw` | 0.002766 | 0.003300 | 5.398 | 12.280 |
| `rcim_retuned_ET19_Bw` | 0.003441 | 0.004028 | 7.021 | 15.287 |
| `rcim_retuned_ERT19_Bw` | 0.003551 | 0.004161 | 7.269 | 13.187 |
| `rcim_retuned_RF19_Bw` | 0.003649 | 0.004256 | 7.543 | 15.083 |
| `paper_retuned_best_Bw` | 0.003675 | 0.004284 | 7.572 | 15.645 |
| `rcim_retuned_SVM19_Bw` | 0.004016 | 0.004599 | 8.813 | 17.215 |
| `rcim_retuned_DT19_Bw` | 0.004578 | 0.005169 | 9.728 | 19.601 |
| `rcim_retuned_HGBM19_Bw` | 0.004683 | 0.005301 | 9.978 | 17.712 |
| `rcim_retuned_LGBM19_Bw` | 0.008105 | 0.008655 | 18.057 | 35.748 |
| `rcim_retuned_ELM19_Bw` | 0.008917 | 0.009518 | 20.169 | 51.896 |
| `rcim_retuned_XGBM19_Bw` | 0.010679 | 0.011209 | 24.184 | 48.082 |
| `rcim_retuned_MLP19_Bw` | 0.019115 | 0.023025 | 44.141 | 88.991 |

### RCIM Model-Bank Reproduction Backward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `SVM19_Bw` | 0.004822 | 0.005116 | 10.864 | 25.533 |
| `track1_best_Bw` | 0.005027 | 0.005212 | 11.860 | 48.106 |
| `LGBM19_Bw` | 0.005037 | 0.005231 | 11.880 | 48.106 |
| `GBM19_Bw` | 0.005180 | 0.005363 | 12.252 | 49.984 |
| `DT19_Bw` | 0.005226 | 0.005409 | 12.359 | 48.860 |
| `ERT19_Bw` | 0.005258 | 0.005442 | 12.434 | 51.665 |
| `RF19_Bw` | 0.005392 | 0.005584 | 12.731 | 55.740 |
| `ET19_Bw` | 0.006273 | 0.006520 | 14.314 | 48.624 |
| `HGBM19_Bw` | 0.006619 | 0.006834 | 15.494 | 53.982 |
| `XGBM19_Bw` | 0.007991 | 0.008195 | 18.722 | 59.067 |
| `ELM19_Bw` | 0.010071 | 0.010486 | 23.034 | 52.159 |
| `MLP19_Bw` | 0.036681 | 0.044921 | 86.544 | 225.831 |

### Wave 1 Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `tree_global` | 0.003290 | 0.003702 | 7.118 | 13.703 |
| `periodic_mlp_Bw` | 0.003574 | 0.004006 | 7.807 | 13.970 |
| `periodic_mlp_global` | 0.003610 | 0.004030 | 7.879 | 13.661 |
| `residual_harmonic_mlp_global` | 0.003639 | 0.004044 | 7.967 | 14.489 |
| `feedforward_Bw` | 0.003644 | 0.004067 | 7.977 | 14.284 |
| `residual_harmonic_mlp_Bw` | 0.003672 | 0.004089 | 8.046 | 14.973 |
| `harmonic_regression_Bw` | 0.003745 | 0.004173 | 8.171 | 15.684 |
| `feedforward_global` | 0.003741 | 0.004188 | 8.186 | 15.259 |
| `harmonic_regression_global` | 0.018006 | 0.018276 | 41.275 | 83.603 |

### Wave 2.1 Temporal Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| `periodic_gru_sequence_global` | 0.002630 | 0.002876 | 6.010 | 12.693 |
| `periodic_lstm_sequence_Bw` | 0.002625 | 0.002877 | 6.013 | 15.382 |
| `periodic_lstm_sequence_global` | 0.002689 | 0.002956 | 6.098 | 14.674 |
| `lstm_sequence_global` | 0.003515 | 0.003944 | 7.666 | 12.502 |
| `lstm_sequence_Bw` | 0.003555 | 0.003985 | 7.767 | 14.507 |
| `gru_sequence_Bw` | 0.003626 | 0.004082 | 7.907 | 12.900 |
| `periodic_temporal_convolution_global` | 0.003604 | 0.003948 | 7.935 | 13.804 |
| `gru_sequence_global` | 0.003637 | 0.004080 | 7.946 | 14.580 |
| `periodic_temporal_convolution_Bw` | 0.003628 | 0.003987 | 7.979 | 13.839 |
| `temporal_convolution_Bw` | 0.003742 | 0.004166 | 8.184 | 13.908 |
| `temporal_convolution_global` | 0.003994 | 0.004438 | 8.798 | 18.339 |

### Wave 2.3 Residual Harmonic Temporal Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | 0.003440 | 0.003793 | 7.510 | 13.160 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | 0.003491 | 0.003876 | 7.627 | 13.540 |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | 0.003502 | 0.003857 | 7.654 | 12.829 |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | 0.003584 | 0.003957 | 7.859 | 14.946 |
| `residual_harmonic_lstm_sequence_dense240_global` | 0.006591 | 0.008932 | 14.858 | 21.728 |
| `residual_harmonic_gru_sequence_dense240_global` | 0.006786 | 0.009221 | 15.282 | 20.990 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | 0.007367 | 0.009945 | 16.660 | 22.200 |
| `residual_harmonic_gru_sequence_dense360_global` | 0.008181 | 0.011621 | 18.502 | 23.968 |
| `residual_harmonic_lstm_sequence_dense360_global` | 0.008860 | 0.013061 | 20.073 | 23.940 |
| `residual_harmonic_gru_sequence_dense240_Bw` | 0.008984 | 0.012987 | 20.358 | 26.370 |
| `residual_harmonic_gru_sequence_dense360_Bw` | 0.009370 | 0.013165 | 21.267 | 25.901 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | 0.010268 | 0.014769 | 23.355 | 29.779 |

### Wave 3.1 Offset-Aware Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `sequential_residual_offset_probe_global` | 0.008806 | 0.009398 | 18.279 | 32.785 |
| `sequential_residual_offset_probe_Bw` | 0.008945 | 0.009670 | 18.730 | 35.533 |

### Wave 3.2 Harmonic-Offset Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2f_bis_clean_sequential_residual_offset_global` | 0.006660 | 0.007243 | 13.756 | 24.509 |
| `track2f_bis_harmonic_residual_offset_global` | 0.008474 | 0.008976 | 17.214 | 35.408 |
| `track2f_bis_clean_sequential_residual_offset_Bw` | 0.008376 | 0.009258 | 17.556 | 34.867 |
| `track2f_bis_harmonic_residual_offset_Bw` | 0.012996 | 0.013533 | 26.826 | 42.348 |

### Wave 3.3 Curve-Aware Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2g_curve_aware_full_curve_composite_global` | 0.002258 | 0.002737 | 4.040 | 10.132 |
| `track2g_curve_aware_raw_offset_global` | 0.009653 | 0.010130 | 20.050 | 31.531 |
| `track2g_curve_aware_pointwise_control_Bw` | 0.009939 | 0.010532 | 20.584 | 36.212 |
| `track2g_curve_aware_raw_centered_shape_Bw` | 0.010075 | 0.010673 | 20.657 | 35.422 |
| `track2g_curve_aware_raw_offset_Bw` | 0.011255 | 0.011824 | 23.166 | 39.304 |
| `track2g_curve_aware_raw_centered_shape_global` | 0.011137 | 0.011575 | 23.462 | 35.847 |
| `track2g_curve_aware_full_curve_composite_Bw` | 0.012620 | 0.013521 | 25.713 | 50.158 |
| `track2g_curve_aware_pointwise_control_global` | 0.013358 | 0.013773 | 27.446 | 48.301 |

### Wave 5.2 series Robust-Loss Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_log_cosh_robust_Bw` | 0.009813 | 0.010421 | 19.966 | 37.983 |
| `track2h_log_cosh_robust_global` | 0.011005 | 0.011437 | 23.172 | 35.371 |
| `track2h_smooth_l1_robust_Bw` | 0.012012 | 0.012561 | 24.411 | 45.374 |
| `track2h_mae_robust_global` | 0.012719 | 0.013122 | 26.537 | 43.911 |
| `track2h_mae_robust_Bw` | 0.014320 | 0.014747 | 30.084 | 52.809 |
| `track2h_smooth_l1_robust_global` | 0.014760 | 0.015146 | 30.600 | 49.591 |

### Wave 5.2 series Quantile Probabilistic Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_gaussian_nll_global` | 0.009465 | 0.009894 | 19.945 | 35.904 |
| `track2h_gaussian_nll_Bw` | 0.009739 | 0.010201 | 20.349 | 31.207 |
| `track2h_quantile_p10_p50_p90_Bw` | 0.011462 | 0.011942 | 23.503 | 44.253 |
| `track2h_quantile_p10_p50_p90_global` | 0.011361 | 0.011796 | 23.554 | 42.592 |

### Wave 5.2 series Mixture Density Heads Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_mdn_k2_Bw` | 0.008282 | 0.010642 | 16.490 | 31.064 |
| `track2h_mdn_k3_Bw` | 0.011511 | 0.011910 | 23.777 | 40.269 |
| `track2h_mdn_k2_global` | 0.011621 | 0.012094 | 24.024 | 46.001 |
| `track2h_mdn_k3_global` | 0.016585 | 0.016922 | 34.616 | 54.718 |

### Wave 4.4 Latent-State Hysteresis Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `track2h_l_gru_offset_residual_global` | 0.002532 | 0.003071 | 4.689 | 10.217 |
| `track2h_l_causal_tcn_offset_residual_Bw` | 0.007773 | 0.008896 | 15.746 | 25.965 |
| `track2h_l_gru_offset_residual_Bw` | 0.016484 | 0.016958 | 34.591 | 59.748 |
| `track2h_l_causal_tcn_offset_residual_global` | 0.021480 | 0.023284 | 46.491 | 83.800 |

### Wave 5.2B Offset And Harmonic Guided Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Bw` | 0.002266 | 0.002708 | 3.986 | 9.758 |
| `wave52b_offset_centered_shape_harmonic_global` | 0.002533 | 0.002985 | 4.422 | 10.180 |

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `feedforward_global` | `forward` | 0.003550 | 0.003979 | 7.916 | 16.195 |
| `feedforward_global` | `backward` | 0.003741 | 0.004188 | 8.186 | 15.259 |
| `feedforward_global` | `combined` | 0.003646 | 0.004083 | 8.051 | 15.583 |
| `gru_sequence_global` | `forward` | 0.003546 | 0.003975 | 7.869 | 14.344 |
| `gru_sequence_global` | `backward` | 0.003637 | 0.004080 | 7.946 | 14.580 |
| `gru_sequence_global` | `combined` | 0.003591 | 0.004028 | 7.907 | 14.389 |
| `harmonic_regression_global` | `forward` | 0.018314 | 0.018547 | 41.749 | 79.404 |
| `harmonic_regression_global` | `backward` | 0.018006 | 0.018276 | 41.275 | 83.603 |
| `harmonic_regression_global` | `combined` | 0.018160 | 0.018412 | 41.512 | 82.048 |
| `lstm_sequence_global` | `forward` | 0.003445 | 0.003863 | 7.642 | 12.032 |
| `lstm_sequence_global` | `backward` | 0.003515 | 0.003944 | 7.666 | 12.502 |
| `lstm_sequence_global` | `combined` | 0.003480 | 0.003903 | 7.654 | 12.430 |
| `periodic_gru_sequence_global` | `forward` | 0.002777 | 0.003023 | 6.267 | 13.580 |
| `periodic_gru_sequence_global` | `backward` | 0.002630 | 0.002876 | 6.010 | 12.693 |
| `periodic_gru_sequence_global` | `combined` | 0.002704 | 0.002949 | 6.139 | 13.200 |
| `periodic_lstm_sequence_global` | `forward` | 0.002726 | 0.002959 | 6.142 | 14.092 |
| `periodic_lstm_sequence_global` | `backward` | 0.002689 | 0.002956 | 6.098 | 14.674 |
| `periodic_lstm_sequence_global` | `combined` | 0.002707 | 0.002958 | 6.120 | 14.717 |
| `periodic_mlp_global` | `forward` | 0.003380 | 0.003791 | 7.493 | 14.349 |
| `periodic_mlp_global` | `backward` | 0.003610 | 0.004030 | 7.879 | 13.661 |
| `periodic_mlp_global` | `combined` | 0.003495 | 0.003910 | 7.686 | 14.284 |
| `periodic_temporal_convolution_global` | `forward` | 0.003407 | 0.003724 | 7.581 | 14.480 |
| `periodic_temporal_convolution_global` | `backward` | 0.003604 | 0.003948 | 7.935 | 13.804 |
| `periodic_temporal_convolution_global` | `combined` | 0.003506 | 0.003836 | 7.758 | 14.308 |
| `residual_harmonic_gru_sequence_dense240_global` | `forward` | 0.006534 | 0.008959 | 14.732 | 20.898 |
| `residual_harmonic_gru_sequence_dense240_global` | `backward` | 0.006786 | 0.009221 | 15.282 | 20.990 |
| `residual_harmonic_gru_sequence_dense240_global` | `combined` | 0.006660 | 0.009090 | 15.007 | 20.940 |
| `residual_harmonic_gru_sequence_dense360_global` | `forward` | 0.007844 | 0.011211 | 17.679 | 22.520 |
| `residual_harmonic_gru_sequence_dense360_global` | `backward` | 0.008181 | 0.011621 | 18.502 | 23.968 |
| `residual_harmonic_gru_sequence_dense360_global` | `combined` | 0.008012 | 0.011416 | 18.090 | 23.559 |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `forward` | 0.003287 | 0.003611 | 7.282 | 12.461 |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `backward` | 0.003584 | 0.003957 | 7.859 | 14.946 |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `combined` | 0.003435 | 0.003784 | 7.571 | 13.869 |
| `residual_harmonic_lstm_sequence_dense240_global` | `forward` | 0.006247 | 0.008597 | 14.061 | 20.066 |
| `residual_harmonic_lstm_sequence_dense240_global` | `backward` | 0.006591 | 0.008932 | 14.858 | 21.728 |
| `residual_harmonic_lstm_sequence_dense240_global` | `combined` | 0.006419 | 0.008765 | 14.460 | 20.628 |
| `residual_harmonic_lstm_sequence_dense360_global` | `forward` | 0.008760 | 0.012992 | 19.759 | 24.068 |
| `residual_harmonic_lstm_sequence_dense360_global` | `backward` | 0.008860 | 0.013061 | 20.073 | 23.940 |
| `residual_harmonic_lstm_sequence_dense360_global` | `combined` | 0.008810 | 0.013026 | 19.916 | 24.052 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `forward` | 0.003245 | 0.003562 | 7.192 | 12.555 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `backward` | 0.003491 | 0.003876 | 7.627 | 13.540 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `combined` | 0.003368 | 0.003719 | 7.409 | 13.041 |
| `residual_harmonic_mlp_global` | `forward` | 0.003649 | 0.004051 | 8.123 | 14.713 |
| `residual_harmonic_mlp_global` | `backward` | 0.003639 | 0.004044 | 7.967 | 14.489 |
| `residual_harmonic_mlp_global` | `combined` | 0.003644 | 0.004048 | 8.045 | 14.717 |
| `sequential_residual_offset_probe_global` | `forward` | 0.011772 | 0.013373 | 25.070 | 64.043 |
| `sequential_residual_offset_probe_global` | `backward` | 0.008806 | 0.009398 | 18.279 | 32.785 |
| `sequential_residual_offset_probe_global` | `combined` | 0.010335 | 0.011447 | 21.780 | 54.389 |
| `temporal_convolution_global` | `forward` | 0.003508 | 0.003928 | 7.792 | 14.045 |
| `temporal_convolution_global` | `backward` | 0.003994 | 0.004438 | 8.798 | 18.339 |
| `temporal_convolution_global` | `combined` | 0.003751 | 0.004183 | 8.295 | 17.247 |
| `track2f_bis_clean_sequential_residual_offset_global` | `forward` | 0.014946 | 0.015784 | 31.986 | 76.955 |
| `track2f_bis_clean_sequential_residual_offset_global` | `backward` | 0.006660 | 0.007243 | 13.756 | 24.509 |
| `track2f_bis_clean_sequential_residual_offset_global` | `combined` | 0.010931 | 0.011645 | 23.153 | 66.991 |
| `track2f_bis_harmonic_residual_offset_global` | `forward` | 0.039482 | 0.039637 | 84.805 | 170.090 |
| `track2f_bis_harmonic_residual_offset_global` | `backward` | 0.008474 | 0.008976 | 17.214 | 35.408 |
| `track2f_bis_harmonic_residual_offset_global` | `combined` | 0.024458 | 0.024780 | 52.055 | 157.788 |
| `track2g_curve_aware_full_curve_composite_global` | `forward` | 0.001798 | 0.002176 | 3.621 | 8.564 |
| `track2g_curve_aware_full_curve_composite_global` | `backward` | 0.002258 | 0.002737 | 4.040 | 10.132 |
| `track2g_curve_aware_full_curve_composite_global` | `combined` | 0.002021 | 0.002448 | 3.824 | 9.460 |
| `track2g_curve_aware_pointwise_control_global` | `forward` | 0.015865 | 0.016241 | 34.752 | 79.981 |
| `track2g_curve_aware_pointwise_control_global` | `backward` | 0.013358 | 0.013773 | 27.446 | 48.301 |
| `track2g_curve_aware_pointwise_control_global` | `combined` | 0.014650 | 0.015045 | 31.212 | 69.019 |
| `track2g_curve_aware_raw_centered_shape_global` | `forward` | 0.008354 | 0.008849 | 18.524 | 30.195 |
| `track2g_curve_aware_raw_centered_shape_global` | `backward` | 0.011137 | 0.011575 | 23.462 | 35.847 |
| `track2g_curve_aware_raw_centered_shape_global` | `combined` | 0.009702 | 0.010170 | 20.917 | 33.589 |
| `track2g_curve_aware_raw_offset_global` | `forward` | 0.009768 | 0.010154 | 20.971 | 56.927 |
| `track2g_curve_aware_raw_offset_global` | `backward` | 0.009653 | 0.010130 | 20.050 | 31.531 |
| `track2g_curve_aware_raw_offset_global` | `combined` | 0.009712 | 0.010143 | 20.524 | 49.082 |
| `track2h_gaussian_nll_global` | `forward` | 0.016491 | 0.016807 | 35.270 | 86.670 |
| `track2h_gaussian_nll_global` | `backward` | 0.009465 | 0.009894 | 19.945 | 35.904 |
| `track2h_gaussian_nll_global` | `combined` | 0.013087 | 0.013458 | 27.845 | 77.071 |
| `track2h_l_causal_tcn_offset_residual_global` | `forward` | 0.021679 | 0.022716 | 46.237 | 109.161 |
| `track2h_l_causal_tcn_offset_residual_global` | `backward` | 0.021480 | 0.023284 | 46.491 | 83.800 |
| `track2h_l_causal_tcn_offset_residual_global` | `combined` | 0.021583 | 0.022991 | 46.360 | 97.912 |
| `track2h_l_gru_offset_residual_global` | `forward` | 0.002172 | 0.002635 | 4.462 | 8.584 |
| `track2h_l_gru_offset_residual_global` | `backward` | 0.002532 | 0.003071 | 4.689 | 10.217 |
| `track2h_l_gru_offset_residual_global` | `combined` | 0.002346 | 0.002846 | 4.572 | 9.808 |
| `track2h_log_cosh_robust_global` | `forward` | 0.006651 | 0.007133 | 14.636 | 27.123 |
| `track2h_log_cosh_robust_global` | `backward` | 0.011005 | 0.011437 | 23.172 | 35.371 |
| `track2h_log_cosh_robust_global` | `combined` | 0.008761 | 0.009218 | 18.772 | 32.617 |
| `track2h_mae_robust_global` | `forward` | 0.007132 | 0.007593 | 15.736 | 28.173 |
| `track2h_mae_robust_global` | `backward` | 0.012719 | 0.013122 | 26.537 | 43.911 |
| `track2h_mae_robust_global` | `combined` | 0.009839 | 0.010272 | 20.969 | 37.437 |
| `track2h_mdn_k2_global` | `forward` | 0.014253 | 0.014687 | 30.002 | 96.021 |
| `track2h_mdn_k2_global` | `backward` | 0.011621 | 0.012094 | 24.024 | 46.001 |
| `track2h_mdn_k2_global` | `combined` | 0.012978 | 0.013430 | 27.105 | 80.630 |
| `track2h_mdn_k3_global` | `forward` | 0.008047 | 0.008537 | 17.449 | 50.984 |
| `track2h_mdn_k3_global` | `backward` | 0.016585 | 0.016922 | 34.616 | 54.718 |
| `track2h_mdn_k3_global` | `combined` | 0.012184 | 0.012600 | 25.767 | 54.085 |
| `track2h_quantile_p10_p50_p90_global` | `forward` | 0.034013 | 0.034165 | 72.887 | 153.467 |
| `track2h_quantile_p10_p50_p90_global` | `backward` | 0.011361 | 0.011796 | 23.554 | 42.592 |
| `track2h_quantile_p10_p50_p90_global` | `combined` | 0.023037 | 0.023327 | 48.983 | 142.345 |
| `track2h_smooth_l1_robust_global` | `forward` | 0.034438 | 0.034618 | 74.024 | 167.540 |
| `track2h_smooth_l1_robust_global` | `backward` | 0.014760 | 0.015146 | 30.600 | 49.591 |
| `track2h_smooth_l1_robust_global` | `combined` | 0.024904 | 0.025183 | 52.984 | 152.879 |
| `tree_global` | `forward` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `tree_global` | `backward` | 0.003290 | 0.003702 | 7.118 | 13.703 |
| `tree_global` | `combined` | 0.003144 | 0.003533 | 6.854 | 13.314 |
| `wave3_harmonic_prior_residual_pointwise_control_global` | `forward` | 0.004833 | 0.005371 | 10.455 | 20.017 |
| `wave3_harmonic_prior_residual_pointwise_control_global` | `backward` | 0.009539 | 0.010032 | 19.825 | 33.810 |
| `wave3_harmonic_prior_residual_pointwise_control_global` | `combined` | 0.007113 | 0.007629 | 14.995 | 31.569 |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `forward` | 0.001769 | 0.002131 | 3.577 | 8.089 |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `backward` | 0.002581 | 0.003040 | 4.545 | 9.839 |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `combined` | 0.002163 | 0.002571 | 4.046 | 9.635 |
| `wave52b_offset_centered_shape_harmonic_global` | `forward` | 0.001929 | 0.002295 | 3.959 | 9.602 |
| `wave52b_offset_centered_shape_harmonic_global` | `backward` | 0.002533 | 0.002985 | 4.422 | 10.180 |
| `wave52b_offset_centered_shape_harmonic_global` | `combined` | 0.002221 | 0.002629 | 4.184 | 9.818 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-02-12-43-56__track2_full_directional_family_matrix_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-02-12-43-56__track2_full_directional_family_matrix_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots`;
- grouped report plot count: `0`;

## Interpretation

Rows are ranked by mean percentage error within each source group
and direction. Directional paper-reference, Wave 1, and Wave 2.1
models are never evaluated on the opposite direction. Global Wave
models remain valid on both directions and are therefore shown in
the directional sections and again in the global breakdown.
The `rcim_track1` forward reference banks use the opposite stored
`h0` sign convention relative to the TE Curve Verification Pipeline reconstruction
contract, so the TE Curve Verification Pipeline comparison applies the documented
source-specific `h0` compatibility multiplier before curve
reconstruction.

## Open Gaps

- This remains an offline TE-curve comparison and does not replace the
  future online `Table 9` compensation benchmark.
- The report uses the saved Python model artifacts from `models/`; ONNX
  parity checks remain a separate deployment-readiness task.
