# Wave 1 Structured Baseline Campaign Plan Report

## Overview

This report defines the first planned campaign of `Wave 1` for the TE model program.

The campaign is not a rerun of the already completed feedforward family. Its purpose is broader:

1. establish the first cross-family comparison beyond the original point-wise feedforward baseline;
2. test whether explicit periodic or structured bias improves TE prediction;
3. verify whether the next useful baselines are still neural, partly analytical, or purely tabular;
4. decide which structured family deserves a refined follow-up campaign.

The current comparison anchor is the already formalized feedforward reference baseline:

- Run: `te_feedforward_stride5_long_large_batch`
- Registry Id: `legacy__te_feedforward_stride5_long_large_batch`
- Validation MAE: `0.0031092546`
- Validation RMSE: `0.0036387309`
- Test MAE: `0.0033006170`
- Test RMSE: `0.0037907639`

Reference artifacts:

- `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/metrics_summary.yaml`
- `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/training_test_report.md`
- `output/registries/families/feedforward/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`

No new run is assumed completed yet. This is a planning document only.

## Why This Wave Makes Sense

The repository now has:

- a stable shared training infrastructure;
- canonical artifact naming and registries;
- a formalized feedforward comparison baseline;
- an approved roadmap that prioritizes structured baselines before temporal and physics-informed models.

The next technically disciplined move is therefore not:

- sequence models;
- Neural ODEs;
- PINNs.

It is:

- testing stronger structured inductive bias at low-to-moderate implementation cost.

This is where the project can most plausibly gain:

- interpretability;
- deployment simplicity;
- better sample efficiency;
- better periodic TE reconstruction quality.

## Wave 1 Families And Their Roles

### 1. Harmonic Regression Baseline

Role:

- strongest interpretability baseline;
- explicit periodic decomposition;
- closest model to classical TE harmonic reasoning.

Main hypothesis:

- a moderate-order harmonic model may explain a large part of TE with much stronger structure than a raw MLP.

Main risk:

- pure harmonic structure may underfit operating-condition interaction unless the coefficient model is made condition-aware.

### 2. Periodic-Feature Feedforward MLP

Role:

- keep the successful feedforward workflow;
- inject periodic inductive bias with minimal architecture risk.

Main hypothesis:

- replacing raw angle-only treatment with explicit `sin/cos` harmonic encoding can improve TE reconstruction without paying the complexity cost of recurrent or physics-informed models.

Main risk:

- too shallow an encoding may add little benefit;
- too deep an encoding may expand the feature space without real gain.

### 3. Residual MLP Over Harmonic Baseline

Role:

- decompose TE into:
  - structured periodic component;
  - learned residual correction.

Main hypothesis:

- part of the current feedforward gain may come from modeling the residual left by a simpler structured approximation rather than learning the whole TE map from scratch.

Main risk:

- if the structured baseline is weak, the residual branch just recreates a full MLP with extra overhead.

### 4. Tree-Based Benchmark

Role:

- non-neural tabular benchmark;
- reality check on whether neural models are actually justified.

Main hypothesis:

- tree ensembles can become competitive on static numeric features and should be measured before assuming a neural model is necessary.

Main risk:

- weaker periodic extrapolation and weaker deployment fit than the structured neural alternatives.

## Main Parameters To Control

The first Wave 1 campaign should stay exploratory, so the parameter count must remain controlled.

### Harmonic Regression Parameters

- harmonic order
- coefficient parameterization
- regularization strength

Expected effect:

- higher order increases expressive periodic detail but also increases overfitting risk and coefficient instability.

### Periodic-Feature MLP Parameters

- number of harmonic encodings
- hidden-layer width and depth
- dropout

Expected effect:

- more periodic encodings increase representational richness;
- wider models test whether periodic features need additional capacity to exploit the bias.

Important practical note:

- MLP-style models remain sensitive to feature scaling, so the training path must keep using the same consistent normalization workflow across train, validation, and test splits.

### Residual Structured-Neural Parameters

- harmonic order of the structured branch
- residual hidden width/depth
- structured branch frozen vs jointly trainable

Expected effect:

- frozen structured branch isolates the residual-learning hypothesis;
- joint tuning tests whether the structured and residual components should co-adapt.

### Tree-Based Benchmark Parameters

- estimator family
- tree depth / leaf size / number of estimators for forest models
- learning rate / max depth / iteration count for histogram boosting

Expected effect:

- `RandomForestRegressor` is a robust non-neural baseline for static numeric features;
- `HistGradientBoostingRegressor` is especially worth testing because the histogram-based implementation is intended to be faster and more scalable on larger tabular datasets than classical gradient boosting;
- preprocessing parity should still be enforced through a `Pipeline` whenever a transform is required, to avoid inconsistent train/test feature handling.

## Implementation Gate Before Campaign Execution

No Wave 1 family should enter campaign execution before these checks pass:

1. successful instantiation from YAML config;
2. one-batch forward pass;
3. finite loss and finite metrics;
4. correct feature dimensionality;
5. correct save/reload behavior where checkpointing applies;
6. correct path integration with the shared output layout;
7. comparable `metrics_summary.yaml` output for campaign reporting.

This gate is mandatory because otherwise the first campaign becomes a debugging session instead of a model-comparison step.

## Candidate Exploratory Matrix

