# Campaign Folder Taxonomy Extension

## Overview

This technical document defines a repository-wide folder taxonomy extension for
campaign-related assets that are still stored in flat roots. The target is to
align `scripts/campaigns`, `doc/reports/analysis/validation_checks`, and
`output/training_campaigns` with the stable domain-first organization already
used under `doc/reports/campaign_results`.

## Technical Approach

The reorganization will preserve existing file and directory names at the leaf
level and will introduce only intermediate taxonomy folders. The first-level
folders will follow the currently established campaign domains already visible
in `doc/reports/campaign_results`: `infrastructure`, `mixed_training`,
`track1`, and `wave1`.

For items that already imply a second-level topic in their name or current
destination patterns, the move will also introduce a topic-local subfolder. The
initial expected second-level folders are:

- `track1/exact_paper/` for exact-paper and exact-model-bank material.
- `track1/harmonic_wise/` for harmonic-wise comparison material.
- `track1/svm/` for the older `SVM`-specific branch where that distinction is
  still useful.

Classification will be derived from the existing launcher names, validation
report names, and campaign output directory names. The move will be constrained
to path reorganization; no training configuration, launcher command content, or
report body content will be rewritten unless a broken repository-owned index or
path registry must be updated to keep navigation coherent.

Because `output/training_campaigns` may be referenced by repository state or
bookkeeping files, the implementation pass will include a targeted reference
scan after the move plan is finalized. If canonical state files or registries
still point to flat paths, those references will be updated in the same change
set.

## Involved Components

- `scripts/campaigns/`
- `doc/reports/analysis/validation_checks/`
- `output/training_campaigns/`
- `doc/reports/campaign_results/` as the taxonomy reference
- `doc/README.md` as the canonical documentation entry point
- repository-owned state or bookkeeping files that may still reference the old
  flat paths

## Implementation Steps

1. Confirm the current live directory contents and derive a deterministic
   domain/topic classification rule from existing names.
2. Register this technical document from `doc/README.md`.
3. Wait for explicit user approval before making any repository reorganization
   changes.
4. Create the missing domain and topic subfolders under the three target roots.
5. Move launcher scripts, validation reports, and training campaign output
   directories into the new taxonomy while preserving leaf names.
6. Run a repository search for references to the moved paths and repair
   repository-owned canonical references where needed.
7. Run Markdown QA on the touched documentation scope and confirm normal final
   newlines.
8. Report the completed reorganization and stop before any commit.
