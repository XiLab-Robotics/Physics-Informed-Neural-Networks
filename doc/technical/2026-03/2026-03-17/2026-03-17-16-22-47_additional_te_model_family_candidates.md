# Additional TE Model Family Candidates

## Overview

This document records a follow-up review of the TE model roadmap and implementation backlog after the first planning pass was already approved.

The review goal was to answer a narrow question:

- are there still relevant algorithm or neural-network families missing from the planning set?

The conclusion is that the current roadmap already covers the main architecture space needed to start implementation, but three additions are worth making explicit:

- `State-Space Sequence Model` as a distinct low-priority temporal exploratory family;
- `Mixture-of-Experts / Regime-Conditioned Model` as a meaningful added family for operating-regime specialization;
- `Kernel Ridge / Gaussian Process` as an optional non-neural benchmark family.

These additions do not invalidate the current priorities. They refine the planning completeness and remove a few remaining blind spots.

## Technical Approach

### Main Conclusion Of The Review

The current planning is already strong enough to start implementation.

It already includes:

- structured static baselines;
- temporal baselines;
- hybrid spectral and smoothness-constrained models;
- low-priority advanced temporal and continuous-state options;
- a deferred PINN track with explicit formulation requirements.

So the question is not whether the roadmap is missing an entire critical direction. It is mostly whether some narrower families should be made explicit for completeness and for later comparison.

### 1. State-Space Sequence Model

This family should be represented explicitly rather than being mentioned only indirectly inside the current `Lightweight Transformer or State-Space Sequence Model` grouping.

Why it matters:

- it is conceptually different from a lightweight transformer;
- it can be a better fit than attention when sequence windows become longer or when compact recurrent-like dynamics are preferred;
- it sits naturally between `TCN` and transformer-style sequence modeling.

Why it should still remain low priority:

- the main temporal families (`lagged-feature`, `GRU`, `LSTM`, `TCN`) should still be tested first;
- the TE problem has not yet shown that broader sequence modeling is needed enough to justify this family.

Decision:

- add it explicitly as a low-priority exploratory temporal family.

### 2. Mixture-of-Experts / Regime-Conditioned Model

This is the most useful truly new addition to the roadmap.

Why it matters:

- TE behavior can change across operating regimes defined by speed, torque, temperature, and direction;
- a single global predictor may average across regimes that are better modeled by partially specialized experts;
- this idea is compatible with multiple backbone types:
  - MLP;
  - harmonic-head;
  - residual architectures.

Potential value:

- improved generalization across heterogeneous operating conditions;
- more interpretable regime specialization if the gating remains simple;
- possible improvement without fully jumping to a large complex architecture.

Main risk:

- unnecessary complexity if the regimes are already smooth enough for a single model;
- unstable or uninterpretable gating if the mixture is made too flexible.

Decision:

- add it as a medium-priority structured/hybrid family after the core structured baselines.

### 3. Kernel Ridge / Gaussian Process Benchmark

This family is not a main implementation target, but it is worth keeping as an optional benchmark.

Why it matters:

- stronger non-neural reference than trees for smooth structured regression;
- potentially useful sample-efficiency benchmark;
- Gaussian-process style models can expose uncertainty information if later needed.

Why it should stay optional:

- scaling is worse than the core model families;
- deployment fit is weaker;
- unlikely to become the final project solution.

Decision:

- add it as a low-priority benchmark branch, not as a primary model family.

### What Still Should Not Be Added Now

The review does not justify adding broader families such as:

- large transformers;
- generic graph neural networks;
- diffusion-style models;
- large autoencoder-based latent generators;
- heavy curve-to-curve convolutional encoders without a specific physical reason.

These would expand the search space without a sufficiently strong link to the current TE problem structure.

### Net Effect On The Roadmap

After this review, the roadmap should be interpreted as:

- complete enough to begin implementation;
- slightly refined by adding one more explicit temporal exploratory branch;
- strengthened by adding one realistic regime-specialized family;
- broadened by one optional non-neural smooth-regression benchmark.

The main priority order should remain unchanged.

## Involved Components

- `README.md`
  Main project document that must reference this note.
- `doc/README.md`
  Internal documentation index that should also list this note.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  Roadmap document that should later be updated with these added families.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  Backlog document that should later expose the additional families operationally.
- `doc/reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md`
  Analytical report that should later mention the added families explicitly.
- `doc/technical/2026-03/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md`
  This technical note.

## Implementation Steps

1. Create this technical note and register it in the documentation indexes.
2. After approval, update the TE roadmap to include:
   - `State-Space Sequence Model`;
   - `Mixture-of-Experts / Regime-Conditioned Model`;
   - optional `Kernel Ridge / Gaussian Process` benchmark.
3. Update the implementation backlog so all three appear with explicit priority and entry conditions.
4. Update the analytical comparison report so the new families are represented in the qualitative comparison matrix.
5. Keep the primary execution order unchanged unless later evidence promotes one of the added families.
