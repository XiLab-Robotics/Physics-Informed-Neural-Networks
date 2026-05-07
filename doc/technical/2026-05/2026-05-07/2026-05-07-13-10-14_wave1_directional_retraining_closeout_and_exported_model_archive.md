# 2026-05-07-13-10-14 Wave1 Directional Retraining Closeout And Exported Model Archive

## Overview

This document plans the formal closeout of the completed
`wave1_directional_retraining_campaign_2026_05_06_16_07_16` campaign.

The campaign has completed successfully with `15/15` runs and `0` failures
under:

- `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/`

The requested closeout scope has three parts:

1. write the final campaign-results report for the completed `Wave 1`
   directional retraining campaign;
2. update the canonical analysis surfaces so the new `global`, `Fw`, and `Bw`
   outcomes are reflected in repository-facing status summaries;
3. create a curated copy of the trained model artifacts under
   `models/exported/`, organized by family and then by `forward`,
   `backward`, and `global`, with both `onnx` and `python` export surfaces.

## Technical Approach

The closeout will treat the completed campaign artifacts and the
registry-backed family outputs as the source of truth.

The implementation will:

1. read the completed campaign bundle and build a dedicated closeout report in
   `doc/reports/campaign_results/`;
2. verify the current family-best registry state for:
   - `tree`, `tree_fw`, `tree_bw`;
   - `feedforward`, `feedforward_fw`, `feedforward_bw`;
   - `periodic_mlp`, `periodic_mlp_fw`, `periodic_mlp_bw`;
   - `harmonic_regression`, `harmonic_regression_fw`, `harmonic_regression_bw`;
   - `residual_harmonic_mlp`, `residual_harmonic_mlp_fw`,
     `residual_harmonic_mlp_bw`;
3. repair any directional-metadata drift discovered in the completed campaign
   winner surfaces before updating canonical summaries;
4. update the main Wave 1 and master-summary analysis documents so the repo
   records the directional comparison explicitly instead of only the older
   global-only picture;
5. build a curated archive under `models/exported/` that separates:
   - base family;
   - `global` / `forward` / `backward`;
   - `onnx` artifacts;
   - `python` artifacts.

The export package should remain repository-owned and inspectable. Where a
native ONNX export does not yet exist for one family, the closeout should make
that explicit and either materialize the ONNX export during closeout or record
the export failure surface cleanly inside the curated archive.

The closeout must not silently rewrite the unrelated protected
`Track 1` active-campaign state. The current
`doc/running/active_training_campaign.yaml` still points to a separate
`Track 1` campaign marked `running`. If the closeout would need to edit that
protected file, a `CRITICAL WARNING` must be surfaced first and explicit user
approval must be obtained before touching it.

## Involved Components

- `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/`
- `output/training_runs/`
- `output/registries/families/`
- `output/registries/program/`
- `doc/reports/campaign_results/`
- `doc/reports/analysis/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/exported/`
- `scripts/reports/closeout/`
- `scripts/reports/pdf/`
- `doc/running/active_training_campaign.yaml`

No subagent is planned for this scope. If subagent help becomes useful later,
the proposed agent, delegated boundary, and approval requirement must be
declared before any launch.

## Implementation Steps

1. Inspect the completed `Wave 1` directional campaign bundle and collect the
   winner, per-family directional best entries, and the artifact roots needed
   for archiving.
2. Repair directional metadata inconsistencies in the registry-facing winner
   surfaces if the completed campaign stored incorrect `training_variant`,
   `base_model_family`, or direction-scope fields.
3. Generate the final closeout report in
   `doc/reports/campaign_results/` and validate the required PDF export.
4. Update the canonical Wave 1 and training-results analysis reports so the
   repo records the new directional comparison in a durable way.
5. Build the curated `models/exported/` archive with family-first layout and
   nested `global`, `forward`, and `backward` directories, each split into
   `onnx` and `python`.
6. Provide the narrow commit commands for the closeout package without
   automatically committing.
