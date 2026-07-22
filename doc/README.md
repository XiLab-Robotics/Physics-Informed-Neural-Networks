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
  implications for RCIM Model-Bank Reproduction and future deployment work.

- [reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md](./reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md)
  Canonical verified reference for the raw, simplified, and polished
  transmission-error datasets, including lineage, schemas, equations, audit
  results, and future-use guidance.

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

- [technical/2026-07/2026-07-06/2026-07-06-14-28-29_dataset_separated_model_artifact_roots.md](./technical/2026-07/2026-07-06/2026-07-06-14-28-29_dataset_separated_model_artifact_roots.md)
  Technical plan for separating curated model artifacts into explicit
  `models/polished_dataset/` and `models/simplified_dataset/` roots while
  preserving existing compatibility paths.

- [technical/2026-07/2026-07-06/2026-07-06-14-47-17_hard_dataset_model_archive_migration.md](./technical/2026-07/2026-07-06/2026-07-06-14-47-17_hard_dataset_model_archive_migration.md)
  Corrected technical plan for the strict dataset-first model archive
  migration, removing duplicate top-level model roots and generating missing
  polished model-development exports from completed campaign checkpoints.

- [technical/2026-07/2026-07-06/2026-07-06-18-38-10_model_family_pruning_decision_report.md](./technical/2026-07/2026-07-06/2026-07-06-18-38-10_model_family_pruning_decision_report.md)
  Technical plan for a forward-led, backward-checked TE model-family pruning
  decision report that pauses `global` model selection and records keep,
  pause, baseline-only, or retire decisions for active model families.

- [technical/2026-07/2026-07-06/2026-07-06-19-38-18_reduced_track2_selected_models_pipeline.md](./technical/2026-07/2026-07-06/2026-07-06-19-38-18_reduced_track2_selected_models_pipeline.md)
  Technical plan for integrating the selected-model pruning decision into a
  reduced `TE Curve Verification Pipeline` that generates only polished and
  simplified forward/backward reports while pausing `global`, overlay, collage,
  and dataset-difference report generation by default.

- [technical/2026-07/2026-07-06/2026-07-06-23-33-02_selected_track2_visual_pdf_reports.md](./technical/2026-07/2026-07-06/2026-07-06-23-33-02_selected_track2_visual_pdf_reports.md)
  Technical plan for regenerating the four reduced selected-model reports as
  visual PDF deliverables with measured-versus-predicted curve collages and
  stable Track 2 table layout rules.

- [technical/2026-07/2026-07-07/2026-07-07-00-47-35_track2_dataset_matched_selected_reports.md](./technical/2026-07/2026-07-07/2026-07-07-00-47-35_track2_dataset_matched_selected_reports.md)
  Technical plan for correcting the reduced selected-model reports so polished
  and simplified reports use dataset-matched model candidates and shared
  four-curve evidence sets per direction.

- [technical/2026-07/2026-07-07/2026-07-07-01-46-06_dataset_input_mode_retraining_campaigns.md](./technical/2026-07/2026-07-07/2026-07-07-01-46-06_dataset_input_mode_retraining_campaigns.md)
  Technical plan for the Aries retraining program that separates
  `simplified_dataset` setpoints, `polished_dataset` setpoints, and
  `polished_dataset` actual-value model artifacts.

- [technical/2026-07/2026-07-07/2026-07-07-02-49-01_actual_values_direction_flag_alignment.md](./technical/2026-07/2026-07-07/2026-07-07-02-49-01_actual_values_direction_flag_alignment.md)
  Technical plan for aligning `polished_dataset` actual-values inputs to the
  same five-feature width used by setpoint-based retraining paths.

- [technical/2026-07/2026-07-07/2026-07-07-11-46-14_familywise_track2_onnx_report_pipeline.md](./technical/2026-07/2026-07-07/2026-07-07-11-46-14_familywise_track2_onnx_report_pipeline.md)
  Technical plan for a familywise `TE Curve Verification Pipeline` ONNX report
  that evaluates dataset/input-mode matched exported models and produces
  configurable forward, backward, and global curve pages.

- [technical/2026-07/2026-07-08/2026-07-08-11-21-45_familywise_sequence_onnx_report_support.md](./technical/2026-07/2026-07-08/2026-07-08-11-21-45_familywise_sequence_onnx_report_support.md)
  Technical plan for extending the familywise ONNX report builder to handle
  sequence-model exports such as `temporal_convolution` while preserving the
  existing point-model report path.

- [reports/analysis/te_curve_verification_pipeline/03_family_reports/tree/[2026-07-07]/track2_tree_familywise_onnx_report.md](./reports/analysis/te_curve_verification_pipeline/03_family_reports/tree/%5B2026-07-07%5D/track2_tree_familywise_onnx_report.md)
  Familywise `tree` ONNX verification report comparing the completed
  simplified setpoint, polished setpoint, and polished actual-value exports
  with 12-curve forward, backward, and global collage pages.

- [technical/2026-07/2026-07-13/2026-07-13-16-31-32_rcim_track1_polished_input_mode_retraining.md](./technical/2026-07/2026-07-13/2026-07-13-16-31-32_rcim_track1_polished_input_mode_retraining.md)
  Technical plan for retraining only the two missing `rcim_track1`
  polished-dataset input-mode campaigns while freezing the audited
  `simplified_dataset` paper-reference baseline.

- [technical/2026-07/2026-07-17/2026-07-17-11-51-04_intermediate_model_selection_cleanup.md](./technical/2026-07/2026-07-17/2026-07-17-11-51-04_intermediate_model_selection_cleanup.md)
  Technical plan for the intermediate post-retraining model-selection cleanup
  report that keeps both temporal-window and non-windowed development paths
  while closing dead-end exploratory branches.

- [technical/2026-07/2026-07-17/2026-07-17-16-43-13_sphinx_pages_build_repair.md](./technical/2026-07/2026-07-17/2026-07-17-16-43-13_sphinx_pages_build_repair.md)
  Technical plan for repairing the GitHub Pages Sphinx build by aligning the
  documentation dependency set and the Pages workflow GitHub Actions versions.

- [technical/2026-07/2026-07-19/2026-07-19-12-05-00_rcim_track1_polished_actual_values_closeout.md](./technical/2026-07/2026-07-19/2026-07-19-12-05-00_rcim_track1_polished_actual_values_closeout.md)
  Closeout for the Aries `rcim_track1` polished actual-values campaign,
  including Slurm terminal status, archive promotion, and artifact checks.

- [technical/2026-07/2026-07-19/2026-07-19-13-20-00_aries_training_operational_runbook.md](./technical/2026-07/2026-07-19/2026-07-19-13-20-00_aries_training_operational_runbook.md)
  Operational runbook for Aries training work, covering normal GPU campaigns,
  the CPU/RAM `rcim_track1` paper-bank pipeline, Slurm cleanup, promotion, and
  Git LFS handling.

- [technical/2026-07/2026-07-19/2026-07-19-14-56-02_rcim_track1_familywise_track2_report.md](./technical/2026-07/2026-07-19/2026-07-19-14-56-02_rcim_track1_familywise_track2_report.md)
  Technical plan for extending the familywise `TE Curve Verification Pipeline`
  report path to evaluate `rcim_track1` paper-reference model-bank archives.

- [technical/2026-07/2026-07-19/2026-07-19-17-07-20_rcim_track1_retuned_best_familywise_report.md](./technical/2026-07/2026-07-19/2026-07-19-17-07-20_rcim_track1_retuned_best_familywise_report.md)
  Technical plan for refreshing the `rcim_track1` familywise report with the
  selected retuned polished surface composition.

- [technical/2026-07/2026-07-19/2026-07-19-17-15-50_selected_models_track2_full_report_refresh.md](./technical/2026-07/2026-07-19/2026-07-19-17-15-50_selected_models_track2_full_report_refresh.md)
  Technical plan for regenerating a complete selected-model
  `TE Curve Verification Pipeline` report using only the shape-first active
  model set and reference anchors.

- [technical/2026-07/2026-07-19/2026-07-19-18-37-50_selected_active_pdf_layout_fix.md](./technical/2026-07/2026-07-19/2026-07-19-18-37-50_selected_active_pdf_layout_fix.md)
  Technical plan for fixing selected-active `TE Curve Verification Pipeline`
  PDF page breaks and table column widths.

- [technical/2026-07/2026-07-19/2026-07-19-21-27-56_models_archive_path_simplification.md](./technical/2026-07/2026-07-19/2026-07-19-21-27-56_models_archive_path_simplification.md)
  Technical plan for shortening the curated `models/` archive layout by
  removing redundant `exported/` and timestamped run-directory levels while
  preserving leaf `reference_inventory.yaml` provenance.

- [technical/2026-07/2026-07-20/2026-07-20-00-42-54_selected_report_markdownlint_spacing_fix.md](./technical/2026-07/2026-07-20/2026-07-20-00-42-54_selected_report_markdownlint_spacing_fix.md)
  Technical plan for repairing `MD032` list-spacing failures in selected-model
  `TE Curve Verification Pipeline` reports.

- [technical/2026-07/2026-07-20/2026-07-20-11-33-31_rcim_track1_offset_crosscheck.md](./technical/2026-07/2026-07-20/2026-07-20-11-33-31_rcim_track1_offset_crosscheck.md)
  Technical plan for cross-checking the latest `RCIM Model-Bank Reproduction`
  retraining offset behavior against simplified, retuned, and original paper
  reference paths.

- [technical/2026-07/2026-07-20/2026-07-20-15-08-33_rcim_track1_retrained_paper_tables_report.md](./technical/2026-07/2026-07-20/2026-07-20-15-08-33_rcim_track1_retrained_paper_tables_report.md)
  Technical plan for generating paper Tables 2-5 equivalents from retrained
  `rcim_track1` model-bank archives across simplified, polished setpoint, and
  polished actual-value datasets.

- [technical/2026-07/2026-07-20/2026-07-20-16-16-28_shape_gated_te_curve_reranker.md](./technical/2026-07/2026-07-20/2026-07-20-16-16-28_shape_gated_te_curve_reranker.md)
  Technical plan for a reduced forward/backward shape-gated
  `TE Curve Verification Pipeline` reranker that keeps scalar-error leaders
  subordinate to curve-shape, harmonic, phase, derivative, offset, and
  per-curve pass-rate evidence.

- [technical/2026-07/2026-07-20/2026-07-20-17-37-46_shape_gate_calibration_and_training_loss_backlog.md](./technical/2026-07/2026-07-20/2026-07-20-17-37-46_shape_gate_calibration_and_training_loss_backlog.md)
  Technical plan for calibrating the strict shape gate so it remains a strong
  model screener without rejecting every candidate, and for recording future
  evaluation of shape, harmonic, phase, offset, and derivative-aware training
  losses.

- [technical/2026-07/2026-07-20/2026-07-20-18-10-35_shape_gate_loss_pilot_and_full_surface_campaign.md](./technical/2026-07/2026-07-20/2026-07-20-18-10-35_shape_gate_loss_pilot_and_full_surface_campaign.md)
  Technical plan for using `polished_dataset` setpoint forward training as the
  first shape-gate loss pilot while preserving the full promotion rule across
  simplified setpoints, polished setpoints, polished actual values, and
  `global` / `Fw` / `Bw` surfaces.

- [reports/campaign_plans/cross_wave/shape_gate_loss/2026-07-20-19-10-23_shape_gate_loss_pilot_campaign_plan_report.md](./reports/campaign_plans/cross_wave/shape_gate_loss/2026-07-20-19-10-23_shape_gate_loss_pilot_campaign_plan_report.md)
  Campaign plan for the one-run shape-gate loss pilot on `polished_dataset`
  setpoints `Fw`, with full promotion deferred until a later three-target,
  three-surface Aries campaign.

- [scripts/campaigns/cross_wave/run_shape_gate_loss_pilot_campaign.md](./scripts/campaigns/cross_wave/run_shape_gate_loss_pilot_campaign.md)
  Launcher note for validating or launching the shape-gate loss pilot locally
  or through the repository-owned remote campaign workflow.

- [reports/analysis/validation_checks/2026-07-20-19-34-33_shape_ga_a3f8de47_te_shape_gate_loss_period_aa0a58de_validation_setup_report.md](./reports/analysis/validation_checks/2026-07-20-19-34-33_shape_ga_a3f8de47_te_shape_gate_loss_period_aa0a58de_validation_setup_report.md)
  One-batch validation report for the `polished_dataset` setpoint `Fw`
  shape-gate loss pilot configuration.

- [reports/campaign_results/cross_wave/shape_gate_loss/2026-07-20-20-12-45_shape_gate_loss_pilot_campaign_results_report.md](./reports/campaign_results/cross_wave/shape_gate_loss/2026-07-20-20-12-45_shape_gate_loss_pilot_campaign_results_report.md)
  Final results report for the completed one-run shape-gate loss pilot on
  `polished_dataset` setpoints `Fw`, including manual remote artifact recovery,
  scalar baseline comparison, and the decision not to promote before a
  checkpoint-level shape-gated reranker pass.

- [technical/2026-07/2026-07-20/2026-07-20-23-31-11_shape_gate_loss_pilot_track2_shape_evaluation.md](./technical/2026-07/2026-07-20/2026-07-20-23-31-11_shape_gate_loss_pilot_track2_shape_evaluation.md)
  Technical plan for evaluating the completed shape-gate loss pilot checkpoint
  inside the shape-gated `TE Curve Verification Pipeline` and attempting
  Track 2 visual generation without promoting from scalar campaign metrics.

- [reports/campaign_results/track_2/verification_plots/shape_gate_loss_pilot_track2_polished_setpoints_fw/track2_candidate_curve_plot_summary.yaml](./reports/campaign_results/track_2/verification_plots/shape_gate_loss_pilot_track2_polished_setpoints_fw/track2_candidate_curve_plot_summary.yaml)
  Summary for the bounded Track 2 truth-versus-prediction PNG plots generated
  from the shape-gate loss pilot checkpoint.

- [technical/2026-07/2026-07-21/2026-07-21-00-01-30_shape_gate_pilot_track2_playback_contract_audit.md](./technical/2026-07/2026-07-21/2026-07-21-00-01-30_shape_gate_pilot_track2_playback_contract_audit.md)
  Technical plan for auditing the checkpoint-to-Track-2 playback contract
  behind the shape-gate loss pilot's offset-dominated full-curve failure.

- [reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-19-31_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_input_mode_fixed_report.md](./reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-19-31_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_input_mode_fixed_report.md)
  Corrected pilot-only `TE Curve Verification Pipeline` comparison report for
  the completed shape-gate loss checkpoint on `polished_dataset` setpoint
  `forward` curves, after fixing lightweight Track 2 input-mode propagation.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-21]/shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gated_te_curve_reranker_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/%5B2026-07-21%5D/shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gated_te_curve_reranker_report.md)
  Corrected shape-gated reranker result for the shape-gate loss pilot
  checkpoint, recording a forward-only recommended-candidate decision after
  fixing polished setpoint input-mode playback.

- [../output/validation_checks/shape_gate_pilot_track2_playback_contract_audit/2026-07-21-00-21-30_full_patched/shape_gate_pilot_track2_playback_contract_audit.md](../output/validation_checks/shape_gate_pilot_track2_playback_contract_audit/2026-07-21-00-21-30_full_patched/shape_gate_pilot_track2_playback_contract_audit.md)
  Full playback-contract audit proving that the earlier offset-dominated Track
  2 failure came from polished input-mode drift, not from the checkpoint.

- [technical/2026-07/2026-07-21/2026-07-21-00-35-29_shape_gate_pilot_patched_polished_setpoints_expansion.md](./technical/2026-07/2026-07-21/2026-07-21-00-35-29_shape_gate_pilot_patched_polished_setpoints_expansion.md)
  Technical plan for a patched polished-setpoint Fw/Bw expansion test after
  correcting the shape-gate pilot Track 2 input-mode playback contract.

- [technical/2026-07/2026-07-21/2026-07-21-09-53-39_track2_sorted_angular_plot_guard.md](./technical/2026-07/2026-07-21/2026-07-21-09-53-39_track2_sorted_angular_plot_guard.md)
  Technical plan for enforcing sorted `0` to `360` degree angular positions in
  Track 2 plotting helpers before rendering measured and predicted TE curves.

- [technical/2026-07/2026-07-21/2026-07-21-12-18-54_shape_gate_loss_v2_checkpoint_selection_pilot.md](./technical/2026-07/2026-07-21/2026-07-21-12-18-54_shape_gate_loss_v2_checkpoint_selection_pilot.md)
  Technical plan for a stricter second shape-gate pilot that treats
  derivative, ripple, harmonic, offset, and per-curve pass-rate metrics as
  checkpoint-selection evidence before any full Aries matrix campaign.

- [technical/2026-07/2026-07-21/2026-07-21-14-59-55_campaign_results_pdf_table_width_fix.md](./technical/2026-07/2026-07-21/2026-07-21-14-59-55_campaign_results_pdf_table_width_fix.md)
  Technical plan for permanent styled-PDF table-width rules covering campaign
  metric-breakdown and pilot-comparison tables.

- [technical/2026-07/2026-07-21/2026-07-21-15-20-56_shape_gate_loss_v2_bounded_track2_screen.md](./technical/2026-07/2026-07-21/2026-07-21-15-20-56_shape_gate_loss_v2_bounded_track2_screen.md)
  Technical plan for a bounded `TE Curve Verification Pipeline` screen of the
  completed shape-gate loss v2 checkpoint before any full-matrix expansion.

- [technical/2026-07/2026-07-21/2026-07-21-18-36-30_parallel_shape_objective_followup.md](./technical/2026-07/2026-07-21/2026-07-21-18-36-30_parallel_shape_objective_followup.md)
  Technical plan for a bounded three-arm follow-up that compares windowed,
  non-windowed, and curve-aware shape-objective candidates before any full
  expansion.

- [technical/2026-07/2026-07-21/2026-07-21-20-34-26_pilot_track2_curve_plot_report_fix.md](./technical/2026-07/2026-07-21/2026-07-21-20-34-26_pilot_track2_curve_plot_report_fix.md)
  Technical plan for correcting pilot closeout reports so the pilot graph
  bundle uses Track 2 measured-versus-predicted TE curve evidence instead of
  scalar-only summary plots.

- [technical/2026-07/2026-07-21/2026-07-21-20-51-39_campaign_pdf_section_pagebreak_rules.md](./technical/2026-07/2026-07-21/2026-07-21-20-51-39_campaign_pdf_section_pagebreak_rules.md)
  Technical plan for permanent campaign styled-PDF page-break rules covering
  `Execution Summary` and the opening `Pilot Graphs` Track 2 plot block.

- [technical/2026-07/2026-07-22/2026-07-22-12-06-03_shape_objective_bounded_track2_screen.md](./technical/2026-07/2026-07-22/2026-07-22-12-06-03_shape_objective_bounded_track2_screen.md)
  Technical plan for the bounded forward `TE Curve Verification Pipeline`
  screen of the shape-objective periodic MLP harmonic pilot winner before any
  promotion decision.

- [technical/2026-07/2026-07-22/2026-07-22-12-54-02_shape_first_training_rule_distillation.md](./technical/2026-07/2026-07-22/2026-07-22-12-54-02_shape_first_training_rule_distillation.md)
  Technical plan for distilling `TE Curve Verification Pipeline`
  shape-first screen rules into training diagnostics, checkpoint-selection
  monitors, and conservative auxiliary-loss candidates without treating the
  failed shape-objective branch as promoted evidence.

- [technical/2026-07/2026-07-22/2026-07-22-15-14-36_remote_training_stream_completion_fix.md](./technical/2026-07/2026-07-22/2026-07-22-15-14-36_remote_training_stream_completion_fix.md)
  Technical plan for fixing completed LAN-remote training campaigns that leave
  the local operator terminal stuck in `remote_run` before artifact sync-back.

- [reports/campaign_plans/cross_wave/shape_gate_loss_v2/2026-07-21-12-21-36_shape_gate_loss_v2_checkpoint_selection_pilot_campaign_plan_report.md](./reports/campaign_plans/cross_wave/shape_gate_loss_v2/2026-07-21-12-21-36_shape_gate_loss_v2_checkpoint_selection_pilot_campaign_plan_report.md)
  Campaign plan for the one-run `polished_dataset` setpoint `Fw` shape-gate
  loss v2 checkpoint-selection pilot.

- [reports/campaign_plans/cross_wave/shape_gate_loss_v2/2026-07-21-15-20-56_shape_gate_loss_v2_bounded_track2_screen_plan_report.md](./reports/campaign_plans/cross_wave/shape_gate_loss_v2/2026-07-21-15-20-56_shape_gate_loss_v2_bounded_track2_screen_plan_report.md)
  Plan for a bounded `polished_dataset` setpoint `Fw`
  `TE Curve Verification Pipeline` screen of the completed shape-gate loss v2
  checkpoint.

- [reports/campaign_plans/cross_wave/shape_objective/2026-07-21-18-36-30_parallel_shape_objective_followup_campaign_plan_report.md](./reports/campaign_plans/cross_wave/shape_objective/2026-07-21-18-36-30_parallel_shape_objective_followup_campaign_plan_report.md)
  Campaign plan for a three-arm bounded shape-objective follow-up comparing
  windowed, non-windowed, and curve-aware candidates on `polished_dataset`
  setpoint `Fw`.

- [reports/campaign_plans/cross_wave/shape_objective/2026-07-22-12-06-03_shape_objective_bounded_track2_screen_plan_report.md](./reports/campaign_plans/cross_wave/shape_objective/2026-07-22-12-06-03_shape_objective_bounded_track2_screen_plan_report.md)
  Plan for a bounded `polished_dataset` setpoint `Fw`
  `TE Curve Verification Pipeline` screen of the shape-objective periodic MLP
  harmonic pilot winner against windowed and non-windowed polished baselines.

- [reports/campaign_plans/cross_wave/shape_first_training_rule_distillation/2026-07-22-13-14-28_shape_first_training_rule_distillation_pilot_campaign_plan_report.md](./reports/campaign_plans/cross_wave/shape_first_training_rule_distillation/2026-07-22-13-14-28_shape_first_training_rule_distillation_pilot_campaign_plan_report.md)
  Campaign plan for a two-arm shape-first training-rule distillation mini-pilot
  that keeps one time-windowed and one non-windowed `polished_dataset` setpoint
  `Fw` candidate in scope.

- [scripts/campaigns/cross_wave/run_parallel_shape_objective_followup_campaign.md](./scripts/campaigns/cross_wave/run_parallel_shape_objective_followup_campaign.md)
  Launcher note for validating or launching the three-arm shape-objective
  follow-up locally or through the repository-owned remote campaign workflow.

- [scripts/campaigns/cross_wave/run_shape_first_training_rule_distillation_pilot_campaign.md](./scripts/campaigns/cross_wave/run_shape_first_training_rule_distillation_pilot_campaign.md)
  Launcher note for validating or launching the two-arm shape-first
  training-rule distillation pilot locally or through the remote campaign
  workflow.

- [reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.md](./reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.md)
  Final results report for the completed two-arm shape-first training-rule
  distillation pilot, including the remote stream recovery note, scalar
  winner, time-windowed versus non-windowed comparison, and bounded
  curve-first next step.

- [reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.pdf](./reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.pdf)
  Styled PDF export of the shape-first training-rule distillation pilot
  closeout report.

- [scripts/campaigns/cross_wave/run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.md](./scripts/campaigns/cross_wave/run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.md)
  Launcher note for validating or launching the shape-gate loss v2
  checkpoint-selection pilot locally or through the remote campaign workflow.

- [scripts/campaigns/track_2/run_shape_gate_loss_v2_bounded_track2_screen.md](./scripts/campaigns/track_2/run_shape_gate_loss_v2_bounded_track2_screen.md)
  Launcher note for the bounded `polished_dataset` setpoint `Fw`
  `TE Curve Verification Pipeline` screen of the shape-gate loss v2 checkpoint.

- [scripts/campaigns/track_2/run_shape_objective_bounded_track2_screen.md](./scripts/campaigns/track_2/run_shape_objective_bounded_track2_screen.md)
  Launcher note for the bounded `polished_dataset` setpoint `Fw`
  `TE Curve Verification Pipeline` screen of the shape-objective periodic MLP
  harmonic pilot winner.

- [../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw_matrix.yaml](../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw_matrix.yaml)
  Forward-only comparison matrix for the bounded shape-gate loss v2 screen,
  covering the v2 registry candidate, the prior shape-gate loss pilot, and
  polished-setpoint forward exported baselines.

- [../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix.yaml](../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix.yaml)
  Forward-only comparison matrix for the bounded shape-objective screen,
  covering the periodic MLP harmonic pilot winner and the required windowed and
  non-windowed polished-setpoint baselines.

- [../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix.yaml](../config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix.yaml)
  Patched polished-setpoint Fw/Bw `TE Curve Verification Pipeline` comparison
  matrix adding the completed shape-gate loss pilot checkpoint to the reduced
  active set.

- [reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-49-22_shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gate_pilot_expansion_polished_setpoints_fw_bw_report.md](./reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-49-22_shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gate_pilot_expansion_polished_setpoints_fw_bw_report.md)
  Patched polished-setpoint Fw/Bw comparison report confirming the shape-gate
  loss pilot is viable but not the strongest reduced-set candidate.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-21]/shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gated_te_curve_reranker_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/%5B2026-07-21%5D/shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gated_te_curve_reranker_report.md)
  Shape-gated reranker result for the patched polished-setpoint Fw/Bw expansion:
  `periodic_gru_sequence_Fw` remains the forward recommendation,
  `periodic_mlp_harmonic_Bw` becomes the backward recommendation, and the
  shape-gate loss pilot remains a non-promoted forward candidate.

- [reports/campaign_results/track_2/verification_plots/shape_gate_pilot_expansion_polished_setpoints_fw_bw/track2_candidate_curve_plot_summary.yaml](./reports/campaign_results/track_2/verification_plots/shape_gate_pilot_expansion_polished_setpoints_fw_bw/track2_candidate_curve_plot_summary.yaml)
  Forward polished-setpoint Track 2 plot summary for the patched shape-gate
  pilot expansion, covering two representative curves per candidate.

- [reports/campaign_results/track_2/verification_plots/shape_gate_pilot_expansion_polished_setpoints_fw_bw_backward/track2_candidate_curve_plot_summary.yaml](./reports/campaign_results/track_2/verification_plots/shape_gate_pilot_expansion_polished_setpoints_fw_bw_backward/track2_candidate_curve_plot_summary.yaml)
  Backward polished-setpoint Track 2 plot summary for the same patched
  expansion.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/rcim_track1_familywise_crosscheck/[2026-07-20]/rcim_track1_familywise_crosscheck_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/rcim_track1_familywise_crosscheck/%5B2026-07-20%5D/rcim_track1_familywise_crosscheck_report.md)
  Diagnostic cross-check separating the latest `rcim_track1` forward `h0`
  offset bug, Wave 4.3 Mixture Density ONNX playback mismatch, Gaussian NLL
  setpoints outlier, and familywise inventory-layout drift.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_setpoints_matrix_shape_gated_te_curve_reranker_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/%5B2026-07-20%5D/selected_active_track2_polished_setpoints_matrix_shape_gated_te_curve_reranker_report.md)
  Shape-gated reduced selected-active reranker for polished setpoint
  forward/backward candidates, with FFT amplitude, harmonic, phase,
  derivative, offset, and per-curve pass-rate diagnostics.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_actual_values_matrix_shape_gated_te_curve_reranker_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/%5B2026-07-20%5D/selected_active_track2_polished_actual_values_matrix_shape_gated_te_curve_reranker_report.md)
  Shape-gated reduced selected-active reranker for polished actual-value
  forward/backward candidates, using the same curve-first diagnostic blocks.

- [reports/analysis/te_curve_verification_pipeline/03_family_reports/rcim_track1/[2026-07-19]/track2_rcim_track1_retrained_paper_tables_report.md](./reports/analysis/te_curve_verification_pipeline/03_family_reports/rcim_track1/%5B2026-07-19%5D/track2_rcim_track1_retrained_paper_tables_report.md)
  Paper Table 2-5 equivalents for the current `rcim_track1` retrained
  model-bank archives across simplified setpoints, polished setpoints, and
  polished actual values, with per-target best-cell highlights for composite
  candidate selection.

- [scripts/tooling/lan_ai/lan_ai_node_server.md](./scripts/tooling/lan_ai/lan_ai_node_server.md)
  Setup and runtime guide for the remote LAN AI workstation.

- [scripts/tooling/video_guides/remote_high_quality_video_pipeline.md](./scripts/tooling/video_guides/remote_high_quality_video_pipeline.md)
  Canonical process note for the validated high-quality TwinCAT/TestRig video pipeline.

- [scripts/campaigns/track_2/run_polished_dataset_track2_verification_refresh.md](./scripts/campaigns/track_2/run_polished_dataset_track2_verification_refresh.md)
  Launcher note for the official polished-dataset `TE Curve Verification
  Pipeline` refresh with local and remote commands.

- [scripts/campaigns/track_2/run_reduced_selected_track2_reports.md](./scripts/campaigns/track_2/run_reduced_selected_track2_reports.md)
  Active reduced selected-model `TE Curve Verification Pipeline` launcher that
  generates only the four polished/simplified forward/backward reports and
  keeps `global`, collage, overlay, and dataset-difference reports paused by
  default.

- [scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.md](./scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.md)
  Aries launcher note for one-at-a-time dataset input-mode retraining campaigns
  across `simplified_dataset` setpoints, `polished_dataset` setpoints, and
  `polished_dataset` actual values.

- [scripts/campaigns/cross_wave/run_rcim_track1_polished_setpoints_campaign.md](./scripts/campaigns/cross_wave/run_rcim_track1_polished_setpoints_campaign.md)
  Launcher note for the prepared `rcim_track1` polished setpoint campaign,
  including local preflight commands, local parallel Windows execution, and
  promotion into the official input-mode model archive.

- [scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.md](./scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.md)
  Aries CPU/RAM Slurm launcher note for the polished `rcim_track1`
  input-mode campaign package.

### Analysis Reports

- [reports/analysis/Complete TE And Dataset Renaming Audit.md](./reports/analysis/Complete%20TE%20And%20Dataset%20Renaming%20Audit.md)
  Complete working-tree audit of the TE taxonomy and simplified-dataset path
  migrations, including tracked, ignored, generated, document, and binary
  files. A styled PDF companion is available at
  `reports/analysis/Complete TE And Dataset Renaming Audit.pdf`.

- [reports/analysis/mmt_te_modeling/MMT TE Modeling Equation Extraction And Reimplementation Plan.md](./reports/analysis/mmt_te_modeling/MMT%20TE%20Modeling%20Equation%20Extraction%20And%20Reimplementation%20Plan.md)
  Equation extraction, implementation notes, MATLAB/Python reproduction entry
  points, and dataset-evaluation plan for the analytical `MMT_TEModeling`
  `RV` reducer transmission-error model.

- [reports/analysis/rcim_paper_reference/RCIM Paper Reference Archive Parity Interpretation.md](./reports/analysis/rcim_paper_reference/RCIM%20Paper%20Reference%20Archive%20Parity%20Interpretation.md)
  Canonical interpretation of the repository-local parity check across
  `models/paper_reference/rcim_original`, `rcim_retuned`, and `rcim_track1`.

- [reports/analysis/rcim_paper_reference/RCIM Original ONNX Release Parity Interpretation.md](./reports/analysis/rcim_paper_reference/RCIM%20Original%20ONNX%20Release%20Parity%20Interpretation.md)
  Canonical interpretation of the recovered original ONNX release parity check
  against the repository `rcim_original/forward` archive and TE Curve Verification Pipeline forward
  curve evaluation.

- [reports/analysis/utilities/linux_script_portability/[2026-05-16]/script_portability_inventory.md](./reports/analysis/utilities/linux_script_portability/%5B2026-05-16%5D/script_portability_inventory.md)
  Refreshed repository-wide script portability inventory after the final
  Linux Bash-equivalent sweep for campaign, tooling, and report scripts.

- [reports/analysis/utilities/linux_script_portability/[2026-05-15]/script_portability_inventory.md](./reports/analysis/utilities/linux_script_portability/%5B2026-05-15%5D/script_portability_inventory.md)
  Repository-wide script portability inventory for the Unimore Aries Linux
  migration, including per-script platform-flag and Bash-equivalent status.

