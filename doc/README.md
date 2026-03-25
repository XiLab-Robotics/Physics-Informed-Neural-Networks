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

### Reference Code Notes

- [reference_codes/README.md](./reference_codes/README.md)
  Index of detailed notes extracted from the reference-code submodules.
- [reference_codes/blind_handover_controller_reference.md](./reference_codes/blind_handover_controller_reference.md)
  Main style baseline for naming, comments, structure, utilities, and Lightning training flow.
- [reference_codes/mediapipe_gesture_recognition_reference.md](./reference_codes/mediapipe_gesture_recognition_reference.md)
  Supporting reference for Hydra-based configuration and ML training utilities.
- [reference_codes/multimodal_fusion_reference.md](./reference_codes/multimodal_fusion_reference.md)
  Supporting reference for compact ROS pipelines, explicit label mapping, and simple Lightning baselines.

### Technical Documents

#### 2026-03-10

- [technical/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md](./technical/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md)
  Technical document for the Conda, PyTorch, and PyTorch Lightning environment baseline.
- [technical/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md](./technical/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md)
  Technical document for the validated TE dataset-processing pipeline and raw-data reconstruction path.
- [technical/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md](./technical/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md)
  Technical document for the `scripts/`, `config/`, and per-script documentation repository rules.
- [technical/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md](./technical/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md)
  Technical document for the grouped `doc/` folder reorganization.
- [technical/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md](./technical/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md)
  Technical document for moving the existing agent submodule and adding the requested `agents/` submodule collection.
- [technical/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md](./technical/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md)
  Technical document for enforcing the technical-document approval workflow plus a mandatory final Git commit.
- [technical/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md](./technical/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md)
  Technical document for replacing the archived reference code `.zip` files in `reference/codes/` with Git submodules.
- [technical/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md](./technical/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md)
  Technical document for creating persistent `doc/reference_codes/` notes from the reference-code submodules.
- [technical/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md](./technical/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md)
  Technical document for the first modular PyTorch Lightning feedforward baseline for TE regression.
- [technical/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md](./technical/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md)
  Technical document for clarifying the original CSV header typo `Poisition_Output_Reducer_Fw` versus the normalized internal column naming.
- [technical/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md](./technical/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md)
  Technical document for requiring a detailed `project_usage_guide.md` update before commit whenever repository functionality changes.
- [technical/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md](./technical/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md)
  Technical document for refreshing `project_usage_guide.md` so it matches the current runnable training and dataset workflows.
- [technical/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md](./technical/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md)
  Technical document for tuning the default dataloader worker and memory-pinning settings of the current feedforward training workflow.
- [technical/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md](./technical/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md)
  Technical document for fixing direct execution of the feedforward training entry point when the repository root is missing from `sys.path`.
- [technical/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md](./technical/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md)
  Technical document for making the feedforward training terminal output cleaner, colorized, and less noisy on Windows.
- [technical/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md](./technical/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md)
  Technical document for formalizing dependency tracking in the workflow and auditing current imports against `requirements.txt`.

#### 2026-03-11

- [technical/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md](./technical/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md)
  Technical document for removing the remaining Lightning startup tip and `_pytree` sanity-check warning from feedforward training output.
- [technical/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md](./technical/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md)
  Technical document for correcting the generator-based context-manager return annotation in the training entry point.
- [technical/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md](./technical/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md)
  Technical document for normalizing blank-line spacing around top-level function definitions in the feedforward training entry point.
- [technical/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md](./technical/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md)
  Technical document for extending the approved function-spacing convention to all project-authored Python scripts.
- [technical/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md](./technical/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md)
  Technical document for extending the approved blank-line spacing convention to top-level class and dataclass declarations.
- [technical/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md](./technical/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md)
  Technical document for propagating the broader manual coding style introduced in commit `228a999c94eb67d1c07eebfbd87c05903e99b694` to the remaining project scripts.
- [technical/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md](./technical/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md)
  Technical document for updating the persistent programming style guide with the approved spacing rules and the broader manual refactoring conventions.
- [technical/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md](./technical/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md)
  Technical document for aligning the persistent programming style guide with the latest approved manual code-style refactoring commit.
- [technical/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md](./technical/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md)
  Technical document for adding a proof feedforward training run, a held-out test phase, and a per-run result report artifact.

#### 2026-03-12

- [technical/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md](./technical/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md)
  Technical document for writing a full analytical report of the feedforward proof run with narrative interpretation and comparison against the reference papers.
