# Remote Campaign User-Driven Launch Handoff

## Overview

This task formalizes the LAN-remote training campaign workflow so Codex no
longer keeps the chat occupied while a prepared remote campaign is being
executed. The target operating model is the same one already used for local
campaigns: Codex prepares the campaign package, generates the dedicated
PowerShell launcher, provides the exact launch command, and then waits for the
user to report when the campaign has been started and when it has finished.

## Technical Approach

The implementation will align the remote-campaign operator flow with the
existing local-campaign pattern without removing the SSH-backed remote runtime
path. The main change is procedural and documentation-facing, but it also needs
small launcher and bookkeeping alignment so the generated remote campaign bundle
is clearly presented as a user-launched artifact rather than a Codex-held live
execution session.

The work will:

1. inspect the current remote launcher and dedicated campaign-wrapper pattern;
2. define the canonical operator handoff points for remote prepared campaigns;
3. update the remote launcher note, usage guide, and any affected campaign
   preparation outputs so they explicitly present the exact terminal command the
   user should run;
4. preserve the existing persistent campaign-state contract in
   `doc/running/active_training_campaign.yaml`, including the follow-up updates
   when the user later reports that the campaign has started or finished.

No subagent is planned for this implementation. The change is local,
repository-specific, and tightly coupled to the existing launcher and
documentation workflow.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `scripts/campaigns/run_*remote*.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/scripts/campaigns/run_*remote*.md`
- `doc/guide/project_usage_guide.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Inspect the current remote campaign launcher flow and the dedicated
   campaign-wrapper scripts to identify where the operator handoff should be
   made explicit.
2. Update the remote launcher preparation workflow so each approved remote
   campaign clearly produces a dedicated PowerShell launcher and a copy-ready
   terminal command for the user.
3. Align the repository documentation and campaign-state wording with the new
   user-driven launch and completion reporting flow.
4. Run the required Markdown checks on the touched Markdown scope.
5. Report the prepared workflow change and wait for explicit approval before
   creating the Git commit.
