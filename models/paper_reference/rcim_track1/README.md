# RCIM Track 1 Paper Reference Models

This folder groups curated paper-reference model archives for the canonical
`Track 1` RCIM paper-reimplementation branch.

Current family archives:

- `svm_reference_models/`

Canonical family archive template:

- `<family>_reference_models/README.md`
- `<family>_reference_models/reference_inventory.yaml`
- `<family>_reference_models/onnx/amplitude/`
- `<family>_reference_models/onnx/phase/`
- `<family>_reference_models/python/amplitude/`
- `<family>_reference_models/python/phase/`
- `<family>_reference_models/data/`
- `<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`

Benchmark integration rule for every future family archive:

- add one dedicated family section to
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
- list the accepted `Track 1` targets, accepted metrics, canonical source run,
  archived `ONNX` path, and any surrogate-export note;
- point the family section to the archive root, inventory, dataset snapshot
  manifest, and reconstruction references.

The long-term target is to extend this root with the remaining paper families:

- `mlp_reference_models/`
- `rf_reference_models/`
- `dt_reference_models/`
- `et_reference_models/`
- `ert_reference_models/`
- `gbm_reference_models/`
- `hgbm_reference_models/`
- `xgbm_reference_models/`
- `lgbm_reference_models/`

The current `svm_reference_models/` package is the template instance to copy
for future family closures.
