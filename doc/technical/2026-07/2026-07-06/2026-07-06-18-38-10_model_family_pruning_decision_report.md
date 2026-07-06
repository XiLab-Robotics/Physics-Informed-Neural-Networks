# Model Family Pruning Decision Report

## Overview

This document plans a model-family pruning decision report for the TE modeling
program. The requested work is to analyze the current report and validation
surface, exclude `global` candidates from near-term model-selection reasoning,
and produce a documented keep / pause / retire decision for each relevant
model family.

The immediate decision scope is `forward` and `backward` only. `forward`
evidence will be treated as the primary decision driver. `backward` evidence
will be used as a consistency check: small disagreements will be recorded
without blocking a forward-led decision, while substantial disagreements will
be flagged for explicit user review before a divergent branch is accepted.

No training campaign or heavy `TE Curve Verification Pipeline` run is planned
by this document. Any future reduced-candidate pipeline must be planned and
approved separately before execution.

## Technical Approach

The report will be evidence-first and will use current repository artifacts,
not memory, as the decision source. The analysis will inspect:

- official `TE Curve Verification Pipeline` decision reports;
- dataset-surface validation reports for `polished_dataset` and
  `simplified_dataset`;
- campaign results reports for completed waves and polished retraining;
- program registries and family-level best entries where they provide scalar
  and artifact-size context;
- the current TE model backlog and status ledgers.

The decision framework will classify each forward/backward model family into
one of these operational states:

- `continue`: keep as an active candidate for the next reduced evaluation;
- `baseline-only`: keep as a comparison baseline, but do not extend;
- `pause`: retain artifacts and documentation, but exclude from near-term
  training and reduced-pipeline candidate sets;
- `retire`: stop considering for future TE model development unless a later
  report reopens it with new evidence.

The report will prioritize simple, deployable, and curve-promising families.
It will penalize models that are heavier without a clear curve or scalar gain,
models that repeatedly underperform across forward and backward, and models
whose advantages are diagnostic rather than deployable.

The `global` surface will be explicitly paused in the report and in the
backlog. It will be excluded from the current pruning decisions and reserved
for the final backlog stage, when all other priority work is complete.

No subagent is planned. If a subagent becomes useful later for independent
report review, the proposed subagent, scope, and approval requirement must be
recorded before launch and explicitly approved by the user.

## Involved Components

Planned read-only evidence sources:

- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/reports/analysis/model_development_waves/`
- `doc/reports/campaign_results/`
- `output/registries/`
- `output/validation_checks/`

Planned authored outputs after approval:

- a new analysis report under `doc/reports/analysis/model_development_waves/`
  or `doc/reports/analysis/te_curve_verification_pipeline/`, with the final
  location chosen from the inspected report taxonomy;
- an update to `doc/running/te_model_live_backlog.md` recording that `global`
  model selection is paused until the final backlog stage.

Protected-file check:

- `doc/running/active_training_campaign.yaml` currently records the
  polished-dataset `TE Curve Verification Pipeline` refresh as completed.
- The protected file list belongs to that closed refresh and does not include
  the planned pruning report or `doc/running/te_model_live_backlog.md`.
- The planned work must not edit the listed protected refresh files without a
  separate explicit approval.

## Implementation Steps

1. Obtain explicit user approval for this technical document.
2. Inventory the current official and dataset-surface report artifacts.
3. Extract forward/backward scalar, curve-first, complexity, deployment, and
   evidence-status signals per model family.
4. Exclude `global` rows from near-term decisions and record the global pause
   policy in the decision report.
5. Define a compact scoring or tiering method that favors forward evidence,
   checks backward agreement, penalizes avoidable complexity, and preserves
   useful baselines.
6. Write the model-family pruning decision report with one decision and
   motivation per model family.
7. Update `doc/running/te_model_live_backlog.md` to pause `global` evaluation
   until it is the last remaining backlog item.
8. Run Markdown QA on the touched Markdown files:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
9. Report completion and wait for explicit commit approval.
