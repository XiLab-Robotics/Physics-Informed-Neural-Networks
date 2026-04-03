# Remote Training Pipeline Hardening And Skill Promotion

## Overview

The first real LAN-remote training campaign proved that the repository-owned
remote execution flow is already usable, but it also exposed one remaining
bookkeeping defect that prevents the workflow from being considered stable
enough for repository-skill promotion.

The concrete failure mode observed during the real campaign was a mismatch
between the `run_instance_id` serialized into the campaign manifest and the
actual immutable output directory created by the tree-regression entrypoint.
That mismatch forced a manual artifact recovery step for one completed run.

This task hardens the remote training pipeline so the generic launcher can
reliably recover all artifacts after real remote execution, then promotes the
validated workflow into a dedicated repository-local Codex skill for future
reuse.

No subagent is currently planned for this implementation. The scope is bounded
to repository-local pipeline, documentation, and skill packaging work.

## Technical Approach

The hardening work should address the root cause before adding recovery layers.
The primary fix is to preserve an already prepared artifact identity when the
campaign runner hands a queue configuration to the concrete training entrypoint.
If the configuration already carries `metadata.run_instance_id`,
`metadata.output_run_name`, and the intended artifact kind, the training
entrypoint must not regenerate a second immutable identity.

After the identity-preservation fix, the remote sync pipeline should still gain
an explicit fallback path so one stale manifest field cannot silently lose
artifacts again. The sync-manifest helper should therefore be extended to
resolve artifact directories from the campaign manifest and, when needed, to
cross-check canonical `run_metadata.yaml` files or adjacent output roots before
building the final sync list.

Once the generic launcher and sync helper are hardened, the repository should
promote the remote-training workflow into a new local skill under
`.codex/skills/`. The skill should explain when to use the workflow, the
required local and remote preflight checks, the expected artifact bookkeeping
behavior, and the exact files to inspect before or after a remote campaign.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/train_tree_regressor.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/run_training_campaign.py`
- `scripts/training/build_remote_training_sync_manifest.py`
- `scripts/campaigns/run_remote_training_campaign.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/guide/project_usage_guide.md`
- `.codex/skills/`
- `doc/README.md`

## Implementation Steps

1. Re-read the real remote-campaign bug surface in the current runner, training
   entrypoints, and sync helper.
2. Fix artifact-identity preservation so already prepared training configs keep
   the same `run_instance_id` through campaign execution.
3. Harden sync-manifest resolution so remote artifact pullback can recover from
   stale manifest path fields without manual intervention.
4. Update the generic remote launcher note and the detailed usage guide to
   reflect the hardened behavior and operator expectations.
5. Create a new repository-local skill for remote LAN training campaigns with a
   concise workflow-oriented `SKILL.md`.
6. Run repository-required checks on the touched Markdown scope and any
   implementation verification needed for the hardened pipeline.
