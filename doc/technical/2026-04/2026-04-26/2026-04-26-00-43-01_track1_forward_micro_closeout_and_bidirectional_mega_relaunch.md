# Track 1 Forward Micro Closeout And Bidirectional Mega Relaunch

## Overview

The forward-only remote micro-campaign has now completed successfully and has
served its intended purpose as the relaunch gate for the original-dataset
Track 1 workflow.

The repository must now:

1. close the forward-only micro-campaign formally as a completed diagnostic
   gate;
2. preserve its operational evidence without promoting its results to the
   benchmark as a scientific closeout wave;
3. regenerate the full bidirectional original-dataset mega-campaign from zero;
4. expose the fresh remote launch command for the new full campaign.

## Technical Approach

The relaunch must reuse the now-validated original-dataset remote stack:

- original-dataset validation runner;
- YAML queue parsing through temporary Python helper scripts;
- ONNX dependency preflight on the remote workstation;
- remote progress markers with reduced console noise;
- canonical output roots under `output/training_campaigns` and
  `output/validation_checks`.

The old broken mega-campaign remains discarded and must not be resumed.

The new mega-campaign should be a fresh package with a new campaign identity,
new active-state payload, and the same approved full-surface intent:

- `10` families;
- `2` directions;
- `20` attempts per family-direction surface;
- `400` total YAML runs.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- `doc/guide/project_usage_guide.md`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1`
- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/`
- `output/training_campaigns/track1/exact_paper/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/`

## Implementation Steps

1. Formalize the completed forward-only micro-campaign through one campaign
   results report that records the successful gate outcome.
2. Reconcile `active_training_campaign.yaml`, which is currently stale because
   it still points to the prepared micro-campaign payload instead of the now
   completed gate outcome.
3. Regenerate the full bidirectional original-dataset mega-campaign from zero
   with a fresh campaign name and canonical remote operator launcher state.
4. Confirm that the mega-campaign launcher still points to the validated
   original-dataset runner path and inherited remote logging behavior.
5. Update the launcher note and usage guide if the operator-facing launch
   contract changed.
6. Run Markdown QA and warning-free Sphinx validation on the touched scope.
7. Stop and wait for explicit user approval before launching the new mega
   campaign.
