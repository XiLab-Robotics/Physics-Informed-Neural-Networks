# 2026-04-29-00-45-52 Rcim Original Pipeline Author Conversation Formalization

## Overview

The repository now contains a newly recovered full RCIM original pipeline root
under:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`

This new root materially changes the recovered-code understanding because it
contains:

- the full top-level training, dataframe-creation, and evaluation scripts in
  one flat operational workspace;
- `instance_v4.py` and `instance_v5.py`;
- `instances_V3/` pickle artifacts used by the original workflow;
- shipped forward and backward dataframe CSVs;
- `output_prediction/`, `evaluation/`, and `model_output_dir/` execution
  artifacts;
- an author-provided `README.md` describing the intended usage;
- direct clarifications from the original authors about how the workflow was
  actually used.

The user also supplied an email-style conversation with the authors. That
conversation is now part of the recovered evidence surface and should be
formalized into the repository's canonical understanding of:

- what the CSVs represent;
- which script variant was used for export versus paper evaluation;
- what the `deg <= 35` filter means;
- how the `.pickle` cache is expected to be created and reused;
- what the evaluation scripts were used for in the paper.

## Technical Approach

The work should treat the new original pipeline root and the author
conversation as primary reference evidence and update the repository-facing
documentation accordingly.

The main documentation outcome should be:

1. refresh the recovered-assets root description so the canonical
   `original_pipeline/` root is described as the author-supplied full
   operational folder, not as a placeholder;
2. update the recovered-asset summary and main analysis reports so they
   reflect the flat operational layout actually received from the authors;
3. capture the author clarifications as explicit repository-owned facts, while
   keeping a distinction between:
   - direct author statements;
   - observed code facts;
   - repository-side inferences.

The new formalized knowledge should include these points.

From the author conversation:

- `0-main_createDFforPrediction.py` is the entry point used to create the
  prediction dataframe CSVs from the original dataset.
- The CSVs are not simple forward/backward splits of the raw dataset; they
  already contain FFT-derived harmonic amplitude and phase features selected as
  the most informative harmonics.
- `1.1-main_prediction_v17.py` is the structure used for final model export on
  the whole dataset.
- `1-main_prediction_v18.py` is the structure used to train models with
  already optimized hyperparameters as used in the paper experiments.
- To repeat hyperparameter optimization on a new dataset, the operative method
  is to use `predictorMLCrossValidationWithHyperparameter` in the
  `MLModelMultipleOutput` class in place of `predictorML_allForExport`, with a
  test-set percentage of `0.20`.
- The `deg <= 35` filter is likely a legacy leftover because the later
  generated CSVs should already exclude temperatures above `35`; this still
  needs empirical checking against the shipped CSV values.
- `2-main_evaluatePrediction_v4.py` was used to rework `output_prediction`
  artifacts into the paper tables.
- The original author used `.pickle` files as a speed-up cache. If the pickle
  is present, the dataframe-creation script reuses it; otherwise it reads the
  CSVs and creates the pickle automatically.

From the newly recovered original pipeline root:

- the actual top-level layout is flat, not split into the previously archived
  `0-dfCreation/`, `1-prediction/`, and `2-evaluation/` folders;
- both dataframe CSVs and execution artifacts are preserved in the folder;
- the root contains a shipped `README.md` written by the authors, which is now
  part of the canonical usage evidence;
- the root includes `instances_V3/` pickle artifacts, which resolves the
  earlier uncertainty about how the original team accelerated data loading.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`
- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- any README or note that still describes `original_pipeline/` as an empty
  placeholder or still assumes only the old split-fragment backup roots

## Implementation Steps

1. Inspect the new `original_pipeline/` root and extract the actual flat file
   layout, shipped artifacts, and execution assumptions from the author README.
2. Translate the author conversation into a repository-owned evidence summary
   that distinguishes author statements from direct code observations.
3. Update the canonical recovered-assets README to describe:
   - the new full original pipeline root;
   - the older split fragment backups;
   - the practical meaning of `v17`, `v18`, `predictorML_allForExport`, and
     `predictorMLCrossValidationWithHyperparameter`.
4. Update the main recovered-asset summary and analysis reports so their code
   descriptions and file pointers reflect the new original root correctly.
5. Flag any still-open ambiguity that may require one more targeted question to
   the authors or one more empirical check on the shipped CSVs and artifacts.
6. Run Markdown QA on all touched repository-owned Markdown files before
   closing the task.
