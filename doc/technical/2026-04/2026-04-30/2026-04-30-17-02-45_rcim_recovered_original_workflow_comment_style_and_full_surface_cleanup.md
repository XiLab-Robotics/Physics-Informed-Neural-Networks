# RCIM Recovered Original Workflow Comment Style And Full Surface Cleanup

## Overview

This document plans a second cleanup pass over the repository-owned RCIM
recovered-original workflow under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`.
The new pass is narrower than the previous structural stabilization work and is
focused on repository-style presentation quality across the full surface:
comment capitalization, comment accuracy, comment verbosity, spacing, docstring
clarity, and removal of stale inline residue that still survives in active
methods.

The user has also manually added comments and adjusted layout in several files,
and has already added `seaborn` to `requirements.txt` because
`utilities/statistics.py` depends on it. This pass must preserve those manual
edits where they are useful while normalizing them to the repository style and
correcting any inaccurate or overly verbose commentary.

## Technical Approach

The pass will process every maintained script in the recovered-original
workflow root and in its `utilities/` subtree. The implementation goal is to
raise the repository-owned copy to the normal documentation and readability
standard of this repository without rewriting the original numerical logic.

The cleanup will follow these rules:

- keep function names, variable names, and executable logic stable;
- keep unused functions in place;
- normalize section-comment capitalization to repository style, for example
  `# Read Component Errors` instead of sentence-case or mixed-case variants;
- shorten or correct verbose manual comments where they are inaccurate or too
  long for local readability;
- add or refine docstrings only where they materially improve local clarity;
- remove commented-out code, stale debug artifacts, obsolete inline notes, and
  unused local residue inside active methods;
- retain the repository-owned divergence log in the workflow `README.md`,
  focusing on meaningful behavioral or maintenance differences from the
  reference root rather than on every cosmetic comment change;
- preserve the newly added `seaborn` dependency in `requirements.txt` and
  validate that the dependency declaration stays aligned with the maintained
  workflow code.

The pass will also revisit `predictorML.py`, especially the
`predictorMLCrossValidation` path and nearby active methods, because the user
has identified remaining legacy comments and unused local variables there.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `requirements.txt`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/recovered_original_workflow.md`
- `site/` API and guide pages if the user-facing documentation surface changes

## Implementation Steps

1. Inspect every maintained Python file in the recovered-original workflow
   subtree and identify remaining legacy comments, stale commented-out code,
   inaccurate manual comments, section-comment capitalization drift, and
   obvious unused local variables inside active methods.
2. Apply file-by-file cleanup with `apply_patch`, preserving executable logic
   and identifier names while normalizing spacing, docstrings, and comments.
3. Revisit `predictorML.py` in more depth, especially the
   `predictorMLCrossValidation` area and nearby active paths, and remove stale
   commented code or unused locals that still obscure the maintained surface.
4. Update the workflow `README.md` so that meaningful repository-owned cleanup
   differences relative to
   `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
   remain documented.
5. Keep `requirements.txt` aligned with the maintained imports, including the
   user-added `seaborn` dependency.
6. Run Python compile checks on the touched Python scope.
7. Run the repository Markdown QA entry points on touched Markdown files.
8. Rebuild the Sphinx portal with `python -m sphinx -W -b html site
   site/_build/html` if the portal-facing surface remains affected.
