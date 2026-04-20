# Track 1 Remaining Family Residual Cellwise Closure Campaigns Plan Report

## Overview

This planning report prepares an aggressive overnight `Track 1` exact-paper
closure wave for the nine non-`SVM` families:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The completed `171`-run cellwise batch already materialized the canonical
reference banks for these families. The next wave is therefore not about
coverage. It is about closing the remaining `ðŸŸ¡` and `ðŸ”´` cells against the
paper.

## Objective

Prepare a high-pressure residual-cell closure campaign that:

- targets only family-target pairs that are still above the paper threshold in
  Tables `2`, `3`, `4`, and `5`;
- keeps the accepted exact-paper family implementations unchanged;
- spends an overnight runtime budget roughly `6-7x` the just-finished
  `171`-run pass;
- maximizes the chance of turning current `ðŸŸ¡/ðŸ”´` cells into `ðŸŸ¢`.

## Campaign Strategy

The previous wave proved that a single reference run per family-target pair is
not enough to close the remaining surface.

The new wave should therefore introduce a `closure-attempt bundle` for every
still-open family-target pair.

Each bundle should contain multiple exact-paper-safe retry variants, such as:

- denser target-local hyperparameter grids;
- wider but still disciplined search around the currently accepted winner;
- deterministic reruns with alternate split or retry seeds when still
  consistent with the benchmark protocol;
- family-specific closure bundles tuned for the target kind:
  - amplitude residual bundle;
  - phase residual bundle.

## Proposed Runtime Budget

The overnight budget should be intentionally aggressive.

Recommended operating envelope:

| Budget Level | Approximate Run Count | Interpretation |
| --- | ---: | --- |
| `Conservative` | `~700` | enough for targeted retries, but not really an overnight push |
| `Recommended` | `~950` | strong closure pressure with meaningful variant depth |
| `Maximum Planned` | `~1100` | full overnight push still within the requested `6-7x` budget |

Recommended default for this wave:

- target budget: `~950-1050` runs;
- preferred design point: `~1000` runs.

This keeps the wave large enough to justify the overnight slot without becoming
an unstructured brute-force sweep.

## Variant Depth Rule

Per unresolved family-target pair, the default retry depth should be:

- `10` closure variants for standard yellow cells;
- `12` closure variants for the most stubborn yellow-to-red cells;
- optional `14` closure variants for explicitly designated high-priority red
  blockers.

High-priority blockers remain concentrated around:

- `0`
- `1`
- `3`
- `156`
- `162`
- `240`

## Family Packaging Principle

The new wave should stay grouped by family and should not be flattened into one
opaque queue.

Each family package should expose:

- one family campaign `README.md`;
- one YAML per closure attempt;
- one family launcher:
  `run_track1_<family>_residual_cellwise_closure_campaign.ps1`;
- one launcher note:
  `doc/scripts/campaigns/run_track1_<family>_residual_cellwise_closure_campaign.md`.

The aggregate orchestration layer should expose:

- `run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1`;
- `doc/scripts/campaigns/run_track1_remaining_family_residual_cellwise_closure_campaigns.md`.

All launchers should follow the repository hybrid standard:

- default: local;
- remote: `-Remote`;
- remote parameters:
  - `RemoteHostAlias`
  - `RemoteRepositoryPath`
  - `RemoteCondaEnvironmentName`

## Exact-Paper Safety Constraints

The closure wave must preserve:

| Setting | Value |
| --- | --- |
| Dataset | same exact-paper recovered dataframe |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Export Policy | ONNX plus Python-usable fitted estimator persistence |
| Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |
| Family Identity | unchanged |
| Benchmark Surface | canonical Tables `2-5` and Table `6` |

This means the campaign is allowed to vary search effort, retry depth, and
target-local closure bundles, but not to change the accepted family algorithm.

## Candidate Campaign Set

| Campaign ID | Family | Intended Scope | Target Type |
| --- | --- | --- | --- |
| `1` | `MLP` | residual closure bundle | unresolved amplitude and phase targets |
| `2` | `RF` | residual closure bundle | unresolved amplitude and phase targets |
| `3` | `DT` | residual closure bundle | unresolved amplitude and phase targets |
| `4` | `ET` | residual closure bundle | unresolved amplitude and phase targets |
| `5` | `ERT` | residual closure bundle | unresolved amplitude and phase targets |
| `6` | `GBM` | residual closure bundle | unresolved amplitude and phase targets |
| `7` | `HGBM` | residual closure bundle | unresolved amplitude and phase targets |
| `8` | `XGBM` | residual closure bundle | unresolved amplitude and phase targets |
| `9` | `LGBM` | residual closure bundle | unresolved amplitude and phase targets |

## Candidate Attempt Naming Rule

Recommended attempt-name pattern:

- amplitude:
  `track1_<family>_amplitude_<harmonic>_closure_attempt_<index>`
- phase:
  `track1_<family>_phase_<harmonic>_closure_attempt_<index>`

Examples:

- `track1_rf_amplitude_162_closure_attempt_03`
- `track1_gbm_phase_156_closure_attempt_11`
- `track1_lgbm_amplitude_240_closure_attempt_08`

## Planned Launch Commands

These commands are planned only. They become real repository commands after the
approved implementation generates the launcher package.

Per-family remote form:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_mlp_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_rf_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_dt_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_et_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_ert_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_gbm_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_hgbm_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_residual_cellwise_closure_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_residual_cellwise_closure_campaign.ps1 -Remote
```

Aggregate overnight remote form:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1 -Remote
```

## Expected Post-Campaign Obligations

The closeout for this wave must update:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `Tables 2-5` family-by-family marker matrices
- harmonic-level Table `6` closure interpretation
- family and aggregate winner bookkeeping
- final Markdown plus validated PDF results report

If the wave materially improves any family enough to justify archive promotion,
the corresponding
`models/paper_reference/rcim_track1/<family>_reference_models/`
inventory should also be updated.
