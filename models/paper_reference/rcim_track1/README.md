# RCIM Track 1 Paper Reference Models

This folder groups curated paper-reference model archives for the canonical
`Track 1` RCIM paper-reimplementation branch.

These archives are the accepted model outputs from the faithful
original-dataset exact-model-bank reimplementation:

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`

That reimplementation is anchored to the recovered original RCIM workflow:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

It preserves the original paper input schema, harmonic amplitude/phase target
surface, family-wise multioutput training shape, restored `GridSearchCV(...)`
search, historical `cross_validate(...)` replay, and original-style per-target
`Python + ONNX` exports. The only documented protocol deviations are pragmatic
compatibility repairs such as the `SVR(kernel="linear")` replacement with
`StandardScaler + LinearSVR` where the historical branch is impractical in the
modern runtime.

The benchmark tables backed by this archive root live in:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Direction branches:

- `forward/`
- `backward/`

Current populated family archives:

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
- `forward/elm_reference_models/`
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
- `backward/elm_reference_models/`

Paper-table families remain the original `10` families used by Tables `2`-`5`.
`ELM` is an additional operational Track 1 family and is archived for both
directions after the completed paper-faithful campaigns provide it.

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

- every future Track 1 closeout must refresh the affected family-reference archive when accepted models change;
- archive entries must preserve source validation summaries, training configs, run metadata, exported ONNX files, Python pickles, and dataset provenance;
- direction-specific closeouts must only replace archives for the completed direction.
