# Track 1 Bidirectional Original-Dataset Mega Campaign Plan Report

## Overview

This planning report defines the first real large-scale campaign package for
the refactored `Track 1` original-dataset exact-model-bank workflow after the
successful structural smoke-validation wave.

The campaign remains fully bidirectional:

- `forward`
- `backward`

and covers the full exact-paper family set on the original repository dataset.

## Objective

Prepare the first large campaign package that materially explores the new
bidirectional original-dataset branch while remaining aligned with the current
family-bank runner architecture.

The runner granularity is one family bank per direction and attempt. Each run
trains the full `19`-target exact-model surface for that family-direction pair.

## Campaign Surface

### Family And Direction Grid

| Direction | Families | Surfaces |
| --- | ---: | ---: |
| `forward` | `10` | `10` |
| `backward` | `10` | `10` |

Total family-direction surfaces: `20`

### Attempt Depth

Each family-direction surface receives `20` attempts with distinct
file-split seeds:

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

| Family | Search Policy |
| --- | --- |
| `SVR` | direct fit, grid search disabled |
| `MLP` | paper-reference grid search enabled |
| `RF` | paper-reference grid search enabled |
| `DT` | paper-reference grid search enabled |
| `ET` | paper-reference grid search enabled |
| `ERT` | paper-reference grid search enabled |
| `GBM` | paper-reference grid search enabled |
| `HGBM` | paper-reference grid search enabled |
| `XGBM` | paper-reference grid search enabled |
| `LGBM` | paper-reference grid search enabled |

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/datasets` |
| Split Policy | file-level `70 / 20 / 10` |
| Direction Policy | separate `forward` and `backward` banks |
| Feature Schema | `rpm`, `deg`, `tor` |
| Harmonic Scope | full exact-paper `19`-target surface |
| Smoke Carryover | smoke settings disabled |
| Export Policy | ONNX plus Python bundle persistence |

## Generated Artifacts

The preparation step should generate:

- campaign configs under the refactored `original_dataset_exact_model_bank`
  campaign tree;
- one remote-capable launcher;
- one launcher usage note;
- one updated `doc/running/active_training_campaign.yaml` in `prepared` state
  with remote metadata populated.

## Launch Command

Primary remote overnight form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_original_dataset_mega_campaign.ps1 -Remote
```

## Expected Post-Campaign Obligations

After execution and closeout, the repository must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the bidirectional paper-reference archives under
  `models/paper_reference/rcim_track1/`;
- the family and program registries impacted by accepted winners.
