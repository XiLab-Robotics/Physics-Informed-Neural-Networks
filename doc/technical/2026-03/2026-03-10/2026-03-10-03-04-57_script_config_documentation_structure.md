# Script, Config, And Documentation Structure

## Overview

This document defines the repository rules for Python script organization, configuration management, and per-script documentation.

The requested structural rules are:

- all Python modules must live under a top-level `scripts/` folder;
- Python code must be organized in explicit subfolders such as `scripts/utils/`, `scripts/datasets/`, and similar task-oriented groups;
- all script configuration files must live under a top-level `config/` folder;
- configuration files must store paths, hyperparameters, switches, and runtime variables;
- every new Python script must have a dedicated `.md` documentation file explaining:
  - what the script does;
  - what it is used for;
  - the detailed role of its functions and classes.

This document also covers the migration of the dataset-processing utilities already created in `data/` during the previous step of the project.

## Technical Approach

The repository will adopt the following layout policy:

- `scripts/`
  Main root for all Python source code.

- `scripts/datasets/`
  Dataset parsing, processing, PyTorch dataset, and dataloader logic.

- `scripts/utils/`
  Generic helper utilities shared by multiple scripts.

- `config/`
  YAML configuration files for dataset paths, training settings, plotting options, and runtime parameters.

- `doc/`
  Technical project documents and script-level markdown documentation.

For the already implemented dataset-processing feature, the migration plan is:

1. move `data/transmission_error_dataset.py` into `scripts/datasets/`;
2. move `data/visualize_transmission_error.py` into `scripts/datasets/` or another suitable `scripts/` subfolder;
3. remove the temporary Python-module role from `data/`, keeping it as dataset storage only;
4. create one or more YAML files in `config/` for:
   - dataset root path;
   - train/validation split;
   - batch size;
   - direction selection;
   - plotting options;
5. create markdown documentation for every Python script involved in the dataset-processing pipeline.

Documentation policy for each script:

- one dedicated `.md` file per Python script;
- the markdown document must include:
  - script overview;
  - main purpose;
  - inputs and outputs;
  - detailed explanation of functions/classes;
  - expected usage pattern when useful.

## Involved Components

- `doc/technical/2026-03/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md`
  Technical rule document for repository script/config/documentation organization.

- `README.md`
  Main project index where this technical document must be referenced.

- `scripts/`
  New root for Python modules.

- `config/`
  New root for YAML configuration files.

- `doc/`
  Storage location for script-level markdown documentation files.

- `data/`
  Dataset storage folder only, without project Python modules after migration.

## Implementation Steps

1. Register this technical document in `README.md`.
2. Create the `scripts/` folder and the needed subfolders for the current dataset-processing task.
3. Create the `config/` folder and add YAML files for dataset and visualization settings.
4. Migrate the existing dataset-processing Python files from `data/` into the new `scripts/` structure.
5. Update imports and command-line entry points accordingly.
6. Add markdown documentation files for each migrated Python script.
7. Validate imports, dataloader creation, and visualization execution using the new paths.
