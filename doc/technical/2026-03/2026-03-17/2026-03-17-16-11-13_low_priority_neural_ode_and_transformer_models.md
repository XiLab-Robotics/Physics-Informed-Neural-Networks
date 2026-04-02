# Low-Priority Neural ODE And Transformer Models

## Overview

This document records the decision to keep `Neural ODE` models and `Lightweight Transformer` models inside the project scope as explicit low-priority exploratory options.

The previous TE model roadmap and implementation backlog did not promote these families into the main execution waves because their current cost-to-value ratio is weaker than:

- structured static baselines;
- temporal models such as lagged-feature MLP, `GRU`, `LSTM`, and `TCN`;
- hybrid structured families such as Fourier-feature, harmonic-head, and smoothness-regularized networks.

The user requested that these two families remain visible in the repository planning rather than being only implicit or conceptually deferred.

This document therefore clarifies:

- why they were not included in the primary backlog waves;
- why they should still remain in scope;
- under which conditions they should enter implementation.

## Technical Approach

### Why Lightweight Transformers Were Not Promoted Earlier

For the current TE case study, `Lightweight Transformer` models were treated as lower-priority than `TCN`, `GRU`, and `LSTM` because:

- the expected useful context length is not yet proven to be long enough to justify attention-based sequence modeling;
- the TE signal has strong periodic and harmonic structure, which is often better addressed first with explicit spectral or structured inductive bias rather than attention alone;
- deployment and runtime transparency are currently better served by simpler sequence families;
- the implementation and tuning cost is higher than the likely short-term value.

This is a prioritization argument, not a rejection of the family.

### Why Neural ODE Models Were Not Promoted Earlier

`Neural ODE` models were treated as lower-priority because the current repository does not yet have a sufficiently fixed continuous-state formulation for the TE problem.

The unresolved questions include:

- whether the natural independent variable should be angle, time, or a mixed time-angle formulation;
- which latent state should evolve continuously;
- whether the desired benefit is dynamic-history modeling, continuous-angle smoothness, or a bridge toward physics-informed residuals;
- how such a model would remain tractable for later deployment.

Without those choices, a `Neural ODE` implementation would be premature and likely less defensible than the more direct temporal or hybrid families already in the backlog.

### Why Both Families Should Still Remain In Scope

Even though they are not first-wave candidates, both families can still become relevant later:

#### Lightweight Transformer Potential

- useful if later evidence shows that TE depends on broader sequence context than `TCN`, `GRU`, or `LSTM` can capture efficiently;
- useful if the sequence representation expands to richer multi-signal windows;
- useful if cross-condition interactions become more important than local periodic structure alone.

#### Neural ODE Potential

- useful if the project evolves toward continuous-state modeling over angle or time;
- useful as a bridge between temporal sequence models and more physics-structured differential formulations;
- useful if the final PINN direction benefits from a learned continuous latent dynamics layer.

### Decision

The repository should keep both families as explicit exploratory branches with `low priority` status.

They should not enter the main implementation program until at least one of the following conditions is met:

1. the best current structured, temporal, and hybrid families have already been implemented and compared;
2. there is concrete evidence that the current families miss longer-range or continuous-state behavior;
3. a clearer deployment or scientific justification emerges for one of these approaches;
4. the user explicitly promotes one of these families into an earlier campaign wave.

### Planned Backlog Placement

The implementation backlog should therefore expose:

- a `Lightweight Transformer` exploratory family after the main temporal models;
- a `Neural ODE / Continuous-State Hybrid` exploratory family after the main hybrid models and before or alongside advanced PINN exploration, depending on the final formulation.

This placement preserves visibility without distorting the main execution order.

## Involved Components

- `README.md`
  Main project document that must reference this note.
- `doc/README.md`
  Internal documentation index that should also list this note.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  Original roadmap where these families were discussed only as lower-priority directions.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  Backlog document that should later be updated so both families appear explicitly as low-priority exploratory branches.
- `doc/reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md`
  Analytical comparison report that should later mention both families more explicitly in the comparative planning.
- `doc/technical/2026-03/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md`
  This technical note.

## Implementation Steps

1. Create this technical note and register it in the documentation indexes.
2. Wait for explicit user approval before modifying the existing roadmap, backlog, or analytical comparison report.
3. After approval, update the roadmap so `Lightweight Transformer` and `Neural ODE` appear explicitly as low-priority exploratory families.
4. Update the implementation backlog so both families have visible deferred backlog entries and later-entry conditions.
5. Update the analytical comparison report so both families are represented in the qualitative comparison matrix as low-priority options.
6. Keep them outside the primary implementation waves unless a later approval explicitly promotes them.
