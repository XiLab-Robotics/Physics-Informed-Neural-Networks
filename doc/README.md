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

- [technical/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md](./technical/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md)
  Technical document for the Conda, PyTorch, and PyTorch Lightning environment baseline.
- [technical/2026-03-10-02-49-17_dataset_processing_pipeline.md](./technical/2026-03-10-02-49-17_dataset_processing_pipeline.md)
  Technical document for the validated TE dataset-processing pipeline and raw-data reconstruction path.
- [technical/2026-03-10-03-04-57_script_config_documentation_structure.md](./technical/2026-03-10-03-04-57_script_config_documentation_structure.md)
  Technical document for the `scripts/`, `config/`, and per-script documentation repository rules.
- [technical/2026-03-10-03-16-44_doc_folder_reorganization.md](./technical/2026-03-10-03-16-44_doc_folder_reorganization.md)
  Technical document for the grouped `doc/` folder reorganization.
- [technical/2026-03-10-15-13-29_agent_submodule_reorganization.md](./technical/2026-03-10-15-13-29_agent_submodule_reorganization.md)
  Technical document for moving the existing agent submodule and adding the requested `agents/` submodule collection.
- [technical/2026-03-10-15-25-39_commit_workflow_rule_update.md](./technical/2026-03-10-15-25-39_commit_workflow_rule_update.md)
  Technical document for enforcing the technical-document approval workflow plus a mandatory final Git commit.
- [technical/2026-03-10-15-33-05_reference_code_submodule_migration.md](./technical/2026-03-10-15-33-05_reference_code_submodule_migration.md)
  Technical document for replacing the archived reference code `.zip` files in `reference/codes/` with Git submodules.
- [technical/2026-03-10-15-58-05_reference_code_style_reference_docs.md](./technical/2026-03-10-15-58-05_reference_code_style_reference_docs.md)
  Technical document for creating persistent `doc/reference_codes/` notes from the reference-code submodules.

### Script Documentation

- [scripts/datasets/transmission_error_dataset.md](./scripts/datasets/transmission_error_dataset.md)
  Script-level documentation for the TE dataset parser, PyTorch dataset, and dataloader utilities.
- [scripts/datasets/visualize_transmission_error.md](./scripts/datasets/visualize_transmission_error.md)
  Script-level documentation for the TE curve visualization utility.

### Guides

- [guide/project_usage_guide.md](./guide/project_usage_guide.md)
  Practical user guide for environment activation, dataset processing, and TE visualization.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `reference_summaries/06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Use `reference_codes/` when a future implementation task needs repository-specific examples instead of only high-level style rules.
- Keep this index updated whenever new project documents are added.
