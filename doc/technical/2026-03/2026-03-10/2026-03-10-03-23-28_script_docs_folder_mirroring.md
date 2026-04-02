# Script Documentation Folder Mirroring

## Overview

This document defines the final organization rule for the markdown files stored under `doc/scripts/`.

The requested rule is:

- the documentation tree inside `doc/scripts/` must mirror the Python module tree inside `scripts/`.

This means the markdown documentation path must reflect the same subfolder structure used by the corresponding Python script.

Example:

- `scripts/datasets/transmission_error_dataset.py`
  -> `doc/scripts/datasets/transmission_error_dataset.md`

- `scripts/datasets/visualize_transmission_error.py`
  -> `doc/scripts/datasets/visualize_transmission_error.md`

## Technical Approach

The current `doc/scripts/` layout still uses flat filenames:

- `scripts_datasets_transmission_error_dataset.md`
- `scripts_datasets_visualize_transmission_error.md`

The final structure will be:

- `doc/scripts/datasets/transmission_error_dataset.md`
- `doc/scripts/datasets/visualize_transmission_error.md`

Required updates:

- create the mirrored subfolders inside `doc/scripts/`;
- move the existing markdown files into the mirrored paths;
- update the references in `README.md`;
- update the references in `doc/README.md`;
- remove residual references to the old flat filenames.

This change affects only markdown documentation paths and does not change runtime Python behavior.

## Involved Components

- `scripts/`
  Source Python tree whose structure must be mirrored.

- `doc/scripts/`
  Documentation tree to reorganize.

- `README.md`
  Main project document to update with the mirrored script-doc paths.

- `doc/README.md`
  Documentation index to update with the mirrored script-doc paths.

## Implementation Steps

1. Create the mirrored subfolder structure inside `doc/scripts/`.
2. Move the script documentation markdown files into the new mirrored paths.
3. Update `README.md` references.
4. Update `doc/README.md` references.
5. Verify that no old flat script-document names remain in repository documentation.
