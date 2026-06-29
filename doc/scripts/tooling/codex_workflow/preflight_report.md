# `preflight_report.py`

## Overview

`scripts/tooling/codex_workflow/preflight_report.py` prints a non-blocking
workflow gate report for StandardML - Codex tasks.

It is intended as a fast mechanical readout before or during Codex work. It does
not replace the repository rules in `AGENTS.md`, the relevant specialist skill,
or direct inspection of task files.

## Command

```powershell
python -B scripts/tooling/codex_workflow/preflight_report.py
```

To check a proposed path list instead of current Git changes:

```powershell
python -B scripts/tooling/codex_workflow/preflight_report.py `
  --changed-path scripts/tooling/codex_workflow/preflight_report.py `
  --changed-path doc/scripts/tooling/codex_workflow/preflight_report.md
```

## Reported Signals

The script reports:

- current Git changed-path count;
- active campaign status from `doc/running/active_training_campaign.yaml`;
- protected-file overlap count;
- latest timestamped technical document;
- path-derived gate signals such as Markdown QA, Python validation, Sphinx
  build, campaign-state review, PDF validation, or Codex workflow
  documentation updates.

## Operational Notes

- The script is report-only and exits successfully when it can read the
  repository state.
- Treat protected-file overlaps as a prompt to read
  `doc/running/active_training_campaign.yaml` and apply the `CRITICAL WARNING`
  rule when needed.
- If this script is later wired into a Codex hook, keep it non-blocking unless
  a separate technical document and user approval explicitly authorize
  enforcement behavior.
