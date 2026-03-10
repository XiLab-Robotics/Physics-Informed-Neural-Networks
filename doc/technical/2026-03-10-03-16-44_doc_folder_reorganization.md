# Documentation Folder Reorganization

## Overview

This document defines the reorganization of the `doc/` folder to keep project documentation easier to navigate and maintain.

The current issue is that `doc/` mixes together three different document categories:

- summaries derived from the reference PDFs;
- timestamped technical project documents;
- script-level documentation files.

The requested objective is to separate these categories into dedicated subfolders and update the repository indexes accordingly.

## Technical Approach

The proposed `doc/` structure is:

- `doc/reference_summaries/`
  For the numbered documents derived from the reference PDFs and reference codebases.

- `doc/technical/`
  For timestamped technical project documents using the `YYYY-MM-DD-HH-mm-SS-feature_name.md` format.

- `doc/scripts/`
  For markdown documentation dedicated to Python scripts.

- `doc/README.md`
  Main documentation index updated to reflect the new grouped structure.

Planned file migration:

1. Move `01...06` documents into `doc/reference_summaries/`.
2. Move timestamped technical documents into `doc/technical/`.
3. Move script documentation files into `doc/scripts/`.
4. Keep `doc/README.md` at the root of `doc/` as the documentation entry point.

Repository-level index changes:

- update `README.md` so that the documentation section references the new grouped paths;
- update `doc/README.md` so that it lists documents by category instead of as one flat list.

This reorganization is documentation-only and does not change runtime code behavior.

## Involved Components

- `doc/`
  Main documentation root to reorganize.

- `doc/reference_summaries/`
  New folder for the `01...06` reference-derived summaries.

- `doc/technical/`
  New folder for timestamped technical project documents.

- `doc/scripts/`
  New folder for script-level markdown documentation.

- `doc/README.md`
  Documentation index to update.

- `README.md`
  Main project document to update with the new grouped documentation paths.

## Implementation Steps

1. Create the new `doc/` subfolders.
2. Move the existing markdown files into their new categories.
3. Update `doc/README.md` to show grouped sections and new relative links.
4. Update `README.md` to reference the new grouped documentation paths.
5. Verify that all documentation links still resolve correctly.
