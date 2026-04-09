# Track 1 Second Iteration Campaign Preparation

## Overview

This document proposes the preparation of a dedicated campaign package for the
second `Track 1` harmonic-wise iteration.

The current repository already has the paper-faithful harmonic-wise pipeline
implemented and the second-iteration preset structure prepared. What is still
missing is the campaign packaging needed to run that second iteration as a
coherent, operator-triggered execution batch rather than as a sequence of
manual one-off commands.

The user requested a complete and thorough campaign preparation with planning,
launcher support, and an explicit operator command.

## Technical Approach

Prepare a dedicated campaign for the second `Track 1` iteration under the
paper-reimplementation branch.

This campaign should remain separate from the standard
`scripts/training/run_training_campaign.py` workflow because the harmonic-wise
pipeline is not a normal model-family training path. It is a
repository-owned offline validation pipeline driven by:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

Therefore the campaign packaging should include:

- a planning report under `doc/reports/campaign_plans/`;
- a dedicated configuration package for the selected harmonic-wise runs;
- a dedicated PowerShell launcher under `scripts/campaigns/`;
- a matching launcher note under `doc/scripts/campaigns/`;
- a persistent campaign-state entry in `doc/running/active_training_campaign.yaml`;
- an explicit operator command to launch the campaign from the terminal.

The campaign should be broad enough to answer the second-iteration questions in
one structured batch, not only in a narrow single-config rerun.

The intended comparison blocks are:

1. current full-RCIM baseline anchor;
2. reduced harmonic-set `HistGradientBoosting` progression;
3. one reduced harmonic-set `RandomForest` diagnostic run;
4. full-RCIM promotion runs to test whether the improved predictor choices
   still hold after returning to the harmonic coverage required by the paper.

## Involved Components

- `doc/reports/campaign_plans/`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Implementation Steps

1. Create a detailed campaign planning report for a comprehensive second
   `Track 1` iteration batch.
2. Define the candidate config matrix, including reduced harmonic stages, full
   RCIM promotion runs, and one diagnostic `RandomForest` comparison.
3. Prepare a dedicated config package for the approved run set under the paper
   reimplementation configuration tree.
4. Create a dedicated PowerShell launcher that executes the harmonic-wise
   pipeline across the approved config list in operator-driven mode.
5. Create the matching launcher note and provide the exact terminal command.
6. Write the prepared campaign state into
   `doc/running/active_training_campaign.yaml`.
7. Stop after preparation and wait for the user to report launch and
   completion in the usual operator-handoff workflow.
