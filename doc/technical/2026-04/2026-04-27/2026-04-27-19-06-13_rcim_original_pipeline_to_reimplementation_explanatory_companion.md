# Overview

This technical document plans one explanatory companion document to place
beside the RCIM exact-paper reimplementation.

The user request is not for another short audit note. The request is for a
deep implementation-facing guide that explains, with concrete code detail:

- how the recovered original prediction pipeline actually works;
- what `predictorML_v7.py` contains beyond the single `v18` branch;
- how the exact-paper repository reimplementation maps onto that original
  workflow;
- which parts are equivalent in modeling intent;
- which parts are explicit engineering reinterpretations rather than literal
  line-by-line ports.

The target audience is someone reading the original recovered code and the
repository reimplementation side by side and needing a durable written guide to
understand what to inspect and how to compare the two code paths correctly.

## Technical Approach

The new companion document will be written as a readable analysis report under
`doc/reports/analysis/` rather than as a launcher note or a technical-only
scratch document.

The document will not replace the existing workflow report or the existing
audit report. Instead it will sit between them:

- more code-detailed than `RCIM Exact Paper Model Bank Workflow.md`;
- more explanatory and pedagogical than
  `RCIM Original Pipeline And Reimplementation Audit.md`.

The planned structure is:

1. explain the original `1-main_prediction_v18.py` flow block by block;
2. explain the role and internal structure of `1-predictorML_v7.py`;
3. identify which classes and methods are active in the `v18` path and which
   are alternative or historical branches;
4. explain the matching reimplementation path through:
   - `run_exact_paper_model_bank_validation.py`;
   - `exact_paper_model_bank_support.py`;
5. map original stages to reimplementation stages:
   - dataframe loading and target selection;
   - family registry and estimator construction;
   - `MultiOutputRegressor` fitting;
   - held-out evaluation;
   - ONNX export;
   - artifact/report generation;
6. state clearly where the reimplementation is:
   - intentionally faithful;
   - structurally refactored;
   - methodologically widened beyond the original script.

The document should keep the strongest level of code traceability possible by
using exact filenames, function names, and code responsibilities, but it should
avoid turning into a raw line-by-line dump of either file.

## Involved Components

Primary original-code references:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-main_prediction_v18.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-predictorML_v7.py`
- optional support context from:
  - `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/main_prediction_v17.py`
  - `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/predictorML_v7.py`

Primary repository reimplementation references:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- secondary context from:
  - `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`
  - `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank_support.py`

Existing related documents to align with:

- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_recovered_original_pipeline.md`

No subagent use is planned. If that changes, explicit user approval will be
requested before any launch.

## Implementation Steps

1. Create a new readable analysis report under `doc/reports/analysis/` focused
   on explanatory side-by-side understanding of the original pipeline and the
   repository reimplementation.
2. Explain the original `v18` runner block by block, including dataset load,
   family list construction, loop semantics, and saved outputs.
3. Explain the internal architecture of `predictorML_v7.py`, separating:
   - the `v18`-active path;
   - alternative multioutput branches;
   - tuning and export branches;
   - historical or experimental utility branches.
4. Explain the reimplementation flow block by block, showing where the old
   monolithic logic was redistributed across support functions.
5. Add a precise original-to-reimplementation mapping section that makes clear
   what stayed conceptually the same and what changed in implementation shape.
6. Register the new analysis report in `doc/README.md`.
7. Run scoped Markdown QA on the touched Markdown files before closing the
   task.
