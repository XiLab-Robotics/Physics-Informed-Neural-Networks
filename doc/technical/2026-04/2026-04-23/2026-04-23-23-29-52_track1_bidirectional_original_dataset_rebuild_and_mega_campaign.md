# Track 1 Bidirectional Original Dataset Rebuild And Mega Campaign

## Overview

This document formalizes the next major `Track 1` evolution after the recent
paper-author clarification on the RCIM forward/backward interpretation.

The current exact-paper `Track 1` branch is based on the recovered forward-only
paper assets and on the recovered `Fw` dataframe. That branch remains valid as
the repository reconstruction of the currently recovered paper release.

However, the next repository-owned `Track 1` execution branch must rebuild the
family-bank workflow directly from the original repository dataset under
`data/datasets/`, explicitly treating `forward` and `backward` as separate
modeling problems. The new branch must therefore generate two distinct family
banks:

- one `forward` bank with `10 x 19` models;
- one `backward` bank with `10 x 19` models.

The repository must also extend the benchmark surface so each of the four
canonical full-matrix tables is represented by:

- the paper reference table;
- the repository `Fw` table;
- the repository `Bw` table.

This work also introduces a future mega-campaign requirement sized well beyond
the minimum `380` directional family-target runs, because the actual closure
goal is to push the new `Fw` and `Bw` table surfaces toward the green paper
targets with repeated retries and family-specific search breadth.

## Technical Approach

The new branch will stop reading the recovered CSV under
`reference/rcim_ml_compensation_recovered_assets/` as its training source.
Instead, it will derive harmonic regression targets directly from the original
repository dataset pipeline already used by repository-native models such as
`feedforward`.

The intended implementation direction is:

- build one original-dataset harmonic-target extraction workflow from
  `data/datasets/`;
- split the extracted harmonic dataset by direction into explicit `Fw` and `Bw`
  bundles;
- train separate exact-paper family banks on each directional bundle;
- preserve the family list:
  `SVR`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`;
- preserve the `19` harmonic targets per direction that currently define the
  canonical `Track 1` family-bank surface;
- disable the current `SVR` grid-search path for this branch and fall back to
  direct `SVR` training for campaign tractability;
- record in the backlog that `SVR` grid-search remains a future escalation path
  if the new `Fw`/`Bw` benchmark surfaces cannot be driven to all-green status
  without it.

The new branch must also decide the canonical split policy for the rebuilt
directional harmonic datasets. The current repository default is
`train/validation/test = 70/20/10`, while the paper uses `80/20` without a
separate validation split. The implementation should therefore evaluate the two
practical options and choose one canonical policy before the mega-campaign is
launched:

1. keep the repository-native `70/20/10` split for consistency with the wider
   repository;
2. use a paper-closer `80/20` split if validation is not materially needed for
   the exact-paper family-bank workflow.

The selected split rule must then be frozen in the new branch configuration and
applied consistently to both directional banks.

The model-reference archive layout under
`models/paper_reference/rcim_track1/` must also be extended so each family
archive becomes direction-aware, with separate `forward` and `backward`
subtrees for:

- ONNX exports;
- Python model artifacts;
- manifests and inventories;
- recreation documentation;
- source-run provenance.

Finally, once the new branch is implemented and stabilized, the repository must
prepare a dedicated mega-campaign with at least one training job for every
family-target-direction combination and a materially larger retry budget for
the difficult open cells.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/running/te_model_live_backlog.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/datasets/transmission_error_dataset.py`
- `config/datasets/transmission_error_dataset.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`
- `models/paper_reference/rcim_track1/`
- future campaign plans under `doc/reports/campaign_plans/track1/exact_paper/`
- future campaign YAML bundles under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`

## Implementation Steps

1. Formalize the new `Track 1` direction-aware branch in the benchmark and in
   the live backlog, including the `SVR` grid-search deferral note.
2. Replace the recovered-CSV training-source dependency with an original-dataset
   harmonic extraction path rooted at `data/datasets/`.
3. Build explicit `forward` and `backward` harmonic datasets and freeze the
   chosen split rule for both branches.
4. Extend the exact-paper family-bank workflow so every family can be trained
   on either directional bundle without changing the family semantics.
5. Expand the canonical benchmark to store, compare, and colorize the paper
   table plus the repository `Fw` and `Bw` tables for each of the four
   full-matrix reference surfaces.
6. Restructure `models/paper_reference/rcim_track1/` so every family archive
   has separate `forward` and `backward` subtrees with complete recreation
   metadata.
7. After the workflow is stable, create the dedicated mega-campaign planning
   report, campaign YAML bundle, launchers, and launcher notes for the
   bidirectional original-dataset rebuild branch.
