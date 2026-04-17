# SVM Reference Model Inventory And Archive

## Overview

This technical document formalizes a repository-owned inventory and archive
workflow for the canonical `SVM` paper-reference models used in
`Track 1`.

The immediate goal is to make the `SVM` reference surface explicit and
reconstructible in two places:

- a dedicated section inside
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- a dedicated archive area under `models/` that preserves a curated copy of
  the reference model artifacts together with the provenance needed to rebuild
  them faithfully.

The requested `SVM` inventory contains:

- `10` amplitude reference models for harmonics
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `9` phase reference models for harmonics
  `1, 3, 39, 40, 78, 81, 156, 162, 240`.

The same documentation and archive pattern is intended to become the canonical
template for the remaining paper families:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

No subagent usage is planned for this work.

## Technical Approach

The implementation should promote one explicit repository-owned canonical
source for the `SVM` reference-model inventory rather than reconstructing the
`19` models manually from scattered reports.

The current best candidate source is the strict exact-paper full-bank
validation artifact:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro/validation_summary.yaml`

That artifact already preserves:

- the paper target schema and harmonic order list;
- the enabled family list;
- the exact `SVR` ONNX export paths for each amplitude and phase target;
- the `paper_family_model_bank.pkl` bundle path;
- the shared training configuration and dependency versions.

The approved implementation should therefore:

1. add a dedicated `SVM Reference Models` section to
   `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
2. enumerate the `19` canonical `SVM` targets explicitly with:
   - harmonic order;
   - target kind (`amplitude` or `phase`);
   - paper table role;
   - canonical model artifact path;
   - source validation run;
   - training-config reference;
   - implementation-code reference;
   - parameter provenance reference;
3. create a new curated archive under `models/` for the `SVM` reference
   inventory;
4. add a dedicated archive `README.md` that records:
   - source run instance;
   - source validation summary;
   - source config path;
   - relevant training/validation scripts;
   - exact family name mapping (`SVM` paper row -> `SVR` implementation);
   - expected artifact naming convention;
   - reconstruction instructions and provenance notes;
5. update `models/README.md` so the new archive area becomes a documented,
   discoverable repository entry point.

The archive should prefer a family- and target-explicit structure such as:

- `models/paper_reference/rcim_track1/svm_reference_models/README.md`
- `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/`
- `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/`

The archive is expected to preserve copied reference artifacts only after the
source paths have been verified to exist and to correspond to the canonical
`SVM` row currently accepted in the benchmark.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `models/README.md`
- `models/paper_reference/rcim_track1/svm_reference_models/`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-17/README.md`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro/validation_summary.yaml`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro/training_config.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

## Implementation Steps

1. Confirm the canonical exact-paper validation artifact and enumerate the
   `19` `SVM` reference targets from that source.
2. Create the curated `models/paper_reference/rcim_track1/svm_reference_models/`
   archive structure and its dedicated provenance `README.md`.
3. Copy or curate the verified `SVM` reference model artifacts into the new
   archive while preserving traceable filenames.
4. Extend `RCIM Paper Reference Benchmark.md` with a dedicated section listing
   all `19` reference models and their provenance.
5. Update `models/README.md`, `doc/technical/2026-04/2026-04-17/README.md`,
   and `doc/README.md` so the new archive and technical document are
   discoverable.
6. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
