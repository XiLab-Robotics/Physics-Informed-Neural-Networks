# Project Documentation Index

This folder contains the internal project documents derived from the reference PDFs and from the reference codebases used to define the coding style of this repository.

## Available Documents

### Reference Summaries

- [reference_summaries/01_Dataset_Operations_Guide.md](./reference_summaries/01_Dataset_Operations_Guide.md)
  Dataset sources, practical references, and operational guidance.
- [reference_summaries/02_MMT_TEModeling_Project_Summary.md](./reference_summaries/02_MMT_TEModeling_Project_Summary.md)
  Analytical TE modeling through equivalent mechanism and loop incremental method.
- [reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md](./reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md)
  ML-driven TE prediction and online PLC/TwinCAT compensation strategy.
- [reference_summaries/04_Machine_Learning_Report_Project_Summary.md](./reference_summaries/04_Machine_Learning_Report_Project_Summary.md)
  Test-rig workflow, harmonic analysis, TwinCAT integration, and practical implementation notes.
- [reference_summaries/05_Data_Series_Explanation_Project_Summary.md](./reference_summaries/05_Data_Series_Explanation_Project_Summary.md)
  Meaning of the measured variables, zeroing procedure, and `DataValid` logic.
- [reference_summaries/06_Programming_Style_Guide.md](./reference_summaries/06_Programming_Style_Guide.md)
  Coding style mapped from `blind_handover_controller`, `mediapipe_gesture_recognition`, and `multimodal_fusion`.
- [reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md](./reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md)
  Summary of the recovered RCIM paper-era ONNX models, code snapshots, backup
  material, TwinCAT XML exports, and heavy instance archive, with repository
  implications for Track 1 and future deployment work.

### Reference Asset Roots

- [../reference/README.md](../reference/README.md)
  Global index of the repository reference surface, including PDFs, imported
  reference codebases, and recovered paper-owned assets.
- [../reference/rcim_ml_compensation_recovered_assets/README.md](../reference/rcim_ml_compensation_recovered_assets/README.md)
  Canonical index of the recovered RCIM paper asset package, including exact
  ONNX models, original and later code snapshots, backup material, TwinCAT XML
  exports, and the archived `instance_v1` subtree.

### Reference Code Notes

- [reference_codes/README.md](./reference_codes/README.md)
  Index of detailed notes extracted from the reference-code submodules.
- [reference_codes/blind_handover_controller_reference.md](./reference_codes/blind_handover_controller_reference.md)
  Main style baseline for naming, comments, structure, utilities, and Lightning training flow.
- [reference_codes/mediapipe_gesture_recognition_reference.md](./reference_codes/mediapipe_gesture_recognition_reference.md)
  Supporting reference for Hydra-based configuration and ML training utilities.
- [reference_codes/multimodal_fusion_reference.md](./reference_codes/multimodal_fusion_reference.md)
  Supporting reference for compact ROS pipelines, explicit label mapping, and simple Lightning baselines.

### Tooling Notes

- [scripts/tooling/README.md](./scripts/tooling/README.md)
  Index of repository-owned tooling notes grouped by domain.
- [scripts/tooling/lan_ai/lan_ai_node_server.md](./scripts/tooling/lan_ai/lan_ai_node_server.md)
  Setup and runtime guide for the remote LAN AI workstation.
- [scripts/tooling/video_guides/remote_high_quality_video_pipeline.md](./scripts/tooling/video_guides/remote_high_quality_video_pipeline.md)
  Canonical process note for the validated high-quality TwinCAT/TestRig video pipeline.

### Analysis Reports

- [reports/analysis/RCIM Exact Paper Model Bank Workflow.md](./reports/analysis/RCIM%20Exact%20Paper%20Model%20Bank%20Workflow.md)
  Explanatory report for the strict paper-faithful RCIM family-bank branch,
  including the exact target schema, recovered family inventory, operating
  principle, Python structure, and relationship with the older repository-owned
  harmonic-wise branch.
- [reports/analysis/RCIM Recovered Asset Deep Analysis.md](./reports/analysis/RCIM%20Recovered%20Asset%20Deep%20Analysis.md)
  Deep implementation-facing analysis of the recovered RCIM paper assets,
  including the exact ONNX family bank, original and later code generations,
  backup evolution, TwinCAT export evidence, archive limitations, and the
  exact consequences for faithful `Track 1` reimplementation.
- [reports/analysis/RCIM Paper Reference Benchmark.md](./reports/analysis/RCIM%20Paper%20Reference%20Benchmark.md)
  Canonical repository-owned extraction of the RCIM ML-compensation paper baseline, including minimum targets, paper-vs-repository status, and the missing pipeline for a true Table 9 comparison.
- [reports/analysis/Training Results Master Summary.md](./reports/analysis/Training%20Results%20Master%20Summary.md)
  Canonical always-updated summary of current project status, best family results, recent campaign changes, and family-by-family ranked outcomes across the TE training program.
- [reports/analysis/Wave 1 - Closeout Status.md](./reports/analysis/Wave%201%20-%20Closeout%20Status.md)
  Consolidated closeout report for `Wave 1`, covering campaign completion status, compared families, family winners, and final ranking.
- [reports/analysis/Skill and Subagent Operational Test.md](./reports/analysis/Skill%20and%20Subagent%20Operational%20Test.md)
  Operational test report for the second wave of repository-owned Codex skills and subagents.
- [reports/analysis/Twincat-Friendly Structured TE Modeling.md](./reports/analysis/Twincat-Friendly%20Structured%20TE%20Modeling.md)
  Reference-backed synthesis of TwinCAT-friendly structured TE modeling implications for the current repository direction.
- [reports/analysis/Code Documentation Platform Comparison.md](./reports/analysis/Code%20Documentation%20Platform%20Comparison.md)
  Comparative analysis of repository documentation-platform options in the readable-filename analysis-report layout.
- [reports/analysis/Local LAN AI Infrastructure Options for Video Knowledge Extraction.md](./reports/analysis/Local%20LAN%20AI%20Infrastructure%20Options%20for%20Video%20Knowledge%20Extraction.md)
  Comparative architecture report for local and LAN-accessible transcript, OCR, and LLM infrastructure for the TwinCAT/TestRig video workflow.
- [reports/analysis/twincat_video_guides/[2026-04-02]/remote_high_quality_video_campaign_sum_up.md](./reports/analysis/twincat_video_guides/%5B2026-04-02%5D/remote_high_quality_video_campaign_sum_up.md)
  Technical sum-up of the completed remote-strong `large-v3` plus `openai/gpt-oss-20b` video campaign across the 11 canonical TwinCAT/TestRig videos.

### Technical Documents

#### 2026-04-20

- [technical/2026-04/2026-04-20/2026-04-20-12-44-46_wave1_dataset_split_export_script.md](./technical/2026-04/2026-04-20/2026-04-20-12-44-46_wave1_dataset_split_export_script.md)
  Technical document for exporting the canonical `Wave 1` dataset split so a
  colleague can reproduce the same `70/20/10` partition with the repository
  seed and randomization logic.
- [technical/2026-04/2026-04-20/2026-04-20-12-57-55_dataset_split_export_script_rename.md](./technical/2026-04/2026-04-20/2026-04-20-12-57-55_dataset_split_export_script_rename.md)
  Technical document for renaming the dataset split export helper to a generic
  script name and aligning the local README references with that rename.

#### 2026-04-19

- [technical/2026-04/2026-04-19/2026-04-19-00-25-58_track1_remaining_family_cellwise_final_closeout.md](./technical/2026-04/2026-04-19/2026-04-19-00-25-58_track1_remaining_family_cellwise_final_closeout.md)
  Technical document for the final closeout of the completed `171`-run
  remaining-family `Track 1` exact-paper cellwise campaign wave, including
  winner-bookkeeping reconstruction, canonical benchmark refresh, and final
  results reporting.
- [technical/2026-04/2026-04-19/2026-04-19-01-04-28_track1_remaining_family_residual_cellwise_closure_campaigns.md](./technical/2026-04/2026-04-19/2026-04-19-01-04-28_track1_remaining_family_residual_cellwise_closure_campaigns.md)
  Technical document for the next aggressive overnight `Track 1`
  residual-cell closure wave, designed to spend a `6-7x` larger compute budget
  on the remaining non-green family-target cells across the nine non-`SVM`
  exact-paper families.
- [technical/2026-04/2026-04-19/2026-04-19-01-33-26_track1_residual_closure_aggregate_launcher_execution_mode_fix.md](./technical/2026-04/2026-04-19/2026-04-19-01-33-26_track1_residual_closure_aggregate_launcher_execution_mode_fix.md)
  Technical document for the narrow aggregate-launcher repair after the
  prepared overnight residual-closure package failed before launch because the
  execution-mode status line used bare `remote/local` PowerShell tokens.
- [technical/2026-04/2026-04-19/2026-04-19-11-23-44_track1_remaining_family_residual_cellwise_closure_final_closeout.md](./technical/2026-04/2026-04-19/2026-04-19-11-23-44_track1_remaining_family_residual_cellwise_closure_final_closeout.md)
  Technical document for the final closeout of the completed `1026`-run
  remaining-family residual-cell closure wave, including reconstructed
  bookkeeping, benchmark refresh, and final Markdown plus PDF reporting.
- [technical/2026-04/2026-04-19/2026-04-19-12-08-11_residual_closeout_styled_pdf_repair.md](./technical/2026-04/2026-04-19/2026-04-19-12-08-11_residual_closeout_styled_pdf_repair.md)
  Technical document for repairing the residual closeout report so its final
  PDF returns to the canonical styled export workflow.
- [technical/2026-04/2026-04-19/2026-04-19-12-20-48_residual_closeout_exact_styled_parity_repair.md](./technical/2026-04/2026-04-19/2026-04-19-12-20-48_residual_closeout_exact_styled_parity_repair.md)
  Technical document for the stricter residual closeout repair that requires
  the final PDF to match the earlier exact-paper closeout style in practice.
- [technical/2026-04/2026-04-19/2026-04-19-13-07-54_styled_pdf_persistent_preview_cleanup_fix.md](./technical/2026-04/2026-04-19/2026-04-19-13-07-54_styled_pdf_persistent_preview_cleanup_fix.md)
  Technical document for fixing the styled PDF exporter so it always renders
  from the stable preview HTML path beside the target PDF and only uses
  `--keep-html` to decide whether that preview file is deleted afterward.
- [technical/2026-04/2026-04-19/2026-04-19-13-17-01_residual_closeout_pdf_table_micro_rebalance.md](./technical/2026-04/2026-04-19/2026-04-19-13-17-01_residual_closeout_pdf_table_micro_rebalance.md)
  Technical document for the narrow PDF table rebalance of the residual
  closeout report, focused on the `Family Recovery Outcome` and
  `Aggregate Ranking` tables.

#### 2026-04-18

- [technical/2026-04/2026-04-18/2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns.md](./technical/2026-04/2026-04-18/2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns.md)
  Technical document for preparing the `171`-run remaining-family `Track 1`
  cellwise exact-paper wave that generalizes the `SVM` reference-model closure
  pattern to every still-open paper family.
- [technical/2026-04/2026-04-18/2026-04-18-17-11-45_track1_partial_closeout_family_row_backfill_in_full_matrix_tables.md](./technical/2026-04/2026-04-18/2026-04-18-17-11-45_track1_partial_closeout_family_row_backfill_in_full_matrix_tables.md)
  Technical document for re-checking the seven-family partial-closeout rerun
  rows and backfilling any still-stale family entries in the canonical `Track 1`
  full-matrix colored benchmark tables.
- [technical/2026-04/2026-04-18/2026-04-18-16-53-26_track1_closeout_pdf_table_layout_rebalance.md](./technical/2026-04/2026-04-18/2026-04-18-16-53-26_track1_closeout_pdf_table_layout_rebalance.md)
  Technical document for the report-specific PDF layout rebalance of the two
  `Track 1` remaining-family closeout reports, covering page-break placement
  and table-column redistribution.
- [technical/2026-04/2026-04-18/2026-04-18-16-47-12_track1_full_matrix_replication_table_refresh_after_closeout.md](./technical/2026-04/2026-04-18/2026-04-18-16-47-12_track1_full_matrix_replication_table_refresh_after_closeout.md)
  Technical document for refreshing the canonical `Track 1` full-matrix
  colored replication tables after closeout and for making that refresh a
  mandatory future closeout step whenever accepted family results improve.
- [technical/2026-04/2026-04-18/2026-04-18-16-29-35_track1_remaining_family_final_closeout_after_xgbm_lgbm_reruns.md](./technical/2026-04/2026-04-18/2026-04-18-16-29-35_track1_remaining_family_final_closeout_after_xgbm_lgbm_reruns.md)
  Technical document for the final closeout of the remaining-family
  `Track 1` exact-paper batch after the pending `XGBM` and `LGBM` reruns
  completed successfully.
