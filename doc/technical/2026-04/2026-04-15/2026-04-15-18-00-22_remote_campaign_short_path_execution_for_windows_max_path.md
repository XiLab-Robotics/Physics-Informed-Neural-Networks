# Remote Campaign Short-Path Execution For Windows Max Path

## Overview

The remote `Track 1` `SVR` campaign investigation has now exposed the actual
root cause on the LAN workstation: the first campaign YAML resolves to a remote
absolute path of exactly `260` characters.

That explains the previously inconsistent behavior:

- `Get-ChildItem` can enumerate the long YAML names inside the campaign
  directory;
- `Test-Path` on the exact file returns `False`;
- Python `Path.exists()` returns `False`;
- Python file creation at the exact destination path fails even though the
  parent directory exists;
- the shorter `README.md` path in the same folder behaves normally.

This is no longer primarily a sync-transport or verification bug. It is a
Windows `MAX_PATH` problem on the remote node.

## Technical Approach

The remote launcher should stop executing verification and training against the
long native repository path directly.

Instead, the launcher should create a short remote execution alias for the
repository root, for example a temporary drive mapping such as `R:` or another
validated unused drive letter, and then use that short path consistently for:

1. post-sync source-file verification;
2. any required source-file materialization step;
3. the remote `run_training_campaign.py` invocation;
4. the post-run manifest and sync-manifest generation steps.

The real repository clone can stay where it is. The fix is to expose that same
clone through a much shorter path during the remote session so the exact-paper
campaign YAMLs and other long repository-managed files remain below the Windows
path-length ceiling.

The launcher should also:

- print the chosen short execution root in the terminal log;
- cleanly remove the temporary mapping after success or failure when possible;
- avoid colliding with an already occupied drive letter.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
  Canonical SSH-backed remote launcher that currently operates directly against
  the long repository path and therefore reproduces the Windows path-length
  failure.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Operator note that should document the short-path execution alias once the
  launcher begins using it.
- `scripts/training/run_training_campaign.py`
  Training entrypoint whose current source-config path resolution fails only
  because the remote absolute paths are too long on the Windows node.
- `doc/running/remote_training_campaign_status.json`
  Tracking surface that should reflect the short execution root if the launcher
  starts recording it.

## Implementation Steps

1. Add a short-path remote execution root setup phase to the remote launcher,
   using a validated temporary drive letter or equivalent short alias.
2. Rebase remote verification, source-file materialization, campaign execution,
   and sync-manifest generation on that short execution root instead of the
   original long repository path.
3. Print the chosen short execution root in the terminal log and status
   surfaces.
4. Clean up the temporary mapping after the remote run whenever possible.
5. Retest the current `Track 1` `SVR` remote campaign and confirm that the
   source-config enqueue phase now gets past the first YAML path.
