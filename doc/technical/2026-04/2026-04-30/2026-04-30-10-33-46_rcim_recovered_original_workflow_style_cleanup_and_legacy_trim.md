# RCIM Recovered Original Workflow Style Cleanup And Legacy Trim

## Overview

This document plans a repository-style cleanup pass over the full
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
subtree.

The goal is to align this recovered-original workflow with the repository
coding and documentation directives while preserving the recovered numerical
logic and the current entrypoint contracts.

This pass is intentionally focused on:

- docstrings;
- section comments and inline comments;
- spacing and formatting cleanup;
- naming-format normalization where formatting can improve without renaming the
  actual identifiers;
- removal of obsolete commented code and local generated residue inside the
  workflow subtree;
- documentation of all meaningful non-comment cleanup decisions in the
  workflow-local README.

This pass must not alter the mathematical behavior of the copied original
functions, must not rename variables or functions, and must not touch
protected campaign files.

## Technical Approach

The current recovered-original workflow is already operational and stabilized
at the path/runtime layer. The next step is a style and hygiene pass that makes
the code easier to read and more consistent with the repository rules without
turning it into a fresh reimplementation.

The pass will therefore:

1. inspect every Python file in the workflow subtree and separate:
   - directly owned repo wrapper code;
   - copied original utility code;
   - generated local residue such as `__pycache__`;
2. add or refine Google-style docstrings where appropriate for repo-owned
   files, and improve existing docstrings or comments in copied utility files
   only where the change is stylistic and behavior-neutral;
3. remove stale commented-out fragments, legacy artifacts, and obsolete guards
   that no longer reflect the now-canonical recovered original root or the
   author clarifications;
4. preserve unused functions when they are part of the copied original helper
   surface, as explicitly requested, even if they are not called today;
5. record all meaningful non-comment cleanup decisions in
   `recovered_original_workflow/README.md`, especially where the repository
   copy intentionally diverges from the literal recovered source by removing:
   - obsolete comments;
   - generated residue;
   - stale guards such as legacy filters that no longer belong in the runtime
     workflow.

The pass may normalize whitespace, blank lines, import grouping, and section
comment placement across the subtree. It must not change behavior through
algorithmic rewrites.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/recovered_original_workflow.md`
- `doc/technical/2026-04/2026-04-30/README.md`
- `doc/README.md`

Expected removable local residue if present:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/__pycache__/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/__pycache__/`

Protected files that remain out of scope:

- `doc/running/active_training_campaign.yaml`
- all campaign files currently listed in the protected-file list

## Implementation Steps

1. Inspect the full workflow subtree and classify repo-owned wrappers, copied
   original utilities, and removable local generated residue.
2. Apply spacing, docstring, import-layout, and comment cleanup across the
   subtree without renaming identifiers or changing numerical behavior.
3. Remove obsolete commented code, obsolete local artifacts, and stale logic
   guards that should no longer remain in the repository-owned workflow copy.
4. Update the workflow-local README so it records meaningful cleanup and legacy
   removals relative to the recovered original reference root.
5. Run `py_compile` on the touched Python scope, run scoped Markdown QA on the
   touched Markdown files, and rebuild the Sphinx portal with `-W` if
   portal-facing documentation changes.
