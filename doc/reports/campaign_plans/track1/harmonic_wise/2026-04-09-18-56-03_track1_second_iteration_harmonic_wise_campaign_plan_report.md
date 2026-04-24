# Track 1 Second Iteration Harmonic-Wise Campaign Plan Report

## Overview

This report defines the next comprehensive campaign for the paper-faithful
harmonic-wise branch.

The repository has already implemented `Track 1` and executed its first real
offline baseline. That baseline proved the pipeline works, but it did not yet
close `Target A`.

Current reference result:

- selected harmonics:
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- validation mean percentage error: `9.474%`
- test mean percentage error: `9.403%`
- `Target A` threshold: `<= 4.7%`
- current status: `not_yet_met`

At the same time, the current oracle truncation-only result is already much
better:

- oracle test mean percentage error: `2.749%`

This campaign therefore focuses on the real bottleneck:

- improving the predictor from operating conditions to harmonic coefficients
  while preserving a paper-faithful harmonic representation.

## Why This Campaign Makes Sense

The current evidence says three things clearly:

1. the harmonic representation itself is not the main blocker;
2. the operating-condition predictor still has room to improve materially;
3. the branch must return to the full RCIM harmonic set before `Track 1` can
   be considered complete.

That means the campaign must not choose between:

- reduced harmonic debugging runs;
- and full-RCIM paper-faithful runs.

It needs both.

The reduced harmonic stages are useful because they isolate the most important
terms:

- `0`
- `1`
- `39`
- later `40`
- later `78`

But the final comparison for `Track 1` still needs at least the paper harmonic
set:

- `0`
- `1`
- `3`
- `39`
- `40`
- `78`
- `81`
- `156`
- `162`
- `240`

## Technical Context

This campaign is not a standard model-family training campaign executed through
`scripts/training/run_training_campaign.py`.

Instead, it is a repository-owned validation campaign built around:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

Each run:

1. loads one harmonic-wise YAML preset;
2. builds the harmonic decomposition targets;
3. fits one estimator per harmonic target;
4. reconstructs TE curves;
5. evaluates held-out validation and test splits;
6. runs offline `Robot` and `Cycloidal` playback probes;
7. writes a validation summary and a Markdown report.

The campaign launcher should therefore orchestrate multiple harmonic-wise
validation runs, not queue them through the standard training-run dispatcher.

## Technical Approach

The campaign should contain eight runs.

### Block 1 - Full-RCIM Reference Anchor

This block establishes the baseline reference inside the campaign package.

It should include:

1. the existing full-RCIM baseline configuration;
2. one full-RCIM engineered-feature configuration using the improved predictor
   defaults;
3. one deeper full-RCIM engineered-feature configuration to test whether the
   promotion back to the paper harmonic set still benefits from more predictor
   capacity.

### Block 2 - Reduced Harmonic Progression

This block isolates the dominant harmonic groups.

It should include:

1. one `0,1,39` run;
2. one `0,1,39,40` run;
3. one `0,1,39,40,78` run.

These runs should all use engineered operating-condition features.

### Block 3 - Diagnostic Non-Promotion Check

This block should include:

1. one `0,1,39` `RandomForest` diagnostic run.

Its purpose is not deployment promotion.

Its purpose is to answer whether the second iteration is winning because of:

- better harmonic staging and features;
- or only because of the current histogram-boosting default.

### Block 4 - Full-RCIM Feature-Isolation Check

This block should include:

1. one full-RCIM run with the improved tree schedule but without engineered
   features.

Its purpose is to isolate the value of engineered operating-condition features
once the harmonic coverage returns to the full paper set.

## Candidate Exploratory Matrix

