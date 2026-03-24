# Wave 1 Campaign Failure Fix And Dispatch

## Overview

The first `Wave 1` structured-baseline campaign completed with a mixed outcome:

- the periodic-feature MLP runs completed successfully;
- the harmonic regression runs failed immediately with a `hidden_size` key lookup error;
- the residual harmonic MLP runs failed for the same reason;
- the random forest run failed during tree fitting with a memory allocation error;
- the histogram-gradient-boosting run completed successfully.

This document defines the correction pass needed before preparing a new campaign. The goal is to restore the missing model-aware handling in the shared training path and to make the tree benchmark less memory fragile on the current Windows environment.

## Technical Approach

The fix will stay narrow and focused on the current campaign infrastructure.

1. Make the training configuration summary model-aware instead of assuming every model exposes a `hidden_size` list.
2. Preserve the current shared training entry point for the neural and structured neural families, but print the correct parameter block for each model type.
3. Reduce the random forest memory pressure by making its runtime parallelism more conservative when running in this repository environment.
4. Keep the campaign artifact structure intact so that the next campaign can reuse the same run registry and output conventions.
5. Preserve a follow-up validation step on a higher-memory machine so the random forest failure can be checked against a larger RAM budget and compared with the current workstation result.

## Involved Components

- `scripts/training/train_feedforward_network.py`
- `scripts/training/run_training_campaign.py`
- `scripts/training/tree_regression_support.py`
- `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/*.yaml`
- `doc/guide/project_usage_guide.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Replace the feedforward-only model summary block with a model-aware configuration printer.
2. Add explicit handling for:
   - feedforward and periodic MLP hidden-layer stacks;
   - harmonic regression harmonic order and coefficient mode;
   - residual harmonic residual widths and freeze mode;
   - tree-model hyperparameters.
3. Make random forest fitting conservative enough to avoid the observed Windows memory allocation failure.
4. Re-run the failed wave 1 entries locally to confirm that the harmonic, residual, and random forest failures are resolved.
5. Update the project usage guide with the corrected campaign workflow before any final commit.
6. Prepare the next exploratory campaign only after the corrected runs are green.
7. Schedule a higher-memory machine retry for the random forest family to determine whether the observed failure is workstation-specific and whether additional memory improves the benchmark outcome.
