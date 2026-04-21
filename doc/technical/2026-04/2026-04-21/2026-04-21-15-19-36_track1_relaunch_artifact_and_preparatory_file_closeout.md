# Track 1 Relaunch Artifact And Preparatory File Closeout

## Overview

This technical document defines the repository cleanup and consolidation pass
for the completed `Track 1` open-cell full-matrix relaunch package that was
used after the first wrapper crash.

The closeout commit already published the canonical campaign-results surface:
the final Markdown report, the validated PDF, the refreshed `Track 1`
benchmark, the refreshed training master summary, the completed
`active_training_campaign.yaml` state, and the aggregate plus family-level
winner-bookkeeping artifacts.

What remains outside Git is the relaunch preparation and execution surface that
made that closeout possible:

- the family campaign YAML directories under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`;
- the family and aggregate launchers under
  `scripts/campaigns/track1/exact_paper/`;
- the matching launcher notes under `doc/scripts/campaigns/`;
- the raw relaunch validation artifacts under
  `doc/reports/analysis/validation_checks/` and
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`.

This task will close that relaunch surface as a repository-owned artifact set
so the preparation package, the execution package, and the validation evidence
for the completed relaunch are all versioned consistently. The earlier missing
`MLP` artifact-recovery problem from the first launch is explicitly out of
scope for this pass and will be handled later as a separate task.

No subagent is planned or authorized for this work.

## Technical Approach

The repository already contains the canonical semantic closeout of the relaunch
wave. This pass will align the still-untracked relaunch preparation assets with
that canonical closeout instead of generating new scientific results.

The implementation will:

1. verify that the untracked relaunch files are exactly the expected campaign
   preparation, launcher, note, and validation-artifact surfaces tied to the
   completed `2026-04-20-23-50-13` wave;
2. inspect the aggregate and family launcher set to ensure the final file set
   is internally consistent with the planning report and with the executed
   relaunch path, including the dedicated `resume_after_mlp` aggregate wrapper;
3. inspect the generated campaign YAML directories to confirm that they are the
   prepared exact-paper relaunch inputs and not unrelated campaign residue;
4. check whether any touched technical or campaign index file still needs
   normalization so the relaunch package is documented cleanly;
5. run Markdown QA on every touched authored Markdown file;
6. stage the relaunch package in a dedicated follow-up commit that complements
   the already-published canonical closeout commit.

The raw validation artifacts will be treated as part of the relaunch evidence
surface because they document the completed family retries that underlie the
accepted closeout reconstruction. The missing first-launch `MLP` artifact
recovery will not be approximated or backfilled during this pass.

## Involved Components

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-20-23-50-13_track1_open_cell_full_matrix_closure_campaigns_plan_report.md`
- `doc/running/active_training_campaign.yaml`
- `doc/scripts/campaigns/run_track1_open_cell_full_matrix_closure_campaigns.md`
- `doc/scripts/campaigns/run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.md`
- `doc/scripts/campaigns/run_track1_mlp_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_rf_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_dt_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_et_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_ert_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_gbm_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_hgbm_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_xgbm_open_cell_full_matrix_closure_campaign.md`
- `doc/scripts/campaigns/run_track1_lgbm_open_cell_full_matrix_closure_campaign.md`
- `scripts/campaigns/track1/exact_paper/run_track1_open_cell_full_matrix_closure_campaigns.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_mlp_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_rf_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_dt_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_et_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_ert_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_gbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_hgbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_xgbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_lgbm_open_cell_full_matrix_closure_campaign.ps1`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-20_track1_*_open_cell_full_matrix_closure_campaign/`
- `doc/reports/analysis/validation_checks/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/technical/2026-04/2026-04-20/README.md`

## Implementation Steps

1. Enumerate the untracked relaunch YAML, launcher, note, and validation
   artifact surfaces and verify that they all map to the completed relaunch
   wave.
2. Normalize or repair any small repository-owned documentation/index issue
   needed to make the relaunch package self-consistent.
3. Stage the relaunch preparation files:
   campaign YAML directories, PowerShell launchers, and launcher notes.
4. Stage the relaunch validation artifacts that correspond to the completed
   retry wave under the canonical validation roots.
5. Run Markdown QA on every touched authored Markdown file.
6. Report the exact staged scope before asking for the final commit approval.