- [technical/2026-04/2026-04-18/2026-04-18-15-39-41_track1_xgbm_lgbm_recovery_v2_exact_paper_and_remote_preflight_fix.md](./technical/2026-04/2026-04-18/2026-04-18-15-39-41_track1_xgbm_lgbm_recovery_v2_exact_paper_and_remote_preflight_fix.md)
  Technical document for the second `XGBM/LGBM` recovery pass, covering the
  exact-paper grid-builder robustness fix and the remote dependency-preflight
  repair.
- [technical/2026-04/2026-04-18/2026-04-18-15-29-53_track1_xgbm_lgbm_recovery_launcher_micro_fix.md](./technical/2026-04/2026-04-18/2026-04-18-15-29-53_track1_xgbm_lgbm_recovery_launcher_micro_fix.md)
  Technical document for the narrow launcher-only repair after the first
  `XGBM/LGBM` recovery attempt failed locally inside the shared remote
  exact-paper dependency-preflight helper.
- [technical/2026-04/2026-04-18/2026-04-18-11-36-29_track1_xgbm_lgbm_remote_dependency_recovery.md](./technical/2026-04/2026-04-18/2026-04-18-11-36-29_track1_xgbm_lgbm_remote_dependency_recovery.md)
  Technical document for the remote-crash recovery path after the interrupted
  `XGBM` launch, including optional-dependency preflight hardening and the
  narrow rerun scope for pending `XGBM` and `LGBM` campaigns.
- [technical/2026-04/2026-04-18/2026-04-18-11-02-15_track1_remaining_family_partial_closeout_and_benchmark_refresh.md](./technical/2026-04/2026-04-18/2026-04-18-11-02-15_track1_remaining_family_partial_closeout_and_benchmark_refresh.md)
  Technical document for verifying the interrupted remaining-family `Track 1`
  batch, closing out only the completed family campaigns, and refreshing the
  canonical benchmark surfaces before the later crash-recovery step.
- [technical/2026-04/2026-04-18/2026-04-18-00-54-22_hybrid_campaign_launcher_remote_flag_standard.md](./technical/2026-04/2026-04-18/2026-04-18-00-54-22_hybrid_campaign_launcher_remote_flag_standard.md)
  Technical document for promoting the hybrid campaign-launcher pattern, where
  one canonical `.ps1` runs locally by default and switches to remote
  execution through `-Remote`.
- [technical/2026-04/2026-04-18/2026-04-18-00-47-14_track1_remaining_exact_paper_family_campaigns.md](./technical/2026-04/2026-04-18/2026-04-18-00-47-14_track1_remaining_exact_paper_family_campaigns.md)
  Technical document for splitting the remaining `Track 1` exact-paper work
  into `9` family-focused campaign packages plus one aggregate sequential
  launcher after `SVM` closure.

#### 2026-04-17

- [technical/2026-04/2026-04-17/2026-04-17-19-46-05_campaign_report_folder_taxonomy_reorganization.md](./technical/2026-04/2026-04-17/2026-04-17-19-46-05_campaign_report_folder_taxonomy_reorganization.md)
  Technical document for reorganizing the flat `campaign_results` and
  `campaign_plans` roots into stable topic subfolders while preserving the
  timestamp-based per-report naming convention.
- [technical/2026-04/2026-04-17/2026-04-17-19-43-39_track1_reference_family_archive_standardization.md](./technical/2026-04/2026-04-17/2026-04-17-19-43-39_track1_reference_family_archive_standardization.md)
  Technical document for promoting the current `SVM` paper-reference archive
  layout into the canonical reusable `Track 1` family standard for all
  remaining paper-model archives.
- [technical/2026-04/2026-04-17/2026-04-17-19-30-41_svm_reference_onnx_subfolder_alignment.md](./technical/2026-04/2026-04-17/2026-04-17-19-30-41_svm_reference_onnx_subfolder_alignment.md)
  Technical document for moving the curated `SVM` reference `ONNX` amplitude
  and phase folders under a dedicated `onnx/` subtree and aligning every
  canonical repository reference to the new archive layout.
- [technical/2026-04/2026-04-17/2026-04-17-19-17-58_svm_reference_models_full_regeneration_provenance.md](./technical/2026-04/2026-04-17/2026-04-17-19-17-58_svm_reference_models_full_regeneration_provenance.md)
  Technical document for extending the curated `SVM` reference archive into a
  fully reconstructible package with explicit training-data provenance,
  Python-usable model artifacts, and target-level regeneration records.
- [technical/2026-04/2026-04-17/2026-04-17-18-52-51_svm_reference_model_inventory_and_archive.md](./technical/2026-04/2026-04-17/2026-04-17-18-52-51_svm_reference_model_inventory_and_archive.md)
  Technical document for formalizing the canonical `SVM` paper-reference
  model inventory inside the benchmark and for creating a curated `models/`
  archive with provenance sufficient to reconstruct the `19` accepted
  reference models.
- [technical/2026-04/2026-04-17/2026-04-17-18-32-17_track1_svm_exact_faithful_final_attempt_results_reporting.md](./technical/2026-04/2026-04-17/2026-04-17-18-32-17_track1_svm_exact_faithful_final_attempt_results_reporting.md)
  Technical document for closing the completed strict paper-faithful `SVR`
  final-attempt campaign through winner-artifact serialization, final
  reporting, PDF validation, and canonical-analysis refresh.
- [technical/2026-04/2026-04-17/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_preparation.md](./technical/2026-04/2026-04-17/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_preparation.md)
  Technical document for deciding whether one last `SVM`-row attempt should
  be prepared under a strict exact-paper `SVR` constraint, without changing
  the recovered algorithm or hyperparameter regime.

#### 2026-04-12

- [technical/2026-04/2026-04-12/2026-04-12-16-47-53_track1_paper_tables_3_4_5_6_canonical_comparison.md](./technical/2026-04/2026-04-12/2026-04-12-16-47-53_track1_paper_tables_3_4_5_6_canonical_comparison.md)
  Technical document for building the canonical `Track 1` paper-table
  comparison against tables `3-6`, including paper targets, repository
  results, explicit gap status, and a closure-oriented harmonic summary.
- [technical/2026-04/2026-04-12/2026-04-12-15-35-39_track1_per_harmonic_paper_table_replication.md](./technical/2026-04/2026-04-12/2026-04-12-15-35-39_track1_per_harmonic_paper_table_replication.md)
  Technical document for redefining `Track 1` completion around faithful
  per-harmonic paper-table replication, including canonical `paper vs
  repository` comparison artifacts and explicit closure status per harmonic.
- [technical/2026-04/2026-04-12/2026-04-12-11-29-44_exact_support_table_metric_width_equalization.md](./technical/2026-04/2026-04-12/2026-04-12-11-29-44_exact_support_table_metric_width_equalization.md)
  Technical document for the final narrow width-equalization pass on the first
  `Exact-Paper Support Runs` table, focused on making `Mean Component MAPE [%]`
  match `Mean Component MAE`.
- [technical/2026-04/2026-04-12/2026-04-12-11-04-10_campaign_results_pdf_micro_rebalance_followup.md](./technical/2026-04/2026-04-12/2026-04-12-11-04-10_campaign_results_pdf_micro_rebalance_followup.md)
  Technical document for a narrow follow-up rebalance of the campaign-results
  PDF table profiles after the first renderer-level promotion, focused on
  `Target A`, `Curve MAE`, and the first `Exact-Paper Support Runs` table.

#### 2026-04-13

- [technical/2026-04/2026-04-13/2026-04-13-22-53-36_track1_exact_paper_open_cell_repair_campaign_results_reporting.md](./technical/2026-04/2026-04-13/2026-04-13-22-53-36_track1_exact_paper_open_cell_repair_campaign_results_reporting.md)
  Technical document for closing the completed `Track 1` exact-paper
  open-cell repair campaign through paper-closure-first reporting and
  validated PDF export.
- [technical/2026-04/2026-04-13/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_preparation.md](./technical/2026-04/2026-04-13/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_preparation.md)
  Technical document for preparing the next `Track 1` campaign as an
  exact-paper open-cell repair batch focused on Tables `3-6` closure rather
  than harmonic-wise winner optimization.
- [technical/2026-04/2026-04-13/2026-04-13-20-35-43_github_quality_check_md012_and_node24_action_alignment.md](./technical/2026-04/2026-04-13/2026-04-13-20-35-43_github_quality_check_md012_and_node24_action_alignment.md)
  Technical document for fixing the reported GitHub quality-check `MD012`
  Markdown failure and aligning the repository workflow actions with the
  GitHub Node 24 migration path.
- [technical/2026-04/2026-04-13/2026-04-13-20-21-12_track1_reporting_template_alignment_to_paper_table_closure.md](./technical/2026-04/2026-04-13/2026-04-13-20-21-12_track1_reporting_template_alignment_to_paper_table_closure.md)
  Technical document for aligning future `Track 1` report-generation and
  summary templates with canonical paper-table closure language instead of the
  old winner-centric harmonic-wise framing.
- [technical/2026-04/2026-04-13/2026-04-13-20-09-32_track1_objective_redefinition_to_paper_table_replication.md](./technical/2026-04/2026-04-13/2026-04-13-20-09-32_track1_objective_redefinition_to_paper_table_replication.md)
  Technical document for promoting the paper-table cell closure criterion to
  the canonical `Track 1` objective and for aligning future plans, analyses,
  and results reports with per-target and per-harmonic status.
- [technical/2026-04/2026-04-13/2026-04-13-15-22-14_github_quality_check_markdown_md012_fix.md](./technical/2026-04/2026-04-13/2026-04-13-15-22-14_github_quality_check_markdown_md012_fix.md)
  Technical document for the narrow GitHub quality-check repair focused on
  `MD012/no-multiple-blanks` failures in harmonic-wise validation Markdown
  reports and, only if needed, the shared report-generation path.

#### 2026-04-14

- [technical/2026-04/2026-04-14/2026-04-14-13-42-10_track1_full_matrix_family_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-13-42-10_track1_full_matrix_family_campaign_preparation.md)
  Technical document for extending the exact-paper workflow and preparing a
  family-by-family `Track 1` full-matrix reproduction campaign across
  amplitudes and phases.
- [technical/2026-04/2026-04-14/2026-04-14-12-11-51_track1_full_matrix_paper_replication_dashboard.md](./technical/2026-04/2026-04-14/2026-04-14-12-11-51_track1_full_matrix_paper_replication_dashboard.md)
  Technical document for correcting the `Track 1` dashboard toward full
  paper-matrix replication, with Tables `3-5` reproduced model-by-model and
  harmonic-by-harmonic instead of only best-per-harmonic summaries.
- [technical/2026-04/2026-04-14/2026-04-14-11-37-05_track1_paper_tables_2_6_canonical_dashboard.md](./technical/2026-04/2026-04-14/2026-04-14-11-37-05_track1_paper_tables_2_6_canonical_dashboard.md)
  Technical document for promoting `RCIM Paper Reference Benchmark.md` into
  the canonical always-updated `Track 1` dashboard for paper Tables `2-6`,
  including repository-owned paper-table reconstructions and color-coded
  repository comparison tables.
- [technical/2026-04/2026-04-14/2026-04-14-10-27-49_track1_exact_paper_open_cell_repair_pdf_table_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-10-27-49_track1_exact_paper_open_cell_repair_pdf_table_rebalance.md)
  Technical document for rebalancing the two `Campaign Ranking` tables in the
  `Track 1` exact-paper open-cell repair campaign-results PDF.
- [technical/2026-04/2026-04-14/2026-04-14-15-17-07_track1_full_matrix_pdf_table_specific_width_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-15-17-07_track1_full_matrix_pdf_table_specific_width_rebalance.md)
  Technical document for introducing table-specific PDF width rules for the
  `Ranked Completed Runs` and `Campaign-Wide Cell Totals` tables in the
  `Track 1` full-matrix campaign results report without changing the generic
  table profile.
- [technical/2026-04/2026-04-14/2026-04-14-16-05-48_track1_benchmark_colored_status_marker_persistence.md](./technical/2026-04/2026-04-14/2026-04-14-16-05-48_track1_benchmark_colored_status_marker_persistence.md)
  Technical document for restoring and permanently preserving the colored
  `🟢/🟡/🔴` status markers in the canonical `Track 1` benchmark full-matrix
  tables during future campaign-driven updates.