- [technical/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md](./technical/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md)
  Technical document for producing a detailed training-configuration explanation report plus a PDF export and heavier workstation-oriented configuration proposals.
- [technical/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md](./technical/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md)
  Technical document for executing and comparing the pending baseline and workstation-oriented feedforward training variants.
- [technical/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md](./technical/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md)
  Technical document for executing a mixed campaign that combines longer schedules, denser point sampling, larger batches, and larger feedforward models.
- [technical/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md](./technical/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md)
  Technical document for making preliminary planning reports and final results reports mandatory companions to every future training campaign.
- [technical/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md](./technical/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md)
  Technical document for renaming the current report files so they include the full timestamp in their filenames.
- [technical/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md](./technical/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md)
  Technical document for reorganizing the technical-document tree by day and the report tree by report type.
- [technical/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md](./technical/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md)
  Technical document for regenerating the training-configuration analysis PDF with a much stronger visual layout and print-oriented styling.
- [technical/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md](./technical/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md)
  Technical document for redesigning the analytical PDF again with a restrained blue palette, white background, better page flow, and more professional typography.
- [technical/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md](./technical/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md)
  Technical document for correcting the analytical PDF printable margins and replacing the dense configuration table with a cleaner professional layout.
- [technical/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md](./technical/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md)
  Technical document for fixing the remaining technical-table fit issues in the analytical PDF and enforcing post-export PDF validation.
- [technical/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md](./technical/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md)
  Technical document for refining the three configuration tables so each one repeats the config name and uses more consistent centered alignment.
- [technical/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md](./technical/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md)
  Technical document for declaring the approved analytical PDF as the project golden standard and encoding its style rules for future reports.
- [technical/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md](./technical/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md)
  Technical document for refactoring the styled PDF exporter to match repository coding style and clarifying that the style rules also apply to utility/report scripts.
- [technical/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md](./technical/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md)
  Technical document for changing the repository workflow so every Git commit requires a final explicit user approval after the work is completed.
- [technical/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md](./technical/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md)
  Technical document for shortening the styled PDF exporter comments and aligning the persistent coding-style rules with the latest user-approved manual refactor.
- [technical/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md](./technical/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md)
  Technical document for reorganizing `config/`, introducing a queue-based batch training workflow, and generating campaign execution reports for later post-training analysis.
- [technical/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md](./technical/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md)
  Technical document for automatic campaign YAML generation, active-campaign state tracking, protected-file warnings, and completion/cancellation handling.

#### 2026-03-13

- [technical/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md](./technical/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md)
  Technical document for writing the final mixed-campaign results report and selecting the best current feedforward training preset.
- [technical/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md](./technical/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md)
  Technical document for making PDF export and PDF validation mandatory for final campaign-results reports.
- [technical/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md](./technical/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md)
  Technical document for repairing the mixed-campaign PDF table widths and tightening the rule so future table-layout defects must be caught before task closure.

#### 2026-03-14

- [technical/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md](./technical/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md)
  Technical document for fixing remaining header spill and semantic config wrapping issues in the campaign-results PDF tables.
- [technical/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md](./technical/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md)
  Technical document for enforcing vertical table-cell centering and cleaner section page-break behavior in the campaign-results PDF.
- [technical/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md](./technical/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md)
  Technical document for evaluating a cleaner internal code layout and moving the external agent submodules under `reference/agents/`.
- [technical/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md](./technical/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md)
  Technical document for moving root `models/` and `training/` source code under `scripts/`, reserving root `models/` for artifacts, and relocating agent submodules under `reference/agents/`.
- [technical/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md](./technical/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md)
  Technical document for reviewing the current GPU training path and proposing practical transfer, precision, and Trainer-level performance optimizations.

#### 2026-03-16

- [technical/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md](./technical/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md)
  Technical document for validating and executing the project environment migration from Python 3.10 to Python 3.12.

#### 2026-03-17

- [technical/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md](./technical/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md)
  Technical planning document for the TE model-family roadmap across standard, temporal, hybrid, and PINN approaches.
- [technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md](./technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md)
  Technical backlog document for implementing, validating, smoke-testing, and comparing all approved TE model families through campaign waves.
- [technical/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md](./technical/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md)
  Technical note for keeping Lightweight Transformer and Neural ODE families explicitly in scope as low-priority exploratory options.
- [technical/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md](./technical/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md)
  Technical review note for adding explicit State-Space, Mixture-of-Experts, and optional Kernel/GP families to the TE planning set.
