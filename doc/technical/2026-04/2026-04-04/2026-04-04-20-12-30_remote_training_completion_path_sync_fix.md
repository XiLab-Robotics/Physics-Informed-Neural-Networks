# Remote Training Completion Path Sync Fix

## Overview

This task fixes the remaining LAN-remote training launcher defect that still
requires manual local recovery after the remote campaign has already completed
successfully. The objective is to make the completion path and artifact return
phase fully automatic again so the launcher can promote a completed remote
campaign back into the local repository without operator intervention.

## Technical Approach

The fix will focus on the local completion path inside
`scripts/campaigns/run_remote_training_campaign.ps1`, especially the post-run
artifact sync stages that happen after the remote training process exits. The
implementation will:

1. reproduce and inspect the failing sync/control-flow path in the current
   launcher;
2. harden the remote-to-local artifact transfer step so it does not fail on the
   current Windows SSH/PowerShell path combination after long remote runs;
3. preserve the existing campaign identity, manifest-driven artifact contract,
   and status/checklist bookkeeping files;
4. update the launcher note and usage guide if the operator-visible behavior or
   recovery semantics change.

No subagent is planned for this implementation. The work is local, bounded, and
tightly coupled to the repository-owned launcher and bookkeeping files.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/guide/project_usage_guide.md`
- `doc/running/remote_training_campaign_status.json`
- `doc/running/remote_training_campaign_checklist.md`

## Implementation Steps

1. Inspect the current launcher completion path and identify the concrete
   failure surface that forced manual recovery in the last remote campaign.
2. Implement a repository-owned fix that keeps the sync contract explicit and
   PowerShell-5-compatible.
3. Update the launcher documentation if the operator flow or failure semantics
   change.
4. Run the required Markdown checks on the touched documentation scope.
5. Report the completed fix and wait for explicit approval before creating the
   Git commit.
