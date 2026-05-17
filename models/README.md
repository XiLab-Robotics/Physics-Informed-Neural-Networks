# Model Artifact Folder

This folder is reserved for trained and exported model artifacts.

Suggested subfolders:

- `checkpoints/` for copied or curated training checkpoints
- `exported/` for ONNX, Structured Text, or other deployment-ready exports
- `exported/<family>/<scope>/` for curated Wave 1 HPO winner archives with `python/`, `onnx/`, local inventories, and source-run provenance bundles
- `paper_reference/` for curated paper-baseline model archives with provenance
  and reconstruction notes

Project-authored Python source code no longer lives here. Source files are stored under:

- `scripts/models/`
- `scripts/training/`

Current curated Track 1 paper-reference archives include:

These archives are the accepted output of the faithful RCIM Track 1
exact-model-bank reimplementation under
`scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`.
They replace older archives when a forward or backward paper-faithful campaign
is closed out, and they are the model artifact backing for
`doc/reports/analysis/RCIM Paper Reference Benchmark.md`.

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
