# Track 1 MLP Family Full-Matrix Repair Campaign

## Overview

This technical document defines the next dedicated `Track 1` preparation step
for the exact-paper `MLP` family after the recovered first-launch artifacts
were reconciled into the canonical local validation roots.

The user requested a new `MLP`-only campaign that tries to repair every
remaining non-green `MLP` cell in the canonical `Track 1` progress surface:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

At the current benchmark state, the exact-paper `MLP` family still has `21`
non-green cells across those four tables:

- `8` open amplitude `MAE` cells;
- `6` open amplitude `RMSE` cells;
- `4` open phase `MAE` cells;
- `3` open phase `RMSE` cells.

This work is campaign preparation only. No training execution is part of this
step until the user explicitly approves the prepared package.

## Technical Approach

The campaign should stay fully aligned with the repository's updated `Track 1`
closure rule, which now reads progress only from the four canonical
full-matrix replication tables and not from the postponed harmonic-wise branch.

The preparation strategy is:

1. read the current `MLP` row from the canonical benchmark and enumerate every
   yellow or red family-target cell;
2. collapse duplicate family-target pairs that are open in more than one table
   into one target-local training queue entry;
3. build a dedicated exact-paper `MLP` repair package whose only objective is
   to improve the family-internal `MLP` row, not the cross-family envelope;
4. size the retry matrix aggressively enough to attack all still-open `MLP`
   targets while keeping the queue practical for one overnight run;
5. preserve the already validated repository pattern:
   - exact-paper config YAML files;
   - immutable run-instance outputs;
   - one family-local launcher;
   - one matching launcher note;
   - one active campaign state entry;
   - remote-ready hybrid launch mode.

The open `MLP` target set should be treated as the union of still-open
family-target pairs across the four tables:

- amplitude targets: `0`, `1`, `3`, `39`, `40`, `81`, `156`, `240`
- phase targets: `1`, `3`, `39`, `162`

This yields `12` distinct `MLP` family-target pairs to repair. The planning
report should explicitly map each pair back to the affected benchmark tables so
that later closeout can distinguish which table statuses improved.

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

- one new campaign planning report for the `MLP` repair wave;
- one new exact-paper campaign config directory dedicated to the `MLP`
  family-only repair queue;
- one dedicated PowerShell launcher under
  `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one updated `doc/running/active_training_campaign.yaml` entry with the new
  prepared campaign state and launch command.

## Implementation Steps

1. Re-read the canonical benchmark and enumerate every current non-green
   `MLP` cell in Tables `2-5`.
2. Convert those cells into the deduplicated exact-paper `MLP` target-pair
   inventory.
3. Define the retry depth and total queue size for one overnight campaign.
4. Create the campaign planning report with the final target inventory,
   attempt matrix, and total run count.
5. Generate the exact-paper YAML files under a dedicated `MLP` campaign
   folder.
6. Create the dedicated PowerShell launcher and the matching launcher note.
7. Update `doc/running/active_training_campaign.yaml` with the prepared
   campaign metadata and launch command.
8. Run repository Markdown warning checks on the touched Markdown scope before
   closing the preparation step.
