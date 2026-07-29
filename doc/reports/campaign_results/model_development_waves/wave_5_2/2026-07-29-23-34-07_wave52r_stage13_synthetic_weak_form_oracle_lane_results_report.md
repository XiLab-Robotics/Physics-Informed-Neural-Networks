# Wave 5.2R Stage 13 Synthetic And Weak-Form Oracle Lane Results

## Executive Outcome

Stage 13 completed all `10 / 10` analytical-oracle entries with zero execution
failures. All ten predeclared synthetic gates passed, deterministic replay was
exact, test-label dependence was absent, and no real-data model was promoted.

The main positive result is not a new predictor. It is a certified weak-form
harmonic diagnostic that remains specific to the declared oscillator law while
avoiding the severe noise amplification observed when a second derivative is
estimated pointwise.

## Campaign Integrity

- Campaign: `wave52r_stage13_synthetic_weak_form_oracle_lane_2026_07_29`
- Output:
  `output/training_campaigns/2026-07-29-23-33-57_wave52r_stage13_synthetic_weak_form_oracle_lane_2026_07_29`
- Completed entries: `10`
- Execution failures: `0`
- Certified synthetic cases: `10`
- Rejected cases: `0`
- Oracle conditions: `64` training-domain H04 conditions
- Test curves checked for provenance only: `97`
- Test-label dependence: `false`
- Real-data promotion allowed: `false`

## Certification Matrix

| ID | Experiment | Primary result | Gate | Decision |
| --- | --- | ---: | ---: | --- |
| `C00` | exact H04 reconstruction | 1.53e-16 max error | <= 1e-10 | certified |
| `H01` | harmonic injection | 1.36e-15 normalized error | <= 0.02 | certified |
| `H02` | harmonic omission | 3.63e12 error ratio | >= 5 | certified |
| `C01` | coefficient-surface perturbation | 1.83e-14 normalized error | <= 0.02 | certified |
| `M01` | misspecified anchor | 2.55e-14 normalized error | <= 0.02 | certified |
| `Q01` | compliance nonlinearity | 5.84e-16 normalized error | <= 0.05 | certified |
| `P01` | pointwise oscillator residual | 103.27 maximum residual | finite baseline | certified baseline |
| `W01` | weak oscillator residual | 0.000640 | <= 0.02 | certified |
| `D01` | sampling-density stress | 128 samples | <= 256 | certified |
| `N01` | wrong-law and shuffled controls | 141.08 rejection ratio | >= 10 | certified |

The near-machine-precision recovery results are expected because these cases
certify internally consistent synthesis and projection paths. They validate
implementation correctness, not real reducer mechanics.

## Harmonic Injection And Omission

The frozen H04 core basis contains orders `1`, `3`, `39`, `40`, `78`, `81`,
`156`, `162`, and `240`. Stage 13 injected the omitted order `2` with known
sine and cosine coefficients.

The extended basis recovered both injected coefficients with normalized error
`1.36e-15`. Removing order `2` increased mean curve RMSE from
`2.42e-17 deg` to `0.003630 deg`, a ratio of `3.63e12`. This proves that the
implemented diagnostic can identify an omitted resolvable harmonic under the
ideal synthetic contract.

## Weak-Form Versus Pointwise Residual

The matched signal satisfies `u''(theta) + 5^2 u(theta) = 0`.

The pointwise lane estimates `u''` from corrupted samples. The weak lane moves
the derivative onto smooth periodic test functions and integrates against
`u`. The comparison uses identical signals, seeds, densities, and noise.

| Samples | Noise | Pointwise residual | Weak residual |
| ---: | ---: | ---: | ---: |
| 2048 | 0 | 1.96e-05 | 5.56e-06 |
| 2048 | 0.01 | 103.273 | 0.000209 |
| 1024 | 0.01 | 26.591 | 0.000153 |
| 512 | 0.01 | 6.421 | 0.000377 |
| 256 | 0.01 | 1.698 | 0.000640 |
| 128 | 0.01 | 0.320 | 0.001486 |

Weak-form residuals were lower in all `12 / 12` non-zero-noise comparisons at
densities of at least `256`. At the predeclared boundary of `256` samples and
noise `0.01`, the weak residual is `0.000640`, more than thirty times below
the `0.02` gate.

The pointwise residual increases with density under fixed per-sample noise
because the second-difference operator amplifies high-frequency corruption by
the inverse square of angular spacing. The weak residual does not differentiate
the measured signal and therefore remains stable.

## Specificity And Observability

At `256` samples and noise `0.001`:

- correct-law weak residual: `0.0003598`;
- wrong-order residual: `0.0868583`, or `241.41` times larger;
- shuffled-angle residual: `0.0507615`, or `141.08` times larger.

The minimum negative-control rejection ratio exceeds the required `10` by more
than one order of magnitude. The weak diagnostic is therefore not merely small
for every input.

All declared densities down to `128` satisfy the weak residual threshold at
noise `0.01`. Stage 13 consequently records `128` as the minimum certified
density inside the tested range. It does not extrapolate below that range.

## What The Result Establishes

Stage 13 establishes that:

- Fourier synthesis and coefficient projection are internally consistent;
- injected and omitted harmonics are detectable under an observable basis;
- known coefficient, anchor, and compliance perturbations are recoverable;
- the weak harmonic residual is substantially more noise-robust than the
  pointwise second-derivative residual;
- wrong-law and shuffled-angle controls are rejected;
- the full result is exactly reproducible with the frozen seed and contract.

## What The Result Does Not Establish

Stage 13 does not establish that:

- order `2` or the synthetic compliance law is a true reducer mechanism;
- the weak residual will improve real measured-curve prediction;
- a physical coefficient is identifiable from setpoints alone;
- H04, K01, or any PINN should be promoted;
- synthetic success satisfies Stage 14 tournament entry.

Any weak-form training loss must enter a later isolated real-data matched
control with leakage, causality, curve-first, and deployment gates.

## Decision And Next Step

The Stage 13 lane is `certified_for_synthetic_use`. No real-data winner is
declared and the accepted model registries remain unchanged.

Stage 14 may now begin the Cross-Formulation Forward Tournament. Only candidates
that already passed their isolated real-data gates may enter. Stage 13 evidence
can support implementation confidence and observability requirements, but it
cannot make an otherwise unqualified candidate eligible.

Physics-integrated Wave 6 remains closed.

For reproducibility, the campaign uses split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`,
seed `314159`, H04 core orders and curve scale, immutable campaign and validation
directories, explicit noise and density grids, and exact deterministic replay.
