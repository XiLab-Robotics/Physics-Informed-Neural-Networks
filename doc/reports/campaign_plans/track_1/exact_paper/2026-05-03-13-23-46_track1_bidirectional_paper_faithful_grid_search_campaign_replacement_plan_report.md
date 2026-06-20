# Track 1 Bidirectional Paper-Faithful Grid-Search Campaign Replacement Plan Report

## Overview

This planning report replaces the currently running
`track1_bidirectional_literal_workflow_refresh_mega_campaign_2026-04-30_02_11_58`
design with a paper-faithful `Track 1` campaign structure.

The replacement is necessary because the `400`-run mega campaign adds a
repository-side repetition layer that is not present in the recovered original
RCIM workflow. The original workflow performs a single hyperparameter-search
pass per model, not a seed-sweep campaign with repeated attempts.

## Objective

Generate a new canonical bidirectional `Track 1` exact-paper baseline using
the literalized family definitions and paper-faithful search semantics:

- `1` grid-search training run for each `forward` family;
- `1` grid-search training run for each `backward` family.

Total planned campaign runs: `20`.

## Campaign Surface

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

## Recovered-Workflow Basis

The recovered original workflow evidence for this replacement is:

- `predictorMLCrossValidationWithHyperparameter(...)` is the original
  hyperparameter-search path;
- it uses `train_test_split(..., random_state=0)`;
- it wraps the model in `GridSearchCV(...)`;
- it does not introduce a multi-seed retry campaign layer.

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/simplified_dataset` |
| Split Policy | file-level `70 / 20 / 10` |
| Direction Policy | separate `forward` and `backward` banks |
| Feature Schema | `rpm`, `deg`, `tor` |
| Harmonic Scope | full exact-paper `19`-target surface |
| Retry Policy | disabled |
| Seed Sweep Policy | disabled |
| Export Policy | ONNX plus Python bundle persistence |
| Baseline Policy | replace the current `400`-run campaign design with a paper-faithful `20`-run design |

## Generated Artifacts

The approved preparation step should generate:

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

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- the bidirectional paper-reference archives under
  `models/paper_reference/rcim_track1/`;
- the impacted family and program registries.
