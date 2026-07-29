# Wave 5.2R Stage 7 Mean And Centered-Shape Multi-Head Model

## Overview

This project implements Stage 7 of the polished-setpoint forward
physics-guided PINN reassessment. Stage 6 showed that global spectral,
derivative, weak-form, and coordinate-network losses redistribute error but do
not simultaneously improve raw, offset, shape, harmonic, and tail metrics.
Stage 7 therefore changes the prediction factorization rather than adding
another global loss.

The scope remains restricted to:

- `polished_dataset`;
- setpoint inputs;
- the `Fw` surface;
- the immutable split signature
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- the canonical uniform `2048`-point angular grid;
- causal inference inputs only.

The user approved this document, implementation, campaign, closeout, PDF, and
commit within the window from `2026-07-29T15:30:41+02:00` through
`2026-07-30T15:30:41+02:00`. No subagent is planned.

## Technical Approach

The model will decompose every predicted curve into two explicit quantities:

```text
predicted_curve = predicted_mean + predicted_zero_mean_shape
```

The mean head predicts the constant Fourier coefficient. The shape head
predicts bounded corrections to the non-constant Stage 5 H04 sine and cosine
coefficients. The shape reconstruction excludes the constant basis and is
then centered through `torch.mean(..., dim=1, keepdim=True)` as an executable
invariant. Adding the `[batch, 1]` mean tensor to the `[batch, 2048]` shape
uses standard PyTorch broadcasting and remains differentiable.

Current PyTorch documentation was resolved through Context7 as
`/pytorch/pytorch`. The implementation will avoid in-place broadcast
operations because current broadcasting documentation requires the in-place
target to retain its original shape.

The matched first screen will compare:

- a frozen Stage 5 H04 reference;
- a monolithic H04 fine-tuning control;
- a fully shared encoder with separate mean and shape heads;
- a partially shared encoder with head-specific branches;
- independent mean and shape networks;
- a shared encoder with gradient-conflict projection;
- analytical PF-A mean plus learned centered shape;
- learned mean plus frozen analytical PF-A shape.

The shared, partially shared, and independent models will use the same bounded
coefficient contract. Parameter counts and training budgets will be persisted.
The gradient-conflict arm will compute separate mean-loss and centered-shape
loss gradients, record their cosine, and project only conflicting shared
gradients before the optimizer step.

## Involved Components

- Stage 7 multi-head model:
  `scripts/models/mean_centered_shape_multi_head_network.py`;
- Stage 7 campaign:
  `scripts/campaigns/wave_5_2/run_wave52r_stage7_mean_centered_shape_multi_head.py`;
- local and remote launcher:
  `scripts/campaigns/wave_5_2/run_wave52r_stage7_mean_centered_shape_multi_head.ps1`;
- campaign plan:
  `doc/reports/campaign_plans/model_development_waves/wave_5_2/mean_centered_shape_multi_head/`;
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage7_mean_centered_shape_multi_head/`;
- launcher note:
  `doc/scripts/campaigns/wave_5_2/run_wave52r_stage7_mean_centered_shape_multi_head.md`;
- closeout builder:
  `scripts/reports/closeout/wave_5_2/build_stage7_mean_centered_shape_closeout.py`;
- campaign artifacts under the canonical immutable training-run and campaign
  output roots;
- synchronized roadmap, live backlog, master summary, closeout ledger, usage
  guide, and Sphinx model API.

## Implementation Steps

1. Freeze the Stage 5 H04 checkpoint, PF-A coefficient inputs, uniform Fourier
   basis, normalization, and Stage 0 split.
2. Implement exact mean and centered-shape outputs with explicit component
   tensors and runtime invariants.
3. Implement shared, partially shared, independent, analytical-mean,
   analytical-shape, and gradient-conflict variants.
4. Add deterministic synthetic checks for exact zero shape mean, reconstruction
   identity, finite gradients, bounds, and component isolation.
5. Create the approved campaign plan, queue YAML, PowerShell launcher, launcher
   note, model report, and protected active campaign state.
6. Preflight the real dataset, split signature, checkpoint compatibility,
   parameter counts, loss scaling, and gradient-cosine instrumentation.
7. Train the matched first screen with seed `314159`.
8. Evaluate raw, mean/offset, centered-shape, derivative, harmonic, closure,
   P95, worst-cell, component, and parameter-efficiency metrics.
9. Continue the best eligible shared design and its independent control on
   seeds `271828` and `161803` only if every first-screen gate passes.
10. Produce the complete Markdown results report, styled PDF, gate artifacts,
    plots, and visual PDF validation.
11. Synchronize the roadmap, backlog, ledger, master summaries, usage guide,
    Sphinx portal, and active campaign state.
12. Run Python, PowerShell, Markdown, Sphinx, PDF, file-size, staged-pack, and
    Git diff preflight before the dedicated Stage 7 commit.

## Exit Gate

A Stage 7 shared or partially shared candidate advances only if it:

- preserves raw MAE and improves both mean/offset and centered-shape MAE by at
  least `0.5%` relative to the frozen H04 reference;
- preserves derivative, closure, retained-amplitude, retained-phase, and P95
  behavior;
- beats the independent-head control on the declared composite score, or
  matches it within `0.5%` while using at most `80%` of its parameters;
- exposes exact zero-mean shape and exact reconstruction identity;
- records mean-versus-shape gradient cosine without hiding negative conflict;
- repeats the same decision across three seeds.

If no candidate passes, Stage 7 closes as a valid negative result. H04 remains
the qualified structured component entering Stage 8.
