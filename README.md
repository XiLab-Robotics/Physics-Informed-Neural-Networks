# StandardML - Codex

Machine-learning workflows for rotational transmission error modeling in RV
reducers, with a repository structure aimed at reproducible experiments,
engineering-oriented documentation, and future physics-informed extensions.

## Overview

This repository studies **rotational transmission error (TE)** in RV reducers
used in industrial robotics.

The project combines:

- experimental TE datasets from a dedicated test rig;
- structured machine-learning baselines implemented in Python;
- reproducible training, validation, and campaign workflows;
- documentation aimed at both engineering use and future model extension;
- a roadmap toward more structured hybrid models and later full PINN work.

The repository name still reflects the long-term physics-informed direction, but
the current implemented surface already includes practical feedforward,
harmonic, periodic-feature, residual-harmonic, and tree-based baselines.

## Why This Repository Exists

Transmission error is a key indicator for reducer accuracy, vibration behavior,
and final robot joint positioning quality.

In this project, the goal is not only to fit data well. The goal is to build TE
models that are:

- accurate on measured operating conditions;
- interpretable enough for engineering analysis;
- structured enough to support future TwinCAT / PLC-friendly deployment;
- extensible toward hybrid and later physics-informed formulations.

## Current Status

Implemented today:

- validated TE dataset processing and visualization utilities;
- feedforward TE regression training with PyTorch Lightning;
- structured baselines for harmonic regression, periodic-feature MLP, and
  residual-harmonic MLP workflows;
- tree-based baselines for comparison;
- one-batch validation checks and smoke-test utilities;
- batch campaign execution and artifact tracking;
- styled report generation and PDF validation tooling;
- repository-owned TwinCAT/TestRig video-guide tooling for high-quality transcript extraction, evidence-driven snapshots, and OCR-assisted report synthesis through Google GenAI;
- a repository-owned LAN AI node path for remote `LM Studio`, `faster-whisper`, and `PaddleOCR` integration while keeping repository orchestration on the current workstation;
- repository-owned per-video report generation for analyzed TwinCAT/TestRig video guides;
- dual `NotebookLM` source-package tracks for guide-local concept videos and
  repository-specific project videos;
- repository-owned isolated-mode and Markdown validation tooling.

Planned or future work:

- broader sequence-aware models such as lagged-window, GRU, LSTM, and TCN
  families;
- additional hybrid TE model families;
- export and deployment hardening for production-oriented inference;
- full PINN formulation once the physics residual design is mature enough.

## Repository At A Glance

The most important folders for a new user are:

- `scripts/`
  Python entry points for training, reporting, and tooling.
- `config/`
  YAML configuration files for datasets, presets, and campaigns.
- `data/datasets/`
  Expected location for validated TE data.
- `output/`
  Training runs, validation checks, smoke tests, campaigns, and registries.
- `doc/`
  Main human-authored documentation, guides, reports, and technical notes.
- `reference/`
  External reference material and imported codebases kept outside the main
  canonical workflow.

If you only want to get started, begin with:

- [Project Usage Guide](./doc/guide/project_usage_guide.md)
- [Documentation Index](./doc/README.md)
- [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai_node_server.md)

## Quick Start

### 0. Clone Safely On Windows

Before cloning on Windows, enable Git long-path support from an elevated
PowerShell prompt:

```powershell
git config --system core.longpaths true
```

Then clone the repository into a reasonably short path such as `C:\Work`.

### 1. Create The Environment

```powershell
conda create -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

### 2. Check The Dataset Root

The default dataset location is configured in
`config/datasets/transmission_error_dataset.yaml`:

```yaml
paths:
  dataset_root: data/datasets
```

Update that path if your validated TE dataset is stored elsewhere.

### 3. Run A First Training Command

For a lightweight verification run:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/trial.yaml
```

For the default feedforward baseline:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

Artifacts are written under:

- `output/training_runs/<model_family>/<run_instance_id>/`

## Example Workflows

