# Track 1 SVM Exact-Faithful Final Attempt Campaign Plan

## Overview

This planning report defines the largest campaign that remains technically
acceptable under the explicit constraint that `SVM` must stay identical to the
paper-side `SVR` path already recovered in the repository.

The campaign must therefore not:

- introduce a new algorithm;
- introduce non-paper hyperparameters;
- widen the search beyond the recovered paper grid;
- reinterpret the task as another heuristic seed or split exploration package.

The planning goal is not to invent a new `SVR` repair strategy. It is to decide
whether one last exact-faithful remote rerun package is worth executing before
declaring the `SVM` row plateaued under faithful reproduction.

## Current Canonical SVM Status

The canonical benchmark currently leaves only these `SVM` row cells open:

- Table `2` amplitude `MAE`: `40`
- Table `3` amplitude `RMSE`: `40`, `240`
- Table `4` phase `MAE`: `162`
- Table `5` phase `RMSE`: `162`

The immediately preceding exact-faithful remote campaign already targeted the
same closure queue through the recovered paper-reference grid path and produced
no new numeric closures.

## Campaign Principle

This package is intentionally narrow because the allowed search space is
already fixed by the paper-faithful branch.

The campaign must keep:

- `training.enabled_families: [SVR]`
- `training.hyperparameter_search.mode: paper_reference_grid_search`
- the existing recovered `SVR` reference grid
- the same exact-paper feature schema
- the same target-scope semantics already used by the canonical branch

The only valid reason to run this package is to check whether a final exact
rerun on the residual cells produces a closure that the earlier run missed.

If it does not, the repository should stop interpreting the residual yellow
cells as an unresolved tuning problem.

## Parameter Meanings And Effects

### Fixed Scientific Controls

- `enabled_families`
  Must remain `SVR` to preserve strict `SVM`-row fidelity.
- `training.hyperparameter_search.mode`
  Must remain `paper_reference_grid_search` so the search path matches the
  recovered paper workflow.
- `input_feature_names`
  Must stay on the exact-paper input set already used by the branch.
- `target_scope.mode`
  Keeps amplitudes and phases separate.
- `target_scope.harmonic_order_filter`
  Restricts evaluation to the residual closure harmonics only.

### Runtime Controls

- `training.hyperparameter_search.grid_search_n_jobs`
  Controls runtime parallelism inside the same recovered grid search and does
  not change the scientific question.
- remote campaign parallel launch
  Affects turnaround time only; it does not create new scientific coverage.

## Candidate Configuration Table

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Name | Scope | Harmonic Filter | Search Mode | Purpose |
| --- | --- | --- | --- | --- | --- |
| `E1` | `track1_svr_exact_faithful_amplitude_pair_repeat` | `amplitudes_only` | `40, 240` | `paper_reference_grid_search` | Repeat the exact paper-faithful amplitude pair search on the two residual amplitude cells together. |
| `E2` | `track1_svr_exact_faithful_amplitude_40_repeat` | `amplitudes_only` | `40` | `paper_reference_grid_search` | Repeat the exact paper-faithful isolated search on harmonic `40`. |
| `E3` | `track1_svr_exact_faithful_amplitude_240_repeat` | `amplitudes_only` | `240` | `paper_reference_grid_search` | Repeat the exact paper-faithful isolated search on harmonic `240`. |
| `E4` | `track1_svr_exact_faithful_phase_162_repeat` | `phases_only` | `162` | `paper_reference_grid_search` | Repeat the exact paper-faithful isolated search on harmonic `162`. |
<!-- markdownlint-enable MD013 -->

## Planned Campaign Size

Recommended package:

- `4` runs total
  - `3` amplitude-side exact-faithful reruns
  - `1` phase-side exact-faithful rerun

This is deliberately not a huge package, because the scientific search space is
already exhausted by construction.

## Success And Failure Reading

Success means at least one of the residual `SVM` yellow cells becomes green in
the canonical benchmark without changing the recovered `SVR` method.

Failure means:

- the exact-faithful reruns reproduce the same residual pattern;
- no new paper-target cell closes;
- the repository should stop treating the `SVM` row as a budget-worthy tuning
  frontier under exact-faithful constraints.

## Operator Deliverables

If and only if the user approves this plan, preparation should later generate:

1. the campaign YAML package;
2. the dedicated remote PowerShell launcher;
3. the matching launcher note;
4. the updated `doc/running/active_training_campaign.yaml` entry;
5. the exact remote launch command.

## Next Step

Wait for explicit user approval of:

- the technical document;
- this campaign planning report;
- the decision to spend one final exact-faithful remote attempt on `SVM`.
