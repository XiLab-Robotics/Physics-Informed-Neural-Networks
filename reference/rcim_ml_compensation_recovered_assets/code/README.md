# RCIM Recovered Code Root

This folder stores the recovered RCIM code surfaces grouped by historical role.

## Canonical Target Root

- [original_pipeline/](./original_pipeline/)

This folder is now intentionally reserved for the full recovered original RCIM
repository that will be installed manually after the archival reorganization.

At the moment it is only a placeholder root.

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

- `backup_legacy_early_snapshot/` is the oldest recovered branch here.
- `backup_latest_snapshot_fragment/` and
  `backup_split_original_pipeline_fragment/` are later recovered fragments.
- `original_pipeline/` is reserved for the full recovered original repository
  and should become the canonical code root after the manual copy step.
