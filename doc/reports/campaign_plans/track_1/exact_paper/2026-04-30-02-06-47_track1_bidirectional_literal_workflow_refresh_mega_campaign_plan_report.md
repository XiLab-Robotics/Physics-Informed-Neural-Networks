# Track 1 Bidirectional Literal-Workflow Refresh Mega Campaign Plan Report

## Overview

This planning report defines the full `Track 1` bidirectional refresh campaign
that must rerun the exact-paper family bank after the repository implementation
was realigned to the recovered original RCIM workflow.

The campaign is intentionally full-surface rather than residual-only because
the family-bank semantics changed at the shared implementation layer used by
the canonical `original_dataset_exact_model_bank` branch.

## Objective

Generate the new canonical `Track 1` bidirectional baseline from the
literalized workflow for all ten exact-paper families and for both playback
directions.

The resulting closeout should replace the old mixed-era benchmark basis with a
scientifically coherent post-alignment baseline.

## Campaign Surface

### Family And Direction Grid

| Direction | Families | Surfaces |
| --- | ---: | ---: |
| `forward` | `10` | `10` |
| `backward` | `10` | `10` |

Total family-direction surfaces: `20`

### Attempt Depth

Each family-direction surface receives `20` attempts with distinct file-split
seeds:

- `0`
- `5`
- `7`
- `9`
- `11`
- `13`
- `15`
- `17`
- `19`
- `21`
- `23`
- `27`
- `29`
- `31`
- `37`
- `42`
- `47`
- `53`
- `59`
- `61`

Total planned campaign runs: `400`

## Family Policy

| Family | Search Policy | Literal-Workflow Status |
| --- | --- | --- |
| `SVR` | paper-reference grid search enabled | literal |
| `MLP` | paper-reference grid search enabled | literal |
| `RF` | paper-reference grid search enabled | literal |
| `DT` | paper-reference grid search enabled | literal |
| `ET` | paper-reference grid search enabled | literal |
| `ERT` | paper-reference grid search enabled | literal |
| `GBM` | paper-reference grid search enabled | literalized with runtime-compatible criterion normalization |
| `HGBM` | paper-reference grid search enabled | literal |
| `XGBM` | paper-reference grid search enabled | literalized with runtime-compatible `n_estimators` key normalization |
| `LGBM` | paper-reference grid search enabled | literal |

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/simplified_dataset` |
| Split Policy | file-level `70 / 20 / 10` |
| Direction Policy | separate `forward` and `backward` banks |
| Feature Schema | `rpm`, `deg`, `tor` |
| Harmonic Scope | full exact-paper `19`-target surface |
| Smoke Carryover | disabled |
| Export Policy | ONNX plus Python bundle persistence |
| Baseline Policy | replace pre-alignment canonical Track 1 baselines after closeout |

## Generated Artifacts

The approved preparation step should generate:

- campaign configs under the `original_dataset_exact_model_bank` campaign tree;
- one remote-capable launcher;
- one launcher usage note;
- one updated `doc/running/active_training_campaign.yaml` in `prepared` state
  with the new bidirectional refresh metadata populated.

## Launch Command

Primary remote overnight form:

```powershell
.\scripts\campaigns\track_1\exact_paper\run_track1_bidirectional_literal_workflow_refresh_mega_campaign.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and closeout, the repository must refresh:

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the bidirectional paper-reference archives under
  `models/paper_reference/rcim_track1/`;
- the impacted family and program registries.