| Config ID | Config Role | Planned Name | Harmonics | Main Parameters | Main Question |
| --- | --- | --- | --- | --- | --- |
| 1 | Full-RCIM baseline anchor | `full_rcim_baseline_reference` | `0,1,3,39,40,78,81,156,162,240` | current baseline `HistGradientBoosting` schedule | Can the campaign reproduce the current reference result cleanly under the prepared campaign workflow? |
| 2 | Reduced-stage HGB | `h013_engineered_stage1` | `0,1,39` | engineered features, `HistGradientBoosting`, higher iter/depth | Does the predictor improve materially when it focuses first on the most important deployed harmonics? |
| 3 | Reduced-stage RF diagnostic | `h013_random_forest_diagnostic` | `0,1,39` | engineered features, bounded `RandomForest` | Is the gain primarily due to the new staged problem setup rather than only the chosen boosting estimator? |
| 4 | Reduced-stage HGB | `h01340_engineered_stage2` | `0,1,39,40` | engineered features, `HistGradientBoosting`, higher iter/depth | Does adding harmonic `40` preserve the gain from the smaller stage or immediately erode it? |
| 5 | Reduced-stage HGB | `h0134078_engineered_stage3` | `0,1,39,40,78` | engineered features, `HistGradientBoosting`, higher iter/depth | Does the predictor stay strong after adding the next practically important harmonic group? |
| 6 | Full-RCIM feature-isolation | `full_rcim_no_engineering_reference` | `0,1,3,39,40,78,81,156,162,240` | refined `HistGradientBoosting`, no engineered features | How much of the full-RCIM gain comes from predictor tuning alone before adding feature engineering? |
| 7 | Full-RCIM promoted HGB | `full_rcim_engineered_balanced` | `0,1,3,39,40,78,81,156,162,240` | engineered features, refined `HistGradientBoosting` | Does the best improved predictor still hold after returning to the full paper harmonic set? |
| 8 | Full-RCIM promoted HGB | `full_rcim_engineered_deeper` | `0,1,3,39,40,78,81,156,162,240` | engineered features, deeper / longer `HistGradientBoosting` | Is there still a meaningful gain left in a more aggressive full-RCIM promotion run? |

## Parameter Notes

### Harmonic Progression Logic

- `0,1,39` is the cleanest reduced paper-deployment anchor.
- `0,1,39,40` tests whether the next deployed harmonic can be absorbed without
  collapsing the gain.
- `0,1,39,40,78` is the final reduced stage before promotion back to the full
  RCIM set.
- the full-RCIM runs remain mandatory because the branch must stay faithful to
  the paper structure rather than ending on a reduced harmonic subset.

### Feature Engineering

The campaign should test derived operating-condition features:

- `speed * torque`
- `speed * temperature`
- `torque * temperature`
- `speed^2`
- `torque^2`

Expected effect:

- give the harmonic predictor a stronger tabular basis without changing the
  paper-faithful output representation.

### Predictor Refinement

The main promoted estimator should remain `HistGradientBoosting`.

The campaign should vary:

- `learning_rate`
- `max_iter`
- `max_depth`
- `min_samples_leaf`
- and, where justified, per-harmonic override capacity for the most important
  terms.

The `RandomForest` run is diagnostic only.

Expected effect:

- establish whether the staged problem setup and engineered features matter on
  their own, even before looking at final deployment preferences.

## Evaluation Rules

The campaign should keep the paper-facing `Track 1` success criteria explicit:

- primary paper metric:
  `test mean percentage error`
- paper threshold for `Target A`:
  `<= 4.7%`

It should also interpret:

- validation mean percentage error;
- oracle mean percentage error;
- curve `MAE`;
- curve `RMSE`;
- per-target harmonic error;
- per-harmonic ranking of dominant error contributors.

The campaign winner should not be selected only from reduced harmonic sets.

Promotion logic should remain:

1. identify the strongest reduced-stage pattern;
2. verify whether it still improves after promotion to the full RCIM set;
3. prefer the best full-RCIM result over a reduced-stage win if the branch is
   to be used as the main `Track 1` comparison anchor.

## Step-By-Step Operational Guide To Prepare

The implementation phase should provide an explicit operator guide that covers:

### Local Workstation

1. confirm the approved harmonic-wise campaign YAML package exists;
2. confirm the dedicated launcher exists and points to the intended config set;
3. launch the campaign with the exact PowerShell command from the repository
   root;
4. watch the per-run validation artifact directories under:
   - `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/`
5. review the generated validation reports under:
   - `doc/reports/analysis/validation_checks/`

### Optional Stronger Workstation / Remote Use

If the user wants the campaign to run on the stronger LAN node instead of the
local workstation, the launcher implementation should keep that path explicit
and operator-driven rather than hidden.

The final preparation step should therefore state clearly whether the approved
launcher executes:

- fully local validation runs;
- or a LAN-remote mirrored invocation path.

## Execution Gate

Before this campaign is launched:

1. the technical document must be approved;
2. this planning report must be approved;
3. the dedicated config package must be generated;
4. the dedicated launcher and launcher note must be generated;
5. the active campaign state must be written to
   `doc/running/active_training_campaign.yaml`;
6. the exact launch command must be provided;
7. the user must explicitly launch the prepared campaign in operator-driven
   mode.

## Next Step

If this planning report is approved, generate the dedicated second-iteration
harmonic-wise campaign package, create the launcher and launcher note, update
the active campaign state, and provide the exact operator command.
