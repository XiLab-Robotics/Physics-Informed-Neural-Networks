# TE Curve Verification Pipeline Directional Comparison Pipeline Alignment

## Overview

This technical document formalizes the next `TE Curve Verification Pipeline` comparison workflow after
the `RCIM Model-Bank Reproduction` paper-faithful closeout split the accepted paper-reference model
archives into explicit `forward` and `backward` surfaces.

The current canonical `TE Curve Verification Pipeline` smoke comparison is still useful, but it is now
too coarse:

- it compares one `LGBM-19` reference bank against one global `feedforward`
  model;
- it evaluates both `forward` and `backward` curves in the same comparison
  pass;
- it does not yet expose directional `feedforward_Fw` and `feedforward_Bw`
  baselines;
- it does not yet scale to all accepted `RCIM Model-Bank Reproduction` families and all relevant
  `Wave 1` family-best models.

The updated pipeline must treat model direction as a first-class comparison
axis. `RCIM Model-Bank Reproduction` contributes `11 x 19` `forward` target models and `11 x 19`
`backward` target models. `Wave 1` contributes the currently accepted family
surface, including global models plus directional `Fw` and `Bw` variants where
they exist.

No subagent use is planned for this implementation. If subagent use becomes
useful later, the exact subagent name, task boundary, and explicit approval
requirement must be added to this document before launching it.

## Technical Approach

The implementation should extend the current
`reference_family_vs_feedforward` workflow into a general `TE Curve Verification Pipeline` comparison
matrix with explicit model-surface metadata.

### Directional Evaluation Contract

Each candidate model must declare one evaluation scope:

| Model Surface | Training Scope | Valid Evaluation Curves |
| --- | --- | --- |
| `global` | `forward + backward` together | `forward` and `backward` |
| `Fw` | `forward` only | `forward` only |
| `Bw` | `backward` only | `backward` only |

This contract applies to:

- `RCIM Model-Bank Reproduction` paper-reference family banks;
- `TE Curve Verification Pipeline` reference-family comparisons;
- `Wave 1` model-family comparisons;
- future waves and future model-family preparation workflows.

Directional models must never be scored on the opposite direction. Global
models may be scored on both directions, but their result tables must keep
`forward` and `backward` metrics separate.

### Dataset Source Contract

All `RCIM Model-Bank Reproduction`, `TE Curve Verification Pipeline`, `Wave 1`, and future-wave training or comparison
pipelines must load the canonical TE dataset directly from:

```text
data/simplified_dataset
```

The loading path must follow the repository dataset pipeline already used by
the repository-owned training models, such as `feedforward`, instead of relying
on copied intermediate datasets or recovered-original prediction CSVs as the
primary data source.

Historical recovered-original artifacts may remain provenance evidence, but
new training and comparison surfaces must derive their train, validation, and
test records from `data/simplified_dataset` through the canonical dataset configuration
and split helpers.

### Revised First TE Curve Verification Pipeline Comparison

The existing `LGBM-19` versus `feedforward` comparison should be replaced by a
direction-aware version:

| Candidate | Archive Or Registry Source | Evaluation Scope |
| --- | --- | --- |
| `LGBM19_Fw` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/` | `forward` curves only |
| `LGBM19_Bw` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/` | `backward` curves only |
| `feedforward` | `output/registries/families/feedforward/` | both directions, reported separately |
| `feedforward_Fw` | `output/registries/families/feedforward_fw/` | `forward` curves only |
| `feedforward_Bw` | `output/registries/families/feedforward_bw/` | `backward` curves only |

The report should preserve the old aggregate evidence as historical context,
but the new canonical verdict must come from direction-valid comparisons only.

### Full TE Curve Verification Pipeline Expansion

After the revised `LGBM19` comparison is working, `TE Curve Verification Pipeline` should expand to:

- all `11` `RCIM Model-Bank Reproduction` `forward` family banks, each with `19` target models,
  evaluated only on `forward` curves;
- all `11` `RCIM Model-Bank Reproduction` `backward` family banks, each with `19` target models,
  evaluated only on `backward` curves;
- all relevant `Wave 1` `Fw` family-best models, evaluated only on `forward`
  curves;
