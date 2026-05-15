# Paper Reference Models

This folder stores curated repository-local copies of model artifacts used as
canonical paper-reference anchors.

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

The Track 1 forward branch now includes the operational `ELM` archive in
addition to the original `10` paper-table families. Backward `ELM` will be
added only after the matching backward campaign is closed.

Every fully curated family archive is expected to preserve:

- the accepted target-level benchmark metrics;
- the canonical source run per accepted target;
- deployment-facing archived exports;
- Python-usable fitted estimators when the training stack supports them;
- dataset provenance and deterministic split reconstruction metadata.