- [reports/analysis/rcim_paper_reference/RCIM Original Pipeline To Reimplementation Companion.md](./reports/analysis/rcim_paper_reference/RCIM%20Original%20Pipeline%20To%20Reimplementation%20Companion.md)
  Deep explanatory companion that walks through the recovered original RCIM
  prediction pipeline, maps the active `v18` path inside `predictorML_v7.py`,
  and explains how the repository exact-paper reimplementation redistributes
  that workflow.

- [reports/analysis/rcim_paper_reference/RCIM Original Pipeline And Reimplementation Audit.md](./reports/analysis/rcim_paper_reference/RCIM%20Original%20Pipeline%20And%20Reimplementation%20Audit.md)
  Code-level audit of the copied recovered RCIM original workflow versus the
  current repository reimplementation, including runnable-stage boundaries and
  the main engineering divergences.

- [reports/analysis/wave1/wave1_best_model_te_curve_prediction/[2026-04-25]/wave1_best_model_te_curve_prediction_report.md](./reports/analysis/wave1/wave1_best_model_te_curve_prediction/%5B2026-04-25%5D/wave1_best_model_te_curve_prediction_report.md)
  Offline comparison report for the current Wave 1 family-best models on a
  deterministic 20% subset of the canonical held-out TE test curves, including
  aggregate metrics and plot artifact pointers.

- [reports/analysis/wave2/Wave 2.1 Temporal Sequence Models.md](./reports/analysis/wave2/Wave%202%20Temporal%20Sequence%20Models.md)
  Explanatory report for the first `Wave 2.1` temporal sequence families:
  temporal convolution, `GRU`, and `LSTM` windowed TE regressors.

- [reports/analysis/wave2/Wave 2.2 Harmonic Temporal Hybrid Models.md](./reports/analysis/wave2/Wave%202B%20Harmonic%20Temporal%20Hybrid%20Models.md)
  Explanatory report for the `Wave 2.2` harmonic-temporal hybrid families that
  add explicit periodic harmonic features to temporal convolution, `GRU`, and
  `LSTM` sequence windows.

- [reports/analysis/wave2/Wave 2.3 Residual Harmonic Temporal Hybrid Models.md](./reports/analysis/wave2/Wave%202C%20Residual%20Harmonic%20Temporal%20Hybrid%20Models.md)
  Explanatory report for the `Wave 2.3` residual harmonic temporal hybrid
  families that add recurrent sequence residuals over a structured harmonic
  base.

- [reports/analysis/wave2/Wave 3.1 Sequential Residual-Offset Probe Model.md](./reports/analysis/wave2/Track%202F%20Sequential%20Residual-Offset%20Probe%20Model.md)
  Explanatory report for the first learned `Wave 3.1`
  `sequential_residual_offset_probe` model, including branch structure,
  causal input boundary, implemented files, and verification status.

- [reports/analysis/rcim_paper_reference/RCIM Exact Paper Model Bank Workflow.md](./reports/analysis/rcim_paper_reference/RCIM%20Exact%20Paper%20Model%20Bank%20Workflow.md)
  Explanatory report for the strict paper-faithful RCIM family-bank branch,
  including the exact target schema, recovered family inventory, operating
  principle, Python structure, and relationship with the older repository-owned
  harmonic-wise branch.

- [reports/analysis/rcim_paper_reference/RCIM Recovered Asset Deep Analysis.md](./reports/analysis/rcim_paper_reference/RCIM%20Recovered%20Asset%20Deep%20Analysis.md)
  Deep implementation-facing analysis of the recovered RCIM paper assets,
  including the exact ONNX family bank, original and later code generations,
  backup evolution, TwinCAT export evidence, archive limitations, and the
  exact consequences for faithful `RCIM Model-Bank Reproduction` reimplementation.

- [reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md](./reports/analysis/rcim_paper_reference/RCIM%20Paper%20Reference%20Benchmark.md)
  Canonical repository-owned RCIM Tables `2`-`5` benchmark surface, now backed
  by the faithful RCIM Model-Bank Reproduction exact-model-bank reimplementation and accepted
  `models/paper_reference/rcim_track1/` archives.

- [reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md](./reports/analysis/te_curve_verification_pipeline/00_overview/TE%20Curve%20Verification%20Pipeline%20Directional%20Model%20Comparison.md)
  Canonical `TE Curve Verification Pipeline` offline matrix comparing accepted `RCIM Model-Bank Reproduction`, recovered
  original, retuned paper-reference banks, and exported `Wave 1` models from
  `models/`, split into forward, backward, and global direction sections.

- [reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md](./reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/%5B2026-06-16%5D/track2_multi_index_curve_first_selection_policy.md)
  Canonical policy for official `TE Curve Verification Pipeline` model selection after the
  curve-first shift, requiring raw-error, mean-centered shape, offset /
  continuity, harmonic / phase, robustness, visual-evidence, and
  deployment-readiness axes instead of scalar `MAE` alone.

- [reports/analysis/TE Program Status And Closeout Ledger.md](./reports/analysis/TE%20Program%20Status%20And%20Closeout%20Ledger.md)
  Maintained official TE modeling status ledger covering `Wave 1` through
  `Wave 5.1`, `CVP 1.1` through `CVP 1.5` and Waves `3.1` through `4.4`, current direction-parallel leaders,
  and the required update rule for future campaign and `TE Curve Verification Pipeline` closeouts.

- [reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Curve Reconstruction And Collage Pipeline.md](./reports/analysis/te_curve_verification_pipeline/00_overview/TE%20Curve%20Verification%20Pipeline%20Curve%20Reconstruction%20And%20Collage%20Pipeline.md)
  Implementation-facing `TE Curve Verification Pipeline` curve-reconstruction guide covering the
  standard best-model collage path, repository models such as
  `harmonic_regression`, paper-original reference-bank reconstruction, and
  mean-centered diagnostic interpretation.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-07-03]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-07-03%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` verification decision for the
  polished-dataset RCIM, early-wave, and full-wave refresh, accepting
  `polished_periodic_gru_sequence` as the model-development baseline while
  retaining `polished_rcim_model_bank_reproduction_ET19_Fw` as the polished
  forward reference-bank leader.

- [reports/analysis/model_development_waves/model_family_pruning/[2026-07-06]/te_model_family_pruning_decision_report.md](./reports/analysis/model_development_waves/model_family_pruning/%5B2026-07-06%5D/te_model_family_pruning_decision_report.md)
  Forward-led, backward-checked model-family pruning report that pauses
  `global` model selection, defines the reduced active candidate set, and
  records keep, baseline-only, pause, or retire decisions for the implemented
  TE model families.

- [reports/analysis/model_development_waves/intermediate_model_selection_cleanup/[2026-07-17]/te_intermediate_model_selection_cleanup_report.md](./reports/analysis/model_development_waves/intermediate_model_selection_cleanup/%5B2026-07-17%5D/te_intermediate_model_selection_cleanup_report.md)
  Intermediate post-retraining model-selection cleanup report that preserves
  one temporal-window path and one non-windowed path, demotes
  `periodic_lstm_sequence_Bw` as a false scalar leader, and closes dead-end
  exploratory branches before the next development cycle.

- [reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-06]/](./reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/%5B2026-07-06%5D/)
  Reduced selected-model `TE Curve Verification Pipeline` report bundle with
  exactly four active reports: polished forward, polished backward, simplified
  forward, and simplified backward.

- [reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]/](./reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/%5B2026-07-19%5D/)
  Selected-active `TE Curve Verification Pipeline` report bundle after the full
  model-family retraining pass, covering simplified setpoints, polished
  setpoints, and polished actual values across forward and backward surfaces.

- [reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-07-03]/track2_best_model_collage_report.md](./reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/%5B2026-07-03%5D/track2_best_model_collage_report.md)
  Styled `TE Curve Verification Pipeline` visual report with four-curve
  collages for the polished refreshed RCIM and model-development candidates
  alongside the historical reference, Wave, and Track candidate families.

- [reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-07-03]/track2_multi_model_curve_comparison_report.md](./reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/%5B2026-07-03%5D/track2_multi_model_curve_comparison_report.md)
  Styled `TE Curve Verification Pipeline` overlay report comparing original TE
  curves against the refreshed polished candidates and the historical
  reference, Wave, and Track candidate families.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-11]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-06-11%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` model-verification report accepting `Wave 4.1` robust
  losses as a verified exploratory baseline without promoting them over the
  current direction-parallel `TE Curve Verification Pipeline` leaders.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/wave2_temporal_model_refresh_plan/[2026-05-24]/track2_wave2_temporal_model_refresh_plan.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/wave2_temporal_model_refresh_plan/%5B2026-05-24%5D/track2_wave2_temporal_model_refresh_plan.md)
  Operational refresh plan for adding the completed `Wave 2.1`
  temporal-model candidates to the official `TE Curve Verification Pipeline` verification matrix,
  visual reports, and update ledger.

- [reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-06-11]/track2_best_model_collage_report.md](./reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/%5B2026-06-11%5D/track2_best_model_collage_report.md)
  Styled `TE Curve Verification Pipeline` visual report with four-curve collages for the current best
  reference, RCIM Model-Bank Reproduction, Wave 1, Wave 2.1, Wave 2.3, Wave 3.1, Wave 3.2, and
  Wave 3.3 and Wave 4 series candidates.

- [reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-06-11]/track2_multi_model_curve_comparison_report.md](./reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/%5B2026-06-11%5D/track2_multi_model_curve_comparison_report.md)
  Styled `TE Curve Verification Pipeline` overlay report comparing original TE curves against
  reference best models and screened Wave 1, Wave 2.1, Wave 2.3, Wave 3.1,
  Wave 3.2, Wave 3.3, and Wave 4 series models.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_first_reranking_report/%5B2026-05-28%5D/track2_curve_first_reranking_report.md)
  `CVP 1.1` curve-first reranking report that ranks accepted `TE Curve Verification Pipeline`
  candidates by full-curve mean percentage error, P95, worst-condition error,
  and curve `MAE` while preserving the causal runtime input boundary.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/curve_payload_diagnostics_report/%5B2026-05-28%5D/track2_curve_payload_diagnostics_report.md)
  `CVP 1.2` curve-payload diagnostics report for screened candidates,
  including peak-to-peak, harmonic amplitude, harmonic phase, derivative,
  smoothness, and closure diagnostics.

- [reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md](./reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/%5B2026-06-02%5D/track2_mean_centered_collage_report.md)
  `TE Curve Verification Pipeline` mean-centered collage diagnostics report that subtracts each
  truth and prediction curve mean after inference, then recomputes curve
  `MAE` and `RMSE` to separate vertical offset from waveform-shape tracking.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/mean_offset_full_matrix_audit/%5B2026-06-03%5D/track2d_mean_offset_full_matrix_audit.md)
  `CVP 1.4` full-matrix mean-offset audit over `111` direction-valid
  candidates and `12,416` curves, separating raw error, curve offset,
  centered-shape error, amplitude error, harmonic phase error, and diagnostic
  failure-mode labels.

- [reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md](./reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/offset_predictability_feasibility/%5B2026-06-03%5D/track2e_offset_predictability_feasibility.md)
  `CVP 1.5` offset-predictability feasibility report that uses completed
  `CVP 1.4` artifacts to test conservative causal offset-correction
  baselines and recommend the next intervention branch per `Fw`, `Bw`, and
  `global` surface.

- [reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification_plan/[2026-06-09]/track2_component_offset_identification_plan.md](./reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification_plan/%5B2026-06-09%5D/track2_component_offset_identification_plan.md)
  `TE Curve Verification Pipeline` component-offset identification plan for testing whether the
  observed curve offset is dominated by `a_0` / `Component 0`, multiple
  harmonics, condition/regime behavior, or experimental repeatability limits
  before opening another training campaign.

- [reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-09]/track2_component_offset_identification_diagnostic.md](./reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/%5B2026-06-09%5D/track2_component_offset_identification_diagnostic.md)
  `TE Curve Verification Pipeline` measured component-offset diagnostic showing harmonic zero as the
  largest average measured component while preserving the conclusion that it
  is a priority suspect, not the sole confirmed cause.

- [reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-09]/track2d_h0_offset_crosscheck.md](./reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/%5B2026-06-09%5D/track2d_h0_offset_crosscheck.md)
  Cross-check of `CVP 1.4` signed offset errors against measured `h0` /
  curve-mean patterns to test whether large model offset failures coincide
  with large `h0` cases.

- [reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/[2026-06-10]/track2d_predicted_mean_h0_surface_diagnostic.md](./reports/analysis/te_curve_verification_pipeline/04_offset_investigations/component_offset_identification/%5B2026-06-10%5D/track2d_predicted_mean_h0_surface_diagnostic.md)
  Diagnostic comparing `CVP 1.4` predicted mean surfaces against measured
  `h0` to identify candidate-specific bias, slope compression, and
  direction/regime offset behavior.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/dispersion_aware_wave_roadmap/[2026-06-10]/track2_dispersion_aware_wave_roadmap.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/dispersion_aware_wave_roadmap/%5B2026-06-10%5D/track2_dispersion_aware_wave_roadmap.md)
  `TE Curve Verification Pipeline` roadmap that inserts dispersion-aware probes, `Wave 5.1` hybrid
  structured models, and `Wave 5.2` first-PINN work before the integrated
  multi-task / multi-head architecture.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/Wave 4.4 Latent-State Hysteresis Probe Model.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/Track%202H-L%20Latent-State%20Hysteresis%20Probe%20Model.md)
  Explanatory report for the `Wave 4.4`
  `latent_state_hysteresis_probe` model, covering causal latent-state
  encoding, base/offset/residual heads, campaign profiles, risks, and
  implemented files.

- [reports/campaign_plans/track_2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md)
  Preliminary `Wave 4 series` campaign plan for robust, quantile/probabilistic,
  mixture-density, and latent-state / hysteresis-aware modeling probes before
  the integrated multi-task / multi-head branch.

- [reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 4.4` latent-state /
  hysteresis-aware package, focused on causal-history state encoders for
  preload, elastic release, direction-transition, and protocol-state effects.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md)
  Final results report for the completed `Wave 4.4` latent-state /
  hysteresis-aware campaign, including scalar branch winners, comparison
  against robust/probabilistic/MDN baselines, registry effects, and the
  boundary that official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/cross_wave/polished_dataset/2026-07-02-10-36-59_polished_full_wave_retraining_campaign_results_report.md](./reports/campaign_results/cross_wave/polished_dataset/2026-07-02-10-36-59_polished_full_wave_retraining_campaign_results_report.md)
  Closeout report for the completed 108-run polished full-wave retraining campaign.

- [reports/campaign_plans/cross_wave/polished_dataset/2026-07-02-11-12-17_polished_te_curve_verification_refresh_campaign_plan_report.md](./reports/campaign_plans/cross_wave/polished_dataset/2026-07-02-11-12-17_polished_te_curve_verification_refresh_campaign_plan_report.md)
  Operator-launch plan for the official polished-dataset `TE Curve Verification
  Pipeline` refresh over the closed RCIM, early-wave, and full-wave retraining
  artifacts.

- [reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-40-05_polished_early_wave_parallel_training_campaign_results_report.md](./reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-40-05_polished_early_wave_parallel_training_campaign_results_report.md)
  Closeout report for the completed 36-run polished early-wave parallel training campaign.

- [reports/campaign_results/cross_wave/polished_dataset/2026-06-22-16-59-14_polished_dataset_stage1_smoke_campaign_results_report.md](./reports/campaign_results/cross_wave/polished_dataset/2026-06-22-16-59-14_polished_dataset_stage1_smoke_campaign_results_report.md)
  Final results report for the completed `polished_dataset` Stage 1 smoke
  campaign, including the eight-run scalar leaderboard, registry effects,
  dataset-schema acceptance, and the boundary that official
  `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md](./reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md)
  Preliminary and prepared campaign plan for the first real `Wave 5.1`
  harmonic-prior residual package across `global`, `Fw`, and `Bw`.

- [reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md](./reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md)
  Final results report for the completed first real `Wave 5.1`
  harmonic-prior residual campaign, including scalar branch winners,
  profile comparison, registry effects, and the normal-closeout boundary that
  kept official `TE Curve Verification Pipeline` curve verification as a separate follow-up step.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-15]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-06-15%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` verification decision for the completed `Wave 5.1`
  harmonic-prior residual candidates, verified as an exploratory baseline and
  not promoted over the accepted direction-parallel leaders.

- [reports/campaign_plans/track_2/2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md)
  Preliminary campaign plan for the next `Wave 4 series` package, focused on
  two- and three-component mixture-density heads across `global`, `Fw`, and
  `Bw`.

- [reports/campaign_plans/track_2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 4.2` package, focused on
  quantile and Gaussian probabilistic regression candidates across `global`,
  `Fw`, and `Bw`.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md)
  Final results report for the completed `Wave 4.2`
  quantile/probabilistic campaign, including scalar branch winners,
  calibration diagnostics, robust-loss comparison, and the boundary that
  official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md)
  Final results report for the completed third `Wave 4.3` mixture-density
  campaign, including scalar branch winners, mixture-collapse diagnostics,
  comparison against robust/probabilistic probes, and the boundary that
  official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-12]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-06-12%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` verification decision for the completed `Wave 4 series`
  quantile/probabilistic candidates, verified as an exploratory baseline and
  not promoted over the accepted direction-parallel leaders.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-13]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-06-13%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` verification decision for the completed `Wave 4 series`
  mixture-density heads candidates, verified as an exploratory baseline with
  a strong backward branch but not promoted over the accepted
  direction-parallel leaders.

- [reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-15]/track2_official_model_verification_report.md](./reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/%5B2026-06-15%5D/track2_official_model_verification_report.md)
  Official `TE Curve Verification Pipeline` verification decision for the completed first real
  `Wave 5.1` harmonic-prior residual candidates, verified as an exploratory
  baseline and not promoted over the accepted direction-parallel leaders.

- [reports/analysis/wave3/Wave 5.1 Hybrid Structured Models.md](./reports/analysis/wave3/Wave%203%20Hybrid%20Structured%20Models.md)
  Design report for `Wave 5.1` hybrid structured TE models, covering harmonic
  prior residual learners, grouped harmonic heads, condition-conditioned
  residual surfaces, and basis-constrained curve decoders.

- [reports/analysis/wave4/Wave 5.2 PINN Formulation And First PINN.md](./reports/analysis/wave4/Wave%204%20PINN%20Formulation%20And%20First%20PINN.md)
  Design report for the first `Wave 5.2` soft-constraint PINN branch, covering
  TE data fit, periodicity, smoothness, harmonic consistency, condition-surface
  consistency, and residual regularization boundaries.

- [reports/analysis/wave4/Wave 5.2A MMT Equation Diagnostic Design.md](./reports/analysis/wave4/Wave%204A%20MMT%20Equation%20Diagnostic%20Design.md)
  Detailed design for using the repository-owned MMT equation reproduction as
  a TE Curve Verification Pipeline analytical diagnostic before feature or PINN integration.

- [reports/analysis/wave4/Wave 5.2B MMT Feature Generator Design.md](./reports/analysis/wave4/Wave%204B%20MMT%20Feature%20Generator%20Design.md)
  Detailed design for turning MMT subsystem terms, harmonic summaries, and
  calibrated analytical residuals into leakage-safe feature candidates.

- [reports/analysis/wave4/Wave 5.2C MMT Soft Constraint PINN Design.md](./reports/analysis/wave4/Wave%204C%20MMT%20Soft%20Constraint%20PINN%20Design.md)
  Detailed design for adding weak MMT equation residuals to a curve or
  harmonic-plus-residual neural model.

- [reports/analysis/wave4/Wave 5.2D Mesh Stiffness Loaded TE PINN Design.md](./reports/analysis/wave4/Wave%204D%20Mesh%20Stiffness%20Loaded%20TE%20PINN%20Design.md)
  Detailed design for exploratory time-varying mesh stiffness and loaded-static
  transmission-error constraints.

- [reports/analysis/wave4/Wave 5.2E Backlash Preload State PINN Design.md](./reports/analysis/wave4/Wave%204E%20Backlash%20Preload%20State%20PINN%20Design.md)
  Detailed design for backlash, preload, direction-transition, and latent-state
  constraints targeting local dispersion.

- [reports/analysis/wave4/Wave 5.2F Cycloid Contact Force PINN Design.md](./reports/analysis/wave4/Wave%204F%20Cycloid%20Contact%20Force%20PINN%20Design.md)
  Detailed design for cycloid-pin contact-force, profile-modification, and
  loaded-TE exploratory constraints.

- [reports/analysis/wave4/Wave 5.2G Planetary Mesh Force LSTE PINN Design.md](./reports/analysis/wave4/Wave%204G%20Planetary%20Mesh%20Force%20LSTE%20PINN%20Design.md)
  Detailed design for planetary-style mesh-force, load-sharing, and
  loaded-static-TE exploratory constraints.

- [reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/wave4a_mmt_equation_diagnostic.md](./reports/analysis/wave4/mmt_equation_diagnostic/%5B2026-06-11%5D/wave4a_mmt_equation_diagnostic.md)
  First `Wave 5.2A` MMT equation-chain diagnostic report, summarizing the
  demonstration `RTE` mean, peak-to-peak amplitude, dominant harmonics, and
  TE Curve Verification Pipeline suspicious-harmonic probe.

- [reports/analysis/wave4/mmt_parameter_inventory/[2026-06-11]/wave4a_mmt_parameter_inventory.md](./reports/analysis/wave4/mmt_parameter_inventory/%5B2026-06-11%5D/wave4a_mmt_parameter_inventory.md)
  `Wave 5.2A` MMT parameter-inventory report, classifying geometry constants,
  dataset metadata, train-only equivalent-error channels, blocked contact
  geometry, and target-only TE boundaries before `Wave 5.2B` or `Wave 5.2C`.

- [technical/2026-06/2026-06-09/2026-06-09-20-03-08_track2d_h0_offset_crosscheck.md](./technical/2026-06/2026-06-09/2026-06-09-20-03-08_track2d_h0_offset_crosscheck.md)
  Technical plan for cross-checking `CVP 1.4` signed offset errors against
  measured `h0` / curve-mean patterns and outliers.

- [technical/2026-06/2026-06-10/2026-06-10-12-51-19_track2d_predicted_mean_h0_surface_diagnostic.md](./technical/2026-06/2026-06-10/2026-06-10-12-51-19_track2d_predicted_mean_h0_surface_diagnostic.md)
  Technical plan for comparing `CVP 1.4` `predicted_mean_deg` surfaces against
  measured `h0` after the h0 magnitude cross-check.

- [technical/2026-06/2026-06-11/2026-06-11-12-32-58_mmt_te_modeling_equation_reimplementation.md](./technical/2026-06/2026-06-11/2026-06-11-12-32-58_mmt_te_modeling_equation_reimplementation.md)
  Technical plan for extracting the `MMT_TEModeling` equations, creating
  MATLAB and Python analytical reimplementation scripts, and planning dataset
  evaluation against repository TE curves.

- [reports/analysis/te_curve_verification_pipeline/04_offset_investigations/original_onnx_offset_diagnostic/[2026-06-04]/track2_original_onnx_offset_diagnostic.md](./reports/analysis/te_curve_verification_pipeline/04_offset_investigations/original_onnx_offset_diagnostic/%5B2026-06-04%5D/track2_original_onnx_offset_diagnostic.md)
  Diagnostic replay of the recovered paper-original `ONNX` release through the
  `TE Curve Verification Pipeline` forward curve evaluator, including raw parity and mean-centered
  offset evidence for the original executable model families.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/original_onnx_fw_collage_report/[2026-06-05]/track2_original_onnx_fw_collage_report.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/original_onnx_fw_collage_report/%5B2026-06-05%5D/track2_original_onnx_fw_collage_report.md)
  Simple `TE Curve Verification Pipeline` collage report and PDF for the recovered paper-original
  `ONNX` `paper_original_best_Fw` composite loaded directly from the `19`
  original target models.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/sparse_original_onnx_variants/[2026-06-08]/track2_sparse_original_onnx_variants_report.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/sparse_original_onnx_variants/%5B2026-06-08%5D/track2_sparse_original_onnx_variants_report.md)
  Sparse original `ONNX` `TE Curve Verification Pipeline` report comparing the component-selected
  simplified RCIM variant and the PLC-oriented all-`HGBM` variant over
  harmonics `0`, `1`, `39`, and `40`.

- [reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/forward_reference_curve_comparison/[2026-06-08]/track2_forward_reference_curve_comparison_report.md](./reports/analysis/te_curve_verification_pipeline/05_reference_and_legacy/forward_reference_curve_comparison/%5B2026-06-08%5D/track2_forward_reference_curve_comparison_report.md)
  Forward `TE Curve Verification Pipeline` curve-comparison report collecting the paper-original,
  paper-retuned, full original `ONNX`, sparse original `ONNX`, and PLC-oriented
  sparse original `ONNX` collages with aggregate and pairwise curve-difference
  metrics.

- [reports/analysis/rcim_paper_reference/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md](./reports/analysis/rcim_paper_reference/rcim_retuned_reference_closeout/%5B2026-05-13%5D/rcim_retuned_reference_closeout_report.md)
  Detailed closeout report for the recovered-original RCIM retuned reference
  archive, including source bundles, export completeness, and retuned Tables
  `2`-`5` for both directions.

- [reports/analysis/project_status/current/Training Results Master Summary.md](./reports/analysis/project_status/current/Training%20Results%20Master%20Summary.md)
  Canonical always-updated summary of current project status, best family
  results, recent campaign changes, and family-by-family ranked outcomes across
  the TE training program.

- [reports/analysis/Repository Status Wave Track Synthesis.md](./reports/analysis/Repository%20Status%20Wave%20Track%20Synthesis.md)
  Consolidated state report covering the repository status, `Wave 1`,
  `Wave 2.1`, `Wave 2.2`, `Wave 2.3`, `TE Curve Verification Pipeline` outcomes, sparse `RCIM` versus
  dense harmonic-bank results, and the curve-first future plan introduced by
  commit `b73220679410276246421b7e2832d8878cff90a0`. A styled PDF companion
  is available at
  `reports/analysis/Repository Status Wave Track Synthesis.pdf`.

- [reports/analysis/wave1/Wave 1 - Closeout Status.md](./reports/analysis/wave1/Wave%201%20-%20Closeout%20Status.md)
  Consolidated closeout report for `Wave 1`, covering campaign completion status, compared families, family winners, and final ranking.

- [reports/analysis/utilities/Skill and Subagent Operational Test.md](./reports/analysis/utilities/Skill%20and%20Subagent%20Operational%20Test.md)
  Operational test report for the second wave of repository-owned Codex skills and subagents.

- [reports/analysis/te_modeling/Twincat-Friendly Structured TE Modeling.md](./reports/analysis/te_modeling/Twincat-Friendly%20Structured%20TE%20Modeling.md)
  Reference-backed synthesis of TwinCAT-friendly structured TE modeling implications for the current repository direction.

- [reports/analysis/te_modeling/Curve-First TE Training Strategy.md](./reports/analysis/te_modeling/Curve-First%20TE%20Training%20Strategy.md)
  Strategy report for shifting TE model selection from scalar pointwise
  `MAE` toward TE Curve Verification Pipeline curve-following quality, harmonic/phase diagnostics,
  and continuous compensation readiness.

- [reports/analysis/utilities/Code Documentation Platform Comparison.md](./reports/analysis/utilities/Code%20Documentation%20Platform%20Comparison.md)
  Comparative analysis of repository documentation-platform options in the readable-filename analysis-report layout.

- [reports/analysis/utilities/Local LAN AI Infrastructure Options for Video Knowledge Extraction.md](./reports/analysis/utilities/Local%20LAN%20AI%20Infrastructure%20Options%20for%20Video%20Knowledge%20Extraction.md)
  Comparative architecture report for local and LAN-accessible transcript, OCR, and LLM infrastructure for the TwinCAT/TestRig video workflow.

- [reports/analysis/twincat_video_guides/[2026-04-02]/remote_high_quality_video_campaign_sum_up.md](./reports/analysis/twincat_video_guides/%5B2026-04-02%5D/remote_high_quality_video_campaign_sum_up.md)
  Technical sum-up of the completed remote-strong `large-v3` plus `openai/gpt-oss-20b` video campaign across the 11 canonical TwinCAT/TestRig videos.

### Technical Documents

#### 2026-07-07

- [technical/2026-07/2026-07-07/2026-07-07-00-47-35_track2_dataset_matched_selected_reports.md](./technical/2026-07/2026-07-07/2026-07-07-00-47-35_track2_dataset_matched_selected_reports.md)
  Technical plan for correcting the reduced selected-model reports so polished
  and simplified reports use dataset-matched model candidates and shared
  four-curve evidence sets per direction.

- [technical/2026-07/2026-07-07/2026-07-07-11-46-14_familywise_track2_onnx_report_pipeline.md](./technical/2026-07/2026-07-07/2026-07-07-11-46-14_familywise_track2_onnx_report_pipeline.md)
  Technical plan for a familywise `TE Curve Verification Pipeline` ONNX report
  that evaluates dataset/input-mode matched exported models and produces
  configurable forward, backward, and global curve pages.

#### 2026-07-06

- [technical/2026-07/2026-07-06/2026-07-06-12-50-44_track2_dataset_surface_pdf_export.md](./technical/2026-07/2026-07-06/2026-07-06-12-50-44_track2_dataset_surface_pdf_export.md)
  Technical plan for exporting and validating the generated dataset/surface
  `TE Curve Verification Pipeline` split reports as styled PDFs.

#### 2026-07-04

- [technical/2026-07/2026-07-04/2026-07-04-00-54-04_track2_dataset_surface_launcher_post_rebase_fix.md](./technical/2026-07/2026-07-04/2026-07-04-00-54-04_track2_dataset_surface_launcher_post_rebase_fix.md)
  Technical plan for aligning the dataset/surface `TE Curve Verification
  Pipeline` launcher with the completed polished closure state and the
  reorganized `te_curve_verification_pipeline` analysis-report tree.

#### 2026-07-02

- [technical/2026-07/2026-07-02/2026-07-02-11-12-17_polished_te_curve_verification_refresh.md](./technical/2026-07/2026-07-02/2026-07-02-11-12-17_polished_te_curve_verification_refresh.md)
  Technical plan for preparing the separate official `TE Curve Verification
  Pipeline` refresh over the polished RCIM, early-wave, and full-wave retraining
  closeouts.

- [technical/2026-07/2026-07-02/2026-07-02-10-36-59_polished_full_wave_retraining_closeout.md](./technical/2026-07/2026-07-02/2026-07-02-10-36-59_polished_full_wave_retraining_closeout.md)
  Technical plan for closing out the completed `108`-run polished full-wave
  retraining campaign, publishing the Markdown/PDF campaign-results report,
  synchronizing status documents, and preserving the separate
  `TE Curve Verification Pipeline` boundary.

#### 2026-06-29

- [technical/2026-06/2026-06-29/2026-06-29-10-40-05_polished_early_wave_parallel_training_closeout.md](./technical/2026-06/2026-06-29/2026-06-29-10-40-05_polished_early_wave_parallel_training_closeout.md)
  Technical plan for closing out the completed 36-run polished early-wave
  parallel training campaign, publishing the Markdown/PDF results report,
  synchronizing status documents, and preserving the parallel RCIM campaign
  provenance.

- [technical/2026-06/2026-06-29/2026-06-29-10-39-38_polished_rcim_model_bank_closeout.md](./technical/2026-06/2026-06-29/2026-06-29-10-39-38_polished_rcim_model_bank_closeout.md)
  Technical plan for closing out the completed polished
  `RCIM Model-Bank Reproduction` campaign, including directional winner
  artifacts, campaign-results reporting, PDF validation, and active-campaign
  state cleanup.

#### 2026-06-25

- [technical/2026-06/2026-06-25/2026-06-25-15-28-26_polished_early_wave_parallel_training.md](./technical/2026-06/2026-06-25/2026-06-25-15-28-26_polished_early_wave_parallel_training.md)
  Technical plan for launching a protected-state-aware early-wave
  `polished_dataset` retraining batch in parallel with the RCIM campaign
  running on another workstation.

- [technical/2026-06/2026-06-25/2026-06-25-15-14-22_polished_rcim_runtime_log_wording.md](./technical/2026-06/2026-06-25/2026-06-25-15-14-22_polished_rcim_runtime_log_wording.md)
  Technical plan for replacing legacy `original-dataset exact` runtime log
  wording in the reused RCIM model-bank runner with dataset-aware polished
  campaign progress messages and explicit dataset-root diagnostics.