- [technical/2026-04/2026-04-14/2026-04-14-16-27-39_track1_benchmark_table_2_5_alignment.md](./technical/2026-04/2026-04-14/2026-04-14-16-27-39_track1_benchmark_table_2_5_alignment.md)
  Technical document for realigning the canonical `Track 1` benchmark so that
  sections labeled `Table 2-5` match the actual paper tables, including the
  missing amplitude-MAE `Table 2` and the demotion of the current repository
  derived harmonic-direction summary.
- [technical/2026-04/2026-04-14/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_preparation.md)
  Technical document for preparing a broad but targeted `SVR` repair campaign
  against the currently open `SVM` cells in the canonical `Track 1` benchmark.
- [technical/2026-04/2026-04-14/2026-04-14-20-50-01_track1_svm_final_closure_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-20-50-01_track1_svm_final_closure_campaign_preparation.md)
  Technical document for preparing the narrow `SVR` final-closure campaign
  against the last residual yellow `SVM` cells in canonical `Track 1`
  Tables `2-5`.
- [technical/2026-04/2026-04-14/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_preparation.md)
  Technical document for preparing the final `SVR` micro-pass against the
  last residual `SVM` harmonics `40`, `240`, and `162` in canonical
  `Track 1`.
- [technical/2026-04/2026-04-14/2026-04-14-18-06-03_track1_svm_repair_pdf_table_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-18-06-03_track1_svm_repair_pdf_table_rebalance.md)
  Technical document for introducing report-specific styled-PDF width rules
  for the `Ranked Completed Runs` and `Table-Level Before Vs After` tables in
  the `Track 1` SVM repair campaign results report.
- [technical/2026-04/2026-04-14/2026-04-14-18-19-07_styled_pdf_table_profile_promotion_for_report_specific_widths.md](./technical/2026-04/2026-04-14/2026-04-14-18-19-07_styled_pdf_table_profile_promotion_for_report_specific_widths.md)
  Technical document for promoting manually validated report-specific table
  width profiles into permanent styled-PDF renderer rules instead of relying on
  visibly wrong generic fallback sizing for dense campaign tables.

#### 2026-04-11

- [technical/2026-04/2026-04-11/2026-04-11-20-32-27_campaign_results_pdf_layout_rule_promotion.md](./technical/2026-04/2026-04-11/2026-04-11-20-32-27_campaign_results_pdf_layout_rule_promotion.md)
  Technical document for promoting the newly repeated campaign-results PDF
  table-layout corrections into reusable renderer rules, with specific focus
  on `Comparable Offline Ranking` and `Exact-Paper Support Runs`.
- [technical/2026-04/2026-04-11/2026-04-11-13-05-23_exact_paper_faithful_campaign_stabilization_debug.md](./technical/2026-04/2026-04-11/2026-04-11-13-05-23_exact_paper_faithful_campaign_stabilization_debug.md)
  Technical document for reproducing and fixing the recurring exact-paper
  faithful-reproduction campaign failures exposed by the new coordinated
  launcher, starting with the export-disabled report-generation crash.

#### 2026-04-10

- [technical/2026-04/2026-04-10/2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_preparation.md](./technical/2026-04/2026-04-10/2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_preparation.md)
  Technical document for opening the next `Track 1` paper-faithful
  reproduction campaign, aimed at turning the stabilized exact-paper bank into
  a benchmark-facing offline reproduction path instead of another narrow
  export-stability pass.
- [technical/2026-04/2026-04-10/2026-04-10-21-24-35_styled_pdf_pipeline_auto_layout_learning.md](./technical/2026-04/2026-04-10/2026-04-10-21-24-35_styled_pdf_pipeline_auto_layout_learning.md)
  Technical document for promoting the successful exact-paper PDF layout
  refinements into reusable styled-report pipeline behavior so future exports
  inherit better table balancing, header wrapping, and page-break discipline
  by default.
- [technical/2026-04/2026-04-10/2026-04-10-21-05-20_exact_paper_campaign_results_pdf_layout_refinement.md](./technical/2026-04/2026-04-10/2026-04-10-21-05-20_exact_paper_campaign_results_pdf_layout_refinement.md)
  Technical document for the narrow styled-PDF layout refinement pass on the
  exact-paper campaign results report, focused on the `Objective And Outcome`
  page break and the two `Ranked Completed Runs` tables.
- [technical/2026-04/2026-04-10/2026-04-10-19-26-39_exact_paper_campaign_results_report.md](./technical/2026-04/2026-04-10/2026-04-10-19-26-39_exact_paper_campaign_results_report.md)
  Technical document for producing the final Markdown plus validated PDF
  campaign-results report for the completed exact-paper model-bank campaign and
  synchronizing the canonical analysis reports afterwards.
- [technical/2026-04/2026-04-10/2026-04-10-18-52-09_exact_paper_campaign_hgbm_export_debug.md](./technical/2026-04/2026-04-10/2026-04-10-18-52-09_exact_paper_campaign_hgbm_export_debug.md)
  Technical document for reproducing and debugging the strict exact-paper
  campaign failure currently observed on `HGBM`
  `fft_y_Fw_filtered_ampl_0` ONNX export before re-running the canonical
  batch launcher.
- [technical/2026-04/2026-04-10/2026-04-10-17-00-06_exact_paper_validation_fix_and_campaignization.md](./technical/2026-04/2026-04-10/2026-04-10-17-00-06_exact_paper_validation_fix_and_campaignization.md)
  Technical document for fixing the exact-paper ONNX export failure and
  converting the strict RCIM exact-paper branch into a repository-style
  batch-run workflow with launcher, logging, and campaign-oriented execution.
- [technical/2026-04/2026-04-10/2026-04-10-17-42-04_track_exact_paper_model_bundles_with_git_lfs.md](./technical/2026-04/2026-04-10/2026-04-10-17-42-04_track_exact_paper_model_bundles_with_git_lfs.md)
  Technical document for tracking only the newly generated exact-paper
  `paper_family_model_bank.pkl` validation bundles with Git LFS so the branch
  remains GitHub push-safe.
- [technical/2026-04/2026-04-10/2026-04-10-18-30-57_exact_paper_untracked_artifact_cleanup.md](./technical/2026-04/2026-04-10/2026-04-10-18-30-57_exact_paper_untracked_artifact_cleanup.md)
  Technical document for removing the leftover untracked exact-paper crash and
  superseded intermediate validation artifacts after the stabilized workflow
  commit.
- [technical/2026-04/2026-04-10/2026-04-10-16-12-21_rcim_exact_model_reimplementation_plan.md](./technical/2026-04/2026-04-10/2026-04-10-16-12-21_rcim_exact_model_reimplementation_plan.md)
  Technical document for evolving the current `Track 1` paper branch into a
  strict RCIM paper-faithful family-bank reimplementation, including the exact
  target schema, recovered model families, paper-style training surface, ONNX
  export surface, and target-wise evaluation flow.
- [technical/2026-04/2026-04-10/2026-04-10-13-30-40_rcim_recovered_asset_deep_analysis_report.md](./technical/2026-04/2026-04-10/2026-04-10-13-30-40_rcim_recovered_asset_deep_analysis_report.md)
  Technical document for producing a deep implementation-facing analysis of
  the recovered RCIM paper assets, including exact ONNX models, recovered code
  generations, TwinCAT XML exports, archive uncertainties, and the precise
  implications for faithful `Track 1` reimplementation.
- [technical/2026-04/2026-04-10/2026-04-10-12-42-35_git_push_pack_size_guard_and_recovered_asset_commit_split.md](./technical/2026-04/2026-04-10/2026-04-10-12-42-35_git_push_pack_size_guard_and_recovered_asset_commit_split.md)
  Technical document for formalizing a GitHub-bound aggregate push-size guard
  in the repository rules and for replacing the oversized recovered-asset
  integration commit with a smaller push-safe commit sequence.
- [technical/2026-04/2026-04-10/2026-04-10-11-19-25_rcim_paper_asset_recovery_and_reference_integration.md](./technical/2026-04/2026-04-10/2026-04-10-11-19-25_rcim_paper_asset_recovery_and_reference_integration.md)
  Technical document for analyzing, classifying, and integrating the newly
  recovered RCIM paper assets from `.temp/` into a coherent paper-specific
  reference area, including exact ONNX models, recovered code snapshots,
  TwinCAT XML exports, backup material, and the heavy `instance_v1` archive.
- [technical/2026-04/2026-04-10/2026-04-10-10-51-32_git_windows_line_ending_and_lfs_hook_noise_resolution.md](./technical/2026-04/2026-04-10/2026-04-10-10-51-32_git_windows_line_ending_and_lfs_hook_noise_resolution.md)
  Technical document for resolving the recurring Git-on-Windows LF/CRLF noise
  and the local Git LFS shell-hook `sh.exe` error path in this repository
  clone.

#### 2026-04-04

- [technical/2026-04/2026-04-04/2026-04-04-22-14-17_targeted_remote_followup_results_pdf_layout_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-22-14-17_targeted_remote_followup_results_pdf_layout_refinement.md)
- [technical/2026-04/2026-04-04/2026-04-04-22-24-40_targeted_remote_followup_results_pdf_layout_rebalance_and_page_break_fix.md](./technical/2026-04/2026-04-04/2026-04-04-22-24-40_targeted_remote_followup_results_pdf_layout_rebalance_and_page_break_fix.md)
- [technical/2026-04/2026-04-04/2026-04-04-22-29-19_targeted_remote_followup_completed_runs_family_column_final_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-22-29-19_targeted_remote_followup_completed_runs_family_column_final_refinement.md)
- [technical/2026-04/2026-04-04/2026-04-04-22-34-46_targeted_remote_followup_completed_runs_family_width_final_micro_adjustment.md](./technical/2026-04/2026-04-04/2026-04-04-22-34-46_targeted_remote_followup_completed_runs_family_width_final_micro_adjustment.md)
  Technical document for refining the styled PDF layout of the targeted remote follow-up campaign results report, including table rebalancing and forced clean page starts for the final conclusions and artifact-reference sections.
- [technical/2026-04/2026-04-04/2026-04-04-22-07-17_large_tree_model_exportability_constraint.md](./technical/2026-04/2026-04-04/2026-04-04-22-07-17_large_tree_model_exportability_constraint.md)
  Technical document for recording that the oversized ~`91 GB` tree-model artifact class is excluded from future deployment/export candidate sets and should not be promoted into the TwinCAT-oriented export branch.
- [technical/2026-04/2026-04-04/2026-04-04-21-35-44_docs_requirements_location_alignment.md](./technical/2026-04/2026-04-04/2026-04-04-21-35-44_docs_requirements_location_alignment.md)
  Technical document for relocating the documentation-only GitHub Pages requirements file out of the repository root and realigning the workflow/documentation references to the corrected support path.
- [technical/2026-04/2026-04-04/2026-04-04-21-31-17_github_pages_workflow_dependency_footprint_fix.md](./technical/2026-04/2026-04-04/2026-04-04-21-31-17_github_pages_workflow_dependency_footprint_fix.md)
  Technical document for fixing the GitHub Pages workflow so the Sphinx portal build no longer installs the full heavyweight training stack and fails with runner disk exhaustion.
- [technical/2026-04/2026-04-04/2026-04-04-20-12-30_remote_training_completion_path_sync_fix.md](./technical/2026-04/2026-04-04/2026-04-04-20-12-30_remote_training_completion_path_sync_fix.md)
  Technical document for fixing the remaining LAN-remote training launcher defect in the local completion path so remote campaigns can sync their canonical artifacts back automatically after successful execution.
- [technical/2026-04/2026-04-04/2026-04-04-11-41-47_remote_training_launcher_command_length_fix.md](./technical/2026-04/2026-04-04/2026-04-04-11-41-47_remote_training_launcher_command_length_fix.md)
  Technical document for fixing the Windows command-line length failure in the SSH-backed remote training launcher so prepared LAN campaigns can start successfully.
- [technical/2026-04/2026-04-04/2026-04-04-11-21-09_targeted_remote_followup_campaign_preparation.md](./technical/2026-04/2026-04-04/2026-04-04-11-21-09_targeted_remote_followup_campaign_preparation.md)
  Technical document for preparing the next targeted LAN-remote follow-up campaign around `residual_harmonic_mlp`, `feedforward`, and `hist_gradient_boosting` after the first validated remote execution.
- [technical/2026-04/2026-04-04/2026-04-04-10-52-03_remote_lan_training_documentation_audit_and_family_best_refresh.md](./technical/2026-04/2026-04-04/2026-04-04-10-52-03_remote_lan_training_documentation_audit_and_family_best_refresh.md)
  Technical document for auditing the repository documentation coverage of the LAN-remote training workflow, refreshing the canonical family-best analysis with the new remote results, and evaluating which follow-up experiments are worth planning on the stronger workstation.
