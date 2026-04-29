# Track 1 Forward Maxi Remote Artifact Recovery And Closeout

## Overview

The forward-only exact-paper maxi campaign
`track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22`
appeared to fail locally because the SSH-backed remote wrapper lost the
`xilab-remote` connection.

Follow-up inspection showed that the remote workstation continued executing the
campaign well beyond the local wrapper failure and produced a large completed
artifact set under the remote repository clone. The next task is therefore not
to relaunch blindly, but to recover the full remote artifact surface into the
local repository and then perform the formal campaign closeout from the
recovered canonical local copy.

This task covers two strictly ordered stages:

1. full manual recovery of the campaign-owned remote artifacts;
2. formal closeout of the recovered campaign, including canonical benchmark
   refresh and persistent state reconciliation.

## Technical Approach

The workflow should treat the remote repository as the execution source of
truth and the local repository as the canonical bookkeeping surface.

The recovery stage should:

- inventory the remote campaign output tree, validation bundles, validation
  reports, and logs produced by the maxi campaign;
- copy back only the campaign-owned artifact surface rather than syncing the
  full remote repository;
- verify that the recovered local artifact set matches the real remote run
  inventory.

The closeout stage should then:

- update `doc/running/active_training_campaign.yaml` from the temporary local
  `cancelled` transport-failure state to the real recovered terminal state;
- generate the campaign results report from the recovered local artifact set;
- refresh the canonical forward benchmark surfaces in
  `RCIM Paper Reference Benchmark.md` and
  `Training Results Master Summary.md`;
- refresh the forward reference archive under
  `models/paper_reference/rcim_track1/forward/` if accepted winners improved;
- validate the required Markdown and PDF deliverables before considering the
  closeout complete.

No subagent use is planned for this recovery and closeout task. If delegation
becomes useful later, explicit user approval will be requested first.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `.temp/remote_training_campaigns/`
- `output/training_campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/`
- `doc/reports/analysis/validation_checks/`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/forward/`
- any current Track 1 closeout helper scripts under `scripts/reports/closeout/track1/`

## Implementation Steps

1. Inventory the remote artifact set actually produced by the maxi campaign and
   freeze the completed run count before copying anything locally.
2. Recover the full campaign-owned artifact surface from `xilab-remote` into
   the local repository.
3. Verify the recovered local artifact set against the remote inventory and
   identify any missing tail artifact before closeout.
4. Reconcile `doc/running/active_training_campaign.yaml` with the recovered
   real campaign outcome and the final results-report backlink.
5. Run the formal Track 1 closeout flow on the recovered local artifact set.
6. Refresh the canonical benchmark, master summary, and forward reference
   archive surfaces justified by the recovered accepted winners.
7. Validate the touched Markdown scope and the final PDF deliverable required
   by the campaign-results workflow.
