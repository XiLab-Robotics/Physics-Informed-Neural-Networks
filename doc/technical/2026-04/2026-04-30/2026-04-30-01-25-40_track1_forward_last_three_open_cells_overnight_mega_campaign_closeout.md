# Track 1 Forward Last Three Open Cells Overnight Mega Campaign Closeout

## Overview

This document prepares the formal closeout of the completed remote original-
dataset exact-model-bank campaign
`track1_forward_last_three_open_cells_overnight_mega_campaign_2026-04-29_18_09_41`.

The campaign was launched to attack only the final `3` residual non-green
forward cells after the previous `84`-run wave failed to produce any
promotion. The closeout must now verify the produced artifact set, register the
campaign outcome canonically, refresh the forward paper-facing benchmark
surface, and update the forward family-reference archives if any accepted
winner improved over the archived entries.

At the start of this gate, the persistent campaign state in
`doc/running/active_training_campaign.yaml` still shows the campaign as
`prepared`, so the closeout must also reconcile the persisted lifecycle fields
with the completed real-world execution.

## Technical Approach

The closeout should reuse the profile-driven helper
`scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
instead of inventing a new one-off report path.

The implementation should:

- add one dedicated campaign profile for the overnight mega campaign;
- audit the local artifact surfaces under `output/training_campaigns/`,
  `output/validation_checks/`, and `doc/reports/analysis/validation_checks/`;
- recover remote artifacts only if the local campaign-owned set is incomplete;
- generate the final Markdown campaign-results report and the required PDF
  export;
- validate the real exported PDF;
- refresh the canonical `RCIM Paper Reference Benchmark.md` and `Training
  Results Master Summary.md`;
- refresh `models/paper_reference/rcim_track1/forward/` if the closeout
  promotes any accepted winner;
- update `doc/running/active_training_campaign.yaml` from the stale prepared
  state to the correct completed state with a real finish time and results
  report path.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  Canonical active-campaign state that must be reconciled during closeout.
- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
  Profile-driven closeout helper that needs the new campaign profile.
- `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells_overnight_mega/`
  Campaign execution logs and campaign-owned bookkeeping artifacts.
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells_overnight_mega/`
  Validation bundles that determine whether the queue completed successfully.
- `doc/reports/analysis/validation_checks/`
  Per-run Markdown validation reports for the overnight mega campaign.
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
  Canonical paper-facing benchmark that must reflect any accepted forward
  improvements.
- `doc/reports/analysis/Training Results Master Summary.md`
  Canonical always-updated program status summary.
- `models/paper_reference/rcim_track1/forward/`
  Mandatory forward archive surface to refresh when the closeout accepts new
  winners.

## Implementation Steps

1. Audit the local campaign-owned artifact set and determine whether remote
   recovery is needed.
2. Add the overnight mega campaign profile to the shared forward closeout
   helper.
3. Run the closeout helper to generate the Markdown campaign-results report.
4. Export the report PDF and validate the real PDF output.
5. Refresh the canonical forward benchmark and master summary surfaces.
6. Refresh the forward family-reference archives if the accepted winners
   changed.
7. Update `doc/running/active_training_campaign.yaml` to the correct completed
   lifecycle state.
8. Run Markdown QA on the touched Markdown scope and stop for explicit user
   approval before any commit.