- [technical/2026-04/2026-04-04/2026-04-04-10-48-09_remote_training_campaign_results_pdf_completed_runs_table_refinement_round_four.md](./technical/2026-04/2026-04-04/2026-04-04-10-48-09_remote_training_campaign_results_pdf_completed_runs_table_refinement_round_four.md)
  Technical document for a fourth narrow refinement pass on the `Ranked Completed Runs` table in the remote training validation campaign PDF, again focused on `Family` width and the `Test MAE [deg]` header fit.
- [technical/2026-04/2026-04-04/2026-04-04-10-45-15_remote_training_campaign_results_pdf_completed_runs_table_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-10-45-15_remote_training_campaign_results_pdf_completed_runs_table_refinement.md)
  Technical document for a final narrow refinement of the `Ranked Completed Runs` table in the remote training validation campaign PDF, focused on `Family` width and cleaner `Test MAE [deg]` header fit.
- [technical/2026-04/2026-04-04/2026-04-04-10-42-25_remote_training_campaign_results_pdf_layout_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-10-42-25_remote_training_campaign_results_pdf_layout_refinement.md)
  Technical document for the second refinement pass on the remote training validation campaign results PDF, including a narrower metric-header fit rebalance and a forced new-page start for `Recommended Next Actions`.
- [technical/2026-04/2026-04-04/2026-04-04-10-35-03_remote_training_campaign_results_pdf_layout_repair.md](./technical/2026-04/2026-04-04/2026-04-04-10-35-03_remote_training_campaign_results_pdf_layout_repair.md)
  Technical document for repairing the styled PDF layout of the remote training validation campaign results report, including table-width rebalance and a forced new-page start for the `Campaign Winner` section.
- [technical/2026-04/2026-04-04/2026-04-04-00-57-29_remote_training_pipeline_hardening_and_skill_promotion.md](./technical/2026-04/2026-04-04/2026-04-04-00-57-29_remote_training_pipeline_hardening_and_skill_promotion.md)
  Technical document for hardening the LAN-remote training campaign pipeline after the first real execution, eliminating the remaining artifact-bookkeeping bug, and promoting the validated workflow into a repository-local Codex skill.

#### 2026-04-05

- [technical/2026-04/2026-04-05/2026-04-05-11-04-45_github_pages_environment_protection_fix_and_node24_alignment.md](./technical/2026-04/2026-04-05/2026-04-05-11-04-45_github_pages_environment_protection_fix_and_node24_alignment.md)
  Technical document for fixing the GitHub Pages deploy blocker caused by `github-pages` environment protection rules and aligning the workflow with GitHub's Node.js 24 action-runtime transition.

#### 2026-04-07

- [technical/2026-04/2026-04-07/2026-04-07-12-47-33_github_pages_live_url_publication_registration.md](./technical/2026-04/2026-04-07/2026-04-07-12-47-33_github_pages_live_url_publication_registration.md)
  Technical document for registering the now-live GitHub Pages public URL of the repository Sphinx portal and updating the main repository entry points to surface that published documentation endpoint.
- [technical/2026-04/2026-04-07/2026-04-07-13-04-01_github_repository_governance_and_automation_baseline.md](./technical/2026-04/2026-04-07/2026-04-07-13-04-01_github_repository_governance_and_automation_baseline.md)
  Technical document for defining the first practical GitHub governance baseline for the public repository, including a separate CI workflow, review templates, ownership hints, Dependabot, and recommended GitHub-side ruleset settings.
- [technical/2026-04/2026-04-07/2026-04-07-15-41-56_github_quality_workflow_naming_and_markdownlint_memory_fix.md](./technical/2026-04/2026-04-07/2026-04-07-15-41-56_github_quality_workflow_naming_and_markdownlint_memory_fix.md)
  Technical document for renaming the new repository-quality workflow to a clearer GitHub-facing label and fixing the GitHub Actions Markdownlint out-of-memory failure by switching to chunked lint execution.

#### 2026-04-08

- [technical/2026-04/2026-04-08/2026-04-08-18-57-43_harmonic_wise_comparison_pipeline.md](./technical/2026-04/2026-04-08/2026-04-08-18-57-43_harmonic_wise_comparison_pipeline.md)
  Technical document for opening the offline paper-aligned harmonic-wise comparison pipeline branch, including harmonic prediction, TE reconstruction, offline motion-profile playback, and the benchmark path needed to close `Target A`.
- [technical/2026-04/2026-04-08/2026-04-08-17-51-22_harmonic_wise_pipeline_before_wave2_temporal_models.md](./technical/2026-04/2026-04-08/2026-04-08-17-51-22_harmonic_wise_pipeline_before_wave2_temporal_models.md)
  Technical document for making the paper-aligned harmonic-wise pipeline the immediate post-Wave-1 branch before the future Wave 2 temporal-model work is opened.
- [technical/2026-04/2026-04-08/2026-04-08-17-28-35_paper_pipeline_breakdown_and_backlog_prioritization.md](./technical/2026-04/2026-04-08/2026-04-08-17-28-35_paper_pipeline_breakdown_and_backlog_prioritization.md)
  Technical document for decomposing the remaining paper-aligned implementation gap into six concrete pipeline stages and prioritizing which stages should land immediately versus later in the backlog.
- [technical/2026-04/2026-04-08/2026-04-08-17-11-00_paper_reference_alignment_and_gap_tracking.md](./technical/2026-04/2026-04-08/2026-04-08-17-11-00_paper_reference_alignment_and_gap_tracking.md)
  Technical document for turning the RCIM ML-compensation paper into a canonical repository benchmark package, adding explicit paper-vs-repository tracking, and recording the missing pipelines required for a true Table 9 comparison.
- [technical/2026-04/2026-04-08/2026-04-08-16-52-12_master_summary_mandatory_maintenance_rule.md](./technical/2026-04/2026-04-08/2026-04-08-16-52-12_master_summary_mandatory_maintenance_rule.md)
  Technical document for promoting the canonical training-results master summary into a mandatory maintained project-control report that must stay synchronized after campaigns and result-registry updates.
- [technical/2026-04/2026-04-08/2026-04-08-16-24-05_canonical_training_results_master_summary.md](./technical/2026-04/2026-04-08/2026-04-08-16-24-05_canonical_training_results_master_summary.md)
  Technical document for creating a canonical always-updated master summary of implemented model families, roadmap state, best results, and family-by-family training outcomes for colleague-facing project control.
- [technical/2026-04/2026-04-08/2026-04-08-16-11-02_post_wave_twincat_deployment_branch_deferral.md](./technical/2026-04/2026-04-08/2026-04-08-16-11-02_post_wave_twincat_deployment_branch_deferral.md)
  Technical document for deferring the TwinCAT deployment-evaluation branch until after the next modeling wave is implemented and reviewed, while keeping the branch available for later re-prioritization.
- [technical/2026-04/2026-04-08/2026-04-08-15-51-10_remote_campaign_user_driven_launch_handoff.md](./technical/2026-04/2026-04-08/2026-04-08-15-51-10_remote_campaign_user_driven_launch_handoff.md)
  Technical document for formalizing the LAN-remote training workflow so Codex prepares the launcher and exact terminal command, then waits for the user to start and finish the campaign instead of holding the live remote execution session open.
- [technical/2026-04/2026-04-08/2026-04-08-12-50-04_github_branch_topology_refactor_and_main_adoption.md](./technical/2026-04/2026-04-08/2026-04-08-12-50-04_github_branch_topology_refactor_and_main_adoption.md)
  Technical document for refactoring the repository branch topology around a new canonical `main` branch, retiring `standard-ml-codex`, and defining the legacy/test handling of the remaining historical branches plus the required GitHub ruleset and Pages follow-up.
- [technical/2026-04/2026-04-08/2026-04-08-13-35-06_post_rename_branch_reference_realignment.md](./technical/2026-04/2026-04-08/2026-04-08-13-35-06_post_rename_branch_reference_realignment.md)
  Technical document for the narrow post-migration cleanup that removes stale pre-rename branch references from the active workflows and current-facing documentation after the repository has already moved to `main`.
- [technical/2026-04/2026-04-08/2026-04-08-13-54-00_github_branch_migration_final_audit.md](./technical/2026-04/2026-04-08/2026-04-08-13-54-00_github_branch_migration_final_audit.md)
  Technical document for the final read-only audit of the completed GitHub branch migration, focused on local tracking, remote branch topology, workflow triggers, and current-facing repository references.

#### 2026-04-09

- [technical/2026-04/2026-04-09/2026-04-09-22-40-59_sphinx_requests_dependency_warning_resolution.md](./technical/2026-04/2026-04-09/2026-04-09-22-40-59_sphinx_requests_dependency_warning_resolution.md)
  Technical document for resolving the previously observed
  `RequestsDependencyWarning` in the canonical Sphinx build path by aligning
  the documentation dependency environment explicitly.
- [technical/2026-04/2026-04-09/2026-04-09-22-19-28_python_script_style_audit_and_rule_enforcement.md](./technical/2026-04/2026-04-09/2026-04-09-22-19-28_python_script_style_audit_and_rule_enforcement.md)
  Technical document for auditing repository-owned Python scripts against the
  approved style baseline and for formalizing a mandatory style-compliance
  check whenever a new Python script is created.
- [technical/2026-04/2026-04-09/2026-04-09-11-56-36_paper_reimplementation_structure_reorganization.md](./technical/2026-04/2026-04-09/2026-04-09-11-56-36_paper_reimplementation_structure_reorganization.md)
  Technical document for reorganizing the paper-faithful reimplementation branch into a dedicated repository structure instead of leaving its scripts, configs, notes, and artifacts mixed with generic training helpers.
- [technical/2026-04/2026-04-09/2026-04-09-11-36-10_dual_track_paper_comparison_strategy.md](./technical/2026-04/2026-04-09/2026-04-09-11-36-10_dual_track_paper_comparison_strategy.md)
  Technical document for separating the paper-faithful harmonic-wise benchmark from the repository direct-TE comparison track and for planning their coordinated backlog integration.

#### 2026-04-03

- [technical/2026-04/2026-04-03/2026-04-03-17-54-21_remote_training_campaign_real_validation_and_setup_guide.md](./technical/2026-04/2026-04-03/2026-04-03-17-54-21_remote_training_campaign_real_validation_and_setup_guide.md)
  Technical document for running the first real remote LAN training campaign, validating the new SSH-backed workflow end-to-end, and preparing the required local/remote setup guidance.
- [technical/2026-04/2026-04-03/2026-04-03-17-10-28_remote_lan_training_campaign_execution_pipeline.md](./technical/2026-04/2026-04-03/2026-04-03-17-10-28_remote_lan_training_campaign_execution_pipeline.md)
  Technical document for adding a repository-owned workflow that launches approved training campaigns from the local workstation while executing the heavy campaign runtime on the stronger LAN workstation.
- [technical/2026-04/2026-04-03/2026-04-03-16-24-46_private_repo_pages_publication_backlog_note.md](./technical/2026-04/2026-04-03/2026-04-03-16-24-46_private_repo_pages_publication_backlog_note.md)
  Technical note for recording that the repository should stay private for now and that GitHub Pages publication of the Sphinx portal must be completed later, after a future public-repo transition.
- [technical/2026-04/2026-04-03/2026-04-03-14-29-07_sphinx_github_pages_publication_and_mandatory_update_pipeline.md](./technical/2026-04/2026-04-03/2026-04-03-14-29-07_sphinx_github_pages_publication_and_mandatory_update_pipeline.md)
  Technical document for publishing the canonical Sphinx portal through GitHub Pages and for formalizing the repository rule that new scripts and features must keep the Sphinx documentation updated and rebuilt.
- [technical/2026-04/2026-04-03/2026-04-03-00-54-03_sphinx_documentation_regeneration.md](./technical/2026-04/2026-04-03/2026-04-03-00-54-03_sphinx_documentation_regeneration.md)
  Technical document for regenerating the canonical repository Sphinx portal through the tracked `site/` build pipeline and resolving any warning-as-error build blockers that appear.
- [technical/2026-04/2026-04-03/2026-04-03-00-44-44_repository_wide_script_documentation_audit_and_rule_formalization.md](./technical/2026-04/2026-04-03/2026-04-03-00-44-44_repository_wide_script_documentation_audit_and_rule_formalization.md)
  Technical document for auditing the full `scripts/` Python tree against the approved comment and docstring format, and for formalizing a single repository-wide rule so every future script must follow the same documentation style by default.
- [technical/2026-04/2026-04-03/2026-04-03-00-34-49_video_guide_script_docstring_and_comment_retrofit.md](./technical/2026-04/2026-04-03/2026-04-03-00-34-49_video_guide_script_docstring_and_comment_retrofit.md)
  Technical document for retrofitting the recent TwinCAT/TestRig video-guide tooling scripts with Google-style docstrings and stronger internal comment coverage aligned with the Sphinx `napoleon` portal.
