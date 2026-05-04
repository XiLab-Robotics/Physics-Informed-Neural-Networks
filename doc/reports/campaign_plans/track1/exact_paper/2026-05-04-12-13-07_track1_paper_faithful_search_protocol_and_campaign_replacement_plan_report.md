# Track 1 Paper-Faithful Search Protocol And Campaign Replacement Plan Report

## Overview

This planning report supersedes the currently active
`track1_bidirectional_literal_workflow_refresh_mega_campaign_2026-04-30_02_11_58`
design and also extends the earlier campaign-only replacement proposal.

The key reason is that the current repository exact-paper branch still misses a
historical protocol stage from the recovered original workflow: after fitting
the `GridSearchCV` wrapper on the held-out training split, the original code
also performs `cross_validate(...)` on the wrapper and then per-target
`cross_validate(...)` on the best wrapped estimators.

## Objective

Produce a paper-faithful bidirectional `Track 1` baseline with two guarantees:

1. the shared exact-paper training path reproduces the historical
   search-and-cross-validation protocol;
2. the campaign design performs exactly one search pass per family-direction
   surface.

## Protocol Alignment Scope

### Historical Workflow Stages To Reproduce

| Stage | Recovered Original Workflow | Current Repo State | Required Action |
| --- | --- | --- | --- |
| Held-out split | `train_test_split(..., random_state=0)` | already aligned | keep |
| Search wrapper | `GridSearchCV(...)` | already aligned | keep |
| Wrapper fit | train on held-out training split | already aligned | keep |
| Global validation | `cross_validate(self.model, X, Y, cv=10, scoring=[...])` | missing | implement |
| Target-wise validation | `cross_validate(best_estimator_.estimators_[i], ...)` | missing | implement |
| Campaign repetition layer | absent | present in `400`-run design | remove |

### Scoring Surface

The historical protocol uses the following scoring set:

- `neg_mean_squared_error`
- `neg_root_mean_squared_error`
- `neg_mean_absolute_error`
- `neg_mean_absolute_percentage_error`

## Replacement Campaign Surface

### Family And Direction Grid

| Direction | Families | Runs |
| --- | ---: | ---: |
| `forward` | `10` | `10` |
| `backward` | `10` | `10` |

Total family-direction surfaces: `20`

### Attempt Policy

Each family-direction surface receives exactly one paper-faithful search pass:

- no seed sweep;
- no retry ladder;
- no repeated robustness campaign;
- one config, one search, one winner per family-direction surface.

## Family Policy

| Family | Search Policy | Literal-Workflow Status |
| --- | --- | --- |
| `SVR` | paper-reference grid search enabled once | literal |
| `MLP` | paper-reference grid search enabled once | literal |
| `RF` | paper-reference grid search enabled once | literal |
| `DT` | paper-reference grid search enabled once | literal |
| `ET` | paper-reference grid search enabled once | literal |
| `ERT` | paper-reference grid search enabled once | literal |
| `GBM` | paper-reference grid search enabled once | literalized with runtime-compatible criterion normalization |
| `HGBM` | paper-reference grid search enabled once | literal |
| `XGBM` | paper-reference grid search enabled once | literalized with runtime-compatible `n_estimators` key normalization |
| `LGBM` | paper-reference grid search enabled once | literal |

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/datasets` |
| Split Policy | file-level `70 / 20 / 10` |
| Direction Policy | separate `forward` and `backward` banks |
| Feature Schema | `rpm`, `deg`, `tor` |
| Harmonic Scope | full exact-paper `19`-target surface |
| Retry Policy | disabled |
| Seed Sweep Policy | disabled |
| Export Policy | ONNX plus Python bundle persistence |
| Active Campaign Policy | do not rewrite the protected active state until explicit approval |

## Generated Artifacts

The approved implementation and preparation step should generate:

- the patched shared exact-paper search protocol;
- smoke-validation evidence for the new protocol summaries;
- campaign configs under the `original_dataset_exact_model_bank` campaign tree;
- one remote-capable launcher;
- one launcher usage note;
- one updated `doc/running/active_training_campaign.yaml` in `prepared` state
  for the replacement campaign.

## Launch Command

The exact launcher path will be materialized after approval together with the
replacement campaign package.

## Expected Post-Campaign Obligations

After execution and closeout, the repository must refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the bidirectional paper-reference archives under
  `models/paper_reference/rcim_track1/`;
- the impacted family and program registries.
