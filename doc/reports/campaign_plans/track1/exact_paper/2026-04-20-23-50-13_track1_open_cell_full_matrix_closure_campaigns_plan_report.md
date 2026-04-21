# Track 1 Open-Cell Full-Matrix Closure Campaigns Plan Report

## Overview

This planning report prepares the next overnight `Track 1` exact-paper
closure wave after the repository focus change that makes Tables `2`-`5`
the only canonical progress surface for the track.

The campaign therefore targets only unresolved family-target pairs in the
four full-matrix replication tables:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The currently open full-bank surface reduces to `28` unresolved non-`SVM`
family-target pairs. This wave allocates `27` exact-paper-safe retry
variants to each pair for a total of `756` planned trainings.

## Objective

Prepare a single overnight package that:

- keeps `Track 1` tied only to the canonical full-matrix tables;
- preserves the accepted `19`-model bank concept for each algorithm family;
- spends the available overnight budget on the still-open family-target
  cells instead of re-running already-green pairs;
- maximizes closure pressure on the residual blockers around `MLP`, late
  amplitude terms, and phase `RMSE` at harmonic `162`.

## Canonical Open Pair Inventory

| Family | Open Amplitude Pairs | Open Phase Pairs | Pair Count | Planned Runs |
| --- | --- | --- | ---: | ---: |
| `MLP` | `0, 1, 3, 39, 81, 156, 240` | `1, 3, 39, 162` | `11` | `297` |
| `RF` | `240` | `162` | `2` | `54` |
| `DT` | `none` | `1, 162` | `2` | `54` |
| `ET` | `none` | `240` | `1` | `27` |
| `ERT` | `156, 162, 240` | `162` | `4` | `108` |
| `GBM` | `none` | `162` | `1` | `27` |
| `HGBM` | `39` | `3, 162` | `3` | `81` |
| `XGBM` | `81` | `1, 162` | `3` | `81` |
| `LGBM` | `none` | `162` | `1` | `27` |

Total unresolved pairs: `28`

Total planned trainings: `756`

## Variant Depth Rule

Every unresolved family-target pair receives the same `27`-attempt retry
bundle built from a `9 x 3` matrix:

- seeds: `0`, `7`, `11`, `13`, `17`, `21`, `23`, `29`, `42`
- test-size values: `0.20`, `0.15`, `0.25`
- total attempts per pair: `27`

This keeps the wave aggressive enough for the overnight slot while staying
within the requested `700-800` total-run envelope.

## Exact-Paper Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset | recovered exact-paper dataframe |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Family Identity | unchanged |
| Search Mode | `paper_reference_grid_search` |
| Export Policy | ONNX plus Python-usable fitted estimator persistence |
| Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |
| Track 1 Progress Surface | canonical Tables `2-5` only |

## Packaging Strategy

The package stays grouped by family and remains compatible with the
repository hybrid launcher workflow.

Generated artifacts:

- one family campaign directory plus `README.md` for each non-`SVM` family;
- one YAML per retry attempt under the corresponding family campaign root;
- one family launcher under `scripts/campaigns/track1/exact_paper/`;
- one family launcher note under `doc/scripts/campaigns/`;
- one aggregate launcher plus aggregate launcher note;
- one updated `doc/running/active_training_campaign.yaml` state file.

## Planned Launch Commands

Aggregate local form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns.ps1
```

Aggregate remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout should update:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- the four canonical full-matrix replication tables;
- the accepted exact-paper family-bank inventories where promotion is
  justified;
- the final campaign-results Markdown and validated PDF report.
