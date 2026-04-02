# Formalize Feedforward Reference Baseline Run

## Overview

The repository currently contains two different feedforward run roles:

- infrastructure verification runs produced during the Wave 0 path and registry reorganization;
- historical feedforward campaign runs produced before the output-layout migration.

This creates a practical ambiguity: the newest run is not the best-performing run, while the best-performing run is stored under a migrated legacy run identifier.

Before starting Wave 1 model implementation, the project should explicitly formalize which already available feedforward run is the canonical reference baseline for future comparisons.

## Technical Approach

The formalization should keep the current numerical best run selected by the registry and make its project role explicit in the live operational documents.

The selected reference should be:

- the run currently identified by the registry best-selection policy;
- stable enough to be used as the baseline comparison target for future model families;
- documented separately from the Wave 0 `trial` run, which should remain classified as an infrastructure-verification artifact rather than as the best baseline result.

The implementation should therefore:

1. preserve the current best feedforward run as the canonical reference baseline;
2. record its exact artifact paths and selection rationale in the live backlog;
3. distinguish it clearly from the Wave 0 `trial` verification run;
4. align the next-step planning language so Wave 1 comparisons reference the canonical feedforward baseline instead of the verification run.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `README.md`
- `doc/README.md`
- `output/registries/families/feedforward/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`

## Implementation Steps

1. Read the current family and program registries to confirm the selected best feedforward run.
2. Update the live backlog so it explicitly names:
   - the current best implemented feedforward baseline run;
   - the registry files that certify that selection;
   - the Wave 0 `trial` run as verification-only evidence.
3. Keep the registry-selected run unchanged unless a new approved rerun supersedes it later.
4. Leave historical campaign reports untouched unless a wording change is needed in the active backlog.
