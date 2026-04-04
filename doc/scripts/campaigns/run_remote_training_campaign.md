# Remote Training Campaign Launcher

## Overview

This launcher is the canonical repository-owned path for starting an approved
training campaign from the current workstation while executing the heavy
training runtime on the stronger LAN workstation.

It mirrors the repository pattern already used for the LAN AI node:

- the current workstation keeps orchestration, documentation, and final review;
- the remote workstation performs the heavier runtime workload;
- the workflow remains explicit and terminal-driven instead of turning into an
  undocumented manual SSH routine.

## Main Role

The launcher:

1. checks reachability of the remote workstation and its training environment;
2. syncs the local `scripts/`, `config/`, `doc/`, and `requirements.txt`
   state to the remote repository path before launch;
3. starts `scripts/training/run_training_campaign.py` on the remote machine
   through SSH and `conda run`;
4. copies back the resulting campaign manifest, training-run artifacts,
   campaign outputs, queue end state, and affected registries into the local
   repository;
5. writes local tracking files under `doc/running/` and a local terminal log
   under `.temp/remote_training_campaigns/`.

## Remote Preconditions

Before using this launcher:

1. the remote workstation must already have a working clone of this repository;
2. the remote workstation must already expose SSH access through the validated
   alias workflow, for example `ssh xilab-remote`;
3. the remote workstation must already have the target Conda environment with
   the repository training dependencies installed;
4. the remote workstation must already have access to the dataset path expected
   by the repository configs.

The validated SSH alias and remote-clone setup process is already documented in:

- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`

Use these environment variables on the current workstation for convenience:

- `STANDARDML_REMOTE_TRAINING_REPO_PATH`
- `STANDARDML_REMOTE_TRAINING_CONDA_ENV`

## Practical Use

Generic usage from the repository root:

```powershell
.\scripts\campaigns\run_remote_training_campaign.ps1 `
  -CampaignConfigPathList @(
      "config\training\residual_harmonic_mlp\campaigns\2026-03-26_wave1_residual_harmonic_family_campaign\01_residual_h08_small_frozen.yaml",
      "config\training\residual_harmonic_mlp\campaigns\2026-03-26_wave1_residual_harmonic_family_campaign\02_residual_h08_small_joint.yaml"
  ) `
  -CampaignName "remote_residual_test_campaign" `
  -PlanningReportPath "doc\reports\campaign_plans\2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md" `
  -RemoteHostAlias "xilab-remote"
```

If the remote repository path and Conda environment are stored in environment
variables, the launcher can stay short.

## Tracking Files

The launcher now writes:

- `doc/running/remote_training_campaign_status.json`
- `doc/running/remote_training_campaign_checklist.md`
- `.temp/remote_training_campaigns/<timestamp>_<campaign_slug>/remote_training_campaign.log`

Use these files to inspect:

- current stage;
- remote host and environment assumptions;
- selected campaign YAML paths;
- remote campaign output directory;
- synchronized artifact paths;
- last failure message when the remote run stops early.

## Sync Contract

The remote path does not blindly overwrite the whole local repository after the
run.

Instead, it syncs back the campaign artifacts that define the canonical result:

- the campaign output directory under `output/training_campaigns/`;
- each per-run artifact directory under `output/training_runs/`;
- the queue end state for the executed YAML files;
- the affected family registries;
- the program-level best registry.

This keeps the local repository as the canonical review surface while still
using the LAN workstation as the execution node.

The sync list is now built on the remote workstation after campaign completion
instead of being inferred only from a local copy of the campaign manifest. That
hardening matters because the helper can inspect the real remote output tree and
recover the canonical artifact directory from `run_metadata.yaml` if one stale
manifest field would otherwise point at the wrong immutable run folder.

The return path now transfers the synchronized artifacts path by path instead of
packing the full artifact set into one large multi-path archive. This keeps the
sync contract manifest-driven, but removes the brittle completion-path behavior
that appeared in the first long remote follow-up campaign.

## Bookkeeping Hardening

The launcher now relies on two complementary protections:

1. the training entrypoints preserve an already prepared `run_instance_id`
   instead of regenerating a second immutable identity when a queue-driven run
   is executed;
2. the remote sync helper still checks the real output tree through
   `run_metadata.yaml` before finalizing the artifact list, so one stale path in
   the manifest does not silently drop a completed run from the sync set.

This means the campaign manifest, queue end state, and synchronized artifact
paths should now converge on the same canonical immutable run directory even
after long remote executions.
