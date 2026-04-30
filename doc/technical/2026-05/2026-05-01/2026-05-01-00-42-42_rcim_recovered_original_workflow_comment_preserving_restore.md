# RCIM Recovered Workflow Comment-Preserving Restore

## Overview

The recent repository-style cleanup pass over
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
overreached the intended scope and removed user-authored manual comments and
local formatting choices that were meant to be preserved.

The user has recovered comment-rich versions of several files as `_old`
backups. The next pass must restore those manual comments and formatting
choices conservatively, then re-apply only minimal repository-style
normalization that does not rewrite local control-flow layout such as inline
`if` usage or other deliberate one-line formatting decisions.

## Technical Approach

The restore pass will treat the `_old` files as the canonical source of truth
for comment content and local formatting in the affected files. The current
workflow files will be reconciled against those backups with these rules:

1. Restore the user-authored manual comments and local formatting from the
   `_old` copies wherever those backups exist.
2. Preserve local layout choices such as inline `if` formatting instead of
   re-expanding or collapsing them according to a generic style preference.
3. Limit style changes to minimal safe fixes:
   - section-comment capitalization where it does not alter comment meaning;
   - docstring cleanup where it does not overwrite user-authored inline notes;
   - spacing fixes only when they do not rewrite deliberate local layout.
4. Keep the existing repository-owned functional fixes that are still needed
   for execution, especially the lazy `seaborn` import strategy in
   `utilities/statistics.py`, unless the `_old` file already includes the same
   behavior.
5. Update the workflow `README.md` to document only the meaningful
   repository-owned divergences from the untouched reference code, not a
   cosmetic history of every comment adjustment.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py`
- matching `_old` backup files in the same subtree
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `requirements.txt` only if the `seaborn` pin or its documentation needs
  alignment after the restore

## Implementation Steps

1. Diff each current file against its `_old` backup and identify the manual
   comments and formatting choices that must be restored verbatim.
2. Restore those comment/layout surfaces conservatively from the `_old`
   versions without changing the executable logic.
3. Re-apply only minimal repository-style normalization that does not fight
   the restored layout.
4. Verify that required runtime fixes still hold, especially:
   - `statistics.py` lazy `seaborn` imports;
   - `predictorML.py` encoding and execution health.
5. Run compile and targeted smoke checks for the active workflow surface.
6. Run Markdown QA on the touched Markdown scope.