- [technical/2026-06/2026-06-25/2026-06-25-13-25-15_polished_rcim_surface_resume_and_report_wording.md](./technical/2026-06/2026-06-25/2026-06-25-13-25-15_polished_rcim_surface_resume_and_report_wording.md)
  Technical plan for adding forward/backward-only resume support to the
  polished `RCIM Model-Bank Reproduction` launcher and correcting
  dataset-aware validation report wording.

#### 2026-06-22

- [technical/2026-06/2026-06-22/2026-06-22-22-55-55_polished_rcim_and_full_wave_retraining_campaigns.md](./technical/2026-06/2026-06-22/2026-06-22-22-55-55_polished_rcim_and_full_wave_retraining_campaigns.md)
  Technical plan for preparing separate `polished_dataset`
  `RCIM Model-Bank Reproduction` and full model-development wave retraining
  campaigns, including the canonical name mapping introduced by the latest wave
  renaming pass.

- [technical/2026-06/2026-06-22/2026-06-22-18-16-56_canonical_wave_model_family_renaming.md](./technical/2026-06/2026-06-22/2026-06-22-18-16-56_canonical_wave_model_family_renaming.md)
  Technical plan for replacing remaining `track2f`, `track2g`, `track2h`,
  and inconsistent `wave3` model-family names with canonical wave-based future
  identifiers while preserving historical artifact traceability.

- [technical/2026-06/2026-06-22/2026-06-22-16-50-24_polished_stage1_smoke_closeout.md](./technical/2026-06/2026-06-22/2026-06-22-16-50-24_polished_stage1_smoke_closeout.md)
  Technical plan for closing out the completed polished Stage 1 smoke
  campaign, preserving failed/interrupted attempt history, producing the
  Markdown/PDF campaign-results report, and keeping `TE Curve Verification
  Pipeline` refresh as a separate follow-up.

- [technical/2026-06/2026-06-22/2026-06-22-12-54-25_dataloader_worker_auto_sizing.md](./technical/2026-06/2026-06-22/2026-06-22-12-54-25_dataloader_worker_auto_sizing.md)
  Technical plan for adding safe `auto` dataloader worker sizing, preserving
  smoke-test determinism, and preventing polished Stage 1 from starting the
  first feedforward run with `num_workers: 0`.

- [technical/2026-06/2026-06-22/2026-06-22-12-26-09_polished_stage1_checkpoint_reload_fix.md](./technical/2026-06/2026-06-22/2026-06-22-12-26-09_polished_stage1_checkpoint_reload_fix.md)
  Technical plan for repairing the polished Stage 1 `input_size: auto`
  best-checkpoint reload failure, extending validation coverage, and
  reconciling the protected campaign state after the failed local launch.

#### 2026-06-21

- [technical/2026-06/2026-06-21/2026-06-21-03-26-07_polished_dataset_default_and_program_retraining.md](./technical/2026-06/2026-06-21/2026-06-21-03-26-07_polished_dataset_default_and_program_retraining.md)
  Technical plan for making polished point measurements the default dataset,
  preserving simplified compatibility, and preparing full program retraining.

- [technical/2026-06/2026-06-21/2026-06-21-00-38-59_final_te_renaming_documentation_consistency.md](./technical/2026-06/2026-06-21/2026-06-21-00-38-59_final_te_renaming_documentation_consistency.md)
  Technical plan for removing the final two reader-facing inconsistencies from
  the completed TE and dataset renaming documentation.

#### 2026-06-20

- [technical/2026-06/2026-06-20/2026-06-20-17-35-49_complete_te_and_dataset_renaming_audit.md](./technical/2026-06/2026-06-20/2026-06-20-17-35-49_complete_te_and_dataset_renaming_audit.md)
  Technical plan for auditing every current repository file against the TE
  taxonomy and canonical simplified-dataset path migrations.

- [technical/2026-06/2026-06-20/2026-06-20-15-46-15_te_naming_audit_and_pdf_regeneration.md](./technical/2026-06/2026-06-20/2026-06-20-15-46-15_te_naming_audit_and_pdf_regeneration.md)
  Technical plan for auditing the TE terminology migration across repository
  sources and regenerating maintained report PDFs that retain stale labels.

- [technical/2026-06/2026-06-20/2026-06-20-12-49-43_te_program_naming_taxonomy_migration.md](./technical/2026-06/2026-06-20/2026-06-20-12-49-43_te_program_naming_taxonomy_migration.md)
  Technical plan for separating the RCIM model-bank reproduction, model
  development waves, and TE curve-verification pipeline terminology.

- [technical/2026-06/2026-06-20/2026-06-20-11-53-54_polished_dataset_generator_progress_logging.md](./technical/2026-06/2026-06-20/2026-06-20-11-53-54_polished_dataset_generator_progress_logging.md)
  Technical plan for correcting the relocated standalone generator paths and
  adding aligned `tqdm` progress logging to both active generator surfaces.

- [technical/2026-06/2026-06-20/2026-06-20-10-38-02_polished_dataset_generator_repository_integration.md](./technical/2026-06/2026-06-20/2026-06-20-10-38-02_polished_dataset_generator_repository_integration.md)
  Technical plan for minimally repairing the complete standalone polished
  dataset generator and maintaining a path-adapted complete repository copy.

- [technical/2026-06/2026-06-20/2026-06-20-09-07-56_dataset_family_reference_documentation.md](./technical/2026-06/2026-06-20/2026-06-20-09-07-56_dataset_family_reference_documentation.md)
  Technical plan for auditing the raw, simplified, and polished transmission
  error datasets and creating canonical future-use reference documentation.

- [technical/2026-06/2026-06-20/2026-06-20-01-16-39_repository_dataset_path_migration.md](./technical/2026-06/2026-06-20/2026-06-20-01-16-39_repository_dataset_path_migration.md)
  Technical plan for replacing every tracked textual `data/simplified_dataset` reference
  with `data/simplified_dataset` across active configuration, scripts,
  documentation, reports, and stored textual artifacts.

#### 2026-06-19

- [technical/2026-06/2026-06-19/2026-06-19-22-48-02_original_and_polished_dataset_github_publication.md](./technical/2026-06/2026-06-19/2026-06-19-22-48-02_original_and_polished_dataset_github_publication.md)
  Technical plan for publishing the complete raw and polished datasets through
  deterministic sub-1-GB commits and separate pushes without Git LFS.

- [technical/2026-06/2026-06-19/2026-06-19-21-46-54_simplified_dataset_github_publication.md](./technical/2026-06/2026-06-19/2026-06-19-21-46-54_simplified_dataset_github_publication.md)
  Technical plan for publishing the complete replacement dataset under
  `data/simplified_dataset/` through bounded Git commits and pushes while
  excluding the separate original and polished dataset trees.

#### 2026-06-18

- [technical/2026-06/2026-06-18/2026-06-18-15-07-27_track2h_latent_state_hysteresis_track2_analysis_preparation.md](./technical/2026-06/2026-06-18/2026-06-18-15-07-27_track2h_latent_state_hysteresis_track2_analysis_preparation.md)
  Technical plan for preparing the separate official `TE Curve Verification Pipeline` verification
  refresh for the completed `Wave 4.4` latent-state / hysteresis-aware
  candidates after the multi-index curve-first policy and artifact
  reorganization.

- [technical/2026-06/2026-06-18/2026-06-18-14-50-13_campaign_artifact_naming_reorganization.md](./technical/2026-06/2026-06-18/2026-06-18-14-50-13_campaign_artifact_naming_reorganization.md)
  Technical plan for consolidating campaign-result and `TE Curve Verification Pipeline` artifact
  naming around canonical filesystem slugs, display names, migration manifests,
  and verified reference updates.

#### 2026-06-16

- [technical/2026-06/2026-06-16/2026-06-16-15-51-03_te_program_status_closeout_ledger.md](./technical/2026-06/2026-06-16/2026-06-16-15-51-03_te_program_status_closeout_ledger.md)
  Technical plan for creating the maintained TE program-status ledger and
  adding it to future campaign closeout governance.

- [technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md](./technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md)
  Technical plan for aligning post-`Wave 5.1` `TE Curve Verification Pipeline` status and preparing
  the next `Wave 4.4` latent-state / hysteresis-aware campaign package.

- [technical/2026-06/2026-06-17/2026-06-17-01-27-10_track2h_latent_state_hysteresis_closeout.md](./technical/2026-06/2026-06-17/2026-06-17-01-27-10_track2h_latent_state_hysteresis_closeout.md)
  Technical closeout note for accepting the completed `Wave 4.4`
  latent-state / hysteresis-aware campaign results, producing the final report
  and PDF, and clearing active campaign state while keeping official
  `TE Curve Verification Pipeline` curve verification separate.

- [technical/2026-06/2026-06-16/2026-06-16-12-37-49_wave3_track2_pdf_asset_path_repair.md](./technical/2026-06/2026-06-16/2026-06-16-12-37-49_wave3_track2_pdf_asset_path_repair.md)
  Technical plan for shortening verbose `Wave 5.1` `TE Curve Verification Pipeline` visual-report asset
  paths and regenerating the styled PDFs after the failed image render.

#### 2026-06-15

- [technical/2026-06/2026-06-15/2026-06-15-17-54-41_wave3_track2_verification_refresh.md](./technical/2026-06/2026-06-15/2026-06-15-17-54-41_wave3_track2_verification_refresh.md)
  Technical plan for preparing the separate official `TE Curve Verification Pipeline` verification
  refresh for the completed first real `Wave 5.1` harmonic-prior residual
  candidates.

- [technical/2026-06/2026-06-15/2026-06-15-16-45-47_aries_cpu_slurm_guide_update.md](./technical/2026-06/2026-06-15/2026-06-15-16-45-47_aries_cpu_slurm_guide_update.md)
  Technical plan for adding CPU-oriented Aries `srun` and `sbatch` examples to
  the cluster user guide.

- [technical/2026-06/2026-06-15/2026-06-15-15-42-48_wave3_harmonic_prior_residual_closeout.md](./technical/2026-06/2026-06-15/2026-06-15-15-42-48_wave3_harmonic_prior_residual_closeout.md)
  Technical closeout note for the completed first real `Wave 5.1`
  harmonic-prior residual campaign, including report, PDF, active-state
  cleanup, and separate `TE Curve Verification Pipeline` boundary.

- [technical/2026-06/2026-06-15/2026-06-15-13-27-18_remote_conda_utf8_no_capture_hardening.md](./technical/2026-06/2026-06-15/2026-06-15-13-27-18_remote_conda_utf8_no_capture_hardening.md)
  Technical plan for hardening shared remote campaign Conda execution against
  Windows CP1252 stdout replay failures by using UTF-8 and no-capture output.

#### 2026-06-14

- [technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md](./technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md)
  Technical plan for preparing the first real `Wave 5.1`
  harmonic-prior residual campaign package after completed `Wave 4 series`
  dispersion-aware verification.

- [technical/2026-06/2026-06-14/2026-06-14-16-49-23_track2_refresh_self_contained_report_closure.md](./technical/2026-06/2026-06-14/2026-06-14-16-49-23_track2_refresh_self_contained_report_closure.md)
  Technical plan for making `TE Curve Verification Pipeline` verification refresh launchers generate
  the official decision report and PDF package directly, so completed operator
  runs do not require manual report regeneration during closure.

#### 2026-06-13

- [technical/2026-06/2026-06-13/2026-06-13-15-15-12_track2h_mixture_density_heads_track2_verification_refresh.md](./technical/2026-06/2026-06-13/2026-06-13-15-15-12_track2h_mixture_density_heads_track2_verification_refresh.md)
  Technical note for preparing the separate operator-launched official
  `TE Curve Verification Pipeline` verification refresh for the six completed `Wave 4 series`
  mixture-density heads candidates, including deterministic mixture-expectation
  playback handling.

- [technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md](./technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md)
  Technical note for preparing the next `Wave 4 series` dispersion-aware package
  around mixture-density heads before latent-state, `Wave 5.1`, `Wave 5.2`, or
  integrated multi-head stages.

- [technical/2026-06/2026-06-13/2026-06-13-10-13-17_track2_visual_builder_auto_group_coverage.md](./technical/2026-06/2026-06-13/2026-06-13-10-13-17_track2_visual_builder_auto_group_coverage.md)
  Technical note for making `TE Curve Verification Pipeline` visual builders cover newly added
  registry-model source groups automatically and fail operator launchers when
  matrix candidates are missing from collage or overlay reports.

#### 2026-06-12

- [technical/2026-06/2026-06-12/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton.md](./technical/2026-06/2026-06-12/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton.md)
  Technical note for preparing a non-campaign `Wave 5.1` grouped harmonic-heads
  skeleton while the separate `Wave 4.2` quantile / probabilistic campaign
  runs elsewhere.

- [technical/2026-06/2026-06-12/2026-06-12-14-30-46_track2h_quantile_probabilistic_track2_verification_refresh.md](./technical/2026-06/2026-06-12/2026-06-12-14-30-46_track2h_quantile_probabilistic_track2_verification_refresh.md)
  Technical note for preparing the separate operator-launched official
  `TE Curve Verification Pipeline` verification refresh for the six completed `Wave 4 series`
  quantile/probabilistic candidates, including deterministic `p50` / `mu`
  playback handling.

- [technical/2026-06/2026-06-12/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton.md](./technical/2026-06/2026-06-12/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton.md)
  Technical note for preparing a non-campaign `Wave 5.2B` MMT feature-generator
  skeleton while the separate `Wave 4.2` quantile / probabilistic campaign
  runs elsewhere.

#### 2026-06-11

- [technical/2026-06/2026-06-11/2026-06-11-23-49-15_track2h_quantile_probabilistic_package.md](./technical/2026-06/2026-06-11/2026-06-11-23-49-15_track2h_quantile_probabilistic_package.md)
  Technical note for preparing the `Wave 4.2` dispersion-aware package
  around quantile and Gaussian probabilistic regression candidates before the
  later mixture-density, latent-state, and multi-head stages.

- [technical/2026-06/2026-06-11/2026-06-11-14-57-02_track2h_track2_verification_refresh.md](./technical/2026-06/2026-06-11/2026-06-11-14-57-02_track2h_track2_verification_refresh.md)
  Plan the separate operator-launched official `TE Curve Verification Pipeline` verification refresh
  for the nine completed `Wave 4.1` robust-loss candidates, preserving
  `global`, `Fw`, and `Bw` as parallel decision surfaces.

- [technical/2026-06/2026-06-11/2026-06-11-20-29-51_wave4a_mmt_parameter_inventory.md](./technical/2026-06/2026-06-11/2026-06-11-20-29-51_wave4a_mmt_parameter_inventory.md)
  Technical note for turning the current `Wave 5.2A` MMT diagnostic-only state
  into a parameter-inventory and calibration-gate artifact before `Wave 5.2B`
  feature generation or `Wave 5.2C` weak MMT losses.

- [technical/2026-06/2026-06-11/2026-06-11-19-54-42_wave3_wave4_backlog_state_alignment.md](./technical/2026-06/2026-06-11/2026-06-11-19-54-42_wave3_wave4_backlog_state_alignment.md)
  Technical note for aligning the operational backlog and training master
  summary with the committed `Wave 5.1` training-smoke-ready and `Wave 5.2A`
  diagnostic-only pre-implementation state.

- [technical/2026-06/2026-06-11/2026-06-11-19-25-32_wave3_wave4_parallel_hardening.md](./technical/2026-06/2026-06-11/2026-06-11-19-25-32_wave3_wave4_parallel_hardening.md)
  Technical note for hardening the `Wave 5.1` skeleton toward training-smoke
  readiness and adding the first `Wave 5.2A` MMT diagnostic report generator
  while `Wave 4 series` continues separately.

- [technical/2026-06/2026-06-11/2026-06-11-15-10-02_wave3_wave4_embryonic_skeletons.md](./technical/2026-06/2026-06-11/2026-06-11-15-10-02_wave3_wave4_embryonic_skeletons.md)
  Technical note for preparing `Wave 5.1` and `Wave 5.2` embryonic skeletons as
  implementation-ready but not campaign-ready.

- [technical/2026-06/2026-06-11/2026-06-11-12-23-30_wave4_pinn_formulation_design.md](./technical/2026-06/2026-06-11/2026-06-11-12-23-30_wave4_pinn_formulation_design.md)
  Technical note for opening the non-invasive `Wave 5.2` PINN formulation
  design step while the separate `Wave 4 series` campaign runs elsewhere.

- [technical/2026-06/2026-06-11/2026-06-11-13-10-10_wave4_pinn_equation_expansion.md](./technical/2026-06/2026-06-11/2026-06-11-13-10-10_wave4_pinn_equation_expansion.md)
  Technical note for expanding `Wave 5.2` into staged MMT-equation,
  mesh-stiffness, loaded-TE, backlash/preload, cycloid-contact, and
  planetary-LSTE exploratory PINN branches.

- [technical/2026-06/2026-06-11/2026-06-11-14-59-42_wave4_subbranch_design_package.md](./technical/2026-06/2026-06-11/2026-06-11-14-59-42_wave4_subbranch_design_package.md)
  Technical note for creating the complete `Wave 5.2A` through `Wave 5.2G`
  sub-branch design package.

- [technical/2026-06/2026-06-11/2026-06-11-12-02-00_wave3_hybrid_structured_model_design.md](./technical/2026-06/2026-06-11/2026-06-11-12-02-00_wave3_hybrid_structured_model_design.md)
  Technical note for opening the non-invasive `Wave 5.1` hybrid structured
  model design step while the separate `Wave 4 series` campaign runs elsewhere.

#### 2026-06-10

- [technical/2026-06/2026-06-10/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probes.md](./technical/2026-06/2026-06-10/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probes.md)
  Technical plan for the `Wave 4 series` dispersion-aware modeling probe branch,
  covering robust losses, uncertainty heads, mixture-density heads, and
  causal latent-state / hysteresis-aware features.

- [technical/2026-06/2026-06-10/2026-06-10-16-18-08_rebase_documentation_repair.md](./technical/2026-06/2026-06-10/2026-06-10-16-18-08_rebase_documentation_repair.md)
  Technical note for repairing documentation-only rebase artifacts in the
  training master summary after combining `Wave 3.3` official verification
  with the dispersion-aware roadmap update.

- [technical/2026-06/2026-06-10/2026-06-10-15-18-10_track2_dispersion_aware_wave_roadmap.md](./technical/2026-06/2026-06-10/2026-06-10-15-18-10_track2_dispersion_aware_wave_roadmap.md)
  Technical note for updating the `TE Curve Verification Pipeline` roadmap with dispersion-aware
  probes, hybrid structured models, first-PINN work, and a later integrated
  multi-task / multi-head stage.

#### 2026-06-09

- [technical/2026-06/2026-06-09/2026-06-09-18-22-15_track2_component_offset_identification_plan.md](./technical/2026-06/2026-06-09/2026-06-09-18-22-15_track2_component_offset_identification_plan.md)
  Plan the separate `TE Curve Verification Pipeline` diagnostic branch for identifying whether the
  observed curve offset is dominated by `a_0` / `Component 0`, multiple
  harmonics, or experiment-condition variability before opening another
  training campaign.

- [technical/2026-06/2026-06-09/2026-06-09-13-11-16_track2g_track2_verification_refresh.md](./technical/2026-06/2026-06-09/2026-06-09-13-11-16_track2g_track2_verification_refresh.md)
  Plan the separate operator-launched official `TE Curve Verification Pipeline` verification refresh
  for the twelve completed `Wave 3.3` curve-aware candidates, preserving
  `global`, `Fw`, and `Bw` as parallel decision surfaces.

#### 2026-06-08

- [technical/2026-06/2026-06-08/2026-06-08-19-11-41_portable_original_onnx_curve_plotter.md](./technical/2026-06/2026-06-08/2026-06-08-19-11-41_portable_original_onnx_curve_plotter.md)
  Plan the repository-independent original paper `ONNX` curve plotter for
  user-provided curve `CSV` files and sparse harmonic selections.

- [technical/2026-06/2026-06-08/2026-06-08-17-59-03_track2g_curve_aware_training_plan.md](./technical/2026-06/2026-06-08/2026-06-08-17-59-03_track2g_curve_aware_training_plan.md)
  Plan the `Wave 3.3` curve-aware training branch after `Wave 3.1` and
  `Wave 3.2`, preserving causal point or short-history runtime inputs
  while testing composite curve loss and multi-head shape/offset modeling for
  separate `global`, `Fw`, and `Bw` decision surfaces.

- [technical/2026-06/2026-06-08/2026-06-08-13-46-58_track2_forward_reference_curve_comparison_report.md](./technical/2026-06/2026-06-08/2026-06-08-13-46-58_track2_forward_reference_curve_comparison_report.md)
  Plan the combined forward `TE Curve Verification Pipeline` reference-curve comparison report across
  paper-original, paper-retuned, full original `ONNX`, and sparse original
  `ONNX` candidates.

- [technical/2026-06/2026-06-08/2026-06-08-13-30-17_rcim_original_sparse_onnx_track2_variants.md](./technical/2026-06/2026-06-08/2026-06-08-13-30-17_rcim_original_sparse_onnx_track2_variants.md)
  Plan the simplified and PLC-oriented sparse original `ONNX` forward
  `TE Curve Verification Pipeline` variants over harmonics `0`, `1`, `39`, and `40`.

- [technical/2026-06/2026-06-08/2026-06-08-12-53-28_track2f_bis_official_track2_refresh_preparation.md](./technical/2026-06/2026-06-08/2026-06-08-12-53-28_track2f_bis_official_track2_refresh_preparation.md)
  Plan the operator-launched official `TE Curve Verification Pipeline` verification refresh for the
  completed `Wave 3.2` harmonic-offset probe, preserving clean and
  harmonic candidates for `global`, `Fw`, and `Bw` as parallel curve-first
  comparison surfaces.

- [technical/2026-06/2026-06-08/2026-06-08-12-32-29_original_onnx_fw_collage_pdf_table_width_repair.md](./technical/2026-06/2026-06-08/2026-06-08-12-32-29_original_onnx_fw_collage_pdf_table_width_repair.md)
  Plan the table-width repair for the simple original paper `ONNX` forward
  `TE Curve Verification Pipeline` collage PDF.

#### 2026-06-05

- [technical/2026-06/2026-06-05/2026-06-05-16-02-33_original_onnx_fw_track2_collage_pdf_and_standalone_plotter.md](./technical/2026-06/2026-06-05/2026-06-05-16-02-33_original_onnx_fw_track2_collage_pdf_and_standalone_plotter.md)
  Plan the simple original paper `ONNX` forward `TE Curve Verification Pipeline` collage PDF and
  standalone hardcoded-ONNX curve plotter.

- [technical/2026-06/2026-06-05/2026-06-05-15-56-59_track2f_bis_campaign_runner_model_type_fix.md](./technical/2026-06/2026-06-05/2026-06-05-15-56-59_track2f_bis_campaign_runner_model_type_fix.md)
  Plan the Wave 3.2 runner fix that registers
  `harmonic_residual_offset_probe` in the campaign runner, then reruns only
  the three failed harmonic-offset entries before normal closeout.

#### 2026-06-04

- [technical/2026-06/2026-06-04/2026-06-04-23-32-17_original_onnx_track2_offset_diagnostic.md](./technical/2026-06/2026-06-04/2026-06-04-23-32-17_original_onnx_track2_offset_diagnostic.md)
  Plan the focused diagnostic that loads recovered original RCIM paper ONNX
  models through `TE Curve Verification Pipeline` and checks whether the investigated mean-offset
  error pattern is present in the original ONNX release.

- [technical/2026-06/2026-06-04/2026-06-04-21-14-52_track2f_bis_harmonic_offset_probe.md](./technical/2026-06/2026-06-04/2026-06-04-21-14-52_track2f_bis_harmonic_offset_probe.md)
  Plan the Wave 3.2 harmonic-offset probe that keeps the clean
  non-harmonic Wave 3.1 branch as a control while adding an explicit harmonic
  shape branch plus causal offset branch for separate `global`, `Fw`, and `Bw`
  comparisons.

- [technical/2026-06/2026-06-04/2026-06-04-21-07-46_track2f_clean_baseline_and_harmonic_offset_followup.md](./technical/2026-06/2026-06-04/2026-06-04-21-07-46_track2f_clean_baseline_and_harmonic_offset_followup.md)
  Plan the Wave 3.1 follow-up documentation update that records
  `sequential_residual_offset_probe` as a clean non-harmonic baseline and
  keeps it in future comparisons against harmonic-offset, multi-head, new
  index, and composite-loss model branches.

- [technical/2026-06/2026-06-04/2026-06-04-16-31-58_track2f_official_track2_refresh_preparation.md](./technical/2026-06/2026-06-04/2026-06-04-16-31-58_track2f_official_track2_refresh_preparation.md)
  Plan the operator-launched official `TE Curve Verification Pipeline` verification refresh for the
  completed `Wave 3.1` offset-aware probe, preserving separate `global`, `Fw`,
  and `Bw` branch candidates and preparing local plus `-Remote` launcher
  commands without running the heavy matrix inside Codex.

- [technical/2026-06/2026-06-04/2026-06-04-16-28-04_track2_curve_reconstruction_documentation.md](./technical/2026-06/2026-06-04/2026-06-04-16-28-04_track2_curve_reconstruction_documentation.md)
  Plan the detailed `TE Curve Verification Pipeline` curve-reconstruction documentation covering
  repository models, paper-original reference banks, collage plotting, and
  mean-centered diagnostic context.

- [technical/2026-06/2026-06-04/2026-06-04-12-47-33_track2f_closeout_pdf_refinement_and_skill_rule.md](./technical/2026-06/2026-06-04/2026-06-04-12-47-33_track2f_closeout_pdf_refinement_and_skill_rule.md)
  Plan the `Wave 3.1` closeout PDF refinement that starts `Execution Summary`
  on a fresh page and updates the campaign closeout skill so generated PDFs
  are always reviewed and repaired before finalization.

- [technical/2026-06/2026-06-04/2026-06-04-12-28-46_track2f_campaign_closeout.md](./technical/2026-06/2026-06-04/2026-06-04-12-28-46_track2f_campaign_closeout.md)
  Plan the completed `Wave 3.1` campaign closeout, including the final
  campaign-results Markdown/PDF deliverable, wrapper-error review, active-state
  cleanup, and explicit preservation of separate `global`, `Fw`, and `Bw`
  best-model branches.

- [technical/2026-06/2026-06-04/2026-06-04-11-15-13_track2f_launcher_exit_flow_fix.md](./technical/2026-06/2026-06-04/2026-06-04-11-15-13_track2f_launcher_exit_flow_fix.md)
  Plan the protected Wave 3.1 launcher fix that prevents Python validation
  stdout from being captured as a false launcher error before the sequential
  training campaign starts.

#### 2026-06-03

- [technical/2026-06/2026-06-03/2026-06-03-18-18-20_track2f_sequential_residual_offset_probe.md](./technical/2026-06/2026-06-03/2026-06-03-18-18-20_track2f_sequential_residual_offset_probe.md)
  Plan the first learned `Wave 3.1` implementation step by adding the
  `sequential_residual_offset_probe` model type and converting the prepared
  sequential descriptors into runnable campaign entries.

- [technical/2026-06/2026-06-03/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md](./technical/2026-06/2026-06-03/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md)
  Plan the `Wave 3.1` offset-aware probe campaign gate that compares
  post-hoc `direction_torque` calibration, sequential residual-offset
  modeling, and multi-head shape/offset training across `Fw`, `Bw`, and
  `global` surfaces.

- [technical/2026-06/2026-06-03/2026-06-03-11-40-21_track2e_offset_predictability_feasibility.md](./technical/2026-06/2026-06-03/2026-06-03-11-40-21_track2e_offset_predictability_feasibility.md)
  Plan the `CVP 1.5` offset-predictability feasibility diagnostic that uses
  completed `CVP 1.4` artifacts to decide whether the next branch should be
  loss reweighting, multi-head shape/offset modeling, sequential offset
  modeling, post-hoc offset calibration, or a non-offset-first intervention.

- [technical/2026-06/2026-06-03/2026-06-03-10-49-06_track2d_pdf_table_layout_rules.md](./technical/2026-06/2026-06-03/2026-06-03-10-49-06_track2d_pdf_table_layout_rules.md)
  Plan the `CVP 1.4` styled-PDF table layout correction and reusable
  generator rule for future mean-offset diagnostic reports.

- [technical/2026-06/2026-06-03/2026-06-03-00-08-04_track2d_mean_offset_full_matrix_audit.md](./technical/2026-06/2026-06-03/2026-06-03-00-08-04_track2d_mean_offset_full_matrix_audit.md)
  Plan the `CVP 1.4` full-matrix audit that decomposes every official
  direction-valid `TE Curve Verification Pipeline` candidate into raw error, curve offset,
  centered-shape error, amplitude error, harmonic phase error, and
  condition-regime behavior before new curve-aware training is opened.

#### 2026-06-02

- [technical/2026-06/2026-06-02/2026-06-02-23-21-05_track2_mean_offset_resolution_strategy.md](./technical/2026-06/2026-06-02/2026-06-02-23-21-05_track2_mean_offset_resolution_strategy.md)
  Plan the documentation update that incorporates the `TE Curve Verification Pipeline`
  mean-centered diagnostic, explains the mean-offset failure mode, and adds the
  next full-matrix offset audit plus curve-aware training strategy.

- [technical/2026-06/2026-06-02/2026-06-02-12-40-01_track2_mean_centered_collage_diagnostics.md](./technical/2026-06/2026-06-02/2026-06-02-12-40-01_track2_mean_centered_collage_diagnostics.md)
  Plan the `TE Curve Verification Pipeline` mean-centered collage diagnostics report that tests
  whether persistent prediction offsets hide stronger TE curve-shape tracking.

- [technical/2026-06/2026-06-02/2026-06-02-12-24-15_technical_document_index_chronological_order.md](./technical/2026-06/2026-06-02/2026-06-02-12-24-15_technical_document_index_chronological_order.md)
  Technical document for reordering the `doc/README.md` technical-document
  index in reverse chronological order while preserving existing links and
  summaries.

#### 2026-05-29

- [technical/2026-05/2026-05-29/2026-05-29-12-23-56_direction_parallel_best_policy.md](./technical/2026-05/2026-05-29/2026-05-29-12-23-56_direction_parallel_best_policy.md)
  Plan the documentation correction that keeps `Fw`, `Bw`, and `global`
  best-model surfaces as parallel branches instead of one single competition.

#### 2026-05-28

- [technical/2026-05/2026-05-28/2026-05-28-19-33-44_track2c_curve_payload_diagnostics.md](./technical/2026-05/2026-05-28/2026-05-28-19-33-44_track2c_curve_payload_diagnostics.md)
  Plan the `CVP 1.2` curve-payload diagnostics pass that will export selected
  truth/prediction curves and measure harmonic, phase, slope, smoothness, and
  stitched-revolution behavior before new training is opened.

- [technical/2026-05/2026-05-28/2026-05-28-18-21-51_repository_status_wave_track_synthesis_pdf_export.md](./technical/2026-05/2026-05-28/2026-05-28-18-21-51_repository_status_wave_track_synthesis_pdf_export.md)
  Plan the styled PDF export and validation pass for the repository status,
  Wave, and `TE Curve Verification Pipeline` synthesis report.

- [technical/2026-05/2026-05-28/2026-05-28-16-59-09_track2b_curve_first_reranking.md](./technical/2026-05/2026-05-28/2026-05-28-16-59-09_track2b_curve_first_reranking.md)
  Plan the `CVP 1.1` curve-first reranking pass that standardizes existing
  `TE Curve Verification Pipeline` curve metrics before opening new training-loss or model-family
  work.

- [technical/2026-05/2026-05-28/2026-05-28-16-58-12_repository_status_wave_track_synthesis_report.md](./technical/2026-05/2026-05-28/2026-05-28-16-58-12_repository_status_wave_track_synthesis_report.md)
  Plan the repository status synthesis report covering current repository
  state, `Wave 1`, `Wave 2.1`, `Wave 2.2`, `Wave 2.3`, `TE Curve Verification Pipeline` outcomes,
  sparse `RCIM` versus dense harmonic-bank results, and the future development
  path including commit `b73220679410276246421b7e2832d8878cff90a0`.

