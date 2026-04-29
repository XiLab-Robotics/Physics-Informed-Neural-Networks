# Track 1 Forward Last Four Open Cells Campaign Plan Report

## Overview

This planning report prepares one final targeted exact-paper `Track 1`
forward-only campaign after the completed `forward_maxi_last_non_green_cells`
wave.

The canonical forward status is now:

- `Table 2`: `97` green, `3` yellow, `0` red
- `Table 3`: `99` green, `1` yellow, `0` red
- `Table 4`: `90` green, `0` yellow, `0` red
- `Table 5`: `90` green, `0` yellow, `0` red

Total forward non-green cells: `4`

Unique forward residual target pairs: `3`

## Objective

Prepare one final remote original-dataset exact-model-bank campaign that
attacks only the last `3` residual forward amplitude pairs responsible for the
remaining `4` open forward cells.

## Canonical Residual Forward Inventory

| Family | Kind | Harmonic | Current Benchmark Status | Surfaces Hit | Severity Tier | Planned Attempts |
| --- | --- | ---: | --- | --- | --- | ---: |
| `ERT` | `ampl` | `156` | `yellow/green` | `Table 2` | `yellow_single_surface` | `24` |
| `ERT` | `ampl` | `240` | `yellow/yellow` | `Table 2`, `Table 3` | `yellow_multi_surface` | `36` |
| `GBM` | `ampl` | `162` | `yellow/green` | `Table 2` | `yellow_single_surface` | `24` |

## Planned Queue Policy

The queue should be materially smaller than the previous `270`-run maxi wave
and should concentrate the extra depth only on the last multi-surface
residual pair.

Planned tier budget:

- `yellow_single_surface`: `24` attempts per pair
- `yellow_multi_surface`: `36` attempts per pair

This yields:

- single-surface yellow runs: `2 pairs x 24 attempts = 48`
- multi-surface yellow runs: `1 pair x 36 attempts = 36`
- total planned runs: `84`

## Retry Structure

The intended retry structure stays narrow and inspectable:

- all attempts remain exact-paper-safe target-level retries;
- the queue varies split policy and random seed without widening feature scope
  or target scope;
- `ERT ampl 240` receives the deepest budget because it is the only remaining
  pair still open on both amplitude surfaces;
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

- one dedicated config directory for the final forward micro-wave;
- one dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note under `doc/scripts/campaigns/`;
- one prepared update to `doc/running/active_training_campaign.yaml`;
- one exact remote launch command for operator handoff.

## Launch Intent

The exact launcher path will be materialized only after implementation
approval, but the campaign is intended to stay in the standard remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\<forward_last_four_open_cells_launcher>.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and review, the closeout must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- the canonical forward colored matrices for Tables `2-3`
- `models/paper_reference/rcim_track1/forward/` if any accepted target winner
  improves over the archived entry
- the final campaign-results Markdown and validated PDF report
