# Overview

This document defines a robust rework of the repository `isolated mode`.

The current historical approach was useful as a first conflict-avoidance pass,
but it had two structural weaknesses:

- it treats isolation mainly as a handoff/archive workflow rather than as a
  hard write-boundary on the active repository;
- it relied on ad-hoc temporary roots such as root-level `readme.temp.md` and a
  legacy archive under `reference/isolated_handoff/`, which made the mode
  noisier than necessary and weakened the later integration discipline.

The requested target behavior is stricter:

- when the user activates isolated mode, every file already present in the
  repository becomes read-only from Codex's operational point of view;
- `README.md` and `AGENTS.md` are included in that lock and must not be edited
  until the user explicitly exits isolated mode;
- during isolated mode, Codex may only create new files and then edit only
  those new files;
- when the user later requests integration, Codex must process the isolated
  session deterministically, integrate each prepared item one by one with a
  double verification pass, and then remove obsolete isolation residue.

This rework should replace the old root-level handoff pattern with a clearer,
repository-owned session model.

## Technical Approach

## 1. Replace Ad-Hoc Handoff With Explicit Isolated Sessions

The preferred structure is a dedicated repository root for isolated sessions:

- `isolated/active/<session_id>/`
- `isolated/completed/<session_id>/`

This is cleaner than the retired `reference/isolated_handoff/` archive because
the material is not reference documentation and should not be archived as if it
were canonical project knowledge. It is operational staging for delayed
integration.

Each `session_id` should be immutable and timestamp-based, for example:

- `2026-03-25-12-39-38_isolated_mode_rework`

## 2. Freeze All Pre-Existing Repository Files During Isolation

When isolated mode is activated, Codex should immediately capture a repository
baseline manifest that records every file already present outside the isolated
session root.

Recommended session metadata files:

- `isolated/active/<session_id>/session_context.md`
- `isolated/active/<session_id>/locked_repository_snapshot.txt`
- `isolated/active/<session_id>/integration_manifest.yaml`
- `isolated/active/<session_id>/integration_checklist.md`
- `isolated/active/<session_id>/work_log.md`
- `isolated/active/<session_id>/staging/`

The operational rule is then simple:

- any file present in `locked_repository_snapshot.txt` is read-only for Codex
  while isolated mode remains active;
- only files created under the current session root may be modified;
- `README.md` and `AGENTS.md` remain locked even if the isolated work would
  normally want to register documents there.

This is stronger and less ambiguous than "avoid shared files".

## 3. Use Structured Staging Instead Of A Free-Form Temporary README

The old `readme.temp.md` pattern should be retired.

Instead, isolated work should be split into explicit files with fixed roles:

- `session_context.md`
  captures why the session exists, the user instruction, and the intended exit
  condition;
- `work_log.md`
  records analysis, created files, deferred decisions, and later integration
  notes;
- `integration_manifest.yaml`
  records every isolated artifact and its intended final action;
- `integration_checklist.md`
  records the replay sequence and verification status for integration.

The main content produced during isolated mode should live in:

- `isolated/active/<session_id>/staging/<planned_target_structure>/`

This means the staging tree should mirror the future canonical destination as
closely as possible without touching existing repository files. That makes the
later import process deterministic without pretending that staging files are
already integrated.

Example:

- future target:
  `doc/guide/New Guide/New Guide.md`
- isolated staging path:
  `isolated/active/<session_id>/staging/doc/guide/New Guide/New Guide.md`

## 4. Make Integration Manifest-Driven

The isolated session must not rely on memory or prose-only replay.

`integration_manifest.yaml` should track, for each prepared item:

- `staging_path`
- `target_path`
- `action`
  - `create_new_file`
  - `derive_and_merge`
  - `replace_generated_artifact`
  - `manual_review_required`
- `source_reason`
- `dependency_paths`
- `integration_notes`
- `status`
  - `prepared`
  - `validated`
  - `integrated`

