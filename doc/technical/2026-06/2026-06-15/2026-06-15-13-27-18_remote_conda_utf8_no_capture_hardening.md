# Remote Conda UTF-8 No-Capture Hardening

## Overview

The first remote launch of
`wave3_harmonic_prior_residual_campaign_2026_06_14` failed before the training
campaign could complete. The failure happened inside `conda run`, not inside
the Wave 5.1 model or campaign YAMLs:

```text
UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd'
```

The remote Windows base Conda process used CP1252 while replaying captured
training stdout. A non-CP1252 character in the captured stream caused Conda
itself to exit with code `1`.

This document is the technical gate for hardening the shared remote training
launcher before the campaign is retried.

## Technical Approach

The fix should be applied to the shared remote launcher, not to the Wave 5.1
campaign package:

- use `conda run --no-capture-output` for remote Python calls so Conda does
  not buffer and re-encode the full training stream;
- set remote Python/console encoding environment variables before Conda calls:
  `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1`;
- set the remote console code page to UTF-8 where available;
- apply the same hardened invocation to remote preflight, source verification,
  campaign execution, and sync-manifest generation;
- leave the Wave 5.1 queue YAMLs unchanged;
- restore the interrupted campaign state to a relaunchable prepared state
  after confirming no completed remote artifacts were accepted locally.

This should make the remote runner stream training output directly and avoid
Conda's CP1252 stdout replay path.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` owns
  the shared remote Conda invocation path.
- `doc/scripts/campaigns/run_remote_training_campaign.md` documents the remote
  launcher behavior.
- `doc/running/active_training_campaign.yaml` currently records the failed
  Wave 5.1 campaign as `running` and should be restored to a relaunchable
  prepared state after the launcher is hardened.
- `doc/running/remote_training_campaign_status.json` and
  `doc/running/remote_training_campaign_checklist.md` record the failed remote
  attempt and should remain useful for diagnosis.
- `.temp/remote_training_campaigns/2026-06-15-10-13-57_wave3_harmonic_prior_residual_campaign_2026_06_14/remote_training_campaign.log`
  contains the observed Conda Unicode failure.

No subagent is planned for this fix.

## Implementation Steps

1. Update the shared remote PowerShell launcher so every remote Conda Python
   call uses a UTF-8 environment and `--no-capture-output`.
2. Update the remote launcher documentation to record the encoding hardening.
3. Restore `doc/running/active_training_campaign.yaml` from `running` to
   `prepared` for the same Wave 5.1 campaign, preserving the launch commands and
   protected-file list.
4. Run PowerShell parser validation on the shared remote launcher.
5. Run Markdown QA on touched authored Markdown.
6. Run the Wave 5.1 launcher `-PreflightOnly` locally.
7. Do not relaunch the remote campaign from Codex; provide the same operator
   command for the user to retry.
