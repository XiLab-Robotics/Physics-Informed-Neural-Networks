# Overview

This document defines a final cleanup batch for the isolated integration residue
that no longer needs to live in canonical root-level or doc-structure
locations.

At this point:

- the isolated-origin canonical migration work has already been completed;
- the documentation proof-of-concept trees have already been archived under
  `reference/documentation_poc/`;
- the old `doc/imports/notebooklm_exports/` root and the root-level
  `readme.temp.md` file remain only as post-integration residue.

The goal of this batch is to remove those now-obsolete live locations without
losing provenance.

## Technical Approach

The cleanup should keep the actual historical material while retiring the
obsolete locations that no longer serve as active repository roots.

The batch should therefore:

- move the full isolated-mode handoff log out of the repository root into a
  dedicated archival subtree under `reference/`;
- move the former `NotebookLM` provenance manifest out of the retired
  `doc/imports/notebooklm_exports/` root into the same archival subtree;
- remove the now-empty `doc/imports/notebooklm_exports/` and
  `doc/reports/analysis/learning_guides/` directories from the live tree;
- update current repository-authored references so they point either to the
  canonical guide structure or to the new archival destination;
- avoid deleting the historical handoff content itself.

Recommended archival destination:

- `reference/isolated_handoff/`

Recommended archived contents:

- `reference/isolated_handoff/readme.temp.md`
- `reference/isolated_handoff/notebooklm_exports_provenance_manifest.md`

## Involved Components

- `readme.temp.md`
- `doc/imports/notebooklm_exports/README.md`
- `doc/imports/notebooklm_exports/`
- `doc/reports/analysis/learning_guides/`
- `reference/isolated_handoff/`
- `README.md`
- `doc/README.md`
- `docs/archives/notebooklm_exports.md`
- `docs/learning_guides/index.rst`
- `AGENTS.md`
- `doc/technical/2026-03/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md`

## Implementation Steps

1. Create a dedicated archive subtree for retired isolated-mode handoff
   artifacts.
2. Move `readme.temp.md` out of the repository root into that archive subtree.
3. Move the former `NotebookLM` provenance manifest out of
   `doc/imports/notebooklm_exports/` into that archive subtree.
4. Remove the now-empty `doc/imports/notebooklm_exports/`, `doc/imports/`, and
   `doc/reports/analysis/learning_guides/` directories from the live tree.
5. Update current repository-authored documentation and project instructions to
   reference the canonical guide root and the new archive location.
6. Re-run targeted searches to confirm that no current-state documentation still
   presents the retired roots as active locations.

## Implementation Result

The cleanup was completed conservatively.

The retired isolated artifacts now live under:

- `reference/isolated_handoff/readme.temp.md`
- `reference/isolated_handoff/notebooklm_exports_provenance_manifest.md`
- `reference/isolated_handoff/README.md`

The following obsolete live-tree roots were removed after their contents were
either migrated canonically or archived:

- `doc/imports/notebooklm_exports/`
- `doc/imports/`
- `doc/reports/analysis/learning_guides/`

Current-state documentation was updated so the canonical guide root remains
`doc/guide/`, while the isolated handoff and the retired `NotebookLM`
provenance manifest are now tracked under `reference/isolated_handoff/`.
