# Track 1 SVR Reference Grid Search Repair Campaign Plan

## Objective

This campaign tests the remaining open `SVR` cells in canonical `Track 1`
through the recovered paper-reference `GridSearchCV` path instead of
repository-invented seed/split sweeps.

The objective is to determine whether the residual `SVM` gaps are due to the
previous non-paper-faithful training path or whether they remain open even when
the recovered paper tuning rule is used.

## Why This Campaign Exists

Earlier `SVR` repair campaigns used deterministic split changes and seed
variations. Those runs were useful to map the row behavior, but they were not
the paper-faithful way to search `SVR` hyperparameters.

The exact-paper workflow now supports the recovered paper-side
`GridSearchCV` path. This campaign is the first targeted use of that exact
training rule on the residual `SVR` cells.

## Current Residual Targets

The campaign is restricted to the `SVR` row and to the residual yellow cells:

- amplitude `40`
- amplitude `240`
- phase `162`

Mapped onto the canonical tables:

- `Table 2`: `40`
- `Table 3`: `40`, `240`
- `Table 4`: `162`
- `Table 5`: `162`

## Parameter Meanings

### Fixed Exact-Paper Controls

- `input_feature_names`
  Exact paper input schema: `rpm`, `deg`, `tor`.
- `maximum_deg`
  Same recovered dataframe cutoff already used by the canonical exact-paper
  branch.
- `test_size`
  Kept fixed to preserve the exact-paper comparison surface.
- `random_seed`
  Kept fixed to avoid introducing non-paper variability.
- `enabled_families`
  Restricted to `SVR` because this campaign is only about the current `SVM`
  row closure.

### Hyperparameter Search Controls

- `training.hyperparameter_search.mode`
  Must stay `paper_reference_grid_search` so the run uses the recovered
  reference grid instead of direct estimator fitting.
- `training.hyperparameter_search.grid_search_n_jobs`
  Parallelism for the search itself; it affects runtime, not the scientific
  target.

### Target Scope Controls

- `target_scope.mode`
  Limits the run to amplitudes or phases.
- `target_scope.harmonic_order_filter`
  Restricts the run to the exact residual harmonics.
- `target_scope.include_phase_zero`
  Must stay `false` when the run targets phases, because the canonical phase
  tables do not include harmonic `0`.

## Candidate Run Table

<!-- markdownlint-disable MD013 -->
| Config | Family | Search Mode | Scope | Harmonics | Scientific Purpose |
| --- | --- | --- | --- | --- | --- |
| `01_track1_svr_reference_grid_amplitude_pair` | `SVR` | `paper_reference_grid_search` | `amplitudes_only` | `40, 240` | Optimize the still-open amplitude pair together. |
| `02_track1_svr_reference_grid_amplitude_40_only` | `SVR` | `paper_reference_grid_search` | `amplitudes_only` | `40` | Remove `240` coupling and optimize `40` alone. |
| `03_track1_svr_reference_grid_amplitude_240_only` | `SVR` | `paper_reference_grid_search` | `amplitudes_only` | `240` | Remove `40` coupling and optimize `240` alone. |
| `04_track1_svr_reference_grid_phase_162_only` | `SVR` | `paper_reference_grid_search` | `phases_only` | `162` | Optimize the remaining phase blocker alone. |
<!-- markdownlint-enable MD013 -->

## Expected Outcomes

Best-case outcome:

- `40` closes in both amplitude tables;
- `240` closes in `Table 3`;
- `162` closes in `Tables 4` and `5`;
- the `SVR` row reaches full closure.

More conservative outcome:

- some current yellow cells improve but do not fully close;
- the campaign still tells us whether the remaining gap is algorithmic under
  the true paper tuning rule rather than under repository sweep heuristics.

## Execution Notes

- This campaign should be launched only after the user approves the prepared
  package.
- Because the run is deterministic and `GridSearchCV`-based, the package should
  stay narrow and inspectable.
- If the campaign still leaves the same cells yellow, the next move should be
  to shift effort to the other model families instead of continuing `SVR`
  sweeps.
