# Wave 5.2R Stage 4 Data-Only Residual Capacity Ladder

## Overview

Stage 4 measures how much of the frozen PF-A analytical error can be learned by
an ordinary neural residual before any physics-guided loss is introduced.

The stage is restricted to `polished_dataset`, setpoint inputs, and the `Fw`
surface with split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.

This technical document is automatically approved under the user's standing
authorization for all sixteen Wave 5.2R stages. No subagent is planned because
repository instructions require separate explicit approval before delegation.

Training remains subject to the separate campaign-planning approval gate.

## Technical Approach

The implementation will keep a PF-A surface explicit and frozen in the primary
hybrid arms. The preparation preflight found that the exact Stage 3/Phase 1
replay used measured operating averages even though the roadmap scope is
setpoint-only. Stage 4 therefore refits the identical complete-quadratic
Polynomial-Fourier formulation using only nominal forward setpoints from the
frozen training split. The legacy measured-input surface remains preserved as
comparison evidence but is not used by the trainable campaign.

Because the setpoint tensor stores torque as a positive magnitude, the
analytical path will reconstruct signed torque explicitly from the direction
flag. Forward torque is `-abs(torque_setpoint)`; no measured torque channel is
used.

Every candidate will expose:

- the analytical anchor curve;
- the learned residual curve;
- the combined curve;
- residual energy relative to anchor energy;
- residual projection onto the nine PF-A harmonic orders;
- operating-support tier.

The first campaign will use identical data loss, optimizer, epoch budget,
batching, split, seed roster, and full-curve evaluation for every learned arm.
Parameter-matched direct predictors will separate residual-architecture value
from analytical-anchor value.

The required ladder is:

| ID | Formulation |
| --- | --- |
| `R0` | frozen PF-A with zero learned residual |
| `R1` | direct data-only MLP without PF-A |
| `R2` | frozen PF-A plus unconstrained residual MLP |
| `R3` | frozen PF-A plus bounded-amplitude residual MLP |
| `R4` | frozen PF-A plus low-rank residual basis |
| `R5` | trainable correction to frozen PF-A coefficients |

The bounded residual will use a differentiable
`residual_bound * torch.tanh(raw_residual)` output. Deterministic DataLoaders
will use a seeded `torch.Generator` and worker seeding. Frozen modules will use
`requires_grad_(False)` and will be excluded from the optimizer parameter
groups.

## Involved Components

- Stage 3 PF-A coefficient surface and validity-envelope artifacts as legacy
  comparison evidence.
- A training-only causal setpoint PF-A refit and explicit causality audit.
- A new explanatory model report for the Stage 4 family.
- New residual-capacity model implementations under `scripts/models/`.
- Training integration under `scripts/training/`.
- Campaign configurations under `config/training/`.
- Campaign preparation and PowerShell launcher under `scripts/campaigns/`.
- Launcher usage note under `doc/scripts/campaigns/`.
- Preliminary plan under `doc/reports/campaign_plans/`.
- Persistent state in `doc/running/active_training_campaign.yaml`.
- Immutable run outputs under `output/training_runs/` and campaign outputs
  under `output/training_campaigns/`.
- Stage 4 result report and validated PDF under
  `doc/reports/campaign_results/`.

## Implementation Steps

1. Freeze the Stage 3 PF-A artifact hash and support-envelope contract, audit
   its runtime-input causality, and derive the campaign anchor from training
   setpoints only.
2. Implement one inspectable model family covering `R1` through `R5`.
3. Preserve `R0` as a no-training analytical control.
4. Match learned-arm parameter counts within a declared tolerance.
5. Add width and depth capacity levels without changing the data contract.
6. Add residual-energy penalties at zero, weak, and moderate strengths.
7. Add frozen, partial-unfreeze, and full-unfreeze coefficient comparisons
   only where the formulation supports them.
8. Record Stage 2 loss, gradient, schedule, and deterministic-batch
   instrumentation.
9. Add one-batch and short smoke validations before full training.
10. Prepare the campaign plan, YAML queue, local and remote PowerShell
    launcher, launcher note, and persistent campaign state.
11. Execute at least three fixed seeds for any candidate that passes the first
    bounded screen.
12. Close the campaign with explicit leaderboard and winner artifacts.
13. Compare every hybrid against both PF-A and a parameter-matched direct MLP
    using raw, centered-shape, offset, harmonic, derivative, robustness, and
    support-tier evidence.
14. Reject any candidate that improves scalar error through opaque analytical
    cancellation or unsupported extrapolation.
15. Generate and visually validate the campaign-results PDF.
16. Synchronize roadmap, backlog, master summary, ledger, guides, and portal.
17. Run source, campaign, Markdown, Sphinx, PDF, Git, and size preflights.
18. Create the dedicated Stage 4 commit and report the result before Stage 5.

## Training Authorization Boundary

Creating the technical document and campaign package does not authorize
training by itself.

Before the first one-batch validation or training run:

- the preliminary campaign-planning report must exist;
- the report must be explicitly approved;
- the campaign YAML, launcher, launcher note, and persistent state must agree;
- no protected active-campaign file may be modified without authorization.

## Exit Decision

A hybrid advances only if it beats:

1. frozen PF-A;
2. its parameter-matched direct data-only control;

while preserving bounded analytical contribution, multi-index full-curve
quality, deterministic stability, and the deployment support contract.
