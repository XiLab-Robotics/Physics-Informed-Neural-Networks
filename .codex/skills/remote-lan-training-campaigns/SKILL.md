---
name: remote-lan-training-campaigns
description: Use when preparing, hardening, launching, or reviewing repository-owned LAN remote training campaigns that execute on a stronger workstation while keeping canonical campaign state and artifacts in the local repository.
---

# Remote LAN Training Campaigns

Use this skill for the repository-owned SSH-backed campaign workflow that runs
training on the LAN workstation and synchronizes the canonical artifacts back to
the local repository.

## Use This Skill For

- remote training-campaign preparation or execution;
- remote-launcher hardening and troubleshooting;
- remote artifact-sync and bookkeeping review;
- local/remote preflight clarification for LAN training runs;
- post-run recovery analysis when a remote campaign completes but artifact sync
  looks inconsistent.

## Do Not Use This Skill For

- generic SSH administration unrelated to repository training;
- the LAN AI node or video-guide workflow;
- single local training runs with no remote execution path.

## Required Checks

1. Read `doc/running/active_training_campaign.yaml`.
2. Confirm the approved planning report and campaign YAML package exist.
3. Read `doc/scripts/campaigns/run_remote_training_campaign.md`.
4. Confirm the remote assumptions:
   - SSH alias resolves;
   - remote repository path exists;
   - remote Conda environment exists;
   - dataset path is valid on the remote workstation.
5. Keep `run_name` separate from immutable `run_instance_id`.

## Workflow Priorities

1. Preserve artifact identity prepared by the campaign runner.
2. Prefer canonical recovery from `run_metadata.yaml` over trusting one stale
   manifest field.
3. Keep the local repository as the canonical review and bookkeeping surface.
4. Sync only the campaign-owned artifact set, not the whole remote repository.
5. Update the launcher note and user guide whenever the remote operator flow
   changes.

## File Targets To Read First

- `scripts/campaigns/run_remote_training_campaign.ps1`
- `scripts/training/run_training_campaign.py`
- `scripts/training/build_remote_training_sync_manifest.py`
- `scripts/training/shared_training_infrastructure.py`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/guide/project_usage_guide.md`
- `doc/running/active_training_campaign.yaml`

## Typical Outputs

- remote campaign launch or review;
- LAN preflight checklist;
- sync-contract hardening;
- bookkeeping bug analysis;
- launcher/documentation alignment pass.