- [technical/2026-04/2026-04-03/2026-04-03-00-24-45_technical_document_monthly_grouping.md](./technical/2026-04/2026-04-03/2026-04-03-00-24-45_technical_document_monthly_grouping.md)
  Technical document for adding a month-level grouping layer above the existing day-based `doc/technical/` history.

#### 2026-04-02

- [technical/2026-04/2026-04-02/2026-04-02-19-14-38_temp_tools_cleanup_and_final_video_guide_reconciliation.md](./technical/2026-04/2026-04-02/2026-04-02-19-14-38_temp_tools_cleanup_and_final_video_guide_reconciliation.md)
  Technical document for auditing `.temp/` and `.tools/`, cleaning stale runtime residue, and performing a final reconciliation pass between the canonical video source bundle and the promoted TwinCAT/TestRig video guides.
- [technical/2026-04/2026-04-02/2026-04-02-19-08-25_transmission_error_foundations_bundle_reference_realignment.md](./technical/2026-04/2026-04-02/2026-04-02-19-08-25_transmission_error_foundations_bundle_reference_realignment.md)
  Technical document for realigning the repository-authored references after manual renaming and cleanup of the promoted Transmission Error Foundations presentation/video bundle.
- [technical/2026-04/2026-04-02/2026-04-02-18-57-43_project_status_presentation_and_video_bundle_integration.md](./technical/2026-04/2026-04-02/2026-04-02-18-57-43_project_status_presentation_and_video_bundle_integration.md)
  Technical document for promoting the imported project-status presentation and video bundle from `.temp/Project_Status/` into the canonical repository guide surface.
- [technical/2026-04/2026-04-02/2026-04-02-18-52-33_repository_wide_markdown_residual_cleanup.md](./technical/2026-04/2026-04-02/2026-04-02-18-52-33_repository_wide_markdown_residual_cleanup.md)
  Technical document for clearing the remaining repository-wide Markdownlint residues in the current Git-tracked Markdown set.
- [technical/2026-04/2026-04-02/2026-04-02-18-46-22_markdown_zero_warning_rule_tightening.md](./technical/2026-04/2026-04-02/2026-04-02-18-46-22_markdown_zero_warning_rule_tightening.md)
  Technical document for tightening the repository Markdown rule so newly created or modified Git-tracked Markdown files must reach zero warnings before task closure.

#### 2026-03-10

- [technical/2026-03/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md](./technical/2026-03/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md)
  Technical document for the Conda, PyTorch, and PyTorch Lightning environment baseline.
- [technical/2026-03/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md](./technical/2026-03/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md)
  Technical document for the validated TE dataset-processing pipeline and raw-data reconstruction path.
- [technical/2026-03/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md](./technical/2026-03/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md)
  Technical document for the `scripts/`, `config/`, and per-script documentation repository rules.
- [technical/2026-03/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md](./technical/2026-03/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md)
  Technical document for the grouped `doc/` folder reorganization.
- [technical/2026-03/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md](./technical/2026-03/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md)
  Technical document for moving the existing agent submodule and adding the requested `agents/` submodule collection.
- [technical/2026-03/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md](./technical/2026-03/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md)
  Technical document for enforcing the technical-document approval workflow plus a mandatory final Git commit.
- [technical/2026-03/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md](./technical/2026-03/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md)
  Technical document for replacing the archived reference code `.zip` files in `reference/codes/` with Git submodules.
- [technical/2026-03/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md](./technical/2026-03/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md)
  Technical document for creating persistent `doc/reference_codes/` notes from the reference-code submodules.
- [technical/2026-03/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md](./technical/2026-03/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md)
  Technical document for the first modular PyTorch Lightning feedforward baseline for TE regression.
- [technical/2026-03/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md](./technical/2026-03/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md)
  Technical document for clarifying the original CSV header typo `Poisition_Output_Reducer_Fw` versus the normalized internal column naming.
- [technical/2026-03/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md](./technical/2026-03/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md)
  Technical document for requiring a detailed `project_usage_guide.md` update before commit whenever repository functionality changes.
- [technical/2026-03/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md](./technical/2026-03/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md)
  Technical document for refreshing `project_usage_guide.md` so it matches the current runnable training and dataset workflows.
- [technical/2026-03/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md](./technical/2026-03/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md)
  Technical document for tuning the default dataloader worker and memory-pinning settings of the current feedforward training workflow.
- [technical/2026-03/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md](./technical/2026-03/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md)
  Technical document for fixing direct execution of the feedforward training entry point when the repository root is missing from `sys.path`.
- [technical/2026-03/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md](./technical/2026-03/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md)
  Technical document for making the feedforward training terminal output cleaner, colorized, and less noisy on Windows.
- [technical/2026-03/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md](./technical/2026-03/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md)
  Technical document for formalizing dependency tracking in the workflow and auditing current imports against `requirements.txt`.

#### 2026-03-11

- [technical/2026-03/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md](./technical/2026-03/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md)
  Technical document for removing the remaining Lightning startup tip and `_pytree` sanity-check warning from feedforward training output.
- [technical/2026-03/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md](./technical/2026-03/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md)
  Technical document for correcting the generator-based context-manager return annotation in the training entry point.
- [technical/2026-03/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md)
  Technical document for normalizing blank-line spacing around top-level function definitions in the feedforward training entry point.
- [technical/2026-03/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md)
  Technical document for extending the approved function-spacing convention to all project-authored Python scripts.
- [technical/2026-03/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md)
  Technical document for extending the approved blank-line spacing convention to top-level class and dataclass declarations.
- [technical/2026-03/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md](./technical/2026-03/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md)
  Technical document for propagating the broader manual coding style introduced in commit `228a999c94eb67d1c07eebfbd87c05903e99b694` to the remaining project scripts.
- [technical/2026-03/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md](./technical/2026-03/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md)
  Technical document for updating the persistent programming style guide with the approved spacing rules and the broader manual refactoring conventions.
- [technical/2026-03/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md](./technical/2026-03/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md)
  Technical document for aligning the persistent programming style guide with the latest approved manual code-style refactoring commit.
- [technical/2026-03/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md](./technical/2026-03/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md)
  Technical document for adding a proof feedforward training run, a held-out test phase, and a per-run result report artifact.

#### 2026-03-12

- [technical/2026-03/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md](./technical/2026-03/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md)
  Technical document for writing a full analytical report of the feedforward proof run with narrative interpretation and comparison against the reference papers.
- [technical/2026-03/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md](./technical/2026-03/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md)
  Technical document for producing a detailed training-configuration explanation report plus a PDF export and heavier workstation-oriented configuration proposals.
- [technical/2026-03/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md](./technical/2026-03/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md)
  Technical document for executing and comparing the pending baseline and workstation-oriented feedforward training variants.
- [technical/2026-03/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md](./technical/2026-03/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md)
  Technical document for executing a mixed campaign that combines longer schedules, denser point sampling, larger batches, and larger feedforward models.
- [technical/2026-03/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md](./technical/2026-03/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md)
  Technical document for making preliminary planning reports and final results reports mandatory companions to every future training campaign.
- [technical/2026-03/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md](./technical/2026-03/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md)
  Technical document for renaming the current report files so they include the full timestamp in their filenames.
- [technical/2026-03/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md](./technical/2026-03/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md)
  Technical document for reorganizing the technical-document tree by day and the report tree by report type.
- [technical/2026-03/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md](./technical/2026-03/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md)
  Technical document for regenerating the training-configuration analysis PDF with a much stronger visual layout and print-oriented styling.
- [technical/2026-03/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md](./technical/2026-03/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md)
  Technical document for redesigning the analytical PDF again with a restrained blue palette, white background, better page flow, and more professional typography.
- [technical/2026-03/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md](./technical/2026-03/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md)
  Technical document for correcting the analytical PDF printable margins and replacing the dense configuration table with a cleaner professional layout.
- [technical/2026-03/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md](./technical/2026-03/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md)
  Technical document for fixing the remaining technical-table fit issues in the analytical PDF and enforcing post-export PDF validation.
- [technical/2026-03/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md](./technical/2026-03/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md)
  Technical document for refining the three configuration tables so each one repeats the config name and uses more consistent centered alignment.
- [technical/2026-03/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md](./technical/2026-03/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md)
  Technical document for declaring the approved analytical PDF as the project golden standard and encoding its style rules for future reports.
- [technical/2026-03/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md](./technical/2026-03/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md)
  Technical document for refactoring the styled PDF exporter to match repository coding style and clarifying that the style rules also apply to utility/report scripts.
- [technical/2026-03/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md](./technical/2026-03/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md)
  Technical document for changing the repository workflow so every Git commit requires a final explicit user approval after the work is completed.
- [technical/2026-03/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md](./technical/2026-03/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md)
  Technical document for shortening the styled PDF exporter comments and aligning the persistent coding-style rules with the latest user-approved manual refactor.
- [technical/2026-03/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md](./technical/2026-03/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md)
  Technical document for reorganizing `config/`, introducing a queue-based batch training workflow, and generating campaign execution reports for later post-training analysis.
- [technical/2026-03/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md](./technical/2026-03/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md)
  Technical document for automatic campaign YAML generation, active-campaign state tracking, protected-file warnings, and completion/cancellation handling.

#### 2026-03-13

- [technical/2026-03/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md](./technical/2026-03/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md)
  Technical document for writing the final mixed-campaign results report and selecting the best current feedforward training preset.
- [technical/2026-03/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md](./technical/2026-03/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md)
  Technical document for making PDF export and PDF validation mandatory for final campaign-results reports.
- [technical/2026-03/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md](./technical/2026-03/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md)
  Technical document for repairing the mixed-campaign PDF table widths and tightening the rule so future table-layout defects must be caught before task closure.

#### 2026-03-14

- [technical/2026-03/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md](./technical/2026-03/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md)
  Technical document for fixing remaining header spill and semantic config wrapping issues in the campaign-results PDF tables.
- [technical/2026-03/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md](./technical/2026-03/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md)
  Technical document for enforcing vertical table-cell centering and cleaner section page-break behavior in the campaign-results PDF.
- [technical/2026-03/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md](./technical/2026-03/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md)
  Technical document for evaluating a cleaner internal code layout and moving the external agent submodules under `reference/agents/`.
- [technical/2026-03/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md](./technical/2026-03/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md)
  Technical document for moving root `models/` and `training/` source code under `scripts/`, reserving root `models/` for artifacts, and relocating agent submodules under `reference/agents/`.
- [technical/2026-03/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md](./technical/2026-03/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md)
  Technical document for reviewing the current GPU training path and proposing practical transfer, precision, and Trainer-level performance optimizations.

#### 2026-03-16

- [technical/2026-03/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md](./technical/2026-03/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md)
  Technical document for validating and executing the project environment migration from Python 3.10 to Python 3.12.

#### 2026-03-17

- [technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md](./technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md)
  Technical planning document for the TE model-family roadmap across standard, temporal, hybrid, and PINN approaches.
- [technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md](./technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md)
  Technical backlog document for implementing, validating, smoke-testing, and comparing all approved TE model families through campaign waves.
- [technical/2026-03/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md](./technical/2026-03/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md)
  Technical note for keeping Lightweight Transformer and Neural ODE families explicitly in scope as low-priority exploratory options.
- [technical/2026-03/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md](./technical/2026-03/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md)
  Technical review note for adding explicit State-Space, Mixture-of-Experts, and optional Kernel/GP families to the TE planning set.
- [technical/2026-03/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md](./technical/2026-03/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md)
  Technical document for the shared training, smoke-test, validation, and metrics infrastructure required before implementing the planned TE model families.
- [technical/2026-03/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md](./technical/2026-03/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md)
  Technical document for moving the TE implementation backlog into a privileged live location under `doc/running/`.
- [technical/2026-03/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md](./technical/2026-03/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md)
  Technical document for cleaning up redundant `variable=variable` function-call arguments while preserving explicit keywords where they improve readability.
- [technical/2026-03/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md](./technical/2026-03/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md)
  Technical document for reorganizing training outputs by artifact type and adding explicit campaign, family, and program best-result registries.
- [technical/2026-03/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md](./technical/2026-03/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md)
  Technical document for migrating the historical `output/feedforward_network/` artifacts into the new training-run structure and rewriting repository-authored path references.
- [technical/2026-03/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md](./technical/2026-03/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md)
  Technical document for removing the remaining feedforward-specific legacy snapshot compatibility from the active training pipeline.
- [technical/2026-03/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md](./technical/2026-03/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md)
  Technical document for formalizing the registry-selected feedforward run as the canonical reference baseline before Wave 1.