- [technical/2026-05/2026-05-28/2026-05-28-16-44-36_causal_input_constraint_clarification.md](./technical/2026-05/2026-05-28/2026-05-28-16-44-36_causal_input_constraint_clarification.md)
  Plan the causal-input clarification for the curve-first TE strategy so
  future models are evaluated on full curves while still consuming only the
  current point, a short causal history, or derived causal features at runtime.

- [technical/2026-05/2026-05-28/2026-05-28-16-32-36_curve_first_te_training_strategy.md](./technical/2026-05/2026-05-28/2026-05-28-16-32-36_curve_first_te_training_strategy.md)
  Plan the curve-first TE training strategy research and documentation refresh
  so future `Wave 1` / `Wave 2.1` follow-up work is judged by continuous
  TE Curve Verification Pipeline curve-following quality, not only scalar pointwise `MAE`.

- [technical/2026-05/2026-05-28/2026-05-28-12-10-21_wave2c_track2_verification_refresh.md](./technical/2026-05/2026-05-28/2026-05-28-12-10-21_wave2c_track2_verification_refresh.md)
  Plan the optional `Wave 2.3` `TE Curve Verification Pipeline` verification refresh, including the
  matrix candidate update, local and `-Remote` operator launcher, visual report
  regeneration, official decision report, and status synchronization.

- [technical/2026-05/2026-05-28/2026-05-28-11-38-20_wave2c_remote_repository_path_fallback.md](./technical/2026-05/2026-05-28/2026-05-28-11-38-20_wave2c_remote_repository_path_fallback.md)
  Plan the `Wave 2.3` remote launcher fallback fix so `-Remote` uses the
  established LAN repository clone path when the environment variable is unset.

- [technical/2026-05/2026-05-28/2026-05-28-11-35-34_wave2c_campaign_closeout.md](./technical/2026-05/2026-05-28/2026-05-28-11-35-34_wave2c_campaign_closeout.md)
  Plan the completed `Wave 2.3` campaign closeout: verify the 18-run
  residual-harmonic temporal hybrid artifact surface, generate the Markdown and
  PDF results report, clear active campaign state, and keep `TE Curve Verification Pipeline` as a
  separate operator-approved follow-up.

#### 2026-05-27

- [technical/2026-05/2026-05-27/2026-05-27-18-35-06_campaign_launcher_remote_execution_standard.md](./technical/2026-05/2026-05-27/2026-05-27-18-35-06_campaign_launcher_remote_execution_standard.md)
  Plan the protected `Wave 2.3` launcher retrofit that adds `-Remote` execution
  plus the repository rule that future campaign launchers must sync required
  sources before remote execution and artifacts after completion.

- [technical/2026-05/2026-05-27/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrids.md](./technical/2026-05/2026-05-27/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrids.md)
  Plan the `Wave 2.3` residual harmonic temporal hybrid branch that uses a
  structured harmonic base with `GRU` and `LSTM` residual sequence branches.

- [technical/2026-05/2026-05-27/2026-05-27-17-51-45_track2_incremental_visual_artifact_sync.md](./technical/2026-05/2026-05-27/2026-05-27-17-51-45_track2_incremental_visual_artifact_sync.md)
  Plan the `TE Curve Verification Pipeline` refresh cleanup that keeps incremental matrix runs and
  remote artifact synchronization focused on new candidate visual artifacts
  instead of regenerating or resynchronizing closed `Wave 1` PNG history.

#### 2026-05-26

- [technical/2026-05/2026-05-26/2026-05-26-14-01-40_campaign_closeout_and_manual_track2_gate.md](./technical/2026-05/2026-05-26/2026-05-26-14-01-40_campaign_closeout_and_manual_track2_gate.md)
  Plan the revised campaign-closeout workflow that separates normal campaign
  closeout from optional operator-launched `TE Curve Verification Pipeline` verification, including
  local and `-Remote` launcher preparation before any heavy TE Curve Verification Pipeline run.

#### 2026-05-25

- [technical/2026-05/2026-05-25/2026-05-25-03-17-26_wave2b_harmonic_temporal_hybrids.md](./technical/2026-05/2026-05-25/2026-05-25-03-17-26_wave2b_harmonic_temporal_hybrids.md)
  Plan the `Wave 2.2` harmonic-temporal hybrid branch that applies explicit
  periodic harmonic feature expansion to the temporal convolution, `GRU`, and
  `LSTM` sequence families before a campaign package is prepared.

- [technical/2026-05/2026-05-25/2026-05-25-03-06-07_track2_verification_refresh_skill.md](./technical/2026-05/2026-05-25/2026-05-25-03-06-07_track2_verification_refresh_skill.md)
  Plan the repository-local Codex skill that captures the post-campaign
  `TE Curve Verification Pipeline` verification refresh workflow: matrix update, visual PDF
  regeneration, official report decision, status updates, QA, and commit
  preflight.

#### 2026-05-24

- [technical/2026-05/2026-05-24/2026-05-24-12-36-49_wave2_closeout_and_track2_refresh_plan.md](./technical/2026-05/2026-05-24/2026-05-24-12-36-49_wave2_closeout_and_track2_refresh_plan.md)
  Plan the `Wave 2.1` temporal-model campaign closeout and the follow-on
  official `TE Curve Verification Pipeline` model-verification refresh required before temporal
  candidates are accepted.

#### 2026-05-21

- [technical/2026-05/2026-05-21/2026-05-21-16-46-08_wave2_temporal_model_entry_plan.md](./technical/2026-05/2026-05-21/2026-05-21-16-46-08_wave2_temporal_model_entry_plan.md)
  Plan the opening of `Wave 2.1` as the temporal-model branch, starting from
  lightweight temporal convolution, `GRU`, and `LSTM` sequence baselines while
  preserving the `global` / `Fw` / `Bw` verification rule and official `Track
  2` closeout workflow.

- [technical/2026-05/2026-05-21/2026-05-21-15-09-15_track2_official_model_verification_report.md](./technical/2026-05/2026-05-21/2026-05-21-15-09-15_track2_official_model_verification_report.md)
  Plan the official `TE Curve Verification Pipeline` model-verification report that consolidates the
  directional metric matrix, best-model collage PDF, multi-model curve
  comparison PDF, and future `TE Curve Verification Pipeline` campaign results into one maintained
  closeout surface.

- [technical/2026-05/2026-05-21/2026-05-21-13-23-42_track2_periodic_mlp_harmonic_report_refresh.md](./technical/2026-05/2026-05-21/2026-05-21-13-23-42_track2_periodic_mlp_harmonic_report_refresh.md)
  Plan the `TE Curve Verification Pipeline` visual report refresh that updates the existing
  `[2026-05-20]` best-model collage and multi-model curve comparison PDFs
  with the newly trained explicit-harmonic `periodic_mlp` family winners.

#### 2026-05-20

- [technical/2026-05/2026-05-20/2026-05-20-22-34-11_periodic_mlp_explicit_harmonic_basis.md](./technical/2026-05/2026-05-20/2026-05-20-22-34-11_periodic_mlp_explicit_harmonic_basis.md)
  Plan the narrow `periodic_mlp` extension that accepts explicit harmonic
  index lists while keeping the pure `feedforward` baseline unchanged and
  leaving the future `Fourier-Feature MLP` family separate.

- [technical/2026-05/2026-05-20/2026-05-20-22-10-13_track3_online_compensation_backlog_formalization.md](./technical/2026-05/2026-05-20/2026-05-20-22-10-13_track3_online_compensation_backlog_formalization.md)
  Plan the documentation-only formalization of future `Track 3` as the online
  compensation, TestRig/TwinCAT, and `Target B` / `Table 9` branch.

- [technical/2026-05/2026-05-20/2026-05-20-20-28-08_target_a_offline_closeout.md](./technical/2026-05/2026-05-20/2026-05-20-20-28-08_target_a_offline_closeout.md)
  Plan the documentation-only closeout of `Target A` as an offline
  direction-qualified paper-comparable benchmark, leaving online compensation
  under `Target B`.

- [technical/2026-05/2026-05-20/2026-05-20-20-27-06_track2_multi_model_curve_comparison_report.md](./technical/2026-05/2026-05-20/2026-05-20-20-27-06_track2_multi_model_curve_comparison_report.md)
  Plan the `TE Curve Verification Pipeline` multi-model overlay report comparing original TE curves,
  reference best models, and screened Wave 1 family-best models.

- [technical/2026-05/2026-05-20/2026-05-20-19-17-04_track2_backward_retuned_baseline_rule.md](./technical/2026-05/2026-05-20/2026-05-20-19-17-04_track2_backward_retuned_baseline_rule.md)
  Plan the `TE Curve Verification Pipeline` and `Target A` documentation rule that uses
  `paper_retuned_best_Bw` as the canonical backward baseline when no
  paper-original backward reference exists.

- [technical/2026-05/2026-05-20/2026-05-20-17-37-09_track2_best_model_collage_pdf_report.md](./technical/2026-05/2026-05-20/2026-05-20-17-37-09_track2_best_model_collage_pdf_report.md)
  Plan the `TE Curve Verification Pipeline` styled PDF report with four-curve collages for the best
  paper-reference, RCIM Model-Bank Reproduction, Wave 1 directional, and Wave 1 global models.

#### 2026-05-19

- [technical/2026-05/2026-05-19/2026-05-19-17-32-08_wave1_high_order_harmonic_tracking.md](./technical/2026-05/2026-05-19/2026-05-19-17-32-08_wave1_high_order_harmonic_tracking.md)
  Plan the `Wave 1` follow-up for sparse RCIM and dense high-order harmonic
  bases in `harmonic_regression` and `residual_harmonic_mlp`, motivated by
  `TE Curve Verification Pipeline` curve smoothing against multi-harmonic TE truth curves.

- [technical/2026-05/2026-05-19/2026-05-19-16-40-26_wave1_future_waves_hydra_config_transition.md](./technical/2026-05/2026-05-19/2026-05-19-16-40-26_wave1_future_waves_hydra_config_transition.md)
  Plan the gradual `Hydra` configuration transition for `Wave 1` and future
  waves while keeping closed `RCIM Model-Bank Reproduction` exact-paper workflows stable unless a
  future non-faithful branch opts in.

- [technical/2026-05/2026-05-19/2026-05-19-16-27-02_rcim_archive_parity_interpretation_and_gbm_grid_fix.md](./technical/2026-05/2026-05-19/2026-05-19-16-27-02_rcim_archive_parity_interpretation_and_gbm_grid_fix.md)
  Plan the refined `rcim_original`, `rcim_retuned`, and `rcim_track1` archive
  parity interpretation plus the RCIM Model-Bank Reproduction GBM grid transcription fix.

- [technical/2026-05/2026-05-19/2026-05-19-15-10-17_obsolete_training_artifact_cleanup.md](./technical/2026-05/2026-05-19/2026-05-19-15-10-17_obsolete_training_artifact_cleanup.md)
  Plan the conservative cleanup of obsolete training, validation, campaign,
  smoke-test, and Git LFS artifacts while preserving registries and accepted
  model archives.

- [technical/2026-05/2026-05-19/2026-05-19-15-00-46_te_model_live_backlog_alignment.md](./technical/2026-05/2026-05-19/2026-05-19-15-00-46_te_model_live_backlog_alignment.md)
  Plan the documentation-only cleanup of the TE model live backlog after the
  recovered original pipeline, retuned reference archive, closed `RCIM Model-Bank Reproduction`,
  active `TE Curve Verification Pipeline`, and directional `Wave 1` rule updates.

- [technical/2026-05/2026-05-19/2026-05-19-10-21-12_analysis_report_reorganization.md](./technical/2026-05/2026-05-19/2026-05-19-10-21-12_analysis_report_reorganization.md)
  Plan the topic-root reorganization of `doc/reports/analysis/`, including
  validation-check report consolidation, RCIM paper-reference grouping, Wave 1
  grouping, and utility report grouping.

- [technical/2026-05/2026-05-19/2026-05-19-09-50-45_paper_reference_parity_command_env_rename_fix.md](./technical/2026-05/2026-05-19/2026-05-19-09-50-45_paper_reference_parity_command_env_rename_fix.md)
  Plan the stale Conda environment-name correction in the paper-reference
  archive parity report command.

#### 2026-05-18

- [technical/2026-05/2026-05-18/2026-05-18-22-27-08_clear_completed_active_campaign_state.md](./technical/2026-05/2026-05-18/2026-05-18-22-27-08_clear_completed_active_campaign_state.md)
  Plan the cleanup of the completed active campaign state so
  `doc/running/active_training_campaign.yaml` no longer protects closed
  campaign files.

- [technical/2026-05/2026-05-18/2026-05-18-22-18-31_conda_environment_rename.md](./technical/2026-05/2026-05-18/2026-05-18-22-18-31_conda_environment_rename.md)
  Plan the repository-wide Conda environment rename from
  `pinns_env` to `pinns_env` and from `pinns_lan_env` to
  `pinns_lan_env`.

- [technical/2026-05/2026-05-18/2026-05-18-22-01-35_rcim_paper_reference_archive_parity_report.md](./technical/2026-05/2026-05-18/2026-05-18-22-01-35_rcim_paper_reference_archive_parity_report.md)
  Plan the repository-local parity report comparing `rcim_original`,
  `rcim_retuned`, and `rcim_track1` archives under `models/paper_reference`.

- [technical/2026-05/2026-05-18/2026-05-18-21-53-46_rcim_original_onnx_parity_interpretation_report.md](./technical/2026-05/2026-05-18/2026-05-18-21-53-46_rcim_original_onnx_parity_interpretation_report.md)
  Plan the canonical interpretation report for the recovered original ONNX
  release parity validation.

- [technical/2026-05/2026-05-18/2026-05-18-20-26-23_rcim_original_onnx_release_parity_validation.md](./technical/2026-05/2026-05-18/2026-05-18-20-26-23_rcim_original_onnx_release_parity_validation.md)
  Plan the forward-only parity validation between the recovered original ONNX
  release, `Tables 2-5`, and the current `rcim_original` TE Curve Verification Pipeline baseline.

- [technical/2026-05/2026-05-18/2026-05-18-20-18-29_rcim_paper_original_table_audit.md](./technical/2026-05/2026-05-18/2026-05-18-20-18-29_rcim_paper_original_table_audit.md)
  Plan the RCIM paper-original table audit and Table 2 marker refresh after
  corrected Table 2 original values.

- [technical/2026-05/2026-05-18/2026-05-18-19-59-32_track2_best_composite_report_visibility_fix.md](./technical/2026-05/2026-05-18/2026-05-18-19-59-32_track2_best_composite_report_visibility_fix.md)
  Plan the `TE Curve Verification Pipeline` report visibility fix that promotes composed best-reference
  models into a dedicated canonical comparison section.

- [technical/2026-05/2026-05-18/2026-05-18-15-37-22_track2_composite_best_reference_models.md](./technical/2026-05/2026-05-18/2026-05-18-15-37-22_track2_composite_best_reference_models.md)
  Plan the `TE Curve Verification Pipeline` composed best-reference candidates assembled from the
  selected paper original, retuned, and RCIM Model-Bank Reproduction harmonic cells.

- [technical/2026-05/2026-05-18/2026-05-18-12-20-17_track2_direction_truth_and_preview_audit.md](./technical/2026-05/2026-05-18/2026-05-18-12-20-17_track2_direction_truth_and_preview_audit.md)
  Plan the `TE Curve Verification Pipeline` direction/truth audit after preview-curve sign concerns,
  plus complete grouped PNG generation under `doc/reports/campaign_results/track_2/verification_plots/`.

- [technical/2026-05/2026-05-18/2026-05-18-11-50-19_track2_report_grouped_source_tables.md](./technical/2026-05/2026-05-18/2026-05-18-11-50-19_track2_report_grouped_source_tables.md)
  Plan the `TE Curve Verification Pipeline` report readability refinement that groups comparison
  tables by original, retuned, RCIM Model-Bank Reproduction, and Wave 1 source families.

- [technical/2026-05/2026-05-18/2026-05-18-10-03-13_track2_original_and_retuned_reference_matrix_extension.md](./technical/2026-05/2026-05-18/2026-05-18-10-03-13_track2_original_and_retuned_reference_matrix_extension.md)
  Plan the next `TE Curve Verification Pipeline` matrix extension for `rcim_original` forward-only and
  `rcim_retuned` forward/backward paper-reference archives from `models/`.

- [technical/2026-05/2026-05-18/2026-05-18-00-53-52_track2_full_directional_matrix_report.md](./technical/2026-05/2026-05-18/2026-05-18-00-53-52_track2_full_directional_matrix_report.md)
  Plan the full `TE Curve Verification Pipeline` directional comparison matrix and standalone report,
  replacing the obsolete mixed `LGBM-19` comparison with `RCIM Model-Bank Reproduction` and `Wave 1`
  model artifacts loaded from `models/`.

#### 2026-05-17

- [technical/2026-05/2026-05-17/2026-05-17-19-01-32_track2_directional_comparison_pipeline_alignment.md](./technical/2026-05/2026-05-17/2026-05-17-19-01-32_track2_directional_comparison_pipeline_alignment.md)
  Plan the direction-aware `TE Curve Verification Pipeline` comparison pipeline, including `RCIM Model-Bank Reproduction`
  forward/backward family banks, `Wave 1` global and directional models, and
  canonical `data/simplified_dataset` loading for future waves.

- [technical/2026-05/2026-05-17/2026-05-17-18-48-59_wave1_campaign_output_taxonomy_repair.md](./technical/2026-05/2026-05-17/2026-05-17-18-48-59_wave1_campaign_output_taxonomy_repair.md)
  Plan the filesystem and metadata repair that moves two completed `Wave 1`
  campaign bundles from the flat `output/training_campaigns/` root into the
  canonical `output/training_campaigns/wave1/` taxonomy.

- [technical/2026-05/2026-05-17/2026-05-17-18-02-23_track1_closure_documentation_alignment.md](./technical/2026-05/2026-05-17/2026-05-17-18-02-23_track1_closure_documentation_alignment.md)
  Plan the documentation-only closure update for `RCIM Model-Bank Reproduction` after completed
  forward and backward paper-faithful campaigns, with a deferred
  restricted-dataset rerun backlog item.

- [technical/2026-05/2026-05-17/2026-05-17-11-40-42_wave1_directional_hpo_closeout_and_export_refresh.md](./technical/2026-05/2026-05-17/2026-05-17-11-40-42_wave1_directional_hpo_closeout_and_export_refresh.md)
  Plan the closeout for the completed `Wave 1` directional best-hyperparameter
  campaign, including bounded-grid and `Optuna` result consolidation, winner
  hyperparameter verification, and refreshed Python plus ONNX exports.

#### 2026-05-16

- [technical/2026-05/2026-05-16/2026-05-16-20-46-00_rcim_original_pipeline_documentation_alignment.md](./technical/2026-05/2026-05-16/2026-05-16-20-46-00_rcim_original_pipeline_documentation_alignment.md)
  Plan the documentation alignment for the recovered RCIM original pipeline,
  faithful exact-model-bank reimplementation, RCIM Model-Bank Reproduction campaigns, benchmark
  tables, and paper-reference model archives.

- [technical/2026-05/2026-05-16/2026-05-16-20-14-35_small_exact_model_bank_lfs_pointer_conversion.md](./technical/2026-05/2026-05-16/2026-05-16-20-14-35_small_exact_model_bank_lfs_pointer_conversion.md)
  Plan the multi-commit conversion of small exact-model-bank
  `paper_family_model_bank.pkl` LFS pointers into normal Git blobs.

- [technical/2026-05/2026-05-16/2026-05-16-20-07-07_track1_backward_paper_faithful_closeout_and_reference_refresh.md](./technical/2026-05/2026-05-16/2026-05-16-20-07-07_track1_backward_paper_faithful_closeout_and_reference_refresh.md)
  Plan the RCIM Model-Bank Reproduction backward paper-faithful campaign closeout, backward
  paper-reference model archive replacement, linked report updates, and RCIM
  Tables `2`-`5` benchmark recompilation.

- [technical/2026-05/2026-05-16/2026-05-16-20-04-43_git_lfs_exact_model_bank_threshold_cleanup.md](./technical/2026-05/2026-05-16/2026-05-16-20-04-43_git_lfs_exact_model_bank_threshold_cleanup.md)
  Plan the Git LFS threshold cleanup for exact-model-bank validation artifacts
  so only required oversized `paper_family_model_bank.pkl` files remain tracked
  through LFS.

- [technical/2026-05/2026-05-16/2026-05-16-12-28-37_python_entrypoint_platform_flag_plan.md](./technical/2026-05/2026-05-16/2026-05-16-12-28-37_python_entrypoint_platform_flag_plan.md)
  Plan the Python-entrypoint Linux portability tranche that adds a uniform
  `--linux` / `--windows` command-line contract to the remaining runnable
  scripts.

#### 2026-05-15

- [technical/2026-05/2026-05-15/2026-05-15-21-12-21_aries_cluster_user_guide_plan.md](./technical/2026-05/2026-05-15/2026-05-15-21-12-21_aries_cluster_user_guide_plan.md)
  Plan the Unimore Aries cluster user guide covering SSH access, GitHub SSH setup, repository clone, Conda environment setup, Slurm interactive tests, and first batch submission.

- [technical/2026-05/2026-05-15/2026-05-15-19-46-50_repository_wide_linux_portability_tranche2_campaign_launcher_plan.md](./technical/2026-05/2026-05-15/2026-05-15-19-46-50_repository_wide_linux_portability_tranche2_campaign_launcher_plan.md)
  Plan the second repository-wide Linux portability tranche, starting from
  protected campaign launcher Bash equivalents and the shared launcher helper.

- [technical/2026-05/2026-05-15/2026-05-15-16-20-20_repository_wide_linux_script_portability_plan.md](./technical/2026-05/2026-05-15/2026-05-15-16-20-20_repository_wide_linux_script_portability_plan.md)
  Plan the repository-wide Linux portability pass so every runnable script is
  either Linux-runnable, has a Linux equivalent, or is explicitly classified as
  Windows-only with a documented replacement.

- [technical/2026-05/2026-05-15/2026-05-15-13-18-01_unimore_aries_linux_portability_plan.md](./technical/2026-05/2026-05-15/2026-05-15-13-18-01_unimore_aries_linux_portability_plan.md)
  Plan the Linux portability pass for Unimore Aries, including platform-aware
  repository-relative paths and Bash equivalents for RCIM Model-Bank Reproduction campaign
  launchers.

- [technical/2026-05/2026-05-15/2026-05-15-12-10-04_track1_forward_closeout_pdf_table_layout_refinement.md](./technical/2026-05/2026-05-15/2026-05-15-12-10-04_track1_forward_closeout_pdf_table_layout_refinement.md)
  Plan the reusable styled-PDF table layout refinement for the RCIM Model-Bank Reproduction forward
  paper-faithful closeout report.

- [technical/2026-05/2026-05-15/2026-05-15-11-11-35_track1_forward_paper_faithful_closeout_and_reference_refresh.md](./technical/2026-05/2026-05-15/2026-05-15-11-11-35_track1_forward_paper_faithful_closeout_and_reference_refresh.md)
  Plan the RCIM Model-Bank Reproduction forward paper-faithful campaign closeout, paper-reference
  model archive replacement, linked report updates, and RCIM Tables `2`-`5`
  benchmark recompilation.

#### 2026-05-14

- [technical/2026-05/2026-05-14/2026-05-14-11-32-41_rcim_retuned_report_family_metric_row_selection_fix.md](./technical/2026-05/2026-05-14/2026-05-14-11-32-41_rcim_retuned_report_family_metric_row_selection_fix.md)
  Plan the recovered-original RCIM retuned report fix that selects the matching
  family row from multi-row eval summaries before regenerating retuned Tables
  `2`-`5` and the styled closeout PDF.

- [technical/2026-05/2026-05-14/2026-05-14-00-07-31_track1_svr_parameter_grid_yaml_serialization_fix.md](./technical/2026-05/2026-05-14/2026-05-14-00-07-31_track1_svr_parameter_grid_yaml_serialization_fix.md)
  Plan the RCIM Model-Bank Reproduction exact-paper validation-summary fix that serializes search
  `parameter_grid` metadata before YAML output so estimator objects from the
  `SVR` branch cannot crash post-export campaign bookkeeping.

#### 2026-05-13

- [technical/2026-05/2026-05-13/2026-05-13-18-22-31_track1_remote_source_sync_temp_directory_fix.md](./technical/2026-05/2026-05-13/2026-05-13-18-22-31_track1_remote_source_sync_temp_directory_fix.md)
  Plan the protected remote launcher fix that creates the remote `.temp`
  directory before uploading the source-sync archive with `scp`.

- [technical/2026-05/2026-05-13/2026-05-13-17-33-38_track1_paper_faithful_elm_queue_completion.md](./technical/2026-05/2026-05-13/2026-05-13-17-33-38_track1_paper_faithful_elm_queue_completion.md)
  Plan the protected RCIM Model-Bank Reproduction paper-faithful queue update that adds forward and
  backward `ELM` YAML entries for the `11`-family launcher command.

- [technical/2026-05/2026-05-13/2026-05-13-16-50-46_rcim_retuned_closeout_pdf_table_layout_refinement.md](./technical/2026-05/2026-05-13/2026-05-13-16-50-46_rcim_retuned_closeout_pdf_table_layout_refinement.md)
  Plan the narrow styled-PDF table layout refinement for the recovered-original
  RCIM retuned closeout report.

- [technical/2026-05/2026-05-13/2026-05-13-16-10-09_rcim_retuned_archive_closeout_and_benchmark_reset.md](./technical/2026-05/2026-05-13/2026-05-13-16-10-09_rcim_retuned_archive_closeout_and_benchmark_reset.md)
  Plan the recovered-original RCIM retuned-model closeout, archive promotion,
  detailed PDF reporting, and canonical paper-reference benchmark reset.

- [technical/2026-05/2026-05-13/2026-05-13-14-14-43_rcim_original_live_log_backpressure_fix.md](./technical/2026-05/2026-05-13/2026-05-13-14-14-43_rcim_original_live_log_backpressure_fix.md)
  Plan the recovered-original RCIM launcher follow-up fix that keeps complete
  persisted stage logs while eliminating the new live-log backpressure path
  that can stall verbose retune runs.

#### 2026-05-12

- [technical/2026-05/2026-05-12/2026-05-12-20-31-03_rcim_original_launcher_live_log_capture_fix.md](./technical/2026-05/2026-05-12/2026-05-12-20-31-03_rcim_original_launcher_live_log_capture_fix.md)
  Plan the recovered-original RCIM launcher fix that replaces unreliable
  PowerShell transcript capture with explicit live stdout/stderr mirroring into
  persistent stage logs.

- [technical/2026-05/2026-05-12/2026-05-12-20-20-40_wave1_optuna_launcher_native_terminal_streaming_restore.md](./technical/2026-05/2026-05-12/2026-05-12-20-20-40_wave1_optuna_launcher_native_terminal_streaming_restore.md)
  Restore native terminal-visible `PyTorch Lightning` progress streaming for
  the `Wave 1` neural `Optuna` launcher while keeping the interpreter and
  persisted-study recovery hardening already added.

- [technical/2026-05/2026-05-12/2026-05-12-18-24-51_requirements_dependency_cleanup.md](./technical/2026-05/2026-05-12/2026-05-12-18-24-51_requirements_dependency_cleanup.md)
  Plan the cleanup of the root, documentation, LAN-node, and recovered-original
  Python requirement surfaces after a repository-wide import and workflow audit.

- [technical/2026-05/2026-05-12/2026-05-12-18-00-33_rcim_original_hgbm_onnx_export_scalar_sanitization.md](./technical/2026-05/2026-05-12/2026-05-12-18-00-33_rcim_original_hgbm_onnx_export_scalar_sanitization.md)
  Plan the narrow recovered-original RCIM `HGBM` ONNX export fix that
  sanitizes histogram-tree scalar types during `skl2onnx` conversion without
  changing training or evaluation behavior.

- [technical/2026-05/2026-05-12/2026-05-12-10-49-02_wave1_directional_hpo_optuna_launcher_recovery_and_micro_validation.md](./technical/2026-05/2026-05-12/2026-05-12-10-49-02_wave1_directional_hpo_optuna_launcher_recovery_and_micro_validation.md)
  Diagnose the failed Wave 1 directional HPO launcher, recover the blocked
  neural `Optuna` study phase, validate the launcher fix through a lightweight
  micro-campaign, and define the closeout conditions for the full directional
  best-hyperparameter campaign.

#### 2026-05-11

- [technical/2026-05/2026-05-11/2026-05-11-19-35-52_optuna_hpo_integration_for_wave1_and_future_waves.md](./technical/2026-05/2026-05-11/2026-05-11-19-35-52_optuna_hpo_integration_for_wave1_and_future_waves.md)
  Plan the promotion of `Optuna` into the canonical neural-family
  hyperparameter-optimization layer for `Wave 1` directional retuning and
  future `Wave 2.1+` model families.

- [technical/2026-05/2026-05-11/2026-05-11-19-20-20_wave1_directional_best_hyperparameter_grid_search_campaign.md](./technical/2026-05/2026-05-11/2026-05-11-19-20-20_wave1_directional_best_hyperparameter_grid_search_campaign.md)
  Plan the bounded best-hyperparameter grid-search campaign for the `15`
  directional `Wave 1` winner surfaces, including explicit GPU-preferred
  execution for neural families and CPU-throttled handling for non-neural
  families.

- [technical/2026-05/2026-05-11/2026-05-11-15-39-02_rcim_original_lgbm_retune_log_flood_and_failure_capture_fix.md](./technical/2026-05/2026-05-11/2026-05-11-15-39-02_rcim_original_lgbm_retune_log_flood_and_failure_capture_fix.md)
  Plan the narrow recovered-original RCIM `LGBM` retune fix that suppresses
  unusable LightGBM log flooding while preserving repository-owned progress
  lines and persistent failure capture.

- [technical/2026-05/2026-05-11/2026-05-11-10-05-21_rcim_original_elm_onnx_export_feature_shape_fix.md](./technical/2026-05/2026-05-11/2026-05-11-10-05-21_rcim_original_elm_onnx_export_feature_shape_fix.md)
  Plan the narrow recovered-original RCIM exporter fix that restores ONNX
  export for fitted `ELMRegressor` targets without changing the training or
  stage semantics.

- [technical/2026-05/2026-05-11/2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md](./technical/2026-05/2026-05-11/2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md)
  Plan the exact-paper export alignment that restores recovered-original-style
  per-target Python plus ONNX export artifacts instead of ONNX-only per-target
  exports.

#### 2026-05-09

- [technical/2026-05/2026-05-09/2026-05-09-21-15-08_rcim_original_svr_pragmatic_linear_fallback.md](./technical/2026-05/2026-05-09/2026-05-09-21-15-08_rcim_original_svr_pragmatic_linear_fallback.md)
  Plan one explicit recovered-original workflow deviation that preserves the paper-faithful SVR RBF branch while replacing the impractical SVR linear branch with a pragmatic StandardScaler plus LinearSVR fallback for retune and best-parameter reload flows.

- [technical/2026-05/2026-05-09/2026-05-09-13-13-36_rcim_original_svr_linear_retune_temp_diagnostics.md](./technical/2026-05/2026-05-09/2026-05-09-13-13-36_rcim_original_svr_linear_retune_temp_diagnostics.md)
  Plan the temporary `temp/`-only diagnostic pass for the recovered-original
  RCIM `SVR` backward retune path to test a tiny mixed `rbf` plus `linear`
  search, estimate the runtime of the full original search, and evaluate a
  regression-appropriate fallback such as `LinearSVR`.

- [technical/2026-05/2026-05-09/2026-05-09-12-10-13_rcim_original_best_parameter_parser_rf_recovery_fix.md](./technical/2026-05/2026-05-09/2026-05-09-12-10-13_rcim_original_best_parameter_parser_rf_recovery_fix.md)
  Plan the narrow recovered-original RCIM parser fix that preserves completed
  `RF` retune artifacts and restores the downstream `Eval` and `Export`
  recovery path without re-running the expensive retune stage.

- [technical/2026-05/2026-05-09/2026-05-09-08-54-10_track1_forward_dt_historical_replay_outcome_table_width_rebalance.md](./technical/2026-05/2026-05-09/2026-05-09-08-54-10_track1_forward_dt_historical_replay_outcome_table_width_rebalance.md)
  Plan the narrow styled-PDF refinement that equalizes the three metric
  columns and widens `Scope` in the `Historical Replay Outcome` table of the
  `forward + DT` paper-faithful subset closeout report.

