# Post-Campaign Wave Naming And Backlog Alignment Reminder

## Overview

The currently running residual-family campaign was prepared with second-wave
style naming in multiple files and identifiers.

That naming is conceptually misaligned with the live roadmap because:

- the live backlog still reserves `Wave 2` for temporal models;
- the current residual-harmonic optimization pass is still part of the
  structured-baseline effort and therefore belongs to the `Wave 1` scope.

The mismatch was identified after the campaign had already entered the
`running` state.

## Technical Approach

Because the campaign is already active, the current baseline files must not be
modified immediately.

The correct handling is therefore:

1. leave the active campaign files unchanged while the campaign is running;
2. record this mismatch explicitly as a repository reminder;
3. after the user declares that the campaign is finished, perform a dedicated
   post-campaign alignment pass.

The post-campaign alignment pass should review and correct, where appropriate:

- live backlog status text;
- technical and planning document framing;
- launcher and campaign naming;
- campaign-state wording;
- any repository surfaces that incorrectly imply that temporal-model `Wave 2`
  work has already begun.

## Involved Components

- `doc/running/te_model_live_backlog.md`
  Live operational backlog that must be realigned after campaign completion.
- `doc/running/active_training_campaign.yaml`
  Active campaign state that currently reflects the running campaign baseline
  and should not be renamed during execution.
- `doc/technical/2026-03-26/2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md`
  Technical note whose naming and wording may need post-campaign review.
- `doc/reports/campaign_plans/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
  Planning report whose wave framing may need post-campaign review.
- `scripts/campaigns/run_wave1_residual_harmonic_family_campaign.ps1`
  Launcher whose naming may need post-campaign review.

## Implementation Steps

1. Record this reminder without modifying the active campaign baseline.
2. Wait until the user confirms that the running campaign is finished.
3. After campaign completion, inspect the final campaign state and artifact
   paths.
4. Perform the wave-naming and backlog-alignment cleanup as a dedicated
   post-campaign task.
