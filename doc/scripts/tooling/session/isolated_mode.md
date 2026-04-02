# `isolated_mode.py`

## Overview

`scripts/tooling/session/isolated_mode.py` formalizes the repository isolated-mode
workflow.

It creates explicit isolated sessions under:

- `isolated/active/<session_id>/`
- `isolated/completed/<session_id>/`

Each session captures a locked snapshot of every repository file that already
existed before the isolated work began. During isolated mode, those pre-existing
files must remain untouched and all new work should live only inside the session
root.

The script replaces the older ad-hoc `readme.temp.md` handoff pattern with:

- `session_context.md`
- `work_log.md`
- `locked_repository_snapshot.txt`
- `integration_manifest.yaml`
- `integration_checklist.md`
- `latest_validation_report.yaml`
- `latest_integration_review.yaml`
- `staging/`

## Commands

### Start A Session

```powershell
python -B scripts/tooling/session/isolated_mode.py start-session `
  --session-label "sphinx_followup" `
  --purpose "Prepare Sphinx changes without touching canonical repository files." `
  --user-request "enter isolated mode"
```

This command:

- creates a timestamped session folder under `isolated/active/`;
- captures the locked-file snapshot;
- initializes the manifest, checklist, and work log;
- creates `staging/` as the only writable area intended for isolated work.

### Register A Staged Artifact

```powershell
python -B scripts/tooling/session/isolated_mode.py add-manifest-item `
  --session-path isolated/active/2026-03-25-12-39-38_sphinx_followup `
  --staging-path isolated/active/2026-03-25-12-39-38_sphinx_followup/staging/doc/guide/New Guide/New Guide.md `
  --target-path doc/guide/New Guide/New Guide.md `
  --action create_new_file `
  --source-reason "New guide drafted entirely in isolated mode."
```

This command registers one staged artifact in `integration_manifest.yaml` and
regenerates the checklist skeleton for later integration.

### Validate The Repository Lock

```powershell
python -B scripts/tooling/session/isolated_mode.py validate-session `
  --session-path isolated/active/2026-03-25-12-39-38_sphinx_followup `
  --fail-on-violation
```

Validation checks:

- modified locked files;
- deleted locked files;
- new files created outside the isolated session root.

This makes the "only new files inside isolated mode" rule inspectable instead
of implicit.

### Prepare The Integration Checklist

```powershell
python -B scripts/tooling/session/isolated_mode.py prepare-integration `
  --session-path isolated/active/2026-03-25-12-39-38_sphinx_followup `
  --fail-on-violation
```

This command:

- reruns lock validation;
- regenerates `latest_integration_review.yaml`;
- updates `integration_checklist.md` with Pass A / Pass B review fields for
  each manifest item.

The intended interpretation is:

- Pass A: revalidate the canonical repository target;
- Pass B: verify that the staged intent was actually absorbed into the final
  repository result.

### Close A Session

```powershell
python -B scripts/tooling/session/isolated_mode.py close-session `
  --session-path isolated/active/2026-03-25-12-39-38_sphinx_followup `
  --destination completed `
  --require-clean-validation
```

Or, if the session should be removed after successful integration:

```powershell
python -B scripts/tooling/session/isolated_mode.py close-session `
  --session-path isolated/active/2026-03-25-12-39-38_sphinx_followup `
  --destination delete `
  --require-clean-validation
```

## Operational Notes

- The expected runtime environment is the project Conda environment
  `standard_ml_codex_env`, where `PyYAML` should normally already be available
  through `requirements.txt`.
- The script keeps a JSON-compatible fallback when `PyYAML` is unavailable, but
  that path is only a defensive compatibility layer and not the preferred
  runtime mode.
- The isolated session excludes `.git/` and the session root itself from the
  locked snapshot.
- The script also ignores `__pycache__/` folders to avoid false positives from
  interpreter cache files.
- `README.md` and `AGENTS.md` are locked automatically if they existed at
  session start, which they do in this repository.
- The script does not integrate staged files automatically. It prepares the
  manifest and the review surface so the later integration pass stays explicit.
