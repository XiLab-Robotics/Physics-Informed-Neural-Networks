# Isolated Integration Reconciliation And Learning Guide Migration

## Overview

This document defines the reconciliation batch required to complete the
integration work originally described in `readme.temp.md`.

The current `integration/sphinx-docs` branch already integrated the
documentation-platform decision trail, the canonical Sphinx portal, and several
API slices. However, the branch did not yet execute the content-migration steps
described for the synchronized post-isolated phase.

The most visible symptom is that:

- the imported `NotebookLM` bundles are still stored under
  `doc/imports/notebooklm_exports/`;
- the learning-guide family is still rooted under
  `doc/reports/analysis/learning_guides/`;
- `doc/guide/` still contains only `project_usage_guide.md`.

This batch therefore exists to reconcile the actual branch state with the
remaining handoff obligations.

## Technical Approach

The reconciliation should follow the synchronized phases described in
`readme.temp.md`, but with one explicit clarification:

- `doc/imports/notebooklm_exports/` was correct as the isolated archival state;
- it is not the intended final canonical state if the synchronized migration is
  approved.

The batch should therefore:

1. move the canonical learning-guide family from
   `doc/reports/analysis/learning_guides/` to `doc/guide/`;
2. preserve each guide-local structure:
   - main Markdown guide;
   - PDF companion;
   - `assets/`;
   - `video_guide_package/`;
3. move the imported `NotebookLM` media from
   `doc/imports/notebooklm_exports/` into the corresponding canonical guide
   folders;
4. normalize imported filenames to readable guide-local names such as
   `Mind Map.png`, `Infographic.png`, `Supporting Brief.pdf`, and
   `Video Overview.mp4`;
5. create a canonical guide folder for `Multilayer Perceptrons`;
6. update shared references in `README.md`, `doc/README.md`, internal guide
   links, and any affected technical notes;
7. decide the residual role of `doc/imports/notebooklm_exports/` after the move:
   - either preserve it as a reduced provenance-only registry;
   - or retire it after successful migration and verification.

This batch should not simultaneously introduce unrelated API or Sphinx-platform
changes.

## Involved Components

- `readme.temp.md`
- `doc/reports/analysis/learning_guides/`
- `doc/guide/`
- `doc/imports/notebooklm_exports/`
- `README.md`
- `doc/README.md`
- the internal Markdown links inside the learning-guide family
- the related technical notes that still mention the pre-migration layout

## Implementation Steps

1. Inventory the current learning-guide tree and the imported `NotebookLM`
   bundles topic by topic.
2. Build the canonical destination folders under `doc/guide/`, including
   `Multilayer Perceptrons/`.
3. Move the repository-authored learning-guide assets from
   `doc/reports/analysis/learning_guides/` into `doc/guide/`.
4. Move the imported `NotebookLM` files into their target guide folders and
   normalize the final filenames.
5. Re-check every affected guide for broken internal links, missing assets, or
   overwritten filenames.
6. Update `README.md`, `doc/README.md`, and any affected technical references
   from the old guide root to the new canonical guide root.
7. Verify that no stale operational reference still treats
   `doc/imports/notebooklm_exports/` as the final canonical destination.
8. Run a final repository-wide verification focused on:
   - guide presence under `doc/guide/`;
   - imported-media presence in the correct guide folders;
   - reference consistency;
   - no accidental loss of PDFs, assets, or video-guide packages.