- [technical/2026-03/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md](./technical/2026-03/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md)
  Technical document for preparing Wave 1 structured-baseline implementation and the first exploratory campaign against the formalized feedforward reference baseline.

#### 2026-03-18

- [technical/2026-03/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md](./technical/2026-03/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md)
  Technical document for making model-level explanatory reports mandatory whenever a new model or new model-specific training workflow is introduced.
- [technical/2026-03/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md](./technical/2026-03/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md)
  Technical document for creating retroactive explanatory reports for the already implemented structured TE model families.
- [technical/2026-03/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md](./technical/2026-03/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md)
  Technical document for exporting the existing model-explanatory reports to styled PDFs and validating the real exported artifacts.
- [technical/2026-03/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md](./technical/2026-03/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md)
  Technical document for requiring visual conceptual diagrams and image assets inside future model-explanatory reports and their PDF exports.
- [technical/2026-03/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md](./technical/2026-03/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md)
  Technical document for retroactively adding diagrams to the existing structured-model reports and preserving those images in the exported PDFs.
- [technical/2026-03/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md](./technical/2026-03/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md)
  Technical document for correcting diagram layout defects, introducing reusable diagram generation, removing figure-background clashes, and adding both conceptual and architecture diagrams to the model reports.
- [technical/2026-03/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md](./technical/2026-03/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md)
  Technical document for correcting diagram geometry defects, improving figure centering, replacing pseudo-arrows with real connectors, and revalidating the SVG and PDF outputs.
- [technical/2026-03/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md](./technical/2026-03/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md)
  Technical document for standardizing the report-generation pipeline with a repository-owned orchestrator, a persistent PDF-validation tooling environment, and cleaner temporary-artifact management.
- [technical/2026-03/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md)
  Technical document for removing obsolete report-pipeline temporary environments and retaining only the intended standardized temporary layout.
- [technical/2026-03/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md](./technical/2026-03/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md)
  Technical document for fully removing the remaining standardized report-pipeline runtime temp root and leaving the repository without runtime temporary folders.
- [technical/2026-03/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md](./technical/2026-03/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md)
  Technical document for making frequent internal section comments an explicit persistent style rule and retrofitting that style into the recent report scripts.
- [technical/2026-03/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md](./technical/2026-03/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md)
  Technical document for a focused section-comment retrofit of the remaining model scripts that still underuse internal `# ...` stage markers.
- [technical/2026-03/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md](./technical/2026-03/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md)
  Technical document for auditing all Python comments under `scripts/` and correcting only the ones whose meaning no longer matches the code they describe.
- [technical/2026-03/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md](./technical/2026-03/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md)
  Technical document for the second pass of model-report diagram refinement, focused on connector pile-up, slide centering, multiline card layout, and safer routing.
- [technical/2026-03/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md](./technical/2026-03/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md)
  Technical document for the third pass of model-report diagram refinement, focused on simplifying neuron arrows, enforcing perpendicular box routing, arrowhead clearance, and model-specific spacing fixes.
- [technical/2026-03/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md)
  Technical document for a formatting-only cleanup that normalizes redundant blank lines between top-level definitions in the model-report diagram generator.
- [technical/2026-03/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md)
  Technical document for a formatting-only repository-wide cleanup that normalizes redundant blank lines between top-level definitions across the Python scripts under `scripts/`.

#### 2026-03-20

- [technical/2026-03/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md](./technical/2026-03/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md)
  Technical planning document for a beginner-to-university learning guide covering neural-network foundations, training/validation/testing, and the TE model-family curriculum from feedforward baselines to planned advanced architectures.
- [technical/2026-03/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md](./technical/2026-03/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md)
  Technical planning document for exporting the learning guides to PDF and requiring explicit user approval of generated guide images before final PDF generation.
- [technical/2026-03/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md](./technical/2026-03/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md)
  Technical planning document for preparing NotebookLM-ready video-guide source packages and adding the related approval-gated workflow rule for future learning-guide videos.
- [technical/2026-03/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md](./technical/2026-03/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md)
  Technical planning document for the architecture learning-guide series starting from the FeedForward Network and extending to the other documented model families.

### Script Documentation

- [scripts/datasets/transmission_error_dataset.md](./scripts/datasets/transmission_error_dataset.md)
  Script-level documentation for the TE dataset parser, PyTorch dataset, and dataloader utilities.
- [scripts/datasets/visualize_transmission_error.md](./scripts/datasets/visualize_transmission_error.md)
  Script-level documentation for the TE curve visualization utility.
- [scripts/reports/generate_model_report_diagrams.md](./scripts/reports/generate_model_report_diagrams.md)
  Script-level documentation for the SVG generator used by the model explanatory reports.
- [scripts/reports/run_report_pipeline.md](./scripts/reports/run_report_pipeline.md)
  Script-level documentation for the orchestration runner that standardizes diagram regeneration, styled PDF export, and PDF validation.
- [scripts/training/train_feedforward_network.md](./scripts/training/train_feedforward_network.md)
  Script-level documentation for the first PyTorch Lightning feedforward training entry point.
- [scripts/training/train_tree_regressor.md](./scripts/training/train_tree_regressor.md)
  Script-level documentation for the tree-based structured-baseline training entry point.
- [scripts/training/run_training_campaign.md](./scripts/training/run_training_campaign.md)
  Script-level documentation for the persistent queue-based batch training runner.
- [scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md](./scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md)
  Script-level documentation for the short Wave 1 recovery campaign launcher.
- [scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md](./scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md)
  Script-level documentation for the canonical Wave 1 residual-harmonic family launcher.
- [scripts/training/validate_training_setup.md](./scripts/training/validate_training_setup.md)
  Script-level documentation for the one-batch validation check used by the shared Wave 0 training infrastructure.
- [scripts/training/run_training_smoke_test.md](./scripts/training/run_training_smoke_test.md)
  Script-level documentation for the minimal Lightning smoke-test entry point used by the shared Wave 0 training infrastructure.
- [scripts/tooling/session/isolated_mode.md](./scripts/tooling/session/isolated_mode.md)
  Script-level documentation for the isolated-session manager that creates locked snapshots, manifest/checklist files, lock-validation reports, and session close-out actions.
- [scripts/tooling/markdown/markdown_style_check.md](./scripts/tooling/markdown/markdown_style_check.md)
  Script-level documentation for the repository-owned Markdown warning checker that scans source `.md` files for blank-line, heading, and single-title issues.
- [scripts/tooling/markdown/run_markdownlint.md](./scripts/tooling/markdown/run_markdownlint.md)
  Script-level documentation for the broader Markdownlint runner that applies the tracked canonical-scope rule profile outside `reference/`.

### Reports

#### Analysis

- [reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md](./reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md)
  Full analytical report for the executed feedforward proof run, including interpretation and comparison against the reference papers.
- [reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md](./reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md)
  Detailed explanation of the training configuration entries, their practical effects, and a comparison between trial, baseline, and heavier workstation-oriented variants.
- [reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf](./reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf)
  PDF export of the detailed training-configuration analysis report and the project golden standard for future styled analytical PDFs.
- [reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md](./reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md)
  Detailed analytical report comparing standard, temporal, hybrid, and PINN model families for the TE case study, including priority and tradeoff analysis.
- [reports/analysis/project_status/[2026-03-27]/Project Status Report.md](./reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Report.md)
  Repository-owned project-status report summarizing completed work, current best results, current objectives, and recommended next steps.
- [reports/analysis/project_status/[2026-03-27]/Project Status Report.pdf](./reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Report.pdf)
  Styled PDF export of the project-status report for stakeholder-friendly review and sharing.
- [reports/analysis/project_status/[2026-03-27]/Project Status Presentation.md](./reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Presentation.md)
  English slide-deck source that summarizes the current repository state and the next execution steps.
- [reports/analysis/project_status/[2026-03-27]/Project Status Presentation.pptx](./reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Presentation.pptx)
  Repository-owned PowerPoint presentation exported from the English Markdown slide deck.
- [reports/analysis/project_status/[2026-03-27]/Project Status Presentation.pdf](./reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Presentation.pdf)
  Slide PDF export of the English project-status presentation for direct sharing and review.
- [reports/analysis/project_status/[2026-03-27]/notebook_lm_assets/notebooklm_video_prompt.md](./reports/analysis/project_status/%5B2026-03-27%5D/notebook_lm_assets/notebooklm_video_prompt.md)
  Ready-to-paste NotebookLM prompt for generating an English project-status video from the grounded repository source package stored under `notebook_lm_assets/`.
- [reports/analysis/project_status/[2026-03-27]/notebook_lm_assets/notebooklm_presentation_prompt.md](./reports/analysis/project_status/%5B2026-03-27%5D/notebook_lm_assets/notebooklm_presentation_prompt.md)
  Ready-to-paste NotebookLM prompt for generating an English project-status presentation from the grounded repository source package stored under `notebook_lm_assets/`.
- [reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.md](./reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.md)
  Lightweight repository-owned validation-check report generated from the one-batch feedforward trial setup validation pass.
- [reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.pdf](./reports/analysis/validation_checks/2026-03-30-10-46-47_feedforward_te_feedforward_trial_skill_operational_test_validation_setup_report.pdf)
  Styled PDF export of the feedforward trial validation-check report.
- [guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md](./guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md)
  Foundational learning guide that explains supervised learning, neurons, MLPs, loss functions, backpropagation, and generalization in the TE project context.
- [guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.pdf](./guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.pdf)
  Styled PDF export of the neural-network foundations learning guide.
