# Track 1 Remaining Family Cellwise Reference Campaigns Plan Report

## Overview

This planning report prepares the next `Track 1` exact-paper wave after the
completed remaining-family full-matrix batch.

The new goal is more ambitious and more granular than the just-finished
row-level campaign:

- reproduce the `SVM` closure pattern for every remaining paper family;
- train one model per paper cell rather than one family model for the whole
  amplitude or phase matrix;
- archive the accepted target-specific models as the canonical family reference
  inventory;
- make every family reconstructible through the same `onnx/`, `python/`,
  dataset-snapshot, and provenance workflow already formalized for `SVM`.

The remaining families are:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

## Objective

Prepare a minimum exact-paper campaign surface of `171` target-specific runs:

- `9` families;
- `10` amplitude targets per family;
- `9` phase targets per family.

This is the smallest campaign wave that fully mirrors the accepted `SVM`
reference-model strategy across every still-open `Track 1` family.

## Canonical Cell Inventory

Amplitude target list:

- `A_0`
- `A_1`
- `A_3`
- `A_39`
- `A_40`
- `A_78`
- `A_81`
- `A_156`
- `A_162`
- `A_240`

Phase target list:

- `phi_1`
- `phi_3`
- `phi_39`
- `phi_40`
- `phi_78`
- `phi_81`
- `phi_156`
- `phi_162`
- `phi_240`

## Shared Exact-Paper Settings

The cellwise wave should preserve the same exact-paper baseline settings
already validated in the repository:

| Setting | Value |
| --- | --- |
| Dataset | `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv` |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| `test_size` | `0.20` |
| `random_seed` | `0` |
| `deterministic` | `true` |
| `threadpool_limit` | `1` |
| Training Mode | `exact-paper single-target family run` |
| Export | `ONNX enabled` plus Python-usable fitted estimator persistence |
| Validation Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |

These settings must stay fixed across the whole `171`-run wave so that family
comparison remains attributable to model-family behavior rather than split or
schema drift.

## Campaign Packaging Principle

The new wave should be split by family, not launched as one `171`-YAML flat
queue with no structure.

Each family package should contain:

- one campaign-local `README.md`;
- `19` YAML files, one per target cell;
- one family launcher:
  `scripts/campaigns/track1/exact_paper/run_track1_<family>_cellwise_reference_campaign.ps1`;
- one launcher note:
  `doc/scripts/campaigns/run_track1_<family>_cellwise_reference_campaign.md`.

The aggregate orchestration layer should contain:

- `scripts/campaigns/track1/exact_paper/run_track1_remaining_family_cellwise_reference_campaigns.ps1`
- `doc/scripts/campaigns/run_track1_remaining_family_cellwise_reference_campaigns.md`

Hybrid launcher rule:

- default path: local execution;
- remote path: enabled by `-Remote`;
- remote parameters:
  - `RemoteHostAlias`
  - `RemoteRepositoryPath`
  - `RemoteCondaEnvironmentName`

## Candidate Family Campaign Set

| Campaign ID | Family | Run Count | Archive Target | Primary Goal |
| --- | --- | ---: | --- | --- |
| `1` | `MLP` | `19` | `mlp_reference_models` | recover best possible cellwise surface |
| `2` | `RF` | `19` | `rf_reference_models` | promote archive-grade amplitude and phase cells |
| `3` | `DT` | `19` | `dt_reference_models` | isolate strong single-target cells from weak row behavior |
| `4` | `ET` | `19` | `et_reference_models` | isolate strong single-target cells from weak row behavior |
| `5` | `ERT` | `19` | `ert_reference_models` | push one of the strongest remaining tree families into archive form |
| `6` | `GBM` | `19` | `gbm_reference_models` | promote strong phase cells and best amplitude recoveries |
| `7` | `HGBM` | `19` | `hgbm_reference_models` | recover high-potential amplitude and phase cells |
| `8` | `XGBM` | `19` | `xgbm_reference_models` | verify boosted-tree target strengths after recovery fixes |
| `9` | `LGBM` | `19` | `lgbm_reference_models` | promote the strongest non-SVM amplitude envelope into archive form |

