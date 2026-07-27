# Wave 5.2R Stage 0 Forward Evidence Freeze

## Executive Summary

Stage 0 is complete and passes its exit gate.

The repository now has one immutable, forward-only baseline contract for
`polished_dataset` with setpoint inputs. The contract covers the same `97`
eligible held-out `Fw` operating conditions for:

- `PF_A_LOCAL_QUADRATIC`;
- `accepted_periodic_mlp_harmonic_Fw`;
- `accepted_periodic_gru_sequence_Fw`.

The split signature is
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
All twelve numerical reproduction checks pass within their declared
tolerances. No training was executed and no test condition entered the
Polynomial-Fourier coefficient fit.

The forward GRU remains the lowest raw-error reference. The harmonic MLP has
the best current composite curve-payload diagnostic score because it preserves
the selected harmonic amplitudes better on average. `PF-A` remains a useful,
inspectable analytical anchor, but it is not the best raw predictor.

## Scope And Evidence Contract

| Field | Frozen value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` only |
| Eligible train conditions | `675` |
| Eligible validation conditions | `194` |
| Eligible test conditions | `97` |
| Quarantined anomalies | `3` training conditions |
| Angular unit | degree |
| Evaluation resolution | full curve |
| Training in this stage | none |

The condition manifest preserves the source path, byte size, and SHA-256 of
every eligible forward curve. The candidate provenance inventory also hashes
the neural checkpoints, model inventories, split evidence, replay outputs,
and Polynomial-Fourier coefficient artifacts used by the freeze.

## Reproduction Result

`PF-A` reproduces the canonical Phase 1 forward test metrics exactly to the
stored floating-point precision. Its four checked metric differences are
`0.0`, against an absolute tolerance of `1e-12` degrees.

The two neural references reproduce the earlier CVP 1.2 evidence within:

- `1e-6` degrees for mean curve MAE;
- `0.01` percentage points for percentage and amplitude metrics;
- `0.01` degrees for mean phase error.

The largest observed neural difference is `0.001085` degrees in the GRU mean
harmonic phase error. This is below tolerance and is consistent with the
current diagnostic implementation rather than a model or split change.

## Baseline Comparison

| Candidate | Mean MAE [deg] | P95 MAE [deg] | Mean RMSE [deg] |
| --- | ---: | ---: | ---: |
| `PF_A_LOCAL_QUADRATIC` | 0.001807 | 0.003942 | 0.002120 |
| Harmonic MLP `Fw` | 0.001694 | 0.004098 | 0.002008 |
| Sequence GRU `Fw` | **0.001618** | **0.003817** | **0.001931** |

| Candidate | Centered MAE [deg] | Absolute mean error [deg] |
| --- | ---: | ---: |
| `PF_A_LOCAL_QUADRATIC` | 0.001385 | 0.000965 |
| Harmonic MLP `Fw` | 0.001390 | 0.000825 |
| Sequence GRU `Fw` | **0.001382** | **0.000690** |

The GRU is the strongest entry reference for raw curve error, upper-tail
error, centered shape, and mean-offset error. `PF-A` narrowly beats the
harmonic MLP on centered MAE, but trails both neural references on raw and
offset metrics.

The Phase 1 and CVP 1.2 metric contracts remain explicit. In particular,
`PF-A` reports retained-coefficient amplitude error in degrees and phase error
in radians, whereas CVP 1.2 reports relative amplitude error in percent and
phase error in degrees. These fields must not be ranked directly across the
analytical and neural contracts.

## Curve-Payload Diagnostics

The derivative metric in the following table is expressed in degrees per
degree.

| Candidate | Mean MPE [%] | P2P error [%] | Derivative RMSE |
| --- | ---: | ---: | ---: |
| Harmonic MLP `Fw` | 3.438600 | 11.801784 | **0.014963** |
| Sequence GRU `Fw` | **3.278427** | **8.443678** | 0.014968 |

| Candidate | Harmonic amplitude error [%] | Harmonic phase error [deg] | Diagnostic score |
| --- | ---: | ---: | ---: |
| Harmonic MLP `Fw` | **15.380051** | 13.591649 | **5.805821** |
| Sequence GRU `Fw` | 19.236860 | **12.165789** | 5.960079 |

The MLP wins the diagnostic score because the score penalizes mean harmonic
amplitude error. The GRU is still better on raw percentage error,
peak-to-peak behavior, and mean phase error. This split result is why Stage 0
freezes both accepted neural references instead of collapsing them into one
winner.

Per-order exports cover harmonics `1`, `3`, `39`, `40`, `78`, `81`, `156`,
`162`, and `240`. Harmonic `0` is represented by the separate mean and offset
channels rather than a phase comparison.

## Operating-Cell Evidence

The normalized operating-cell table contains `291` rows:

- `97` for `PF-A`;
- `97` for the harmonic MLP;
- `97` for the sequence GRU.

Each row retains speed, torque, oil temperature, raw MAE, RMSE, centered MAE,
and absolute curve-mean error. This table is the Stage 0 input for later
worst-cell, regime, robustness, and residual analyses.

## Leakage And Provenance Audit

The no-test-fit gate passes for three independent reasons:

1. the Polynomial-Fourier replay declares `training_executed: false`;
2. its coefficient artifact declares
   `fit_scope: eligible training conditions only`;
3. both neural candidates are pre-existing exported Wave 1 models evaluated
   by an inference-only comparison runner.

The fresh Polynomial-Fourier replay and neural replay write into isolated
Stage 0 directories and do not overwrite the earlier Phase 0, Phase 1, or
Phase 2 evidence.

## Exit Gate

| Check | Result |
| --- | --- |
| Split identity | Pass |
| Eligible condition counts | Pass |
| Exactly 97 test curves | Pass |
| Exact three-candidate roster | Pass |
| Forward-only evidence | Pass |
| Finite metrics | Pass |
| Reproduction tolerances | Pass |
| No test data in fit state | Pass |

**Decision:** accept the Stage 0 evidence freeze and authorize Stage 1,
Extended Scientific Technique Discovery. This decision authorizes research
and documentation only. Any later training stage still requires its campaign
planning package and campaign approval gate.

## Machine-Readable Artifacts

The canonical freeze root is:

`output/analysis/wave_5_2r/stage0_forward_evidence_freeze/frozen_contract/`

It contains:

- `stage0_forward_evidence_freeze.yaml`;
- `forward_condition_manifest.csv`;
- `baseline_metrics.csv`;
- `operating_cell_metrics.csv`;
- `harmonic_band_metrics.csv`;
- `provenance.csv`;
- `reproduction_comparison.csv`.

The full neural curve payloads remain under
`output/validation_checks/wave52r_stage0_forward_curve_payload_diagnostics/`.
The isolated `PF-A` replay remains under
`output/analysis/wave_5_2r/stage0_forward_evidence_freeze/pf_a_reproduction/`.

## Reproduction Commands

Build and validate the frozen contract with:

- `conda run --no-capture-output -n pinns_env python -B scripts/analysis/wave_5_2r/stage0_forward_evidence_freeze/build_stage0_forward_evidence_freeze.py`;
- `conda run --no-capture-output -n pinns_env python -B scripts/analysis/wave_5_2r/stage0_forward_evidence_freeze/validate_stage0_forward_evidence_freeze.py`.

The replay configs and exact evidence paths are stored under
`config/analysis/wave_5_2r/stage0_forward_evidence_freeze/`.

## Conclusion

Stage 0 removes ambiguity from all later `Wave 5.2R` comparisons. The forward
GRU is the raw-error reference, the harmonic MLP is the current
harmonic-diagnostic reference, and `PF-A` is the analytical anchor. Later
stages must beat matched controls on this exact test surface and must preserve
the contract-specific units recorded here.
