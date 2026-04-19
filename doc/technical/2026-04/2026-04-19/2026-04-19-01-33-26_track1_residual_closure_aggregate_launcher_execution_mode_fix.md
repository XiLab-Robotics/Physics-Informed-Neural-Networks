# Track 1 Residual Closure Aggregate Launcher Execution Mode Fix

## Overview

The newly prepared aggregate launcher for the overnight `Track 1`
remaining-family residual-cell closure wave fails before launching any family
campaign.

The failure occurs immediately in:

- `scripts/campaigns/run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1`

Observed error:

- PowerShell interprets `remote` and `local` inside the execution-mode status
  line as commands rather than string literals;
- the aggregate launcher therefore aborts before the first family launcher is
  invoked.

Because this launcher belongs to the currently prepared campaign tracked in
`doc/running/active_training_campaign.yaml`, it is a protected campaign file.
Runtime repair therefore still requires explicit user approval before the file
is modified.

## Technical Approach

This is a narrow launcher-only repair.

The root cause is the execution-mode banner:

- current pattern:
  `$(if ($Remote) { remote } else { local })`
- required pattern:
  `$(if ($Remote) { 'remote' } else { 'local' })`

The fix should:

1. replace the unquoted tokens with explicit string literals;
2. keep the rest of the aggregate launcher unchanged;
3. re-run a PowerShell parser check on the fixed launcher;
4. leave the family launchers, YAML queue, and campaign state untouched.

This is intentionally a micro-fix. The bug is in operator-facing launcher
syntax, not in the exact-paper training pipeline or in the remote execution
workflow itself.

## Involved Components

- `scripts/campaigns/run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1`
- `doc/running/active_training_campaign.yaml`
- `doc/scripts/campaigns/run_track1_remaining_family_residual_cellwise_closure_campaigns.md`
- `doc/technical/2026-04/2026-04-19/README.md`
- `doc/README.md`

No subagent is planned for this task. The repair is too small and too tightly
coupled to the active campaign package to justify delegation.

## Implementation Steps

1. Patch the aggregate launcher execution-mode line to use quoted string
   literals.
2. Run a PowerShell parser validation on the repaired launcher.
3. Run the Markdown warning pass on the touched Markdown scope.
4. Return the corrected aggregate remote-launch command to the user for the
   overnight run.
