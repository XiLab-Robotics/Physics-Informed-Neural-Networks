# Track 1 Full Matrix Paper Replication Dashboard

## Overview

This technical document corrects the interpretation of the requested
`Track 1` dashboard.

The previous dashboard direction focused too much on:

- best repository result per harmonic;
- closure summaries derived from the current best run;
- compressed status views inspired by Tables `3-6`.

That is not the primary first target of `Track 1` as clarified by the user.

The clarified first `Track 1` target is:

- reproduce the full paper result matrices for the same model families;
- reproduce them separately for amplitude and phase prediction;
- preserve the same paper-style layout where each row is one model family and
  each column is one harmonic;
- show our repository results in a directly analogous matrix;
- highlight each repository cell as:
  - `green` when the paper result is reached or beaten;
  - `yellow` when it is close or still acceptable for follow-up;
  - `red` when it is not yet reproduced.

Concretely, the immediate dashboard priority is:

1. Table `3` full amplitude matrix replication;
2. Table `4` full phase matrix replication;
3. then the same paper-facing treatment for the remaining related tables.

This means the primary reading surface must show, for every tested family:

- `SVM`
- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

across every harmonic column used by the paper, not only the harmonic-wise
winner or best-family envelope.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The dashboard must be reframed from a `best achieved` view into a
`paper-matrix replication` view.

The canonical document may still remain
`doc/reports/analysis/RCIM Paper Reference Benchmark.md`, but its new section
must be organized around direct matrix replication first.

Required dashboard structure:

1. show the repository-owned reconstruction of the original paper table;
2. show one repository matrix with the same row and column structure;
3. in the repository matrix, each cell must correspond to:
   - the same model family row;
   - the same harmonic column;
   - the same metric type as the paper table;
4. add a same-shape status matrix or inline cell status markers so the user can
   see immediately which paper cells have already been replicated and which are
   still missing.

Immediate table mapping:

- Table `3`
  amplitude `RMSE` full matrix for all listed model families and harmonics;
- Table `4`
  phase-side matrix in the same paper row/column style;
- Table `5`
  second phase metric matrix in the same paper row/column style;
- Table `6`
  harmonic-selected summary remains useful, but it is a downstream summary and
  must not replace the full-matrix replication view;
- Table `2`
  may be included as contextual paper-side summary, but it is not the primary
  replication target compared with the full matrices of Tables `3-5`.

Repository consequence:

- the current `best per harmonic` comparison remains useful as a secondary
  summary;
- but the primary `Track 1` dashboard must now answer:
  `For each paper model family and each harmonic, did we reproduce the paper
  cell or not?`

This likely requires the repository table surface to serialize, per family and
per harmonic:

- our reproduced metric value;
- the paper target value;
- the gap versus paper;
- the traffic-light status.

For readability, the dashboard may use one of these two layouts:

1. one numeric matrix plus one aligned color-status matrix; or
2. one matrix where each cell contains the repository value together with a
   compact status marker.

The first implementation should prefer the more readable option after checking
real table width in Markdown and PDF views.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/validation_checks/track1/exact_paper/forward/shared/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`
- `doc/reports/analysis/validation_checks/track1/exact_paper/forward/shared/2026-04-13-22-09-00_paper_reimplementation_rcim_exact_model_bank_exact_open_cell_paper_family_reference_campaign_run_exact_paper_model_bank_report.md`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/open_cell_repair/shared/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/validation_summary.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `doc/README.md`

## Implementation Steps

1. Reframe the canonical `Track 1` dashboard around full paper-matrix
   replication rather than best-per-harmonic closure only.
2. Build the repository-owned dashboard for Table `3` first:
   - original paper matrix;
   - repository replicated matrix with the same model rows and harmonic
     columns;
   - explicit per-cell status.
3. Apply the same structure to Table `4`.
4. Extend the same replication surface to Table `5`.
5. Keep Tables `6` and `2` as supporting summary/context tables rather than as
   substitutes for the full matrices.
6. Define and document the exact `green / yellow / red` policy for matrix
   cells in a way that can be reused after every future `Track 1` update.
7. Update the benchmark report so future `Track 1` progress must refresh these
   matrices after every material improvement.
8. Run Markdown warning checks on the touched Markdown files and confirm clean
   trailing newline state before closing the task.

Implementation must not begin until the user explicitly approves this
technical document, per repository policy.
