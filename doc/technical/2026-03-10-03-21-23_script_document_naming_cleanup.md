# Script Document Naming Cleanup

## Overview

This document defines a naming cleanup for the markdown files stored in `doc/scripts/`.

The current script documentation files use the prefix `scripts_`, for example:

- `scripts_datasets_transmission_error_dataset.md`
- `scripts_datasets_visualize_transmission_error.md`

The requested change is to remove the `scripts_` prefix and keep cleaner names that still preserve the script scope and origin.

## Technical Approach

The naming cleanup will only affect markdown documentation files inside `doc/scripts/`.

Planned rename mapping:

- `scripts_datasets_transmission_error_dataset.md`
  -> `datasets_transmission_error_dataset.md`

- `scripts_datasets_visualize_transmission_error.md`
  -> `datasets_visualize_transmission_error.md`

Required follow-up updates:

- update references in `README.md`;
- update references in `doc/README.md`;
- verify that no old `scripts_*.md` references remain.

This change is documentation-only and does not affect Python module paths or runtime code behavior.

## Involved Components

- `doc/scripts/`
  Folder containing the script-level documentation files to rename.

- `doc/README.md`
  Documentation index that must be updated with the new file names.

- `README.md`
  Main project document that must be updated with the new file names.

## Implementation Steps

1. Rename the markdown files inside `doc/scripts/`.
2. Update `doc/README.md` with the new names.
3. Update `README.md` with the new names.
4. Search for residual references to the old `scripts_` names and remove them.
