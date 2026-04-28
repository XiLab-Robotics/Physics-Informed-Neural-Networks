# Track 1 Forward Last Non-Green Cells Campaign Closeout

## Overview

This technical document defines the closeout scope for the completed
`track1_forward_last_non_green_cells_campaign_2026-04-28_11_36_05` wave.

The campaign was prepared as the final forward-only exact-paper retry package
for the last non-green amplitude target pairs still open across Tables `2-3`
after the earlier `forward_final_open_cells` closeout. The closeout must now
determine whether this last retry wave improved the accepted forward benchmark
surface, materialize the final campaign-results deliverables, refresh the
canonical benchmark summaries, and update the forward paper-reference archive
only where a newly accepted target winner truly improves over the archived
entry.

At the time this document is registered, the persistent campaign state still
marks the wave as `running`, while the observed validation artifact set already
matches the full prepared queue:

- queue size in active state: `108`
- observed validation bundle count under
  `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells/`:
  `108`

## Technical Approach

The closeout should follow the same governed path already used for the earlier
forward and bidirectional Track 1 exact-paper closeouts:

1. verify the completed artifact set and aggregate the accepted campaign
   winners;
2. run the repository-owned forward closeout utility against the active
   campaign state;
3. materialize the final campaign-results Markdown report and validate the
   PDF export;
4. refresh `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
5. refresh `doc/reports/analysis/Training Results Master Summary.md`;
6. refresh `models/paper_reference/rcim_track1/forward/` only for target-level
   accepted winners that improve over the stored archive entries;
7. update `doc/running/active_training_campaign.yaml` from `running` to
   `completed`, including the finished timestamp and report path.

The important success criterion is not only bookkeeping completion. The
important success criterion is whether the final forward non-green count drops
below the current `10`-cell residual surface and whether any remaining open
cells are now constrained to a smaller accepted target set than the pre-closeout
state recorded in the campaign plan.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-28-11-21-25_track1_forward_last_non_green_cells_campaign_plan_report.md`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/forward/`
- `output/training_campaigns/track1/exact_paper/forward_last_non_green_cells/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells/`
- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`

## Implementation Steps

1. Verify that the completed validation artifact count matches the prepared
   queue and confirm the active campaign identity.
2. Extend or reuse the existing forward closeout utility so it supports the
   `forward_last_non_green_cells` profile.
3. Run the closeout flow to generate campaign leaderboard and best-run
   bookkeeping artifacts plus the final campaign-results Markdown report.
4. Export and validate the styled PDF companion for the final report.
5. Review the benchmark deltas and refresh the directional paper-reference
   archive only where accepted winners improved.
6. Update the persistent active campaign state to `completed`.

No subagent use is planned for this closeout task. If subagent use becomes
desirable later, it must be proposed explicitly and approved before launch.
