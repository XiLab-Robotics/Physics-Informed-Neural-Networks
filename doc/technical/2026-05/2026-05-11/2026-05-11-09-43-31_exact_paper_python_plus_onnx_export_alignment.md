# Exact-Paper Python Plus ONNX Export Alignment

## Overview

The current exact-paper reimplementation persists the full fitted family bank
as one bundle artifact and exports per-target ONNX files, but it does not also
persist one per-target Python estimator artifact alongside each ONNX export.
The recovered original workflow does both, writing a `.pkl` Python artifact
for every exported target estimator before attempting the ONNX conversion.

## Technical Approach

Align the exact-paper export surface with the recovered original workflow so
every exact-paper export stage always materializes:

1. the existing bank-level `paper_family_model_bank.pkl` bundle;
2. per-target Python estimator artifacts; and
3. per-target ONNX artifacts.

The change should preserve the current mathematical workflow and only extend
the export artifact contract. Export summaries and validation reports should be
updated so the Python export surface is explicit and auditable.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Re-read the recovered original export path and capture the exact artifact
   contract for Python plus ONNX per-target exports.
2. Extend the shared exact-paper export helper so it always writes the Python
   estimator artifact before ONNX conversion, mirroring the recovered workflow.
3. Update export summaries, validation summaries, and operator-facing docs so
   the Python export surface is visible and expected.
4. Re-run a narrow exact-paper validation check and Markdown QA on the touched
   documentation scope.
