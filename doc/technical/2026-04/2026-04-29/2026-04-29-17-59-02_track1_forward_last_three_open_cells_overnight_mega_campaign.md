# 2026-04-29-17-59-02 Track1 Forward Last Three Open Cells Overnight Mega Campaign

## Overview

This document prepares one overnight exact-paper `Track 1` forward-only mega
campaign after the completed
`track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21` closeout
failed to promote any new winners.

The canonical forward residual still contains exactly `3` non-green cells, all
on `Table 2 - Amplitude MAE Full-Matrix Replication`:

- `ERT ampl 156`
- `ERT ampl 240`
- `GBM ampl 162`

The implementation step after approval should therefore prepare one deeper
overnight campaign that keeps the same narrow pair inventory but increases the
retry budget materially into the low-hundreds range.

## Technical Approach

The campaign should reuse the same exact-paper forward repair workflow already
used by the previous residual waves, but it should stop pretending that one
more `84`-run micro-batch is enough.

The queue should stay pair-tight and benchmark-safe while increasing the search
depth substantially:

- `ERT ampl 156`: deep single-surface yellow retry tier
- `ERT ampl 240`: deepest stubborn single-surface retry tier
- `GBM ampl 162`: deep single-surface yellow retry tier

The intended implementation path after approval is:

1. create one planning report under `doc/reports/campaign_plans/`;
2. generate one dedicated config root under
   `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`;
3. generate one dedicated preparer and one dedicated remote launcher under
   `scripts/campaigns/track1/exact_paper/`;
4. generate the matching launcher note under `doc/scripts/campaigns/`;
5. update `doc/running/active_training_campaign.yaml` with the prepared queue;
6. after execution, run the normal forward closeout path and refresh the
   canonical reports and forward reference archives only if accepted winners
   improve.

No subagent use is planned for this task. If subagent delegation becomes
useful later, it must be proposed explicitly and approved before use.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/`
- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `models/paper_reference/rcim_track1/forward/`

## Implementation Steps

1. Freeze the canonical residual inventory for the last `3` forward non-green
   cells from the benchmark and latest closeout report.
2. Write the planning report with the exact pair inventory and proposed
   overnight retry budget in the low-hundreds range.
3. Wait for explicit user approval before generating any campaign YAML,
   launcher, launcher note, or campaign-state update.
4. After approval, implement the campaign package and surface the exact launch
   command.
