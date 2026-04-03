# Remote Training Campaign Real Validation And Setup Guide

## Overview

This document defines the next implementation phase for the newly added remote
LAN training workflow:

1. run one real approved campaign through the new remote-training path;
2. use that campaign to validate the end-to-end remote execution and artifact
   synchronization flow on the stronger LAN workstation;
3. prepare explicit step-by-step operational guidance for what must exist on
   the local workstation and on the remote workstation before the real run;
4. keep the result structured enough that the workflow can later be promoted
   into a repository skill if the real validation succeeds.

The current repository already contains the new remote launcher and sync logic,
but it has only been validated syntactically and through local helper checks.
The next step should therefore be a real campaign that is meaningful for the
project itself, not a dummy launch with no training value.

## Technical Approach

The real validation should use one campaign that serves two purposes at once.

### 1. Validate The Original Higher-Memory Tree Question

The campaign should include a focused random-forest branch because that is the
clearest already-approved reason for using a stronger machine:

- the original more aggressive random-forest configuration failed with a
  `MemoryError` on the local workstation;
- the later conservative recovery variant completed, but with substantially
  weaker accuracy than the current `hist_gradient_boosting` leader;
- the repository still explicitly records the higher-memory follow-up as an
  open worthwhile engineering question.

### 2. Validate The Remote Neural Path Too

The campaign should also include a small number of heavier feedforward
configurations so the remote path is not validated only on CPU-side
`scikit-learn` runs.

This matters because the new remote launcher must also prove that it can:

- execute Lightning-based runs remotely;
- synchronize checkpoint-bearing output trees back correctly;
- keep registry updates coherent across both tree and neural families.

### 3. Keep The First Real Remote Campaign Narrow

The first real validation should remain deliberately small and interpretable.

The recommended shape is:

- a small random-forest ladder that is stronger than the previous conservative
  local rerun;
- one stronger `HistGradientBoostingRegressor` reference probe;
- two heavier feedforward runs that are already meaningful in the repository
  configuration space.

The goal is not to perform an unlimited search. The goal is to:

- obtain one meaningful remote tree answer;
- exercise both CPU-heavy and GPU-heavy branches;
- verify end-to-end artifact synchronization;
- keep the run count low enough that the first real validation remains easy to
  inspect and recover if something goes wrong.

### 4. Operational Guidance

The implementation should also add a clear step-by-step guide that states:

- what must already be configured on the remote workstation;
- what must be configured on the local workstation;
- what command should be launched locally;
- what tracking files should be watched during execution;
- what artifact locations should be checked after synchronization;
- what failure signatures should be treated as remote setup issues instead of
  model-quality results.

## Involved Components

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `scripts/training/build_remote_training_sync_manifest.py`
- `config/training/`
- `doc/reports/campaign_plans/`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md`
- `site/`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Keep this technical document as the approval gate for the real remote
   campaign validation phase.
2. Create a campaign planning report for a narrow but meaningful remote
   validation campaign that includes both tree and feedforward candidates.
3. After approval, generate the campaign YAML package dedicated to the remote
   validation run.
4. Write the prepared campaign state to `doc/running/active_training_campaign.yaml`.
5. Add the missing step-by-step setup and execution guidance for local and
   remote machines.
6. Launch the approved campaign through the new remote launcher and monitor the
   local tracking files.
7. Verify that campaign outputs, training runs, queue end state, and registries
   synchronize back into the canonical local repository state.
8. If the real validation succeeds, document the result and evaluate whether
   the remote-training workflow is stable enough to later become a repository
   skill.
9. Run Markdown warning checks on the touched Markdown scope.
10. Stop after implementation and verification, report the outcome, and wait
    for explicit approval before creating any Git commit.
