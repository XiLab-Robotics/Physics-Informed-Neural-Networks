# Track 1 MLP Family Full-Matrix Repair Campaign Plan Report

## Overview

This planning report prepares the next dedicated exact-paper `MLP` family
repair wave under the canonical `Track 1` closure rule that reads progress
only from the four full-matrix replication tables.

The campaign scopes every still-non-green `MLP` family-target cell in:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

Because `MAE` and `RMSE` share the same exact-paper target models inside a
given amplitude or phase branch, the open `MLP` cells collapse into `12`
distinct family-target repair pairs.

## Objective

Prepare one overnight-ready `MLP` package that:

- attacks every current non-green `MLP` target pair in the canonical benchmark;
- keeps the family-local scope separate from the cross-family Track 1 envelope;
- preserves exact-paper-safe inputs, target scoping, and export rules;
- uses a retry depth large enough to give the weakest `MLP` targets another
  meaningful search wave without inflating into a multi-family mega-campaign.

## Canonical MLP Repair Inventory

| Target Branch | Harmonics | Affected Tables | Pair Count | Planned Runs |
| --- | --- | --- | ---: | ---: |
| `Amplitude` | `0, 1, 3, 39, 40, 81, 156, 240` | `Table 2`, `Table 3` | `8` | `216` |
| `Phase` | `1, 3, 39, 162` | `Table 4`, `Table 5` | `4` | `108` |

Total distinct target pairs: `12`

Total planned trainings: `324`

## Per-Table Open-Cell Coverage

| Benchmark Table | Open MLP Cells Covered By This Campaign |
| --- | --- |
| `Table 2 - Amplitude MAE` | `0, 1, 3, 39, 40, 81, 156, 240` |
| `Table 3 - Amplitude RMSE` | `0, 1, 3, 39, 81, 240` |
| `Table 4 - Phase MAE` | `1, 3, 39, 162` |
| `Table 5 - Phase RMSE` | `1, 39, 162` |

## Variant Depth Rule

Each deduplicated `MLP` target pair receives the same `27`-attempt retry
bundle built from a `9 x 3` matrix:

- seeds: `0`, `7`, `11`, `13`, `17`, `21`, `23`, `29`, `42`
- test-size values: `0.20`, `0.15`, `0.25`
- total attempts per target pair: `27`

This keeps the campaign materially stronger than the earlier `6`-attempt
residual-cell wave while remaining well below the previous `756`-run
multi-family overnight package.

## Exact-Paper Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset | recovered exact-paper dataframe |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Family Identity | `MLP` only |
| Search Mode | `paper_reference_grid_search` |
| Export Policy | ONNX plus Python-usable fitted estimator persistence |
| Output Root | `output/validation_checks/paper_reimplementation_rcim_exact_model_bank` |
| Track 1 Progress Surface | canonical Tables `2-5` only |

## Packaging Strategy

Generated artifacts for this preparation step:

- one dedicated `MLP` campaign config directory with `324` YAML files;
- one config-bundle `README.md` inside the campaign directory;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one planned update to `doc/running/active_training_campaign.yaml` after
  explicit approval for the protected state file.

## Planned Launch Commands

Local form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_family_full_matrix_repair_campaign.ps1
```

Remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_family_full_matrix_repair_campaign.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout should update:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the `MLP` row of the four canonical full-matrix replication tables;
- the accepted exact-paper `MLP` family inventory where promotions are justified;
- the final campaign-results Markdown and validated PDF report.
