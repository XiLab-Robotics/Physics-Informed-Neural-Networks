# Track 1 Bidirectional Mega Campaign Remote Repackaging And Interrupted State Reconciliation

## Overview

The prepared `Track 1` bidirectional original-dataset mega-campaign was
packaged incorrectly as a local sequential launcher instead of following the
standard remote campaign pattern already used in prior `Track 1` exact-paper
work.

The user started the local launcher and then interrupted it. The active
campaign state still reports the campaign as `running`, so the persistent
campaign baseline is now inconsistent with reality.

This task repairs that situation in two stages:

1. close the current incorrectly packaged campaign as `interrupted`;
2. repackage the same bidirectional mega-campaign surface with the canonical
   remote launcher pattern and remote metadata.

## Technical Approach

The repair must preserve the already approved scientific campaign surface:

- `10` families;
- `2` directions;
- `20` attempts per family-direction surface;
- total queue size `400`.

Only the campaign orchestration layer changes.

The corrected package should:

- replace the local sequential launcher with a remote-capable launcher that
  follows the established exact-paper `-Remote` pattern;
- populate remote campaign metadata in
  `doc/running/active_training_campaign.yaml`;
- keep the generated YAML queue aligned with the existing campaign naming and
  artifact roots unless a narrow rename is required for consistency;
- expose the exact remote launch command expected by the operator.

The interrupted local attempt should not be treated as a valid scientific run.
It should be recorded only as an interrupted packaging mistake so the next
campaign starts from a clean and truthful operational state.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-25-12-02-54_track1_bidirectional_original_dataset_mega_campaign_plan_report.md`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- any shared remote exact-paper launcher helper reused by the corrected wrapper
- `doc/guide/project_usage_guide.md` if the user-facing launch contract changes

## Implementation Steps

1. Mark the current active campaign as `interrupted` with an explicit note that
   the package was incorrectly prepared as local instead of remote.
2. Review the existing exact-paper remote launcher pattern and reuse it for the
   bidirectional mega-campaign wrapper.
3. Update the preparation script so the active campaign state is emitted as a
   remote campaign with populated remote metadata instead of
   `local_sequential_launcher`.
4. Update the mega-campaign launcher and launcher note so the operator gets the
   canonical `-Remote` path and parameters.
5. Regenerate or refresh the prepared campaign state and verify that the queue,
   launcher, planning report, and persistent state remain aligned.
6. Run Markdown QA on touched documentation and rebuild Sphinx if portal-facing
   docs change.
