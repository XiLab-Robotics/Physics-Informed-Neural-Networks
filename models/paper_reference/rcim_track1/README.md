# RCIM Track 1 Paper Reference Models

This folder groups curated paper-reference model archives for the canonical
`Track 1` RCIM paper-reimplementation branch.

Direction branches:

- `forward/`
- `backward/`

Current populated family archives under `forward/`:

- `forward/svm_reference_models/`
- `forward/mlp_reference_models/`
- `forward/rf_reference_models/`
- `forward/dt_reference_models/`
- `forward/et_reference_models/`
- `forward/ert_reference_models/`
- `forward/gbm_reference_models/`
- `forward/hgbm_reference_models/`
- `forward/xgbm_reference_models/`
- `forward/lgbm_reference_models/`

Canonical family archive template:

- `<direction>/<family>_reference_models/README.md`
- `<direction>/<family>_reference_models/reference_inventory.yaml`
- `<direction>/<family>_reference_models/onnx/amplitude/`
- `<direction>/<family>_reference_models/onnx/phase/`
- `<direction>/<family>_reference_models/python/amplitude/`
- `<direction>/<family>_reference_models/python/phase/`
- `<direction>/<family>_reference_models/data/`
- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`

Benchmark integration rule for every future family archive:

- add one dedicated family section to
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- list the accepted `Track 1` targets, accepted metrics, canonical source run,
  archived `ONNX` path, and any surrogate-export note;
- point the family section to the archive root, inventory, dataset snapshot
  manifest, and reconstruction references.

The current repository now treats the `forward/` branch as the canonical
benchmark asset surface completed so far. The `backward/` branch is reserved
for the future rebuild sourced from the original dataset under `data/datasets/`.
