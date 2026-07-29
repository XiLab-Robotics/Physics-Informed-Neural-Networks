# Wave 5.2R Stage 5 Complex Harmonic Coefficient Residuals Campaign Plan

## Overview

This preliminary report defines the representation-aligned Stage 5 campaign on
`polished_dataset` setpoint `Fw` curves.

The approved technical document is:

- `doc/technical/2026-07/2026-07-28/2026-07-28-15-56-46_wave52r_stage5_complex_harmonic_coefficient_residuals.md`

The campaign tests whether explicit sine/cosine coefficient learning can improve
canonical full-curve TE prediction without repeating Stage 4 analytical
cancellation. It does not introduce MMT and does not claim a validated physical
residual merely because a Fourier representation is used.

## Frozen Scope

- program stage: Wave 5.2R Stage 5;
- dataset: `polished_dataset`;
- input mode: setpoints;
- surface: `Fw`;
- schema: `polished_setpoint_complex_curve_v1`;
- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- training curves: `675`;
- validation curves: `194`;
- test curves: `97`;
- excluded metadata anomalies: the three Stage 0 quarantined conditions;
- uniform angular samples per curve: `2048`;
- analytical anchor: `PF_A_SETPOINT_QUADRATIC`;
- first-screen seed: `314159`;
- conditional stability seeds: `271828` and `161803`;
- official TE Curve Verification Pipeline: excluded from normal closeout.

The only runtime inputs are output angle, nominal speed setpoint, signed torque
derived from torque magnitude plus the forward direction contract, and nominal
temperature setpoint.

## Representation Contract

The dataset builder must:

1. reuse the frozen Stage 0 split without reassignment;
2. sort and periodically close each accepted forward curve;
3. resample onto the same uniform `2048`-point angular grid;
4. compute sine and cosine coefficients with one deterministic convention;
5. fit all coefficient normalization using training curves only;
6. preserve raw coefficients, normalized coefficients, reconstructed curves,
   source hashes, and reconstruction residuals;
7. fail if a validation or test target influences order selection,
   normalization, scale calibration, or neighboring-condition topology.

No training candidate may consume the original long point payload. Full-curve
training and bounded evaluation must call the same representation module.

## Harmonic Order Sets

| Set | Orders | Purpose |
| --- | --- | --- |
| `core` | `1, 3, 39, 40, 78, 81, 156, 162, 240` | causal PF-A comparison |
| `core_plus_residual` | core plus `2, 80, 159, 237` | Stage 4 residual evidence |
| `data_selected` | frozen by training-only stable residual energy | bounded discovery |

The data-selected set must declare:

- selection threshold;
- bootstrap stability;
- maximum number of orders;
- excluded aliases;
- Nyquist margin;
- band assignment;
- validation and test non-use proof.

## Candidate Matrix

The first screen contains eighteen runs at seed `314159`.

### Matched Controls

| ID | Candidate | Order set | Capacity |
| --- | --- | --- | --- |
| `C01` | direct uniform-curve MLP | not applicable | compact |
| `C02` | direct uniform-curve MLP | not applicable | deep |
| `C03` | direct coefficient MLP | core | compact |
| `C04` | direct coefficient MLP | core | deep |
| `C05` | direct coefficient MLP | core plus residual | compact |
| `C06` | direct coefficient MLP | core plus residual | deep |
| `C07` | direct coefficient MLP | data selected | compact |
| `C08` | direct coefficient MLP | data selected | deep |

### Anchored Coefficient Candidates

| ID | Candidate | Order set | Capacity | Auxiliary guidance |
| --- | --- | --- | --- | --- |
| `H01` | PF-A plus coefficient correction | core | compact | curve plus complex |
| `H02` | PF-A plus coefficient correction | core | deep | curve plus complex |
| `H03` | bounded coefficient correction | core | compact | curve plus complex |
| `H04` | bounded coefficient correction | core | deep | curve plus complex |
| `H05` | band-separated correction | core plus residual | compact | curve, complex, band |
| `H06` | band-separated correction | core plus residual | deep | curve, complex, band |
| `H07` | band-separated correction | data selected | compact | curve, complex, band |
| `H08` | band-separated correction | data selected | deep | curve, complex, band |

### Smoothness Ablations

| ID | Base candidate | Surface weight |
| --- | --- | ---: |
| `A01` | H05 compact | weak |
| `A02` | H05 compact | moderate |

The smoothness arms are included in the eighteen-run total; the primary matrix
contains eight controls, eight hybrids, and two ablations. C07 and C08 are
mandatory because H07 and H08 cannot be judged against a direct model using a
different coefficient order set.

