# Overview

This technical document plans the next reorganization pass for the recovered
RCIM workflow and the surrounding paper-reimplementation script surface.

The current reorganization already achieved these goals:

- one recovered-original workflow instead of competing copied roots;
- three recovered stages:
  - `dataframe_creation/`
  - `training/`
  - `evaluation/`
- dedicated workflow subfolders across
  `scripts/paper_reimplementation/rcim_ml_compensation/`.

The user now wants a second pass focused on file naming and export-facing
coherence.

The concrete request is to rename original-style script names such as:

- `0-main_createDFforPrediction.py` -> `create_dataframe.py`
- `0-statistic.py` -> `statistics.py`

and extend the same logic across the reorganized recovered workflow and, where
appropriate, the surrounding workflow folders.

The user also asked for a rationale for the repository-owned wrapper runner
that was introduced during the first reorganization pass.

## Technical Approach

The rename pass should improve repository coherence without losing the ability
to inspect the copied recovered code and without breaking the script and export
surface that now depends on the new folder taxonomy.

The main design goals are:

1. replace legacy ordinal or mixed-style filenames with repository-consistent
   descriptive names;
2. keep import relationships valid after renaming;
3. keep the recovered-original workflow README, script notes, guide pages, and
   Sphinx API pages aligned with the new names;
4. preserve the code-level mapping to the original recovered files so readers
   can still understand what each renamed file came from;
5. ensure the repository-owned wrapper and export paths continue to work after
   the rename.

For the recovered-original workflow, the likely target names are:

- `dataframe_creation/0-main_createDFforPrediction.py`
  -> `dataframe_creation/create_dataframe.py`
- `dataframe_creation/0-statistic.py`
  -> `dataframe_creation/statistics.py`
- `training/main_prediction_v17.py`
  -> `training/train_and_export_models.py`
- `training/predictorML_v7.py`
  -> `training/predictor_multioutput.py`
- `evaluation/0-statistic.py`
  -> `evaluation/statistics.py`
- `evaluation/2-main_evaluatePrediction_v4.py`
  -> `evaluation/evaluate_predictions.py`
- `evaluation/2-main_evaluateSignals.py`
  -> `evaluation/evaluate_signals.py`

The wrapper runner itself should also be reviewed for naming consistency, but
it should remain repository-owned rather than pretending to be an original
recovered file.

The export-alignment part of the pass should specifically check:

- ONNX export directory naming;
- prediction CSV directory naming;
- references in README and script notes;
- any remaining hardcoded original-style path fragments that became misleading
  after the first reorganization.

## Involved Components

Primary recovered-original workflow files:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/dataframe_creation/0-main_createDFforPrediction.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/dataframe_creation/0-statistic.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training/main_prediction_v17.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training/predictorML_v7.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluation/0-statistic.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluation/2-main_evaluatePrediction_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluation/2-main_evaluateSignals.py`

Likely documentation surfaces to update:

- `doc/README.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/`
- `doc/guide/project_usage_guide.md`
- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `site/api/paper_reimplementation/`
- `site/guide/project_usage_guide.md`

Related repository-owned workflow folders that may need naming review for
consistency:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`

No subagent use is planned. If that changes, explicit user approval will be
requested before any launch.

## Implementation Steps

1. Enumerate the recovered-original stage files that still use legacy
   ordinal-style or mixed-style names.
2. Rename those files to descriptive repository-consistent names and update all
   imports, wrapper references, and documentation pointers.
3. Review whether the surrounding workflow folders also need small naming
   alignments for symmetry with the recovered workflow.
4. Check ONNX export and prediction-export path logic after renaming so the
   reorganization does not break artifact generation.
5. Refresh the recovered-original README and related analysis notes so the new
   names remain traceable back to the original recovered files.
6. Run scoped verification:
   - `py_compile` on touched Python files;
   - at least one recovered-original smoke run;
   - Markdown QA on touched Markdown files;
   - Sphinx rebuild if portal-facing source files change again.
7. Report completion and wait for explicit commit approval before creating any
   Git commit.
