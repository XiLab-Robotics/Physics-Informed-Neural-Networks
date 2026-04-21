# Remote Wrapper Report Path Fix And Track1 Relaunch Preparation

## Overview

This document covers the recovery work after the overnight `Track 1`
`open_cell_full_matrix` campaign appeared to crash during the first `MLP`
family launcher.

The log analysis shows that the actual `MLP` family batch completed all
`297/297` configured runs. The failure happened later in the remote wrapper
artifact-reconciliation phase, where the wrapper searched for generated
Markdown validation reports under a stale path:

- expected by wrapper:
  `doc/reports/analysis/validation_checks/track1/exact_paper/`
- actually produced by the validation script during this wave:
  `doc/reports/analysis/validation_checks/`

The practical consequence is that the aggregate overnight launcher stopped
after `MLP`, so the later family launchers were not executed even though the
remote `MLP` run itself finished successfully.

## Technical Approach

The recovery should be split into two tightly scoped parts.

Part `1`: repair the remote exact-paper wrapper so the artifact lookup matches
the real report-output path produced by the validation script.

Part `2`: prepare a relaunch path that starts from the first not-yet-executed
family launcher instead of replaying the already completed `MLP` batch.

The wrapper repair should prefer the repository's current canonical output path
and should not rely on historical report locations. The failure surface should
also become more explicit so a future mismatch shows both the expected search
root and the actual discovered candidate paths.

The relaunch package should preserve the existing prepared campaign identity
but should expose a restart entry point that skips `MLP` and continues with:

- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

Because `doc/running/active_training_campaign.yaml` is currently protected by
the active campaign workflow, any status update from `active` to an
interrupted/relaunch-prepared state must be treated as an explicitly approved
protected-file edit.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_open_cell_full_matrix_closure_campaigns.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_rf_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_dt_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_et_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_ert_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_gbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_hgbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_xgbm_open_cell_full_matrix_closure_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_lgbm_open_cell_full_matrix_closure_campaign.ps1`
- `doc/scripts/campaigns/run_track1_open_cell_full_matrix_closure_campaigns.md`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-20-23-50-13_track1_open_cell_full_matrix_closure_campaigns_plan_report.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Confirm the exact mismatch between the remote wrapper search root and the
   real validation report output root.
2. Repair `run_exact_paper_campaign_remote.ps1` so it resolves the current
   exact-paper validation report path correctly.
3. Harden the remote wrapper diagnostics so future path mismatches show the
   searched roots and any discovered candidate report files.
4. Prepare a relaunch entry point that resumes from the first family not yet
   executed after the completed `MLP` batch.
5. Update the matching launcher note and any planning wording that still
   implies a clean full replay instead of a post-`MLP` relaunch.
6. If explicitly approved, update the protected
   `doc/running/active_training_campaign.yaml` state to reflect the interrupted
   first launch and the prepared relaunch baseline.
7. Run Markdown QA on every touched repository-owned Markdown file.
