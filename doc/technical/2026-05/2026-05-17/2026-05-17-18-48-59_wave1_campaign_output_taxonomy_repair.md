# Wave 1 Campaign Output Taxonomy Repair

## Overview

Two completed `Wave 1` campaign output bundles are still stored directly under
`output/training_campaigns/` instead of the domain-first
`output/training_campaigns/wave1/` taxonomy:

- `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- `output/training_campaigns/2026-05-11-20-07-44_wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_1`

The likely cause is historical execution before or outside the finalized
campaign-output taxonomy. The bundle manifests still record flat-root
`campaign_output_directory` and `log_path` values, so the repair must update
both the physical directory layout and the campaign-local metadata.

## Technical Approach

Move the completed bundles into the existing `Wave 1` taxonomy without changing
their immutable campaign folder names. Use topic folders under
`output/training_campaigns/wave1/` so the resulting layout remains readable and
consistent with the existing `directional_best_hyperparameter_search` folder:

- `output/training_campaigns/wave1/directional_retraining/<campaign_bundle>`
- `output/training_campaigns/wave1/directional_best_hyperparameter_search/<campaign_bundle>`

After the move, update campaign-local metadata that contains the old flat
paths, especially `campaign_manifest.yaml`, `campaign_execution_report.md`,
`campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
`campaign_best_run.md` when they contain path references. Search repository
documentation and campaign state for references to the old flat paths and
update only the references that are part of canonical repo bookkeeping.

No subagent use is planned for this repair. If a subagent becomes necessary,
the task boundary and approval requirement must be documented here before use.

## Involved Components

- `output/training_campaigns/`
- `output/training_campaigns/wave1/`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/wave1/`
- Campaign-local metadata files inside the two moved output bundles
- Canonical documentation references discovered by targeted search

## Implementation Steps

1. Verify the active campaign state and confirm the two target bundles are not
   listed as protected campaign files.
2. Create the missing `output/training_campaigns/wave1/directional_retraining/`
   topic folder.
3. Move the two completed campaign bundles into their `Wave 1` topic folders.
4. Replace old flat-root path references inside the moved bundle metadata with
   the new taxonomy paths.
5. Run a targeted repository search for both old bundle paths and update
   canonical references that should follow the moved artifacts.
6. Validate that no old flat-root references remain except, if needed,
   intentionally historical prose.
7. Run Markdown QA on touched Git-tracked Markdown files.