#### 2026-05-08

- [technical/2026-05/2026-05-08/2026-05-08-19-50-40_track1_forward_dt_paper_faithful_search_closeout.md](./technical/2026-05/2026-05-08/2026-05-08-19-50-40_track1_forward_dt_paper_faithful_search_closeout.md)
  Plan the closeout for the successful single-run `forward + DT + search`
  exact-paper subset bundle without mutating the canonical interrupted state of
  the parent `20`-run paper-faithful campaign.

- [technical/2026-05/2026-05-08/2026-05-08-16-58-27_track1_exact_paper_write_progress_completed_activity_fix.md](./technical/2026-05/2026-05-08/2026-05-08-16-58-27_track1_exact_paper_write_progress_completed_activity_fix.md)
  Plan the narrow exact-paper wrapper fix that adds the missing `-Activity`
  argument to sub-progress `Write-Progress -Completed` calls so remote
  launchers stop prompting interactively.

- [technical/2026-05/2026-05-08/2026-05-08-15-40-54_track1_exact_paper_families_alias_and_csv_support.md](./technical/2026-05/2026-05-08/2026-05-08-15-40-54_track1_exact_paper_families_alias_and_csv_support.md)
  Plan the narrow follow-up that keeps the new exact-paper `-Family` launcher
  surface but also adds a recovered-original-style `-Families` alias that
  accepts either one value or a CSV family list.

- [technical/2026-05/2026-05-08/2026-05-08-15-16-17_track1_exact_paper_family_stage_launcher_and_live_progress_rework.md](./technical/2026-05/2026-05-08/2026-05-08-15-16-17_track1_exact_paper_family_stage_launcher_and_live_progress_rework.md)
  Plan the exact-paper launcher rework that records the interrupted
  paper-faithful campaign, adds a family-and-stage operator surface analogous
  to the recovered-original launcher, and greatly improves live progress
  visibility during search and historical cross-validation.

- [technical/2026-05/2026-05-08/2026-05-08-11-49-11_rcim_original_launcher_foreground_console_and_transcript_fix.md](./technical/2026-05/2026-05-08/2026-05-08-11-49-11_rcim_original_launcher_foreground_console_and_transcript_fix.md)
  Plan the next recovered-original RCIM launcher repair that removes the
  still-interfering relay layer, restores native foreground-console
  `GridSearchCV` verbosity, and re-establishes a clean `Ctrl+C` contract while
  keeping persistent stage logs.

- [technical/2026-05/2026-05-08/2026-05-08-00-57-25_rcim_original_launcher_process_relay_and_console_attachment_fix.md](./technical/2026-05/2026-05-08/2026-05-08-00-57-25_rcim_original_launcher_process_relay_and_console_attachment_fix.md)
  Plan the second recovered-original RCIM launcher repair that fixes the
  process relay so the PowerShell wrapper stays attached to the real training
  stage and preserves the same live console contract as the direct Python
  command.

- [technical/2026-05/2026-05-08/2026-05-08-00-39-20_rcim_original_launcher_live_output_and_ctrl_c_fix.md](./technical/2026-05/2026-05-08/2026-05-08-00-39-20_rcim_original_launcher_live_output_and_ctrl_c_fix.md)
  Plan the shared recovered-original RCIM launcher fix that restores the full
  high-verbosity live retune output and clean `Ctrl+C` interruption behavior
  that the direct Python command already exposes.

#### 2026-05-07

- [technical/2026-05/2026-05-07/2026-05-07-22-58-44_rcim_original_launcher_direct_env_python_preference.md](./technical/2026-05/2026-05-07/2026-05-07-22-58-44_rcim_original_launcher_direct_env_python_preference.md)
  Plan the narrow launcher hardening that makes the shared recovered-original
  RCIM training stages prefer the Conda environment-local `python.exe` over
  `conda run` when live progress streaming reliability matters.

- [technical/2026-05/2026-05-07/2026-05-07-16-39-56_rcim_recovered_workflow_readme_retune_verbose_command_completion.md](./technical/2026-05/2026-05-07/2026-05-07-16-39-56_rcim_recovered_workflow_readme_retune_verbose_command_completion.md)
  Plan the narrow documentation-only follow-up that adds the missing unified
  launcher retune-verbosity command example to the recovered-original RCIM
  workflow README.

- [technical/2026-05/2026-05-07/2026-05-07-15-58-15_rcim_exact_paper_workflow_readme_expansion.md](./technical/2026-05/2026-05-07/2026-05-07-15-58-15_rcim_exact_paper_workflow_readme_expansion.md)
  Plan the expansion of the root `rcim_ml_compensation` README into an
  operator-facing exact-paper workflow guide with commands, stage control, and
  pipeline structure comparable in depth to the recovered-original README.

- [technical/2026-05/2026-05-07/2026-05-07-15-18-56_track1_exact_paper_detailed_progress_logging_and_stage_control_alignment.md](./technical/2026-05/2026-05-07/2026-05-07-15-18-56_track1_exact_paper_detailed_progress_logging_and_stage_control_alignment.md)
  Plan the observability and launcher-control alignment that makes the
  exact-paper RCIM Model-Bank Reproduction reimplementation expose frequent live progress and a
  stage-aware operator flow analogous to the unified recovered-original RCIM
  launcher.

- [technical/2026-05/2026-05-07/2026-05-07-15-00-31_rcim_original_retune_progress_logging_and_monitoring.md](./technical/2026-05/2026-05-07/2026-05-07-15-00-31_rcim_original_retune_progress_logging_and_monitoring.md)
  Plan the observability pass that makes the recovered-original RCIM retune
  stage emit readable live progress and incremental log updates without
  changing the historical nested search protocol.

- [technical/2026-05/2026-05-07/2026-05-07-14-14-12_training_results_master_summary_directional_sectioning_and_future_wave_policy.md](./technical/2026-05/2026-05-07/2026-05-07-14-14-12_training_results_master_summary_directional_sectioning_and_future_wave_policy.md)
  Plan the formal promotion of `global` / `Fw` / `Bw` scope-separated tables
  and grids inside the canonical training-results master summary for `Wave 1`,
  and define the same reporting contract for all future multi-scope waves.

- [technical/2026-05/2026-05-07/2026-05-07-13-40-00_wave1_exported_archive_provenance_alignment.md](./technical/2026-05/2026-05-07/2026-05-07-13-40-00_wave1_exported_archive_provenance_alignment.md)
  Plan the follow-up alignment that upgrades `models/exported/` from a
  binary-only Wave 1 delivery surface to a provenance-rich archive with local
  inventories, source-run snapshots, and scope-level reconstruction metadata.

- [technical/2026-05/2026-05-07/2026-05-07-13-10-14_wave1_directional_retraining_closeout_and_exported_model_archive.md](./technical/2026-05/2026-05-07/2026-05-07-13-10-14_wave1_directional_retraining_closeout_and_exported_model_archive.md)
  Plan the closeout of the completed Wave 1 directional retraining campaign,
  including canonical summary updates, directional metadata repair, PDF-backed
  results reporting, and the curated `models/exported/` archive split by
  family and `global` / `forward` / `backward`.

#### 2026-05-06

- [technical/2026-05/2026-05-06/2026-05-06-15-53-01_wave1_directional_retraining_and_future_wave_extension.md](./technical/2026-05/2026-05-06/2026-05-06-15-53-01_wave1_directional_retraining_and_future_wave_extension.md)
  Plan the formal directional retraining of all implemented `Wave 1`
  families into `global`, `Fw`, and `Bw` variants, and promote the same
  three-surface rule into future `Wave 2.1+` family-preparation pipelines.

#### 2026-05-05

- [technical/2026-05/2026-05-05/2026-05-05-00-08-16_rcim_original_forward_reference_closeout.md](./technical/2026-05/2026-05-05/2026-05-05-00-08-16_rcim_original_forward_reference_closeout.md)
  Plan the closeout of the completed RCIM original forward reference bundle by
  promoting the exported family artifacts into the curated
  `models/paper_reference/rcim_original/forward` archive with the same
  family-level structure already used by `rcim_track1`.

#### 2026-05-04

- [technical/2026-05/2026-05-04/2026-05-04-23-14-36_rcim_recovered_workflow_readme_command_surface_completion.md](./technical/2026-05/2026-05-04/2026-05-04-23-14-36_rcim_recovered_workflow_readme_command_surface_completion.md)
  Plan the command-surface completion pass for the recovered-original RCIM
  workflow README so it consolidates the unified launcher, compatibility
  wrappers, and the main operator command examples in one practical location.

- [technical/2026-05/2026-05-04/2026-05-04-19-12-31_rcim_original_unified_launcher_and_best_parameter_flow.md](./technical/2026-05/2026-05-04/2026-05-04-19-12-31_rcim_original_unified_launcher_and_best_parameter_flow.md)
  Plan the unification of the recovered-original RCIM paper-reference launcher
  surface across `forward` and `backward`, including the new branch/stage CLI
  model, automatic retune-to-eval-to-export chaining, and a repository-owned
  stored best-hyperparameter registry.

- [technical/2026-05/2026-05-04/2026-05-04-17-45-11_rcim_original_launcher_process_capture_fix.md](./technical/2026-05/2026-05-04/2026-05-04-17-45-11_rcim_original_launcher_process_capture_fix.md)
  Plan the fix for the shared recovered-original RCIM PowerShell launcher
  process-capture layer so stage logs are written correctly, successful
  stages stop exiting non-zero, and the automatic transition from
  `paper_eval` to `paper_export` becomes reliable.

- [technical/2026-05/2026-05-04/2026-05-04-15-36-05_rcim_original_training_surface_completion_and_launcher_hardening.md](./technical/2026-05/2026-05-04/2026-05-04-15-36-05_rcim_original_training_surface_completion_and_launcher_hardening.md)
  Plan the completion and hardening pass for the recovered original RCIM paper-reference workflow, including missing-family coverage, persistent launcher logging, progress reporting, output-root relocation, and ONNX/Python export alignment.

- [technical/2026-05/2026-05-04/2026-05-04-12-13-07_track1_paper_faithful_search_protocol_and_campaign_replacement.md](./technical/2026-05/2026-05-04/2026-05-04-12-13-07_track1_paper_faithful_search_protocol_and_campaign_replacement.md)
  Plan the missing exact-paper search-protocol alignment to the recovered original RCIM workflow, including the historical `cross_validate(...)` stage, and the replacement of the active `400`-run campaign with a paper-faithful `20`-run design.

#### 2026-05-03

- [technical/2026-05/2026-05-03/2026-05-03-13-23-46_track1_bidirectional_paper_faithful_grid_search_campaign_replacement.md](./technical/2026-05/2026-05-03/2026-05-03-13-23-46_track1_bidirectional_paper_faithful_grid_search_campaign_replacement.md)
  Plan the replacement of the active RCIM Model-Bank Reproduction bidirectional `400`-run literal-refresh mega campaign with a paper-faithful `20`-run grid-search campaign that performs exactly one search pass per family-direction surface.

#### 2026-05-02

- [technical/2026-05/2026-05-02/2026-05-02-12-31-12_rcim_original_reference_training_and_archive_plan.md](./technical/2026-05/2026-05-02/2026-05-02-12-31-12_rcim_original_reference_training_and_archive_plan.md)
  Plan the operator-run retraining of the recovered original RCIM workflow into `models/paper_reference/rcim_original/`, including the `forward` `v18` replay, the `backward` `v17` retuning step, and the current manual handoff gap before a valid `backward` tuned replay.

#### 2026-05-01

- [technical/2026-05/2026-05-01/2026-05-01-22-56-02_rcim_recovered_original_workflow_simplification_and_pickle_cache_relocation.md](./technical/2026-05/2026-05-01/2026-05-01-22-56-02_rcim_recovered_original_workflow_simplification_and_pickle_cache_relocation.md)
  Plan the next recovered RCIM workflow refactor that extracts repeated helper blocks, translates repository-owned Italian identifiers to English, and relocates the persistent pickle cache from per-run validation artifacts to a shared `data/` directory.

- [technical/2026-05/2026-05-01/2026-05-01-22-36-34_rcim_instance_variant_file_removal.md](./technical/2026-05/2026-05-01/2026-05-01-22-36-34_rcim_instance_variant_file_removal.md)
  Plan the final recovered RCIM instance-helper cleanup that removes `instance_v4.py` and `instance_v5.py` from the repository-owned workflow subtree and leaves `instance.py` as the sole active runtime helper.

- [technical/2026-05/2026-05-01/2026-05-01-22-22-33_rcim_instance_unification_and_v4_deactivation.md](./technical/2026-05/2026-05-01/2026-05-01-22-22-33_rcim_instance_unification_and_v4_deactivation.md)
  Plan the recovered RCIM instance-helper cleanup that promotes the active `instance_v5.py` runtime surface to `instance.py`, removes `instance_v4.py` from the active path, and records the migration plus future commit hash in the workflow README.

- [technical/2026-05/2026-05-01/2026-05-01-19-02-56_rcim_predictorml_comment_fill_and_capitalization_normalization.md](./technical/2026-05/2026-05-01/2026-05-01-19-02-56_rcim_predictorml_comment_fill_and_capitalization_normalization.md)
  Plan the narrow follow-up pass that fills standalone `#` comment placeholders and normalizes inline-comment capitalization inside the recovered RCIM `predictorML.py` helper without changing its logic.

- [technical/2026-05/2026-05-01/2026-05-01-12-06-00_rcim_instance_comment_fill_and_capitalization_normalization.md](./technical/2026-05/2026-05-01/2026-05-01-12-06-00_rcim_instance_comment_fill_and_capitalization_normalization.md)
  Plan the narrow follow-up pass that fills the standalone `#` comment placeholders in the recovered RCIM instance helpers and normalizes the capitalization of their inline comments.

- [technical/2026-05/2026-05-01/2026-05-01-11-01-49_rcim_recovered_original_workflow_utility_visual_style_normalization.md](./technical/2026-05/2026-05-01/2026-05-01-11-01-49_rcim_recovered_original_workflow_utility_visual_style_normalization.md)
  Plan the follow-up visual style-normalization pass over the recovered-original RCIM utility files so they match the repository-authored spacing, comment capitalization, and inline-comment density already established in the main workflow entrypoints.

- [technical/2026-05/2026-05-01/2026-05-01-01-38-44_rcim_recovered_original_workflow_utility_cleanup_and_style_alignment.md](./technical/2026-05/2026-05-01/2026-05-01-01-38-44_rcim_recovered_original_workflow_utility_cleanup_and_style_alignment.md)
  Plan the final utility-focused cleanup and style-alignment pass over the recovered-original RCIM workflow, limited to `instance_v4.py`, `instance_v5.py`, `predictorML.py`, and the adjacent workflow README.

- [technical/2026-05/2026-05-01/2026-05-01-00-42-42_rcim_recovered_original_workflow_comment_preserving_restore.md](./technical/2026-05/2026-05-01/2026-05-01-00-42-42_rcim_recovered_original_workflow_comment_preserving_restore.md)
  Plan a conservative restoration of the recovered-original RCIM workflow so the user-authored inline comments and local formatting are recovered from the `_old` backup copies and only minimal repository-style normalization is applied afterward.

#### 2026-04-30

- [technical/2026-04/2026-04-30/2026-04-30-10-33-46_rcim_recovered_original_workflow_style_cleanup_and_legacy_trim.md](./technical/2026-04/2026-04-30/2026-04-30-10-33-46_rcim_recovered_original_workflow_style_cleanup_and_legacy_trim.md)
  Plan a repository-style cleanup pass over the recovered-original RCIM workflow, focused on docstrings, comments, spacing, and removal of obsolete local residue while preserving numerical behavior.

- [technical/2026-04/2026-04-30/2026-04-30-10-10-06_rcim_recovered_original_workflow_stabilization_pass.md](./technical/2026-04/2026-04-30/2026-04-30-10-10-06_rcim_recovered_original_workflow_stabilization_pass.md)
  Plan the next stabilization pass for the rebuilt recovered-original RCIM workflow, focused on repository-owned path handling, clearer `Fw`/`Bw` semantics, and campaign-safe operational cleanup.

- [technical/2026-04/2026-04-30/2026-04-30-02-06-47_track1_bidirectional_literal_workflow_refresh_mega_campaign.md](./technical/2026-04/2026-04-30/2026-04-30-02-06-47_track1_bidirectional_literal_workflow_refresh_mega_campaign.md)
  Plan the full RCIM Model-Bank Reproduction bidirectional mega-campaign refresh after the exact-paper family bank was realigned to the recovered original workflow.

- [technical/2026-04/2026-04-30/2026-04-30-01-48-18_track1_literal_alignment_to_recovered_original_workflow.md](./technical/2026-04/2026-04-30/2026-04-30-01-48-18_track1_literal_alignment_to_recovered_original_workflow.md)
  Plan the literal alignment of the RCIM Model-Bank Reproduction exact-paper reimplementation to the recovered original RCIM workflow across all ten model families.

- [technical/2026-04/2026-04-30/2026-04-30-01-25-40_track1_forward_last_three_open_cells_overnight_mega_campaign_closeout.md](./technical/2026-04/2026-04-30/2026-04-30-01-25-40_track1_forward_last_three_open_cells_overnight_mega_campaign_closeout.md)
  Plan the formal closeout of the completed forward-only overnight mega campaign that targeted the last three non-green forward cells, including artifact audit, profile registration, benchmark refresh, archive refresh, and persistent state reconciliation.

#### 2026-04-29

- [technical/2026-04/2026-04-29/2026-04-29-18-22-46_original_dataset_exact_model_bank_validation_report_path_length_hardening.md](./technical/2026-04/2026-04-29/2026-04-29-18-22-46_original_dataset_exact_model_bank_validation_report_path_length_hardening.md)
  Plan the shared original-dataset exact-model-bank validation-report path hardening that repairs the failed overnight mega campaign and prevents future Windows path-length failures for the same validation-report surface.

- [technical/2026-04/2026-04-29/2026-04-29-17-59-02_track1_forward_last_three_open_cells_overnight_mega_campaign.md](./technical/2026-04/2026-04-29/2026-04-29-17-59-02_track1_forward_last_three_open_cells_overnight_mega_campaign.md)
  Planning gate for one overnight forward-only mega campaign that pushes a few hundred exact-paper retries against the last three non-green forward cells after the failed last-three-open-cells wave.

- [technical/2026-04/2026-04-29/2026-04-29-17-10-49_rcim_recovered_original_workflow_reset_and_direct_three_script_layout.md](./technical/2026-04/2026-04-29/2026-04-29-17-10-49_rcim_recovered_original_workflow_reset_and_direct_three_script_layout.md)
  Plan the reset of the repository-owned recovered RCIM workflow so it is rebuilt directly from the newly recovered original scripts into three direct entrypoints plus a `utilities/` module folder, without an external runner.

- [technical/2026-04/2026-04-29/2026-04-29-16-56-16_rcim_v17_v18_canonical_usage_alignment_and_backward_backlog.md](./technical/2026-04/2026-04-29/2026-04-29-16-56-16_rcim_v17_v18_canonical_usage_alignment_and_backward_backlog.md)
  Plan the RCIM documentation alignment that treats the author README as the canonical usage rule for `v17`, `v18`, and tuning, and records the future backward branch explicitly in the live backlog.

- [technical/2026-04/2026-04-29/2026-04-29-16-33-05_track1_forward_last_three_open_cells_campaign_closeout.md](./technical/2026-04/2026-04-29/2026-04-29-16-33-05_track1_forward_last_three_open_cells_campaign_closeout.md)
  Plan the formal closeout of the completed final forward-only last-three-open-cells campaign, including profile registration, benchmark refresh, archive refresh, and persistent state completion.

- [technical/2026-04/2026-04-29/2026-04-29-14-27-58_track1_forward_last_three_open_cells_campaign.md](./technical/2026-04/2026-04-29/2026-04-29-14-27-58_track1_forward_last_three_open_cells_campaign.md)
  Planning gate for the next forward-only exact-paper micro-campaign that targets the last three non-green forward cells remaining after the last-four-open-cells closeout.

- [technical/2026-04/2026-04-29/2026-04-29-13-42-13_track1_forward_last_four_open_cells_campaign_closeout.md](./technical/2026-04/2026-04-29/2026-04-29-13-42-13_track1_forward_last_four_open_cells_campaign_closeout.md)
  Plan the formal closeout of the completed final forward-only last-four-open-cells campaign, including profile registration, benchmark refresh, archive refresh, and persistent state completion.

- [technical/2026-04/2026-04-29/2026-04-29-11-55-47_track1_forward_last_four_open_cells_campaign.md](./technical/2026-04/2026-04-29/2026-04-29-11-55-47_track1_forward_last_four_open_cells_campaign.md)
  Planning gate for one final targeted forward exact-paper campaign to repair the last four open forward cells after the maxi wave closeout.

- [technical/2026-04/2026-04-29/2026-04-29-11-28-31_track1_forward_maxi_remote_artifact_recovery_and_closeout.md](./technical/2026-04/2026-04-29/2026-04-29-11-28-31_track1_forward_maxi_remote_artifact_recovery_and_closeout.md)
  Plan the full manual recovery of the remote artifact set for the interrupted
  forward maxi campaign and the formal closeout that follows from the recovered
  local copy.

- [technical/2026-04/2026-04-29/2026-04-29-01-37-16_track1_forward_maxi_last_non_green_cells_campaign.md](./technical/2026-04/2026-04-29/2026-04-29-01-37-16_track1_forward_maxi_last_non_green_cells_campaign.md)
  Plan the next forward-only RCIM Model-Bank Reproduction maxi campaign that targets the final `7`
  amplitude repair pairs with a few hundred exact-paper-safe retries.

- [technical/2026-04/2026-04-29/2026-04-29-00-45-52_rcim_original_pipeline_author_conversation_formalization.md](./technical/2026-04/2026-04-29/2026-04-29-00-45-52_rcim_original_pipeline_author_conversation_formalization.md)
  Plan the formalization of the newly recovered full RCIM original pipeline root, the author clarifications, and the resulting updates to the canonical recovered-asset documentation.

#### 2026-04-28

- [technical/2026-04/2026-04-28/2026-04-28-19-57-56_rcim_reference_code_root_reorganization.md](./technical/2026-04/2026-04-28/2026-04-28-19-57-56_rcim_reference_code_root_reorganization.md)
  Plan the reorganization of the recovered RCIM reference-code root so the full original repository lands under original_pipeline and the current split snapshots move into clearly named backup surfaces.

- [technical/2026-04/2026-04-28/2026-04-28-17-09-01_rewrite_recent_commits_and_separate_paper_reimplementation_from_campaign_artifacts.md](./technical/2026-04/2026-04-28/2026-04-28-17-09-01_rewrite_recent_commits_and_separate_paper_reimplementation_from_campaign_artifacts.md)
  Plan the local-history rewrite needed to separate the recent RCIM Model-Bank Reproduction campaign artifact package from unrelated RCIM paper-reimplementation changes.

- [technical/2026-04/2026-04-28/2026-04-28-16-06-05_track1_forward_last_non_green_cells_campaign_closeout.md](./technical/2026-04/2026-04-28/2026-04-28-16-06-05_track1_forward_last_non_green_cells_campaign_closeout.md)
  Plan the formal closeout of the completed final forward-only RCIM Model-Bank Reproduction last-non-green-cells campaign, including benchmark refresh, archive refresh, and persistent state completion.

- [technical/2026-04/2026-04-28/2026-04-28-13-45-35_rcim_recovered_workflow_script_renaming_and_export_alignment.md](./technical/2026-04/2026-04-28/2026-04-28-13-45-35_rcim_recovered_workflow_script_renaming_and_export_alignment.md)
  Plan the next RCIM recovered-workflow reorganization pass focused on
  repository-consistent script renaming and export-path alignment after the
  first subtree taxonomy cleanup.

- [technical/2026-04/2026-04-28/2026-04-28-13-00-21_rcim_recovered_original_workflow_reorganization_and_scripts_subtree_taxonomy.md](./technical/2026-04/2026-04-28/2026-04-28-13-00-21_rcim_recovered_original_workflow_reorganization_and_scripts_subtree_taxonomy.md)
  Plan the reorganization of the recovered RCIM original workflow copy into
  three stage folders based on the `latest_snapshot` training branch and the
  broader taxonomy cleanup of the `scripts/paper_reimplementation/rcim_ml_compensation/`
  subtree.

- [technical/2026-04/2026-04-28/2026-04-28-12-07-42_rcim_deg_temperature_documentation_clarification.md](./technical/2026-04/2026-04-28/2026-04-28-12-07-42_rcim_deg_temperature_documentation_clarification.md)
  Plan a documentation clarification that states explicitly that `deg` in the
  recovered RCIM prediction CSVs is oil temperature and that `deg <= 35` is a
  thermal filter in the original workflow.

- [technical/2026-04/2026-04-28/2026-04-28-11-21-25_track1_forward_last_non_green_cells_campaign.md](./technical/2026-04/2026-04-28/2026-04-28-11-21-25_track1_forward_last_non_green_cells_campaign.md)
  Plan the next forward-only RCIM Model-Bank Reproduction residual campaign that targets only the last `7` amplitude target pairs still carrying non-green benchmark status.

- [technical/2026-04/2026-04-28/2026-04-28-10-52-54_track1_forward_final_open_cells_campaign_closeout.md](./technical/2026-04/2026-04-28/2026-04-28-10-52-54_track1_forward_final_open_cells_campaign_closeout.md)
  Plan the formal closeout of the completed final forward-only RCIM Model-Bank Reproduction residual-cell campaign, including benchmark refresh, archive refresh, and persistent state completion.

- [technical/2026-04/2026-04-28/2026-04-28-00-15-20_track1_forward_final_open_cells_campaign.md](./technical/2026-04/2026-04-28/2026-04-28-00-15-20_track1_forward_final_open_cells_campaign.md)
  Plan the final forward-only RCIM Model-Bank Reproduction residual-cell campaign that targets only the last non-green canonical forward pairs in Tables 2-5.

#### 2026-04-27

- [technical/2026-04/2026-04-27/2026-04-27-23-29-14_scripts_reports_reorganization_and_pipeline_path_formalization.md](./technical/2026-04/2026-04-27/2026-04-27-23-29-14_scripts_reports_reorganization_and_pipeline_path_formalization.md)
  Plan the reorganization of `scripts/reports/` into dedicated closeout, presentation, PDF, analysis, and RCIM Model-Bank Reproduction support subfolders, and formalize the new paths in campaign and report documentation.

- [technical/2026-04/2026-04-27/2026-04-27-23-27-38_track1_closeout_reference_archive_refresh_enforcement.md](./technical/2026-04/2026-04-27/2026-04-27-23-27-38_track1_closeout_reference_archive_refresh_enforcement.md)
  Plan the RCIM Model-Bank Reproduction closeout pipeline fix that makes `models/paper_reference/rcim_track1/` refresh mandatory and reusable for the current forward closeout path and future backward closeout paths.

- [technical/2026-04/2026-04-27/2026-04-27-23-13-41_styled_pdf_pipeline_default_table_width_rebalancing.md](./technical/2026-04/2026-04-27/2026-04-27-23-13-41_styled_pdf_pipeline_default_table_width_rebalancing.md)
  Plan the styled PDF renderer improvement that promotes recurring table-width rebalancing into default first-pass profiles instead of repeated post-export manual fixes.

- [technical/2026-04/2026-04-27/2026-04-27-22-18-57_track1_forward_open_cell_repair_closeout_and_forward_benchmark_refresh.md](./technical/2026-04/2026-04-27/2026-04-27-22-18-57_track1_forward_open_cell_repair_closeout_and_forward_benchmark_refresh.md)
  Plan the formal closeout of the completed forward open-cell repair campaign and the canonical benchmark refresh for the `forward` branch.

- [technical/2026-04/2026-04-27/2026-04-27-22-04-48_track1_forward_open_cell_repair_remote_artifact_sync_length_fix.md](./technical/2026-04/2026-04-27/2026-04-27-22-04-48_track1_forward_open_cell_repair_remote_artifact_sync_length_fix.md)
  Plan the narrow repair of the post-run remote artifact packaging failure that blocked local synchronization after the completed `300/300` forward open-cell repair campaign.

- [technical/2026-04/2026-04-27/2026-04-27-19-06-13_rcim_original_pipeline_to_reimplementation_explanatory_companion.md](./technical/2026-04/2026-04-27/2026-04-27-19-06-13_rcim_original_pipeline_to_reimplementation_explanatory_companion.md)
  Plan a deep explanatory companion report that walks through the recovered
  original RCIM prediction pipeline and maps it carefully onto the repository
  reimplementation.

- [technical/2026-04/2026-04-27/2026-04-27-16-25-53_rcim_original_pipeline_runnable_workflow_and_diff_audit.md](./technical/2026-04/2026-04-27/2026-04-27-16-25-53_rcim_original_pipeline_runnable_workflow_and_diff_audit.md)
  Plan a repository-owned runnable copy of the recovered RCIM original
  pipeline plus a structured code-difference audit against the current
  reimplementation.

- [technical/2026-04/2026-04-27/2026-04-27-13-10-45_original_dataset_exact_model_bank_lfs_repair_for_github_push.md](./technical/2026-04/2026-04-27/2026-04-27-13-10-45_original_dataset_exact_model_bank_lfs_repair_for_github_push.md)
  Plan the Git LFS policy and local-history repair required after an oversized original-dataset exact-model-bank validation bundle blocked the GitHub push.

- [technical/2026-04/2026-04-27/2026-04-27-13-00-21_track1_forward_open_cell_repair_campaign.md](./technical/2026-04/2026-04-27/2026-04-27-13-00-21_track1_forward_open_cell_repair_campaign.md)
  Plan a forward-only RCIM Model-Bank Reproduction original-dataset repair campaign that targets only the still non-green forward cells in Tables 2-5 through a target-level retry queue.

- [technical/2026-04/2026-04-27/2026-04-27-11-08-53_track1_bidirectional_original_dataset_mega_closeout_and_reference_archive_refresh.md](./technical/2026-04/2026-04-27/2026-04-27-11-08-53_track1_bidirectional_original_dataset_mega_closeout_and_reference_archive_refresh.md)
  Plan the closeout of the completed bidirectional original-dataset RCIM Model-Bank Reproduction mega-campaign, the benchmark-table refresh, and the promotion of the new canonical forward/backward paper-reference model archives.

#### 2026-04-26

- [technical/2026-04/2026-04-26/2026-04-26-00-43-01_track1_forward_micro_closeout_and_bidirectional_mega_relaunch.md](./technical/2026-04/2026-04-26/2026-04-26-00-43-01_track1_forward_micro_closeout_and_bidirectional_mega_relaunch.md)
  Plan the formal closeout of the completed forward-only remote micro gate and the fresh regeneration of the full bidirectional original-dataset RCIM Model-Bank Reproduction mega-campaign from zero.

#### 2026-04-25

- [technical/2026-04/2026-04-25/2026-04-25-22-59-19_track1_forward_remote_micro_runner_mismatch_repair_and_remote_bringup.md](./technical/2026-04/2026-04-25/2026-04-25-22-59-19_track1_forward_remote_micro_runner_mismatch_repair_and_remote_bringup.md)
  Plan the repair of the forward-only remote micro-campaign after it launched the legacy recovered-CSV exact-paper runner instead of the original-dataset validation branch, and keep iterating on remote bringup fixes until the `10`-run gate completes cleanly.

- [technical/2026-04/2026-04-25/2026-04-25-22-43-08_track1_interrupted_mega_campaign_discard_closeout_and_remote_micro_relaunch_gate.md](./technical/2026-04/2026-04-25/2026-04-25-22-43-08_track1_interrupted_mega_campaign_discard_closeout_and_remote_micro_relaunch_gate.md)
  Plan the interrupted-discard closeout of the broken RCIM Model-Bank Reproduction bidirectional mega-campaign, the preparation of a fresh forward-only `10`-run remote micro-campaign, and the gate that must pass before regenerating the full mega-campaign from zero.

- [technical/2026-04/2026-04-25/2026-04-25-22-27-14_track1_remote_campaign_progress_ui_and_log_stream_cleanup.md](./technical/2026-04/2026-04-25/2026-04-25-22-27-14_track1_remote_campaign_progress_ui_and_log_stream_cleanup.md)
  Plan a protected-file redesign of the remote RCIM Model-Bank Reproduction campaign progress surface, separating total campaign progress, active task progress, and verbose grid-search noise into a clearer operator-facing stream.

