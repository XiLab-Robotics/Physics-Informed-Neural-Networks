# Training Terminal Output Cleanup

## Overview

The current terminal output of `training/train_feedforward_network.py` is difficult to read during normal execution.

The main issues are:

- the full `pformat()` dump of the YAML configuration is too dense for interactive terminal use;
- lifecycle `print()` calls overlap with Lightning progress-bar rendering;
- the default Lightning model summary adds noise without improving the training workflow;
- known Lightning runtime warnings and suggestions visually dominate the useful project messages;
- the current output does not visually separate configuration, dataset, normalization, runtime status, and final artifacts.

The user requested a more readable and colorized terminal experience, while keeping the code aligned with the repository style.

## Technical Approach

The cleanup will keep the training logic unchanged and only improve the terminal UX of the training entry point.

The planned implementation is:

1. Use `colorama` for terminal colors because it is already available in the current Conda environment and works reliably on Windows terminals.
2. Replace the raw `pformat()` configuration dump with explicit section printers:
   - configuration overview;
   - dataset summary;
   - normalization summary;
   - trainer/runtime summary;
   - final artifact summary.
3. Add small reusable print helpers for:
   - section headers;
   - key/value rows;
   - success, warning, and info messages.
4. Replace the current lifecycle callbacks with cleaner messages that do not fight the progress bar output.
5. Configure the Lightning trainer output more deliberately:
   - use an explicit `TQDMProgressBar` callback with a controlled refresh rate;
   - disable the default model summary and print a compact project-specific model summary instead.
6. Remove console noise where it is low-signal and dependency-internal:
   - suppress the known Lightning `_pytree` deprecation warning;
   - set `persistent_workers=True` when `num_workers > 0` so Lightning does not keep printing the worker-initialization suggestion.
7. Update user-facing documentation so the usage guide matches the refined terminal behavior.

This approach keeps the existing training pipeline intact while making the terminal output fit the repository's readability goals.

## Involved Components

- `training/train_feedforward_network.py`
  Main entry point that prints configuration, runtime status, and final training outputs.
- `training/transmission_error_datamodule.py`
  May receive the `persistent_workers` adjustment to remove repeated Lightning suggestions.
- `doc/guide/project_usage_guide.md`
  Must be updated because the runnable training workflow and terminal behavior are being refined.
- `README.md`
  Main technical-document index.
- `doc/README.md`
  Internal documentation index.

## Implementation Steps

1. Add small colorized terminal-print helpers in `training/train_feedforward_network.py` using `colorama`.
2. Replace the dense configuration dump with compact section-based summaries and aligned key/value formatting.
3. Swap the current start/validation `print()` callbacks for output that coexists cleanly with Lightning progress bars.
4. Add a controlled Lightning progress-bar callback and disable the default model summary in favor of a concise custom summary.
5. Update the datamodule to enable `persistent_workers` only when `num_workers > 0`.
6. Filter the single known dependency-internal warning that currently pollutes the console.
7. Update `doc/guide/project_usage_guide.md` to reflect the cleaner terminal workflow.
8. Verify the direct command `python training/train_feedforward_network.py` with a temporary `fast_dev_run` configuration.
9. Commit the changes immediately after verification.
