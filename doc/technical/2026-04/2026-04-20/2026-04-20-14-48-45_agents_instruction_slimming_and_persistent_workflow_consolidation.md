# Agents Instruction Slimming And Persistent Workflow Consolidation

## Overview

The repository instruction surface has grown substantially and now mixes:

- always-on operational rules that must be considered for almost every task;
- domain-specific workflow policy that is relevant only for training, styled
  PDF work, guide generation, or commit/publish closeout;
- implementation detail that is already captured by repository-owned skills,
  tooling notes, or persistent scripts.

This increases context load and encourages repeated ad hoc command patterns,
including inline Python snippets for PDF export or validation that should
instead use the repository-owned command entry points already available under
`scripts/reports/` and `scripts/tooling/markdown/`.

The goal of this document is to define a leaner instruction architecture that
keeps the required safety and quality bar while reducing always-on policy
overhead and making the stable workflow entry points more explicit.

No subagent usage is planned for this document. If later implementation work
would benefit from a subagent, that runtime launch would still require explicit
user approval.

## Technical Approach

### 1. Split Core Rules From On-Demand Policy

`AGENTS.md` should be reduced to a compact always-on core that covers only the
rules that materially affect most repository tasks. The core should retain at
least:

- the technical-document-first gate for repository changes;
- the explicit approval gate before implementation begins;
- the no-commit-without-approval rule;
- the touched-Markdown warning pass for created or modified repository Markdown;
- the `Context7` requirement for the listed library families;
- the active-campaign protection check when a request may touch training or
  campaign-sensitive files.

Detailed policy that is not relevant to every task should move out of the
always-on instruction path and be referenced only when the task enters the
corresponding domain.

### 2. Move Specialist Workflow Detail Into Domain Policy Documents Or Skills

The following detail should no longer live as always-active prose inside the
main instruction file:

- the long `NotebookLM` guide-bundle workflow and export naming rules;
- most styled-PDF micro-layout requirements for tables, units, and page breaks;
- the full training campaign lifecycle description once the core gating rules
  are preserved elsewhere;
- detailed GitHub push-size and publication-stage checks that matter only at the
  final commit or publish step;
- the longest coding-style prose that is already represented by the canonical
  style summary in `doc/reference_summaries/06_Programming_Style_Guide.md`.

These should instead be kept in stable repository-owned locations such as:

- the existing skills under `.codex/skills/`;
- tooling usage notes under `doc/scripts/tooling/`;
- dedicated policy documents under `doc/` when the rules are domain-local but
  still need durable repository ownership.

`AGENTS.md` can then point to these policy surfaces without inlining all of
their detail on every task.

### 3. Deduplicate Repeated Rules Inside The Core Instruction Surface

Even within the current core behavior, several rule families are repeated in
multiple forms. The slimming pass should collapse these into one canonical
statement per concern:

- technical-document creation and approval gating;
- `README.md` update criteria;
- training planning and active-campaign handling;
- Markdown zero-warning closeout requirements;
- Sphinx rebuild conditions for documentation-facing changes.

The resulting structure should prefer one authoritative rule plus references to
the implementing script or policy note, rather than restating the same policy
in several sections.

### 4. Standardize Persistent Command Entry Points

The repository already contains persistent command entry points that should
replace repeated inline scripting during normal operation:

- `python -B scripts/reports/run_report_pipeline.py`
- `python -B scripts/reports/validate_report_pdf.py`
- `python -B scripts/tooling/markdown/run_markdownlint.py`

The future workflow should explicitly prefer those entry points over ad hoc
inline Python blocks except when debugging a broken tool. This reduces token
usage, keeps behavior reproducible, and avoids one-off command drift.

### 5. Add Missing Lightweight Helpers Where Repetition Still Exists

The largest remaining repeated manual step is the creation and registration of
new technical documents. A lightweight repository-owned helper should be
considered for:

- reading the real local timestamp;
- creating the dated technical-document path with the required section
  scaffold;
- updating the day-local technical `README.md`;
- updating `doc/README.md` or a narrower canonical index when required.

This helper would reduce repeated manual bookkeeping while preserving the
approval-gated workflow.

### 6. Clarify Lazy-Load Task Classes

The streamlined instruction model should make explicit which policy families are
loaded only on demand:

- training and campaign governance only for training or campaign work, or when
  protected campaign files may be touched;
- styled PDF validation policy only for report or guide PDF export work;
- `NotebookLM` and video-package policy only for guide and export tasks;
- commit, push-size, and publish checks only during commit or release closeout;
- Sphinx portal rebuild rules only when the affected scope enters the canonical
  `site/` surface or its documentation entry points.

This prevents unrelated tasks from inheriting large policy payloads they do not
need.

## Involved Components

- `AGENTS.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-20/README.md`
- `.codex/skills/markdown-report-qa/SKILL.md`
- `.codex/skills/styled-report-pdf-qa/SKILL.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `doc/scripts/tooling/README.md`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `scripts/tooling/markdown/run_markdownlint.py`
- future repository-owned helper for technical-document scaffolding and
  registration

## Implementation Steps

1. Create and register this technical document as the planning baseline for the
   instruction-slimming work.
2. Refactor `AGENTS.md` into a shorter always-on core plus references to
   on-demand policy surfaces.
3. Move specialist workflow detail into durable domain-owned locations such as
   skills, tooling notes, or narrower policy documents.
4. Remove duplicated rule statements so each major policy concern has one
   canonical home.
5. Update the core instruction wording to explicitly prefer the persistent
   report and Markdown tooling entry points over ad hoc inline Python snippets.
6. Evaluate and, if approved, implement a small repository-owned helper for
   timestamped technical-document creation and index registration.
7. Re-run Markdown warning checks on the touched Markdown scope and confirm
   normal single-final-newline state before closing the task.
