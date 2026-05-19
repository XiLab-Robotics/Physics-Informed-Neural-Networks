# Track 2 Composite Best Reference Models

## Overview

This technical note plans the next `Track 2` extension: add composed
paper-reference candidates that assemble one harmonic-wise model from the best
available family cell instead of using one single family across all harmonic
targets.

The requested candidates are:

- `paper_original_best_Fw`;
- `paper_retuned_best_Fw`;
- `track1_best_Fw`;
- `paper_retuned_best_Bw`;
- `track1_best_Bw`.

There is no `paper_original_best_Bw` candidate because the paper original table
surface is forward-only in the current repository benchmark.

No implementation code should be changed until this cell-selection plan is
approved.

## Technical Approach

The composed model will keep the existing `Track 2` reconstruction contract:

- amplitude harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- phase harmonics: `1, 3, 39, 40, 78, 81, 156, 162, 240`;
- forward candidates are evaluated only on forward curves;
- backward candidates are evaluated only on backward curves;
- input curves continue to load from `data/datasets` through the canonical
  dataset configuration.

For the paper original forward candidate, the selector must follow the
paper-level `Table 6` deployment selection. That selection is historical
paper evidence and does not simply choose every raw minimum in Tables `2-5`.

For retuned and Track 1 composed candidates, the proposed selector mirrors the
paper deployment role:

- select amplitude model cells from Table `3` (`Amplitude RMSE`);
- select phase model cells from Table `5` (`Phase RMSE`);
- keep Table `2` and Table `4` minima as audit metadata in the generated
  composed inventory so the choice remains inspectable.

If this arbitration rule is not what is desired, it should be changed before
implementation.

## Selected Composite Cells

### Forward Paper Original Composite

Source rule: historical paper `Table 6`.

| Target | Selected Families |
| --- | --- |
| amplitude `A*_k` | `0:SVM`, `1:RF`, `3:HGBM`, `39:HGBM`, `40:ERT`, `78:HGBM`, `81:RF`, `156:ERT`, `162:ERT`, `240:ERT` |
| phase `phi*_k` | `1:LGBM`, `3:HGBM`, `39:HGBM`, `40:GBM`, `78:RF`, `81:RF`, `156:RF`, `162:ERT`, `240:ERT` |

### Forward Paper Retuned Composite

Source rule: current `Paper Retuned` forward tables. Amplitude comes from
Table `3`; phase comes from Table `5`.

| Target | Selected Families |
| --- | --- |
| amplitude `A*_k` | `0:LGBM`, `1:ERT`, `3:HGBM`, `39:LGBM`, `40:ERT`, `78:HGBM`, `81:RF`, `156:ERT`, `162:RF`, `240:RF` |
| phase `phi*_k` | `1:XGBM`, `3:GBM`, `39:LGBM`, `40:RF`, `78:GBM`, `81:RF`, `156:ERT`, `162:ERT`, `240:ERT` |

### Forward Track 1 Composite

Source rule: current `Track 1` forward tables. Amplitude comes from Table `3`;
phase comes from Table `5`.

| Target | Selected Families |
| --- | --- |
| amplitude `A*_k` | `0:SVM`, `1:HGBM`, `3:ERT`, `39:ERT`, `40:ERT`, `78:ERT`, `81:ERT`, `156:ERT`, `162:ET`, `240:ERT` |
| phase `phi*_k` | `1:RF`, `3:GBM`, `39:RF`, `40:GBM`, `78:GBM`, `81:ERT`, `156:ERT`, `162:RF`, `240:DT` |

### Backward Paper Retuned Composite

Source rule: current `Paper Retuned` backward tables. Amplitude comes from
Table `3`; phase comes from Table `5`.

| Target | Selected Families |
| --- | --- |
| amplitude `A*_k` | `0:RF`, `1:ERT`, `3:ERT`, `39:RF`, `40:ERT`, `78:ERT`, `81:ERT`, `156:ERT`, `162:RF`, `240:RF` |
| phase `phi*_k` | `1:GBM`, `3:RF`, `39:ERT`, `40:RF`, `78:RF`, `81:ERT`, `156:RF`, `162:ERT`, `240:RF` |

### Backward Track 1 Composite

Source rule: current `Track 1` backward tables. Amplitude comes from Table `3`;
phase comes from Table `5`.

