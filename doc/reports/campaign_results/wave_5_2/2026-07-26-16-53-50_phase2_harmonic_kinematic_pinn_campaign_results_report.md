# Phase 2 Harmonic And Kinematic PINN Campaign Results Report

## Overview

This report closes Wave 5.2 Phase 2 of the sixteen-phase full-PINN
theory-validation roadmap. Phase 2 implemented and tested the repository's
first target-free differentiable angular-oscillator residual, periodic
value-and-slope closure, and an optional frozen Bauer analytical anchor.

The canonical campaign completed all eight direction-separated runs:

- campaign:
  `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26`;
- dataset: `polished_dataset`, causal `setpoints` input mode;
- common eligible split: `675` train, `194` validation, and `97` test
  conditions per direction;
- surfaces: `Fw` and `Bw`, never merged for selection;
- completed runs: `8`;
- failed runs: `0`;
- campaign duration: approximately `2 h 35 min`;
- scalar program-best promotion: none;
- Phase 2 physics promotion: none.

The phase is complete as a valid negative result. The infrastructure and
falsification evidence advance to Phase 3, but no Phase 2 oscillator,
periodic-boundary, or Bauer-anchor loss weight becomes a default physical
ingredient.

## Evidence Contract

The canonical restart used the exact Phase 1 paired-condition assignment
signature:

```text
c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16
```

Three Phase 0 anomalous training conditions remained quarantined. Every arm
used the same:

