# Track 1 MLP First-Launch Artifact Recovery

## Overview

This technical document defines the recovery of the missing local repository
artifacts for the first `MLP` launch inside the completed `Track 1`
open-cell full-matrix closure wave.

The current repository state already reflects the canonical closeout decision
that the `MLP` retry wave was completed remotely but only partially
reconciled locally. The log evidence confirms the root issue:

- the first `MLP` family launcher completed the remote training batch;
- the remote wrapper then failed during artifact reconciliation when it could
  not find the generated validation report for
  `track1_mlp_amplitude_0_closure_attempt_07`;
- the relaunch later covered the non-`MLP` families only, leaving the original
  `MLP` artifact gap unresolved.

The remaining task is therefore not a retraining task. It is a local artifact
recovery and bookkeeping task for the already executed first-launch `MLP`
retry wave, currently quantified as `297` remotely completed runs whose local
validation artifacts were not fully synchronized into the canonical repository
layout.

No subagent is planned or authorized for this work.

## Technical Approach

The recovery will reconstruct the first-launch `MLP` retry wave from primary
campaign evidence rather than from inferred benchmark values.

The implementation will:

1. build the canonical inventory of the intended `MLP` retry runs from the
   approved campaign YAML package and the first-launch remote log;
2. extract the exact subset already synchronized locally before the wrapper
   stopped;
3. inspect the remote campaign root and related validation-report/output roots
   on the LAN workstation for the missing `MLP` artifacts;
4. resynchronize only the missing campaign-owned artifact set back into the
   canonical local repository paths:
   - `doc/reports/analysis/validation_checks/`
   - `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
   - any campaign-owned bookkeeping path still needed for deterministic review;
5. verify how many of the `297` intended runs become fully recoverable after
   the artifact pass;
6. prepare the repository so a later closeout refresh can safely reconsider
   `MLP` benchmark promotion based on real recovered artifacts.

This task intentionally stops short of a benchmark-refresh or report-rewrite
unless the recovered artifact set is first shown to be complete enough for a
trustworthy `MLP` post-closeout reconciliation. If the remote workstation no
longer contains the required first-launch artifacts, the task should report
that limitation explicitly instead of silently substituting a rerun.

## Involved Components

- `.temp/track1_open_cell_full_matrix_closure_campaigns_2026_04_20_23_50_13.log`
- `.temp/remote_training_campaigns/`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-20-23-50-13_track1_open_cell_full_matrix_closure_campaigns_plan_report.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-20_track1_mlp_open_cell_full_matrix_closure_campaign/`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `doc/reports/analysis/validation_checks/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- remote repository roots under:
  `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
- `doc/technical/2026-04/2026-04-21/README.md`
- `doc/README.md`

## Implementation Steps

1. Confirm the intended `MLP` first-launch run inventory and the exact local
   artifact shortfall.
2. Inspect the remote campaign and validation roots for the missing first-launch
   `MLP` artifacts.
3. Resynchronize the recoverable missing artifacts into the canonical local
   validation roots without relaunching training.
4. Recount the recovered-vs-missing `MLP` run surface after synchronization.
5. Record the recovery result and the remaining limitations, if any.
6. Run Markdown QA on the touched repository-authored Markdown files.
