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

### Script Documentation

- [scripts/datasets/transmission_error_dataset.md](./scripts/datasets/transmission_error_dataset.md)
  Script-level documentation for the TE dataset parser, PyTorch dataset, and dataloader utilities.
- [scripts/datasets/visualize_transmission_error.md](./scripts/datasets/visualize_transmission_error.md)
  Script-level documentation for the TE curve visualization utility.
- [scripts/training/train_feedforward_network.md](./scripts/training/train_feedforward_network.md)
  Script-level documentation for the first PyTorch Lightning feedforward training entry point.

### Reports

#### Analysis

- [reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md](./reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md)
  Full analytical report for the executed feedforward proof run, including interpretation and comparison against the reference papers.
- [reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md](./reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md)
  Detailed explanation of the training configuration entries, their practical effects, and a comparison between trial, baseline, and heavier workstation-oriented variants.
- [reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf](./reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf)
  PDF export of the detailed training-configuration analysis report.

#### Campaign Plans

- [reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md](./reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md)
  Planning report for the next mixed feedforward campaign that combines longer schedules, denser point sampling, larger batches, and larger models.

#### Campaign Results

- [reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md](./reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md)
  Comparative results report for the executed baseline, high-density, high-epoch, and high-compute feedforward training campaign.

### Guides

- [guide/project_usage_guide.md](./guide/project_usage_guide.md)
  Practical user guide for environment activation, dataset processing, and TE visualization.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `reference_summaries/06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Use `reference_codes/` when a future implementation task needs repository-specific examples instead of only high-level style rules.
- Keep this index updated whenever new project documents are added.

