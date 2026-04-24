# Track 1 MLP Residual Cell Final Closure Campaign

## Overview

This technical document defines the next dedicated `Track 1` preparation step
for the exact-paper `MLP` family after the completed `MLP` family repair wave
reduced the accepted row to only `7` non-green cells across the canonical
full-matrix replication benchmark.

The user requested a follow-up `MLP` campaign that focuses only on the
remaining residual cells in the four canonical `Track 1` progress tables:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

At the current benchmark state, the accepted exact-paper `MLP` row remains
open only on:

- amplitude target `1` in `Table 2` and `Table 3`;
- amplitude target `156` in `Table 2`;
- amplitude target `240` in `Table 2` and `Table 3`;
- phase target `162` in `Table 4` and `Table 5`.

This work is campaign preparation only. No training execution is part of this
step until the user explicitly approves the prepared package.

## Technical Approach

The new wave should be materially narrower than the previous `324`-run
family-wide `MLP` campaign and should act as a final residual-cell closure
attempt for the four still-open exact-paper target pairs:

- amplitude `1`;
- amplitude `156`;
- amplitude `240`;
- phase `162`.

The preparation strategy is:

1. read the accepted `MLP` row from the canonical benchmark and confirm the
   exact residual-cell inventory;
2. collapse duplicated table entries into the four distinct family-target
   repair pairs listed above;
3. prepare a dedicated exact-paper `MLP` residual campaign that spends all
   compute budget only on those four pairs;
4. increase retry depth relative to the previous `27`-attempt-per-pair pattern
   by expanding the seed schedule while keeping the same exact-paper-safe MLP
   grid-search mode, so the remaining hard cells receive a stronger final
   search wave without introducing unsupported YAML-side estimator overrides;
5. preserve the repository's campaign-safe workflow:
   - exact-paper YAML queue files;
   - immutable run-instance outputs;
   - one dedicated PowerShell launcher;
   - one matching launcher note;
   - one updated active campaign state entry after approval.

The planning report should keep the mapping between target pairs and affected
tables explicit so later closeout can state whether each accepted promotion
closes one table or two tables at once.

No subagent is planned for this work. The task remains a repository-owned
campaign preparation flow in the main rollout.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/forward/`

After approval, the expected implementation outputs are:

- one new campaign planning report for the residual-cell `MLP` closure wave;
- one new exact-paper campaign config directory dedicated to the four residual
  `MLP` target pairs;
- one dedicated PowerShell launcher under
  `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one updated `doc/running/active_training_campaign.yaml` entry with the new
  prepared campaign metadata and launch command.

## Implementation Steps

1. Re-read the canonical benchmark and confirm the current residual `MLP`
   cells on Tables `2-5`.
2. Convert those cells into the deduplicated exact-paper target-pair inventory
   of `A1`, `A156`, `A240`, and `P162`.
3. Define a stronger residual retry matrix and total queue size for one
   overnight-ready final `MLP` closure attempt.
4. Create the campaign planning report with target inventory, attempt matrix,
   and total run count.
5. Generate the exact-paper YAML files under a dedicated residual `MLP`
   campaign folder.
6. Create the dedicated PowerShell launcher and the matching launcher note.
7. Update `doc/running/active_training_campaign.yaml` with the prepared
   campaign metadata and launch command.
8. Run repository Markdown warning checks on the touched Markdown scope before
   closing the preparation step.
