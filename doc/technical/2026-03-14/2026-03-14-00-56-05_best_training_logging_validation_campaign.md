# Best Training Logging Validation Campaign

## Overview

This document defines the preparation approach for a focused feedforward training campaign that runs only the current recommended preset:

- `config/training/feedforward/presets/best_training.yaml`

The purpose of this campaign is not to compare multiple hyperparameter variants. The purpose is to validate the revised campaign-runner terminal behavior under a real long-form training workflow while reusing the strongest currently recommended feedforward preset.

The key questions are:

1. Does the campaign runner now expose the same live terminal logging as direct single-run training?
2. Does the queue-based campaign workflow still generate the expected manifest, report, checkpoints, metrics, and campaign logs for a real run?
3. Does the current `best_training` preset still execute cleanly as a one-item campaign after the campaign-logging refactor?

## Technical Approach

The campaign should remain intentionally narrow:

1. reuse `best_training.yaml` without changing the training hyperparameters;
2. create a dedicated one-item campaign folder under `config/training/feedforward/campaigns/`;
3. copy the preset into a campaign-specific YAML file with metadata that points back to the planning report and campaign name;
4. store the prepared campaign state in `doc/running/active_training_campaign.yaml`;
5. provide the exact launch command for the user to execute from the activated Conda environment;
6. after the user confirms the campaign has started or finished, update the persistent campaign state accordingly and collect the resulting artifacts for the mandatory final reporting flow.

This keeps the test scientifically simple:

- no new architecture;
- no parameter search;
- no ambiguity about whether output differences come from hyperparameter changes or from the revised runner behavior.

## Involved Components

- `config/training/feedforward/presets/best_training.yaml`
  Source preset reused without changing its training configuration.
- `config/training/feedforward/campaigns/`
  Target location for the generated one-item campaign YAML.
- `training/run_training_campaign.py`
  Campaign runner whose latest terminal/logging behavior is the main workflow under validation.
- `doc/reports/campaign_plans/`
  Location of the required preliminary planning report.
- `doc/running/active_training_campaign.yaml`
  Persistent state file that must track the prepared campaign and its protected files.
- `output/training_campaigns/`
  Root where the campaign-level manifest, execution report, and terminal logs will be generated once the campaign is launched.

## Implementation Steps

1. Create the preliminary planning report for the one-item `best_training` validation campaign.
2. Wait for explicit user approval before generating campaign YAML files or updating the active campaign state.
3. After approval, generate a dedicated campaign folder and one YAML file derived from `best_training.yaml`.
4. Write the prepared campaign metadata and protected file list into `doc/running/active_training_campaign.yaml`.
5. Provide the exact launch command for the user.
6. After the run, inspect the produced campaign manifest, execution report, and per-run training artifacts to support the final results workflow.
