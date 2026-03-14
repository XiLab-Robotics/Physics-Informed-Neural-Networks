# Scripts Root Code Reorganization And Reference Agents Move

## Overview

This document defines the repository reorganization requested by the user.

The approved structural direction to implement is:

- move the external agent submodules from `agents/` to `reference/agents/`;
- move the authored source code currently under root `models/` into `scripts/models/`;
- move the authored source code currently under root `training/` into `scripts/training/`;
- reserve the root `models/` folder for trained and exported model artifacts instead of Python source files.

This keeps the repository root simpler:

- `reference/` contains external references, including agent collections;
- `scripts/` contains project-authored executable and importable Python code;
- `models/` becomes an artifact folder for produced model files.

The same approach also answers the future-growth question raised by the user: if new testing scripts are needed later, they should live under `scripts/testing/`, not as another unrelated top-level root folder.

## Technical Approach

### Target Structure

The requested target layout is:

```text
reference/
  agents/
    claude-code-agents/
    claude-code-subagents/
    awesome-claude-code-subagents/
    wshobson-agents/

scripts/
  datasets/
  reports/
  models/
  training/

models/
  checkpoints/
  exported/
```

The exact artifact subfolders under root `models/` can be refined during implementation, but the key rule is fixed:

- root `models/` is no longer Python source code;
- root `models/` stores trained, checkpointed, or exported model artifacts.

### Rationale

This direction is intentionally simple and consistent with the current repository habits.

It avoids introducing a new `src/` package while still solving the current confusion:

- all authored Python code lives under one umbrella, `scripts/`;
- external reusable references live under `reference/`;
- generated model outputs live under `models/`.

With this approach:

- dataset code remains in `scripts/datasets/`;
- report tooling remains in `scripts/reports/`;
- model definitions move to `scripts/models/`;
- training entry points and Lightning modules move to `scripts/training/`;
- future testing utilities can be added under `scripts/testing/`.

### Import And Path Updates

The current imports depend on the old root layout, for example:

- `from models.feedforward_network import ...`
- `from training.transmission_error_datamodule import ...`

After the migration, those imports must become:

- `from scripts.models.feedforward_network import ...`
- `from scripts.training.transmission_error_datamodule import ...`

The training entry points already bootstrap the repository root into `sys.path`, so direct execution from the repository root can remain supported after the import updates.

Path-sensitive code must also be checked where file location is used to resolve:

- project root;
- default config paths;
- output paths;
- report-generation paths.

### Agent Submodule Move

The requested `agents/` move is structurally aligned with the repository:

- `reference/codes/` already stores external code references;
- `reference/agents/` should store external agent workflow references.

This requires:

- moving the working-tree submodule directories;
- updating `.gitmodules` paths from `agents/...` to `reference/agents/...`;
- verifying submodule status after the move;
- updating documentation that currently refers to top-level `agents/`.

### Documentation Impact

Several documents currently describe the old layout, especially:

- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`

The migration will require command-path and structure updates so the documentation matches the new repository layout.

Historical technical and analysis documents that mention old paths can remain as historical records unless a direct correction is needed for active usage guidance.

## Involved Components

- `.gitmodules`
  Must be updated so the agent submodules point to `reference/agents/...`.
- `README.md`
  Must reflect the new root structure and the new role of `models/`.
- `doc/README.md`
  Should reference this technical document.
- `doc/guide/project_usage_guide.md`
  Must be updated after approval because runnable paths and repository navigation change.
- `agents/`
  Current top-level location of the external agent submodules to be moved.
- `reference/agents/`
  Requested new location for the external agent submodules.
- `models/feedforward_network.py`
  Current model-definition module to move into `scripts/models/`.
- `models/model_factory.py`
  Current model-factory module to move into `scripts/models/`.
- `training/train_feedforward_network.py`
  Current training entry point to move into `scripts/training/`.
- `training/run_training_campaign.py`
  Current campaign runner to move into `scripts/training/`.
- `training/transmission_error_datamodule.py`
  Current Lightning data module to move into `scripts/training/`.
- `training/transmission_error_regression_module.py`
  Current Lightning module to move into `scripts/training/`.
- `scripts/datasets/transmission_error_dataset.py`
  Existing dataset module whose imports must be updated to the new `scripts.models` and `scripts.training` locations where relevant.
- `scripts/reports/generate_styled_report_pdf.py`
  Existing report utility that stays under `scripts/` but may need path reference updates.
- `scripts/reports/validate_report_pdf.py`
  Existing report validation utility that stays under `scripts/` but may need path reference updates.
- `models/`
  Root folder to be repurposed from source code storage to trained/exported model artifact storage.

## Implementation Steps

1. Create this technical document and register it in the main project documentation.
2. Wait for explicit user approval before modifying the repository structure or implementation code.
3. Move the external agent submodules from `agents/` to `reference/agents/`.
4. Update `.gitmodules` to the new `reference/agents/...` paths and verify Git submodule state.
5. Move root `models/` source files into `scripts/models/`.
6. Move root `training/` source files into `scripts/training/`.
7. Create or normalize the root `models/` artifact structure for trained and exported model outputs.
8. Update Python imports and every path-sensitive script reference affected by the moved files.
9. Update usage and structure documentation so commands and folder meanings remain accurate.
10. Verify the migration with directory inspection, `rg` path checks, direct script smoke tests, and `git status`.
