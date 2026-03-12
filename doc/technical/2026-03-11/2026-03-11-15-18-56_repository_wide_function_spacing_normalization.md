# Repository-Wide Function Spacing Normalization

## Overview

The previous style-normalization change was initially applied to `training/train_feedforward_network.py`.

The user then clarified two points:

- the requested convention must be applied to all project scripts, not only to the training entry point;
- `training/train_feedforward_network.py` has now been manually adjusted by the user and must be treated as the style reference for the remaining scripts.

The target convention is:

- one blank line between each top-level function signature and its docstring;
- one blank line between consecutive top-level function definitions.

The current manual formatting in `training/train_feedforward_network.py` should therefore be mirrored in the other project-authored Python files wherever the same top-level function structure appears.

This normalization must be applied only to the project-authored Python code and must exclude:

- `reference/`
- `agents/`
- generated output folders
- temporary user work folders

## Technical Approach

The change is purely stylistic and must not alter runtime behavior.

The current repository scope for the normalization is:

- `models/`
- `training/`
- `scripts/`

Within that scope, the implementation will:

1. inspect `training/train_feedforward_network.py` as the approved reference example;
2. inspect every remaining `.py` file that contains top-level functions;
3. insert one blank line after each top-level `def ...:` line before the docstring;
4. collapse any double blank-line separation between consecutive top-level functions to a single blank line;
5. leave classes, imports, constants, comments, and runtime logic unchanged unless needed to match the approved file-level layout pattern already present in the reference file.

This will be done manually with repository-aware edits instead of using a generic formatter, because the user asked for the other scripts to follow the currently approved style of `training/train_feedforward_network.py`, not merely a generic formatter default.

## Involved Components

- `models/feedforward_network.py`
- `models/model_factory.py`
- `training/transmission_error_datamodule.py`
- `training/transmission_error_regression_module.py`
- `scripts/datasets/transmission_error_dataset.py`
- `scripts/datasets/visualize_transmission_error.py`
- `training/train_feedforward_network.py`
  Style reference that defines the approved target layout for the remaining scripts.
- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index.

## Implementation Steps

1. Read `training/train_feedforward_network.py` and treat its current manual formatting as the approved style reference.
2. Scan the remaining project-authored Python files under `models/`, `training/`, and `scripts/`.
3. Normalize the blank lines around top-level function definitions so they match the approved reference file.
4. Keep package-marker files such as `__init__.py` unchanged unless they actually contain affected function definitions.
5. Run a lightweight syntax validation over the edited Python files.
6. Create the required Git commit immediately after the approved modification.
