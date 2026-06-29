---
name: standardml-workflow-gate
description: Use at the start of non-trivial StandardML - Codex repository work to identify which approval gates, protected-file checks, documentation updates, QA commands, specialist skills, and optional subagent reviews apply before editing, training, reporting, exporting, or committing.
---

# StandardML Workflow Gate

## Overview

Select the repository workflow gates before acting. This skill is a routing and
preflight discipline; it does not replace specialist skills such as
`campaign-architect`, `pytorch-training-workflows`, `styled-report-pdf-qa`, or
`git-commit-preflight`.

## Gate Sequence

Apply these checks in order:

1. Read `AGENTS.md` and the user request.
2. If repository files may be changed, confirm a technical document exists,
   is registered, and has explicit user approval before implementation.
3. Read `doc/running/active_training_campaign.yaml` before touching training,
   campaign, launcher, config, registry, report-closeout, or protected-state
   files.
4. If the task is training-related, require both the technical document and the
   campaign planning report before any training or experiment execution.
5. Route to the narrowest specialist skill:
   - campaign package or closeout: `campaign-architect`;
   - campaign PowerShell launcher: `powershell-campaign-tooling`;
   - Python/PyTorch/ML workflow: `pytorch-training-workflows`;
   - Markdown hygiene: `markdown-report-qa`;
   - styled PDF/report export: `styled-report-pdf-qa`;
   - presentation export: `presentation-export-workflows`;
   - reference synthesis: `scientific-reference-synthesizer`;
   - remote LAN training: `remote-lan-training-campaigns`;
   - TwinCAT/export planning: `twincat-export-preparation`;
   - commit preparation: `git-commit-preflight`;
   - TE Curve Verification Pipeline refresh:
     `track2-verification-refresh`.
6. If subagent help would be useful, name the proposed subagent, reason, and
   exact delegated scope, then wait for explicit approval before launch.
7. Before closing the task, map touched files to the required QA commands.

## Protected-State Checks

Always inspect `doc/running/active_training_campaign.yaml` when a task might
touch:

- `config/`;
- `scripts/campaigns/`;
- `scripts/training/`;
- `scripts/models/`;
- `doc/running/`;
- campaign planning reports;
- campaign result reports;
- output registries.

If the requested change would modify a listed protected file, issue a
`CRITICAL WARNING` and wait for explicit user approval before editing it.

## Documentation And QA Routing

Use these closure rules:

- touched repository Markdown: run Markdown style and Markdownlint checks on
  the touched scope;
- final campaign-results report: export Markdown and PDF, then validate the
  real PDF;
- Sphinx portal scope changed: run `python -m sphinx -W -b html site site/_build/html`;
- Python scripts changed: run `python -m py_compile` or a stronger relevant
  validation command;
- campaign package changed: validate package, launcher preflight, active state,
  and launcher note alignment;
- commit requested: run `git-commit-preflight` and check file-size risk before
  committing.

## Optional Preflight Script

When a mechanical readout is useful, run:

```powershell
python -B scripts/tooling/codex_workflow/preflight_report.py
```

The script is report-only. Treat it as evidence for the decision, not as a
replacement for reading the relevant files.