- all relevant `Wave 1` `Bw` family-best models, evaluated only on `backward`
  curves;
- all relevant `Wave 1` global family-best models, evaluated on both
  directions and reported with direction-separated metrics.

The comparison output should make the tested direction, model surface, source
registry or archive, and dataset split explicit for every row.

## Involved Components

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
  - restore a concise `TE Curve Verification Pipeline` section;
  - describe the direction-aware comparison contract;
  - link the current historical `LGBM-19` smoke report and the future canonical
    direction-aware replacement.
- `doc/reports/analysis/Training Results Master Summary.md`
  - keep the `global/Fw/Bw` family policy and online `Table 9` gap aligned with
    the benchmark.
- `doc/reports/analysis/validation_checks/track2/`
  - store the next direction-aware `TE Curve Verification Pipeline` comparison reports.
- `output/validation_checks/track2_reference_comparison/`
  - store immutable validation artifacts for each comparison run.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  - replace the single-reference-bank config with a matrix-capable config or
    add a new direction-aware config alongside the existing historical one.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  - generalize the runner and support utilities so candidate entries can load
    `RCIM Model-Bank Reproduction` reference banks and `Wave 1` registry-backed models using the same
    evaluation contract.
- `models/paper_reference/rcim_track1/forward/`
  - source root for `RCIM Model-Bank Reproduction` forward family banks.
- `models/paper_reference/rcim_track1/backward/`
  - source root for `RCIM Model-Bank Reproduction` backward family banks.
- `output/registries/families/`
  - source root for `Wave 1` global, `Fw`, and `Bw` family-best registry
    entries.
- `config/datasets/transmission_error_dataset.yaml`
  - canonical dataset configuration used to reach `data/simplified_dataset`.
- `data/simplified_dataset/`
  - canonical TE curve source for new `RCIM Model-Bank Reproduction`, `TE Curve Verification Pipeline`, `Wave 1`, and
    future-wave workflows.

## Implementation Steps

1. Recover the document-only `TE Curve Verification Pipeline` context in
   `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`.
   - Record the historical `LGBM-19` versus global `feedforward` smoke result
     as superseded evidence.
   - Add the new direction-aware comparison rule.
   - Add the planned full matrix scope.
2. Update `Training Results Master Summary.md` if needed so it matches the
   benchmark wording for:
   - `global`, `Fw`, and `Bw` model-family surfaces;
   - direct loading from `data/simplified_dataset`;
   - online `Table 9` remaining outside the current offline `TE Curve Verification Pipeline` scope.
3. Add or revise `TE Curve Verification Pipeline` comparison configuration so each candidate row has:
   - `candidate_id`;
   - `candidate_family`;
   - `candidate_surface` as `global`, `Fw`, or `Bw`;
   - `candidate_kind` as `track1_reference_bank` or `wave1_registry_model`;
   - source archive or registry path;
   - allowed evaluation directions.
4. Generalize the `TE Curve Verification Pipeline` runner to evaluate a candidate matrix instead of
   one hard-coded `LGBM-19` bank plus one hard-coded `feedforward` model.
5. Add direction filtering before metric computation.
   - `Fw` candidates receive only `direction_label == "forward"` records.
   - `Bw` candidates receive only `direction_label == "backward"` records.
   - `global` candidates receive both directions but output direction-split
     metrics.
6. Add the revised first comparison:
   - `LGBM19_Fw`;
   - `LGBM19_Bw`;
   - global `feedforward`;
   - `feedforward_Fw`;
   - `feedforward_Bw`.
7. Add the future full-matrix config generation path for:
   - `11` `RCIM Model-Bank Reproduction` forward family banks;
   - `11` `RCIM Model-Bank Reproduction` backward family banks;
   - `Wave 1` global, `Fw`, and `Bw` family-best registry entries.
8. Ensure every new report and validation summary records:
   - dataset root;
   - dataset config path;
   - split policy;
   - candidate source path;
   - model surface;
   - valid evaluation direction;
   - metric denominator.
9. Run the updated `TE Curve Verification Pipeline` comparison in validation mode only after the user
   approves this technical document and any required campaign or validation
   planning document.
10. Run Markdown QA on every touched Markdown file before closeout.
