# Track 1 Reference Family Archive Standardization

## Overview

The repository now has a curated `SVM` paper-reference archive under
`models/paper_reference/rcim_track1/forward/svm_reference_models/`, plus canonical
benchmark documentation that identifies the accepted `Track 1` reference models
and their reconstruction provenance.

This work should be formalized as a reusable standard for every remaining
`Track 1` paper family:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The goal is to make the `SVM` organization pattern the canonical archive and
documentation contract for all `Track 1` paper-reference families, so future
family closures follow one deterministic structure instead of ad hoc per-family
layouts.

## Technical Approach

The standardization will promote the current `SVM` archive into a family-agnostic
`Track 1` reference package pattern.

Each family archive will be expected to provide:

- a family root under
  `models/paper_reference/rcim_track1/<family>_reference_models/`;
- a dedicated `README.md`;
- a machine-readable `reference_inventory.yaml`;
- deployment-facing `onnx/` exports grouped into `amplitude/` and `phase/`;
- Python-usable fitted estimators grouped into `python/amplitude/` and
  `python/phase/`;
- a tracked dataset snapshot and dataset manifest;
- copied source-run config and metadata snapshots;
- copied split manifests for deterministic reconstruction;
- explicit references from the canonical benchmark document.

The implementation should also formalize benchmark-side expectations:

- `RCIM Paper Reference Benchmark.md` should have one dedicated section per
  paper family once that family is archived;
- each section should list the accepted `Track 1` reference targets for the
  family, their canonical source run, accepted metrics, and archived model
  paths;
- the benchmark should use consistent language for archive root, inventory,
  dataset snapshot, reconstruction references, and implementation notes.

The standardization should further define a repeatable provenance contract for
future families:

- exact fitted estimator parameters serialized per target when possible;
- explicit source bundle path;
- dataset hash and snapshot path;
- feature list and target list;
- train/test row counts and exact split indices;
- test size, random seed, harmonic filter, and target-scope mode;
- clear handling notes when exported deployment artifacts use a surrogate
  estimator surface that differs from the original Python-side fitted model.

## Involved Components

- `models/paper_reference/README.md`
- `models/paper_reference/rcim_track1/README.md`
- `models/paper_reference/rcim_track1/forward/svm_reference_models/`
- future family roots under `models/paper_reference/rcim_track1/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-17/README.md`

## Implementation Steps

1. Formalize the `Track 1` family archive contract in the `models/paper_reference/`
   documentation so the `SVM` layout becomes the canonical template.
2. Add a reusable family-standard section to the canonical benchmark guidance so
   future family sections follow one reporting pattern.
3. Align the `rcim_track1` archive README with the family-wide structure and
   naming convention.
4. Keep the current `SVM` archive as the first fully populated reference
   instance and declare it as the template implementation for future families.
5. Validate the touched Markdown scope before closing the task.
