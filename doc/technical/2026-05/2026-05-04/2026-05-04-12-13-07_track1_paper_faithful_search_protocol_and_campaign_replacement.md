# 2026-05-04-12-13-07 Track1 Paper-Faithful Search Protocol And Campaign Replacement

## Overview

This document supersedes the earlier campaign-only replacement gate by adding
the missing protocol-alignment work that is still required before a
paper-faithful `Track 1` rerun can be prepared.

The recovered original RCIM workflow does not stop at `GridSearchCV.fit(...)`.
Its historical hyperparameter-search branch also executes a
`cross_validate(...)` sweep on the search wrapper and then re-scores the best
wrapped estimators target by target. The current repository reimplementation
does not yet reproduce that protocol stage.

Therefore the next exact-paper refresh must do two things in sequence:

1. align the repository search protocol to the recovered original workflow;
2. replace the active `400`-run campaign with a paper-faithful `20`-run
   campaign that performs exactly one search pass per family-direction surface.

## Technical Approach

Treat the recovered original workflow under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow`
as the behavioral source of truth for both:

- family definitions and family grids;
- the historical search-and-cross-validation protocol around the fit.

The implementation scope will:

1. preserve the already aligned family registries and parameter grids;
2. add the missing historical `cross_validate(...)` stage after the search fit
   in the shared exact-paper training path used by both
   `exact_paper_model_bank` and `original_dataset_exact_model_bank`;
3. store the resulting protocol summaries in a repository-owned structure so
   closeout, validation, and future audits can inspect them;
4. replace the repeated-seed `400`-run campaign design with a single-pass
   paper-faithful `20`-run campaign;
5. keep `doc/running/active_training_campaign.yaml` untouched until explicit
   approval because it is protected while the current campaign is still
   marked `running`.

The target protocol semantics are:

- one held-out split with `train_test_split(..., random_state=0)`;
- one `GridSearchCV(...)` wrapper per family-direction surface;
- one `cross_validate(...)` pass on that wrapper across the full surface;
- one target-wise `cross_validate(...)` pass on each best wrapped estimator;
- no seed sweep and no campaign-level retries.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`

No subagent is planned for this scope. If subagent assistance becomes useful
later, it must be declared and approved before use.

## Implementation Steps

1. Freeze the protocol delta and the campaign replacement in a new planning
   report that supersedes the previous `400`-run literal-refresh plan.
2. After approval, patch the shared exact-paper training flow so it reproduces
   the recovered historical search-plus-cross-validation protocol.
3. Verify the new protocol summary outputs on a narrow smoke surface before
   generating the replacement campaign package.
4. Materialize the new bidirectional exact-paper campaign with `20` total
   runs, one per family-direction surface.
5. Generate the matching YAML set, PowerShell launcher, and launcher note.
6. Update `doc/running/active_training_campaign.yaml` from the current active
   `400`-run campaign state to the replacement campaign state only after
   explicit approval.
7. Provide the exact launch command for the new paper-faithful campaign.
