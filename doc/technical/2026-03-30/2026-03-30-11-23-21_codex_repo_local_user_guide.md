# Codex Repo-Local User Guide

## Overview

This document defines a repository-owned user guide dedicated to the local
Codex workflow used inside StandardML - Codex.

The repository already contains the raw ingredients:

- repository-owned skills under `.codex/skills/`;
- repository-owned subagents under `.codex/agents/`;
- technical rules for automatic skill use and approval-gated subagent use;
- several technical documents that explain how these artifacts were introduced.

What is currently missing is a single user-facing guide that explains, in one
place:

- which skills exist;
- which subagents exist;
- when skills are used automatically;
- when subagents may be proposed;
- how the system works in practical repository terms.

## Technical Approach

The implementation should create a dedicated guide under `doc/guide/` with a
matching PDF companion in the same guide-local folder.

The guide should be practical rather than historical. It should explain the
current usable system, not restate every technical decision document.

The guide should cover:

1. current repository-owned skills and what each one is for;
2. current repository-owned subagents and what each one is for;
3. the rule for automatic skill use;
4. the rule for approval-gated subagent launches;
5. simple task-to-artifact examples such as:
   campaign work, report/PDF work, presentation work, training workflow work,
   TwinCAT/export preparation, and commit preflight;
6. the difference between:
   direct Codex work, skill-driven workflow, and subagent delegation.

The guide should be repository-owned, English-first, and suitable for future
human reuse. It should also be detailed enough that the user does not need to
reconstruct the workflow from scattered technical notes.

No custom diagrams are required for this guide. A text-first guide plus PDF
companion is sufficient for the approved scope.

## Involved Components

- `doc/guide/`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`
- `README.md`
- `.codex/skills/`
- `.codex/agents/`
- `doc/technical/2026-03-27/2026-03-27-17-44-33_codex_skill_autonomy_and_subagent_approval_rule.md`
- `doc/technical/2026-03-27/2026-03-27-17-48-41_additional_codex_skills_and_subagents_for_ml_testing_reports_and_commit_workflows.md`
- `doc/technical/2026-03-30/2026-03-30-11-04-41_skill_and_subagent_operational_test_wave_two.md`

Planned subagent use during implementation:

- none

The guide can be implemented directly from current repository artifacts and
does not require runtime subagent use.

## Implementation Steps

1. Create a guide-local folder under `doc/guide/` for the Codex repo-local
   workflow.
2. Write the canonical guide Markdown explaining the current skill and subagent
   system.
3. Export the guide to a guide-local PDF companion.
4. Update `doc/README.md` so the new guide is discoverable from the
   documentation index.
5. Update `doc/guide/project_usage_guide.md` with a short pointer to the new
   specialized guide if that improves discoverability.
6. Run Markdown QA on the touched Markdown files before closing the task.