This prevents the old failure mode where artifacts are copied aside and later
interpreted manually with too much ambiguity.

## 5. Enforce Double Verification During Integration

When the user exits isolated mode and requests integration, Codex must process
the session in a strict order.

Required verification pass A: repository-state revalidation

- re-read the current target file if it exists;
- confirm whether the target changed since the session started;
- confirm that the target still belongs in the expected location;
- confirm that no newer canonical content already supersedes the staged file.

Required verification pass B: staged-item integration review

- compare the staged artifact against the current target;
- decide whether the correct operation is create, merge, partial extraction, or
  discard;
- update the checklist entry before and after the integration step;
- verify that the integrated result really absorbed the staged intent.

Only after both passes succeed should the item be marked `integrated`.

## 6. Clean Up Only After Verified Import

Once all manifest items are integrated or intentionally discarded:

- move the session from `isolated/active/` to `isolated/completed/` if the user
  wants retention;
- or remove the session entirely if the user wants a clean repository and the
  integration trail is already captured in canonical docs and Git history.

The default cleanup should remove obsolete staging residue after successful
integration. The repository should not keep long-lived "handoff archives" under
`reference/` for work that has already been processed.

## 7. Implementation Form

After approval, the repository change should formalize isolated mode in two
layers:

- behavioral rules in `AGENTS.md`;
- lightweight helper tooling in new repository-owned files, likely under
  `scripts/tooling/` or an equivalent utility subtree.

The tooling should cover:

- session initialization;
- locked-file snapshot generation;
- manifest/checklist template generation;
- post-session validation that no locked file was modified during isolation;
- integration-time validation of staged artifacts.

## 8. Validation Strategy

After approval, testing should cover at least these cases:

1. start isolated mode on a clean repository and confirm that only new files
   under the session root are created;
2. simulate an attempted edit to a locked file and confirm that the validation
   tooling flags it as a protocol violation;
3. create multiple staged artifacts mapped to different canonical targets and
   confirm that the manifest/checklist flow processes them one by one;
4. simulate a target file changing after isolated preparation and confirm that
   the integration workflow forces revalidation instead of blind import;
5. confirm that cleanup removes obsolete session residue after successful
   integration.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/README.md`
- `doc/technical/2026-03/2026-03-24/2026-03-24-20-58-19_isolated_integration_reconciliation_and_learning_guide_migration.md`
- `doc/technical/2026-03/2026-03-24/2026-03-24-22-45-37_isolated_integration_remaining_work_verification.md`
- `doc/technical/2026-03/2026-03-24/2026-03-24-23-25-32_isolated_handoff_and_provenance_root_retirement.md`
- retired legacy isolated archive:
  - `reference/isolated_handoff/`
- future isolated session root:
  - `isolated/active/`
  - `isolated/completed/`
- future helper tooling:
  - `scripts/tooling/`

## Implementation Steps

1. Formalize the new isolated-mode behavior in a technical document and obtain
   explicit approval before code or instruction changes.
2. Replace the old `readme.temp.md` / legacy isolated-handoff mental
   model with a session-based `isolated/active/<session_id>/` structure.
3. Add repository instructions that define isolated mode as a hard lock on all
   pre-existing repository files, including `README.md` and `AGENTS.md`.
4. Implement helper tooling to create a session root, capture the locked-file
   snapshot, and generate manifest/checklist templates.
5. Implement validation tooling that checks whether isolated work touched any
   locked file.
6. Implement integration tooling or a guided integration workflow that consumes
   `integration_manifest.yaml` and `integration_checklist.md`.
7. Test isolated session start, staged-file authoring, locked-file validation,
   integration-time revalidation, and cleanup behavior.
8. Update the repository documentation to describe the final isolated-mode
   workflow and retire obsolete references to `readme.temp.md` and the legacy
   isolated-handoff archive where they are presented as active practice.