The recommended first campaign is a compact 10-config exploratory matrix.

It is intentionally not exhaustive. The point is to identify which families deserve refined follow-up campaigns.

| Config ID | Family | Candidate Name | Main Parameters | Main Question |
| --- | --- | --- | --- | --- |
| 1 | Harmonic Regression | `harmonic_order06_static` | order `6`, global coefficients, light L2 regularization | How much TE can a very simple harmonic basis explain on its own? |
| 2 | Harmonic Regression | `harmonic_order12_static` | order `12`, global coefficients, light L2 regularization | Does a deeper harmonic dictionary materially improve the static structured baseline? |
| 3 | Harmonic Regression | `harmonic_order12_linear_conditioned` | order `12`, coefficients linearly conditioned on speed/torque/temperature/direction | Is mild condition-awareness enough to keep the harmonic family competitive? |
| 4 | Periodic-Feature MLP | `periodic_mlp_h04_standard` | harmonic encoding depth `4`, hidden `128-128-64`, dropout `0.1` | Does low-depth periodic encoding already beat the raw-angle feedforward baseline? |
| 5 | Periodic-Feature MLP | `periodic_mlp_h08_standard` | harmonic encoding depth `8`, hidden `128-128-64`, dropout `0.1` | Does a richer periodic expansion unlock better TE detail reconstruction? |
| 6 | Periodic-Feature MLP | `periodic_mlp_h08_wide` | harmonic encoding depth `8`, hidden `256-128-64`, dropout `0.1` | If encoding helps, does extra capacity help exploit it further? |
| 7 | Residual Harmonic + MLP | `residual_h12_small_frozen` | harmonic order `12`, residual `64-64`, structured branch frozen | Is residual learning over a fixed harmonic baseline already stronger than direct prediction? |
| 8 | Residual Harmonic + MLP | `residual_h12_small_joint` | harmonic order `12`, residual `64-64`, joint optimization | Does joint adaptation outperform a fixed-structure-plus-residual decomposition? |
| 9 | Tree Benchmark | `random_forest_tabular` | `RandomForestRegressor`, medium forest size, moderate leaf regularization | Is a robust tree ensemble already competitive enough to justify keeping non-neural baselines in scope? |
| 10 | Tree Benchmark | `hist_gbr_tabular` | `HistGradientBoostingRegressor`, moderate depth, moderate iterations, conservative learning rate | Does histogram boosting become the strongest non-neural benchmark on the static TE features? |

## Recommended Default Hyperparameter Bands

These ranges should guide the first implementation presets.

### Harmonic Regression

- harmonic order: `6`, `12`, `18`
- coefficient regularization: `1e-6`, `1e-5`, `1e-4`

### Periodic-Feature MLP

- harmonic depth: `4`, `8`, `12`
- hidden size families:
  - `128-128-64`
  - `256-128-64`
- dropout: `0.0`, `0.1`

### Residual Harmonic + MLP

- harmonic order: `12`
- residual widths:
  - `64-64`
  - `128-64`
- training mode:
  - frozen structured branch
  - joint optimization

### Tree Benchmarks

- random forest:
  - `n_estimators`: `300` to `800`
  - `max_depth`: `None` or moderate bounded depth
  - `min_samples_leaf`: `1`, `3`, `5`
- histogram boosting:
  - `max_depth`: moderate
  - `learning_rate`: conservative
  - `max_iter`: medium to high

These are planning bands, not yet approved execution values.

## Evaluation Rules

The campaign should compare each family against the current feedforward reference baseline using:

- validation MAE
- validation RMSE
- test MAE
- test RMSE
- model complexity / trainable parameter count where meaningful
- interpretability notes
- deployment viability notes

Additional qualitative questions:

1. Does the model express periodicity in a way that is easier to inspect than the current feedforward baseline?
2. Does the model appear TwinCAT/PLC-friendlier than a generic dense neural network?
3. Does the gain, if any, justify the added implementation and tuning cost?

## Promotion Rules After The Exploratory Campaign

### Promote Immediately

- if a family clearly beats the feedforward reference baseline on test MAE without unacceptable deployment or complexity penalties.

### Keep For Refined Campaign

- if a family does not win immediately but shows:
  - strong interpretability;
  - clear validation promise;
  - evidence that a small hyperparameter refinement is justified.

### Defer Or Stop

- if a family is clearly worse than the feedforward reference baseline and offers no interpretability or deployment upside.

## Recommended Execution Order After Approval

The recommended order is:

1. implement harmonic regression
2. implement periodic-feature MLP
3. implement residual harmonic + MLP
4. implement tree benchmark
5. run family-specific smoke-test and validation checks
6. execute the exploratory campaign

This order is deliberate:

- harmonic regression is the cleanest structured baseline;
- periodic-feature MLP is the lowest-risk upgrade of the existing neural path;
- residual harmonic + MLP depends conceptually on the harmonic branch;
- the tree benchmark can be added once the canonical static feature matrix path is clean.

## Immediate Recommendation

This campaign plan is strong enough to approve as the next step.

My recommendation is:

- approve the Wave 1 preparation package;
- then implement the four structured-baseline families plus their validation/smoke-test support;
- then generate the campaign YAML files for the exploratory matrix defined here.

That keeps the project aligned with the roadmap while using the already formalized best feedforward run as a stable comparison anchor.
