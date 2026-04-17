# Track 1 SVM Exact-Faithful Final Attempt Preparation

## Overview

This technical document prepares a decision on whether `Track 1` should run one
last `SVM`-row attempt under a strict paper-faithful constraint.

The user requirement is explicit:

- keep the model family as recovered paper `SVR`;
- keep the paper-faithful training rule already implemented in the repository;
- do not introduce a new algorithm;
- do not expand or alter the paper hyperparameter search space;
- do not reinterpret the task as a new generic tuning campaign.

The current canonical benchmark shows that the `SVM` row is already very close
to the paper row, with only the following residual yellow cells:

- Table `2` amplitude `MAE`: harmonic `40`
- Table `3` amplitude `RMSE`: harmonics `40`, `240`
- Table `4` phase `MAE`: harmonic `162`
- Table `5` phase `RMSE`: harmonic `162`

The immediately preceding remote `SVR` reference-grid repair campaign already
executed the recovered paper-faithful `GridSearchCV` path on those exact
residual targets and confirmed that the remaining gaps stayed open.

This means the next preparation step is not a normal “more budget” campaign
decision. It is a policy decision about whether a final exact-faithful rerun
package is still justified despite the fact that the paper-faithful search has
already been exercised once end to end.

No subagent use is planned for this task. Campaign preparation, documentation,
and any possible launcher packaging should remain local and repository-owned.

## Technical Approach

The preparation must preserve scientific interpretability first.

Under the user-approved constraint, the repository must not change:

- `SVR` as the only enabled family for this attempt;
- the recovered paper-faithful `paper_reference_grid_search` path;
- the exact `SVR` search space already used by the recovered branch;
- the paper-facing feature schema and target decomposition;
- the canonical exact-paper evaluation logic.

Because of those constraints, a new “huge” remote campaign is not technically
well justified. Parallelizing many runs only helps when there are real
scientific degrees of freedom to explore. Under strict exact-faithful `SVR`,
the legitimate degrees of freedom are extremely limited.

The only defensible final attempt is therefore a narrow exact-faithful package
whose role is:

1. confirm that the already recovered paper-faithful `SVR` route remains
   reproducible on the remote workstation;
2. isolate the last residual targets in the same exact-paper search regime;
3. verify whether any exact-faithful rerun closes cells through run-local
   variance rather than through repository-invented tuning changes.

The practical implication is:

- a broad sweep is not recommended;
- a small exact-faithful confirmation package is the maximum technically clean
  option;
- if that package still leaves the same cells yellow, the repository should
  treat the residual `SVM` gap as structurally open under the current exact
  paper reproduction path instead of continuing `SVR` budget spending.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/2026-04-17-11-00-54_track1_svr_reference_grid_search_repair_campaign_results_report.md`
- `doc/reports/campaign_plans/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`

## Implementation Steps

1. Create a dedicated planning report for an exact-faithful final-attempt
   package that does not alter the recovered `SVR` algorithm or hyperparameter
   regime.
2. Ask for explicit user approval of this technical document and the planning
   report before generating any campaign package.
3. If approval is granted, prepare only a narrow exact-faithful rerun package
   for the residual cells `40`, `240`, and `162`.
4. Keep the launcher package remote-ready, but do not broaden the run matrix
   into a generic parallel sweep.
5. If the user later approves execution and the rerun still leaves the same
   cells yellow, close the branch as an exact-faithful `SVR` plateau rather
   than opening another large `SVM` campaign.
