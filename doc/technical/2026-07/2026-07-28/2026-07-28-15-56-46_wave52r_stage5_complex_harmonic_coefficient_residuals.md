# Wave 5.2R Stage 5 Complex Harmonic Coefficient Residuals

## Overview

Stage 5 tests whether the polished-setpoint forward TE problem becomes more
learnable and more interpretable when the network operates on explicit complex
Fourier coefficients instead of sampled pointwise residuals.

The stage is restricted to `polished_dataset`, setpoint inputs, and the `Fw`
surface with split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
MMT remains deferred and is not part of this work.

Stage 4 established a critical representation failure: pointwise training on
the long polished payload produced apparent scalar improvements that became
analytical cancellation on the canonical uniformly resampled curve surface.
Stage 5 removes that ambiguity. The curve used to derive coefficient targets,
the curve reconstructed during training, and the curve used during bounded
evaluation will share one frozen angular grid and one normalization contract.

This document and the associated campaign are approved under the user's
standing twenty-four-hour authorization. No subagent is planned because
delegation requires separate explicit approval.

## Technical Approach

Every accepted raw forward curve will be sorted by output angle, deduplicated
according to the existing curve contract, closed periodically, and resampled
onto a uniform `0 <= theta < 2*pi` grid with `4096` samples. The resampling
method, angular grid, source-file hash, split identity, and resulting curve hash
will be recorded. The frozen grid contains `2048` samples, matching the
repository's Phase 1 Polynomial-Fourier and canonical curve-first contract.

For a declared harmonic order set `H`, the real-valued coefficient vector is:

```text
z = [a_0, a_1, b_1, ..., a_h, b_h]
```

where:

```text
TE(theta) = a_0
          + sum over h in H of
              a_h * cos(h * theta)
            + b_h * sin(h * theta)
```

Sine and cosine coefficients are learned directly. Amplitude and phase are
derived only for reporting, so the training objective cannot suffer from phase
wrap discontinuities.

The primary Stage 5 comparison contains:

| ID | Formulation |
| --- | --- |
| `C0` | frozen causal PF-A analytical anchor |
| `C1` | direct curve MLP on the uniform angular grid |
| `C2` | direct coefficient MLP without PF-A |
| `H1` | frozen PF-A coefficients plus learned coefficient corrections |
| `H2` | bounded PF-A coefficient corrections |
| `H3` | band-separated PF-A coefficient corrections |
| `H4` | H3 plus neighboring-condition coefficient-surface smoothness |

The direct coefficient control and each anchored coefficient candidate will use
the same causal operating inputs, coefficient order set, hidden capacity,
optimizer, epoch budget, seed, and reconstructed-curve loss. Parameter counts
must agree within five percent where the output contract permits a direct
match.

Three nested order sets will be frozen before campaign execution:

- `core`: PF-A orders `1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `core_plus_residual`: core plus Stage 4 residual orders
  `2, 80, 159, 237`;
- `data_selected`: a training-only set selected by stable residual energy,
  excluding validation and test evidence.

The band contract will keep these outputs separately inspectable:

- offset;
- order `1`;
- low orders;
- reducer-related middle orders;
- high-order ripple;
- exploratory residual orders.

The loss is:

```text
L = lambda_curve * L_curve
  + lambda_complex * L_complex_coefficients
  + lambda_band * L_band_balance
  + lambda_surface * L_condition_surface_smoothness
```

`L_curve` is always active. Auxiliary weights are calibrated from training-only
scales and declared in immutable queue YAML. Smoothness uses only neighboring
training conditions and cannot connect training samples to validation or test
targets.

## Involved Components

- A persistent uniform full-curve and coefficient dataset builder under
  `scripts/data/` or `scripts/analysis/wave_5_2r/`.
- Immutable Stage 5 curve, coefficient, split, order-set, and normalization
  manifests under `output/analysis/wave_5_2r/`.
- A dedicated complex-coefficient model under `scripts/models/`.
- Model-factory and central campaign-runner registration.
- Named coefficient, band, curve, and surface loss instrumentation in the
  training module.
- Campaign preparation under `scripts/campaigns/wave_5_2/`.
- Campaign YAML and queue configurations under `config/training/`.
- A local and remote PowerShell launcher plus its documentation.
- Persistent campaign state in `doc/running/active_training_campaign.yaml`.
- A model report describing reconstruction, bands, losses, controls, and
  deployment implications.
- Immutable validation, training, campaign, closeout, and PDF artifacts.
- Roadmap, backlog, master-summary, ledger, usage-guide, and Sphinx portal
  synchronization.

## Implementation Steps

1. Freeze the Stage 4 failure evidence and causal PF-A artifact hashes.
2. Build the uniform `2048`-sample forward curve representation from the
   already frozen Stage 0 split.
3. Prove that coefficient extraction followed by reconstruction is numerically
   exact up to the declared omitted-order residual.
4. Fit coefficient normalization on training curves only.
5. Freeze the core, core-plus-residual, and data-selected order sets.
6. Produce coefficient-energy, stability, and band-coverage diagnostics.
7. Implement direct-curve, direct-coefficient, anchored, bounded, banded, and
   smoothness-guided candidates.
8. Expose offset, base coefficients, coefficient corrections, reconstructed
   curve, band energies, and correction-to-anchor ratios.
9. Add per-loss values, gradient norms, gradient cosines, update ratios, and
   deterministic fingerprints using the Stage 2 instrumentation.
10. Prepare the campaign plan, YAML queue, launcher, launcher note, model
    report, and persistent campaign state.
11. Run source, reconstruction, causality, leakage, parameter-match, one-batch,
    local-launcher, and remote-launcher preflights.
12. Execute the first fixed-seed bounded screen.
13. Execute the two additional declared seeds only for candidates that pass the
    first curve-first screen.
14. Close the campaign using raw, centered-shape, offset, derivative, closure,
    harmonic amplitude, harmonic phase, tail, robustness, and support evidence.
15. Reject any scalar improvement caused by coefficient cancellation, excess
    residual energy, representation drift, or target leakage.
16. Generate and visually validate the campaign-results PDF.
17. Synchronize all canonical program-status and user-facing documentation.
18. Run Markdown, Sphinx, PDF, Git, and repository-size preflights.
19. Commit Stage 5 and report its result before Stage 6.

## Training And Approval Status

The required preliminary campaign plan will be created before any one-batch or
training execution. The technical document, campaign plan, campaign execution,
closeout, PDF, and commit are covered by the active standing approval until
`2026-07-28T23:57:23+02:00`.

## Exit Decision

A Stage 5 candidate advances only if it:

1. beats the frozen PF-A anchor;
2. beats its matched direct coefficient or direct curve control;
3. improves the canonical reconstructed full-curve metrics;
4. preserves offset, derivative, closure, harmonic amplitude, and harmonic
   phase behavior;
5. remains stable across the declared seeds;
6. keeps correction energy and per-band corrections within declared bounds;
7. uses no validation-derived, test-derived, measured-runtime, or target-derived
   input.

Lower coefficient loss alone is not sufficient for promotion.
