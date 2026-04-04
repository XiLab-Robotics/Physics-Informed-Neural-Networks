# Remote Training Launcher Command-Length Fix

## Overview

The prepared targeted LAN-remote follow-up campaign failed before the remote
training process actually started.

The failure is operational, not model-related:

- `ssh.exe : The command line is too long.`

The current remote launcher builds a large encoded PowerShell command and sends
it directly to `ssh.exe`. The new campaign is large enough that the resulting
Windows command line exceeds the local launcher limit before the remote
workstation can even start `run_training_campaign.py`.

Because the current active campaign is marked as `prepared`, this fix touches a
protected campaign file and requires explicit user approval before the
implementation proceeds.

## Technical Approach

The fix should keep the current repository-owned SSH workflow but change how the
remote script payload is transported.

Instead of passing the full encoded script as one oversized command-line
argument to `ssh.exe`, the launcher should use a shorter remote bootstrap path
that stays below the Windows command-line limit. The minimal safe direction is
to stage the remote PowerShell payload into a temporary file inside the remote
repository and then invoke that file through a short `ssh` command.

This keeps the current orchestration model intact:

- local workstation remains the canonical control surface;
- remote workstation still executes the same campaign logic;
- artifact sync and bookkeeping stay in the existing launcher;
- only the transport mechanism for the remote PowerShell payload changes.

After the fix, the blocked campaign should be relaunched through the already
prepared dedicated launcher without regenerating the campaign package.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `scripts/campaigns/run_targeted_remote_followup_campaign.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/scripts/campaigns/run_targeted_remote_followup_campaign.md`
- `doc/guide/project_usage_guide.md`
- `doc/running/active_training_campaign.yaml`
- `doc/running/remote_training_campaign_status.json`
- `doc/running/remote_training_campaign_checklist.md`

## Implementation Steps

1. Refactor the remote PowerShell transport in
   `scripts/campaigns/run_remote_training_campaign.ps1` so the launcher no
   longer sends an oversized encoded script directly on the `ssh.exe` command
   line.
2. Keep the existing remote execution semantics and artifact-sync behavior
   unchanged outside the transport fix.
3. Update the canonical launcher note and any affected user-facing workflow
   guidance if the operator-visible behavior changes.
4. Re-run the prepared targeted remote follow-up campaign after the fix.
5. Record the real execution outcome only after the campaign either completes
   or fails for a model-side reason instead of a launcher transport limit.
