# Paper Reference Models

This folder stores curated repository-local copies of model artifacts used as
canonical paper-reference anchors.

For RCIM Track 1, the paper-reference models are not generic experiment
outputs. They are the accepted archives promoted during closeout of the
faithful exact-model-bank campaigns implemented under:

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`

Those campaigns reproduce the recovered original RCIM pipeline protocol as
literally as practical on the repository dataset and feed the canonical Tables
`2`-`5` benchmark surface:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Current topic roots:

- `rcim_track1/`
- `rcim_original/`
- `rcim_retuned/`

For `Track 1` paper-reimplementation families, the canonical family package
contract is:

- `models/paper_reference/rcim_track1/forward/<family>_reference_models/`
- `models/paper_reference/rcim_track1/backward/<family>_reference_models/`
- `README.md`
- `reference_inventory.yaml`
- `onnx/amplitude/`
- `onnx/phase/`
- `python/amplitude/`
- `python/phase/`
- `data/`
- `dataset_snapshot_manifest.yaml`
- `source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `source_runs/<run_instance_id>/split_manifest.yaml`

The Track 1 forward and backward branches now include the operational
`ELM` archive in addition to the original `10` paper-table families.

Every fully curated family archive is expected to preserve:

- the accepted target-level benchmark metrics;
- the canonical source run per accepted target;
- deployment-facing archived exports;
- Python-usable fitted estimators when the training stack supports them;
- dataset provenance and deterministic split reconstruction metadata.
