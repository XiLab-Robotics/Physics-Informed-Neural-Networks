# Track 1 Forward Maxi Last Non-Green Cells Campaign Plan Report

## Overview

This planning report prepares a new exact-paper `Track 1` forward-only maxi
campaign after the completed `forward_last_non_green_cells` wave.

The canonical forward status is now:

- `Table 2`: `93` green, `5` yellow, `2` red
- `Table 3`: `98` green, `1` yellow, `1` red
- `Table 4`: `90` green, `0` yellow, `0` red
- `Table 5`: `90` green, `0` yellow, `0` red

Total forward non-green cells: `9`

Unique forward residual target pairs: `7`

## Objective

Prepare one remote original-dataset exact-model-bank campaign that attacks
only the last `7` non-green forward amplitude pairs with a few hundred runs,
leaving every already-green forward target untouched.

## Canonical Residual Forward Inventory

| Family | Kind | Harmonic | Current Benchmark Status | Surfaces Hit | Severity Tier | Planned Attempts |
| --- | --- | ---: | --- | --- | --- | ---: |
| `ERT` | `ampl` | `156` | `yellow/green` | `Table 2` | `yellow_single_surface` | `24` |
| `ERT` | `ampl` | `162` | `yellow/green` | `Table 2`, `Table 3` | `yellow_multi_surface` | `36` |
| `ERT` | `ampl` | `240` | `yellow/yellow` | `Table 2`, `Table 3` | `yellow_multi_surface` | `36` |
| `GBM` | `ampl` | `162` | `red/red` | `Table 2`, `Table 3` | `red_multi_surface` | `63` |
| `XGBM` | `ampl` | `240` | `yellow/green` | `Table 2` | `yellow_single_surface` | `24` |
| `LGBM` | `ampl` | `0` | `yellow/green` | `Table 2` | `yellow_single_surface` | `24` |
| `LGBM` | `ampl` | `162` | `red/green` | `Table 2`, `Table 3` | `red_multi_surface` | `63` |

## Planned Queue Policy

The queue should be materially larger than the previous `108`-run residual
wave and should concentrate the extra depth on the two hardest `h162`
pressure points.

Planned tier budget:

- `yellow_single_surface`: `24` attempts per pair
- `yellow_multi_surface`: `36` attempts per pair
- `red_multi_surface`: `63` attempts per pair

This yields:

- single-surface yellow runs: `3 pairs x 24 attempts = 72`
- multi-surface yellow runs: `2 pairs x 36 attempts = 72`
- red multi-surface runs: `2 pairs x 63 attempts = 126`
- total planned runs: `270`

## Retry Structure

The intended retry structure stays inspectable even at this scale:

- all attempts remain exact-paper-safe target-level retries;
- the queue varies split policy and random seed without widening feature scope
  or target scope;
- red-tier retries receive the deepest budget because they still miss the paper
  threshold on at least one active amplitude surface;
- no `phase` target is included;
- no already-green harmonic receives a retry slot;
- no backward work is mixed into this campaign.

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

- one dedicated config directory for the forward maxi wave;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one prepared update to `doc/running/active_training_campaign.yaml`;
- one exact remote launch command for operator handoff.

## Launch Intent

The exact launcher path will be materialized only after implementation
approval, but the campaign is intended to stay in the standard remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\<forward_maxi_last_non_green_launcher>.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- the canonical forward colored matrices for Tables `2-3`
- `models/paper_reference/rcim_track1/forward/` if any accepted target winner
  improves over the archived entry
- the final campaign-results Markdown and validated PDF report