- [guide/Neural%20Network%20Foundations/concept_video_package/video_source_brief.md](./guide/Neural%20Network%20Foundations/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the neural-network foundations concept video package.
- [guide/Neural%20Network%20Foundations/project_video_package/video_source_brief.md](./guide/Neural%20Network%20Foundations/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the neural-network foundations project video package.
- [guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md](./guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md)
  Learning guide that explains dataset splits, optimizer-driven training, validation logic, test-set discipline, and TE-specific evaluation pitfalls.
- [guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.pdf](./guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.pdf)
  Styled PDF export of the training, validation, and testing learning guide.
- [guide/Training,%20Validation,%20And%20Testing/concept_video_package/video_source_brief.md](./guide/Training,%20Validation,%20And%20Testing/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the training, validation, and testing concept video package.
- [guide/Training,%20Validation,%20And%20Testing/project_video_package/video_source_brief.md](./guide/Training,%20Validation,%20And%20Testing/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the training, validation, and testing project video package.
- [guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md](./guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md)
  Curriculum guide that introduces the TE model families from feedforward and harmonic baselines through the planned temporal, hybrid, and PINN directions.
- [guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.pdf](./guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.pdf)
  Styled PDF export of the TE model curriculum learning guide.
- [guide/TE%20Model%20Curriculum/concept_video_package/video_source_brief.md](./guide/TE%20Model%20Curriculum/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the TE model curriculum concept video package.
- [guide/TE%20Model%20Curriculum/project_video_package/video_source_brief.md](./guide/TE%20Model%20Curriculum/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the TE model curriculum project video package.
- [guide/FeedForward%20Network/FeedForward%20Network.md](./guide/FeedForward%20Network/FeedForward%20Network.md)
  Learning guide that explains the feedforward architecture as the baseline MLP for the TE curriculum, with implementation and training context.
- [guide/FeedForward%20Network/FeedForward%20Network.pdf](./guide/FeedForward%20Network/FeedForward%20Network.pdf)
  Styled PDF export of the feedforward network learning guide.
- [guide/FeedForward%20Network/concept_video_package/video_source_brief.md](./guide/FeedForward%20Network/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the feedforward-network concept video package.
- [guide/FeedForward%20Network/project_video_package/video_source_brief.md](./guide/FeedForward%20Network/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the feedforward-network project video package.
- [guide/Harmonic%20Regression/Harmonic%20Regression.md](./guide/Harmonic%20Regression/Harmonic%20Regression.md)
  Learning guide that explains harmonic regression as the periodic structured baseline and its repository integration.
- [guide/Harmonic%20Regression/Harmonic%20Regression.pdf](./guide/Harmonic%20Regression/Harmonic%20Regression.pdf)
  Styled PDF export of the harmonic regression learning guide.
- [guide/Harmonic%20Regression/concept_video_package/video_source_brief.md](./guide/Harmonic%20Regression/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the harmonic-regression concept video package.
- [guide/Harmonic%20Regression/project_video_package/video_source_brief.md](./guide/Harmonic%20Regression/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the harmonic-regression project video package.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md)
  Learning guide that explains the periodic-feature hybrid architecture that combines explicit periodic encoding with an MLP backend.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf)
  Styled PDF export of the periodic-feature network learning guide.
- [guide/Periodic%20Feature%20Network/concept_video_package/video_source_brief.md](./guide/Periodic%20Feature%20Network/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the periodic-feature-network concept video package.
- [guide/Periodic%20Feature%20Network/project_video_package/video_source_brief.md](./guide/Periodic%20Feature%20Network/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the periodic-feature-network project video package.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md)
  Learning guide that explains the residual-harmonic hybrid architecture and its structured-plus-residual decomposition.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf)
  Styled PDF export of the residual-harmonic network learning guide.
- [guide/Residual%20Harmonic%20Network/concept_video_package/video_source_brief.md](./guide/Residual%20Harmonic%20Network/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the residual-harmonic-network concept video package.
- [guide/Residual%20Harmonic%20Network/project_video_package/video_source_brief.md](./guide/Residual%20Harmonic%20Network/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the residual-harmonic-network project video package.
- [guide/Multilayer%20Perceptrons/concept_video_package/video_source_brief.md](./guide/Multilayer%20Perceptrons/concept_video_package/video_source_brief.md)
  Neutral NotebookLM-oriented source brief for the Multilayer Perceptrons concept video package.
- [guide/Multilayer%20Perceptrons/project_video_package/video_source_brief.md](./guide/Multilayer%20Perceptrons/project_video_package/video_source_brief.md)
  Repository-specific NotebookLM-oriented source brief for the Multilayer Perceptrons bridge-topic project video package.
- [guide/FeedForward%20Network/FeedForward%20Network.md](./guide/FeedForward%20Network/FeedForward%20Network.md)
  Unified canonical guide for the implemented feedforward TE baseline, combining conceptual framing, strengths and limits, Python model walkthrough, and training-path explanation.
- [guide/FeedForward%20Network/FeedForward%20Network.pdf](./guide/FeedForward%20Network/FeedForward%20Network.pdf)
  Styled PDF export of the unified feedforward model guide.
- [guide/Harmonic%20Regression/Harmonic%20Regression.md](./guide/Harmonic%20Regression/Harmonic%20Regression.md)
  Unified canonical guide for the implemented harmonic-regression TE baseline, combining the harmonic principle, coefficient modes, conceptual framing, and repository integration details.
- [guide/Harmonic%20Regression/Harmonic%20Regression.pdf](./guide/Harmonic%20Regression/Harmonic%20Regression.pdf)
  Styled PDF export of the unified harmonic-regression model guide.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md)
  Unified canonical guide for the implemented periodic-feature TE network, combining periodic feature expansion, conceptual structure, and training integration notes.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf)
  Styled PDF export of the unified periodic-feature network guide.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md)
  Unified canonical guide for the implemented residual-harmonic TE network, combining branch decomposition, hybrid interpretation, auxiliary outputs, and structured-vs-residual training diagnostics.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf)
  Styled PDF export of the unified residual-harmonic network guide.

#### Latest Campaign Plans

- [reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md](./reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md)
  Planning report for the next mixed feedforward campaign that combines longer schedules, denser point sampling, larger batches, and larger models.
- [reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md](./reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md)
  Planning report for the first Wave 1 structured-baseline exploratory campaign across harmonic, periodic-feature, residual, and tree-based model families.
- [reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md](./reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md)
  Planning report for the Wave 1 recovery campaign that reruns the failed harmonic, residual, and random forest branches after the model-aware summary fix.
- [reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md](./reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md)
  Historical-filename planning report for the Wave 1 residual-harmonic familywise follow-up campaign, focused on a broad hyperparameter search inside the residual harmonic MLP family.
- [technical/2026-03/2026-03-20/2026-03-20-15-55-21_campaign_launcher_short_command.md](./technical/2026-03/2026-03-20/2026-03-20-15-55-21_campaign_launcher_short_command.md)
  Technical document for a short launcher wrapper that keeps the existing training logs and terminal behavior intact.
- [technical/2026-03/2026-03-24/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md](./technical/2026-03/2026-03-24/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md)
  Technical document for the final reporting work of the completed Wave 1 structured baseline recovery campaign.
- [technical/2026-03/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_analysis.md](./technical/2026-03/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_analysis.md)
  Integration analysis for recovering the isolated documentation work onto the synchronized repository state.
- [technical/2026-03/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_checklist.md](./technical/2026-03/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_checklist.md)
  Explicit checklist for the isolated-work recovery and the first canonical Sphinx integration steps.
- [technical/2026-03/2026-03-24/2026-03-24-19-40-45_sphinx_batch0_canonical_foundation.md](./technical/2026-03/2026-03-24/2026-03-24-19-40-45_sphinx_batch0_canonical_foundation.md)
  Technical implementation note for the canonical Batch 0 Sphinx foundation.
- [technical/2026-03/2026-03-24/2026-03-24-19-59-54_sphinx_canonical_integration_phase1.md](./technical/2026-03/2026-03-24/2026-03-24-19-59-54_sphinx_canonical_integration_phase1.md)
  Technical implementation note for the first canonical integration phase after the Sphinx foundation batch.
- [technical/2026-03/2026-03-24/2026-03-24-20-05-31_sphinx_canonical_integration_phase2.md](./technical/2026-03/2026-03-24/2026-03-24-20-05-31_sphinx_canonical_integration_phase2.md)
  Technical implementation note for the second canonical integration phase that exposes recovered isolated documentation assets and the styled PDF exporter inside the Sphinx portal.
- [technical/2026-03/2026-03-24/2026-03-24-20-13-56_sphinx_canonical_integration_phase3_core_training_infrastructure.md](./technical/2026-03/2026-03-24/2026-03-24-20-13-56_sphinx_canonical_integration_phase3_core_training_infrastructure.md)
  Technical implementation note for the next canonical Sphinx integration batch focused on the shared training infrastructure API surface.
- [technical/2026-03/2026-03-24/2026-03-24-20-23-49_sphinx_canonical_integration_phase4_model_family_api_coverage.md](./technical/2026-03/2026-03-24/2026-03-24-20-23-49_sphinx_canonical_integration_phase4_model_family_api_coverage.md)
  Technical implementation note for the next canonical Sphinx integration batch focused on model-family API coverage and model-factory routing.
- [technical/2026-03/2026-03-24/2026-03-24-20-58-19_isolated_integration_reconciliation_and_learning_guide_migration.md](./technical/2026-03/2026-03-24/2026-03-24-20-58-19_isolated_integration_reconciliation_and_learning_guide_migration.md)
  Technical reconciliation note for completing the still-open isolated-branch integration work around learning-guide migration and NotebookLM media relocation.
- [technical/2026-03/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md](./technical/2026-03/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md)
  Technical verification note for checking whether any isolated-branch work still remains outside the canonical repository state after reconciliation.
- [technical/2026-03/2026-03-24/2026-03-24-22-51-28_documentation_poc_cleanup_and_archival.md](./technical/2026-03/2026-03-24/2026-03-24-22-51-28_documentation_poc_cleanup_and_archival.md)
  Technical cleanup note for relocating the remaining isolated documentation proof-of-concept artifacts out of the repository root and into an archival location.
- [technical/2026-03/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md](./technical/2026-03/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md)
  Technical cleanup note for retiring the now-empty isolated handoff roots and relocating their remaining provenance artifacts into a dedicated archive subtree.
- [technical/2026-03/2026-03-25/2026-03-25-12-39-38_isolated_mode_rework.md](./technical/2026-03/2026-03-25/2026-03-25-12-39-38_isolated_mode_rework.md)
  Technical design document for replacing the old isolated handoff pattern with explicit session roots, locked-file snapshots, structured manifests, and deterministic integration checklists.
- [technical/2026-03/2026-03-25/2026-03-25-13-03-35_remove_legacy_isolated_handoff_archive.md](./technical/2026-03/2026-03-25/2026-03-25-13-03-35_remove_legacy_isolated_handoff_archive.md)
  Technical cleanup document for preserving only the useful isolated-mode lessons in canonical documentation and removing the legacy `reference/isolated_handoff/` archive subtree.
- [technical/2026-03/2026-03-25/2026-03-25-13-10-20_markdown_warning_cleanup_and_lint_workflow.md](./technical/2026-03/2026-03-25/2026-03-25-13-10-20_markdown_warning_cleanup_and_lint_workflow.md)
  Technical document for cleaning up current Markdown warnings and adding a repository-owned terminal checker so future Markdown files can be validated directly from source.
- [technical/2026-03/2026-03-25/2026-03-25-14-05-16_extended_markdownlint_rule_baseline.md](./technical/2026-03/2026-03-25/2026-03-25-14-05-16_extended_markdownlint_rule_baseline.md)
  Technical document for formalizing the broader Markdownlint baseline, tracked rule policy, and canonical non-`reference/` scope.
- [technical/2026-03/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md](./technical/2026-03/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md)
  Technical document for redesigning the repository README as a GitHub-facing landing page for a new human user.
- [technical/2026-03/2026-03-25/2026-03-25-14-51-40_readme_maintenance_rule.md](./technical/2026-03/2026-03-25/2026-03-25-14-51-40_readme_maintenance_rule.md)
  Technical document for keeping the GitHub-facing README aligned with public repository presentation changes.
- [technical/2026-04/2026-04-02/2026-04-02-14-24-24_readme_landing_page_and_registry_separation_rule.md](./technical/2026-04/2026-04-02/2026-04-02-14-24-24_readme_landing_page_and_registry_separation_rule.md)
  Technical document for keeping `README.md` GitHub-facing while moving detailed technical registries and operational indexes into `doc/`.
- [technical/2026-04/2026-04-02/2026-04-02-14-40-15_skill_frontmatter_bom_compatibility_fix.md](./technical/2026-04/2026-04-02/2026-04-02-14-40-15_skill_frontmatter_bom_compatibility_fix.md)
  Technical document for fixing a UTF-8 BOM regression that broke YAML frontmatter detection in a repository-local Codex skill.
- [technical/2026-04/2026-04-02/2026-04-02-14-49-10_video_source_bundle_git_lfs_dedup_and_renaming.md](./technical/2026-04/2026-04-02/2026-04-02-14-49-10_video_source_bundle_git_lfs_dedup_and_renaming.md)
  Technical document for moving the TwinCAT/TestRig source video bundle into a canonical reference-owned location with Git LFS, deduplication, and clearer naming.
- [technical/2026-04/2026-04-02/2026-04-02-18-16-07_video_guide_canonical_cleanup_and_source_reference_alignment.md](./technical/2026-04/2026-04-02/2026-04-02-18-16-07_video_guide_canonical_cleanup_and_source_reference_alignment.md)
  Technical document for removing legacy duplicate promoted video-guide aliases and aligning the canonical guide tree to the tracked source bundle with explicit source-video provenance.
- [technical/2026-04/2026-04-02/2026-04-02-18-34-16_repository_wide_markdown_warning_elimination_and_policy_alignment.md](./technical/2026-04/2026-04-02/2026-04-02-18-34-16_repository_wide_markdown_warning_elimination_and_policy_alignment.md)
  Technical document for eliminating repository-wide Markdown warnings across Git-tracked authored Markdown files and aligning the documentation surface with a zero-warning policy.
- [technical/2026-04/2026-04-02/2026-04-02-18-40-31_video_guides_markdown_strict_cleanup_and_lint_alignment.md](./technical/2026-04/2026-04-02/2026-04-02-18-40-31_video_guides_markdown_strict_cleanup_and_lint_alignment.md)
  Technical document for hardening the canonical TwinCAT/TestRig video-guide Markdown files against stricter editor linting and aligning them with the repository zero-warning policy.
- [technical/2026-04/2026-04-20/2026-04-20-14-48-45_agents_instruction_slimming_and_persistent_workflow_consolidation.md](./technical/2026-04/2026-04-20/2026-04-20-14-48-45_agents_instruction_slimming_and_persistent_workflow_consolidation.md)
  Technical document for slimming the always-on repository instruction surface, moving specialist workflow policy to on-demand references, and preferring persistent repository-owned command entry points over repeated inline scripting.
- [technical/2026-04/2026-04-20/2026-04-20-15-19-14_technical_document_scaffold_and_index_helper.md](./technical/2026-04/2026-04-20/2026-04-20-15-19-14_technical_document_scaffold_and_index_helper.md)
  Technical document for a lightweight Python helper that creates timestamped technical documents with the required section scaffold and registers them in the day-local index and `doc/README.md`.
- [technical/2026-03/2026-03-25/2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md](./technical/2026-03/2026-03-25/2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md)
  Technical document for separating the canonical `doc/` source tree from the Sphinx portal root by renaming `docs/` to `site/`.
- [technical/2026-03/2026-03-25/2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md](./technical/2026-03/2026-03-25/2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md)
  Technical document for introducing dual `NotebookLM` concept/project video-package tracks and explicit export naming across the guide tree.
- [technical/2026-03/2026-03-25/2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md](./technical/2026-03/2026-03-25/2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md)
  Technical document for making future guide-worthy topics produce the full guide bundle plus the two final ready-to-paste `NotebookLM` prompt files by default.
- [technical/2026-03/2026-03-26/2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md](./technical/2026-03/2026-03-26/2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md)
  Technical document for refining the Wave 1 recovery campaign results PDF page breaks and table column balance.
- [technical/2026-03/2026-03-26/2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md](./technical/2026-03/2026-03-26/2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md)
  Historical-filename technical document for organizing the Wave 1 familywise follow-up optimization program before any tuned cross-family comparison.
- [technical/2026-03/2026-03-26/2026-03-26-14-19-56_campaign_launcher_script_mandatory_rule.md](./technical/2026-03/2026-03-26/2026-03-26-14-19-56_campaign_launcher_script_mandatory_rule.md)
  Technical document for making a dedicated PowerShell launcher and launcher usage note mandatory parts of every prepared training campaign.
- [technical/2026-03/2026-03-27/2026-03-27-12-24-15_backlog_and_documentation_integration_for_twincat_deployment_tracks.md](./technical/2026-03/2026-03-27/2026-03-27-12-24-15_backlog_and_documentation_integration_for_twincat_deployment_tracks.md)
  Technical note for integrating the approved TwinCAT deployment-evaluation plan into the operational backlog and documentation indexes.
- [technical/2026-03/2026-03-27/2026-03-27-12-44-18_readme_md012_final_check_rule.md](./technical/2026-03/2026-03-27/2026-03-27-12-44-18_readme_md012_final_check_rule.md)
  Technical note for making the README `MD012` repeated-blank-line check an explicit final-pass documentation rule.
- [technical/2026-03/2026-03-27/2026-03-27-12-45-14_markdown_warning_final_check_rule_for_created_and_modified_docs.md](./technical/2026-03/2026-03-27/2026-03-27-12-45-14_markdown_warning_final_check_rule_for_created_and_modified_docs.md)
  Technical note for requiring Markdown warning checks on repository-owned Markdown files created or modified by a task.
- [technical/2026-03/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive.md](./technical/2026-03/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive.md)
  Canonical archive of the existing `concept_video_package` NotebookLM commands, plus the reusable bilingual template for future topics.
- [technical/2026-03/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive_and_reuse_template.md](./technical/2026-03/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive_and_reuse_template.md)
  Technical rationale for converting the temporary concept-video command list into a canonical archive and reusable future-topic template.
- [technical/2026-03/2026-03-27/2026-03-27-12-58-39_editor_markdown_ignore_for_tools_directory.md](./technical/2026-03/2026-03-27/2026-03-27-12-58-39_editor_markdown_ignore_for_tools_directory.md)
  Technical note for reducing editor-side Markdown warning noise from the local `.tools/` helper directory while keeping canonical repository lint behavior unchanged.

#### 2026-03-30

- [technical/2026-03/2026-03-30/2026-03-30-11-41-57_wave1_closeout_audit_and_summary_report.md](./technical/2026-03/2026-03-30/2026-03-30-11-41-57_wave1_closeout_audit_and_summary_report.md)
  Technical document for auditing the remaining `Wave 1` closeout work and preparing the consolidated final summary report.
- [technical/2026-03/2026-03-30/2026-03-30-12-03-06_doc_reports_reorganization_alignment_and_naming_rule.md](./technical/2026-03/2026-03-30/2026-03-30-12-03-06_doc_reports_reorganization_alignment_and_naming_rule.md)
  Technical document for analyzing the manual `doc/reports/` reorganization and planning the documentation realignment around the new structure.
- [technical/2026-03/2026-03-30/2026-03-30-12-04-47_doc_reports_topic_root_and_readable_filename_rule.md](./technical/2026-03/2026-03-30/2026-03-30-12-04-47_doc_reports_topic_root_and_readable_filename_rule.md)
  Technical rule document for the new `doc/reports/` topic-root, dated-bundle, and readable-filename convention.

#### Campaign Results

- [reports/campaign_results/2026-04-17-18-33-39_track1_svm_exact_faithful_final_attempt_campaign_results_report.md](./reports/campaign_results/2026-04-17-18-33-39_track1_svm_exact_faithful_final_attempt_campaign_results_report.md)
  Final results report for the completed strict paper-faithful `SVR` final
  attempt on the residual `SVM` yellow cells, including the repeated plateau
  confirmation and the validated PDF closeout.
- [reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md](./reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md)
  Final results report for the completed exact-paper RCIM family-bank campaign,
  including strict-reference promotion, `SVR` surrogate diagnostics, and the
  validated exact-paper export-status outcome.
- [reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md](./reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md)
  Final results report for the completed `Track 1` exact-paper open-cell
  repair campaign, including paper-table closure status, harmonic-state
  changes, and the explicit confirmation that no new numeric paper cells were
  closed.
- [reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md](./reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md)
  Final results report for the completed second `Track 1` paper-faithful harmonic-wise campaign, including reduced-set diagnostics, full-RCIM comparison, and the updated `Target A` status.
- [reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md](./reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md)
  Comparative results report for the executed baseline, high-density, high-epoch, and high-compute feedforward training campaign.
- [reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md](./reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md)
  Final results report for the completed mixed feedforward campaign, including the recommended best-training preset selection.
- [reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md](./reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md)
  Final results report for the completed Wave 1 recovery campaign, including campaign ranking, family-level outcomes, and program-level context.
- [reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md](./reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md)
  Final results report for the completed Wave 1 residual-harmonic family optimization campaign, including familywise ranking and the promoted residual-family winner.

#### Campaign Plans

- [reports/campaign_plans/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md](./reports/campaign_plans/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md)
  Planning report for deciding whether one final exact-faithful `SVR` rerun
  package is still justified for the residual `SVM` yellow cells.
- [reports/campaign_plans/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md](./reports/campaign_plans/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md)
  Planning report for the next umbrella `Track 1` campaign package, organized
  as family-by-family amplitude and phase reproduction runs for the full
  paper-matrix objective.
- [reports/campaign_plans/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md](./reports/campaign_plans/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md)
  Planning report for the next `Track 1` exact-paper open-cell repair
  campaign, centered on the still-open cells and harmonic states in canonical
  Tables `3-6`.
- [reports/campaign_plans/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md](./reports/campaign_plans/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md)
  Planning report for the first exact-paper RCIM family-bank batch campaign,
  including diagnostic and strict-reference runs, export-failure handling
  strategy, and the intended PowerShell launcher workflow.

### Running State

- [running/te_model_live_backlog.md](./running/te_model_live_backlog.md)
  Privileged live backlog for the TE model implementation program, including current wave status, next steps, deferred branches, and future TwinCAT deployment-track decisions.
- [running/README.md](./running/README.md)
  Explanation of the persistent running-state workflow, including the live backlog and active campaign tracking.
- [running/active_training_campaign.yaml](./running/active_training_campaign.yaml)
  Current prepared or active training campaign state, including protected files and launch commands.

### Guides

- [guide/project_usage_guide.md](./guide/project_usage_guide.md)
  Practical user guide for environment activation, dataset processing, and TE visualization.
- [guide/Codex Repo-Local Workflow/Codex Repo-Local Workflow.md](./guide/Codex%20Repo-Local%20Workflow/Codex%20Repo-Local%20Workflow.md)
  Practical user guide for the repository-local Codex skill and subagent system.
- [guide/Transmission Error Foundations/README.md](./guide/Transmission%20Error%20Foundations/README.md)
  Onboarding-oriented bilingual presentation and video bundle that explains transmission error foundations, measurement motivation, and the TE modeling roadmap for new students.
- [guide/Harmonic-Wise Paper Reimplementation Pipeline/Harmonic-Wise Paper Reimplementation Pipeline.md](./guide/Harmonic-Wise%20Paper%20Reimplementation%20Pipeline/Harmonic-Wise%20Paper%20Reimplementation%20Pipeline.md)
  Guide-local explanation of the paper-faithful harmonic-wise pipeline, including diagrams and NotebookLM source packages for future video-guide and presentation workflows.
- [technical/2026-04/2026-04-09/2026-04-09-12-47-17_harmonic_wise_pipeline_guide_and_notebooklm_package.md](./technical/2026-04/2026-04-09/2026-04-09-12-47-17_harmonic_wise_pipeline_guide_and_notebooklm_package.md)
  Technical plan for the guide-local documentation, diagrams, PDF companion, and NotebookLM source packages for the harmonic-wise paper-reimplementation pipeline.
- [technical/2026-04/2026-04-09/2026-04-09-16-42-43_notebooklm_export_integration_for_harmonic_wise_guide.md](./technical/2026-04/2026-04-09/2026-04-09-16-42-43_notebooklm_export_integration_for_harmonic_wise_guide.md)
  Technical plan for importing, renaming, and canonically placing the generated NotebookLM concept and project exports for the harmonic-wise guide.
- [technical/2026-04/2026-04-09/2026-04-09-17-55-53_remove_redundant_language_suffixes_from_guide_exports.md](./technical/2026-04/2026-04-09/2026-04-09-17-55-53_remove_redundant_language_suffixes_from_guide_exports.md)
  Technical plan for removing redundant language suffixes from imported NotebookLM exports already organized under the English and Italiano guide folders.
- [technical/2026-04/2026-04-09/2026-04-09-18-06-16_bilingual_notebooklm_export_filename_convention.md](./technical/2026-04/2026-04-09/2026-04-09-18-06-16_bilingual_notebooklm_export_filename_convention.md)
  Technical plan for clarifying that imported bilingual NotebookLM exports should not repeat the language in filenames when the parent folder already declares it.
- [technical/2026-04/2026-04-09/2026-04-09-18-31-24_track1_second_harmonic_wise_iteration.md](./technical/2026-04/2026-04-09/2026-04-09-18-31-24_track1_second_harmonic_wise_iteration.md)
  Technical plan for the second Track 1 harmonic-wise iteration, including progressive harmonic-set experiments, feature engineering, and promotion back to the full RCIM harmonic set.
- [technical/2026-04/2026-04-09/2026-04-09-18-56-03_track1_second_iteration_campaign_preparation.md](./technical/2026-04/2026-04-09/2026-04-09-18-56-03_track1_second_iteration_campaign_preparation.md)
  Technical plan for packaging the second Track 1 harmonic-wise iteration as a dedicated operator-driven campaign with configs, launcher, launcher note, and persistent campaign state.
- [technical/2026-04/2026-04-09/2026-04-09-21-41-11_track1_second_iteration_campaign_pdf_table_refinement.md](./technical/2026-04/2026-04-09/2026-04-09-21-41-11_track1_second_iteration_campaign_pdf_table_refinement.md)
  Technical plan for refining the `Ranked Completed Runs` table layout in the Track 1 second-iteration campaign PDF and formalizing the unit-wrapping preference.
- [technical/2026-04/2026-04-09/2026-04-09-21-43-01_pdf_metric_header_unit_wrapping_rule.md](./technical/2026-04/2026-04-09/2026-04-09-21-43-01_pdf_metric_header_unit_wrapping_rule.md)
  Technical plan for making metric-unit second-line wrapping an explicit default rule for narrow styled-PDF metric headers.
- [technical/2026-04/2026-04-09/2026-04-09-21-49-49_track1_second_iteration_campaign_pdf_objective_pagebreak_refinement.md](./technical/2026-04/2026-04-09/2026-04-09-21-49-49_track1_second_iteration_campaign_pdf_objective_pagebreak_refinement.md)
  Technical plan for tightening the `Objective And Outcome` bullets so the Track 1 second-iteration campaign PDF avoids a weak section start on a nearly empty page.
- [technical/2026-04/2026-04-09/2026-04-09-21-53-17_track1_second_iteration_campaign_pdf_rank_column_rebalance.md](./technical/2026-04/2026-04-09/2026-04-09-21-53-17_track1_second_iteration_campaign_pdf_rank_column_rebalance.md)
  Technical plan for slightly widening the `Rank` column and correspondingly shrinking `Test MAE` in the Track 1 second-iteration campaign PDF table.
- [technical/2026-04/2026-04-09/2026-04-09-22-10-21_track1_campaign_random_forest_bundle_git_lfs_tracking.md](./technical/2026-04/2026-04-09/2026-04-09-22-10-21_track1_campaign_random_forest_bundle_git_lfs_tracking.md)
  Technical plan for tracking the oversized RandomForest harmonic-wise campaign bundle through Git LFS so the pending commit remains GitHub-safe.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` as the visual golden standard for future styled analytical PDF reports.
- Treat `reference_summaries/06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Use `reference_codes/` when a future implementation task needs repository-specific examples instead of only high-level style rules.
- Keep this index updated whenever new project documents are added.
