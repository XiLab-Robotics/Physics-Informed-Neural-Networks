# Track 1 Bidirectional Original-Dataset Smoke And Mega Campaign Plan Report

## Overview

This planning report defines the next `Track 1` execution wave after the
folder-taxonomy refactor and after the introduction of the new
`original_dataset_exact_model_bank` workflow.

The work is split into two ordered phases:

1. a structural smoke-validation wave covering every exact-paper family on both
   `forward` and `backward`;
2. the preparation of the real large bidirectional campaign once the smoke wave
   confirms the workflow is stable.

## Objective

Validate that the refactored original-dataset bidirectional workflow runs end
to end for all ten families before spending the compute budget required for the
full `10 x 19 x 2` reproduction campaign.

The smoke wave is intentionally operational rather than scientific:

- it must prove that the pipeline works;
- it must not be interpreted as the new benchmark truth;
- it exists to de-risk the subsequent mega-campaign.

## Smoke Validation Scope

### Family And Direction Matrix

| Family | Forward Smoke Run | Backward Smoke Run | Total |
| --- | ---: | ---: | ---: |
| `SVR` | `1` | `1` | `2` |
| `MLP` | `1` | `1` | `2` |
| `RF` | `1` | `1` | `2` |
| `DT` | `1` | `1` | `2` |
| `ET` | `1` | `1` | `2` |
| `ERT` | `1` | `1` | `2` |
| `GBM` | `1` | `1` | `2` |
| `HGBM` | `1` | `1` | `2` |
| `XGBM` | `1` | `1` | `2` |
| `LGBM` | `1` | `1` | `2` |

Total smoke validations: `20`

### Smoke Intent

Each smoke run must validate:

- config loading under the refactored config tree;
- dataset-path resolution under `data/datasets`;
- direction-specific sample extraction;
- harmonic decomposition and target naming;
- family fit completion;
- validation-summary generation;
- Markdown report generation;
- ONNX export handling.

### Smoke Lightweight Rule

The smoke runs should aggressively reduce cost while preserving the end-to-end
path:

- one family per run;
- one direction per run;
- minimal parallelism;
- no attempt to optimize metrics;
- keep `SVR` without grid search;
- if needed, allow a smoke-only reduced harmonic subset or reduced split size,
  but only if the runner path remains representative of the full workflow.

## Benchmark Reset Plan

`doc/reports/analysis/RCIM Paper Reference Benchmark.md` must be reset before
the new bidirectional campaign becomes the canonical reference.

Planned benchmark changes:

- preserve the paper-side matrices as the canonical literature reference;
- remove the old recovered forward-only repository-side numeric tables as the
  active benchmark surface;
- introduce fresh repository-owned sections for:
  - `Forward Repository-Side Matrix`
  - `Backward Repository-Side Matrix`
- mark all repository-side cells as pending until the new original-dataset
  runs are produced;
- explicitly state that the prior recovered exact-paper wave is historical and
  no longer the active `Track 1` benchmark baseline.

## Mega-Campaign Target Surface

The full campaign remains the real scientific objective:

- `10` families;
- `19` canonical targets per direction;
- `2` directions;
- minimum canonical training surface: `380` runs.

The final mega-campaign may exceed `380` runs if retry depth, seed variation,
or family-specific attempt bundles are needed.

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/datasets` |
| Split Policy | file-level `70 / 20 / 10` |
| Direction Policy | separate `forward` and `backward` runs |
| Feature Schema | `rpm`, `deg`, `tor` |
| Harmonic Scope | canonical exact-paper harmonic surface |
| `SVR` Search Policy | no grid search during smoke and first mega-campaign pass |
| Protected Campaign Rule | do not overwrite unrelated campaign artifacts |
| Benchmark Rule | do not treat smoke metrics as accepted benchmark results |

## Planned Outputs

After approval, this work should generate:

- smoke configs for `20` validation runs;
- smoke reports and validation summaries;
- reset benchmark tables in `RCIM Paper Reference Benchmark.md`;
- one dedicated large-campaign package for the bidirectional original-dataset
  reproduction wave;
- the corresponding launchers, launcher notes, and active-campaign state.

## Planned Execution Order

1. Execute the `20` smoke validations.
2. Review failures and patch the workflow if needed.
3. Reset the canonical benchmark tables to the fresh restart state.
4. Prepare the full bidirectional mega-campaign package.
5. Stop and wait for explicit approval before launching the large campaign.
