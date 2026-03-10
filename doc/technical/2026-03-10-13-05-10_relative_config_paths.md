# Relative Config Paths

## Overview

This document defines the migration from absolute filesystem paths to project-root-relative paths inside the YAML configuration files.

The requested change is:

- `config/dataset_processing.yaml`
  must store `dataset_root` as a path relative to the repository root;

- `config/visualization.yaml`
  must store `dataset_config_path` as a path relative to the repository root.

The code must also be updated so that these relative config values are resolved correctly from the project root rather than from the current working directory.

## Technical Approach

The repository already has a stable project-root reference in the dataset scripts.

The implementation will:

1. replace absolute paths in YAML files with repository-root-relative paths;
2. add explicit helper logic in the Python scripts to resolve config paths against `PROJECT_PATH`;
3. keep support for absolute paths when provided intentionally in the future;
4. update documentation examples so they show relative YAML paths instead of machine-specific absolute paths.

Planned config changes:

- `config/dataset_processing.yaml`
  - `paths.dataset_root: data/datasets`

- `config/visualization.yaml`
  - `paths.dataset_config_path: config/dataset_processing.yaml`

Planned code behavior:

- if a config path is already absolute, use it as-is;
- if a config path is relative, join it with the repository root and then resolve it.

This keeps the configuration portable across machines and repository clones.

## Involved Components

- `config/dataset_processing.yaml`
  Dataset root configuration to convert to project-relative form.

- `config/visualization.yaml`
  Dataset-config pointer to convert to project-relative form.

- `scripts/datasets/transmission_error_dataset.py`
  Dataset config path resolution to update.

- `scripts/datasets/visualize_transmission_error.py`
  Visualization config path resolution to update.

- `doc/guide/project_usage_guide.md`
  Usage guide examples to update.

- `README.md`
  Main project document index already tracking this technical document.

## Implementation Steps

1. Convert YAML config paths to repository-root-relative values.
2. Add helper resolution logic for relative and absolute config values.
3. Update the dataset-processing script to resolve `dataset_root` from project root.
4. Update the visualization script to resolve `dataset_config_path` from project root.
5. Update the guide examples and explanations to use the new relative paths.
6. Verify dataloader creation and visualization with the updated configs.
