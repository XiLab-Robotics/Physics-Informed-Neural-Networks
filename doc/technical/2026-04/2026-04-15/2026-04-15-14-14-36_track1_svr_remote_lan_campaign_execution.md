# Track 1 SVR Remote LAN Campaign Execution

## Overview

The current `Track 1` `SVR` reference-grid repair campaign is already prepared
and approved locally, but the first local attempts show that the
paper-reference `GridSearchCV` path is heavy enough to justify execution on the
stronger LAN workstation. The repository already contains a canonical
SSH-backed remote campaign launcher, so the correct next step is not to invent
an ad-hoc remote routine, but to adapt this prepared exact-paper campaign to
the existing repository-owned remote workflow.

This document defines the narrow work needed to run the current `SVR`
reference-grid repair campaign on the LAN workstation while keeping the local
repository as the canonical state, bookkeeping, and review surface.

## Technical Approach

The implementation should reuse the existing remote campaign launcher
infrastructure under `scripts/campaigns/run_remote_training_campaign.ps1`
instead of creating a new one-off launcher for this specific exact-paper
campaign.

The remote execution path should:

1. use the already approved campaign YAML package for
   `track1_svr_reference_grid_search_repair_campaign`;
2. keep the current planning report and campaign identity visible in the remote
   launcher invocation;
3. execute on the LAN workstation through the validated SSH alias;
4. use the remote repository clone and remote Conda environment already
   expected by the canonical launcher;
5. sync back the campaign manifest, validation artifacts, campaign output, and
   affected registries into the local repository after completion.

Because the current campaign is already marked `active` in
`doc/running/active_training_campaign.yaml`, the implementation must handle the
transition carefully and update the campaign state explicitly rather than
silently repurposing the old local-launch assumptions.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
  Canonical repository-owned remote launcher that should be reused.
- `doc/scripts/campaigns/run_remote_training_campaign.md`
  Canonical operator documentation for the SSH-backed campaign path.
- `doc/running/active_training_campaign.yaml`
  Current protected campaign state that must be updated carefully if the launch
  mode changes from local to remote.
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svr_reference_grid_search_repair_campaign/`
  Already approved exact-paper campaign package that should remain the source
  of truth for the queue.
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign.md`
  Current local-launch note that may need a companion remote-launch note or a
  cross-reference if the operator flow is expanded.

## Implementation Steps

1. Inspect the remote launcher contract and map the current exact-paper `SVR`
   campaign onto its required parameters.
2. Prepare a dedicated remote-launch wrapper or a precise operator command for
   this campaign using the canonical remote launcher.
3. Update the active campaign state so the launch mode, remote host alias,
   remote repository path, and remote Conda environment are explicit.
4. Add or update the campaign launcher note so the operator has one exact
   remote command to run from the repository root.
5. Verify the resulting command and file mapping without executing the remote
   run yet, then hand the exact command to the operator.
