# RCIM Recovered Assets - Project Summary

## Source

- Recovered exact ONNX models:
  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`
- Recovered original code:
  `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- Recovered later code snapshot:
  `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- Recovered backup assets:
  `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy/`
  and `reference/rcim_ml_compensation_recovered_assets/backup/onnx_variants/`
- Recovered TwinCAT XML exports:
  `reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml/`
- Recovered instance archive:
  `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`

Important clarification:

- the current path name is legacy and will be renamed after campaign closeout;
- the assets currently stored under this root are the recovered `forward`
  assets only.

## What The Recovered Assets Actually Say

- The paper workflow is genuinely harmonic-wise.
- The recovered exact ONNX release is organized by model family and by target
  type `ampl` and `phase`.
- The exact recovered harmonic set is:
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`.
- The recovered original code is staged as:
  dataframe creation, prediction/export, and evaluation.
- The main recovered input columns are `rpm`, `deg`, and `tor`.
- The recovered dataframe and prediction entrypoints are explicitly `Fw`
  forward-side artifacts.
- The TwinCAT XML exports confirm that a PLC-facing export path existed in the
  paper ecosystem.

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
- The recovered later code snapshot and the exact paper release are related,
  but not identical, so they must not be merged conceptually.
- The recovered package does not currently contain the backward-side model bank
  implied by the generalized paper notation.
- The backup ONNX bundles contain historical variants and experimental branches,
  so they should not be mistaken for the exact paper benchmark without explicit
  mapping.
- The recovered TwinCAT XML exports are useful evidence, but they do not yet
  mean that the repository has a working end-to-end online compensation branch.
