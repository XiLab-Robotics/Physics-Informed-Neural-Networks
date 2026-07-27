# Wave 5.2R Stage 3 Analytical Anchor Reproduction And Stress Tests

## Overview

Stage 3 qualifies `PF_A_LOCAL_QUADRATIC` as an inspectable forward analytical
component instead of relying only on its Phase 1 aggregate ranking. The stage
is restricted to the frozen `polished_dataset`, setpoint-input, `Fw` contract.

The canonical model will be refitted only on the frozen training split. The
validation and test partitions remain evaluation-only. The stage does not
train a neural network and therefore does not open a training campaign.

This technical document is automatically approved under the user's standing
authorization for all sixteen Wave 5.2R stages. No subagent is planned because
repository instructions require separate explicit approval before delegation.

## Technical Approach

The analysis will reuse the repository-owned Polynomial-Fourier primitives and
the immutable split signature from Stage 0. It will independently refit the
complete-quadratic coefficient surface and compare the resulting feature
statistics, coefficient matrix, condition number, predictions, and metrics
with the Phase 1 evidence.

Offset plus ordered sine and cosine coefficients will remain explicit
throughout the workflow. Stability will be measured with deterministic
bootstrap refits and train-only operating-axis holdouts. Analytical
corruptions will be applied after fitting so their effect can be attributed to
the anchor rather than to data leakage or residual-network capacity.

The deployable envelope will distinguish:

- supported interpolation inside the frozen training bounds;
- sparse or corner support inside those bounds;
- unsupported extrapolation outside the bounds;
- finite numerical execution from trustworthy physical use.

## Involved Components

- `scripts/analysis/polynomial_fourier_benchmark/`
  - frozen curve loading;
  - Fourier projection and reconstruction;
  - complete-quadratic fitting;
  - recovered ONNX and PLC comparators.
- `scripts/analysis/wave_5_2r/stage3_analytical_anchor_reproduction_and_stress_tests/`
  - independent refit;
  - variant comparison;
  - coefficient and condition-number stability analysis;
  - holdout and corruption sweeps;
  - validity-envelope generation;
  - exit-gate validation.
- `output/analysis/wave_5_2r/stage3_analytical_anchor_reproduction_and_stress_tests/`
  - refit coefficients;
  - reproduction metrics;
  - variant, holdout, bootstrap, corruption, and envelope evidence;
  - exit-gate summary.
- Stage 3 script documentation, usage-guide entry, Sphinx registration where
  applicable, detailed Markdown report, and validated PDF.
- Canonical roadmap, backlog, training-results summary, and closeout ledger.

## Implementation Steps

1. Load the frozen split and verify its Stage 0 signature.
2. Refit the `PF-A` local-order complete-quadratic surface on `Fw` training
   curves only.
3. Reproduce Phase 1 feature statistics, condition number, coefficient matrix,
   full-resolution predictions, and aggregate metrics within explicit
   tolerances.
4. Serialize offset and every ordered sine/cosine coefficient surface.
5. Compare local, reduced, paper-derived, recovered ONNX sparse, and
   PLC-safe harmonic subsets on the same forward evaluation surface.
6. Run deterministic bootstrap coefficient and prediction-stability analysis.
7. Run train-only torque, speed, temperature, and corner holdout refits.
8. Run coefficient-scale, phase, order-omission, and operating-input-shift
   corruption sweeps.
9. Define interpolation, sparse-corner, and unsupported-extrapolation tiers
   for deployment.
10. Assert finite predictions across every valid forward condition and reject
    unstable variants as anchors.
11. Generate machine-readable evidence and the detailed Markdown/PDF report.
12. Synchronize the roadmap and project-status documents.
13. Run Python compilation, deterministic rerun checks, Markdown QA, Sphinx QA
    when portal sources change, PDF raster validation, Git checks, and commit
    size preflight.
14. Create the dedicated Stage 3 commit and report its conclusions before
    beginning Stage 4.

## Outcome

Stage 3 completed with all twelve exit gates passing.

- PF-A reproduced every selected Phase 1 quantity with zero difference at
  tolerance `1e-12`.
- All `966` eligible forward conditions produced finite predictions.
- Sixty-four deterministic bootstrap refits remained bounded.
- Seventeen train-only holdouts exposed the lowest-temperature regime as the
  most difficult extrapolation.
- Thirty-eight corruptions identified low-order omission and torque-input
  shifts as the largest anchor sensitivities.
- The deployment contract now distinguishes supported core, sparse or corner
  support, and unsupported extrapolation.

PF-A is qualified as a bounded analytical component only inside
`supported_core`. Stage 4 Data-Only Residual Capacity Ladder is authorized.
