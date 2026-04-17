# Paper Reference Models

This folder stores curated repository-local copies of model artifacts used as
canonical paper-reference anchors.

The purpose of this archive is not to replace the immutable raw validation
artifacts under `output/validation_checks/`. Instead, it provides a stable,
human-auditable location for the subset of models that the benchmark accepts as
the repository-owned reference surface for paper replication.

Current topic roots:

- `rcim_track1/`

Canonical archive standard for future paper-family archives:

- family-scoped artifact folder;
- dedicated `README.md`;
- machine-readable inventory file;
- explicit references to source run, config, and training code.

For `Track 1` paper-reimplementation families, the canonical family package
contract is:

- `models/paper_reference/rcim_track1/<family>_reference_models/`
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
- dataset provenance and deterministic split reconstruction metadata;
- family-specific implementation notes when exported deployment artifacts use a
  surrogate estimator surface that differs from the original Python model.

The current `SVM` archive under `rcim_track1/svm_reference_models/` is the
first fully populated reference implementation of this standard.