- causal angle, speed, torque, temperature, and direction contract;
- `675 / 194 / 97` direction-specific condition split;
- stride `8`;
- batch size `4`;
- distributed `4,096`-point curve cap;
- `64` physics collocation points per batch;
- `24`-epoch ceiling and patience `5`;
- harmonic order set `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and
  `240`.

The smallest audited source curve still supplied at least `1,350` angular
samples after stride, more than `2.8` times the `480`-sample Nyquist minimum
for order `240`. The training loop evaluated at least `10,800` physics
collocation points per epoch.

Earlier interrupted or diagnostic attempts are retained for provenance but
are ineligible for this phase decision. Immutable candidate-registry
snapshots bind the bounded curve-payload diagnostic to the eight canonical
checkpoints.

## Candidate Definitions

| Arm | Architecture And Loss | Scientific Role |
| --- | --- | --- |
| `H0` | Explicit Fourier heads, no physics loss | Structured data-driven control; not a full PINN |
| `H1` | Implicit harmonic heads plus normalized oscillator residual | Isolated governing-residual test |
| `H2` | `H1` plus periodic value and slope closure | Oscillator and kinematic-boundary test |
| `H3` | `H2` plus frozen Phase 1 Bauer coefficient anchor | Analytical-plus-PINN guidance test |

For order \(k\), the target-free oscillator residual was:

```text
R_k = (1 / k^2) * d2 h_k / d theta2 + h_k
```

The normalization prevents high orders from dominating only because of their
derivative scale. Periodic closure was evaluated at matched causal
conditions:

```text
y(0, u) = y(2 pi, u)
dy/dtheta(0, u) = dy/dtheta(2 pi, u)
```

## Scalar Campaign Results

The campaign leaderboard is a training diagnostic only. It ranks all
directions together by test MAE and therefore cannot make a program or
physics promotion.

| Rank | Arm | Surface | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `H0` Fourier control | `Fw` | 0.001646 | 0.002040 | 0.001852 |
| 2 | `H1` oscillator | `Bw` | 0.001723 | 0.002210 | 0.001856 |
| 3 | `H2` oscillator + periodic | `Fw` | 0.001784 | 0.002245 | 0.002074 |
| 4 | `H3` oscillator + periodic + Bauer | `Bw` | 0.001931 | 0.002469 | 0.002087 |
| 5 | `H1` oscillator | `Fw` | 0.001951 | 0.002401 | 0.002127 |
| 6 | `H2` oscillator + periodic | `Bw` | 0.001966 | 0.002545 | 0.002018 |
| 7 | `H0` Fourier control | `Bw` | 0.002066 | 0.002643 | 0.002077 |
| 8 | `H3` oscillator + periodic + Bauer | `Fw` | 0.002389 | 0.003042 | 0.002898 |

Direction-specific scalar interpretation:

- `Fw`: `H0` remains best. Every genuine PINN arm increases held-out MAE.
- `Bw`: `H1` improves test MAE by about `16.6%` relative to `H0`, but scalar
  gain alone is insufficient.
- `H3-Fw`: the Bauer-anchor test loss reaches approximately `9.01`, versus
  approximately `0.00455` on `Bw`. The frozen anchor is therefore not stable
  enough across directions to retain at the tested weight.
- the program winner remains the accepted `periodic_gru_sequence_bw`; the
  program registry is not changed.

## Common-Split Curve-Payload Evaluation

A bounded `CVP 1.2` diagnostic replayed:

- the eight canonical Phase 2 checkpoints;
- the accepted non-windowed periodic harmonic MLP for `Fw` and `Bw`;
- the accepted time-windowed periodic GRU for `Fw` and `Bw`;
- exactly `97` common held-out curves per direction;
- full-resolution source curves for metrics;
- reduced payload samples only for repository-size control.

This is a Phase 2 closeout diagnostic, not the heavy official
`TE Curve Verification Pipeline` refresh and not an automatic registry
promotion.

MAE and closure are in degrees, MPE and amplitude error are percentages, and
phase error is in degrees.

| Rank | Candidate | Surface | MAE | MPE | Amp. Err. | Phase Err. | Closure |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | accepted periodic harmonic MLP | `Fw` | 0.001694 | 3.439 | 15.380 | 13.592 | 0.000881 |
| 2 | accepted periodic GRU | `Fw` | 0.001618 | 3.278 | 19.237 | 12.167 | 0.000892 |
| 3 | accepted periodic harmonic MLP | `Bw` | 0.001912 | 3.581 | 21.132 | 17.127 | 0.000861 |
| 4 | accepted periodic GRU | `Bw` | 0.001837 | 3.494 | 31.498 | 15.321 | 0.001313 |
| 5 | Phase 2 `H0` | `Fw` | 0.001998 | 4.174 | 39.328 | 21.029 | 0.000872 |
| 6 | Phase 2 `H1` | `Fw` | 0.002232 | 4.734 | 43.016 | 19.899 | 0.000857 |
| 7 | Phase 2 `H2` | `Fw` | 0.002102 | 4.407 | 49.491 | 20.335 | 0.000938 |
| 8 | Phase 2 `H1` | `Bw` | 0.002186 | 4.234 | 52.097 | 24.208 | 0.000865 |
| 9 | Phase 2 `H3` | `Bw` | 0.002386 | 4.710 | 56.022 | 25.209 | 0.000864 |
| 10 | Phase 2 `H0` | `Bw` | 0.002494 | 5.021 | 48.979 | 33.574 | 0.000868 |
| 11 | Phase 2 `H2` | `Bw` | 0.002414 | 4.802 | 60.967 | 25.537 | 0.000869 |
| 12 | Phase 2 `H3` | `Fw` | 0.002651 | 5.644 | 69.329 | 27.110 | 0.000957 |

The four accepted baselines occupy the first four composite diagnostic
positions. No Phase 2 candidate displaces either the time-windowed or
non-windowed accepted reference on its valid surface.

The scalar test loop and the full-curve replay use the same held-out
conditions but different angular sampling. The scalar metrics use the
training data-module stride and distributed point cap; the closeout
diagnostic uses every source-curve point. Their absolute MAE values are
therefore not expected to be identical.

## Dominant And Selected Harmonic Evidence

Order `1` is dominant on both surfaces, with mean truth amplitude close to
`0.0172 deg`. The next strongest mean amplitudes are:

- `Fw`: orders `39`, `78`, `40`, and `3`;
- `Bw`: orders `156`, `78`, `3`, and `162`.

Relative to `H0`, `H1-Bw` produces a real but incomplete improvement:

| Order | H0 Amp. Error [%] | H1 Amp. Error [%] | H0 Phase Error [deg] | H1 Phase Error [deg] |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3.409 | 0.777 | 0.476 | 0.308 |
| 3 | 24.878 | 15.860 | 17.565 | 16.569 |
| 39 | 32.804 | 18.625 | 27.104 | 29.702 |
| 40 | 61.137 | 23.522 | 48.798 | 16.044 |
| 78 | 29.109 | 55.215 | 35.880 | 15.069 |
| 156 | 84.639 | 137.757 | 56.514 | 36.276 |
| 240 | 66.010 | 98.020 | 33.241 | 26.228 |

This shows why scalar-only acceptance would be misleading. The oscillator
prior helps the dominant order and several low or intermediate orders, but it
redistributes error into other physically relevant harmonics.

On `Fw`, `H1` slightly improves mean phase error but worsens mean amplitude
error and raw curve error. `H2` does not recover a consistent advantage.
`H3` becomes the weakest Phase 2 candidate on `Fw`.

## Physics Residual Evidence

The deterministic validator proves:

- an admissible sine/cosine component has maximum normalized residual near
  `1.19e-7`;
- a deliberately inadmissible component has residual mean square near `1.57`;
- enabled physics terms backpropagate nonzero gradients;
- explicit and implicit inference paths remain finite.

The real campaign proves the residual participates in optimization, but a
smaller residual does not imply a better TE curve. Representative held-out
physics diagnostics are:

| Arm | Surface | Oscillator Loss | Periodic Value Loss | Periodic Slope Loss | Bauer Anchor Loss |
| --- | --- | ---: | ---: | ---: | ---: |
| `H1` | `Fw` | 0.02585 | 0.000832 | 0.90053 | 0 |
| `H1` | `Bw` | 0.02576 | 0.000582 | 5.81174 | 0 |
| `H2` | `Fw` | 0.01861 | 0.002293 | 0.001295 | 0 |
| `H2` | `Bw` | 0.02517 | 0.000065 | 0.001812 | 0 |
| `H3` | `Fw` | 0.02207 | 0.005010 | 0.001813 | 9.01045 |
| `H3` | `Bw` | 0.01794 | 0.001408 | 0.000636 | 0.004550 |

The periodic slope term works as intended in `H2` and `H3`, reducing the
unweighted diagnostic by several orders of magnitude relative to `H1`.
However, the offline closure mismatch was already approximately
`0.0009 deg` for all candidates. Tightening the mathematical boundary does
not materially improve the measured curve surface.

## Exit-Gate Decision

The Phase 2 exit rule was:

> Promote only constraints that improve held-out harmonic fidelity without
> degrading raw error, offset behavior, or direction-specific continuity.

Decision: **Phase 2 complete; no physical constraint promoted.**

Rationale:

1. `Fw` retains the Fourier control over every genuine PINN arm on raw and
   composite curve evidence.
2. `H1-Bw` is the strongest physics signal, but its amplitude improvement is
   not consistent across selected orders.
3. periodic closure reduces its own residual but does not create a
   compensating curve-first gain.
4. the Bauer anchor is directionally unstable at the tested weight and is
   rejected as a default training term.
5. accepted GRU and harmonic-MLP baselines remain stronger on the common
   held-out surface.

No repeat-seed or broad physics-weight escalation is justified for a
non-passing arm. The negative screen is the stopping rule that prevents
spending additional training budget on a formulation that failed its initial
multi-index gate.

## Retained Engineering Value

The phase still delivers reusable infrastructure:

- a differentiable mechanism-grouped harmonic-head PINN;
- higher-order angular automatic differentiation;
- bounded target-free collocation;
- separate oscillator, periodic-value, periodic-slope, and analytical-anchor
  logging;
- exact common-split support in training and CVP playback;
- immutable campaign checkpoint snapshots;
- full per-order harmonic diagnostic export;
- a local and `-Remote` campaign package;
- an inspectable inference path compatible with later TwinCAT simplification.

Phase 3 may reuse the condition encoder, explicit intermediate quantities,
common split, controls, and reporting surface. It must not inherit nonzero
Phase 2 physics weights by default.

## Registry And Program Status

- The campaign winner artifact remains `H0-Fw`, explicitly labeled scalar.
- The current program-best registry remains
  `te_periodic_gru_sequence_bw`.
- No official CVP recommendation changes.
- `H1-Bw` is retained as exploratory evidence, not an accepted model.
- The general full-PINN roadmap advances to Phase 3:
  quasi-static compliance and elastic-offset PINNs.
- The paper-faithful MMT branch remains deferred and does not block Phase 3.

## Artifact Inventory

Canonical campaign:

- `output/training_campaigns/2026-07-26-14-03-44_phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26/`
- `campaign_leaderboard.yaml`
- `campaign_best_run.yaml`
- `campaign_best_run.md`
- `campaign_execution_report.md`
- `candidate_registries/`

Curve-payload evidence:

- `output/validation_checks/phase2_harmonic_kinematic_pinn_curve_payload_diagnostics/2026-07-26-16-49-48__track2c_curve_payload_diagnostics/`
- `candidate_payload_diagnostics.csv`
- `curve_payload_diagnostics.csv`
- `harmonic_payload_diagnostics.csv`
- `curve_payload_samples.jsonl`
- `track2_curve_payload_diagnostics_summary.yaml`

Documentation:

- `doc/reports/analysis/model_development_waves/wave_5_2/harmonic_kinematic_pinn/[2026-07-26]/phase2_harmonic_kinematic_pinn_model_report.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/harmonic_kinematic_pinn/curve_payload_diagnostics/[2026-07-26]/track2_curve_payload_diagnostics_report.md`
- `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`

## Next Step

Prepare Phase 3 as a new isolated formulation:

- bounded signed torque-to-deflection compliance;
- temperature-conditioned stiffness;
- direction-specific elastic and backlash offsets;
- zero-torque intercept and monotonicity checks;
- explicit comparison against the accepted baselines and the Phase 2 Fourier
  control;
- no automatic reuse of the rejected Phase 2 physical losses.
