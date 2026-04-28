# Track 1 Forward Last Non-Green Cells Campaign Plan Report

## Overview

This planning report prepares the next exact-paper `Track 1` repair wave after
the completed `forward_final_open_cells` closeout.

The canonical forward status is now:

- `Table 2`: `93` green, `4` yellow, `3` red
- `Table 3`: `97` green, `2` yellow, `1` red
- `Table 4`: `90` green, `0` yellow, `0` red
- `Table 5`: `90` green, `0` yellow, `0` red

Total forward non-green cells: `10`

Unique forward residual target pairs: `7`

## Objective

Prepare one last forward-only original-dataset exact-model-bank repair
campaign that retries only the `7` still non-green amplitude target pairs and
leaves every already-green forward target untouched.

## Canonical Residual Forward Inventory

| Family | Kind | Harmonic | Current Benchmark Status | Surfaces Hit | Severity |
| --- | --- | ---: | --- | --- | --- |
| `ERT` | `ampl` | `156` | `yellow/green` | `Table 2` | `yellow_only` |
| `ERT` | `ampl` | `162` | `red/red` | `Table 2`, `Table 3` | `red_multi_surface` |
| `ERT` | `ampl` | `240` | `yellow/yellow` | `Table 2`, `Table 3` | `yellow_multi_surface` |
| `GBM` | `ampl` | `162` | `red/red` | `Table 2`, `Table 3` | `red_multi_surface` |
| `XGBM` | `ampl` | `240` | `yellow/green` | `Table 2` | `yellow_only` |
| `LGBM` | `ampl` | `0` | `yellow/green` | `Table 2` | `yellow_only` |
| `LGBM` | `ampl` | `162` | `red/yellow` | `Table 2`, `Table 3` | `red_multi_surface` |

## Planned Queue Policy

The queue should be more aggressive than the previous `76`-run wave and focus
only on the last amplitude residues with a materially larger retry budget:

- base retry matrix for every residual target pair: `12` attempts;
- escalation retry matrix only for the `3` still-red `h162` pairs:
  `8` extra attempts.

This yields:

- base runs: `7 pairs x 12 attempts = 84`
- escalation runs: `3 red pairs x 8 extra attempts = 24`
- total planned runs: `108`

## Retry Structure

The intended retry structure remains fully inspectable even with the stronger
budget:

- base attempts vary seed and split policy in a small exact-paper-safe matrix;
- escalation attempts apply only to:
  - `ERT ampl 162`
  - `GBM ampl 162`
  - `LGBM ampl 162`
- no `phase` targets are included;
- no already-green harmonic receives a retry slot.

## Family Scope Notes

- `ERT`: remains in scope for `ampl 156`, `ampl 162`, and `ampl 240`.
- `GBM`: remains in scope only for `ampl 162`.
- `XGBM`: remains in scope only for `ampl 240`.
- `LGBM`: remains in scope for `ampl 0` and `ampl 162`.

Families with no remaining forward amplitude non-green targets stay out of
scope.

## Exact-Paper Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset | original-dataset exact-model-bank dataframe |
| Direction | `forward` only |
| Surface Scope | amplitude only |
| Input Features | `rpm`, `deg`, `tor` |
| `maximum_deg` | `35.0` |
| Runner | `original_dataset_exact_model_bank` |
| Search Mode | target-level exact-paper repair |
| Export Policy | ONNX plus Python estimator persistence |
| Remote Mode | `xilab-remote` |
| Archive Rule | refresh `models/paper_reference/rcim_track1/forward/` only when an accepted winner improves |

## Packaging Strategy

Generated artifacts for the implementation step after approval:

- one dedicated residual forward campaign planning report;
- one dedicated config directory for the last forward non-green amplitude wave;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one prepared update to `doc/running/active_training_campaign.yaml`.

## Planned Launch Form

The exact launcher path will be materialized only after implementation
approval, but the campaign is intended to stay in the standard remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\<forward_last_non_green_launcher>.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the canonical forward colored matrices for Tables `2-3`;
- `models/paper_reference/rcim_track1/forward/` if any accepted target winner
  improves over the archived entry;
- the final campaign-results Markdown and validated PDF report.
