---
name: markdown-report-qa
description: Use when checking or repairing repository Markdown quality, report-export prerequisites, and documentation QA workflows in StandardML - Codex. This skill is for repository-authored documentation and analytical report hygiene.
---

# Markdown Report QA

Run documentation QA with repository-specific rules, not generic Markdown
cleanup.

## Use This Skill For

- Markdown lint cleanup;
- documentation QA on repository-authored files;
- report-preparation checks before styled PDF export;
- validation of documentation workflow consistency.

## Do Not Use This Skill For

- editing generated artifacts under excluded roots;
- rewriting large documents for style only;
- protected-file edits during an active campaign without explicit approval.

## Required Checks

1. Prefer repository-owned lint commands before ad hoc fixes.
2. Limit scope to canonical authored files, not `reference/` unless the task
   explicitly targets repository-owned reference summaries or notes.
3. If the task touches report-export workflows, verify real output expectations
   rather than only source formatting.

## Commands To Prefer

```powershell
python -B scripts/tooling/run_markdownlint.py
python -B scripts/tooling/markdown_style_check.py --fail-on-warning
```

## Repository QA Priorities

- fix active warning classes with minimal churn;
- preserve document meaning and source attribution;
- keep technical docs registered from `README.md` when required;
- remember that PDF-related work is not complete until the real PDF output is
  validated.

## File Targets To Read First

- `.markdownlint-cli2.jsonc`
- `scripts/tooling/run_markdownlint.py`
- `scripts/tooling/markdown_style_check.py`
- `doc/scripts/tooling/`
- relevant source Markdown files in `doc/`, `README.md`, and `AGENTS.md`
