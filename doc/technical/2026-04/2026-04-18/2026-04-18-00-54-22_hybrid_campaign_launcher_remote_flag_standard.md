# Hybrid Campaign Launcher Remote Flag Standard

## Overview

This document formalizes a repository-wide launcher rule for future campaign
preparation work.

The requested standard is that new campaign launchers should not be split into:

- one local-only `.ps1`;
- one separate remote-only `.ps1`.

Instead, new campaigns should prefer one hybrid launcher that supports both
execution modes:

- local execution by default;
- remote execution through a `-Remote` switch.

This rule is being introduced while preparing the next exact-paper `Track 1`
family campaigns, but the intent is broader: future campaign creation should
reuse the same launcher contract whenever the workflow is compatible with the
existing local plus LAN-remote campaign infrastructure.

## Technical Approach

The hybrid launcher standard should be:

- one canonical launcher per campaign;
- one canonical launcher note per campaign;
- one shared campaign identity regardless of execution mode;
- one optional `-Remote` switch that activates the repository remote-operator
  execution path.

When `-Remote` is omitted, the launcher should behave like the current local
campaign wrappers:

- resolve the campaign config list;
- run the campaign locally;
- write logs and artifacts under the prepared local output roots.

When `-Remote` is present, the same launcher should expose the already familiar
remote arguments:

- `RemoteHostAlias`
- `RemoteRepositoryPath`
- `RemoteCondaEnvironmentName`

and should then execute the corresponding remote workflow:

- LAN preflight;
- source sync;
- remote launcher execution against the same prepared campaign package;
- synchronized artifact recovery into the local repository.

This keeps campaign operation simpler for the user and avoids redundant local
and remote launcher pairs for every new campaign.

## Involved Components

- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `scripts/training/run_training_campaign.py`
- `scripts/training/build_remote_training_sync_manifest.py`
- `scripts/training/shared_training_infrastructure.py`
- `doc/guide/project_usage_guide.md`
- campaign-local YAML packages under `config/`

No subagent is planned for this work. The standardization remains local to the
repository campaign workflow.

## Implementation Steps

1. Update the currently approved `Track 1` remaining-family campaign plan so it
   explicitly uses hybrid launchers with a `-Remote` switch.
2. During the approved implementation phase, generate the new family launchers
   and the aggregate launcher in hybrid form rather than producing separate
   local and remote script pairs.
3. Reuse the existing remote-operator argument contract:
   `RemoteHostAlias`, `RemoteRepositoryPath`, and
   `RemoteCondaEnvironmentName`.
4. Document the hybrid launcher rule in the generated launcher notes so users
   can see both the default local command and the `-Remote` variant.
5. Treat this hybrid pattern as the default for future new campaign creation,
   unless a campaign has a concrete technical reason that prevents local and
   remote execution from sharing one canonical `.ps1`.
