# Track 1 MLP Residual Cell Final Closure Campaign Plan Report

## Overview

This planning report prepares the next dedicated exact-paper `MLP` campaign
under the canonical `Track 1` closure rule that reads progress only from the
four full-matrix replication tables.

The campaign targets only the still-non-green accepted `MLP` cells in:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

At the current accepted benchmark state, those residual cells collapse into
only `4` distinct exact-paper repair pairs.

## Objective

Prepare one last narrow overnight-ready `MLP` package that:

- attacks only the residual accepted `MLP` cells still blocking full family
  closure on Tables `2-5`;
- spends more retry depth per pair than the previous family-wide `MLP`
  campaign;
- keeps the scope strictly family-local and exact-paper-safe;
- remains small enough to inspect and relaunch easily if one hard pair still
  fails to close.

## Canonical Residual MLP Inventory

| Target Branch | Harmonics | Affected Tables | Pair Count | Planned Runs |
| --- | --- | --- | ---: | ---: |
| `Amplitude` | `1, 156, 240` | `Table 2`, `Table 3` | `3` | `162` |
| `Phase` | `162` | `Table 4`, `Table 5` | `1` | `54` |

Total distinct target pairs: `4`

Total planned trainings: `216`

## Per-Table Residual Coverage

| Benchmark Table | Residual MLP Cells Covered By This Campaign |
| --- | --- |
| `Table 2 - Amplitude MAE` | `1, 156, 240` |
| `Table 3 - Amplitude RMSE` | `1, 240` |
| `Table 4 - Phase MAE` | `162` |
| `Table 5 - Phase RMSE` | `162` |

## Variant Depth Rule

Each residual target pair receives `54` attempts built from an inspectable
`18 x 3` matrix:

- seeds: `0`, `5`, `7`, `9`, `11`, `13`, `15`, `17`, `19`, `21`, `23`, `27`,
  `29`, `31`, `37`, `42`, `47`, `53`
- test-size values: `0.20`, `0.15`, `0.25`
- total attempts per target pair: `54`

This doubles the previous `27`-attempt-per-pair depth while keeping the total
campaign size at `216` runs, which is still practical for one overnight wave.
The repository's exact-paper MLP grid search does not expose a YAML-side
estimator-capacity override, so the stronger residual wave is implemented by
expanding the retry schedule rather than introducing a second custom capacity
axis.

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

- one dedicated residual `MLP` campaign config directory with `216` YAML files;
- one config-bundle `README.md` inside the campaign directory;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one planned update to `doc/running/active_training_campaign.yaml` after
  explicit approval for the protected state file.

## Planned Launch Commands

Local form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_residual_cell_final_closure_campaign.ps1
```

Remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_residual_cell_final_closure_campaign.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout should update:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the accepted `MLP` row inside the four canonical full-matrix replication
  tables;
- the exact-paper `MLP` family winner bookkeeping if new promotions are
  justified;
- the final campaign-results Markdown and validated PDF report.
