# RCIM Track 1 Paper Reference Models

This folder groups curated paper-reference model archives for the canonical
`Track 1` RCIM paper-reimplementation branch.

Direction branches:

- `forward/`
- `backward/`

Current populated family archives under both directions:

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
- `backward/svm_reference_models/`
- `backward/mlp_reference_models/`
- `backward/rf_reference_models/`
- `backward/dt_reference_models/`
- `backward/et_reference_models/`
- `backward/ert_reference_models/`
- `backward/gbm_reference_models/`
- `backward/hgbm_reference_models/`
- `backward/xgbm_reference_models/`
- `backward/lgbm_reference_models/`

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

Closeout rule:

- every future Track 1 closeout must compare newly accepted target winners against the archive entries already stored here;
- when a newly accepted winner improves the stored archive entry, the archive must be replaced together with its provenance bundle and linked benchmark references;
- when the accepted winner does not improve, the stored archive entry must remain unchanged.