- [technical/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md](./technical/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md)
  Technical document for the shared training, smoke-test, validation, and metrics infrastructure required before implementing the planned TE model families.
- [technical/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md](./technical/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md)
  Technical document for moving the TE implementation backlog into a privileged live location under `doc/running/`.
- [technical/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md](./technical/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md)
  Technical document for cleaning up redundant `variable=variable` function-call arguments while preserving explicit keywords where they improve readability.
- [technical/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md](./technical/2026-03-17/2026-03-17-19-34-45_training_output_reorganization_and_best_result_registry.md)
  Technical document for reorganizing training outputs by artifact type and adding explicit campaign, family, and program best-result registries.
- [technical/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md](./technical/2026-03-17/2026-03-17-20-06-23_legacy_feedforward_output_migration.md)
  Technical document for migrating the historical `output/feedforward_network/` artifacts into the new training-run structure and rewriting repository-authored path references.
- [technical/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md](./technical/2026-03-17/2026-03-17-20-24-57_remove_feedforward_legacy_backward_compatibility.md)
  Technical document for removing the remaining feedforward-specific legacy snapshot compatibility from the active training pipeline.
- [technical/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md](./technical/2026-03-17/2026-03-17-20-46-59_formalize_feedforward_reference_baseline_run.md)
  Technical document for formalizing the registry-selected feedforward run as the canonical reference baseline before Wave 1.
- [technical/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md](./technical/2026-03-17/2026-03-17-21-00-57_wave1_structured_baseline_campaign_preparation.md)
  Technical document for preparing Wave 1 structured-baseline implementation and the first exploratory campaign against the formalized feedforward reference baseline.

#### 2026-03-18

- [technical/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md](./technical/2026-03-18/2026-03-18-00-12-54_model_and_training_explanatory_report_rule.md)
  Technical document for making model-level explanatory reports mandatory whenever a new model or new model-specific training workflow is introduced.
- [technical/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md](./technical/2026-03-18/2026-03-18-00-22-41_retroactive_model_explanatory_reports_for_existing_structured_models.md)
  Technical document for creating retroactive explanatory reports for the already implemented structured TE model families.
- [technical/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md](./technical/2026-03-18/2026-03-18-00-39-43_pdf_export_for_existing_model_explanatory_reports.md)
  Technical document for exporting the existing model-explanatory reports to styled PDFs and validating the real exported artifacts.
- [technical/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md](./technical/2026-03-18/2026-03-18-00-45-12_model_report_diagram_and_image_rule.md)
  Technical document for requiring visual conceptual diagrams and image assets inside future model-explanatory reports and their PDF exports.
- [technical/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md](./technical/2026-03-18/2026-03-18-00-56-18_retroactive_model_report_diagrams_and_pdf_image_integration.md)
  Technical document for retroactively adding diagrams to the existing structured-model reports and preserving those images in the exported PDFs.
- [technical/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md](./technical/2026-03-18/2026-03-18-01-09-27_model_report_diagram_quality_and_dual_visualization_upgrade.md)
  Technical document for correcting diagram layout defects, introducing reusable diagram generation, removing figure-background clashes, and adding both conceptual and architecture diagrams to the model reports.
- [technical/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md](./technical/2026-03-18/2026-03-18-01-24-18_diagram_geometry_and_pdf_figure_layout_corrections.md)
  Technical document for correcting diagram geometry defects, improving figure centering, replacing pseudo-arrows with real connectors, and revalidating the SVG and PDF outputs.
- [technical/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md](./technical/2026-03-18/2026-03-18-17-19-42_report_pipeline_standardization_and_tooling_env.md)
  Technical document for standardizing the report-generation pipeline with a repository-owned orchestrator, a persistent PDF-validation tooling environment, and cleaner temporary-artifact management.
- [technical/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md](./technical/2026-03-18/2026-03-18-17-30-42_report_pipeline_temp_cleanup.md)
  Technical document for removing obsolete report-pipeline temporary environments and retaining only the intended standardized temporary layout.
- [technical/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md](./technical/2026-03-18/2026-03-18-17-38-39_full_report_pipeline_temp_reset.md)
  Technical document for fully removing the remaining standardized report-pipeline runtime temp root and leaving the repository without runtime temporary folders.
- [technical/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md](./technical/2026-03-18/2026-03-18-17-48-21_section_comment_frequency_rule_and_report_script_retrofit.md)
  Technical document for making frequent internal section comments an explicit persistent style rule and retrofitting that style into the recent report scripts.
