# Track 1 Overnight Open-Cell Full-Matrix Closure Campaigns

## Overview

This technical document defines the next `Track 1` training wave after the
scope clarification that made the four full-matrix replication tables the only
canonical progress surface for `Track 1`.

The requested goal is to prepare a new overnight training package that targets
only the still-open cells in:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The user confirmed that `Track 1` should now be interpreted as the exact-paper
family-bank implementation branch, with completion defined as `19` accepted
models for each of the `10` algorithm families and with harmonic-wise work
postponed to a separate follow-up branch.

The intended execution window is an overnight run budget of approximately
`700-800` training jobs in total.

## Technical Approach

The new wave should stay fully aligned with the canonical `Track 1` reading:

1. use only the still-open full-matrix cells as the training target surface;
2. avoid spending overnight budget on cells that are already green in the
   canonical benchmark;
3. preserve the repository pattern already validated by the earlier
   residual-cell closure wave:
   - family-local campaign grouping;
   - target-local exact-paper configs;
   - aggregate launcher plus family launchers;
   - hybrid local/remote launch mode;
   - canonical campaign planning and campaign state recording;
4. scale the retry budget to the user's requested overnight capacity, targeting
   roughly `700-800` training jobs across the still-open family-target cells.

The practical design target is a new exact-paper closure package that:

- enumerates the current non-green cells across `Table 2-5`;
- maps those cells to family-target training configs;
- assigns a retry count per cell that stays within the overnight budget;
- produces dedicated family campaign bundles plus one aggregate sequential
  launcher.

The preferred planning logic is:

- prioritize harmonics already called out in the canonical benchmark as still
  concentrated open areas;
- bias more retry budget toward cells that are still red before yellow cells;
- preserve inspectability by keeping every training config target-specific and
  family-explicit.

No subagent is planned for this work. The task is a repository-owned campaign
preparation flow and remains in the main rollout.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/forward/`

The implementation is expected to create after approval:

- one new campaign planning report under
  `doc/reports/campaign_plans/track1/exact_paper/`;
- one new exact-paper campaign config folder under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`;
- family-local launchers under `scripts/campaigns/track1/exact_paper/`;
- matching launcher notes under `doc/scripts/campaigns/`;
- one aggregate launcher;
- one refreshed `active_training_campaign.yaml` entry for the prepared wave.

## Implementation Steps

1. Re-read the canonical benchmark and enumerate only the still-open
   full-matrix cells in `Table 2-5`.
2. Convert that open-cell inventory into a family-target training queue for the
   exact-paper family bank.
3. Allocate retry counts so the total queue stays within the requested
   overnight budget of about `700-800` training jobs.
4. Create the campaign planning report with the final queue definition and
   compute budget.
5. Generate the campaign YAML files for each family-target retry job.
6. Create the family-local and aggregate PowerShell launchers plus the matching
   launcher notes.
7. Update `doc/running/active_training_campaign.yaml` with the prepared
   campaign state and exact launch commands.
8. Run repository Markdown warning checks on the touched Markdown scope.
