# Track 1 Remaining Exact-Paper Family Campaigns Plan Report

## Overview

This planning report prepares the next `Track 1` campaign wave after the
project-level acceptance of the `SVM` row.

The goal is to prepare dedicated exact-paper campaigns for the `9` remaining
paper-model families:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The requested outcome is not one large mixed launcher only. The user asked for:

- one runnable campaign path per remaining family;
- explicit terminal commands for each family campaign;
- one aggregate command that launches all `9` campaigns in sequence;
- and the ability to call the same `.ps1` locally by default or on the remote
  workstation through a `-Remote` switch.

## Current Evidence Base

The existing full-matrix exact-paper campaign already gives the baseline
difficulty and the current row-level status:

- strongest remaining families: `RF`, `ERT`, `GBM`, `HGBM`, `LGBM`;
- medium remaining families: `DT`, `ET`;
- weak remaining families: `XGBM`, `MLP`.

From the canonical benchmark:

- amplitude-side blockers remain concentrated on `156`, `162`, and `240`;
- phase-side blockers remain concentrated on `162` and `240`;
- `MLP` is materially off-paper and should be prepared as a benchmark-complete
  row, not as an expected near-closure branch;
- `RF`, `ERT`, `GBM`, `HGBM`, and `LGBM` are the most credible archive-grade
  candidates for the next family-closing passes.

## Campaign Principle

The remaining work should be split by family, not by one more all-family batch.

Each family campaign should include exactly two exact-paper runs:

- amplitude full-matrix reproduction for that family;
- phase full-matrix reproduction for that family.

This gives the user:

- simpler remote execution control;
- clearer failure isolation;
- easier future archive promotion family by family;
- one command per family plus one aggregate sequence command.

## Candidate Campaign Set

| Campaign ID | Family | Amplitude Run Name | Phase Run Name | Priority |
| --- | --- | --- | --- | --- |
| `1` | `MLP` | `track1_mlp_amplitude_full_matrix` | `track1_mlp_phase_full_matrix` | benchmark-complete |
| `2` | `RF` | `track1_rf_amplitude_full_matrix` | `track1_rf_phase_full_matrix` | high |
| `3` | `DT` | `track1_dt_amplitude_full_matrix` | `track1_dt_phase_full_matrix` | medium |
| `4` | `ET` | `track1_et_amplitude_full_matrix` | `track1_et_phase_full_matrix` | medium |
| `5` | `ERT` | `track1_ert_amplitude_full_matrix` | `track1_ert_phase_full_matrix` | high |
| `6` | `GBM` | `track1_gbm_amplitude_full_matrix` | `track1_gbm_phase_full_matrix` | high |
| `7` | `HGBM` | `track1_hgbm_amplitude_full_matrix` | `track1_hgbm_phase_full_matrix` | high |
| `8` | `XGBM` | `track1_xgbm_amplitude_full_matrix` | `track1_xgbm_phase_full_matrix` | medium |
| `9` | `LGBM` | `track1_lgbm_amplitude_full_matrix` | `track1_lgbm_phase_full_matrix` | high |

## Per-Family Campaign Package Rule

Every prepared family campaign should follow the same structure:

- campaign config directory containing:
  - `README.md`
  - `01_<family>_amplitude_full_matrix.yaml`
  - `02_<family>_phase_full_matrix.yaml`
- hybrid launcher:
  - `scripts/campaigns/track1/exact_paper/run_track1_<family>_full_matrix_campaign.ps1`
- launcher note:
  - `doc/scripts/campaigns/run_track1_<family>_full_matrix_campaign.md`

The aggregate sequential layer should add:

- `scripts/campaigns/track1/exact_paper/run_track1_remaining_family_full_matrix_campaigns.ps1`
- `doc/scripts/campaigns/run_track1_remaining_family_full_matrix_campaigns.md`

Hybrid launcher rule:

- default execution path: local machine;
- remote execution path: enabled by `-Remote`;
- remote parameters exposed only when `-Remote` is active:
  - `RemoteHostAlias`
  - `RemoteRepositoryPath`
  - `RemoteCondaEnvironmentName`

## Shared Exact-Paper Settings

Every family run should keep the same exact-paper baseline settings already
validated in the repository:

| Setting | Value |
| --- | --- |
| Dataset | `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv` |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| `test_size` | `0.20` |
| `random_seed` | `0` |
| `deterministic` | `true` |
| `threadpool_limit` | `1` |
| Export | `ONNX enabled` |
| Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |

Amplitude target scope:

- `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`,
  `A_240`

Phase target scope:

- `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`,
  `phi_162`, `phi_240`

## Intended Launcher Names

| Family | Intended Launcher |
| --- | --- |
| `MLP` | `run_track1_mlp_full_matrix_campaign.ps1` |
| `RF` | `run_track1_rf_full_matrix_campaign.ps1` |
| `DT` | `run_track1_dt_full_matrix_campaign.ps1` |
| `ET` | `run_track1_et_full_matrix_campaign.ps1` |
| `ERT` | `run_track1_ert_full_matrix_campaign.ps1` |
| `GBM` | `run_track1_gbm_full_matrix_campaign.ps1` |
| `HGBM` | `run_track1_hgbm_full_matrix_campaign.ps1` |
| `XGBM` | `run_track1_xgbm_full_matrix_campaign.ps1` |
| `LGBM` | `run_track1_lgbm_full_matrix_campaign.ps1` |

Aggregate sequential launcher:

- `run_track1_remaining_family_full_matrix_campaigns.ps1`

## Intended Launch Commands

These are the commands that should exist after the campaign package is
generated:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_mlp_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_rf_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_dt_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_et_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_ert_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_gbm_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_hgbm_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_full_matrix_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_full_matrix_campaign.ps1
```

Aggregate sequential command:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_full_matrix_campaigns.ps1
```

Remote variants that should also exist after generation:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_mlp_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_rf_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_dt_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_et_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_ert_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_gbm_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_hgbm_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_full_matrix_campaigns.ps1 -Remote
```

These commands are still planned commands at this stage. They become actual
repository commands only after the approved implementation step generates the
launchers.

Each generated launcher should follow the same remote operator pattern already
used by the accepted `SVM` remote campaign when `-Remote` is active:

- `RemoteHostAlias`
- `RemoteRepositoryPath`
- `RemoteCondaEnvironmentName`

so the user can launch all family campaigns on the remote workstation with the
same operational contract already validated in the repository.

## Why This Packaging Is Better Than One More 18-Run Umbrella

This split is operationally cleaner than repeating one all-family launcher:

- a family failure does not block interpretation of the other families;
- future archive promotion can happen family by family;
- the user can re-run one family without touching the other `8`;
- the aggregate sequential wrapper still preserves one-command convenience.

## Execution Gate

Before any YAML package or launcher is generated:

1. the technical document must be approved;
2. this planning report must be approved;
3. the family-by-family campaign split must be accepted as the canonical
   remaining `Track 1` preparation strategy.

After approval, the implementation phase should generate the actual campaign
artifacts and then provide the exact commands from the created files.
