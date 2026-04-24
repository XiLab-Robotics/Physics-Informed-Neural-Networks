# Track 1 Remaining Yellow-Cell Multi-Family Campaign Bundle Plan Report

## Overview

This planning report prepares the next exact-paper `Track 1` overnight bundle
focused only on the still-yellow accepted family-row cells across the four
canonical full-matrix replication tables:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The global benchmark envelope is already much healthier than the family-row
surface, so this bundle deliberately targets the accepted row-local yellow
cells that still keep `SVM`, `MLP`, `ET`, `ERT`, `HGBM`, and `XGBM` open under
the `10 x 19` Track 1 completion rule.

## Objective

Prepare one dedicated family-local campaign for each still-open family, plus
one aggregate overnight launcher that executes the six campaigns in sequence
without re-opening already green cells.

## Canonical Residual Yellow Inventory

| Family | Yellow Target Pairs | Pair Count | Planned Runs |
| --- | --- | ---: | ---: |
| `SVM` | `A40`, `A240`, `P162` | `3` | `180` |
| `MLP` | `P162` | `1` | `60` |
| `ET` | `P1` | `1` | `60` |
| `ERT` | `A156`, `A162`, `A240` | `3` | `180` |
| `HGBM` | `A39` | `1` | `60` |
| `XGBM` | `P1`, `P162` | `2` | `120` |

Total distinct target pairs: `11`

Total planned trainings: `660`

## Retry Depth Rule

Each distinct family-target pair receives `60` attempts built from an
inspectable `20 x 3` retry matrix:

- seeds: `0`, `5`, `7`, `9`, `11`, `13`, `15`, `17`, `19`, `21`, `23`, `27`,
  `29`, `31`, `37`, `42`, `47`, `53`, `59`, `61`
- test-size values: `0.20`, `0.15`, `0.25`
- total attempts per target pair: `60`

This keeps the whole overnight bundle at `660` trainings, which stays inside
the requested night-run budget while still giving materially more depth than
the earlier `27`-attempt open-cell wave.

## Family Scoping Notes

- `SVM`: keep the family in scope because its accepted row still has yellow
  cells on `A40`, `A240`, and `P162`, even though the global benchmark envelope
  is already numerically stronger on those harmonics.
- `MLP`: only `P162` remains yellow after the dedicated family repair and final
  residual closeout waves.
- `ET`: only `P1` remains yellow, so this family gets a narrow one-pair repair
  campaign.
- `ERT`: the only remaining yellow cells are the three amplitude late-harmonic
  targets `A156`, `A162`, and `A240`.
- `HGBM`: only `A39` remains yellow.
- `XGBM`: only `P1` and `P162` remain yellow.

## Exact-Paper Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset | recovered exact-paper dataframe |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Search Mode | `paper_reference_grid_search` |
| Family Scope | one exact-paper family per launcher |
| Export Policy | ONNX plus Python-usable fitted estimator persistence |
| Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |
| Track 1 Progress Surface | accepted family-row status on canonical Tables `2-5` |

## Packaging Strategy

Generated artifacts for this preparation step:

- one bundle planning report for the six-family yellow-cell closure wave;
- six dedicated exact-paper family campaign config directories;
- six dedicated PowerShell family launchers under `scripts/campaigns/track1/exact_paper/`;
- six matching launcher notes under `doc/scripts/campaigns/`;
- one aggregate overnight launcher that sequences the six family launchers;
- one aggregate launcher note;
- one prepared update to `doc/running/active_training_campaign.yaml` for the new bundle.

## Planned Launch Commands

Primary remote overnight form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_remaining_yellow_cell_campaigns.ps1 -Remote
```

Local form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_remaining_yellow_cell_campaigns.ps1
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the accepted family-row colored replication matrices for Tables `2-5`;
- exact-paper family registries if any new accepted winners are promoted;
- the final campaign-results Markdown and validated PDF report for the bundle.
