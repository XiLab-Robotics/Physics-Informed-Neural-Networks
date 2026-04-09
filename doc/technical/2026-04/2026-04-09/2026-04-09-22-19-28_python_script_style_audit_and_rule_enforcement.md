# Python Script Style Audit And Rule Enforcement

## Overview

This document covers a narrow repository-governance task with two linked goals:

1. audit the repository-owned Python scripts previously created through Codex
   work against the current formatting, comment, docstring, and structure
   rules;
2. formalize in the canonical repository rules that this style-compliance check
   is mandatory whenever a new repository-owned Python script is created.

The user request is intentionally operational rather than feature-oriented. The
main outcome should therefore be a verified audit pass over the relevant Python
script surface plus a rule update that prevents future drift.

To avoid ambiguity around which scripts count as "created by Codex", the audit
should use the repository-owned Python script surface under `scripts/` as the
enforcement baseline, then focus any remediation on the files that remain
misaligned with the currently approved style direction.

No subagent is planned for this task. The work is a local audit plus
documentation and rule maintenance, and any future delegated audit would still
require explicit user approval at runtime.

## Technical Approach

The implementation should proceed in three coordinated phases.

### 1. Audit The Python Script Surface

Inspect the repository-owned Python files under `scripts/` against the current
style baseline already defined by:

- `AGENTS.md`;
- `doc/reference_summaries/06_Programming_Style_Guide.md`;
- the repository reference-code notes derived from
  `blind_handover_controller`, `mediapipe_gesture_recognition`, and
  `multimodal_fusion`.

The audit should check at least:

- module-level docstring presence and quality where expected;
- Google-style docstrings for public modules, classes, dataclasses, and
  non-trivial public functions;
- comment coverage and quality inside non-trivial functions;
- explicit staged logic, naming clarity, and spacing consistency;
- obvious residual formatting drift against the approved repository style.

### 2. Apply Targeted Script Fixes

If the audit finds Python scripts that remain materially misaligned, patch only
the affected files and keep behavior unchanged. The focus should stay on style
compliance rather than opportunistic refactoring.

### 3. Formalize The Mandatory Future Check

Update the canonical repository rule surfaces so they explicitly require a
style-compliance review whenever a new repository-owned Python script is
created.

The rule update should make it explicit that new script work is not complete
until the author has checked:

- formatting and spacing alignment;
- docstring alignment with the Google-style default;
- section-comment coverage for non-trivial functions;
- naming and staged-logic readability against the repository baseline.

The most important canonical rule surfaces for this formalization are:

- `AGENTS.md`;
- `doc/reference_summaries/06_Programming_Style_Guide.md`.

## Involved Components

- `AGENTS.md`
- `doc/README.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `doc/technical/2026-04/2026-04-09/2026-04-09-22-19-28_python_script_style_audit_and_rule_enforcement.md`
- Python files under `scripts/`

## Implementation Steps

1. Audit the repository-owned Python script surface under `scripts/` and
   identify any remaining style or documentation gaps.
2. Patch the misaligned Python files found by the audit, keeping runtime
   behavior unchanged.
3. Update `AGENTS.md` to require an explicit style-compliance pass whenever a
   new repository-owned Python script is created.
4. Update `doc/reference_summaries/06_Programming_Style_Guide.md` so the same
   requirement is recorded in the persistent programming-style guidance.
5. Register this technical document from `doc/README.md`.
6. Run focused validation on any touched Python files.
7. Run Markdown warning checks on the touched Markdown scope and resolve any
   warnings before closing the task.
8. Report the completed audit and rule changes, then wait for explicit approval
   before creating any Git commit.
