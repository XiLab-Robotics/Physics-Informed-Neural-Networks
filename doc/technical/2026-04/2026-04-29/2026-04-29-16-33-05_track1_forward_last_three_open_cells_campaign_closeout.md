# 2026-04-29-16-33-05 Track1 Forward Last Three Open Cells Campaign Closeout

## Overview

This document gates the formal closeout of the completed exact-paper
`Track 1` forward-only campaign
`track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21`.

The campaign was prepared to repair the last `3` non-green forward cells after
the previous `last_four_open_cells` closeout reduced the residual forward
inventory from `4` to `3`.

Before the closeout can run, the profile-driven forward closeout helper must be
extended to recognize this new campaign name and its dedicated validation root.
After that extension, the normal forward closeout path should produce the
campaign results report, export and validate the PDF, refresh the canonical
benchmark/master-summary documents, refresh the forward reference archives if
accepted winners improve, and mark the persistent campaign state as completed.

## Technical Approach

The implementation should reuse the existing profile-driven closeout surface in
`scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
rather than introducing another one-off closeout script.

The expected sequence after approval is:

1. inspect `doc/running/active_training_campaign.yaml` and confirm that the
   campaign still owns the protected campaign state boundary;
2. add one new campaign profile entry for
   `track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21`,
   including the validation root
   `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells`
   and the run-name pattern for `_last_three_open_cells_attempt_`;
3. verify whether the campaign artifacts are already present locally or whether
   remote recovery from `xilab-remote` is still required;
4. run the canonical closeout path to generate the Markdown report, the PDF
   export, and the PDF validation evidence;
5. refresh
   `doc/reports/analysis/RCIM Paper Reference Benchmark.md` and
   `doc/reports/analysis/Training Results Master Summary.md`;
6. refresh the accepted forward paper-reference family archives as a mandatory
   closeout side effect if the new winners improve the tracked canonical
   results;
7. update `doc/running/active_training_campaign.yaml` from `running` to the
   final persisted state with the real completion timestamp and results-report
   path.

No subagent use is planned for this task. If subagent delegation becomes
useful, the proposed agent, its bounded scope, and the approval requirement
must be recorded and approved before use.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-29-14-28-06_track1_forward_last_three_open_cells_campaign_plan_report.md`
- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
- `output/training_campaigns/track1/exact_paper/forward_last_three_open_cells/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells/`
- `doc/reports/campaign_results/track1/exact_paper/`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/`

## Implementation Steps

1. Extend the forward closeout helper with one profile entry for the completed
   `last_three_open_cells` campaign.
2. Audit the artifact completeness for the `84`-run queue locally and recover
   missing remote artifacts only if the local set is incomplete.
3. Run the formal closeout to materialize the campaign results report.
4. Export the real PDF and validate it against the produced deliverable.
5. Refresh the canonical benchmark, master summary, and forward reference
   archives as required by the accepted winners.
6. Update the persistent campaign state and run Markdown QA on the touched
   repository-authored Markdown scope.
7. Report completion and wait for explicit commit approval instead of creating
   a commit automatically.
