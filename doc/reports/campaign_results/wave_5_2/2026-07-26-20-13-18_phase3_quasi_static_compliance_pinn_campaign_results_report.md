# Phase 3 Quasi-Static Compliance PINN Campaign Results Report

## Overview

This report closes Wave 5.2 Phase 3 of the sixteen-phase full-PINN
theory-validation roadmap. Phase 3 implemented and tested bounded
quasi-static compliance, temperature-conditioned stiffness,
direction-specific nonlinear compliance, hard elastic-offset equations, and
shared-stiffness formulations.

The canonical campaign and its bounded stability follow-up completed:

- main campaign:
  `phase3_quasi_static_compliance_pinn_2026_07_26`;
- stability campaign:
  `phase3_c1_fw_stability_repeat_2026_07_26`;
- dataset: `polished_dataset`, causal `setpoints` input mode;
- directional split: `675` train, `194` validation, and `97` test curves;
- main campaign: `12 / 12` completed, `0` failed;
- stability campaign: `2 / 2` completed, `0` failed;
- evaluated surfaces: separate `Fw`, `Bw`, and bounded `global`;
- Phase 3 physical-ingredient promotion: none;
- accepted-reference replacement: none.

Phase 3 is complete as a valid negative result. The tested compliance laws
are implemented, differentiable, inspectable, and physically bounded, but no
formulation passed the complete predictive-stability exit gate.

## Evidence Contract

Every run reused the immutable common-split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.

Three anomalous training conditions remained quarantined. Directional arms
used `675 / 194 / 97` curves and global controls used
`1,350 / 388 / 194`. Every candidate preserved:

- causal angle, speed, nominal torque, temperature, and direction inputs;
- the audited convention that measured torque is negative for `Fw` and
  positive for `Bw`;
- stride `8`, batch size `4`, and a `4,096`-point curve cap;
- the same nine periodic orders;
- a `20`-epoch ceiling and patience `5`;
- target-free physical residuals;
- separate raw, offset, centered-shape, peak-to-peak, harmonic-amplitude, and
  harmonic-phase evidence.

The stability follow-up changed only the random initialization contract. It
added `training.random_seed` values `314159` and `271828` and called
`seed_everything(seed, workers=True)` before model and dataloader creation.

## Candidate Definitions

| Arm | Mean Or Physical Law | Scientific Role |
| --- | --- | --- |
| `C0` | learned mean plus zero-mean Fourier branch | matched data-driven control; not a PINN |
| `C1` | learned mean with bounded linear-compliance derivative residual | isolated soft compliance PINN |
| `C2` | `C1` with temperature-conditioned bounded stiffness | temperature-transfer PINN |
| `C3` | `C1` with bounded odd nonlinear torque response | nonlinear monotonic-compliance PINN |
| `C4` | hard direction-specific elastic equation plus periodic residual | hard white-box offset PINN |
| `C5` | hard shared stiffness with direction-specific intercepts | paired-direction compatibility PINN |

For `C1`, the target-free differential residual is
`d mean_TE / d tau_signed = 1 / k_direction`.

All stiffness values are strictly bounded through
`k = k_min + (k_max - k_min) * sigmoid(raw_k)`.

`C4` and `C5` place the elastic equation directly in the forward path:
`mean_TE = intercept_direction + tau_signed / k`.

The learned periodic branch contains sine and cosine terms only and therefore
has zero continuous-cycle mean by construction.

## Identifiability And Implementation Evidence

The training-only audit passed before campaign preparation:

- `1,932` eligible directional curves;
- full-rank `C1`, `C2`, `C3`, and `C5` design matrices;
- training-only stiffness estimates near `27.2` to `27.5 kNm/deg`;
- positive unconstrained compliance slopes;
- no evidence for ordered load-unload loops or direction-reversal state.

That last point is important: Phase 3 can test quasi-static elastic
compliance, but it cannot claim hysteresis, friction memory, or backlash-state
identification from static condition files.

The deterministic model validator proved:

- exact signed-torque reconstruction;
- positive bounded stiffness for all physical formulations;
- finite C0-C5 outputs and losses;
- nonzero gradients through `C1`, `C2`, and `C3` residuals;
- exact hard-equation reconstruction for `C4` and `C5`;
- positive temperature-conditioned compliance;
- nonnegative nonlinear compliance increments;
- shared `C5` stiffness;
- near-zero periodic mean;
- Lightning training and inference-context compatibility.

## Scalar Campaign Results

The scalar leaderboard uses the training datamodule's reduced angular
sampling. It is a campaign diagnostic, not a promotion decision.

