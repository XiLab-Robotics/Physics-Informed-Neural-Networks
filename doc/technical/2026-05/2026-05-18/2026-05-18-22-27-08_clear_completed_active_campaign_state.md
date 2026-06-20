# Clear Completed Active Campaign State

## Overview

This document plans the cleanup of `doc/running/active_training_campaign.yaml`
after the RCIM Model-Bank Reproduction bidirectional paper-faithful grid-search campaign completed.
The user confirmed that the campaign is finished and approved removing it from
the running state so the files listed in `protected_file_list` are no longer
locked by the active-campaign guard.

The current state already records:

- `status: completed`;
- `pending_family_list: []`;
- `finished_at: '2026-05-16T19:04:25+02:00'`;
- `completion_recorded_at: '2026-05-16T20:20:45+02:00'`;
- a canonical results report at
  `doc/reports/campaign_results/track_1/exact_paper/backward/2026-05-16-20-07-07_track1_backward_paper_faithful_grid_search_closeout_report.md`;
- the expected campaign output directory under
  `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/`.

## Technical Approach

Keep `doc/running/active_training_campaign.yaml` as the canonical state-file
entry point, but replace the completed campaign payload with an explicit
`status: none` record. This preserves tooling expectations that the file exists
while removing active protected-file locks.

The replacement state will retain only a compact pointer to the last cleared
completed campaign and the closeout report. It will set `protected_file_list`
to an empty list.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/running/README.md`
- `doc/README.md`
- Current RCIM Model-Bank Reproduction paper-faithful campaign output under
  `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/`
- Planning report:
  `doc/reports/campaign_plans/track_1/exact_paper/2026-05-13-17-33-38_track1_paper_faithful_elm_queue_addendum_plan_report.md`

## Implementation Steps

1. Confirm the active campaign status is `completed`, has no pending families,
   and points to an existing output directory.
2. Replace `doc/running/active_training_campaign.yaml` with a compact
   `status: none` state and an empty `protected_file_list`.
3. Update `doc/running/README.md` to document `status: none`.
4. Register this technical document from `doc/README.md`.
5. Run Markdown checks on touched Markdown files.
6. Leave Git commit creation for a separate explicit approval.

No subagent use is planned for this change.
