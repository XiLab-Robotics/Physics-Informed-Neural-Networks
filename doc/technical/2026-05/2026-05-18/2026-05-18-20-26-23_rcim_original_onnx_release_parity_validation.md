# RCIM Original ONNX Release Parity Validation

## Overview

This technical note plans a forward-only parity validation for the recovered
paper-original ONNX release under
`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`.

The goal is to evaluate those original ONNX models in the same local testing
context used for the current repository reimplementation:

- same dataset configuration and forward-only split;
- same seed and deterministic split policy;
- same `Tables 2-5` target metrics;
- same `Track 2` curve-reconstruction evaluation used for
  `models/paper_reference/rcim_original/forward`.

The validation is an evaluation-only workflow. It must not retrain models or
mutate the recovered reference assets.

## Technical Approach

Add an ONNX-backed paper-reference candidate surface that mirrors the existing
Python artifact surface for `rcim_original` forward models. The implementation
will use `onnxruntime.InferenceSession` with `CPUExecutionProvider`, resolve the
first input name from the loaded graph, pass NumPy `float32` feature arrays, and
read the first output tensor as the prediction vector.

The parity workflow will produce two comparison layers:

1. `Tables 2-5` split evaluation:
   - evaluate each ONNX family/target artifact on the exact forward test split;
   - compare target-level `MAE` and `RMSE` against the repository
     `rcim_original` forward Python artifact metrics and the paper table
     targets already carried by the benchmark.
2. `Track 2` curve-reconstruction evaluation:
   - expose the ONNX release as a source group parallel to
     `rcim_original`;
   - evaluate it on the same forward curves, denominator, and plotting path
     used by the current Track 2 validation;
   - report deltas against `models/paper_reference/rcim_original/forward`.

The recovered ONNX release currently contains `201` `.onnx` files. The expected
paper surface is `10` families times `20` target models, so the manifest step
must flag and handle the extra `RF/ampl/RandomForestRegressor_ampl240 (1).onnx`
duplicate explicitly.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`
  - immutable recovered original ONNX source artifacts.
- `models/paper_reference/rcim_original/forward`
  - current repository paper-original forward Python/ONNX archive used as the
    parity baseline.
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/baseline_forward.yaml`
  - canonical forward split, seed, target scope, and selected harmonics for the
    `Tables 2-5` evaluation.
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/`
  - existing exact-paper split, target, metric, and table-report machinery.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  - existing Track 2 curve-reconstruction comparison pipeline.
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
  - benchmark report to receive the ONNX release parity findings after
    validation.
- `doc/reports/analysis/Track 2 Directional Model Comparison.md`
  - Track 2 report to receive the ONNX release forward comparison findings.

## Implementation Steps

1. Build a deterministic ONNX release manifest keyed by family, target kind,
   and harmonic, with duplicate-file detection and an explicit duplicate policy.
2. Add a small ONNX inference adapter that loads one model with ONNX Runtime,
   runs CPU inference from canonical feature arrays, and normalizes prediction
   shape for the existing metric code.
3. Add a forward-only ONNX release validation entry point that reuses the
   `baseline_forward.yaml` dataset split and computes the same `Tables 2-5`
   metrics as the current exact-paper pipeline.
4. Extend the Track 2 loader with an ONNX-backed source kind, or add a narrow
   Track 2 ONNX parity runner if that is cleaner than broadening the canonical
   matrix immediately.
5. Write output under `output/validation_checks/track2_reference_comparison/`
   or a sibling validation root with an immutable timestamped run instance.
6. Generate a parity report with:
   - ONNX release inventory status;
   - `Tables 2-5` metric deltas versus `rcim_original` forward artifacts;
   - Track 2 curve metric deltas versus `rcim_original` forward artifacts;
   - any failed or unsupported ONNX files.
7. Refresh the canonical benchmark and Track 2 report only after the validation
   output is produced and inspected.
8. Run Python compilation, scoped Markdown QA, and Sphinx build checks before
   requesting commit approval.
