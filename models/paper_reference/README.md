# Paper Reference Models

This folder stores curated repository-local copies of model artifacts used as
canonical paper-reference anchors.

The purpose of this archive is not to replace the immutable raw validation
artifacts under `output/validation_checks/`. Instead, it provides a stable,
human-auditable location for the subset of models that the benchmark accepts as
the repository-owned reference surface for paper replication.

Current topic roots:

- `rcim_track1/`

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

Every fully curated family archive is expected to preserve:

- the accepted target-level benchmark metrics;
- the canonical source run per accepted target;
- deployment-facing archived exports;
- Python-usable fitted estimators when the training stack supports them;
- dataset provenance and deterministic split reconstruction metadata.

The bidirectional original-dataset Track 1 mega-campaign closeout is the first
wave that fully populates both `forward` and `backward` archive branches.
