# RCIM Recovered Original Workflow Utility Cleanup And Style Alignment

## Overview

This task plans a new cleanup and style-alignment pass for the repository-owned
RCIM recovered-original workflow under:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

The scope is intentionally narrow and focuses only on the utility modules that
still carry visible legacy residue after the earlier workflow rebuild and
comment-preserving restore:

- `utilities/instance_v4.py`
- `utilities/instance_v5.py`
- `utilities/predictorML.py`

The goal is to finish the repository-owned cleanup of those three utility
modules so they match the style direction already established manually in:

- `create_dataframe.py`
- `training_models.py`
- `evaluate_models.py`
- `workflow_runtime.py`

The requested pass must preserve the numerical behavior and public callable
surface of the recovered-original workflow while improving readability and
maintainability.

## Technical Approach

The implementation pass will follow these rules:

1. Keep the original numerical logic and callable behavior unchanged.
2. Do not rename functions, variables, or other identifiers.
3. Clean old commented-out fragments, dead local residue, and obviously stale
   legacy attempts that are still present inside the three utility modules.
4. Align layout, spacing, and section-comment style to the repository style
   already adopted in the recovered-original workflow main entrypoints.
5. Add many short inline `#` comments before non-trivial logical blocks, using
   the repository-preferred title-style capitalization.
6. Preserve useful user-authored local formatting patterns where they already
   express the intended structure clearly.
7. Keep `README.md` in the workflow folder updated with the meaningful
   repository-owned divergences from the untouched reference originals.

Special handling by file:

- `instance_v4.py`
  focus on spacing, block comments, constructor/readability cleanup, and
  removal of clearly obsolete commented-out residue still left in the file.
- `instance_v5.py`
  same cleanup direction as `instance_v4.py`, with special attention to the
  longer signal-reconstruction helpers and the mixed `Fw`/`Bw` branches.
- `predictorML.py`
  finish the cleanup of legacy commented-out material, dead locals, and layout
  inconsistencies while preserving the active training/export/evaluation paths.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `requirements.txt`
  only if dependency documentation needs to be realigned while touching the
  workflow documentation surface.

Validation scope:

- `py_compile` on the recovered-original workflow subtree
- targeted smoke runs for at least one active recovered-original path
- Markdown QA on the touched documentation scope

No subagents are planned for this task.

## Implementation Steps

1. Inspect the current state of `instance_v4.py`, `instance_v5.py`, and
   `predictorML.py` to isolate remaining legacy residue and style drift.
2. Clean obsolete commented-out blocks and dead residue that still pollute the
   active repository-owned utility surface.
3. Normalize spacing, section structure, and inline comments so the utility
   modules visually match the style now used in the recovered-original
   entrypoints.
4. Add repository-style inline `#` comments before non-trivial logical blocks
   throughout the three utility modules.
5. Update the workflow `README.md` so it records the meaningful cleanup
   divergences relative to
   `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`.
6. Run `py_compile`, one or more smoke checks, and Markdown QA on the touched
   documentation scope.
