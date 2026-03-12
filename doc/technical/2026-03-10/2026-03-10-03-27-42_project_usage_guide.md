# Project Usage Guide

## Overview

This document defines a user-facing guide to explain how to use the current project scripts from setup to dataset processing and visualization.

The guide will be stored under:

- `doc/guide/`

The requested content includes:

- how to process the dataset;
- how to visualize the processed dataset;
- how to train the model;
- how to run inference;
- command examples and step-by-step explanations.

Important scope constraint recorded on March 10, 2026:

- the current repository implements dataset-processing and visualization scripts only;
- no training script, Lightning training entry point, or inference script is currently present in `scripts/`.

Therefore the guide must distinguish clearly between:

1. currently available workflows;
2. planned workflows that are not implemented yet.

## Technical Approach

The guide will be structured as a practical operational document rather than a design document.

Planned sections:

1. Environment Preparation
   - Conda environment activation
   - dependency installation recap

2. Repository Structure Relevant To Usage
   - `scripts/`
   - `config/`
   - `data/datasets/`
   - `doc/`

3. Dataset Processing Workflow
   - explain dataset config file
   - explain how the validated TE dataset is loaded
   - explain how to instantiate dataloaders from Python

4. Dataset Visualization Workflow
   - explain visualization config
   - provide command-line examples
   - explain output behavior with and without `--save-path`

5. Current Project Limitations
   - state explicitly that training and inference entry points are not yet implemented
   - explain what is already ready for the next step

6. Planned Next Steps
   - LightningDataModule
   - training script
   - inference/export utilities

The guide must avoid claiming that training or inference can be executed if the corresponding scripts do not yet exist.

## Involved Components

- `doc/guide/`
  New folder that will contain user-facing usage guides.

- `doc/guide/project_usage_guide.md`
  Main operational guide for the current project workflows.

- `scripts/datasets/transmission_error_dataset.py`
  Dataset processing entry point described in the guide.

- `scripts/datasets/visualize_transmission_error.py`
  Visualization entry point described in the guide.

- `config/dataset_processing.yaml`
  Dataset-processing configuration described in the guide.

- `config/visualization.yaml`
  Visualization configuration described in the guide.

- `README.md`
  Main project document that should reference the new guide.

- `doc/README.md`
  Documentation index that should reference the new guide.

## Implementation Steps

1. Create the technical document for the guide.
2. Create `doc/guide/` and add the project usage guide markdown file.
3. Document the currently available dataset-processing workflow with Python examples and command-line examples.
4. Document the visualization workflow with YAML references and command-line examples.
5. Add an explicit section clarifying that training and inference scripts are not implemented yet.
6. Update `README.md` and `doc/README.md` to reference the new guide.
