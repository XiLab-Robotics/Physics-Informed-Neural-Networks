# RCIM Recovered Original Workflow Utility Visual Style Normalization

## Overview

This document formalizes one additional repository-owned cleanup pass over the
recovered original RCIM workflow utilities under:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`

The goal is narrower and more style-specific than the previous utility cleanup
pass. The user explicitly wants the utility files to match the visual writing
style already established manually in:

- `create_dataframe.py`
- `training_models.py`
- `evaluate_models.py`
- `workflow_runtime.py`

In practice this means:

- wider vertical spacing;
- repository-style comment capitalization;
- many more inline `#` comments in active logic blocks;
- docstring formatting aligned to the repository-authored surface;
- removal of remaining stale commented-out residue in the active code paths.

The numerical logic and the legacy branch structure must remain intact.

## Technical Approach

The pass will be conservative with respect to behavior and identifiers, but
aggressive with respect to visual normalization.

The implementation will:

1. keep existing class names, function names, and variable names unchanged;
1. preserve the recovered original logic, including active legacy branches;
1. normalize comment style to the repository pattern used by the user:
   - blank line after class declaration;
   - docstrings padded in the same local visual style when already used;
   - short Title-Case inline comments such as
     `# Keep the Original Wrapper Contract Intact.`;
   - more section comments before non-trivial logical blocks;
1. remove leftover commented-out garbage from the active execution paths where
   it no longer serves as meaningful documentation;
1. keep live historical methods that are not currently called, but still align
   their layout and comments where touched;
1. update the workflow `README.md` only to record meaningful repository-owned
   style and cleanup divergence from the reference root.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/technical/2026-05/2026-05-01/README.md`
- `doc/README.md`

Reference and style anchors:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- the current repository-owned main workflow scripts under
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

## Implementation Steps

1. inspect the current utility-file state and identify remaining visual drift;
1. normalize class spacing, docstring spacing, and inline comment style in
   `instance_v4.py`;
1. apply the same style pass to `instance_v5.py`;
1. perform the deepest pass on `predictorML.py`, focusing on active methods and
   the remaining commented-out residue in the current repository-owned copy;
1. update the workflow `README.md` to record any meaningful cleanup divergence;
1. run:
   - `py_compile` on the recovered workflow subtree;
   - at least one `paper_eval` smoke run through `training_models.py`;
   - Markdown QA on the touched Markdown scope.
