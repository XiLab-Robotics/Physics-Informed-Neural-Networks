# RCIM Recovered Code Root

This folder stores the recovered RCIM code surfaces grouped by historical role.

## Canonical Full Original Root

- [original_pipeline/](./original_pipeline/)

This is now the canonical author-supplied full original RCIM workflow root.

Observed contents include:

- flat top-level execution scripts rather than the older split folder layout;
- `instances_V3/` with `969` `.pickle` caches;
- shipped forward and backward dataframe CSVs;
- `output_prediction/` artifacts;
- `evaluation/` artifacts;
- the author-provided executable `README.md`.

This root is now the main reference surface for:

- dataframe generation;
- paper-side training and export usage;
- evaluation-table generation;
- understanding how the original team actually ran the workflow.

## Historical Backup Roots

- [backup_split_original_pipeline_fragment/](./backup_split_original_pipeline_fragment/)
  Split late-stage fragment that previously lived under the misleading
  `original_pipeline/` name.
- [backup_latest_snapshot_fragment/](./backup_latest_snapshot_fragment/)
  Narrow late-stage export-oriented fragment that previously lived under
  `latest_snapshot/`.
- [backup_legacy_early_snapshot/](./backup_legacy_early_snapshot/)
  Much earlier backup surface that previously lived under `backup_legacy/`.

## Interpretation

- `original_pipeline/` is now the strongest recovered code evidence because it
  comes directly from the authors and includes scripts, caches, and generated
  artifacts in one operational folder.
- `backup_split_original_pipeline_fragment/` remains useful as a previous
  reconstruction of the staged workflow, but it is no longer the canonical
  original root.
- `backup_latest_snapshot_fragment/` remains useful as a narrower export
  snapshot centered on the `v17` branch.
- `backup_legacy_early_snapshot/` remains the oldest recovered branch and is
  still useful for tracking the earlier harmonic-set evolution.
