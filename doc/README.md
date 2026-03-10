# Project Documentation Index

This folder contains the internal project documents derived from the reference PDFs and from the reference codebases used to define the coding style of this repository.

## Available Documents

- [01_Dataset_Operations_Guide.md](./01_Dataset_Operations_Guide.md)
  Dataset sources, practical references, and operational guidance.
- [02_MMT_TEModeling_Project_Summary.md](./02_MMT_TEModeling_Project_Summary.md)
  Analytical TE modeling through equivalent mechanism and loop incremental method.
- [03_RCIM_ML_Compensation_Project_Summary.md](./03_RCIM_ML_Compensation_Project_Summary.md)
  ML-driven TE prediction and online PLC/TwinCAT compensation strategy.
- [04_Machine_Learning_Report_Project_Summary.md](./04_Machine_Learning_Report_Project_Summary.md)
  Test-rig workflow, harmonic analysis, TwinCAT integration, and practical implementation notes.
- [05_Data_Series_Explanation_Project_Summary.md](./05_Data_Series_Explanation_Project_Summary.md)
  Meaning of the measured variables, zeroing procedure, and `DataValid` logic.
- [06_Programming_Style_Guide.md](./06_Programming_Style_Guide.md)
  Coding style mapped from `blind_handover_controller`, `mediapipe_gesture_recognition`, and `multimodal_fusion`.
- [2026-03-10-02-21-36-pytorch_lightning_environment_setup.md](./2026-03-10-02-21-36-pytorch_lightning_environment_setup.md)
  Technical document for the Conda, PyTorch, and PyTorch Lightning environment baseline.
- [2026-03-10-02-49-17_dataset_processing_pipeline.md](./2026-03-10-02-49-17_dataset_processing_pipeline.md)
  Technical document for the validated TE dataset-processing pipeline and raw-data reconstruction path.
- [2026-03-10-03-04-57_script_config_documentation_structure.md](./2026-03-10-03-04-57_script_config_documentation_structure.md)
  Technical document for the `scripts/`, `config/`, and per-script documentation repository rules.
- [scripts_datasets_transmission_error_dataset.md](./scripts_datasets_transmission_error_dataset.md)
  Script-level documentation for the TE dataset parser, PyTorch dataset, and dataloader utilities.
- [scripts_datasets_visualize_transmission_error.md](./scripts_datasets_visualize_transmission_error.md)
  Script-level documentation for the TE curve visualization utility.

## Usage

- Use these documents as the working baseline for dataset interpretation, TE modeling, ML compensation, and code implementation choices.
- Treat `06_Programming_Style_Guide.md` as the style reference for new code written in this repository.
- Keep this index updated whenever new project documents are added.