- [technical/2026-04/2026-04-25/2026-04-25-22-20-57_track1_mlp_overflow_stabilization_for_original_dataset_exact_model_bank.md](./technical/2026-04/2026-04-25/2026-04-25-22-20-57_track1_mlp_overflow_stabilization_for_original_dataset_exact_model_bank.md)
  Plan the MLP stabilization pass for the running RCIM Model-Bank Reproduction original-dataset exact-model-bank campaign, covering feature scaling, solver/runtime adjustments, and overflow-warning mitigation without widening the campaign surface.

- [technical/2026-04/2026-04-25/2026-04-25-16-00-29_track1_bidirectional_remote_onnx_dependency_guard_and_interrupted_state_repair.md](./technical/2026-04/2026-04-25/2026-04-25-16-00-29_track1_bidirectional_remote_onnx_dependency_guard_and_interrupted_state_repair.md)
  Technical document for reconciling the interrupted RCIM Model-Bank Reproduction bidirectional mega-campaign state and hardening the remote ONNX export path with explicit dependency guards and preflight checks.

- [technical/2026-04/2026-04-25/2026-04-25-13-26-38_track1_bidirectional_remote_launcher_path_literal_fix_and_preparation_formalization.md](./technical/2026-04/2026-04-25/2026-04-25-13-26-38_track1_bidirectional_remote_launcher_path_literal_fix_and_preparation_formalization.md)
  Technical document for hardening the bidirectional RCIM Model-Bank Reproduction remote launcher against Windows path literal quoting failures and for promoting the validated remote-bootstrap fixes into the campaign preparation pipeline.

- [technical/2026-04/2026-04-25/2026-04-25-13-05-18_remote_exact_paper_wrapper_missing_output_root_compatibility_fix.md](./technical/2026-04/2026-04-25/2026-04-25-13-05-18_remote_exact_paper_wrapper_missing_output_root_compatibility_fix.md)
  Technical document for fixing the shared remote exact-paper wrapper so it
  can launch campaigns whose output roots do not exist yet at preflight time.

- [technical/2026-04/2026-04-25/2026-04-25-12-44-18_track1_bidirectional_mega_campaign_remote_repackaging_and_interrupted_state_reconciliation.md](./technical/2026-04/2026-04-25/2026-04-25-12-44-18_track1_bidirectional_mega_campaign_remote_repackaging_and_interrupted_state_reconciliation.md)
  Technical document for closing the wrongly packaged local bidirectional
  mega-campaign as interrupted and repackaging the same approved campaign
  surface with the canonical remote RCIM Model-Bank Reproduction launcher pattern.

- [technical/2026-04/2026-04-25/2026-04-25-12-26-22_track1_bidirectional_mega_launcher_yaml_compatibility_fix.md](./technical/2026-04/2026-04-25/2026-04-25-12-26-22_track1_bidirectional_mega_launcher_yaml_compatibility_fix.md)
  Technical document for repairing the bidirectional RCIM Model-Bank Reproduction mega-campaign
  PowerShell launcher so it can read the active campaign YAML without relying
  on the unavailable `ConvertFrom-Yaml` cmdlet.

- [technical/2026-04/2026-04-25/2026-04-25-11-47-14_track1_bidirectional_smoke_validation_and_mega_campaign_reset.md](./technical/2026-04/2026-04-25/2026-04-25-11-47-14_track1_bidirectional_smoke_validation_and_mega_campaign_reset.md)
  Technical document for validating the refactored original-dataset bidirectional RCIM Model-Bank Reproduction workflow through one smoke run per family and direction, resetting the canonical RCIM benchmark tables for the fresh restart, and preparing the subsequent mega-campaign surface.

- [technical/2026-04/2026-04-25/2026-04-25-11-01-19_wave1_best_model_te_curve_prediction_report.md](./technical/2026-04/2026-04-25/2026-04-25-11-01-19_wave1_best_model_te_curve_prediction_report.md)
  Technical document for adding a non-training evaluation script that loads the
  Wave 1 family-best TE models, evaluates them on the held-out test-curve
  subset, plots prediction curves, and generates a comparison report.

#### 2026-04-24

- [technical/2026-04/2026-04-24/2026-04-24-18-01-00_track1_exact_paper_second_pass_taxonomy_reorganization.md](./technical/2026-04/2026-04-24/2026-04-24-18-01-00_track1_exact_paper_second_pass_taxonomy_reorganization.md)
  Technical document for the second-pass internal taxonomy reorganization of RCIM Model-Bank Reproduction exact-paper forward configs, training-campaign outputs, and validation outputs, including grouped subfolders by campaign phase and family plus cleanup of remaining flat roots and duplicated forward path fragments.

- [technical/2026-04/2026-04-24/2026-04-24-16-10-10_rcim_forward_backward_artifact_reorganization_and_generic_recovered_root_restore.md](./technical/2026-04/2026-04-24/2026-04-24-16-10-10_rcim_forward_backward_artifact_reorganization_and_generic_recovered_root_restore.md)
  Technical document for restoring the generic recovered RCIM asset root and
  moving the real forward-versus-backward separation into campaign configs,
  validation reports, campaign results, paper-reference models, and output
  artifacts.

- [technical/2026-04/2026-04-24/2026-04-24-15-05-52_track1_interrupted_svm_partial_closeout_candidate_scientific_gains_pdf_table_rebalance.md](./technical/2026-04/2026-04-24/2026-04-24-15-05-52_track1_interrupted_svm_partial_closeout_candidate_scientific_gains_pdf_table_rebalance.md)
  Plan the styled PDF table-width rebalance for the two Candidate Scientific Gains tables in the interrupted SVM partial closeout report, shrinking Candidate and MAE, matching MAE to RMSE, and widening Run Instance plus Notes.

- [technical/2026-04/2026-04-24/2026-04-24-13-47-29_styled_pdf_pipeline_chromium_manual_handoff_rule.md](./technical/2026-04/2026-04-24/2026-04-24-13-47-29_styled_pdf_pipeline_chromium_manual_handoff_rule.md)
  Plan the styled PDF pipeline rule update that forbids PyMuPDF fallback and requires a documented manual Chromium export handoff command whenever the repository-owned headless export cannot materialize the PDF.

- [technical/2026-04/2026-04-24/2026-04-24-12-53-39_track1_interrupted_svm_partial_closeout_pdf_export_repair.md](./technical/2026-04/2026-04-24/2026-04-24-12-53-39_track1_interrupted_svm_partial_closeout_pdf_export_repair.md)
  Plan the final PDF export repair for the interrupted RCIM Model-Bank Reproduction SVM partial closeout report after the initial headless browser export failed.

- [technical/2026-04/2026-04-24/2026-04-24-11-30-11_track1_interrupted_remaining_yellow_cell_manual_sync_script.md](./technical/2026-04/2026-04-24/2026-04-24-11-30-11_track1_interrupted_remaining_yellow_cell_manual_sync_script.md)
  Plan the single local PowerShell helper that manually synchronizes the interrupted RCIM Model-Bank Reproduction SVM remaining-yellow-cell artifacts before partial closeout.

- [technical/2026-04/2026-04-24/2026-04-24-10-01-22_track1_interrupted_remaining_yellow_cell_campaign_manual_sync_and_partial_closeout.md](./technical/2026-04/2026-04-24/2026-04-24-10-01-22_track1_interrupted_remaining_yellow_cell_campaign_manual_sync_and_partial_closeout.md)
  Technical document for manually synchronizing the remote artifacts of the
  interrupted exact-paper `RCIM Model-Bank Reproduction` remaining-yellow-cell bundle, formally
  closing the campaign as a partial interrupted wave, and handing off only
  afterward to the deferred post-closeout asset-root migration workflow.

#### 2026-04-23

- [technical/2026-04/2026-04-23/2026-04-23-23-29-52_track1_bidirectional_original_dataset_rebuild_and_mega_campaign.md](./technical/2026-04/2026-04-23/2026-04-23-23-29-52_track1_bidirectional_original_dataset_rebuild_and_mega_campaign.md)
  Technical document for rebuilding `RCIM Model-Bank Reproduction` from the original repository
  dataset with separate `forward` and `backward` family banks, expanding the
  canonical benchmark to dual-direction tables, restructuring the reference
  archives, and preparing a future mega-campaign after workflow stabilization.

- [technical/2026-04/2026-04-23/2026-04-23-23-15-55_post_closeout_forward_asset_root_migration_workflow.md](./technical/2026-04/2026-04-23/2026-04-23-23-15-55_post_closeout_forward_asset_root_migration_workflow.md)
  Technical document for the deferred post-closeout rename of the legacy RCIM
  recovered-asset root and the corresponding operational path migration across
  campaign configs and other repository references once the active campaign is
  no longer protected.

- [technical/2026-04/2026-04-23/2026-04-23-23-07-18_rcim_forward_backward_reference_clarification_and_recovered_asset_rename.md](./technical/2026-04/2026-04-23/2026-04-23-23-07-18_rcim_forward_backward_reference_clarification_and_recovered_asset_rename.md)
  Technical document for formalizing the RCIM paper's forward-versus-backward
  model separation, updating the repository reference documentation
  accordingly, and renaming the recovered asset root so the stored models are
  explicitly marked as forward-only.

- [technical/2026-04/2026-04-23/2026-04-23-18-42-31_track1_lgbm19_vs_feedforward_curve_space_comparison.md](./technical/2026-04/2026-04-23/2026-04-23-18-42-31_track1_lgbm19_vs_feedforward_curve_space_comparison.md)
  Technical document for the first implementation pass of a shared
  curve-space comparison between the paper-faithful `LGBM` `19`-model bank and
  the best direct-TE `feedforward` baseline, designed for later extension to
  cherry-picked harmonic banks and other `RCIM Model-Bank Reproduction` families.

- [technical/2026-04/2026-04-23/2026-04-23-12-32-05_track1_remote_campaign_total_progress_monitor.md](./technical/2026-04/2026-04-23/2026-04-23-12-32-05_track1_remote_campaign_total_progress_monitor.md)
  Technical document for adding one read-only remote monitoring script that
  reports the real aggregate progress of the current exact-paper `RCIM Model-Bank Reproduction`
  remaining-yellow-cell campaign bundle after the original local launcher
  terminal was lost.

#### 2026-04-22

- [technical/2026-04/2026-04-22/2026-04-22-17-51-21_track1_family_reference_archives_and_closeout_integration.md](./technical/2026-04/2026-04-22/2026-04-22-17-51-21_track1_family_reference_archives_and_closeout_integration.md)
  Technical document for extending the curated `RCIM Model-Bank Reproduction` paper-reference
  archive pattern from `SVM` to every other exact-paper family and for making
  family-archive refresh a mandatory future closeout step whenever accepted
  family results improve.

- [technical/2026-04/2026-04-22/2026-04-22-09-03-17_track1_remaining_yellow_cell_campaign_svm_alias_fix.md](./technical/2026-04/2026-04-22/2026-04-22-09-03-17_track1_remaining_yellow_cell_campaign_svm_alias_fix.md)
  Technical document for the narrow post-launch repair of the prepared
  `RCIM Model-Bank Reproduction` remaining-yellow-cell overnight bundle after the first `SVM`
  config failed because the exact-paper runner expects the canonical family
  name `SVR` rather than the paper-facing alias `SVM`.

- [technical/2026-04/2026-04-22/2026-04-22-01-36-32_track1_remaining_yellow_cells_multi_family_campaign_bundle.md](./technical/2026-04/2026-04-22/2026-04-22-01-36-32_track1_remaining_yellow_cells_multi_family_campaign_bundle.md)
  Technical document for preparing the next overnight exact-paper `RCIM Model-Bank Reproduction`
  package as a multi-family yellow-cell bundle with one campaign per still-open
  family and one global launcher across the unfinished families.

- [technical/2026-04/2026-04-22/2026-04-22-01-19-27_track1_mlp_residual_closeout_pdf_targeted_pair_default_layout.md](./technical/2026-04/2026-04-22/2026-04-22-01-19-27_track1_mlp_residual_closeout_pdf_targeted_pair_default_layout.md)
  Technical document for the narrow residual `MLP` closeout PDF repair,
  focused on forcing `Targeted Pair Outcome` onto a fresh page and promoting
  the accepted `MLP` targeted-pair table widths into the automatic styled-PDF
  defaults for future reports.

- [technical/2026-04/2026-04-22/2026-04-22-01-03-07_track1_mlp_residual_cell_final_closure_closeout.md](./technical/2026-04/2026-04-22/2026-04-22-01-03-07_track1_mlp_residual_cell_final_closure_closeout.md)
  Technical document for formally closing the completed exact-paper `RCIM Model-Bank Reproduction`
  residual-cell `MLP` final-closure wave through results reporting, PDF
  validation, active-state backlinking, and canonical benchmark refresh.

#### 2026-04-21

- [technical/2026-04/2026-04-21/2026-04-21-23-32-36_track1_mlp_residual_cell_final_closure_campaign.md](./technical/2026-04/2026-04-21/2026-04-21-23-32-36_track1_mlp_residual_cell_final_closure_campaign.md)
  Technical document for preparing the final narrow exact-paper `RCIM Model-Bank Reproduction`
  `MLP` residual-cell closure wave, focused only on the four still-open
  accepted `MLP` target pairs across the canonical full-matrix tables.

- [technical/2026-04/2026-04-21/2026-04-21-22-57-46_track1_mlp_closeout_pdf_targeted_pair_outcome_rebalance.md](./technical/2026-04/2026-04-21/2026-04-21-22-57-46_track1_mlp_closeout_pdf_targeted_pair_outcome_rebalance.md)
  Technical document for the narrow PDF-only layout rebalance of the final
  `RCIM Model-Bank Reproduction` `MLP` closeout report, focused on the `Targeted Pair Outcome`
  page break and column-width redistribution.

- [technical/2026-04/2026-04-21/2026-04-21-22-08-26_track1_mlp_family_full_matrix_repair_closeout.md](./technical/2026-04/2026-04-21/2026-04-21-22-08-26_track1_mlp_family_full_matrix_repair_closeout.md)
  Technical document for formally closing the completed exact-paper `RCIM Model-Bank Reproduction`
  `MLP` family repair wave through results reporting, PDF validation,
  active-state backlinking, and canonical benchmark refresh.

- [technical/2026-04/2026-04-21/2026-04-21-17-16-53_track1_mlp_family_full_matrix_repair_campaign.md](./technical/2026-04/2026-04-21/2026-04-21-17-16-53_track1_mlp_family_full_matrix_repair_campaign.md)
  Technical document for preparing a dedicated exact-paper `RCIM Model-Bank Reproduction` `MLP`
  family repair wave that targets every still-non-green `MLP` family-target
  pair across the four canonical full-matrix replication tables.

- [technical/2026-04/2026-04-21/2026-04-21-16-26-57_track1_mlp_first_launch_closeout_refresh_after_artifact_recovery.md](./technical/2026-04/2026-04-21/2026-04-21-16-26-57_track1_mlp_first_launch_closeout_refresh_after_artifact_recovery.md)
  Technical document for refreshing the canonical `RCIM Model-Bank Reproduction` closeout and
  benchmark bookkeeping after the full local recovery of the `MLP`
  first-launch artifact set.

- [technical/2026-04/2026-04-21/2026-04-21-16-01-48_track1_mlp_first_launch_artifact_recovery.md](./technical/2026-04/2026-04-21/2026-04-21-16-01-48_track1_mlp_first_launch_artifact_recovery.md)
  Technical document for recovering the missing local repository artifacts of
  the first `MLP` launch in the `RCIM Model-Bank Reproduction` open-cell full-matrix closure wave,
  treating the problem as post-run artifact reconciliation rather than a new
  training pass.

- [technical/2026-04/2026-04-21/2026-04-21-15-34-39_track1_open_cell_closeout_pdf_table_layout_micro_rebalance.md](./technical/2026-04/2026-04-21/2026-04-21-15-34-39_track1_open_cell_closeout_pdf_table_layout_micro_rebalance.md)
  Technical document for the narrow PDF-only table rebalance of the final
  `RCIM Model-Bank Reproduction` open-cell full-matrix closeout report, focused on the
  `Family Representative Outcome` and `Canonical Benchmark Outcome` tables.

- [technical/2026-04/2026-04-21/2026-04-21-15-19-36_track1_relaunch_artifact_and_preparatory_file_closeout.md](./technical/2026-04/2026-04-21/2026-04-21-15-19-36_track1_relaunch_artifact_and_preparatory_file_closeout.md)
  Technical document for consolidating the completed `RCIM Model-Bank Reproduction` relaunch
  package by versioning its campaign YAMLs, launchers, launcher notes, and raw
  validation artifacts, while leaving the earlier missing `MLP` first-launch
  artifact recovery for a later dedicated task.

- [technical/2026-04/2026-04-21/2026-04-21-14-44-53_track1_open_cell_full_matrix_closure_campaigns_closeout.md](./technical/2026-04/2026-04-21/2026-04-21-14-44-53_track1_open_cell_full_matrix_closure_campaigns_closeout.md)
  Technical document for formally closing the completed `RCIM Model-Bank Reproduction` open-cell
  full-matrix closure wave through final results reporting, PDF validation,
  active-state backlinking, and canonical benchmark refresh.

- [technical/2026-04/2026-04-21/2026-04-21-09-26-42_remote_wrapper_report_path_fix_and_track1_relaunch_preparation.md](./technical/2026-04/2026-04-21/2026-04-21-09-26-42_remote_wrapper_report_path_fix_and_track1_relaunch_preparation.md)
  Technical document for repairing the exact-paper remote wrapper after the
  overnight `RCIM Model-Bank Reproduction` launch stopped during artifact reconciliation despite the
  completed `MLP` batch, and for preparing a relaunch that resumes from the
  first not-yet-executed family.

#### 2026-04-20

- [technical/2026-04/2026-04-20/2026-04-20-23-46-33_track1_overnight_open_cell_full_matrix_closure_campaigns.md](./technical/2026-04/2026-04-20/2026-04-20-23-46-33_track1_overnight_open_cell_full_matrix_closure_campaigns.md)
  Technical document for preparing the next overnight `RCIM Model-Bank Reproduction` exact-paper
  closure wave, focused only on the still-open cells in the canonical
  `Table 2-5` full-matrix replication surface and sized for roughly
  `700-800` training jobs.

- [technical/2026-04/2026-04-20/2026-04-20-23-21-36_track1_scope_separation_from_harmonic_wise_branch.md](./technical/2026-04/2026-04-20/2026-04-20-23-21-36_track1_scope_separation_from_harmonic_wise_branch.md)
  Technical document for separating canonical `RCIM Model-Bank Reproduction` family-bank progress
  from the postponed harmonic-wise follow-up branch and for keeping `RCIM Model-Bank Reproduction`
  status tied only to the four full-matrix replication tables plus the
  `10 x 19` model-bank completion rule.

- [technical/2026-04/2026-04-20/2026-04-20-23-12-52_track1_benchmark_status_marker_encoding_repair.md](./technical/2026-04/2026-04-20/2026-04-20-23-12-52_track1_benchmark_status_marker_encoding_repair.md)
  Technical document for repairing corrupted green/yellow/red status markers
  in the canonical `RCIM Model-Bank Reproduction` benchmark so the benchmark tables again render
  the intended `🟢/🟡/🔴` state markers.

- [technical/2026-04/2026-04-20/2026-04-20-23-00-20_markdownlint_chunk_failure_cleanup_for_campaign_readmes_and_remote_checklist.md](./technical/2026-04/2026-04-20/2026-04-20-23-00-20_markdownlint_chunk_failure_cleanup_for_campaign_readmes_and_remote_checklist.md)
  Technical document for repairing the Markdownlint chunk failure caused by missing blank-line separation in the residual-closure campaign package READMEs and an extra blank line in the remote training campaign checklist.

- [technical/2026-04/2026-04-20/2026-04-20-22-46-07_track1_tables_2_5_progress_focus_and_completion_definition.md](./technical/2026-04/2026-04-20/2026-04-20-22-46-07_track1_tables_2_5_progress_focus_and_completion_definition.md)
  Technical document for making the four colored `RCIM Model-Bank Reproduction` full-matrix
  replication tables the canonical progress surface and for defining `RCIM Model-Bank Reproduction`
  completion as `19` accepted models across each of the `10` algorithm
  families.

- [technical/2026-04/2026-04-20/2026-04-20-16-03-46_campaign_folder_taxonomy_extension.md](./technical/2026-04/2026-04-20/2026-04-20-16-03-46_campaign_folder_taxonomy_extension.md)
  Technical document for extending the stable campaign-results folder taxonomy
  to the still-flat `scripts/campaigns`, validation-check analysis bundle, and
  `output/training_campaigns` roots.

- [technical/2026-04/2026-04-20/2026-04-20-12-57-55_dataset_split_export_script_rename.md](./technical/2026-04/2026-04-20/2026-04-20-12-57-55_dataset_split_export_script_rename.md)
  Technical document for renaming the dataset split export helper to a generic
  script name and aligning the local README references with that rename.

- [technical/2026-04/2026-04-20/2026-04-20-12-44-46_wave1_dataset_split_export_script.md](./technical/2026-04/2026-04-20/2026-04-20-12-44-46_wave1_dataset_split_export_script.md)
  Technical document for exporting the canonical `Wave 1` dataset split so a
  colleague can reproduce the same `70/20/10` partition with the repository
  seed and randomization logic.

#### 2026-04-19

- [technical/2026-04/2026-04-19/2026-04-19-13-17-01_residual_closeout_pdf_table_micro_rebalance.md](./technical/2026-04/2026-04-19/2026-04-19-13-17-01_residual_closeout_pdf_table_micro_rebalance.md)
  Technical document for the narrow PDF table rebalance of the residual
  closeout report, focused on the `Family Recovery Outcome` and
  `Aggregate Ranking` tables.

- [technical/2026-04/2026-04-19/2026-04-19-13-07-54_styled_pdf_persistent_preview_cleanup_fix.md](./technical/2026-04/2026-04-19/2026-04-19-13-07-54_styled_pdf_persistent_preview_cleanup_fix.md)
  Technical document for fixing the styled PDF exporter so it always renders
  from the stable preview HTML path beside the target PDF and only uses
  `--keep-html` to decide whether that preview file is deleted afterward.

- [technical/2026-04/2026-04-19/2026-04-19-12-20-48_residual_closeout_exact_styled_parity_repair.md](./technical/2026-04/2026-04-19/2026-04-19-12-20-48_residual_closeout_exact_styled_parity_repair.md)
  Technical document for the stricter residual closeout repair that requires
  the final PDF to match the earlier exact-paper closeout style in practice.

- [technical/2026-04/2026-04-19/2026-04-19-12-08-11_residual_closeout_styled_pdf_repair.md](./technical/2026-04/2026-04-19/2026-04-19-12-08-11_residual_closeout_styled_pdf_repair.md)
  Technical document for repairing the residual closeout report so its final
  PDF returns to the canonical styled export workflow.

- [technical/2026-04/2026-04-19/2026-04-19-11-23-44_track1_remaining_family_residual_cellwise_closure_final_closeout.md](./technical/2026-04/2026-04-19/2026-04-19-11-23-44_track1_remaining_family_residual_cellwise_closure_final_closeout.md)
  Technical document for the final closeout of the completed `1026`-run
  remaining-family residual-cell closure wave, including reconstructed
  bookkeeping, benchmark refresh, and final Markdown plus PDF reporting.

- [technical/2026-04/2026-04-19/2026-04-19-01-33-26_track1_residual_closure_aggregate_launcher_execution_mode_fix.md](./technical/2026-04/2026-04-19/2026-04-19-01-33-26_track1_residual_closure_aggregate_launcher_execution_mode_fix.md)
  Technical document for the narrow aggregate-launcher repair after the
  prepared overnight residual-closure package failed before launch because the
  execution-mode status line used bare `remote/local` PowerShell tokens.

- [technical/2026-04/2026-04-19/2026-04-19-01-04-28_track1_remaining_family_residual_cellwise_closure_campaigns.md](./technical/2026-04/2026-04-19/2026-04-19-01-04-28_track1_remaining_family_residual_cellwise_closure_campaigns.md)
  Technical document for the next aggressive overnight `RCIM Model-Bank Reproduction`
  residual-cell closure wave, designed to spend a `6-7x` larger compute budget
  on the remaining non-green family-target cells across the nine non-`SVM`
  exact-paper families.

- [technical/2026-04/2026-04-19/2026-04-19-00-25-58_track1_remaining_family_cellwise_final_closeout.md](./technical/2026-04/2026-04-19/2026-04-19-00-25-58_track1_remaining_family_cellwise_final_closeout.md)
  Technical document for the final closeout of the completed `171`-run
  remaining-family `RCIM Model-Bank Reproduction` exact-paper cellwise campaign wave, including
  winner-bookkeeping reconstruction, canonical benchmark refresh, and final
  results reporting.

#### 2026-04-18

- [technical/2026-04/2026-04-18/2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns.md](./technical/2026-04/2026-04-18/2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns.md)
  Technical document for preparing the `171`-run remaining-family `RCIM Model-Bank Reproduction`
  cellwise exact-paper wave that generalizes the `SVM` reference-model closure
  pattern to every still-open paper family.

- [technical/2026-04/2026-04-18/2026-04-18-17-11-45_track1_partial_closeout_family_row_backfill_in_full_matrix_tables.md](./technical/2026-04/2026-04-18/2026-04-18-17-11-45_track1_partial_closeout_family_row_backfill_in_full_matrix_tables.md)
  Technical document for re-checking the seven-family partial-closeout rerun
  rows and backfilling any still-stale family entries in the canonical `RCIM Model-Bank Reproduction`
  full-matrix colored benchmark tables.

- [technical/2026-04/2026-04-18/2026-04-18-16-53-26_track1_closeout_pdf_table_layout_rebalance.md](./technical/2026-04/2026-04-18/2026-04-18-16-53-26_track1_closeout_pdf_table_layout_rebalance.md)
  Technical document for the report-specific PDF layout rebalance of the two
  `RCIM Model-Bank Reproduction` remaining-family closeout reports, covering page-break placement
  and table-column redistribution.

- [technical/2026-04/2026-04-18/2026-04-18-16-47-12_track1_full_matrix_replication_table_refresh_after_closeout.md](./technical/2026-04/2026-04-18/2026-04-18-16-47-12_track1_full_matrix_replication_table_refresh_after_closeout.md)
  Technical document for refreshing the canonical `RCIM Model-Bank Reproduction` full-matrix
  colored replication tables after closeout and for making that refresh a
  mandatory future closeout step whenever accepted family results improve.

- [technical/2026-04/2026-04-18/2026-04-18-16-29-35_track1_remaining_family_final_closeout_after_xgbm_lgbm_reruns.md](./technical/2026-04/2026-04-18/2026-04-18-16-29-35_track1_remaining_family_final_closeout_after_xgbm_lgbm_reruns.md)
  Technical document for the final closeout of the remaining-family
  `RCIM Model-Bank Reproduction` exact-paper batch after the pending `XGBM` and `LGBM` reruns
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
  Technical document for verifying the interrupted remaining-family `RCIM Model-Bank Reproduction`
  batch, closing out only the completed family campaigns, and refreshing the
  canonical benchmark surfaces before the later crash-recovery step.

- [technical/2026-04/2026-04-18/2026-04-18-00-54-22_hybrid_campaign_launcher_remote_flag_standard.md](./technical/2026-04/2026-04-18/2026-04-18-00-54-22_hybrid_campaign_launcher_remote_flag_standard.md)
  Technical document for promoting the hybrid campaign-launcher pattern, where
  one canonical `.ps1` runs locally by default and switches to remote
  execution through `-Remote`.

- [technical/2026-04/2026-04-18/2026-04-18-00-47-14_track1_remaining_exact_paper_family_campaigns.md](./technical/2026-04/2026-04-18/2026-04-18-00-47-14_track1_remaining_exact_paper_family_campaigns.md)
  Technical document for splitting the remaining `RCIM Model-Bank Reproduction` exact-paper work
  into `9` family-focused campaign packages plus one aggregate sequential
  launcher after `SVM` closure.

#### 2026-04-17

- [technical/2026-04/2026-04-17/2026-04-17-19-46-05_campaign_report_folder_taxonomy_reorganization.md](./technical/2026-04/2026-04-17/2026-04-17-19-46-05_campaign_report_folder_taxonomy_reorganization.md)
  Technical document for reorganizing the flat `campaign_results` and
  `campaign_plans` roots into stable topic subfolders while preserving the
  timestamp-based per-report naming convention.

- [technical/2026-04/2026-04-17/2026-04-17-19-43-39_track1_reference_family_archive_standardization.md](./technical/2026-04/2026-04-17/2026-04-17-19-43-39_track1_reference_family_archive_standardization.md)
  Technical document for promoting the current `SVM` paper-reference archive
  layout into the canonical reusable `RCIM Model-Bank Reproduction` family standard for all
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

#### 2026-04-14

- [technical/2026-04/2026-04-14/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_preparation.md)
  Technical document for preparing the final `SVR` micro-pass against the
  last residual `SVM` harmonics `40`, `240`, and `162` in canonical
  `RCIM Model-Bank Reproduction`.

- [technical/2026-04/2026-04-14/2026-04-14-20-50-01_track1_svm_final_closure_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-20-50-01_track1_svm_final_closure_campaign_preparation.md)
  Technical document for preparing the narrow `SVR` final-closure campaign
  against the last residual yellow `SVM` cells in canonical `RCIM Model-Bank Reproduction`
  Tables `2-5`.

- [technical/2026-04/2026-04-14/2026-04-14-18-19-07_styled_pdf_table_profile_promotion_for_report_specific_widths.md](./technical/2026-04/2026-04-14/2026-04-14-18-19-07_styled_pdf_table_profile_promotion_for_report_specific_widths.md)
  Technical document for promoting manually validated report-specific table
  width profiles into permanent styled-PDF renderer rules instead of relying on
  visibly wrong generic fallback sizing for dense campaign tables.

- [technical/2026-04/2026-04-14/2026-04-14-18-06-03_track1_svm_repair_pdf_table_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-18-06-03_track1_svm_repair_pdf_table_rebalance.md)
  Technical document for introducing report-specific styled-PDF width rules
  for the `Ranked Completed Runs` and `Table-Level Before Vs After` tables in
  the `RCIM Model-Bank Reproduction` SVM repair campaign results report.

- [technical/2026-04/2026-04-14/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_preparation.md)
  Technical document for preparing a broad but targeted `SVR` repair campaign
  against the currently open `SVM` cells in the canonical `RCIM Model-Bank Reproduction` benchmark.

- [technical/2026-04/2026-04-14/2026-04-14-16-27-39_track1_benchmark_table_2_5_alignment.md](./technical/2026-04/2026-04-14/2026-04-14-16-27-39_track1_benchmark_table_2_5_alignment.md)
  Technical document for realigning the canonical `RCIM Model-Bank Reproduction` benchmark so that
  sections labeled `Table 2-5` match the actual paper tables, including the
  missing amplitude-MAE `Table 2` and the demotion of the current repository
  derived harmonic-direction summary.

- [technical/2026-04/2026-04-14/2026-04-14-16-05-48_track1_benchmark_colored_status_marker_persistence.md](./technical/2026-04/2026-04-14/2026-04-14-16-05-48_track1_benchmark_colored_status_marker_persistence.md)
  Technical document for restoring and permanently preserving the colored
  `🟢/🟡/🔴` status markers in the canonical `RCIM Model-Bank Reproduction` benchmark full-matrix
  tables during future campaign-driven updates.

- [technical/2026-04/2026-04-14/2026-04-14-15-17-07_track1_full_matrix_pdf_table_specific_width_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-15-17-07_track1_full_matrix_pdf_table_specific_width_rebalance.md)
  Technical document for introducing table-specific PDF width rules for the
  `Ranked Completed Runs` and `Campaign-Wide Cell Totals` tables in the
  `RCIM Model-Bank Reproduction` full-matrix campaign results report without changing the generic
  table profile.

- [technical/2026-04/2026-04-14/2026-04-14-13-42-10_track1_full_matrix_family_campaign_preparation.md](./technical/2026-04/2026-04-14/2026-04-14-13-42-10_track1_full_matrix_family_campaign_preparation.md)
  Technical document for extending the exact-paper workflow and preparing a
  family-by-family `RCIM Model-Bank Reproduction` full-matrix reproduction campaign across
  amplitudes and phases.

