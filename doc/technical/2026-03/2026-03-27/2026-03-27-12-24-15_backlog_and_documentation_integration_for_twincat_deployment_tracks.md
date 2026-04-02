# Backlog And Documentation Integration For TwinCAT Deployment Tracks

## Overview

Two approved technical documents already established a future TwinCAT
deployment-evaluation workstream for this repository:

- `2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
- `2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md`

Those documents defined:

- the imported TestRig TwinCAT reference baseline;
- the need to preserve the legacy Beckhoff deployment path as the main target;
- the need to evaluate the newer `TF3820/TF3830` path in parallel;
- the option to execute preparatory work in isolated mode when needed.

The repository still needs one more step: integrate those approved decisions
into the operational backlog and into the running/documentation indexes so the
plan is visible from the canonical execution surfaces rather than living only in
historical technical notes.

## Technical Approach

This change is documentation-only.

It should:

- update the live backlog so the TwinCAT deployment work becomes an explicit
  future execution item;
- expose the new planning note in the documentation indexes;
- keep the legacy `TF38x0` branch clearly marked as the primary deployment
  direction;
- keep the `TF3820/TF3830` branch clearly marked as a secondary comparison
  track rather than an already-approved replacement.

The change should not:

- modify campaign YAML files;
- alter campaign artifacts or registries;
- change training code or current deployment code;
- claim that either TwinCAT deployment branch has already been implemented.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/running/te_model_live_backlog.md`
  Canonical operational backlog that should now include the TwinCAT deployment
  evaluation branch explicitly.
- `doc/README.md`
  Main project documentation index that should expose this technical note and
  the updated running-state meaning.
- `doc/running/README.md`
  Running-state index that should mention the new deployment-evaluation track
  inside the operational backlog role.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Existing reference note that already captures the technical baseline to which
  the backlog entry should point.
- `doc/technical/2026-03/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
  Approved technical note that established the TestRig TwinCAT analysis task.
- `doc/technical/2026-03/2026-03-26/2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md`
  Approved technical note that established the post-campaign dual-track
  deployment evaluation plan.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Update the live backlog so TwinCAT deployment evaluation becomes an explicit
   planned execution item.
3. Mark the legacy `TF38x0` branch as the primary deployment target in the live
   backlog.
4. Mark the `TF3820/TF3830` branch as a separate comparison track with isolated
   mode allowed for preparatory work when appropriate.
5. Update the documentation indexes so future sessions can find the new plan
   from canonical repository entry points.
6. Report completion and wait for explicit user approval before any commit.
