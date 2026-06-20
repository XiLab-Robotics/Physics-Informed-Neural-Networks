# Wave 2.1 Closeout And TE Curve Verification Pipeline Refresh Plan

## Overview

Close out the completed `Wave 2.1` temporal-model entry campaign and plan the
official `TE Curve Verification Pipeline` verification refresh for the new temporal candidates.

The campaign `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15`
completed all `9` planned runs:

- `temporal_convolution` across `global`, `Fw`, and `Bw`;
- `gru_sequence` across `global`, `Fw`, and `Bw`;
- `lstm_sequence` across `global`, `Fw`, and `Bw`.

The local campaign winner is `te_gru_sequence_remote_Fw` with test MAE
`0.0033327306155115366`. This is a training-campaign result, not yet an
accepted `TE Curve Verification Pipeline` verification result. Acceptance requires the official
direction-aware `TE Curve Verification Pipeline` matrix and visual evidence to be refreshed.

No subagent use is planned for this task.

## Technical Approach

Use two separate deliverables:

1. A `Wave 2.1` campaign closeout report under `doc/reports/campaign_results/`
   with a styled PDF companion.
2. A `TE Curve Verification Pipeline` refresh plan/report path that records how the newly trained
   temporal candidates will be added to the official model-verification
   workflow.

The closeout report should summarize:

- campaign package and execution provenance;
- all `9` candidate runs;
- campaign leaderboard and best run;
- comparison against the existing `Wave 1` and official `TE Curve Verification Pipeline` baselines;
- decision boundary between training success and official verification.

The `TE Curve Verification Pipeline` refresh plan should require:

- adding the `Wave 2.1` candidates to the direction-aware matrix;
- regenerating candidate collages for the relevant temporal winners;
- regenerating multi-model overlays against the current reference and `Wave 1`
  anchors;
- updating the official `TE Curve Verification Pipeline` model-verification report ledger;
- exporting and validating the official `TE Curve Verification Pipeline` PDF after the refreshed
  matrix and visual reports exist.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/`
- `output/training_runs/temporal_convolution*/`
- `output/training_runs/gru_sequence*/`
- `output/training_runs/lstm_sequence*/`
- `output/registries/families/temporal_convolution*/`
- `output/registries/families/gru_sequence*/`
- `output/registries/families/lstm_sequence*/`
- `output/registries/program/current_best_solution.yaml`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/wave_2/`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/`
- `doc/reports/analysis/track2/best_model_collage_report/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/`
- `scripts/reports/pdf/`
- `doc/README.md`

## Implementation Steps

1. Verify the campaign manifest, leaderboard, best-run file, and family
   registries for all `9` Wave 2.1 runs.
2. Create the Wave 2.1 closeout report under
   `doc/reports/campaign_results/wave_2/`.
3. Export the closeout report to PDF and validate the real PDF deliverable.
4. Update `Training Results Master Summary.md`, `te_model_live_backlog.md`,
   and `doc/README.md` with the closeout interpretation.
5. Create a TE Curve Verification refresh plan/report that lists the exact candidates,
   matrix rows, visual outputs, and official PDF refresh requirements.
6. Do not treat any Wave 2.1 temporal model as officially accepted until the
   refreshed `TE Curve Verification Pipeline` matrix and visual reports are generated and reviewed.
7. Run Markdown QA, PDF validation, and Sphinx validation for touched
   documentation and portal surfaces.