| Rank | Arm | Surface | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `C1` | `Fw` | 0.001495 | 0.001887 | 0.001702 |
| 2 | `C2` | `Fw` | 0.001551 | 0.001950 | 0.001672 |
| 3 | `C0` | `Fw` | 0.001611 | 0.002017 | 0.001774 |
| 4 | `C2` | `Bw` | 0.001624 | 0.002068 | 0.001727 |
| 5 | `C3` | `Fw` | 0.001745 | 0.002209 | 0.001942 |
| 6 | `C0` | `Bw` | 0.001825 | 0.002313 | 0.001927 |
| 7 | `C1` | `Bw` | 0.001877 | 0.002386 | 0.001970 |
| 8 | `C3` | `Bw` | 0.001926 | 0.002441 | 0.002038 |
| 9 | `C0` | `global` | 0.002050 | 0.002529 | 0.001977 |
| 10 | `C4` | `Fw` | 0.002087 | 0.002481 | 0.002301 |
| 11 | `C5` | `global` | 0.002103 | 0.002550 | 0.002448 |
| 12 | `C4` | `Bw` | 0.002350 | 0.002859 | 0.002758 |

The scalar screen selected `C1-Fw` for the authorized stability gate. It did
not promote the arm.

## Full-Curve Multi-Index Screen

The bounded CVP 1.2 replay evaluated the twelve Phase 3 checkpoints and four
accepted references at full source-curve resolution. This is closeout
evidence, not the heavy official TE Curve Verification Pipeline refresh.

### Forward Surface

