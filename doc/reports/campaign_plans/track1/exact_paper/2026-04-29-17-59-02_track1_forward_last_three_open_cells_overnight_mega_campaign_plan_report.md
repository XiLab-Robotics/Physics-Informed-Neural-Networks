# Track 1 Forward Last Three Open Cells Overnight Mega Campaign Plan Report

## Overview

This planning report prepares one overnight exact-paper `Track 1` forward-only
mega campaign after the completed `forward_last_three_open_cells` wave failed
to promote any new winners.

The canonical forward status is still:

- `Table 2`: `97` green, `3` yellow, `0` red
- `Table 3`: `100` green, `0` yellow, `0` red
- `Table 4`: `90` green, `0` yellow, `0` red
- `Table 5`: `90` green, `0` yellow, `0` red

Total forward non-green cells: `3`

Unique forward residual target pairs: `3`

## Objective

Prepare one overnight remote original-dataset exact-model-bank mega campaign
that attacks only the last `3` residual forward amplitude pairs with a budget
large enough to justify a final serious overnight search.

## Canonical Residual Forward Inventory

| Family | Kind | Harmonic | Current Benchmark Status | Surfaces Hit | Severity Tier | Planned Attempts |
| --- | --- | ---: | --- | --- | --- | ---: |
| `ERT` | `ampl` | `156` | `yellow` | `Table 2` | `yellow_single_surface_deep` | `72` |
| `ERT` | `ampl` | `240` | `yellow` | `Table 2` | `yellow_single_surface_stubborn_maxi` | `96` |
| `GBM` | `ampl` | `162` | `yellow` | `Table 2` | `yellow_single_surface_deep` | `72` |

## Planned Queue Policy

The previous `84`-run wave already confirmed that a shallow residual retry set
does not move this surface. The overnight queue should therefore stay pair-tight
but increase depth materially.

Planned tier budget:

- `yellow_single_surface_deep`: `72` attempts per pair
- `yellow_single_surface_stubborn_maxi`: `96` attempts per pair

This yields:

- deep single-surface yellow runs: `2 pairs x 72 attempts = 144`
- stubborn single-surface maxi runs: `1 pair x 96 attempts = 96`
- total planned runs: `240`

## Retry Structure

The intended retry structure stays narrow and inspectable:

- all attempts remain exact-paper-safe target-level retries;
- the queue varies split policy and random seed without widening feature scope
  or target scope;
- `ERT ampl 240` receives the deepest budget because it repeatedly emerges as
  the strongest residual candidate without actually crossing the paper-side
  `Table 2` threshold;
- `ERT ampl 156` and `GBM ampl 162` both receive enough depth to avoid another
  underpowered overnight pass;
- no `phase` target is included;
- no already-green harmonic receives a retry slot;
- no backward work is mixed into this campaign.

## Family Scope Notes

- `ERT`: remains in scope for `ampl 156` and `ampl 240`.
- `GBM`: remains in scope only for `ampl 162`.

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

- one dedicated config directory for the overnight forward mega-wave;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one prepared update to `doc/running/active_training_campaign.yaml`;
- one exact remote launch command for operator handoff.

## Launch Intent

The exact launcher path will be materialized only after implementation
approval, but the campaign is intended to stay in the standard remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\<forward_last_three_open_cells_overnight_mega_launcher>.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- the canonical forward colored matrix for `Table 2`
- `models/paper_reference/rcim_track1/forward/` if any accepted target winner
  improves over the archived entry
- the final campaign-results Markdown and validated PDF report
