# SVM Reference Models Full Regeneration Provenance

## Overview

This technical document formalizes the final provenance-completion step needed
to make the curated `SVM` reference archive fully regenerable in practice and
fully auditable in writing.

The current repository already contains:

- the canonical `19` `SVM` reference ONNX artifacts;
- the benchmark-side inventory of the accepted `SVM` reference row;
- the source run, config, and validation artifact references for each
  accepted target.

The remaining gap is that the archive is not yet self-sufficient for a
`100%` faithful reconstruction workflow without additional interpretation.

To close that gap, the repository should preserve and serialize, in one place,
all of the following for the canonical `SVM` reference set:

- the exact training-data provenance used by each accepted target;
- the split and seed configuration used to fit it;
- the exact target scope used by the source run;
- the Python-usable model artifacts, not only ONNX exports;
- the reconstruction ledger needed to reproduce the same accepted model
  outputs again later.

No subagent usage is planned for this work.

## Technical Approach

The provenance-completion task should extend the current
`models/paper_reference/rcim_track1/svm_reference_models/` archive into a
dual-format, reconstruction-grade package.

The approved implementation should do five things:

1. Preserve a Python-usable artifact surface for the canonical `SVM`
   reference models in addition to ONNX.
   The preferred repository-native format is a curated Python-side serialized
   artifact copied from the source exact-paper model bundles or reconstructed
   from them into a smaller family-target archive, rather than relying on ONNX
   alone.
2. Serialize a canonical training-data provenance record, including:
   - source dataframe path;
   - filtered row count;
   - train row count;
   - test row count;
   - split fraction;
   - seed;
   - input feature list;
   - target name;
   - target scope mode;
   - harmonic filter.
3. Serialize the exact implementation references needed for regeneration:
   - validation script path;
   - support-module path;
   - source config path;
   - source validation-summary path;
   - source run instance id;
   - export estimator name;
   - surrogate strategy when applicable.
4. Extend the current inventory so that each of the `19` targets has an
   explicit regeneration record with both:
   - ONNX archived path;
   - Python archived path.
5. Update the benchmark narrative and the archive README so they explicitly
   state that the repository now has a fully reconstructible `SVM` reference
   archive and clarify any remaining limits, if a limit cannot be eliminated.

The implementation should avoid copying oversized bundle artifacts blindly.
If the monolithic `paper_family_model_bank.pkl` remains too large for the
curated archive, the task should extract the per-target or per-run Python-side
artifacts needed for reconstruction into a smaller structured archive instead
of duplicating the full monolithic bundle unchanged.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `models/.gitignore`
- `models/README.md`
- `models/paper_reference/README.md`
- `models/paper_reference/rcim_track1/README.md`
- `models/paper_reference/rcim_track1/svm_reference_models/README.md`
- `models/paper_reference/rcim_track1/svm_reference_models/reference_inventory.yaml`
- `models/paper_reference/rcim_track1/svm_reference_models/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

## Implementation Steps

1. Inspect the source exact-paper model bundles and determine the smallest
   Python-usable artifact unit that can be archived safely for the `19`
   canonical `SVM` references.
2. Create the Python-side archive layout under
   `models/paper_reference/rcim_track1/svm_reference_models/`.
3. Populate the archive with both:
   - ONNX reference artifacts;
   - Python-usable serialized model artifacts.
4. Extend `reference_inventory.yaml` with the full regeneration ledger for
   each target.
5. Update the benchmark section and archive README to state the new
   reconstruction guarantee clearly.
6. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
