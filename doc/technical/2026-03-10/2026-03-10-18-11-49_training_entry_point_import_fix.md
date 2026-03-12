# Training Entry-Point Import Fix

## Overview

The current `training/train_feedforward_network.py` entry point works when imported from the repository root, but it fails when executed directly with:

```powershell
python training/train_feedforward_network.py
```

The observed runtime error is:

```text
ModuleNotFoundError: No module named 'models'
```

This happens because Python initializes `sys.path` from the script directory when a file is executed directly, so the repository root is not guaranteed to be available for absolute project imports such as `models.model_factory`.

## Technical Approach

The fix will make the training entry point self-contained for direct script execution from the repository root.

The planned implementation is:

1. Resolve the repository root from `__file__`.
2. Insert the repository root into `sys.path` before importing internal project modules.
3. Keep the existing absolute import style (`models.*`, `training.*`, `scripts.*`) so the codebase remains consistent and readable.
4. Update the usage guide so the documented command `python training/train_feedforward_network.py` matches real behavior.

This approach is preferable to forcing only `python -m training.train_feedforward_network`, because the current project documentation and user workflow already expose the direct script command.

## Involved Components

- `training/train_feedforward_network.py`
  Training entry point that currently fails under direct execution.
- `doc/guide/project_usage_guide.md`
  Must be updated because this is a runnable workflow fix.
- `README.md`
  Main technical-document index.
- `doc/README.md`
  Internal documentation index.

## Implementation Steps

1. Add a small bootstrap block at the top of `training/train_feedforward_network.py` that appends the repository root to `sys.path` before internal imports.
2. Keep the rest of the training logic unchanged.
3. Update `doc/guide/project_usage_guide.md` to state that the documented direct script command is supported.
4. Run a direct execution verification of the training entry point with a temporary `fast_dev_run` configuration.
5. Commit the fix immediately after the implementation and verification.
