# Polished Early-Wave Parallel Training

## Overview

The polished `RCIM Model-Bank Reproduction` campaign is being run on another
workstation. This checkout should remain usable for a separate, bounded
`polished_dataset` training batch that starts the model-development retraining
without overwriting or closing the active RCIM campaign state.

The intended batch is the early-wave subset of the already prepared
`polished_dataset_full_wave_retraining_2026_06_22` campaign: the first 36
queue configs, covering the baseline/static and temporal model families across
`global`, `fw`, and `bw` surfaces.

## Technical Approach

Create a dedicated early-wave campaign package that references the existing
validated full-wave queue configs instead of duplicating or modifying them.
This keeps the canonical full-wave campaign intact while allowing operator
execution of the first training block on this machine.

Because `doc/running/active_training_campaign.yaml` currently marks the RCIM
campaign as prepared and protected, this work must not silently replace that
state. The launcher can be prepared independently, but starting the campaign
requires explicit operator approval acknowledging that the RCIM campaign is
running elsewhere and that this local checkout will execute an early-wave
parallel batch.

## Involved Components

- `data/polished_dataset/`
- `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/queue/`
- `scripts/training/run_training_campaign.py`
- `scripts/campaigns/cross_wave/`
- `doc/scripts/campaigns/cross_wave/`
- `doc/reports/campaign_plans/cross_wave/polished_dataset/`
- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/`

## Implementation Steps

1. Use the existing polished full-wave queue entries `001` through `036`.
2. Create a dedicated early-wave campaign manifest referencing those configs.
3. Create an operator-facing PowerShell launcher with local and `-Remote`
   execution paths.
4. Create a launcher note and campaign plan documenting the 36-run scope.
5. Update active campaign state only after explicit approval because the RCIM
   campaign remains protected.
6. Run preflight only before handing off the launch command.
7. Do not start training from Codex until the user explicitly approves this
   campaign package and the protected-state override.