| Candidate | Raw MAE | Abs. Offset | Centered MAE | P2P [%] | Amp. Err. [%] | Phase [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| accepted periodic GRU | 0.001618 | 0.000690 | 0.001382 | 8.445 | 19.237 | 12.167 |
| accepted periodic MLP | 0.001694 | 0.000825 | 0.001390 | 11.802 | 15.380 | 13.592 |
| `C1` | 0.001843 | 0.000932 | 0.001481 | 10.009 | 34.128 | 21.434 |
| `C2` | 0.001910 | 0.000979 | 0.001563 | 6.550 | 49.504 | 23.278 |
| `C0` | 0.001953 | 0.000989 | 0.001608 | 6.463 | 40.930 | 22.373 |
| `C3` | 0.002068 | 0.001099 | 0.001662 | 11.284 | 44.033 | 32.643 |
| `C4` | 0.002387 | 0.001585 | 0.001476 | 8.996 | 30.879 | 18.527 |

`C1-Fw` improved over `C0-Fw` on raw error, absolute offset, centered shape,
harmonic amplitude, and phase. It worsened peak-to-peak error and remained
behind both accepted references. This qualified it for repeat seeds, not for
acceptance.

### Backward Surface

| Candidate | Raw MAE | Abs. Offset | Centered MAE | P2P [%] | Amp. Err. [%] | Phase [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| accepted periodic GRU | 0.001837 | 0.000606 | 0.001649 | 6.641 | 31.498 | 15.321 |
| accepted periodic MLP | 0.001912 | 0.000612 | 0.001677 | 11.625 | 21.132 | 17.127 |
| `C2` | 0.002097 | 0.000746 | 0.001859 | 6.424 | 47.274 | 30.608 |
| `C0` | 0.002283 | 0.001068 | 0.001830 | 6.108 | 39.341 | 28.223 |
| `C1` | 0.002331 | 0.000973 | 0.001985 | 5.992 | 69.396 | 33.184 |
| `C3` | 0.002375 | 0.001051 | 0.001978 | 7.398 | 60.411 | 25.984 |
| `C4` | 0.002813 | 0.001655 | 0.002031 | 8.019 | 58.130 | 32.574 |

`C2-Bw` improved raw and offset error over `C0-Bw`, but centered shape,
harmonic amplitude, and phase regressed. No backward arm passed the joint
gate.

### Global Surface

| Candidate | Raw MAE | Abs. Offset | Centered MAE | P2P [%] | Amp. Err. [%] | Phase [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `C0-global` | 0.002386 | 0.001238 | 0.001834 | 7.977 | 51.201 | 42.068 |
| `C5-global` | 0.002507 | 0.001635 | 0.001643 | 8.577 | 39.428 | 23.656 |

The shared-stiffness equation improved centered shape and harmonic fidelity,
but regressed raw error and offset. It therefore failed the global gate.

## C1-Fw Initialization-Stability Audit

The initial C1-Fw run and two seeded repeats were replayed on the same
full-resolution `97`-curve Fw test surface.

Stiffness is in `Nm/deg`; raw, offset, and centered errors are in degrees;
amplitude is in percent; phase is in degrees.

| Run | Seed | Stiffness | Raw | Offset | Centered | Amp. | Phase | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| initial C1-Fw | not recorded | 28,275.59 | 0.001843 | 0.000932 | 0.001481 | 34.128 | 21.434 | pass |
| C1-Fw repeat | 314159 | 27,259.39 | 0.001816 | 0.000872 | 0.001513 | 41.194 | 20.030 | pass |
| C1-Fw repeat | 271828 | 28,958.11 | 0.002198 | 0.001350 | 0.001605 | 45.693 | 22.966 | fail |

The physical parameter itself is stable:

- mean fitted forward stiffness: `28,164.36 Nm/deg`;
- population standard deviation: `697.95 Nm/deg`;
- population coefficient of variation: `2.48%`;
- stiffness-bound loss: zero for all three checkpoints;
- compliance-monotonicity loss: zero for all three checkpoints.

The predictive benefit is not stable. The `271828` repeat worsens raw error,
absolute offset, and harmonic-amplitude fidelity relative to `C0-Fw`.
Consequently, only `2 / 3` runs pass the predeclared curve-first gate.

## Exit-Gate Decision

The Phase 3 exit rule was:

The rule requires stiffness-like parameters to be stable, physically signed,
and predictive outside the fitting conditions.

Decision: **Phase 3 complete; no compliance residual promoted.**

Rationale:

1. the positive bounded stiffness estimate is numerically stable, so the
   parameterization itself works;
2. the initial C1-Fw signal is reproducible for one seed but not for both
   authorized repeats;
3. C2-Bw and C5-global trade raw or offset error against shape and harmonic
   improvements instead of improving the full surface;
4. hard C4 equations underfit raw and offset behavior;
5. all Phase 3 candidates remain behind the accepted periodic GRU and
   periodic harmonic MLP on their valid surfaces;
6. the dataset lacks ordered reversal cycles required to reinterpret static
   offsets as hysteresis or backlash state.

No Phase 3 loss weight becomes a default ingredient for later compositions.
The implementation and audits remain reusable falsification evidence.

## Registry And Program Status

- The scalar main-campaign winner is `C1-Fw`.
- The scalar stability-campaign winner is C1-Fw seed `314159`.
- Neither scalar winner is promoted.
- The current program-best registry remains
  `te_periodic_gru_sequence_bw`.
- The accepted Fw time-windowed and non-windowed references remain unchanged.
- No official TE Curve Verification Pipeline recommendation changes.
- Wave 5.2 advances to Phase 4 hysteresis, friction, and memory feasibility.

## Retained Engineering Value

Phase 3 delivers:

- an inspectable C0-C5 quasi-static compliance model family;
- explicit signed-torque reconstruction;
- bounded stiffness and direction intercept parameters;
- soft differential residuals and hard elastic equations;
- temperature-conditioned and nonlinear-compliance ablations;
- separate periodic and quasi-static outputs;
- reproducible model and worker seeding for future campaigns;
- checkpoint-level physical-parameter extraction;
- full-curve raw, offset, centered, peak-to-peak, and harmonic diagnostics;
- local and remote campaign launchers;
- TwinCAT-oriented intermediate quantities.

These components remain available as controls, diagnostic terms, or future
reformulation ingredients. They are not validated physical ingredients at the
tested weights and architecture.

## Artifact Inventory

Main campaign:

- `output/training_campaigns/2026-07-26-17-46-18_phase3_quasi_static_compliance_pinn_2026_07_26/`;
- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- `candidate_registries/`.

Stability campaign:

- `output/training_campaigns/2026-07-26-19-52-45_phase3_c1_fw_stability_repeat_2026_07_26/`;
- two immutable seeded training runs;
- repeat candidate-registry snapshots.

Curve-first evidence:

- `output/validation_checks/phase3_quasi_static_compliance_pinn_curve_payload_diagnostics/2026-07-26-19-39-21__track2c_curve_payload_diagnostics/`;
- `output/validation_checks/phase3_c1_fw_stability_curve_payload_diagnostics/2026-07-26-20-10-35__track2c_curve_payload_diagnostics/`;
- `output/analysis/pinn_program_compliance/phase3_c1_fw_stability_audit.yaml`;
- `output/analysis/pinn_program_compliance/phase3_c1_fw_stability_audit.csv`.

Documentation:

- Phase 3 technical document and campaign plan;
- compliance identifiability audit;
- quasi-static compliance PINN model report;
- C1-Fw stability audit;
- main and stability launcher notes;
- this Markdown report and its validated styled PDF companion.

## Next Step

Advance to Phase 4 as a feasibility-first gate:

1. audit whether source files preserve ordered acquisition, reversals,
   repeated cycles, and causal warm-up state;
2. distinguish directly trainable hysteresis laws from synthetic or
   offline-oracle-only tests;
3. do not launch Bouc-Wen, rolling-friction, play/stop, or stateful training
   unless repeated reversal cycles and stable causal state evolution are
   demonstrably available;
4. preserve a matched NARX or GRU causal-history comparator;
5. keep all rejected Phase 2 and Phase 3 physics weights at zero by default.
