# Track 1 Remaining Family Residual Cellwise Closure Campaigns

## Overview

This document prepares the next `Track 1` exact-paper closure wave after the
completed `171`-run remaining-family cellwise reference batch.

The previous wave successfully materialized the canonical `19`-model reference
banks for the nine non-`SVM` families, but the benchmark still contains many
`🟡` and `🔴` cells across the family rows in Tables `2`, `3`, `4`, and `5`.

The new objective is not another broad family refresh. It is an aggressive
overnight closure pass targeted only at the still-open family-target cells that
remain above the paper thresholds.

The requested operating constraint is also explicit:

- use the same exact-paper family implementations already accepted in the
  repository;
- keep the work family-by-family and cell-by-cell, like the accepted `SVM`
  workflow;
- spend a much larger overnight compute budget than the previous `171`-run
  pass;
- bias the campaign toward many closure attempts rather than conservative
  minimal reruns.

## Technical Approach

The correct strategy is an aggressive `residual-cell closure` campaign layer on
top of the already archived cellwise banks.

Instead of retraining the already-closed green cells, the new wave should:

1. extract the current non-green family-target surface from the canonical
   benchmark;
2. map each unresolved family-target pair to a dedicated retry bundle;
3. run multiple exact-paper-safe closure variants per unresolved target;
4. promote only those retry runs that improve the accepted benchmark row
   without violating the exact-paper family identity.

The retry budget should be intentionally large. A practical target is an
overnight wave in the order of `~900-1100` runs, which is roughly `6-7x` the
runtime budget of the just-finished `171`-run cellwise batch.

The proposed baseline envelope is:

- unresolved family-target pairs only;
- approximately `10-12` closure variants per unresolved pair;
- family-local packaging so that recovery and closeout remain inspectable;
- hybrid launchers with `-Remote` as the canonical overnight execution path.

Allowed variation space:

- denser exact-paper-faithful hyperparameter search grids;
- wider seed and split retries when still acceptable under the benchmark
  protocol;
- target-local retry bundles separated by amplitude versus phase scope;
- family-specific closure bundles where the family implementation remains the
  same and only the paper-faithful search effort increases.

Disallowed variation space:

- changing the model family identity;
- replacing exact-paper family logic with a different algorithm;
- blurring the provenance between already accepted reference-bank runs and the
  new closure-attempt runs;
- reopening already green cells just to spend extra runtime.

This campaign should therefore be read as:

- `same family`;
- `same paper-facing objective`;
- `more closure pressure`;
- `many more retries on the residual cells only`.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `output/training_campaigns/`
- `models/paper_reference/rcim_track1/`

The implementation is expected to create:

- one residual-closure package per family;
- one aggregate overnight launcher;
- closure-attempt YAML sets for every unresolved family-target pair;
- launcher notes aligned with the hybrid `-Remote` standard;
- a new active-campaign state entry in `doc/running/active_training_campaign.yaml`.

No subagent is planned for this task. The work is expected to stay in the main
rollout because the critical path is campaign-safe packaging and benchmark
alignment rather than a parallel sidecar analysis task.

## Implementation Steps

1. Quantify the current unresolved family-target surface from the canonical
   benchmark and freeze the retry inventory.
2. Create the campaign planning report with the closure-variant matrix and the
   targeted overnight run budget.
3. Wait for explicit user approval of both the technical document and the
   planning report.
4. After approval, generate the residual-closure YAML packages, hybrid family
   launchers, aggregate overnight launcher, and launcher notes.
5. Register the prepared campaign in
   `doc/running/active_training_campaign.yaml`.
6. After execution, perform full closeout with winner bookkeeping, benchmark
   refresh, `Tables 2-5` refresh, master-summary refresh, and validated PDF
   results reporting.
