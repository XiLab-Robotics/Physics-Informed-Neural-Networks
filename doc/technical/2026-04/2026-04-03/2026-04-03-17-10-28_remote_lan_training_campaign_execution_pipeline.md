# Remote LAN Training Campaign Execution Pipeline

## Overview

This document defines the proposed repository-owned workflow for launching
approved training campaigns from the current workstation while executing the
heavy training workload on the stronger LAN workstation.

The goal is to mirror the already validated LAN AI operating model:

- keep orchestration, campaign preparation, and final documentation on the
  current workstation;
- use the remote workstation for the heavier runtime workload;
- keep the process explicit, inspectable, and repository-owned instead of
  relying on ad-hoc manual remote commands.

The user-facing target is:

- prepare the campaign locally with the existing repository workflow;
- launch the approved campaign from the local terminal;
- run the training entries on the remote workstation through SSH;
- collect the resulting artifacts back into the canonical local repository
  state.

## Technical Approach

The implementation should introduce a dedicated remote-training path that is
parallel to the existing local campaign path, not a hidden rewrite of the
current launchers.

### 1. Canonical Runtime Topology

The preferred topology should be:

- current workstation:
  - prepares the technical document and planning report;
  - generates the campaign YAML package;
  - owns the canonical Git repository used for reviews, reports, and commits;
  - launches the remote campaign from the local terminal;
  - receives the final promoted training artifacts and campaign bookkeeping.
- remote workstation:
  - hosts a synchronized clone of the same repository;
  - hosts the stronger CPU / RAM / GPU environment;
  - executes the training campaign runner;
  - writes remote-side temporary and final campaign artifacts before the local
    synchronization step.

### 2. Remote Campaign Control

The repository should expose a dedicated remote launcher, likely PowerShell-
based, that:

- uses the validated SSH alias workflow already documented for the LAN AI node;
- checks reachability of the remote workstation before launch;
- runs the campaign through a non-interactive remote command such as
  `ssh xilab-remote "cd ... && conda run -n ... python scripts/training/run_training_campaign.py ..."`;
- keeps campaign identity explicit in terminal output;
- writes local run-state tracking so a remote campaign is not an invisible
  manual process.

The remote-training path should remain explicit rather than silently replacing
the existing local `scripts/campaigns/*.ps1` launchers.

### 3. Artifact And Registry Discipline

This is the critical design constraint.

The implementation should avoid creating two drifting canonical states between
the local repository and the remote clone.

The first practical direction should be:

- treat the remote workstation as the execution node, not as the long-term
  canonical artifact registry;
- sync the campaign artifacts that matter back into the local repository after
  the remote run;
- keep the final review, results reporting, and Git-tracked state updates on
  the current workstation.

The remote workflow should explicitly define how to handle at least:

- `output/training_runs/`
- `output/training_campaigns/`
- `output/registries/families/`
- `output/registries/program/`
- campaign logs
- `doc/running/active_training_campaign.yaml` when the active campaign is
  launched remotely

The implementation should prefer a narrow, explicit synchronization step over a
blind full-repository overwrite.

### 4. Documentation And Operational Surface

If implemented, the remote path should include:

- a launcher under `scripts/campaigns/` or an adjacent canonical remote-
  training script root;
- a matching usage note under `doc/scripts/campaigns/` or another canonical
  workflow note;
- a detailed user-facing update in `doc/guide/project_usage_guide.md`;
- Sphinx portal updates under `site/`;
- explicit setup notes for the remote training environment, similar in spirit
  to the LAN AI node setup guide.

### 5. Initial Scope Boundary

The first implementation batch should stay intentionally narrow.

It should focus on:

- one repository-owned remote campaign execution path;
- one remote workstation accessed through SSH;
- one documented environment name and repository-root assumption on that remote
  machine;
- explicit stop-on-failure behavior;
- explicit post-run artifact synchronization;
- no attempt yet at multi-node scheduling, distributed training, queue
  balancing, or unattended orchestration across several machines.

## Involved Components

- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `scripts/training/run_training_campaign.py`
- `doc/running/active_training_campaign.yaml`
- `doc/guide/project_usage_guide.md`
- `site/`
- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`
- optionally a new remote-training setup note under `doc/scripts/tooling/`

## Implementation Steps

1. Keep this technical document as the approval gate for the remote-training
   workflow design.
2. After approval, inspect the current campaign launchers and choose the
   narrowest canonical integration point for a remote campaign launcher.
3. Define the remote environment assumptions and the artifact synchronization
   contract explicitly before editing the training launcher path.
4. Implement the repository-owned remote launcher and its paired
   documentation note.
5. Update the user-facing documentation and the Sphinx portal so the remote
   campaign path is discoverable and treated as a supported workflow.
6. Verify the new workflow with the narrowest safe validation pass available
   without starting an uncontrolled long campaign.
7. Run Markdown warning checks on the touched Markdown scope.
8. Stop after implementation and verification, report the outcome, and wait
   for explicit approval before creating any Git commit.