### Run The Current Best Feedforward Preset

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/best_training.yaml
```

### Launch A Prepared Campaign

```powershell
python scripts/training/run_training_campaign.py
```

### Use The Short Wave 1 Recovery Launcher

```powershell
.\scripts\campaigns\run_wave1_structured_baseline_recovery_campaign.ps1
```

### Use The Wave 1 Residual Launcher

```powershell
.\scripts\campaigns\run_wave1_residual_harmonic_family_campaign.ps1
```

### Check Markdown Quality For Repository Docs

```powershell
python -B scripts/tooling/run_markdownlint.py
python -B scripts/tooling/markdown_style_check.py --fail-on-warning
```

### Analyze TwinCAT Video Guides

```powershell
python -B scripts/tooling/analyze_video_guides.py
```

### Extract High-Quality TwinCAT Video Knowledge

```powershell
python -B scripts/tooling/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1
```

### Use The LAN AI Node For Video Knowledge Extraction

```powershell
python -B scripts/tooling/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider lan
```

Before using the LAN path, complete:

- [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai_node_server.md)

## Documentation For New Users

If you are opening the repository for the first time, use this reading order:

1. [Project Usage Guide](./doc/guide/project_usage_guide.md)
   Main runnable-workflow reference.
2. [Documentation Index](./doc/README.md)
   Entry point for guides, reports, and technical notes.
3. [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai_node_server.md)
   Full Windows-first setup for the remote `LM Studio` and LAN AI node
   workstation.
4. Model guides under `doc/guide/`
   Best place to understand the implemented model families at a conceptual
   level.
5. Analysis reports under `doc/reports/analysis/`
   Useful when you want deeper training or model-family interpretation.

Recommended guide entry points:

- [Neural Network Foundations](./doc/guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md)
- [Training, Validation, And Testing](./doc/guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md)
- [TE Model Curriculum](./doc/guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md)
- [FeedForward Network](./doc/guide/FeedForward%20Network/FeedForward%20Network.md)
- [Harmonic Regression](./doc/guide/Harmonic%20Regression/Harmonic%20Regression.md)
- [Periodic Feature Network](./doc/guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md)
- [Residual Harmonic Network](./doc/guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md)

## Main Implemented Model Families

- `feedforward`
  Point-wise MLP baseline for TE regression.
- `harmonic_regression`
  Structured harmonic baseline with explicit periodic bias.
- `periodic_mlp`
  Hybrid model combining periodic features with neural regression.
- `residual_harmonic_mlp`
  Structured-plus-residual decomposition for TE prediction.
- `tree`
  Tabular baselines for honest comparison against neural approaches.

## Output And Reproducibility

The repository separates artifacts by workflow type instead of mixing everything
into one flat output root.

Important locations:

- `output/training_runs/`
- `output/validation_checks/`
- `output/smoke_tests/`
- `output/training_campaigns/`
- `output/registries/families/`
- `output/registries/program/`

This keeps run identity, campaign outcomes, and best-result tracking explicit
and inspectable.

## Project Notes

- The canonical user-facing documentation lives in `doc/`, not in `reference/`.
- `reference/` is intentionally kept out of the main maintenance workflow.
- The GitHub-facing README redesign rationale is documented in
  [2026-03-25-14-31-40_readme_github_landing_page_redesign.md](./doc/technical/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md).
- The README maintenance rule rationale is documented in
  [2026-03-25-14-51-40_readme_maintenance_rule.md](./doc/technical/2026-03-25/2026-03-25-14-51-40_readme_maintenance_rule.md).
- The MD034 bare-URL cleanup scope is documented in
  [2026-03-26-16-23-32_markdown_md034_no_bare_urls_cleanup.md](./doc/technical/2026-03-26/2026-03-26-16-23-32_markdown_md034_no_bare_urls_cleanup.md).
- The Sphinx portal root rename rationale is documented in
  [2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md](./doc/technical/2026-03-25/2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md).
- The dual `NotebookLM` video-package strategy rationale is documented in
  [2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md](./doc/technical/2026-03-25/2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md).
- The future guide-bundle and `NotebookLM` prompt rule rationale is documented in
  [2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md](./doc/technical/2026-03-25/2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md).
- The concept-export integration rationale for the three new `NotebookLM` bundles is documented in
  [2026-03-25-17-30-31_integrate_concept_notebooklm_exports_for_three_guides.md](./doc/technical/2026-03-25/2026-03-25-17-30-31_integrate_concept_notebooklm_exports_for_three_guides.md).
- The Wave 1 recovery campaign PDF layout refinement rationale is documented in
  [2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md](./doc/technical/2026-03-26/2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md).
- The Wave 1 familywise hyperparameter-optimization campaign rationale is documented in
  [2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md](./doc/technical/2026-03-26/2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md).
- The mandatory campaign-launcher script rationale is documented in
  [2026-03-26-14-19-56_campaign_launcher_script_mandatory_rule.md](./doc/technical/2026-03-26/2026-03-26-14-19-56_campaign_launcher_script_mandatory_rule.md).
- The post-campaign wave-naming alignment reminder is documented in
  [2026-03-26-15-18-40_post_campaign_wave_naming_and_backlog_alignment_reminder.md](./doc/technical/2026-03-26/2026-03-26-15-18-40_post_campaign_wave_naming_and_backlog_alignment_reminder.md).
- The Wave 1 wave-naming and backlog-alignment cleanup plan is documented in
  [2026-03-27-10-49-23_wave1_wave_naming_and_backlog_alignment_cleanup.md](./doc/technical/2026-03-27/2026-03-27-10-49-23_wave1_wave_naming_and_backlog_alignment_cleanup.md).
- The Wave 1 residual-harmonic family campaign results-report plan is documented in
  [2026-03-27-11-49-15_wave1_residual_harmonic_family_campaign_results_report.md](./doc/technical/2026-03-27/2026-03-27-11-49-15_wave1_residual_harmonic_family_campaign_results_report.md).
- The Wave 1 residual campaign results PDF layout refinement is documented in
  [2026-03-27-12-03-20_wave1_residual_campaign_results_pdf_table_rebalance_and_page_breaks.md](./doc/technical/2026-03-27/2026-03-27-12-03-20_wave1_residual_campaign_results_pdf_table_rebalance_and_page_breaks.md).
- The TwinCAT ML export and TestRig reference-analysis rationale is documented in
  [2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md](./doc/technical/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md).
- The post-campaign TwinCAT deployment-evaluation and isolated parallel-track rationale is documented in
  [2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md](./doc/technical/2026-03-26/2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md).
- The backlog and documentation integration rationale for the approved TwinCAT deployment tracks is documented in
  [2026-03-27-12-24-15_backlog_and_documentation_integration_for_twincat_deployment_tracks.md](./doc/technical/2026-03-27/2026-03-27-12-24-15_backlog_and_documentation_integration_for_twincat_deployment_tracks.md).
- The README `MD012` final-check rule is documented in
  [2026-03-27-12-44-18_readme_md012_final_check_rule.md](./doc/technical/2026-03-27/2026-03-27-12-44-18_readme_md012_final_check_rule.md).
- The Markdown warning final-check rule for created and modified documents is documented in
  [2026-03-27-12-45-14_markdown_warning_final_check_rule_for_created_and_modified_docs.md](./doc/technical/2026-03-27/2026-03-27-12-45-14_markdown_warning_final_check_rule_for_created_and_modified_docs.md).
- The repository-owned archive plan for project-video `NotebookLM` prompts across the current guide tree is documented in
  [2026-03-27-13-11-51_archive_project_notebooklm_video_prompts_for_all_guides.md](./doc/technical/2026-03-27/2026-03-27-13-11-51_archive_project_notebooklm_video_prompts_for_all_guides.md).
- The guide-local archive plan for concept-video `NotebookLM` prompts across the current guide tree is documented in
  [2026-03-27-13-57-37_archive_concept_notebooklm_video_prompts_into_guide_local_packages.md](./doc/technical/2026-03-27/2026-03-27-13-57-37_archive_concept_notebooklm_video_prompts_into_guide_local_packages.md).
- The language-aware guide-export reorganization plan for Italian and English `NotebookLM` media is documented in
  [2026-03-27-14-07-14_guide_language_split_for_notebooklm_exports.md](./doc/technical/2026-03-27/2026-03-27-14-07-14_guide_language_split_for_notebooklm_exports.md).
- The TwinCAT video-guides knowledge-extraction pipeline rationale is documented in
  [2026-03-30-12-30-07_twincat_video_guides_knowledge_extraction_pipeline.md](./doc/technical/2026-03-30/2026-03-30-12-30-07_twincat_video_guides_knowledge_extraction_pipeline.md).
- The Tesseract OCR and full per-video report extension for TwinCAT guides is documented in
  [2026-03-30-13-05-35_tesseract_ocr_and_full_video_reports_for_twincat_guides.md](./doc/technical/2026-03-30/2026-03-30-13-05-35_tesseract_ocr_and_full_video_reports_for_twincat_guides.md).
- The transcript and OCR quality rework plan for TwinCAT video guides is documented in
  [2026-03-30-14-46-25_twincat_video_guides_transcript_and_ocr_quality_rework.md](./doc/technical/2026-03-30/2026-03-30-14-46-25_twincat_video_guides_transcript_and_ocr_quality_rework.md).
- The three-stage high-quality video knowledge-extraction workflow plan is documented in
  [2026-03-30-18-02-12_three_stage_high_quality_video_knowledge_extraction_workflow.md](./doc/technical/2026-03-30/2026-03-30-18-02-12_three_stage_high_quality_video_knowledge_extraction_workflow.md).
- The Google GenAI adaptation plan for the three-stage video knowledge-extraction workflow is documented in
  [2026-03-30-19-49-34_google_genai_adaptation_for_three_stage_video_knowledge_extraction.md](./doc/technical/2026-03-30/2026-03-30-19-49-34_google_genai_adaptation_for_three_stage_video_knowledge_extraction.md).
- The local/LAN AI inference and transcription architecture-report plan is documented in
  [2026-03-30-21-48-58_local_lan_ai_inference_and_transcription_architecture_report.md](./doc/technical/2026-03-30/2026-03-30-21-48-58_local_lan_ai_inference_and_transcription_architecture_report.md).
- The LM Studio-based LAN AI node plan for video knowledge extraction is documented in
  [2026-03-30-22-01-25_lm_studio_lan_ai_node_for_video_knowledge_extraction.md](./doc/technical/2026-03-30/2026-03-30-22-01-25_lm_studio_lan_ai_node_for_video_knowledge_extraction.md).
- The Windows Sphinx compatibility fix for the `colorama` lower bound is documented in
  [2026-03-30-23-33-16_colorama_lower_bound_fix_for_windows_sphinx_compatibility.md](./doc/technical/2026-03-30/2026-03-30-23-33-16_colorama_lower_bound_fix_for_windows_sphinx_compatibility.md).
- The clean-install dependency-resolution fix for the Windows documentation stack is documented in
  [2026-03-30-23-39-04_requirements_resolution_fix_for_windows_clean_installs.md](./doc/technical/2026-03-30/2026-03-30-23-39-04_requirements_resolution_fix_for_windows_clean_installs.md).
- The LAN AI server setup-guide expansion plan is documented in
  [2026-03-31-09-54-32_lan_ai_server_setup_guide_expansion.md](./doc/technical/2026-03-31/2026-03-31-09-54-32_lan_ai_server_setup_guide_expansion.md).
- The `Machine_Learning_1` TwinCAT video filename-correction plan is documented in
  [2026-03-31-10-16-16_machine_learning_1_video_filename_correction.md](./doc/technical/2026-03-31/2026-03-31-10-16-16_machine_learning_1_video_filename_correction.md).
- The requirements-cleanup plan for unused repository dependencies is documented in
  [2026-03-31-10-36-56_requirements_cleanup_for_unused_repository_dependencies.md](./doc/technical/2026-03-31/2026-03-31-10-36-56_requirements_cleanup_for_unused_repository_dependencies.md).
- The SSH key-based access extension for the LAN AI node guide is documented in
  [2026-03-31-12-30-02_ssh_key_based_access_extension_for_lan_ai_node_guide.md](./doc/technical/2026-03-31/2026-03-31-12-30-02_ssh_key_based_access_extension_for_lan_ai_node_guide.md).
- The English project-export integration plan for the existing guide tree is documented in
  [2026-03-28-11-53-52_integrate_english_project_notebooklm_exports_for_existing_guides.md](./doc/technical/2026-03-28/2026-03-28-11-53-52_integrate_english_project_notebooklm_exports_for_existing_guides.md).
- The Codex skill-autonomy and subagent-approval rule is documented in
  [2026-03-27-17-44-33_codex_skill_autonomy_and_subagent_approval_rule.md](./doc/technical/2026-03-27/2026-03-27-17-44-33_codex_skill_autonomy_and_subagent_approval_rule.md).
- The additional Codex skills and subagents plan for ML, testing, reports, and commit workflows is documented in
  [2026-03-27-17-48-41_additional_codex_skills_and_subagents_for_ml_testing_reports_and_commit_workflows.md](./doc/technical/2026-03-27/2026-03-27-17-48-41_additional_codex_skills_and_subagents_for_ml_testing_reports_and_commit_workflows.md).
- The project-status report, presentation, and NotebookLM source-bundle plan is documented in
  [2026-03-27-18-09-50_project_status_report_presentation_and_notebooklm_source_bundle.md](./doc/technical/2026-03-27/2026-03-27-18-09-50_project_status_report_presentation_and_notebooklm_source_bundle.md).
- The project-status report PDF section page-break adjustment plan is documented in
  [2026-03-27-19-05-09_project_status_report_pdf_section_page_break_adjustment.md](./doc/technical/2026-03-27/2026-03-27-19-05-09_project_status_report_pdf_section_page_break_adjustment.md).
- The project-status report plan for removing the forced new page before the gaps section is documented in
  [2026-03-27-19-13-28_project_status_report_remove_gap_section_forced_page_break.md](./doc/technical/2026-03-27/2026-03-27-19-13-28_project_status_report_remove_gap_section_forced_page_break.md).
- The project-status report plan for moving the forced new page from the conclusion to the roadmap section is documented in
  [2026-03-27-19-20-37_project_status_report_move_forced_page_break_from_conclusion_to_roadmap.md](./doc/technical/2026-03-27/2026-03-27-19-20-37_project_status_report_move_forced_page_break_from_conclusion_to_roadmap.md).
- The project-status presentation `.pptx` and slide-PDF pipeline rationale is documented in
  [2026-03-27-19-38-55_project_status_presentation_pptx_and_slide_pdf_pipeline.md](./doc/technical/2026-03-27/2026-03-27-19-38-55_project_status_presentation_pptx_and_slide_pdf_pipeline.md).
- The approved `English/` subfolder layout for guide-local English exports is documented in
  [2026-03-27-14-16-10_english_subfolder_layout_for_guide_exports.md](./doc/technical/2026-03-27/2026-03-27-14-16-10_english_subfolder_layout_for_guide_exports.md).
- The guide-package relocation plan for moving `concept_video_package` and `project_video_package` under `assets/` is documented in
  [2026-03-27-14-35-13_move_guide_video_packages_under_assets.md](./doc/technical/2026-03-27/2026-03-27-14-35-13_move_guide_video_packages_under_assets.md).
- The cleanup plan for removing guide-local `English/README.md` files is documented in
  [2026-03-27-14-41-40_remove_english_folder_readme_files.md](./doc/technical/2026-03-27/2026-03-27-14-41-40_remove_english_folder_readme_files.md).
- The documentation realignment plan for the current `Italiano/` plus `English/` guide layout is documented in
  [2026-03-27-16-40-02_realign_guide_documentation_to_italiano_and_english_layout.md](./doc/technical/2026-03-27/2026-03-27-16-40-02_realign_guide_documentation_to_italiano_and_english_layout.md).
- The Codex-native skills and subagents customization scope is documented in
  [2026-03-26-16-38-28_codex_native_skills_and_subagents_for_ml_documentation_and_campaign_workflows.md](./doc/technical/2026-03-26/2026-03-26-16-38-28_codex_native_skills_and_subagents_for_ml_documentation_and_campaign_workflows.md).
- The concept NotebookLM export integration scope for FeedForward, Harmonic, and Periodic guides is documented in
  [2026-03-26-17-22-54_integrate_concept_notebooklm_exports_for_feedforward_harmonic_and_periodic_guides.md](./doc/technical/2026-03-26/2026-03-26-17-22-54_integrate_concept_notebooklm_exports_for_feedforward_harmonic_and_periodic_guides.md).
- The concept NotebookLM export integration scope for Multilayer and Residual guides is documented in
  [2026-03-26-18-14-50_integrate_concept_notebooklm_exports_for_multilayer_and_residual_guides.md](./doc/technical/2026-03-26/2026-03-26-18-14-50_integrate_concept_notebooklm_exports_for_multilayer_and_residual_guides.md).
- The concept-video command archive and reuse-template rationale is documented in
  [2026-03-27-12-50-37_concept_video_package_command_archive_and_reuse_template.md](./doc/technical/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive_and_reuse_template.md).
- The canonical concept-video command archive is documented in
  [2026-03-27-12-50-37_concept_video_package_command_archive.md](./doc/technical/2026-03-27/2026-03-27-12-50-37_concept_video_package_command_archive.md).
- The editor-side Markdown ignore plan for the `.tools/` directory is documented in
  [2026-03-27-12-58-39_editor_markdown_ignore_for_tools_directory.md](./doc/technical/2026-03-27/2026-03-27-12-58-39_editor_markdown_ignore_for_tools_directory.md).
- The Markdown final blank-line check rule is documented in
  [2026-03-27-13-03-50_markdown_final_blank_line_check_rule.md](./doc/technical/2026-03-27/2026-03-27-13-03-50_markdown_final_blank_line_check_rule.md).
- The presentation-export workflow skill plan is documented in
  [2026-03-28-11-26-06_presentation_export_workflows_skill.md](./doc/technical/2026-03-28/2026-03-28-11-26-06_presentation_export_workflows_skill.md).
- The XiLab Research template integration plan for the presentation pipeline and skill is documented in
  [2026-03-28-11-31-25_xilab_research_template_integration_for_presentation_pipeline_and_skill.md](./doc/technical/2026-03-28/2026-03-28-11-31-25_xilab_research_template_integration_for_presentation_pipeline_and_skill.md).
- The Italian project-export integration plan for the `Multilayer Perceptrons` guide is documented in
  [2026-03-28-12-03-04_integrate_italian_project_notebooklm_exports_for_multilayer_perceptrons.md](./doc/technical/2026-03-28/2026-03-28-12-03-04_integrate_italian_project_notebooklm_exports_for_multilayer_perceptrons.md).
- The NotebookLM project-status presentation and video export integration plan is documented in
  [2026-03-28-12-06-26_integrate_notebooklm_project_status_presentation_and_video_exports.md](./doc/technical/2026-03-28/2026-03-28-12-06-26_integrate_notebooklm_project_status_presentation_and_video_exports.md).
- The documentation realignment plan for the project-status `notebook_lm_assets` layout is documented in
  [2026-03-28-12-11-07_realign_project_status_notebooklm_documentation_to_notebook_lm_assets_layout.md](./doc/technical/2026-03-28/2026-03-28-12-11-07_realign_project_status_notebooklm_documentation_to_notebook_lm_assets_layout.md).
- The validation-setup report export plan for the skill operational test is documented in
  [2026-03-30-10-30-15_validation_setup_report_export_for_skill_operational_test.md](./doc/technical/2026-03-30/2026-03-30-10-30-15_validation_setup_report_export_for_skill_operational_test.md).
- The validation-setup report PDF export regression plan is documented in
  [2026-03-30-10-57-14_validation_setup_report_pdf_export_regression_in_report_pipeline.md](./doc/technical/2026-03-30/2026-03-30-10-57-14_validation_setup_report_pdf_export_regression_in_report_pipeline.md).
- The second operational-test wave for the remaining Codex skills and
  subagents is documented in
  [2026-03-30-11-04-41_skill_and_subagent_operational_test_wave_two.md](./doc/technical/2026-03-30/2026-03-30-11-04-41_skill_and_subagent_operational_test_wave_two.md).
- The TwinCAT export-preparation skill and campaign-package reviewer subagent
  plan is documented in
  [2026-03-30-11-17-58_twincat_export_preparation_skill_and_campaign_package_reviewer_subagent.md](./doc/technical/2026-03-30/2026-03-30-11-17-58_twincat_export_preparation_skill_and_campaign_package_reviewer_subagent.md).
- The Codex repo-local user-guide plan is documented in
  [2026-03-30-11-23-21_codex_repo_local_user_guide.md](./doc/technical/2026-03-30/2026-03-30-11-23-21_codex_repo_local_user_guide.md).
- The Wave 1 closeout audit and consolidated summary-report plan is documented in
  [2026-03-30-11-41-57_wave1_closeout_audit_and_summary_report.md](./doc/technical/2026-03-30/2026-03-30-11-41-57_wave1_closeout_audit_and_summary_report.md).
- The `doc/reports/` reorganization alignment and naming-rule plan is documented in
  [2026-03-30-12-03-06_doc_reports_reorganization_alignment_and_naming_rule.md](./doc/technical/2026-03-30/2026-03-30-12-03-06_doc_reports_reorganization_alignment_and_naming_rule.md).
- The `doc/reports/` topic-root and readable-filename rule is documented in
  [2026-03-30-12-04-47_doc_reports_topic_root_and_readable_filename_rule.md](./doc/technical/2026-03-30/2026-03-30-12-04-47_doc_reports_topic_root_and_readable_filename_rule.md).
- The `AGENTS.md` rule integration plan for the new `doc/reports/` structure is documented in
  [2026-03-30-12-14-42_agentes_rule_for_doc_reports_topic_root_and_readable_filenames.md](./doc/technical/2026-03-30/2026-03-30-12-14-42_agentes_rule_for_doc_reports_topic_root_and_readable_filenames.md).

## Next Steps

The near-term direction of the repository is to strengthen structured TE
baselines, keep the training/reporting workflow reliable, and progressively move
toward richer hybrid and eventually physics-informed models once the formulation
is technically justified.
