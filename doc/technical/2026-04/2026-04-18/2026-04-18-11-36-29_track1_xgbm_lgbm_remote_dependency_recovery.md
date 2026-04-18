# Track 1 XGBM LGBM Remote Dependency Recovery

## Overview

This technical document formalizes the recovery path for the interrupted
remaining-family `Track 1` batch after the remote `XGBM` launcher failed on
`2026-04-18`.

The crash evidence is explicit: the remote Conda environment
`standard_ml_lan_node` does not currently expose the optional Python package
required by the repository-owned exact-paper `XGBM` workflow. The failing
traceback stopped at:

- `create_exact_paper_base_estimator("XGBM")`
- `_assert_optional_dependency(XGBRegressor, "xgboost")`

with the assertion:

`Required dependency is missing for exact paper reimplementation | xgboost.`

This means the interruption is not currently a model-quality issue and not a
YAML-package issue. It is an environment-preflight gap in the hybrid remote
campaign launcher.

The recovery work therefore has two tightly scoped goals:

1. harden the remote exact-paper launcher so optional family dependencies are
   checked before the expensive remote sync-and-run stage proceeds;
2. prepare a narrow recovery rerun package for the only two pending families:
   `XGBM` and `LGBM`.

No subagent use is planned for this implementation.

## Technical Approach

The repository already handles optional exact-paper families correctly inside
Python by asserting that `xgboost` or `lightgbm` is importable before building
the estimator. The weakness is that the remote PowerShell wrapper does not
surface this requirement until after the full source sync and launch step.

The recovery implementation should therefore:

1. add a remote optional-dependency preflight in
   `scripts/campaigns/run_exact_paper_campaign_remote.ps1`;
2. infer the required optional packages from the requested family names or run
   names;
3. verify those imports inside the same remote Conda environment used by the
   real training entrypoint;
4. fail early with a precise message naming the missing package and the family
   that requires it;
5. keep the existing exact-paper Python assertions as the final defensive
   layer rather than replacing them;
6. prepare a recovery campaign plan for rerunning only `XGBM` and `LGBM` after
   the remote environment is repaired.

The exact import surface matches the library documentation:

- `xgboost.XGBRegressor` from the `xgboost` Python package, documented by the
  official XGBoost Python-package guidance;
- `lightgbm.LGBMRegressor` from the `lightgbm` Python package, documented by
  the official LightGBM Python API guidance.

These library references were verified through Context7 before writing this
recovery plan.

## Involved Components

- `scripts/campaigns/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/run_track1_xgbm_full_matrix_campaign.ps1`
- `scripts/campaigns/run_track1_lgbm_full_matrix_campaign.ps1`
- `scripts/campaigns/run_track1_remaining_family_full_matrix_campaigns.ps1`
- `doc/scripts/campaigns/run_track1_xgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_lgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_remaining_family_full_matrix_campaigns.md`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/`
- remote Conda environment `standard_ml_lan_node`

## Implementation Steps

1. Create a dedicated recovery planning report for the pending `XGBM` and
   `LGBM` rerun package.
2. Add remote optional-dependency preflight logic to the hybrid exact-paper
   remote launcher.
3. Document the new remote preflight behavior in the affected launcher notes.
4. Prepare a narrow rerun handoff for the pending `XGBM` and `LGBM` campaigns.
5. After user approval and remote environment repair, rerun the pending
   campaigns and then perform the final closeout and benchmark refresh.
