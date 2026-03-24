# Wave 1 Structured Baseline Recovery Campaign Plan Report

## Overview

The first `Wave 1` structured-baseline campaign is complete, but it exposed two implementation defects that must be corrected before any new comparison campaign can be trusted:

1. the shared training summary assumed every neural model exposed `hidden_size`, which broke the harmonic and residual families immediately;
2. the `RandomForestRegressor` branch was too memory aggressive for the current workstation and failed during fit.

The periodic-feature MLP family and the histogram-gradient-boosting tree benchmark completed successfully in the first sweep. The recovery campaign defined here is therefore not a broad rerun of all families. It is a focused rerun of the families that failed so the project can regain a clean comparison baseline after the code fixes.

This recovery campaign has two goals:

1. prove that the shared training path now handles each model family with the correct configuration schema;
2. determine whether the conservative tree configuration can complete successfully on the current workstation before a higher-memory retry is scheduled separately.

Reference artifacts from the first campaign:

- `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/campaign_execution_report.md`
- `output/training_campaigns/2026-03-20-14-18-30_wave1_structured_baseline_campaign_2026_03_17_21_01_47/campaign_manifest.yaml`
- `output/registries/program/current_best_solution.yaml`

## Technical Context

The failure pattern is now understood:

- harmonic regression and residual harmonic MLP were routed through the feedforward summary block, which tried to print `hidden_size` and raised a `KeyError`;
- the random forest training path reached fit time but failed with a `MemoryError` during tree growth;
- the successful periodic-feature runs confirm that the shared infrastructure itself is usable, but not yet uniformly schema-aware across all model families.

The code fixes already applied before this planning report address the model-summary bug and make the random forest branch more conservative by clamping non-positive `n_jobs` to a single process.

## Technical Approach

The recovery campaign will stay small and deterministic.

1. Re-run the three harmonic regression configurations that failed in the first campaign.
2. Re-run the two residual harmonic configurations that failed in the first campaign.
3. Re-run the random forest benchmark with conservative memory behavior so the current workstation can be validated first.
4. Keep the run names distinct from the first campaign by appending a recovery suffix.
5. Preserve the same dataset, split logic, and evaluation metrics so the result is directly comparable with the first campaign.

The campaign is intentionally not expanding to additional periodic-feature or histogram-gradient-boosting variants, because those families already completed successfully and do not need recovery work.

## Involved Components

- `scripts/training/train_feedforward_network.py`
- `scripts/training/tree_regression_support.py`
- `scripts/training/run_training_campaign.py`
- `scripts/models/model_factory.py`
- `scripts/models/harmonic_regression.py`
- `scripts/models/residual_harmonic_network.py`
- `doc/running/te_model_live_backlog.md`
- `doc/running/active_training_campaign.yaml`
- `doc/guide/project_usage_guide.md`

## Candidate Exploratory Matrix

| Config ID | Family | Candidate Name | Main Parameters | Main Question |
| --- | --- | --- | --- | --- |
| 1 | Harmonic Regression | `harmonic_order06_static_recovery` | order `6`, global coefficients, light L2 regularization | Does the model now run end-to-end once the summary printer is model-aware? |
| 2 | Harmonic Regression | `harmonic_order12_static_recovery` | order `12`, global coefficients, light L2 regularization | Does the higher-order static harmonic baseline remain numerically stable after the fix? |
| 3 | Harmonic Regression | `harmonic_order12_linear_conditioned_recovery` | order `12`, coefficients linearly conditioned on speed/torque/temperature/direction | Does the conditioned harmonic variant now execute without schema mismatch? |
| 4 | Residual Harmonic + MLP | `residual_h12_small_frozen_recovery` | harmonic order `12`, residual `64-64`, structured branch frozen | Does the frozen residual decomposition train successfully with the corrected training summary? |
| 5 | Residual Harmonic + MLP | `residual_h12_small_joint_recovery` | harmonic order `12`, residual `64-64`, joint optimization | Does the jointly trained residual decomposition now complete cleanly? |
| 6 | Tree Benchmark | `random_forest_tabular_conservative` | `RandomForestRegressor`, reduced estimator count, bounded depth, conservative leaf size, single-process fit | Can the random forest complete on the current workstation when memory pressure is reduced? |

## Parameter Notes

### Harmonic Regression

- `harmonic_order` controls periodic detail.
- `coefficient_mode` controls whether coefficients remain static or are linearly conditioned on operating variables.
- The recovery run keeps the same structural idea as the failed campaign, because the failure was in the shared execution path rather than the harmonic design itself.

### Residual Harmonic + MLP

- `harmonic_order` defines the structured branch.
- `residual_hidden_size` controls the learned correction capacity.
- `freeze_structured_branch` distinguishes a fixed structured baseline from joint adaptation.
- The recovery campaign keeps the same widths as the first sweep so the comparison stays anchored to the original design intent.

### Random Forest

- `n_estimators` is reduced to lower memory demand.
- `max_depth` is bounded to avoid excessive tree growth on the current machine.
- `min_samples_leaf` is increased to keep leaves less fragmented.
- `n_jobs` is set to `1` so the fit is single-process and more predictable on this workstation.

## Evaluation Rules

The recovery campaign should be judged by:

- successful end-to-end completion of the harmonic and residual runs;
- absence of the `hidden_size` `KeyError`;
- successful completion or clearly bounded failure of the random forest run on the current workstation;
- validation MAE and RMSE;
- test MAE and RMSE;
- parameter count where meaningful;
- notes about whether the tree result is still sensitive to workstation memory.

## Execution Gate

Before the campaign is launched:

1. the new YAML configs must be created;
2. the corrected training code must be in place;
3. the campaign state must be written to `doc/running/active_training_campaign.yaml`;
4. the exact launch command must be provided;
5. the user must explicitly approve the campaign plan.

## Next Step

If this plan is approved, generate the campaign YAML files and launch the recovery campaign. After the campaign completes, prepare the mandatory results report and isolate the random forest family for the separate higher-memory validation step.
