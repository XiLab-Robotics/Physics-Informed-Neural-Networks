# RCIM Recovered Assets - Project Summary

## Source

- Recovered exact ONNX models:
  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`
- Recovered original code:
  `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- Recovered later code snapshot:
  `reference/rcim_ml_compensation_recovered_assets/code/backup_latest_snapshot_fragment/`
- Recovered backup assets:
  `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy_early_snapshot/`
  and
  `reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/`
  and `reference/rcim_ml_compensation_recovered_assets/backup/onnx_variants/`
- Recovered TwinCAT XML exports:
  `reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml/`
- Recovered instance archive:
  `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`

Important clarification:

- the recovered asset root remains generic because the code and backup surface
  is generic recovered material;
- the exact ONNX paper release and the shipped `Fw` dataframe currently stored
  under this root are `forward` only.

## What The Recovered Assets Actually Say

- The paper workflow is genuinely harmonic-wise.
- The recovered exact ONNX release is organized by model family and by target
  type `ampl` and `phase`.
- The exact recovered harmonic set is:
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`.
- The recovered original code is staged as:
  dataframe creation, prediction/export, and evaluation.
- The full author-supplied original root now lives under
  `code/original_pipeline/`, while the older split staged reconstruction
  remains archived under `code/backup_split_original_pipeline_fragment/`.
- The main recovered input columns are `rpm`, `deg`, and `tor`.
- The shipped original root now includes both `Fw` and `Bw` dataframe CSVs,
  both with `969` rows and `20` harmonic targets.
- Both shipped CSVs already contain only `deg = 25, 30, 35`, which supports
  the author statement that the later dataset versions already excluded
  temperatures above `35` degrees.
- The TwinCAT XML exports confirm that a PLC-facing export path existed in the
  paper ecosystem.
- The author guidance distinguishes:
  - `1.1-main_prediction_v17.py` for whole-dataset export;
  - `1-main_prediction_v18.py` for paper-side training with already optimized
    parameters;
  - `predictorMLCrossValidationWithHyperparameter` as the method to reuse when
    retuning hyperparameters on a new dataset.

## Why It Matters For This Repository

- It confirms that `Track 1` is correctly positioned as a harmonic-wise paper
  reimplementation branch.
- It clarifies that the currently recovered `Track 1` paper asset surface is
  the forward-only branch, not a combined forward/backward bank.
- It gives us exact recovered ONNX artifacts for the paper families, instead
  of relying only on textual interpretation of the paper.
- It provides original code snapshots that can be mined for:
  target parameterization,
  export patterns,
  evaluation logic,
  and deployment constraints.
- It strengthens the repository-owned paper comparison because we now have
  source-code and model artifacts, not only the paper PDF.

## What Is Already Implemented Here

- The repository already has the paper PDF and a high-level summary.
- The repository already has a paper-faithful harmonic-wise offline pipeline
  under `scripts/paper_reimplementation/rcim_ml_compensation/`.
- The repository already tracks paper-vs-repository status in
  `RCIM Paper Reference Benchmark.md`.

## What Remains Missing, Risky, Or Uncertain

- The heavy `instance_v1` pickle archive is preserved, but not yet fully
  runnable because the recovered class environment is incomplete.
- The recovered later code snapshot fragment and the exact paper release are
  related, but not identical, so they must not be merged conceptually.
- The author README text refers to `1-main_prediction_v17.py`, but the shipped
  file is named `1.1-main_prediction_v17.py`; this appears to be a naming
  mismatch in the note, not a second missing file.
- The recovered package does not currently contain the backward-side model bank
  implied by the generalized paper notation.
- The shipped evaluation entrypoint `2-main_evaluatePrediction_v4.py` is still
  forward-coded in practice because it calls `predicted_TE_Fw_*` methods and
  points to `output_prediction/instV3.8_Fw_allFreq_def/`.
- The backup ONNX bundles contain historical variants and experimental branches,
  so they should not be mistaken for the exact paper benchmark without explicit
  mapping.
- The recovered TwinCAT XML exports are useful evidence, but they do not yet
  mean that the repository has a working end-to-end online compensation branch.
