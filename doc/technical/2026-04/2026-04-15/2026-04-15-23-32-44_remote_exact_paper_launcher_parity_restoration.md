# Remote Exact-Paper Launcher Parity Restoration

## Overview

The current LAN remote wrapper for
`track1_svr_reference_grid_search_repair_campaign` has drifted away from the
behavior of the approved local launcher
`scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign.ps1`.
The result is unacceptable operator experience and incorrect execution
semantics:

- the local repository receives an unwanted path-shaped extraction tree rooted
  at `Users/Martina Salami/...`;
- the remote wrapper does not expose the same per-run live logs and failure
  semantics as the local exact-paper launcher;
- the remote execution path calls the generic campaign runner
  `run_training_campaign.py`, which does not support
  `exact_paper_family_bank`, so the campaign fails immediately while the
  remote wrapper still appears superficially successful.

The restoration goal is strict launcher parity: the remote workflow must behave
like the local exact-paper launcher, with remote-only pre-sync and post-sync
steps wrapped around the same exact-paper run loop.

## Technical Approach

The fix will stop treating this exact-paper campaign as a generic training
campaign. Instead, the remote flow will be restructured around the already
approved exact-paper launcher contract:

1. keep the exact same campaign identity, config list, log naming, and
   run-by-run failure handling used by the local launcher;
2. perform remote preflight and source sync before the run;
3. execute the real exact-paper per-config workflow remotely, equivalent to the
   local `run_track1_svr_reference_grid_search_repair_campaign.ps1` behavior;
4. stream remote terminal output and preserve per-run log files under the
   remote campaign output tree exactly as the local launcher does;
5. sync back only the canonical campaign-owned artifact set into the local
   repository, without recreating any absolute-remote-path directory tree.

The generic `run_remote_training_campaign.ps1` helper will be narrowed so it
can support a launcher-parity mode for exact-paper operator campaigns rather
than forcing everything through `run_training_campaign.py`.

`run_training_campaign.py` is not being abandoned. It remains the intended
entrypoint when the project returns to temporal-model campaign execution. A
follow-up backlog item must therefore verify and repair that generic pipeline
after the current remote exact-paper restoration, and restore any code paths
that were destabilized by the recent remote-launch debugging commits.

## Involved Components

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
- `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign.ps1`
- `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.md`
- `doc/running/active_training_campaign.yaml`

Protected campaign files expected to require modification:

- `scripts/campaigns/track1/svm/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.md`

No subagent is planned for this implementation.

## Implementation Steps

1. Inspect the local exact-paper launcher and identify the minimal remote-only
   wrapper points that should exist before and after the run loop.
2. Refactor the remote launcher path so exact-paper campaigns invoke the same
   per-config validation workflow and log layout as the local launcher instead
   of the generic training campaign runner.
3. Remove the current sync-back behavior that materializes remote absolute-path
   trees inside the local repository and replace it with repository-relative
   artifact sync only.
4. Align remote failure handling so a failed exact-paper config fails the remote
   campaign visibly and immediately, just like the local launcher.
5. Update the remote launcher notes and active campaign metadata to describe
   the parity-based remote operator flow.
6. Record a backlog follow-up for `run_training_campaign.py` so the temporal
   campaign pipeline is revalidated and, if needed, restored to the last known
   good behavior before the recent remote exact-paper debugging sequence.
7. Run Markdown QA on the touched documentation scope and validate the remote
   launcher command contract before closing the task.