- [technical/2026-04/2026-04-14/2026-04-14-12-11-51_track1_full_matrix_paper_replication_dashboard.md](./technical/2026-04/2026-04-14/2026-04-14-12-11-51_track1_full_matrix_paper_replication_dashboard.md)
  Technical document for correcting the `RCIM Model-Bank Reproduction` dashboard toward full
  paper-matrix replication, with Tables `3-5` reproduced model-by-model and
  harmonic-by-harmonic instead of only best-per-harmonic summaries.

- [technical/2026-04/2026-04-14/2026-04-14-11-37-05_track1_paper_tables_2_6_canonical_dashboard.md](./technical/2026-04/2026-04-14/2026-04-14-11-37-05_track1_paper_tables_2_6_canonical_dashboard.md)
  Technical document for promoting `RCIM Paper Reference Benchmark.md` into
  the canonical always-updated `RCIM Model-Bank Reproduction` dashboard for paper Tables `2-6`,
  including repository-owned paper-table reconstructions and color-coded
  repository comparison tables.

- [technical/2026-04/2026-04-14/2026-04-14-10-27-49_track1_exact_paper_open_cell_repair_pdf_table_rebalance.md](./technical/2026-04/2026-04-14/2026-04-14-10-27-49_track1_exact_paper_open_cell_repair_pdf_table_rebalance.md)
  Technical document for rebalancing the two `Campaign Ranking` tables in the
  `RCIM Model-Bank Reproduction` exact-paper open-cell repair campaign-results PDF.

#### 2026-04-13

- [technical/2026-04/2026-04-13/2026-04-13-22-53-36_track1_exact_paper_open_cell_repair_campaign_results_reporting.md](./technical/2026-04/2026-04-13/2026-04-13-22-53-36_track1_exact_paper_open_cell_repair_campaign_results_reporting.md)
  Technical document for closing the completed `RCIM Model-Bank Reproduction` exact-paper
  open-cell repair campaign through paper-closure-first reporting and
  validated PDF export.

- [technical/2026-04/2026-04-13/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_preparation.md](./technical/2026-04/2026-04-13/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_preparation.md)
  Technical document for preparing the next `RCIM Model-Bank Reproduction` campaign as an
  exact-paper open-cell repair batch focused on Tables `3-6` closure rather
  than harmonic-wise winner optimization.

- [technical/2026-04/2026-04-13/2026-04-13-20-35-43_github_quality_check_md012_and_node24_action_alignment.md](./technical/2026-04/2026-04-13/2026-04-13-20-35-43_github_quality_check_md012_and_node24_action_alignment.md)
  Technical document for fixing the reported GitHub quality-check `MD012`
  Markdown failure and aligning the repository workflow actions with the
  GitHub Node 24 migration path.

- [technical/2026-04/2026-04-13/2026-04-13-20-21-12_track1_reporting_template_alignment_to_paper_table_closure.md](./technical/2026-04/2026-04-13/2026-04-13-20-21-12_track1_reporting_template_alignment_to_paper_table_closure.md)
  Technical document for aligning future `RCIM Model-Bank Reproduction` report-generation and
  summary templates with canonical paper-table closure language instead of the
  old winner-centric harmonic-wise framing.

- [technical/2026-04/2026-04-13/2026-04-13-20-09-32_track1_objective_redefinition_to_paper_table_replication.md](./technical/2026-04/2026-04-13/2026-04-13-20-09-32_track1_objective_redefinition_to_paper_table_replication.md)
  Technical document for promoting the paper-table cell closure criterion to
  the canonical `RCIM Model-Bank Reproduction` objective and for aligning future plans, analyses,
  and results reports with per-target and per-harmonic status.

- [technical/2026-04/2026-04-13/2026-04-13-15-22-14_github_quality_check_markdown_md012_fix.md](./technical/2026-04/2026-04-13/2026-04-13-15-22-14_github_quality_check_markdown_md012_fix.md)
  Technical document for the narrow GitHub quality-check repair focused on
  `MD012/no-multiple-blanks` failures in harmonic-wise validation Markdown
  reports and, only if needed, the shared report-generation path.

#### 2026-04-12

- [technical/2026-04/2026-04-12/2026-04-12-16-47-53_track1_paper_tables_3_4_5_6_canonical_comparison.md](./technical/2026-04/2026-04-12/2026-04-12-16-47-53_track1_paper_tables_3_4_5_6_canonical_comparison.md)
  Technical document for building the canonical `RCIM Model-Bank Reproduction` paper-table
  comparison against tables `3-6`, including paper targets, repository
  results, explicit gap status, and a closure-oriented harmonic summary.

- [technical/2026-04/2026-04-12/2026-04-12-15-35-39_track1_per_harmonic_paper_table_replication.md](./technical/2026-04/2026-04-12/2026-04-12-15-35-39_track1_per_harmonic_paper_table_replication.md)
  Technical document for redefining `RCIM Model-Bank Reproduction` completion around faithful
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
  Technical document for opening the next `RCIM Model-Bank Reproduction` paper-faithful
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

- [technical/2026-04/2026-04-10/2026-04-10-18-30-57_exact_paper_untracked_artifact_cleanup.md](./technical/2026-04/2026-04-10/2026-04-10-18-30-57_exact_paper_untracked_artifact_cleanup.md)
  Technical document for removing the leftover untracked exact-paper crash and
  superseded intermediate validation artifacts after the stabilized workflow
  commit.

- [technical/2026-04/2026-04-10/2026-04-10-17-42-04_track_exact_paper_model_bundles_with_git_lfs.md](./technical/2026-04/2026-04-10/2026-04-10-17-42-04_track_exact_paper_model_bundles_with_git_lfs.md)
  Technical document for tracking only the newly generated exact-paper
  `paper_family_model_bank.pkl` validation bundles with Git LFS so the branch
  remains GitHub push-safe.

- [technical/2026-04/2026-04-10/2026-04-10-17-00-06_exact_paper_validation_fix_and_campaignization.md](./technical/2026-04/2026-04-10/2026-04-10-17-00-06_exact_paper_validation_fix_and_campaignization.md)
  Technical document for fixing the exact-paper ONNX export failure and
  converting the strict RCIM exact-paper branch into a repository-style
  batch-run workflow with launcher, logging, and campaign-oriented execution.

- [technical/2026-04/2026-04-10/2026-04-10-16-12-21_rcim_exact_model_reimplementation_plan.md](./technical/2026-04/2026-04-10/2026-04-10-16-12-21_rcim_exact_model_reimplementation_plan.md)
  Technical document for evolving the current `RCIM Model-Bank Reproduction` paper branch into a
  strict RCIM paper-faithful family-bank reimplementation, including the exact
  target schema, recovered model families, paper-style training surface, ONNX
  export surface, and target-wise evaluation flow.

- [technical/2026-04/2026-04-10/2026-04-10-13-30-40_rcim_recovered_asset_deep_analysis_report.md](./technical/2026-04/2026-04-10/2026-04-10-13-30-40_rcim_recovered_asset_deep_analysis_report.md)
  Technical document for producing a deep implementation-facing analysis of
  the recovered RCIM paper assets, including exact ONNX models, recovered code
  generations, TwinCAT XML exports, archive uncertainties, and the precise
  implications for faithful `RCIM Model-Bank Reproduction` reimplementation.

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

#### 2026-04-08

- [technical/2026-04/2026-04-08/2026-04-08-18-57-43_harmonic_wise_comparison_pipeline.md](./technical/2026-04/2026-04-08/2026-04-08-18-57-43_harmonic_wise_comparison_pipeline.md)
  Technical document for opening the offline paper-aligned harmonic-wise comparison pipeline branch, including harmonic prediction, TE reconstruction, offline motion-profile playback, and the benchmark path needed to close `Target A`.

- [technical/2026-04/2026-04-08/2026-04-08-17-51-22_harmonic_wise_pipeline_before_wave2_temporal_models.md](./technical/2026-04/2026-04-08/2026-04-08-17-51-22_harmonic_wise_pipeline_before_wave2_temporal_models.md)
  Technical document for making the paper-aligned harmonic-wise pipeline the immediate post-Wave-1 branch before the future Wave 2.1 temporal-model work is opened.

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

- [technical/2026-04/2026-04-08/2026-04-08-13-54-00_github_branch_migration_final_audit.md](./technical/2026-04/2026-04-08/2026-04-08-13-54-00_github_branch_migration_final_audit.md)
  Technical document for the final read-only audit of the completed GitHub branch migration, focused on local tracking, remote branch topology, workflow triggers, and current-facing repository references.

- [technical/2026-04/2026-04-08/2026-04-08-13-35-06_post_rename_branch_reference_realignment.md](./technical/2026-04/2026-04-08/2026-04-08-13-35-06_post_rename_branch_reference_realignment.md)
  Technical document for the narrow post-migration cleanup that removes stale pre-rename branch references from the active workflows and current-facing documentation after the repository has already moved to `main`.

- [technical/2026-04/2026-04-08/2026-04-08-12-50-04_github_branch_topology_refactor_and_main_adoption.md](./technical/2026-04/2026-04-08/2026-04-08-12-50-04_github_branch_topology_refactor_and_main_adoption.md)
  Technical document for refactoring the repository branch topology around a new canonical `main` branch, retiring `standard-ml-codex`, and defining the legacy/test handling of the remaining historical branches plus the required GitHub ruleset and Pages follow-up.

#### 2026-04-07

- [technical/2026-04/2026-04-07/2026-04-07-15-41-56_github_quality_workflow_naming_and_markdownlint_memory_fix.md](./technical/2026-04/2026-04-07/2026-04-07-15-41-56_github_quality_workflow_naming_and_markdownlint_memory_fix.md)
  Technical document for renaming the new repository-quality workflow to a clearer GitHub-facing label and fixing the GitHub Actions Markdownlint out-of-memory failure by switching to chunked lint execution.

- [technical/2026-04/2026-04-07/2026-04-07-13-04-01_github_repository_governance_and_automation_baseline.md](./technical/2026-04/2026-04-07/2026-04-07-13-04-01_github_repository_governance_and_automation_baseline.md)
  Technical document for defining the first practical GitHub governance baseline for the public repository, including a separate CI workflow, review templates, ownership hints, Dependabot, and recommended GitHub-side ruleset settings.

- [technical/2026-04/2026-04-07/2026-04-07-12-47-33_github_pages_live_url_publication_registration.md](./technical/2026-04/2026-04-07/2026-04-07-12-47-33_github_pages_live_url_publication_registration.md)
  Technical document for registering the now-live GitHub Pages public URL of the repository Sphinx portal and updating the main repository entry points to surface that published documentation endpoint.

#### 2026-04-05

- [technical/2026-04/2026-04-05/2026-04-05-11-04-45_github_pages_environment_protection_fix_and_node24_alignment.md](./technical/2026-04/2026-04-05/2026-04-05-11-04-45_github_pages_environment_protection_fix_and_node24_alignment.md)
  Technical document for fixing the GitHub Pages deploy blocker caused by `github-pages` environment protection rules and aligning the workflow with GitHub's Node.js 24 action-runtime transition.

#### 2026-04-04

- [technical/2026-04/2026-04-04/2026-04-04-22-34-46_targeted_remote_followup_completed_runs_family_width_final_micro_adjustment.md](./technical/2026-04/2026-04-04/2026-04-04-22-34-46_targeted_remote_followup_completed_runs_family_width_final_micro_adjustment.md)
  Technical document for refining the styled PDF layout of the targeted remote follow-up campaign results report, including table rebalancing and forced clean page starts for the final conclusions and artifact-reference sections.

- [technical/2026-04/2026-04-04/2026-04-04-22-29-19_targeted_remote_followup_completed_runs_family_column_final_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-22-29-19_targeted_remote_followup_completed_runs_family_column_final_refinement.md)

- [technical/2026-04/2026-04-04/2026-04-04-22-24-40_targeted_remote_followup_results_pdf_layout_rebalance_and_page_break_fix.md](./technical/2026-04/2026-04-04/2026-04-04-22-24-40_targeted_remote_followup_results_pdf_layout_rebalance_and_page_break_fix.md)

- [technical/2026-04/2026-04-04/2026-04-04-22-14-17_targeted_remote_followup_results_pdf_layout_refinement.md](./technical/2026-04/2026-04-04/2026-04-04-22-14-17_targeted_remote_followup_results_pdf_layout_refinement.md)

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

#### 2026-03-20

- [technical/2026-03/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md](./technical/2026-03/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md)
  Technical planning document for the architecture learning-guide series starting from the FeedForward Network and extending to the other documented model families.

- [technical/2026-03/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md](./technical/2026-03/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md)
  Technical planning document for preparing NotebookLM-ready video-guide source packages and adding the related approval-gated workflow rule for future learning-guide videos.

- [technical/2026-03/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md](./technical/2026-03/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md)
  Technical planning document for exporting the learning guides to PDF and requiring explicit user approval of generated guide images before final PDF generation.

- [technical/2026-03/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md](./technical/2026-03/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md)
  Technical planning document for a beginner-to-university learning guide covering neural-network foundations, training/validation/testing, and the TE model-family curriculum from feedforward baselines to planned advanced architectures.

#### 2026-03-18

- [technical/2026-03/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md)
  Technical document for a formatting-only repository-wide cleanup that normalizes redundant blank lines between top-level definitions across the Python scripts under `scripts/`.

- [technical/2026-03/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md)
  Technical document for a formatting-only cleanup that normalizes redundant blank lines between top-level definitions in the model-report diagram generator.

- [technical/2026-03/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md](./technical/2026-03/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md)
  Technical document for the third pass of model-report diagram refinement, focused on simplifying neuron arrows, enforcing perpendicular box routing, arrowhead clearance, and model-specific spacing fixes.

- [technical/2026-03/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md](./technical/2026-03/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md)
  Technical document for the second pass of model-report diagram refinement, focused on connector pile-up, slide centering, multiline card layout, and safer routing.

- [technical/2026-03/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md](./technical/2026-03/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md)
  Technical document for auditing all Python comments under `scripts/` and correcting only the ones whose meaning no longer matches the code they describe.

- [technical/2026-03/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md](./technical/2026-03/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md)
  Technical document for a focused section-comment retrofit of the remaining model scripts that still underuse internal `# ...` stage markers.

- [technical/2026-03/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md](./technical/2026-03/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md)
  Technical document for making frequent internal section comments an explicit persistent style rule and retrofitting that style into the recent report scripts.

- [technical/2026-03/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md](./technical/2026-03/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md)
  Technical document for fully removing the remaining standardized report-pipeline runtime temp root and leaving the repository without runtime temporary folders.

- [technical/2026-03/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md](./technical/2026-03/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md)
  Technical document for removing obsolete report-pipeline temporary environments and retaining only the intended standardized temporary layout.

- [technical/2026-03/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md](./technical/2026-03/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md)
  Technical document for standardizing the report-generation pipeline with a repository-owned orchestrator, a persistent PDF-validation tooling environment, and cleaner temporary-artifact management.

- [technical/2026-03/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md](./technical/2026-03/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md)
  Technical document for correcting diagram geometry defects, improving figure centering, replacing pseudo-arrows with real connectors, and revalidating the SVG and PDF outputs.

- [technical/2026-03/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md](./technical/2026-03/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md)
  Technical document for correcting diagram layout defects, introducing reusable diagram generation, removing figure-background clashes, and adding both conceptual and architecture diagrams to the model reports.

- [technical/2026-03/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md](./technical/2026-03/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md)
  Technical document for retroactively adding diagrams to the existing structured-model reports and preserving those images in the exported PDFs.

- [technical/2026-03/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md](./technical/2026-03/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md)
  Technical document for requiring visual conceptual diagrams and image assets inside future model-explanatory reports and their PDF exports.

- [technical/2026-03/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md](./technical/2026-03/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md)
  Technical document for exporting the existing model-explanatory reports to styled PDFs and validating the real exported artifacts.

- [technical/2026-03/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md](./technical/2026-03/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md)
  Technical document for creating retroactive explanatory reports for the already implemented structured TE model families.

- [technical/2026-03/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md](./technical/2026-03/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md)
  Technical document for making model-level explanatory reports mandatory whenever a new model or new model-specific training workflow is introduced.

#### 2026-03-17

- [technical/2026-03/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md](./technical/2026-03/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md)
  Technical document for preparing Wave 1 structured-baseline implementation and the first exploratory campaign against the formalized feedforward reference baseline.

- [technical/2026-03/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md](./technical/2026-03/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md)
  Technical document for formalizing the registry-selected feedforward run as the canonical reference baseline before Wave 1.

- [technical/2026-03/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md](./technical/2026-03/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md)
  Technical document for removing the remaining feedforward-specific legacy snapshot compatibility from the active training pipeline.

- [technical/2026-03/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md](./technical/2026-03/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md)
  Technical document for migrating the historical `output/feedforward_network/` artifacts into the new training-run structure and rewriting repository-authored path references.

- [technical/2026-03/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md](./technical/2026-03/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md)
  Technical document for reorganizing training outputs by artifact type and adding explicit campaign, family, and program best-result registries.

- [technical/2026-03/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md](./technical/2026-03/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md)
  Technical document for cleaning up redundant `variable=variable` function-call arguments while preserving explicit keywords where they improve readability.

- [technical/2026-03/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md](./technical/2026-03/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md)
  Technical document for moving the TE implementation backlog into a privileged live location under `doc/running/`.

- [technical/2026-03/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md](./technical/2026-03/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md)
  Technical document for the shared training, smoke-test, validation, and metrics infrastructure required before implementing the planned TE model families.

- [technical/2026-03/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md](./technical/2026-03/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md)
  Technical review note for adding explicit State-Space, Mixture-of-Experts, and optional Kernel/GP families to the TE planning set.

- [technical/2026-03/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md](./technical/2026-03/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md)
  Technical note for keeping Lightweight Transformer and Neural ODE families explicitly in scope as low-priority exploratory options.

- [technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md](./technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md)
  Technical backlog document for implementing, validating, smoke-testing, and comparing all approved TE model families through campaign waves.

- [technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md](./technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md)
  Technical planning document for the TE model-family roadmap across standard, temporal, hybrid, and PINN approaches.

#### 2026-03-16

- [technical/2026-03/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md](./technical/2026-03/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md)
  Technical document for validating and executing the project environment migration from Python 3.10 to Python 3.12.

#### 2026-03-14

- [technical/2026-03/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md](./technical/2026-03/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md)
  Technical document for reviewing the current GPU training path and proposing practical transfer, precision, and Trainer-level performance optimizations.

- [technical/2026-03/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md](./technical/2026-03/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md)
  Technical document for moving root `models/` and `training/` source code under `scripts/`, reserving root `models/` for artifacts, and relocating agent submodules under `reference/agents/`.

- [technical/2026-03/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md](./technical/2026-03/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md)
  Technical document for evaluating a cleaner internal code layout and moving the external agent submodules under `reference/agents/`.

- [technical/2026-03/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md](./technical/2026-03/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md)
  Technical document for enforcing vertical table-cell centering and cleaner section page-break behavior in the campaign-results PDF.

- [technical/2026-03/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md](./technical/2026-03/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md)
  Technical document for fixing remaining header spill and semantic config wrapping issues in the campaign-results PDF tables.

#### 2026-03-13

- [technical/2026-03/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md](./technical/2026-03/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md)
  Technical document for repairing the mixed-campaign PDF table widths and tightening the rule so future table-layout defects must be caught before task closure.

- [technical/2026-03/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md](./technical/2026-03/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md)
  Technical document for making PDF export and PDF validation mandatory for final campaign-results reports.

- [technical/2026-03/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md](./technical/2026-03/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md)
  Technical document for writing the final mixed-campaign results report and selecting the best current feedforward training preset.

#### 2026-03-12

- [technical/2026-03/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md](./technical/2026-03/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md)
  Technical document for automatic campaign YAML generation, active-campaign state tracking, protected-file warnings, and completion/cancellation handling.

- [technical/2026-03/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md](./technical/2026-03/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md)
  Technical document for reorganizing `config/`, introducing a queue-based batch training workflow, and generating campaign execution reports for later post-training analysis.

- [technical/2026-03/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md](./technical/2026-03/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md)
  Technical document for shortening the styled PDF exporter comments and aligning the persistent coding-style rules with the latest user-approved manual refactor.

- [technical/2026-03/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md](./technical/2026-03/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md)
  Technical document for changing the repository workflow so every Git commit requires a final explicit user approval after the work is completed.

- [technical/2026-03/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md](./technical/2026-03/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md)
  Technical document for refactoring the styled PDF exporter to match repository coding style and clarifying that the style rules also apply to utility/report scripts.

- [technical/2026-03/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md](./technical/2026-03/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md)
  Technical document for declaring the approved analytical PDF as the project golden standard and encoding its style rules for future reports.

- [technical/2026-03/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md](./technical/2026-03/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md)
  Technical document for refining the three configuration tables so each one repeats the config name and uses more consistent centered alignment.

- [technical/2026-03/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md](./technical/2026-03/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md)
  Technical document for fixing the remaining technical-table fit issues in the analytical PDF and enforcing post-export PDF validation.

- [technical/2026-03/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md](./technical/2026-03/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md)
  Technical document for correcting the analytical PDF printable margins and replacing the dense configuration table with a cleaner professional layout.

- [technical/2026-03/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md](./technical/2026-03/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md)
  Technical document for redesigning the analytical PDF again with a restrained blue palette, white background, better page flow, and more professional typography.

- [technical/2026-03/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md](./technical/2026-03/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md)
  Technical document for regenerating the training-configuration analysis PDF with a much stronger visual layout and print-oriented styling.

- [technical/2026-03/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md](./technical/2026-03/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md)
  Technical document for reorganizing the technical-document tree by day and the report tree by report type.

- [technical/2026-03/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md](./technical/2026-03/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md)
  Technical document for renaming the current report files so they include the full timestamp in their filenames.

- [technical/2026-03/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md](./technical/2026-03/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md)
  Technical document for making preliminary planning reports and final results reports mandatory companions to every future training campaign.

- [technical/2026-03/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md](./technical/2026-03/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md)
  Technical document for executing a mixed campaign that combines longer schedules, denser point sampling, larger batches, and larger feedforward models.

- [technical/2026-03/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md](./technical/2026-03/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md)
  Technical document for executing and comparing the pending baseline and workstation-oriented feedforward training variants.

- [technical/2026-03/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md](./technical/2026-03/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md)
  Technical document for producing a detailed training-configuration explanation report plus a PDF export and heavier workstation-oriented configuration proposals.

- [technical/2026-03/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md](./technical/2026-03/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md)
  Technical document for writing a full analytical report of the feedforward proof run with narrative interpretation and comparison against the reference papers.

#### 2026-03-11

- [technical/2026-03/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md](./technical/2026-03/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md)
  Technical document for adding a proof feedforward training run, a held-out test phase, and a per-run result report artifact.

- [technical/2026-03/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md](./technical/2026-03/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md)
  Technical document for aligning the persistent programming style guide with the latest approved manual code-style refactoring commit.

- [technical/2026-03/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md](./technical/2026-03/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md)
  Technical document for updating the persistent programming style guide with the approved spacing rules and the broader manual refactoring conventions.

- [technical/2026-03/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md](./technical/2026-03/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md)
  Technical document for propagating the broader manual coding style introduced in commit `228a999c94eb67d1c07eebfbd87c05903e99b694` to the remaining project scripts.

- [technical/2026-03/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md)
  Technical document for extending the approved blank-line spacing convention to top-level class and dataclass declarations.

- [technical/2026-03/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md)
  Technical document for extending the approved function-spacing convention to all project-authored Python scripts.

- [technical/2026-03/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md](./technical/2026-03/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md)
  Technical document for normalizing blank-line spacing around top-level function definitions in the feedforward training entry point.

- [technical/2026-03/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md](./technical/2026-03/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md)
  Technical document for correcting the generator-based context-manager return annotation in the training entry point.

- [technical/2026-03/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md](./technical/2026-03/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md)
  Technical document for removing the remaining Lightning startup tip and `_pytree` sanity-check warning from feedforward training output.

#### 2026-03-10

- [technical/2026-03/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md](./technical/2026-03/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md)
  Technical document for formalizing dependency tracking in the workflow and auditing current imports against `requirements.txt`.

- [technical/2026-03/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md](./technical/2026-03/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md)
  Technical document for making the feedforward training terminal output cleaner, colorized, and less noisy on Windows.

- [technical/2026-03/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md](./technical/2026-03/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md)
  Technical document for fixing direct execution of the feedforward training entry point when the repository root is missing from `sys.path`.

- [technical/2026-03/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md](./technical/2026-03/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md)
  Technical document for tuning the default dataloader worker and memory-pinning settings of the current feedforward training workflow.

- [technical/2026-03/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md](./technical/2026-03/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md)
  Technical document for refreshing `project_usage_guide.md` so it matches the current runnable training and dataset workflows.

- [technical/2026-03/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md](./technical/2026-03/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md)
  Technical document for requiring a detailed `project_usage_guide.md` update before commit whenever repository functionality changes.

- [technical/2026-03/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md](./technical/2026-03/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md)
  Technical document for clarifying the original CSV header typo `Poisition_Output_Reducer_Fw` versus the normalized internal column naming.

- [technical/2026-03/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md](./technical/2026-03/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md)
  Technical document for the first modular PyTorch Lightning feedforward baseline for TE regression.

- [technical/2026-03/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md](./technical/2026-03/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md)
  Technical document for creating persistent `doc/reference_codes/` notes from the reference-code submodules.

- [technical/2026-03/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md](./technical/2026-03/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md)
  Technical document for replacing the archived reference code `.zip` files in `reference/codes/` with Git submodules.

- [technical/2026-03/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md](./technical/2026-03/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md)
  Technical document for enforcing the technical-document approval workflow plus a mandatory final Git commit.

- [technical/2026-03/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md](./technical/2026-03/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md)
  Technical document for moving the existing agent submodule and adding the requested `agents/` submodule collection.

- [technical/2026-03/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md](./technical/2026-03/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md)
  Technical document for the grouped `doc/` folder reorganization.

- [technical/2026-03/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md](./technical/2026-03/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md)
  Technical document for the `scripts/`, `config/`, and per-script documentation repository rules.

- [technical/2026-03/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md](./technical/2026-03/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md)
  Technical document for the validated TE dataset-processing pipeline and raw-data reconstruction path.

- [technical/2026-03/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md](./technical/2026-03/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md)
  Technical document for the Conda, PyTorch, and PyTorch Lightning environment baseline.

### Script Documentation

- [scripts/datasets/generate_polished_transmission_error_dataset.md](./scripts/datasets/generate_polished_transmission_error_dataset.md)
  Guide for the aligned standalone and repository-integrated polished
  transmission-error dataset generators.

- [scripts/datasets/transmission_error_dataset.md](./scripts/datasets/transmission_error_dataset.md)
  Script-level documentation for the TE dataset parser, PyTorch dataset, and dataloader utilities.

- [scripts/datasets/visualize_transmission_error.md](./scripts/datasets/visualize_transmission_error.md)
  Script-level documentation for the TE curve visualization utility.

- [scripts/reports/README.md](./scripts/reports/README.md)
  Canonical index for the reorganized `scripts/reports/` subfolders and their operator-facing notes.

- [scripts/reports/analysis/generate_model_report_diagrams.md](./scripts/reports/analysis/generate_model_report_diagrams.md)
  Script-level documentation for the SVG generator used by the model explanatory reports.

- [scripts/reports/analysis/build_track2_curve_first_reranking_report.md](./scripts/reports/analysis/build_track2_curve_first_reranking_report.md)
  Script-level documentation for the `CVP 1.1` curve-first reranking report
  builder.

- [scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.md](./scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.md)
  Script-level documentation for the `CVP 1.2` curve-payload diagnostics
  report builder.

- [scripts/reports/analysis/build_track2_mean_centered_collage_report.md](./scripts/reports/analysis/build_track2_mean_centered_collage_report.md)
  Script-level documentation for the `TE Curve Verification Pipeline` mean-centered collage
  diagnostics report builder.

- [scripts/reports/analysis/build_track2_official_model_verification_report.md](./scripts/reports/analysis/build_track2_official_model_verification_report.md)
  Script-level documentation for the official `TE Curve Verification Pipeline` verification report
  builder used by self-contained verification-refresh launchers.

- [scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.md](./scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.md)
  Script-level documentation for the `CVP 1.4` full-matrix mean-offset audit
  report builder, including chunked execution and merge-only finalization.

- [scripts/reports/analysis/build_track2e_offset_predictability_feasibility.md](./scripts/reports/analysis/build_track2e_offset_predictability_feasibility.md)
  Script-level documentation for the `CVP 1.5` offset-predictability
  feasibility report builder and its conservative causal correction baselines.

- [scripts/reports/analysis/generate_training_results_master_summary.md](./scripts/reports/analysis/generate_training_results_master_summary.md)
  Script-level documentation for the canonical training-results master-summary generator.

- [scripts/reports/pdf/run_report_pipeline.md](./scripts/reports/pdf/run_report_pipeline.md)
  Script-level documentation for the orchestration runner that standardizes diagram regeneration, styled PDF export, and PDF validation.

- [scripts/reports/presentation/run_presentation_pipeline.md](./scripts/reports/presentation/run_presentation_pipeline.md)
  Script-level documentation for the repository-owned Markdown-to-presentation pipeline runner.

- [scripts/reports/closeout/README.md](./scripts/reports/closeout/README.md)
  Script-level documentation for the canonical RCIM Model-Bank Reproduction closeout entrypoint subtree.

- [scripts/training/train_feedforward_network.md](./scripts/training/train_feedforward_network.md)
  Script-level documentation for the first PyTorch Lightning feedforward training entry point.

- [scripts/training/train_tree_regressor.md](./scripts/training/train_tree_regressor.md)
  Script-level documentation for the tree-based structured-baseline training entry point.

- [scripts/training/run_training_campaign.md](./scripts/training/run_training_campaign.md)
  Script-level documentation for the persistent queue-based batch training runner.

- [scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.md](./scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.md)
  Script-level documentation for the prepared polished `RCIM Model-Bank
  Reproduction` launcher with local and `-Remote` execution paths.

- [scripts/campaigns/cross_wave/run_rcim_track1_polished_setpoints_campaign.md](./scripts/campaigns/cross_wave/run_rcim_track1_polished_setpoints_campaign.md)
  Script-level documentation for the prepared `rcim_track1` polished setpoint
  campaign with local preflight commands, local parallel Windows execution, and
  official model-archive promotion.

- [scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.md](./scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.md)
  Script-level documentation for the Aries CPU/RAM Slurm launcher that runs
  the polished `rcim_track1` input-mode surfaces sequentially.

- [scripts/campaigns/cross_wave/run_polished_dataset_early_wave_parallel_training_campaign.md](./scripts/campaigns/cross_wave/run_polished_dataset_early_wave_parallel_training_campaign.md)
  Script-level documentation for the 36-run early-wave `polished_dataset`
  retraining launcher prepared for parallel execution on a second workstation.

- [scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.md](./scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.md)
  Script-level documentation for the prepared 108-run polished full-wave
  model-development retraining launcher with local and `-Remote` execution
  paths.

- [scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md](./scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md)
  Script-level documentation for the short Wave 1 recovery campaign launcher.

- [scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md](./scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md)
  Script-level documentation for the canonical Wave 1 residual-harmonic family launcher.

- [scripts/campaigns/run_wave1_directional_best_hyperparameter_search_campaign.md](./scripts/campaigns/run_wave1_directional_best_hyperparameter_search_campaign.md)
  Script-level documentation for the mixed bounded-grid plus Optuna Wave 1 directional best-hyperparameter search launcher.

- [scripts/campaigns/wave_3/wave3_embryonic_skeleton_checks.md](./scripts/campaigns/wave_3/wave3_embryonic_skeleton_checks.md)
  Script-level documentation for the dry-run `Wave 5.1` embryonic skeleton
  checker. It validates implementation readiness without queueing or launching
  training.

- [scripts/campaigns/wave_3/wave3_training_smoke_ready_checks.md](./scripts/campaigns/wave_3/wave3_training_smoke_ready_checks.md)
  Script-level documentation for the dry-run `Wave 5.1` training-smoke-ready
  checker. It runs one-batch validation without creating a campaign queue.

