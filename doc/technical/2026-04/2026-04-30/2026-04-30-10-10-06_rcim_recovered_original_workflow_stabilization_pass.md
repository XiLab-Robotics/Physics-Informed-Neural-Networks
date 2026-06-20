# RCIM Recovered Original Workflow Stabilization Pass

## Overview

This document plans the next stabilization pass for the repository-owned
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
surface that was rebuilt from the newly recovered original RCIM codebase.

The focus of this pass is not to redesign the recovered logic. The focus is to
stabilize the direct three-script execution surface around:

- repository-owned path handling;
- consistent runtime-root behavior across dataframe, training, and evaluation;
- clearer `Fw` versus `Bw` operator semantics;
- explicit documentation of the current forward-only evaluation limitation;
- campaign-safe separation from the currently prepared/running RCIM Model-Bank Reproduction campaign.

This pass must avoid edits to protected campaign files listed in
`doc/running/active_training_campaign.yaml`.

## Technical Approach

The workflow was already rebuilt into direct entrypoints:

- `create_dataframe.py`
- `training_models.py`
- `evaluate_models.py`

plus copied original modules under `utilities/`.

The next pass will keep that structure, but tighten the operational layer that
wraps the copied original code:

1. factor the path/runtime-root conventions into a clearer shared pattern
   across the three entrypoints, while still keeping the original helper logic
   almost unchanged;
2. validate that default input roots and output roots are coherent with the now
   canonical recovered original root under
   `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`;
3. make the `Fw`/`Bw` behavior clearer in the CLI and documentation so the
   current state is explicit:
   - dataframe creation supports both `Fw` and `Bw`;
   - training supports both `Fw` and `Bw`;
   - shipped evaluation is still effectively `Fw`-only;
4. review whether repeated local helper logic inside the three main scripts can
   be reduced into a minimal shared utility without rewriting the original
   numerical logic;
5. refresh the workflow README and adjacent script documentation so the runtime
   directory contract, default roots, and mode mapping are fully explicit.

The current active campaign state shows a mismatch between the user-reported
`running` state and the persisted `prepared` state. This stabilization pass
must not edit that protected state file unless the user asks for that fix
explicitly.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/recovered_original_workflow.md`
- `doc/guide/project_usage_guide.md`
- `site/api/paper_reimplementation/`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-30/README.md`

Protected files that must remain untouched during this pass unless separately
approved:

- `doc/running/active_training_campaign.yaml`
- campaign launchers and campaign-plan files currently listed in
  `active_training_campaign.yaml`

## Implementation Steps

1. Inspect the three rebuilt entrypoints and identify duplicated runtime-root
   and direction-normalization logic that can be stabilized without changing
   the original modeling logic.
2. Apply a narrow refactor to improve path handling consistency and default-root
   clarity across dataframe creation, training, and evaluation.
3. Keep `utilities/` numerically faithful to the recovered original code and
   avoid behavioral rewrites unless a path or execution bug forces a minimal
   compatibility fix.
4. Update the workflow README and adjacent documentation to reflect the final
   stabilized path contract, CLI semantics, and current `Fw`/`Bw` capabilities.
5. Run `py_compile` on the touched Python scope, rerun targeted smoke checks if
   behavior changed, run scoped Markdown QA on touched Markdown files, and
   rebuild the Sphinx portal with `-W` if portal-facing docs change.
