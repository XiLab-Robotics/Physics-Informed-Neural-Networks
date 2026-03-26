# Wave2 Familywise Hyperparameter Optimization Campaign

## Overview

The completed `Wave 1` and recovery campaign established a clear next step for
the repository:

- stop broad one-shot screening;
- move to deeper hyperparameter optimization inside the most relevant model
  families;
- keep family searches separated rather than mixing all candidate families in a
  single campaign;
- compare the resulting family champions only after each family has received a
  meaningful optimization pass.

The user explicitly requested an aggressive search posture with enough time to
test many configurations, while preserving the family-by-family structure.

This technical document defines the `Wave 2` direction as a familywise
best-training campaign program rather than one mixed cross-family queue.

## Technical Approach

The `Wave 2` program should be organized as a sequence of family-specific
campaigns, each with its own planning report, generated YAML set, launch
command, artifact root, and final results report.

The main rationale is:

1. the current repository already has family baselines good enough to justify
   targeted optimization;
2. mixing all families again too early would spend queue budget on breadth
   rather than depth;
3. family-specific searches make it easier to interpret which hyperparameters
   matter for each modeling principle;
4. the final comparison becomes stronger when each family is represented by a
   tuned champion rather than by a baseline preset.

### Program Structure

The `Wave 2` optimization program should be split into separate family tracks.

The expected initial priority is:

1. `residual_harmonic_mlp`
   Best recovered structured-neural family and strongest practical challenger to
   the current global tree leader.
2. `tree`
   Includes the current global best `hist_gradient_boosting` solution and the
   still-relevant random-forest branch.
3. `harmonic_regression`
   Lower priority for outright leaderboard position, but still important as a
   structured interpretable reference family.

Feedforward optimization has already received a deeper best-training pass, so
it should remain a historical optimized reference unless the user later asks for
another feedforward-specific revisit.

### Familywise Search Philosophy

Each family campaign should be broad enough to meaningfully test multiple
levers, not just tiny local tweaks around one preset.

The familywise search should prefer staged sweeps such as:

1. architecture capacity;
2. family-specific structural settings;
3. optimization schedule;
4. regularization;
5. data-density or training-budget adjustments when they are still relevant for
   that family.

The intention is not blind exhaustive grid search. The intention is a large but
defensible engineering search that explores the highest-value levers for each
family.

### Residual Harmonic MLP Search Scope

The residual family should receive the largest early budget.

The likely search axes are:

- harmonic order;
- frozen versus joint optimization mode;
- residual-head width and depth;
- residual activation choice if configurable;
- optimizer learning rate and weight decay;
- schedule length, patience, and early-stopping sensitivity;
- optional batch-size or data-density adjustments when they still affect
  convergence quality.

The current recovery winner
`te_residual_h12_small_joint_recovery` should be treated as the reference anchor
for this family.

### Tree Family Search Scope

The tree family should be split conceptually into at least two subtracks:

- `hist_gradient_boosting`
- `random_forest`

The goals differ:

- `hist_gradient_boosting` is already the global best and should be tuned to
  measure its practical ceiling;
- `random_forest` should be tuned with explicit awareness of workstation memory
  and runtime pressure.

The likely tree search axes are:

- estimator count;
- depth / leaf-size controls;
- learning-rate and iteration count for boosting;
- feature-bin or histogram controls when supported;
- memory-safe versus higher-capacity random-forest settings.

### Harmonic Regression Search Scope

Harmonic regression is not expected to become the top global family, but it
still deserves a proper optimization pass as the main compact structured
reference.

The likely search axes are:

- harmonic order;
- static versus conditioned variants;
- conditioning feature combinations;
- coefficient regularization strength when supported.

The search should remain broad enough to test whether a better conditioned
harmonic setup can materially improve over the current linear-conditioned Wave 1
reference.

### Comparison Strategy After Family Optimization

The program should explicitly delay the final cross-family comparison until each
selected family has a `Wave 2` champion.

That final comparison should use:

- the best tuned residual family run;
- the best tuned tree-family run;
- the best tuned harmonic family run;
- the already-optimized feedforward reference only if still needed as an
  additional comparison baseline.

This avoids comparing an optimized family champion against a mostly untuned
baseline from another family.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that should reference this technical note.
- `doc/reports/campaign_plans/`
  Destination for the family-specific preliminary planning reports that must be
  created before any new `Wave 2` training execution.
- `doc/reports/campaign_results/`
  Destination for the final family-specific results reports after each approved
  campaign completes.
- `doc/running/active_training_campaign.yaml`
  Persistent state that must track whichever family campaign is currently
  prepared or active.
- `config/training/`
  Root where future family-specific campaign YAML files will be generated.
- `output/training_campaigns/`
  Artifact root for the resulting familywise `Wave 2` campaign outputs.
- `output/registries/families/`
  Family-level leaderboard and best-run registries that must be updated after
  campaign completion.
- `output/registries/program/current_best_solution.yaml`
  Program-level reference winner that future tuned champions must challenge.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. Wait for explicit user approval before creating any campaign-planning report
   or campaign YAML set.
3. After approval, create the first `Wave 2` planning report in
   `doc/reports/campaign_plans/` for the highest-priority family campaign.
4. Define a broad but structured candidate configuration table for that family,
   including the main hyperparameter axes and the rationale for each group.
5. After planning approval, generate the family-specific campaign YAML files,
   update `doc/running/active_training_campaign.yaml`, and provide the exact
   launch command.
6. Execute one approved family campaign at a time and produce the mandatory
   family-specific results report plus validated PDF.
7. Repeat the same workflow for the remaining selected families.
8. Only after the familywise optimization passes are complete, prepare the
   final cross-family comparison of the tuned champions.