| Target | Selected Families |
| --- | --- |
| amplitude `A*_k` | `0:LGBM`, `1:ERT`, `3:GBM`, `39:LGBM`, `40:RF`, `78:LGBM`, `81:ERT`, `156:ERT`, `162:LGBM`, `240:LGBM` |
| phase `phi*_k` | `1:RF`, `3:LGBM`, `39:DT`, `40:ERT`, `78:LGBM`, `81:LGBM`, `156:ERT`, `162:DT`, `240:DT` |

## Audit Cells From Tables 2 And 4

These cells are not proposed as the default composed-model selector, but they
will be preserved as audit metadata because the user request explicitly
references Tables `2-5`.

### Forward Paper Retuned Audit Cells

| Table | Best Families |
| --- | --- |
| Table `2` amplitude MAE | `0:LGBM`, `1:ERT`, `3:HGBM`, `39:LGBM`, `40:ERT`, `78:HGBM`, `81:RF`, `156:ERT`, `162:ERT`, `240:RF` |
| Table `4` phase MAE | `1:XGBM`, `3:GBM`, `39:HGBM`, `40:XGBM`, `78:GBM`, `81:XGBM`, `156:ERT`, `162:ERT`, `240:RF` |

### Forward Track 1 Audit Cells

| Table | Best Families |
| --- | --- |
| Table `2` amplitude MAE | `0:RF`, `1:ERT`, `3:ERT`, `39:ERT`, `40:ERT`, `78:ERT`, `81:ERT`, `156:ERT`, `162:ERT`, `240:ERT` |
| Table `4` phase MAE | `1:RF`, `3:GBM`, `39:ERT`, `40:ERT`, `78:GBM`, `81:ERT`, `156:ERT`, `162:ERT`, `240:ERT` |

### Backward Paper Retuned Audit Cells

| Table | Best Families |
| --- | --- |
| Table `2` amplitude MAE | `0:RF`, `1:ERT`, `3:RF`, `39:ERT`, `40:ERT`, `78:ERT`, `81:ERT`, `156:ERT`, `162:ERT`, `240:RF` |
| Table `4` phase MAE | `1:ERT`, `3:RF`, `39:ERT`, `40:RF`, `78:ERT`, `81:ERT`, `156:RF`, `162:ERT`, `240:RF` |

### Backward Track 1 Audit Cells

| Table | Best Families |
| --- | --- |
| Table `2` amplitude MAE | `0:LGBM`, `1:ERT`, `3:GBM`, `39:LGBM`, `40:RF`, `78:LGBM`, `81:ERT`, `156:ERT`, `162:ERT`, `240:LGBM` |
| Table `4` phase MAE | `1:RF`, `3:LGBM`, `39:DT`, `40:ERT`, `78:GBM`, `81:ERT`, `156:ERT`, `162:DT`, `240:DT` |

## Involved Components

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
  - source of Tables `2-5` and the currently accepted paper-reference cells.
- `models/paper_reference/rcim_original/forward/`
  - forward-only recovered original paper-reference inventories.
- `models/paper_reference/rcim_retuned/forward/`
  - forward retuned paper-reference inventories.
- `models/paper_reference/rcim_retuned/backward/`
  - backward retuned paper-reference inventories.
- `models/paper_reference/rcim_track1/forward/`
  - accepted Track 1 forward family inventories.
- `models/paper_reference/rcim_track1/backward/`
  - accepted Track 1 backward family inventories.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - candidate loading, coefficient prediction, and curve reconstruction helpers.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
  - Track 2 comparison runner.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  - canonical Track 2 matrix configuration.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - canonical Track 2 report to refresh after implementation.

## Implementation Steps

1. Add a composed-reference candidate representation that maps each
   `amplitude` or `phase` harmonic target to one source family inventory.
2. Add five generated composite candidates to the full Track 2 matrix:
   `paper_original_best_Fw`, `paper_retuned_best_Fw`, `track1_best_Fw`,
   `paper_retuned_best_Bw`, and `track1_best_Bw`.
3. Reuse the existing source-specific `h0` compatibility rule for any composed
   candidate entry that pulls `h0` from `rcim_track1` forward.
4. Reconstruct TE curves by dispatching each harmonic target prediction to the
   selected family inventory, then combining the predicted coefficients through
   the existing Track 2 reconstruction path.
5. Extend validation summaries and reports so the composed candidates appear in
   the relevant `original`, `original retuned`, and `track 1` groups.
6. Regenerate the full Track 2 validation matrix and grouped PNG previews.
7. Refresh `RCIM Paper Reference Benchmark.md`,
   `Track 2 Directional Model Comparison.md`, and
   `Training Results Master Summary.md` with the composed-candidate results.
8. Run scoped Python compilation and Markdown QA before asking for commit
   approval.