- [scripts/campaigns/wave_4/wave4_embryonic_skeleton_checks.md](./scripts/campaigns/wave_4/wave4_embryonic_skeleton_checks.md)
  Script-level documentation for the dry-run `Wave 5.2A` embryonic skeleton
  checker. It validates implementation readiness without queueing or launching
  training.

- [scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.md](./scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.md)
  Script-level documentation for the `Wave 5.2A` MMT equation diagnostic report
  generator.

- [scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.md](./scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.md)
  Script-level documentation for the `Wave 5.2A` MMT parameter-inventory report
  builder.

- [scripts/campaigns/run_wave1_high_order_harmonic_tracking_campaign.md](./scripts/campaigns/run_wave1_high_order_harmonic_tracking_campaign.md)
  Script-level documentation for the prepared Wave 1 high-order harmonic
  tracking launcher across RCIM sparse, dense `0..240`, and dense `0..360`
  harmonic banks.

- [scripts/campaigns/run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.md](./scripts/campaigns/run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.md)
  Script-level documentation for the prepared Wave 1 `periodic_mlp` explicit
  harmonic tracking launcher across RCIM sparse, dense `0..240`, and dense
  `0..360` fixed periodic-feature banks.

- [scripts/campaigns/run_wave2_temporal_model_entry_campaign.md](./scripts/campaigns/run_wave2_temporal_model_entry_campaign.md)
  Script-level documentation for the prepared Wave 2.1 temporal-model entry
  launcher across temporal convolution, `GRU`, and `LSTM` sequence baselines.

- [scripts/campaigns/wave_2/run_wave2b_harmonic_temporal_hybrid_campaign.md](./scripts/campaigns/wave_2/run_wave2b_harmonic_temporal_hybrid_campaign.md)
  Script-level documentation for the prepared Wave 2.2 harmonic-temporal
  hybrid launcher across periodic temporal convolution, periodic `GRU`, and
  periodic `LSTM` sequence models.

- [scripts/campaigns/track_2/run_track2f_bis_harmonic_offset_probe_campaign.md](./scripts/campaigns/track_2/run_track2f_bis_harmonic_offset_probe_campaign.md)
  Script-level documentation for the prepared Wave 3.2 harmonic-offset
  launcher across clean non-harmonic controls and explicit harmonic-offset
  probes for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2f_bis_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2f_bis_track2_verification_refresh.md)
  Script-level documentation for the operator-launched Wave 3.2 official
  `TE Curve Verification Pipeline` verification refresh across clean and harmonic candidates for
  `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2g_curve_aware_training_campaign.md](./scripts/campaigns/track_2/run_track2g_curve_aware_training_campaign.md)
  Script-level documentation for the prepared Wave 3.3 curve-aware training
  launcher across pointwise-control, centered-shape, offset, and full
  composite loss profiles for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2g_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2g_track2_verification_refresh.md)
  Script-level documentation for the operator-launched Wave 3.3 official
  `TE Curve Verification Pipeline` verification refresh across all twelve curve-aware candidates for
  `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2h_track2_verification_refresh.md)
  Script-level documentation for the operator-launched Wave 4 series official
  `TE Curve Verification Pipeline` verification refresh across all nine robust-loss candidates for
  `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.md](./scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.md)
  Script-level documentation for the prepared `Wave 4 series`
  quantile/probabilistic campaign launcher across `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.md](./scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.md)
  Script-level documentation for the prepared `Wave 4.3` mixture-density heads
  campaign launcher across `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_campaign.md](./scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_campaign.md)
  Script-level documentation for the prepared `Wave 4.4` latent-state /
  hysteresis-aware campaign launcher across `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.md)
  Script-level documentation for the operator-launched `Wave 4.4`
  latent-state / hysteresis-aware official `TE Curve Verification Pipeline` verification refresh
  across all six candidates for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_quantile_probabilistic_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2h_quantile_probabilistic_track2_verification_refresh.md)
  Script-level documentation for the operator-launched `Wave 4 series`
  quantile/probabilistic official `TE Curve Verification Pipeline` verification refresh across all
  six probabilistic candidates for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_track2h_mixture_density_heads_track2_verification_refresh.md](./scripts/campaigns/track_2/run_track2h_mixture_density_heads_track2_verification_refresh.md)
  Script-level documentation for the operator-launched `Wave 4 series`
  mixture-density heads official `TE Curve Verification Pipeline` verification refresh across all
  six MDN candidates for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/track_2/run_wave3_harmonic_prior_residual_track2_verification_refresh.md](./scripts/campaigns/track_2/run_wave3_harmonic_prior_residual_track2_verification_refresh.md)
  Script-level documentation for the operator-launched `Wave 5.1`
  harmonic-prior residual official `TE Curve Verification Pipeline` verification refresh across all
  six completed candidates for `global`, `Fw`, and `Bw`.

- [scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.md](./scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.md)
  Script-level documentation for the prepared first real `Wave 5.1`
  harmonic-prior residual campaign launcher across `global`, `Fw`, and `Bw`.

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

- [Shape-First Training-Rule Distillation Pilot Campaign Results](reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.md)
  Final closeout report for the two-arm time-windowed versus non-windowed
  shape-first training-rule distillation pilot.

- [Shape-First Training-Rule Distillation Pilot Campaign Results PDF](reports/campaign_results/cross_wave/shape_first_training_rule_distillation/2026-07-22-15-20-49_shape_first_training_rule_distillation_pilot_campaign_results_report.pdf)
  Styled PDF export for the shape-first training-rule distillation pilot
  closeout.

- [Parallel Shape-Objective Follow-Up Track 2 Curve Plot Summary](reports/campaign_results/track_2/verification_plots/shape_objective_followup_polished_setpoints_fw/track2_candidate_curve_plot_summary.yaml)
  Manifest for the bounded Track 2 measured-versus-predicted TE curve plots generated for the shape-objective follow-up pilot.

- [Parallel Shape-Objective Follow-Up Campaign Results](reports/campaign_results/cross_wave/shape_objective/2026-07-21-19-31-21_parallel_shape_objective_followup_campaign_results_report.md)

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

- [reports/analysis/validation_checks/2026-06-04-23-08-24_track2f_bi_2c54bdf1_te_track2f_bis_clean_residual_o_00ddc617_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-04-23-08-24_track2f_bi_2c54bdf1_te_track2f_bis_clean_residual_o_00ddc617_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.2 clean non-harmonic
  control `global` entry.

- [reports/analysis/validation_checks/2026-06-04-23-08-24_track2f_bi_da4c30ce_te_track2f_bis_harmonic_residua_7fa047ef_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-04-23-08-24_track2f_bi_da4c30ce_te_track2f_bis_harmonic_residua_7fa047ef_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.2 harmonic-offset
  `global` entry.

- [reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_ca617bbd_te_track2g_curve_aware_pointwis_239993a2_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_ca617bbd_te_track2g_curve_aware_pointwis_239993a2_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.3 pointwise-control
  `global` entry.

- [reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_b85b1190_te_track2g_curve_aware_raw_cent_9365d702_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_b85b1190_te_track2g_curve_aware_raw_cent_9365d702_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.3 raw plus centered-shape
  `global` entry.

- [reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_1430b431_te_track2g_curve_aware_raw_offs_951f470e_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_1430b431_te_track2g_curve_aware_raw_offs_951f470e_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.3 raw plus offset
  `global` entry.

- [reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_3c0ce19b_te_track2g_curve_aware_full_cur_f7e39520_validation_setup_report.md](./reports/analysis/validation_checks/2026-06-08-18-14-31_track2g_cu_3c0ce19b_te_track2g_curve_aware_full_cur_f7e39520_validation_setup_report.md)
  One-batch validation setup report for the Wave 3.3 full composite curve-loss
  `global` entry.

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

- [reports/campaign_plans/cross_wave/input_modes/2026-07-13-16-35-39_rcim_track1_polished_input_mode_campaign_plan_report.md](./reports/campaign_plans/cross_wave/input_modes/2026-07-13-16-35-39_rcim_track1_polished_input_mode_campaign_plan_report.md)
  Planning gate for the two missing `rcim_track1` polished-dataset
  input-mode campaigns, keeping the audited simplified paper-reference
  baseline frozen.

- [reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md)
  Preliminary campaign plan for the next `Wave 4.4` package, focused on
  causal latent-state / hysteresis-aware candidates across `global`, `Fw`,
  and `Bw`.

- [reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md](./reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md)
  Preliminary and prepared campaign plan for the first real `Wave 5.1`
  harmonic-prior residual package across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/track_2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 4.2` package, focused on
  quantile and Gaussian probabilistic regression candidates across `global`,
  `Fw`, and `Bw`.

- [reports/campaign_plans/track_2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 4 series` dispersion-aware modeling
  probes across robust, probabilistic, mixture, and causal latent-state
  candidate groups.

- [reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md](./reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md)
  Preliminary plan for a non-campaign `Wave 5.1` training-smoke-ready hardening
  pass plus the first `Wave 5.2A` MMT equation diagnostic report generator.

- [reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md](./reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md)
  Preliminary plan for preparing `Wave 5.1` and `Wave 5.2` embryonic model,
  diagnostic, validator, dry-run launcher, and configuration skeletons without
  making either wave campaign-ready.

- [reports/campaign_plans/track_2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 3.3` curve-aware training probe,
  testing pointwise-control, centered-shape, offset, and full composite loss
  profiles across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/track_2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 3.2` harmonic-offset probe that
  compares clean non-harmonic Wave 3.1-like controls against explicit
  harmonic-offset candidates across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/track_2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 3.1` offset-aware probe comparing
  post-hoc causal offset calibration, sequential residual-offset modeling, and
  multi-head shape/offset training across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md](./reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 2.2` harmonic-temporal hybrid
  campaign, comparing periodic temporal convolution, periodic `GRU`, and
  periodic `LSTM` sequence models across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md](./reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md)
  Preliminary campaign plan for the first `Wave 2.1` temporal-model entry
  campaign, comparing temporal convolution, `GRU`, and `LSTM` sequence
  baselines across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md](./reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md)
  Planning report for the next mixed feedforward campaign that combines longer schedules, denser point sampling, larger batches, and larger models.

- [reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md](./reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md)
  Planning report for the first Wave 1 structured-baseline exploratory campaign across harmonic, periodic-feature, residual, and tree-based model families.

- [reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md](./reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md)
  Planning report for the Wave 1 recovery campaign that reruns the failed harmonic, residual, and random forest branches after the model-aware summary fix.

- [reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md](./reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md)
  Historical-filename planning report for the Wave 1 residual-harmonic familywise follow-up campaign, focused on a broad hyperparameter search inside the residual harmonic MLP family.

- [reports/campaign_plans/wave_1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md](./reports/campaign_plans/wave_1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md)
  Campaign-planning report for the mixed bounded-grid plus Optuna refinement pass across all `15` directional `Wave 1` winner surfaces.

- [reports/campaign_plans/wave_1/2026-05-12-10-49-02_wave1_directional_optuna_recovery_micro_campaign_plan_report.md](./reports/campaign_plans/wave_1/2026-05-12-10-49-02_wave1_directional_optuna_recovery_micro_campaign_plan_report.md)
  Lightweight recovery-campaign plan for reproducing and validating the blocked
  neural `Optuna` launcher path before resuming the full directional HPO
  campaign.

- [reports/campaign_plans/wave_1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md](./reports/campaign_plans/wave_1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md)
  Planning report for the `periodic_mlp` fixed-feature follow-up campaign
  that mirrors the high-order harmonic bank comparison with `9` directional
  sparse and dense periodic-feature runs.

- [reports/campaign_plans/track_1/exact_paper/2026-05-13-17-33-38_track1_paper_faithful_elm_queue_addendum_plan_report.md](./reports/campaign_plans/track_1/exact_paper/2026-05-13-17-33-38_track1_paper_faithful_elm_queue_addendum_plan_report.md)
  Addendum for extending the RCIM Model-Bank Reproduction paper-faithful campaign queue with one
  `ELM` search run per direction.

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

- [reports/campaign_results/cross_wave/shape_gate_loss/2026-07-20-20-12-45_shape_gate_loss_pilot_campaign_results_report.md](./reports/campaign_results/cross_wave/shape_gate_loss/2026-07-20-20-12-45_shape_gate_loss_pilot_campaign_results_report.md)
  Final results report for the completed one-run shape-gate loss pilot on
  `polished_dataset` setpoints `Fw`, including manual remote artifact recovery,
  scalar baseline comparison, and the decision not to promote before a
  checkpoint-level shape-gated reranker pass.

- [reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-39-38_polished_rcim_model_bank_reproduction_campaign_results_report.md](./reports/campaign_results/cross_wave/polished_dataset/2026-06-29-10-39-38_polished_rcim_model_bank_reproduction_campaign_results_report.md)
  Final results report for the completed polished `RCIM Model-Bank
  Reproduction` forward/backward campaign, including direction-specific ERT
  winners, export completeness, the GitHub artifact-size boundary, and the
  boundary that official `TE Curve Verification Pipeline` curve verification
  remains separate.

- [reports/campaign_results/cross_wave/polished_dataset/2026-06-22-16-59-14_polished_dataset_stage1_smoke_campaign_results_report.md](./reports/campaign_results/cross_wave/polished_dataset/2026-06-22-16-59-14_polished_dataset_stage1_smoke_campaign_results_report.md)
  Final results report for the completed `polished_dataset` Stage 1 smoke
  campaign, including the eight-run scalar leaderboard, registry effects,
  dataset-schema acceptance, and the boundary that official
  `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-17-01-27-10_track2h_latent_state_hysteresis_campaign_results_report.md)
  Final results report for the completed `Wave 4.4` latent-state /
  hysteresis-aware campaign, including scalar branch winners, comparison
  against robust/probabilistic/MDN baselines, registry effects, and the
  boundary that official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md](./reports/campaign_results/wave_3/2026-06-15-15-30-20_wave3_harmonic_prior_residual_campaign_results_report.md)
  Final results report for the completed first real `Wave 5.1`
  harmonic-prior residual campaign, including scalar branch winners,
  profile comparison, registry effects, and the normal-closeout boundary that
  kept official `TE Curve Verification Pipeline` curve verification as a separate follow-up step.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-13-13-24-37_track2h_mixture_density_heads_campaign_results_report.md)
  Final results report for the completed third `Wave 4.3` mixture-density
  campaign, including scalar branch winners, mixture-collapse diagnostics,
  comparison against robust/probabilistic probes, and the boundary that
  official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-12-13-54-57_track2h_quantile_probabilistic_campaign_results_report.md)
  Final results report for the completed `Wave 4.2`
  quantile/probabilistic campaign, including scalar branch winners,
  calibration diagnostics, robust-loss comparison, and the boundary that
  official `TE Curve Verification Pipeline` curve verification remains separate.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-11-14-01-57_track2h_dispersion_aware_modeling_campaign_results_report.md)
  Final results report for the completed `Wave 4.1` robust-loss
  dispersion-aware campaign, including separate `global`, `Fw`, and `Bw`
  branch winners, robust-loss interpretation, registry effects, and the
  boundary that official `TE Curve Verification Pipeline` curve verification remains a separate
  operator-launched workflow.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md)
  Final results report for the completed `Wave 3.3` curve-aware training
  campaign, including separate `global`, `Fw`, and `Bw` branch winners,
  loss-profile interpretation, registry effects, and the boundary that
  official `TE Curve Verification Pipeline` curve verification remains a separate
  operator-launched workflow.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report.md)
  Final results report for the completed-after-repair `Wave 3.2`
  harmonic-offset probe campaign, including clean and harmonic candidates
  for `global`, `Fw`, and `Bw`, the runner registration repair, launcher
  wrapper hardening, registry effects, and the boundary that official
  `TE Curve Verification Pipeline` curve verification remains a separate operator-launched workflow.

- [reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md](./reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md)
  Final results report for the completed `Wave 3.1` offset-aware
  probe campaign, including separate `global`, `Fw`, and `Bw`
  branch results, runner-wrapper diagnostics, registry effects, and
  the boundary that official `TE Curve Verification Pipeline` verification remains a
  separate operator-launched workflow.

- [reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md](./reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md)
  Final results report for the completed `Wave 2.3` residual harmonic
  temporal hybrid campaign, including the 18-run sparse/dense
  harmonic-basis leaderboard, registry effects, and the explicit
  boundary that `TE Curve Verification Pipeline` remains a separate optional workflow.

- [reports/campaign_results/wave_2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md](./reports/campaign_results/wave_2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md)
  Final results report for the completed `Wave 2.2` harmonic-temporal
  hybrid campaign, including the 9-run leaderboard, registry effects,
  and the explicit boundary that `TE Curve Verification Pipeline` remains a separate
  operator-launched workflow.

- [reports/campaign_results/wave_2/2026-05-24-12-36-49_wave2_temporal_model_entry_campaign_results_report.md](./reports/campaign_results/wave_2/2026-05-24-12-36-49_wave2_temporal_model_entry_campaign_results_report.md)
  Final results report for the completed `Wave 2.1` temporal-model entry
  campaign, including temporal convolution, `GRU`, and `LSTM` candidates
  across `global`, `Fw`, and `Bw`.

- [reports/campaign_results/wave_1/2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report.md](./reports/campaign_results/wave_1/2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report.md)
  Final results report for the completed `Wave 1` `periodic_mlp` explicit
  harmonic tracking campaign, including the 9-run leaderboard and
  registry-impact summary.

- [reports/campaign_results/2026-04-17-18-33-39_track1_svm_exact_faithful_final_attempt_campaign_results_report.md](./reports/campaign_results/2026-04-17-18-33-39_track1_svm_exact_faithful_final_attempt_campaign_results_report.md)
  Final results report for the completed strict paper-faithful `SVR` final
  attempt on the residual `SVM` yellow cells, including the repeated plateau
  confirmation and the validated PDF closeout.

- [reports/campaign_results/track_1/exact_paper/2026-05-08-19-53-19_track1_forward_dt_paper_faithful_search_campaign_results_report.md](./reports/campaign_results/track_1/exact_paper/2026-05-08-19-53-19_track1_forward_dt_paper_faithful_search_campaign_results_report.md)
  Final results report for the completed single-run `forward + DT + search`
  exact-paper subset closeout, including the paper-faithful search replay
  outcome, validated PDF export, and subset bookkeeping artifacts.

- [reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md](./reports/campaign_results/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md)
  Final results report for the completed exact-paper RCIM family-bank campaign,
  including strict-reference promotion, `SVR` surrogate diagnostics, and the
  validated exact-paper export-status outcome.

- [reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md](./reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md)
  Final results report for the completed `RCIM Model-Bank Reproduction` exact-paper open-cell
  repair campaign, including paper-table closure status, harmonic-state
  changes, and the explicit confirmation that no new numeric paper cells were
  closed.

- [reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md](./reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md)
  Final results report for the completed second `RCIM Model-Bank Reproduction` paper-faithful harmonic-wise campaign, including reduced-set diagnostics, full-RCIM comparison, and the updated `Target A` status.

- [reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md](./reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md)
  Comparative results report for the executed baseline, high-density, high-epoch, and high-compute feedforward training campaign.

- [reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md](./reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md)
  Final results report for the completed mixed feedforward campaign, including the recommended best-training preset selection.

- [reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md](./reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md)
  Final results report for the completed Wave 1 recovery campaign, including campaign ranking, family-level outcomes, and program-level context.

- [reports/campaign_results/wave_1/2026-05-07-13-29-12_wave1_directional_retraining_campaign_results_report.md](./reports/campaign_results/wave_1/2026-05-07-13-29-12_wave1_directional_retraining_campaign_results_report.md)
  Final results report for the completed Wave 1 directional retraining campaign, including repaired directional registry metadata, the consolidated 15-run ranking, and the provenance-rich Python plus ONNX archive under `models/exported/`.

- [reports/campaign_results/wave_1/2026-05-17-11-40-42_wave1_directional_best_hyperparameter_search_campaign_results_report.md](./reports/campaign_results/wave_1/2026-05-17-11-40-42_wave1_directional_best_hyperparameter_search_campaign_results_report.md)
  Final results report for the completed Wave 1 directional best-hyperparameter
  search campaign, including the bounded-grid and Optuna surfaces, verified best
  hyperparameters, and refreshed Python plus ONNX exports under
  `models/exported/`.

- [reports/campaign_results/wave_1/2026-05-20-12-25-49_wave1_high_order_harmonic_tracking_campaign_results_report.md](./reports/campaign_results/wave_1/2026-05-20-12-25-49_wave1_high_order_harmonic_tracking_campaign_results_report.md)
  Final results report for the completed Wave 1 high-order harmonic tracking
  campaign, including the `RCIM` sparse, dense `0..240`, and dense `0..360`
  harmonic-bank comparison and the validated closeout artifact set.

- [reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md](./reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md)
  Final results report for the completed Wave 1 residual-harmonic family optimization campaign, including familywise ranking and the promoted residual-family winner.

#### Campaign Plans

- [reports/campaign_plans/cross_wave/polished_dataset/2026-06-25-15-28-26_polished_early_wave_parallel_training_campaign_plan_report.md](./reports/campaign_plans/cross_wave/polished_dataset/2026-06-25-15-28-26_polished_early_wave_parallel_training_campaign_plan_report.md)
  Planning gate for a 36-run early-wave `polished_dataset` retraining batch
  designed to run in parallel with the protected RCIM campaign on another
  workstation.

- [reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_rcim_model_bank_reproduction_campaign_plan_report.md](./reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_rcim_model_bank_reproduction_campaign_plan_report.md)
  Prepared campaign plan for rerunning the `RCIM Model-Bank Reproduction`
  workflow on `polished_dataset` forward and backward measured curves.

- [reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md](./reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md)
  Prepared campaign plan for the 108-run canonical full-wave model-development
  retraining package on `polished_dataset` across `global`, `fw`, and `bw`
  surfaces.

- [reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md](./reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md)
  Preliminary staged plan for retraining all eligible repository-owned model
  families on polished point measurements and performing a later Track 2
  refresh while freezing paper-original and paper-retuned models.

- [reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md](./reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 4.4` latent-state /
  hysteresis-aware package across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md](./reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md)
  Preliminary and prepared campaign plan for the first real `Wave 5.1`
  harmonic-prior residual package across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_3/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton_plan_report.md](./reports/campaign_plans/wave_3/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton_plan_report.md)
  Preliminary plan for a non-campaign `Wave 5.1` grouped harmonic-heads skeleton
  with factory construction, point/sequence forward checks, and a dry-run
  launcher.

- [reports/campaign_plans/wave_4/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton_plan_report.md](./reports/campaign_plans/wave_4/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton_plan_report.md)
  Preliminary plan for a non-campaign `Wave 5.2B` MMT feature-generator skeleton
  with leakage-aware metadata, validation outputs, and a dry-run launcher.

- [reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md](./reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md)
  Preliminary plan for hardening the `Wave 5.1` skeleton with one-batch
  training-stack validation and generating the first `Wave 5.2A` MMT equation
  diagnostic report.

- [reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md](./reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md)
  Preliminary plan for preparing `Wave 5.1` and `Wave 5.2` embryonic skeletons as
  implementation-ready but not campaign-ready scaffolds.

- [reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md](./reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 2.2` harmonic-temporal hybrid
  campaign, comparing periodic temporal convolution, periodic `GRU`, and
  periodic `LSTM` sequence models across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md](./reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md)
  Preliminary campaign plan for the first `Wave 2.1` temporal-model entry
  campaign, comparing temporal convolution, `GRU`, and `LSTM` sequence
  baselines across `global`, `Fw`, and `Bw`.

- [reports/campaign_plans/wave_1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md](./reports/campaign_plans/wave_1/2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 1` `periodic_mlp` explicit harmonic
  tracking follow-up, comparing RCIM sparse, dense `0..240`, and dense
  `0..360` fixed periodic-feature banks across `global`, `fw`, and `bw`.

- [reports/campaign_plans/wave_1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md](./reports/campaign_plans/wave_1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md)
  Preliminary campaign plan for the `Wave 1` high-order harmonic tracking
  follow-up, comparing baseline, RCIM sparse, dense `0..240`, and dense
  `0..360` harmonic banks for `harmonic_regression` and
  `residual_harmonic_mlp`.

- [reports/campaign_plans/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md](./reports/campaign_plans/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md)
  Planning report for deciding whether one final exact-faithful `SVR` rerun
  package is still justified for the residual `SVM` yellow cells.

- [reports/campaign_plans/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md](./reports/campaign_plans/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md)
  Planning report for the next umbrella `RCIM Model-Bank Reproduction` campaign package, organized
  as family-by-family amplitude and phase reproduction runs for the full
  paper-matrix objective.

- [reports/campaign_plans/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md](./reports/campaign_plans/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md)
  Planning report for the next `RCIM Model-Bank Reproduction` exact-paper open-cell repair
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

- [guide/aries_cluster_user_guide.md](./guide/aries_cluster_user_guide.md)
  Practical user guide for first use of the Unimore Aries cluster with SSH,
  GitHub SSH keys, repository setup, Conda, Slurm `srun`, and a first `sbatch`
  smoke test.

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

- [technical/2026-06/2026-06-16/2026-06-16-16-55-46_track2_multi_index_curve_first_selection_policy.md](./technical/2026-06/2026-06-16/2026-06-16-16-55-46_track2_multi_index_curve_first_selection_policy.md)
  Technical plan for shifting official `TE Curve Verification Pipeline` model selection from
  scalar-error-first ranking to multi-index curve-first selection across
  raw error, mean-centered shape, offset, harmonic / phase, robustness, and
  recommended per-surface candidates.

- [technical/2026-04/2026-04-09/2026-04-09-16-42-43_notebooklm_export_integration_for_harmonic_wise_guide.md](./technical/2026-04/2026-04-09/2026-04-09-16-42-43_notebooklm_export_integration_for_harmonic_wise_guide.md)
  Technical plan for importing, renaming, and canonically placing the generated NotebookLM concept and project exports for the harmonic-wise guide.

- [technical/2026-04/2026-04-09/2026-04-09-17-55-53_remove_redundant_language_suffixes_from_guide_exports.md](./technical/2026-04/2026-04-09/2026-04-09-17-55-53_remove_redundant_language_suffixes_from_guide_exports.md)
  Technical plan for removing redundant language suffixes from imported NotebookLM exports already organized under the English and Italiano guide folders.

- [technical/2026-04/2026-04-09/2026-04-09-18-06-16_bilingual_notebooklm_export_filename_convention.md](./technical/2026-04/2026-04-09/2026-04-09-18-06-16_bilingual_notebooklm_export_filename_convention.md)
  Technical plan for clarifying that imported bilingual NotebookLM exports should not repeat the language in filenames when the parent folder already declares it.

- [technical/2026-04/2026-04-09/2026-04-09-18-31-24_track1_second_harmonic_wise_iteration.md](./technical/2026-04/2026-04-09/2026-04-09-18-31-24_track1_second_harmonic_wise_iteration.md)
  Technical plan for the second RCIM Model-Bank Reproduction harmonic-wise iteration, including progressive harmonic-set experiments, feature engineering, and promotion back to the full RCIM harmonic set.

- [technical/2026-04/2026-04-09/2026-04-09-18-56-03_track1_second_iteration_campaign_preparation.md](./technical/2026-04/2026-04-09/2026-04-09-18-56-03_track1_second_iteration_campaign_preparation.md)
  Technical plan for packaging the second RCIM Model-Bank Reproduction harmonic-wise iteration as a dedicated operator-driven campaign with configs, launcher, launcher note, and persistent campaign state.

- [technical/2026-04/2026-04-09/2026-04-09-21-41-11_track1_second_iteration_campaign_pdf_table_refinement.md](./technical/2026-04/2026-04-09/2026-04-09-21-41-11_track1_second_iteration_campaign_pdf_table_refinement.md)
  Technical plan for refining the `Ranked Completed Runs` table layout in the RCIM Model-Bank Reproduction second-iteration campaign PDF and formalizing the unit-wrapping preference.

- [technical/2026-04/2026-04-09/2026-04-09-21-43-01_pdf_metric_header_unit_wrapping_rule.md](./technical/2026-04/2026-04-09/2026-04-09-21-43-01_pdf_metric_header_unit_wrapping_rule.md)
  Technical plan for making metric-unit second-line wrapping an explicit default rule for narrow styled-PDF metric headers.

- [technical/2026-04/2026-04-09/2026-04-09-21-49-49_track1_second_iteration_campaign_pdf_objective_pagebreak_refinement.md](./technical/2026-04/2026-04-09/2026-04-09-21-49-49_track1_second_iteration_campaign_pdf_objective_pagebreak_refinement.md)
  Technical plan for tightening the `Objective And Outcome` bullets so the RCIM Model-Bank Reproduction second-iteration campaign PDF avoids a weak section start on a nearly empty page.

- [technical/2026-04/2026-04-09/2026-04-09-21-53-17_track1_second_iteration_campaign_pdf_rank_column_rebalance.md](./technical/2026-04/2026-04-09/2026-04-09-21-53-17_track1_second_iteration_campaign_pdf_rank_column_rebalance.md)
  Technical plan for slightly widening the `Rank` column and correspondingly shrinking `Test MAE` in the RCIM Model-Bank Reproduction second-iteration campaign PDF table.

- [technical/2026-04/2026-04-09/2026-04-09-22-10-21_track1_campaign_random_forest_bundle_git_lfs_tracking.md](./technical/2026-04/2026-04-09/2026-04-09-22-10-21_track1_campaign_random_forest_bundle_git_lfs_tracking.md)
  Technical plan for tracking the oversized RandomForest harmonic-wise campaign bundle through Git LFS so the pending commit remains GitHub-safe.

- [technical/2026-04/2026-04-30/2026-04-30-17-02-45_rcim_recovered_original_workflow_comment_style_and_full_surface_cleanup.md](./technical/2026-04/2026-04-30/2026-04-30-17-02-45_rcim_recovered_original_workflow_comment_style_and_full_surface_cleanup.md)
  Technical plan for the second recovered-original RCIM workflow cleanup pass, focused on comment style, comment accuracy, full-surface stale-residue removal, and dependency-aligned readability normalization.

- [technical/2026-05/2026-05-02/2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md](./technical/2026-05/2026-05-02/2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md)
  Technical plan for simplifying the recovered RCIM pickle-cache contract to a
  shared `data/original_pipeline_instances/` directory, adding an explicit
  cache-rebuild flag, and deferring dataset-shrinking-aware cache partitioning
  to the backlog.

- [technical/2026-05/2026-05-11/2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md](./technical/2026-05/2026-05-11/2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md)
  Technical plan for restoring recovered-original-style per-target `Python +
  ONNX` export artifacts in the exact-paper workflow instead of `ONNX` only
  per-target exports.

- [technical/2026-05/2026-05-11/2026-05-11-09-59-51_track1_exact_paper_linear_svr_fallback_alignment.md](./technical/2026-05/2026-05-11/2026-05-11-09-59-51_track1_exact_paper_linear_svr_fallback_alignment.md)
  Technical plan for aligning the RCIM Model-Bank Reproduction exact-paper `SVR` family with the
  recovered-original pragmatic `LinearSVR` fallback used in place of the
  historical `SVR(kernel="linear")` branch.

- [technical/2026-05/2026-05-11/2026-05-11-16-26-01_track1_exact_paper_elm_export_hardening_and_quiet_lgbm.md](./technical/2026-05/2026-05-11/2026-05-11-16-26-01_track1_exact_paper_elm_export_hardening_and_quiet_lgbm.md)
  Technical plan for porting the recovered-original ELM export hardening into
  the RCIM Model-Bank Reproduction exact-paper shared exporter and for adopting the quieter
  repository-owned `LGBMRegressor` factory in the active RCIM Model-Bank Reproduction exact-paper
  family bank.

- [technical/2026-05/2026-05-11/2026-05-11-16-28-59_track1_exact_paper_add_elm_and_quiet_lgbm.md](./technical/2026-05/2026-05-11/2026-05-11-16-28-59_track1_exact_paper_add_elm_and_quiet_lgbm.md)
  Superseding technical plan for adding `ELM` to the canonical RCIM Model-Bank Reproduction
  exact-paper family bank and for adopting the quieter repository-owned
  `LGBMRegressor` factory.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` as the visual golden standard for future styled analytical PDF reports.
- Treat `reference_summaries/06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Use `reference_codes/` when a future implementation task needs repository-specific examples instead of only high-level style rules.
- Keep this index updated whenever new project documents are added.