## Parameter-Matching Contract

Each anchored candidate must have a direct coefficient control with:

- identical causal operating inputs;
- identical order set;
- identical coefficient normalization;
- identical hidden capacity;
- identical curve reconstruction;
- identical optimizer and epoch budget;
- trainable parameter-count mismatch no greater than five percent.

The direct curve controls are representation controls and are not required to
match the coefficient-output dimension. Their trainable capacity must instead
match the compact and deep parameter tiers declared by the preparation report.

## Loss Contract

Every coefficient candidate uses:

```text
L_total =
    lambda_curve * L_curve
  + lambda_complex * L_complex
  + lambda_band * L_band
  + lambda_surface * L_surface
```

The fixed rules are:

- `L_curve` is active in every learned arm;
- direct curve controls use `L_curve` only;
- direct coefficient and H01-H04 arms use `L_curve + L_complex`;
- H05-H08 add band-balanced coefficient error;
- A01-A02 add neighboring-training-condition surface smoothness;
- no coefficient objective may use amplitude/phase coordinates directly;
- no auxiliary term may use validation or test neighbors.

Training-only calibration will normalize each named loss so the initial
gradient-scale ratio is recorded. Fixed weights remain the primary screen.
Adaptive weighting is reserved for Stage 11.

## Bounded-Correction Contract

H03-H08 must expose per-coefficient bounds derived from training-only PF-A
coefficient residual quantiles. A separate offset bound is required.

The validator must prove:

- zero correction reproduces PF-A exactly;
- every bounded correction respects its declared coefficient limit;
- reconstructed curves exactly match the emitted coefficients;
- correction RMS does not dominate anchor RMS;
- no band correction exceeds its declared energy ratio.

## Training Budget

Every first-screen run uses:

- full uniform curves with `2048` angular samples;
- curve batch size: `16`;
- workers: `2`;
- precision: float32;
- optimizer: AdamW;
- learning rate: `5e-4`;
- weight decay: `1e-5`;
- maximum epochs: `48`;
- minimum epochs: `8`;
- early-stopping patience: `8`;
- deterministic seed and DataLoader generator;
- checkpoint selection based on a predeclared validation curve-first score.

The preparation script may reduce the batch size after one-batch memory
validation. It may not change the split, angular grid, order set, loss profile,
candidate identity, or seed without updating this report.

## First-Screen Exit Gate

A hybrid passes the first screen only when it simultaneously:

1. improves test full-curve MAE over PF-A;
2. improves test full-curve MAE over its matched direct control;
3. does not regress centered MAE, offset error, derivative RMSE, closure,
   harmonic amplitude, or harmonic phase beyond the frozen Stage 0 tolerances;
4. keeps correction-to-anchor RMS at or below `0.5`;
5. respects coefficient and band bounds;
6. is finite on every supported-core curve;
7. contains no representation mismatch or leakage finding.

Only passing candidates receive the two stability-seed continuations. If no
candidate passes, the campaign closes as a valid negative Stage 5 result.

## Required Preflight

Before training, the package must prove:

1. source, split, PF-A, and Stage 4 evidence hashes agree;
2. all `966` accepted forward curves are represented once;
3. the three quarantined conditions remain excluded;
4. every curve uses the identical uniform angular grid;
5. coefficient extraction and reconstruction satisfy the declared tolerance;
6. coefficient normalization is training-only;
7. data-selected orders are training-only and deterministic;
8. direct controls never call the analytical-anchor path;
9. zero corrections replay PF-A exactly;
10. bounded coefficients cannot exceed their limits;
11. smoothness edges connect training conditions only;
12. parameter matching passes;
13. every candidate completes a real one-batch forward/backward/update cycle;
14. local and remote launcher preflights agree;
15. the persistent campaign state matches the generated package.

## Closeout Evidence

Normal closeout must produce:

- campaign manifest, execution report, leaderboard, and explicit winner;
- coefficient and band decision matrices;
- full-curve raw, centered, offset, derivative, closure, harmonic, and tail
  metrics;
- correction-to-anchor and band-energy diagnostics;
- representative measured-versus-predicted curves;
- coefficient-surface and operating-condition plots;
- deterministic stability evidence when triggered;
- Markdown campaign-results report and visually validated PDF;
- synchronized backlog, roadmap, master summary, ledger, usage guide, and
  Sphinx portal.

## Authorization

The technical document, this campaign plan, package generation, one-batch
validation, training, closeout, PDF export, documentation synchronization, and
dedicated commit are approved by the user's standing authorization until
`2026-07-28T23:57:23+02:00`.