- [technical/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md](./technical/2026-03-18/2026-03-18-18-05-52_targeted_model_script_comment_retrofit.md)
  Technical document for a focused section-comment retrofit of the remaining model scripts that still underuse internal `# ...` stage markers.
- [technical/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md](./technical/2026-03-18/2026-03-18-18-17-36_repository_wide_comment_semantic_audit.md)
  Technical document for auditing all Python comments under `scripts/` and correcting only the ones whose meaning no longer matches the code they describe.
- [technical/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md](./technical/2026-03-18/2026-03-18-18-43-52_second_pass_model_report_diagram_layout_refinement.md)
  Technical document for the second pass of model-report diagram refinement, focused on connector pile-up, slide centering, multiline card layout, and safer routing.
- [technical/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md](./technical/2026-03-18/2026-03-18-19-24-36_third_pass_model_report_arrow_and_spacing_refinement.md)
  Technical document for the third pass of model-report diagram refinement, focused on simplifying neuron arrows, enforcing perpendicular box routing, arrowhead clearance, and model-specific spacing fixes.
- [technical/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md](./technical/2026-03-18/2026-03-18-20-01-27_generate_model_report_diagrams_spacing_cleanup.md)
  Technical document for a formatting-only cleanup that normalizes redundant blank lines between top-level definitions in the model-report diagram generator.
- [technical/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md](./technical/2026-03-18/2026-03-18-20-05-42_repository_wide_script_spacing_cleanup.md)
  Technical document for a formatting-only repository-wide cleanup that normalizes redundant blank lines between top-level definitions across the Python scripts under `scripts/`.

#### 2026-03-20

- [technical/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md](./technical/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md)
  Technical planning document for a beginner-to-university learning guide covering neural-network foundations, training/validation/testing, and the TE model-family curriculum from feedforward baselines to planned advanced architectures.
- [technical/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md](./technical/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md)
  Technical planning document for exporting the learning guides to PDF and requiring explicit user approval of generated guide images before final PDF generation.
- [technical/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md](./technical/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md)
  Technical planning document for preparing NotebookLM-ready video-guide source packages and adding the related approval-gated workflow rule for future learning-guide videos.
- [technical/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md](./technical/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md)
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
- [scripts/training/validate_training_setup.md](./scripts/training/validate_training_setup.md)
  Script-level documentation for the one-batch validation check used by the shared Wave 0 training infrastructure.
- [scripts/training/run_training_smoke_test.md](./scripts/training/run_training_smoke_test.md)
  Script-level documentation for the minimal Lightning smoke-test entry point used by the shared Wave 0 training infrastructure.
- [scripts/tooling/isolated_mode.md](./scripts/tooling/isolated_mode.md)
  Script-level documentation for the isolated-session manager that creates locked snapshots, manifest/checklist files, lock-validation reports, and session close-out actions.
- [scripts/tooling/markdown_style_check.md](./scripts/tooling/markdown_style_check.md)
  Script-level documentation for the repository-owned Markdown warning checker that scans source `.md` files for blank-line, heading, and single-title issues.
- [scripts/tooling/run_markdownlint.md](./scripts/tooling/run_markdownlint.md)
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
- [guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md](./guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md)
  Foundational learning guide that explains supervised learning, neurons, MLPs, loss functions, backpropagation, and generalization in the TE project context.
- [guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.pdf](./guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.pdf)
  Styled PDF export of the neural-network foundations learning guide.