## Cellwise Run Naming Rule

Each target-specific run should make the family, target kind, and harmonic
explicit.

Recommended run-name pattern:

- amplitude:
  `track1_<family>_amplitude_<harmonic>_cellwise_reference`
- phase:
  `track1_<family>_phase_<harmonic>_cellwise_reference`

Example names:

- `track1_rf_amplitude_162_cellwise_reference`
- `track1_rf_phase_240_cellwise_reference`
- `track1_lgbm_amplitude_40_cellwise_reference`
- `track1_lgbm_phase_81_cellwise_reference`

## Candidate Run Matrix

| Family | Amplitude Runs | Phase Runs | Total |
| --- | --- | --- | ---: |
| `MLP` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `RF` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `DT` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `ET` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `ERT` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `GBM` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `HGBM` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `XGBM` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |
| `LGBM` | `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`, `A_240` | `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`, `phi_156`, `phi_162`, `phi_240` | `19` |

## Planned Launcher Inventory

Per-family launchers to generate after approval:

| Family | Intended Launcher |
| --- | --- |
| `MLP` | `run_track1_mlp_cellwise_reference_campaign.ps1` |
| `RF` | `run_track1_rf_cellwise_reference_campaign.ps1` |
| `DT` | `run_track1_dt_cellwise_reference_campaign.ps1` |
| `ET` | `run_track1_et_cellwise_reference_campaign.ps1` |
| `ERT` | `run_track1_ert_cellwise_reference_campaign.ps1` |
| `GBM` | `run_track1_gbm_cellwise_reference_campaign.ps1` |
| `HGBM` | `run_track1_hgbm_cellwise_reference_campaign.ps1` |
| `XGBM` | `run_track1_xgbm_cellwise_reference_campaign.ps1` |
| `LGBM` | `run_track1_lgbm_cellwise_reference_campaign.ps1` |

Aggregate sequential launcher to generate after approval:

- `run_track1_remaining_family_cellwise_reference_campaigns.ps1`

## Intended Launch Commands

These are planned commands only. They become real repository commands only
after the approved implementation generates the launcher set.

Local form:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_mlp_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_rf_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_dt_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_et_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_ert_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_gbm_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_hgbm_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_cellwise_reference_campaign.ps1
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_cellwise_reference_campaigns.ps1
```

Remote form:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_mlp_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_rf_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_dt_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_et_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_ert_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_gbm_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_hgbm_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_cellwise_reference_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_cellwise_reference_campaigns.ps1 -Remote
```

## Expected Closeout Consequences

If the wave is approved and later executed, each family closeout is expected to
perform more than a normal campaign report refresh.

Each successful family closure should also:

- update accepted family cells in `RCIM Paper Reference Benchmark.md`;
- refresh the colored family-by-family `Tables 2-5` when accepted values
  improve;
- refresh `Training Results Master Summary.md`;
- serialize campaign winner artifacts;
- create or extend the family archive under
  `models/paper_reference/rcim_track1/<family>_reference_models/`;
- pin the accepted family inventory in a dedicated benchmark section, as
  already done for `SVM`.

## Why This Wave Is The Correct Next Step

The completed full-matrix row campaigns improved the benchmark, but they still
left the project far from `Track 1` closure.

The main reason is structural:

- row-wise family runs dilute target-specific strengths;
- several families have clear strong cells hidden inside weak aggregate rows;
- `SVM` already proved that target-specific canonicalization is the right
  archive-grade closure pattern.

This `171`-run cellwise wave is therefore the first remaining-family campaign
that is directly aligned with the accepted end state rather than only with
intermediate row-level diagnostics.

## Execution Gate

Before any YAML package or launcher is generated:

1. the technical document must be approved;
2. this planning report must be approved;
3. the `171`-run family-by-family cellwise campaign strategy must be accepted.

After approval, the implementation phase should generate the actual family
campaign packages, hybrid launchers, launcher notes, persistent campaign state,
and the exact runnable terminal commands.
