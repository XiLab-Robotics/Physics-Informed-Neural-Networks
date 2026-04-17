# Paper Reference Models

This folder stores curated repository-local copies of model artifacts used as
canonical paper-reference anchors.

The purpose of this archive is not to replace the immutable raw validation
artifacts under `output/validation_checks/`. Instead, it provides a stable,
human-auditable location for the subset of models that the benchmark accepts as
the repository-owned reference surface for paper replication.

Current topic roots:

- `rcim_track1/`

Future paper-family archives should follow the same pattern:

- family-scoped artifact folder;
- dedicated `README.md`;
- machine-readable inventory file;
- explicit references to source run, config, and training code.
