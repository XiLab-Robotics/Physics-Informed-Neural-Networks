# Repository Dataset Path Migration

## Overview

Replace every repository text reference to the removed legacy dataset root with
the canonical `data/simplified_dataset` path.

The initial audit found 1,814 tracked text files containing the old path in
forward-slash or Windows backslash form. The affected surface includes active
configuration, training campaign variants, Python scripts, user-facing
documentation, technical documents, reports, validation summaries, and stored
CSV or YAML artifacts.

This migration intentionally includes historical and generated textual
artifacts because the approved requirement is repository-wide removal of the
old path. Existing numerical results and model files will not be regenerated;
only their textual dataset-path references will be normalized.

## Technical Approach

Perform an exact mechanical migration from both slash variants of the legacy
dataset root to the corresponding slash variant of
`data/simplified_dataset`.

Only Git-tracked text files will be modified. Binary files, dataset contents,
model files, and Git history will remain unchanged.

The migration will be validated in layers:

1. Active configuration and training paths must resolve to the existing
   `data/simplified_dataset` directory.
2. Python scripts must contain no executable or metadata reference to the old
   path.
3. Repository documentation, reports, summaries, and textual output artifacts
   must contain no remaining old-path occurrence.
4. The canonical dataset loader and representative visualization or
   dataloader entry points must successfully resolve the migrated path.
5. All touched authored Markdown must pass repository Markdown QA.
6. The Sphinx documentation portal must build without warnings because the
   public README and project usage guide are in scope.

## Involved Components

- `config/`
  - Canonical dataset configuration and materialized campaign variants.
- `scripts/`
  - Dataset, training, paper-reimplementation, and report tooling references.
- `README.md`
  - Public repository dataset layout and configuration examples.
- `doc/`
  - User guides, technical documents, reports, and documentation indices.
- `output/`
  - Tracked textual validation and analysis artifacts containing stored source
    paths.
- `site/`
  - Canonical Sphinx portal to rebuild after the documentation migration.
- `data/simplified_dataset/`
  - Existing replacement dataset root that all migrated operational references
    must resolve to.

## Implementation Steps

1. Re-run the tracked-text inventory immediately before editing.
2. Replace both slash variants in every matching Git-tracked text file.
3. Confirm that no tracked text file still contains either old-path form.
4. Confirm that the replacement did not create duplicated or malformed path
   segments.
5. Validate the canonical dataset configuration and representative dataset
   loading entry points without running a training campaign.
6. Run targeted Python or configuration checks for affected operational
   scripts.
7. Run repository Markdown style and markdownlint checks over all touched
   authored Markdown files.
8. Build the Sphinx portal with warnings treated as errors.
9. Review the final diff, report the migration outcome, and wait for explicit
   approval before creating a Git commit.