- [guide/Neural%20Network%20Foundations/video_guide_package/video_guide_source_brief.md](./guide/Neural%20Network%20Foundations/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the neural-network foundations video guide package.
- [guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md](./guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md)
  Learning guide that explains dataset splits, optimizer-driven training, validation logic, test-set discipline, and TE-specific evaluation pitfalls.
- [guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.pdf](./guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.pdf)
  Styled PDF export of the training, validation, and testing learning guide.
- [guide/Training,%20Validation,%20And%20Testing/video_guide_package/video_guide_source_brief.md](./guide/Training,%20Validation,%20And%20Testing/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the training, validation, and testing video guide package.
- [guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md](./guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md)
  Curriculum guide that introduces the TE model families from feedforward and harmonic baselines through the planned temporal, hybrid, and PINN directions.
- [guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.pdf](./guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.pdf)
  Styled PDF export of the TE model curriculum learning guide.
- [guide/TE%20Model%20Curriculum/video_guide_package/video_guide_source_brief.md](./guide/TE%20Model%20Curriculum/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the TE model curriculum video guide package.
- [guide/FeedForward%20Network/FeedForward%20Network.md](./guide/FeedForward%20Network/FeedForward%20Network.md)
  Learning guide that explains the feedforward architecture as the baseline MLP for the TE curriculum, with implementation and training context.
- [guide/FeedForward%20Network/FeedForward%20Network.pdf](./guide/FeedForward%20Network/FeedForward%20Network.pdf)
  Styled PDF export of the feedforward network learning guide.
- [guide/FeedForward%20Network/video_guide_package/video_guide_source_brief.md](./guide/FeedForward%20Network/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the feedforward network video guide package.
- [guide/Harmonic%20Regression/Harmonic%20Regression.md](./guide/Harmonic%20Regression/Harmonic%20Regression.md)
  Learning guide that explains harmonic regression as the periodic structured baseline and its repository integration.
- [guide/Harmonic%20Regression/Harmonic%20Regression.pdf](./guide/Harmonic%20Regression/Harmonic%20Regression.pdf)
  Styled PDF export of the harmonic regression learning guide.
- [guide/Harmonic%20Regression/video_guide_package/video_guide_source_brief.md](./guide/Harmonic%20Regression/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the harmonic regression video guide package.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md)
  Learning guide that explains the periodic-feature hybrid architecture that combines explicit periodic encoding with an MLP backend.
- [guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf](./guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.pdf)
  Styled PDF export of the periodic-feature network learning guide.
- [guide/Periodic%20Feature%20Network/video_guide_package/video_guide_source_brief.md](./guide/Periodic%20Feature%20Network/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the periodic-feature network video guide package.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md)
  Learning guide that explains the residual-harmonic hybrid architecture and its structured-plus-residual decomposition.
- [guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf](./guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.pdf)
  Styled PDF export of the residual-harmonic network learning guide.
- [guide/Residual%20Harmonic%20Network/video_guide_package/video_guide_source_brief.md](./guide/Residual%20Harmonic%20Network/video_guide_package/video_guide_source_brief.md)
  NotebookLM-oriented source brief for the residual-harmonic network video guide package.
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

#### Campaign Plans

- [reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md](./reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md)
  Planning report for the next mixed feedforward campaign that combines longer schedules, denser point sampling, larger batches, and larger models.
- [reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md](./reports/campaign_plans/2026-03-17-21-01-47_wave1_structured_baseline_campaign_plan_report.md)
  Planning report for the first Wave 1 structured-baseline exploratory campaign across harmonic, periodic-feature, residual, and tree-based model families.
- [reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md](./reports/campaign_plans/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md)
  Planning report for the Wave 1 recovery campaign that reruns the failed harmonic, residual, and random forest branches after the model-aware summary fix.
- [technical/2026-03-20/2026-03-20-15-55-21_campaign_launcher_short_command.md](./technical/2026-03-20/2026-03-20-15-55-21_campaign_launcher_short_command.md)
  Technical document for a short launcher wrapper that keeps the existing training logs and terminal behavior intact.
- [technical/2026-03-24/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md](./technical/2026-03-24/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md)
  Technical document for the final reporting work of the completed Wave 1 structured baseline recovery campaign.
- [technical/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_analysis.md](./technical/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_analysis.md)
  Integration analysis for recovering the isolated documentation work onto the synchronized repository state.
- [technical/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_checklist.md](./technical/2026-03-24/2026-03-24-16-12-46_sphinx_isolated_integration_checklist.md)
  Explicit checklist for the isolated-work recovery and the first canonical Sphinx integration steps.
- [technical/2026-03-24/2026-03-24-19-40-45_sphinx_batch0_canonical_foundation.md](./technical/2026-03-24/2026-03-24-19-40-45_sphinx_batch0_canonical_foundation.md)
  Technical implementation note for the canonical Batch 0 Sphinx foundation.
- [technical/2026-03-24/2026-03-24-19-59-54_sphinx_canonical_integration_phase1.md](./technical/2026-03-24/2026-03-24-19-59-54_sphinx_canonical_integration_phase1.md)
  Technical implementation note for the first canonical integration phase after the Sphinx foundation batch.
- [technical/2026-03-24/2026-03-24-20-05-31_sphinx_canonical_integration_phase2.md](./technical/2026-03-24/2026-03-24-20-05-31_sphinx_canonical_integration_phase2.md)
  Technical implementation note for the second canonical integration phase that exposes recovered isolated documentation assets and the styled PDF exporter inside the Sphinx portal.
- [technical/2026-03-24/2026-03-24-20-13-56_sphinx_canonical_integration_phase3_core_training_infrastructure.md](./technical/2026-03-24/2026-03-24-20-13-56_sphinx_canonical_integration_phase3_core_training_infrastructure.md)
  Technical implementation note for the next canonical Sphinx integration batch focused on the shared training infrastructure API surface.
- [technical/2026-03-24/2026-03-24-20-23-49_sphinx_canonical_integration_phase4_model_family_api_coverage.md](./technical/2026-03-24/2026-03-24-20-23-49_sphinx_canonical_integration_phase4_model_family_api_coverage.md)
  Technical implementation note for the next canonical Sphinx integration batch focused on model-family API coverage and model-factory routing.
- [technical/2026-03-24/2026-03-24-20-58-19_isolated_integration_reconciliation_and_learning_guide_migration.md](./technical/2026-03-24/2026-03-24-20-58-19_isolated_integration_reconciliation_and_learning_guide_migration.md)
  Technical reconciliation note for completing the still-open isolated-branch integration work around learning-guide migration and NotebookLM media relocation.
- [technical/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md](./technical/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md)
  Technical verification note for checking whether any isolated-branch work still remains outside the canonical repository state after reconciliation.
- [technical/2026-03-24/2026-03-24-22-51-28_documentation_poc_cleanup_and_archival.md](./technical/2026-03-24/2026-03-24-22-51-28_documentation_poc_cleanup_and_archival.md)
  Technical cleanup note for relocating the remaining isolated documentation proof-of-concept artifacts out of the repository root and into an archival location.
- [technical/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md](./technical/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md)
  Technical cleanup note for retiring the now-empty isolated handoff roots and relocating their remaining provenance artifacts into a dedicated archive subtree.
- [technical/2026-03-25/2026-03-25-12-39-38_isolated_mode_rework.md](./technical/2026-03-25/2026-03-25-12-39-38_isolated_mode_rework.md)
  Technical design document for replacing the old isolated handoff pattern with explicit session roots, locked-file snapshots, structured manifests, and deterministic integration checklists.
- [technical/2026-03-25/2026-03-25-13-03-35_remove_legacy_isolated_handoff_archive.md](./technical/2026-03-25/2026-03-25-13-03-35_remove_legacy_isolated_handoff_archive.md)
  Technical cleanup document for preserving only the useful isolated-mode lessons in canonical documentation and removing the legacy `reference/isolated_handoff/` archive subtree.
- [technical/2026-03-25/2026-03-25-13-10-20_markdown_warning_cleanup_and_lint_workflow.md](./technical/2026-03-25/2026-03-25-13-10-20_markdown_warning_cleanup_and_lint_workflow.md)
  Technical document for cleaning up current Markdown warnings and adding a repository-owned terminal checker so future Markdown files can be validated directly from source.
- [technical/2026-03-25/2026-03-25-14-05-16_extended_markdownlint_rule_baseline.md](./technical/2026-03-25/2026-03-25-14-05-16_extended_markdownlint_rule_baseline.md)
  Technical document for formalizing the broader Markdownlint baseline, tracked rule policy, and canonical non-`reference/` scope.
- [technical/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md](./technical/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md)
  Technical document for redesigning the repository README as a GitHub-facing landing page for a new human user.

#### Campaign Results

- [reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md](./reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md)
  Comparative results report for the executed baseline, high-density, high-epoch, and high-compute feedforward training campaign.
- [reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md](./reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md)
  Final results report for the completed mixed feedforward campaign, including the recommended best-training preset selection.
- [reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md](./reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md)
  Final results report for the completed Wave 1 recovery campaign, including campaign ranking, family-level outcomes, and program-level context.

### Running State

- [running/te_model_live_backlog.md](./running/te_model_live_backlog.md)
  Privileged live backlog for the TE model implementation program, including current wave status, next steps, and deferred branches.
- [running/README.md](./running/README.md)
  Explanation of the persistent running-state workflow, including the live backlog and active campaign tracking.
- [running/active_training_campaign.yaml](./running/active_training_campaign.yaml)
  Current prepared or active training campaign state, including protected files and launch commands.

### Guides

- [guide/project_usage_guide.md](./guide/project_usage_guide.md)
  Practical user guide for environment activation, dataset processing, and TE visualization.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` as the visual golden standard for future styled analytical PDF reports.
- Treat `reference_summaries/06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Use `reference_codes/` when a future implementation task needs repository-specific examples instead of only high-level style rules.
- Keep this index updated whenever new project documents are added.
