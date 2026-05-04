# RCIM Original Paper Reference Models

This folder groups curated paper-reference model archives generated from the
recovered original RCIM training workflow.

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
- `forward/lgbm_reference_models/`
- `forward/xgbm_reference_models/`
- `forward/elm_reference_models/`

Canonical family archive template:

- `<direction>/<family>_reference_models/README.md`
- `<direction>/<family>_reference_models/reference_inventory.yaml`
- `<direction>/<family>_reference_models/onnx/amplitude/`
- `<direction>/<family>_reference_models/onnx/phase/`
- `<direction>/<family>_reference_models/python/amplitude/`
- `<direction>/<family>_reference_models/python/phase/`
- `<direction>/<family>_reference_models/data/`
- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/launcher_summary.snapshot.json`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/eval.run_summary.snapshot.json`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/export.run_summary.snapshot.json`

Current closeout note:

- the forward branch was populated from `output/training_campaigns/rcim_original/forward/2026-05-04-23-19-35__fw_original_bundle`;
- backward remains intentionally unpopulated until its own reference closeout is completed.
