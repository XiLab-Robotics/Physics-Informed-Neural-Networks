# Track 1 Forward Final Open-Cells Campaign Plan Report

## Overview

This planning report prepares the next exact-paper `Track 1` repair wave after
the completed `forward_open_cell_repair` closeout.

The new wave is intentionally narrow and attacks only the last canonical
forward non-green cells still open across:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The current canonical forward status is:

- `Table 2`: `94` green, `3` yellow, `3` red
- `Table 3`: `96` green, `3` yellow, `1` red
- `Table 4`: `89` green, `1` yellow, `0` red
- `Table 5`: `90` green, `0` yellow, `0` red

Total forward non-green cells: `11`

Unique forward residual target pairs: `8`

## Objective

Prepare one final forward-only original-dataset exact-model-bank repair
campaign that retries only the `8` residual forward target pairs and leaves
all already-green forward cells untouched.

## Canonical Residual Forward Inventory

| Family | Kind | Harmonic | Current Benchmark Status | Surfaces Hit | Severity |
| --- | --- | ---: | --- | --- | --- |
| `ERT` | `ampl` | `156` | `yellow` | `Table 2` | `yellow_only` |
| `ERT` | `ampl` | `162` | `red` | `Table 2` | `red` |
| `ERT` | `ampl` | `240` | `yellow` | `Table 2`, `Table 3` | `yellow_multi_surface` |
| `GBM` | `ampl` | `162` | `red` | `Table 2`, `Table 3` | `red_multi_surface` |
| `LGBM` | `ampl` | `0` | `yellow` | `Table 2` | `yellow_only` |
| `LGBM` | `ampl` | `162` | `red/yellow` | `Table 2`, `Table 3` | `red_multi_surface` |
| `XGBM` | `ampl` | `240` | `yellow` | `Table 3` | `yellow_only` |
| `LGBM` | `phase` | `81` | `yellow` | `Table 4` | `yellow_only` |

## Planned Queue Policy

The queue is intentionally smaller than the prior `300`-run wave and uses a
two-tier retry budget:

- base retry matrix for every residual target pair: `8` attempts;
- escalation retry matrix only for currently red amplitude pairs:
  `4` extra attempts.

This yields:

- base runs: `8 pairs x 8 attempts = 64`
- escalation runs: `3 red pairs x 4 extra attempts = 12`
- total planned runs: `76`

## Retry Structure

The intended retry policy is still inspectable rather than open-ended:

- base attempts vary seed and split policy in a small exact-paper-safe matrix;
- escalation attempts apply only to:
  - `ERT ampl 162`
  - `GBM ampl 162`
  - `LGBM ampl 162`
- no extra escalation is applied to already-yellow-only pairs.

## Family Scope Notes

- `ERT`: remains in scope only for the late-harmonic amplitude residuals
  `156`, `162`, and `240`.
- `GBM`: remains in scope only for `ampl 162`, which is still red on both
  forward amplitude surfaces.
- `LGBM`: remains in scope for `ampl 0`, `ampl 162`, and `phase 81`.
- `XGBM`: remains in scope only for `ampl 240`.

Families with no remaining forward non-green targets stay out of scope.

## Exact-Paper Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset | original-dataset exact-model-bank dataframe |
| Direction | `forward` only |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Runner | `original_dataset_exact_model_bank` |
| Search Mode | target-level exact-paper repair |
| Export Policy | ONNX plus Python estimator persistence |
| Remote Mode | `xilab-remote` |
| Archive Rule | refresh `models/paper_reference/rcim_track1/forward/` only when an accepted winner improves |

## Packaging Strategy

Generated artifacts for the implementation step after approval:

- one residual forward campaign planning report;
- one dedicated config directory for the final forward open-cell residual wave;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one prepared update to `doc/running/active_training_campaign.yaml`.

## Planned Launch Form

The exact launcher path will be materialized only after implementation
approval, but the campaign is intended to stay in the standard remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\<final_forward_open_cells_launcher>.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the canonical forward colored matrices for Tables `2-5`;
- `models/paper_reference/rcim_track1/forward/` if any accepted target winner
  improves over the archived entry;
- the final campaign-results Markdown and validated PDF report.
