# Campaign Launcher Remote Execution Standard

## Overview

Plan the retrofit that makes the prepared `Wave 2C` campaign launcher runnable
with `-Remote` and formalizes the same remote-capable launcher requirement for
future campaign packages.

The current `Wave 2C` launcher is local-only. Its real parameter surface is:

```powershell
param(
    [string]$PythonExecutable = "python"
)
```

The user approved modifying protected campaign files for this task. The
prepared campaign state currently protects the `Wave 2C` launcher and launcher
note, so this document records the intended protected-file edit before code is
changed.

No Codex subagent is planned for this work. If subagent use becomes useful
later, the proposed subagent name, task boundary, and approval requirement must
be documented before asking for approval.

## Technical Approach

The implementation should keep the dedicated campaign launcher as the operator
entry point and add a `-Remote` path instead of replacing it with a generic
manual command.

The `Wave 2C` launcher should support:

- local execution with the existing command;
- remote execution with `-Remote`;
- configurable `RemoteHostAlias`, `RemoteRepositoryPath`, and
  `RemoteCondaEnvironmentName`, using the same environment-variable defaults
  already used by repository remote-training tooling;
- source sync before remote launch for the code, configs, docs, launcher, and
  active campaign state needed by the campaign;
- remote execution through the repository-owned
  `scripts/training/run_training_campaign.py` queue runner;
- artifact sync back after remote completion for campaign outputs, training
  runs, queue end state, registries, and campaign state artifacts;
- explicit failure if source sync, remote execution, or artifact sync fails.

The implementation should prefer reusing
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` where
practical, because that script already owns the manifest-driven remote sync
contract. The dedicated `Wave 2C` launcher can dispatch to the generic remote
infrastructure in `-Remote` mode while retaining its local queue-file list for
normal execution.

The repository rule should also be formalized in `AGENTS.md`: every future
campaign launcher must provide a remote execution path and must synchronize
required source inputs before launch and campaign artifacts after completion.

## Involved Components

- `scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1`
  Protected prepared launcher to retrofit with `-Remote`.
- `doc/scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.md`
  Protected operator note to update with local and remote commands.
- `scripts/campaigns/wave_2/prepare_wave2c_residual_harmonic_temporal_hybrid_campaign.py`
  Campaign package generator to update so regenerated launchers preserve
  `-Remote` support.
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  Existing remote training campaign infrastructure to reuse or mirror.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Existing remote workflow contract and sync semantics.
- `doc/running/active_training_campaign.yaml`
  Prepared campaign state to keep aligned with the new local and remote launch
  commands.
- `AGENTS.md`
  Repository instruction file where the future-launcher rule must be added.
- `doc/guide/project_usage_guide.md`
  User-facing guide to update if the approved work changes the campaign launch
  flow.
- `site/`
  Sphinx source tree to update or rebuild if user-facing documentation changes
  within portal scope.

## Implementation Steps

1. Wait for explicit approval of this technical document.
2. Read the current generic remote launcher implementation and identify the
   minimal dedicated-launcher wrapper needed for Wave 2C.
3. Add `-Remote` parameters to the Wave 2C launcher:
   `RemoteHostAlias`, `RemoteRepositoryPath`, and
   `RemoteCondaEnvironmentName`.
4. In local mode, preserve the existing local campaign execution behavior.
5. In remote mode, dispatch to the generic remote training launcher with the
   18 prepared Wave 2C queue YAML files, campaign name, planning report path,
   and remote settings.
6. Update the Wave 2C launcher note with both local and `-Remote` commands and
   the source/artifact sync contract.
7. Update the Wave 2C preparation script so regenerated launchers and notes keep
   the same `-Remote` behavior.
8. Update `doc/running/active_training_campaign.yaml` so `launch_command_list`
   includes both local and remote commands.
9. Add the future-launcher rule to `AGENTS.md`.
10. Update user-facing docs if needed and rebuild the Sphinx portal with
    warning-as-error behavior.
11. Run PowerShell parse checks, Markdown QA, and any targeted launcher
    dry-run/help checks that do not launch training.
