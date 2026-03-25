# Overview

This document defines the cleanup and canonicalization follow-up for the newly
implemented isolated-mode workflow.

The repository now has a proper isolated-session model under:

- `isolated/active/`
- `isolated/completed/`

Because of that, the older archive subtree:

- `reference/isolated_handoff/`

is no longer desired as a retained repository artifact.

The user explicitly requested:

- keep only the useful information that still deserves long-term tracking;
- move that useful information into proper technical documentation;
- remove the legacy handoff archive files entirely;
- acknowledge that `PyYAML` should normally be available from the project
  Conda environment `standard_ml_codex_env`, because it is already tracked in
  `requirements.txt`.

# Technical Approach

## 1. Treat `reference/isolated_handoff/` As Legacy Residue

The legacy archive currently contains:

- `reference/isolated_handoff/readme.temp.md`
- `reference/isolated_handoff/notebooklm_exports_provenance_manifest.md`
- `reference/isolated_handoff/README.md`

Those files describe a historical first-pass isolated workflow based on
handoff/archive behavior rather than on the new hard-lock session model.

They should no longer remain in the live repository because:

- they encode the wrong operational pattern for future isolated work;
- they keep a non-canonical archive root alive under `reference/`;
- they create unnecessary ambiguity about whether isolated work should be
  archived or properly integrated.

## 2. Preserve Only The Useful Historical Signals

The useful information to retain is limited and should be migrated into
canonical documentation rather than preserved as a raw archive dump.

The retained signals are:

- the historical fact that an earlier isolated-mode attempt existed;
- the design lesson that `readme.temp.md` and `reference/isolated_handoff/`
  were not robust enough;
- the provenance fact that the previous isolated work mainly concerned
  `NotebookLM` archive ingestion, documentation-platform evaluation, and later
  synchronized Sphinx integration;
- the policy decision that future isolated work must use explicit session roots,
  locked snapshots, structured manifests, and deterministic integration
  checklists.

Those points belong in:

- the new isolated-mode technical document;
- the repository instructions;
- any still-relevant canonical archive/guide documentation that currently
  references the old archive as if it were still the live provenance source.

## 3. Remove Canonical References To The Legacy Archive

Current canonical repository-authored documents still reference
`reference/isolated_handoff/` directly.

These references should be updated so that:

- the new isolated-mode rule points only to the session-based workflow;
- canonical archive pages no longer present `reference/isolated_handoff/` as an
  active or retained root;
- historical technical notes may still mention the old path when describing the
  past, but current-state documentation should not depend on the physical
  presence of that folder.

## 4. Clarify The `PyYAML` Environment Assumption

The repository already tracks:

- `PyYAML>=6.0,<7.0`

inside `requirements.txt`.

Therefore, the normal operational assumption should be:

- when the project is run inside `standard_ml_codex_env`, `PyYAML` is expected
  to be available.

The isolated-mode manager can keep its current fallback behavior as a defensive
compatibility measure for accidental execution outside the intended environment,
but the documentation should not imply that the fallback is the preferred
runtime mode.

## 5. Cleanup Scope

After approval, the cleanup should:

- migrate the still-useful trace into current technical documentation if needed;
- delete the three files under `reference/isolated_handoff/`;
- remove now-obsolete current-state references to that archive root;
- keep historical technical documents intact where they explicitly describe the
  old workflow as past state;
- update the isolated-mode script documentation so `standard_ml_codex_env`
  remains the expected runtime environment and the fallback is treated as
  secondary protection only.

# Involved Components

- `reference/isolated_handoff/readme.temp.md`
- `reference/isolated_handoff/notebooklm_exports_provenance_manifest.md`
- `reference/isolated_handoff/README.md`
- `doc/technical/2026-03-25/2026-03-25-12-39-38_isolated_mode_rework.md`
- `AGENTS.md`
- `doc/scripts/tooling/isolated_mode.md`
- `docs/archives/notebooklm_exports.md`
- `docs/learning_guides/index.rst`
- any other current-state canonical documents that still present
  `reference/isolated_handoff/` as an active dependency

# Implementation Steps

1. Record this cleanup decision in a new technical document and register it in
   `README.md`.
2. Review `reference/isolated_handoff/` and extract only the small subset of
   historical lessons that still deserve canonical tracking.
3. Update the current isolated-mode technical documentation so those lessons are
   preserved without requiring the old archive files.
4. Update current-state canonical documents that still reference
   `reference/isolated_handoff/` as a live root.
5. Update the isolated-mode script documentation to clarify that
   `standard_ml_codex_env` is the expected runtime environment and that the
   no-`PyYAML` fallback is only a defensive compatibility layer.
6. Remove the legacy files under `reference/isolated_handoff/`.
7. Re-run targeted searches to confirm that no active repository workflow still
   depends on the removed archive subtree.
