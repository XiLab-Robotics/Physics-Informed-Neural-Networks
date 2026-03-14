# Repository Code Layout Reorganization And Agent Reference Migration

## Overview

This document defines a repository reorganization requested to reduce the current top-level folder sprawl and make future growth clearer.

The current authored Python code is split across:

- `scripts/` for dataset and report utilities;
- `models/` for neural-network definitions;
- `training/` for training entry points and Lightning modules.

This layout is still manageable, but it scales poorly because every new workflow risks creating another top-level folder such as `testing/`, `evaluation/`, `inference/`, or `export/`.

The request also includes moving the external agent collections from the current top-level `agents/` folder into `reference/agents/`, with the Git submodule paths migrated accordingly.

The goal is therefore twofold:

1. define a sustainable repository layout for project-authored code;
2. move the external agent references under `reference/agents/` so they live with the other external reference material.

## Technical Approach

### Current Problems

The present layout mixes two different concerns:

- reusable Python modules imported by other project files;
- command-line entry points used as operational scripts.

This causes three structural issues:

1. top-level growth is driven by execution mode instead of domain ownership;
2. imports expose implementation placement decisions such as `scripts.datasets...`;
3. adding a new workflow implies a new top-level namespace instead of extending a coherent internal package.

### Evaluated Layout Options

#### Option A - Keep The Current Root Split And Add More Top-Level Folders

Example direction:

```text
scripts/
models/
training/
testing/
evaluation/
```

Advantages:

- minimal migration effort;
- almost no import churn for the current files;
- easy to understand in the very short term.

Limitations:

- root-level clutter keeps growing;
- the distinction between library code and executable entry points remains blurry;
- future workflows such as inference/export/report validation continue to fragment the repository.

This option is not recommended except for a strictly minimal reorganization.

#### Option B - Group By Functional Area At Root

Example direction:

```text
data_processing/
models/
training/
evaluation/
reporting/
```

Advantages:

- slightly clearer than the current `scripts/` bucket;
- explicit naming for testing/evaluation/reporting.

Limitations:

- still creates one top-level folder per workflow family;
- still mixes importable code and runnable entry points;
- does not solve long-term namespace growth.

This option is clearer than the current state but still not the best long-term structure.

#### Option C - Introduce One Internal Package Plus Thin CLI Folders

Example direction:

```text
src/
  standard_ml/
    datasets/
    models/
    training/
    evaluation/
    reports/
    utils/
tools/
  datasets/
  training/
  evaluation/
  reports/
```

Advantages:

- one stable home for project-authored Python code;
- execution entry points are separated from reusable modules;
- future workflows extend the internal package instead of creating new root folders;
- imports become domain-oriented, for example `standard_ml.datasets...`;
- test and evaluation utilities can be added under `tools/` without changing the core layout model.

Limitations:

- largest migration effort;
- requires updating imports, path-resolution helpers, and user-facing commands;
- should be executed carefully because training and dataset scripts currently use direct file execution patterns.

This is the recommended option because it solves the structural problem instead of only renaming folders.

### Recommended Final Direction

The recommended target is Option C with a repository-specific package name:

```text
src/
  standard_ml/
    datasets/
      transmission_error_dataset.py
    models/
      feedforward_network.py
      model_factory.py
    training/
      transmission_error_datamodule.py
      transmission_error_regression_module.py
    reports/
      generate_styled_report_pdf.py
      validate_report_pdf.py
    utils/
tools/
  datasets/
    visualize_transmission_error.py
  training/
    train_feedforward_network.py
    run_training_campaign.py
reference/
  agents/
    claude-code-agents/
    claude-code-subagents/
    awesome-claude-code-subagents/
    wshobson-agents/
```

Design rules behind this recommendation:

- reusable code belongs in `src/standard_ml/`;
- user-invoked scripts stay thin and live in `tools/`;
- new workflows such as testing or evaluation become `tools/testing/` or `tools/evaluation/`, not new core roots;
- external reference repositories belong under `reference/agents/`, aligned with `reference/codes/`.

### Migration Scope

The current code already shows the expected update surface:

- imports from `scripts.datasets...`;
- imports from `models...`;
- imports from `training...`;
- direct `PROJECT_PATH` derivation from file location;
- documentation and setup notes that still refer to top-level `agents/`.

The migration should therefore be handled in two layers:

1. move files into the new package and CLI layout;
2. update imports and path resolution so direct execution still works from the repository root.

### Path Strategy

To keep execution reliable after the migration:

- package modules should resolve the project root from `Path(__file__).resolve()` relative to `src/standard_ml/...`;
- thin CLI scripts under `tools/` should inject the repository root into `sys.path` only when needed for direct execution;
- all default config paths should continue to be rooted at the repository-level `config/` folder;
- all documented commands should be updated to the new entry-point paths.

### Agent Submodule Migration

The external agent repositories are references, not project runtime code.

For that reason, the requested move to `reference/agents/` is structurally sound and should be executed regardless of the chosen authored-code layout.

This requires:

- moving the working-tree directories from `agents/*` to `reference/agents/*`;
- updating `.gitmodules` paths;
- verifying Git submodule metadata and status after the move;
- updating README references that currently describe `agents/` as a top-level folder.

## Involved Components

- `README.md`
  Main project document that must reference this technical document and reflect the approved repository layout.
- `doc/README.md`
  Internal documentation index that should also be updated after approval for consistency.
- `.gitmodules`
  Git submodule metadata that must be updated for the `reference/agents/` migration.
- `agents/`
  Current top-level location of the external agent submodules to be moved.
- `reference/agents/`
  Requested new location of the external agent submodules.
- `scripts/datasets/transmission_error_dataset.py`
  Current dataset-processing library module used by training code.
- `scripts/datasets/visualize_transmission_error.py`
  Current dataset visualization CLI-oriented script.
- `scripts/reports/generate_styled_report_pdf.py`
  Current report-generation utility that should move into the internal package.
- `scripts/reports/validate_report_pdf.py`
  Current report-validation utility that should move into the internal package.
- `models/feedforward_network.py`
  Current model definition module.
- `models/model_factory.py`
  Current model-dispatch module.
- `training/train_feedforward_network.py`
  Current training entry point that should become a thin CLI wrapper.
- `training/run_training_campaign.py`
  Current campaign runner that should become a thin CLI wrapper.
- `training/transmission_error_datamodule.py`
  Current Lightning data module.
- `training/transmission_error_regression_module.py`
  Current Lightning module.
- `config/`
  Repository-level configuration root whose paths must remain stable.
- `doc/guide/project_usage_guide.md`
  Must be updated after approval because runnable commands and repository navigation will change.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before changing any implementation code or repository structure.
3. After approval, create the new `src/standard_ml/` package and `tools/` CLI folders.
4. Move reusable modules from `scripts/`, `models/`, and `training/` into the package domains:
   - `datasets/`
   - `models/`
   - `training/`
   - `reports/`
   - `utils/` if needed during cleanup.
5. Convert `train_feedforward_network.py`, `run_training_campaign.py`, and `visualize_transmission_error.py` into thin command-line entry points under `tools/`.
6. Update imports and path-resolution helpers so all default config and output paths still resolve from the repository root.
7. Move the external agent submodules from `agents/` to `reference/agents/` and update `.gitmodules` accordingly.
8. Update repository documentation, especially `README.md`, `doc/README.md`, and `doc/guide/project_usage_guide.md`, so the new layout and commands are explicit.
9. Verify the migration with directory inspection, `rg` path checks, direct script smoke tests, and `git status`.
