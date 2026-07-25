# Phase 0 PINN Program Foundations Report

## Decision

Phase 0 is **passed**. The canonical Wave 5.2 dataset now has a
versioned foundation contract for coordinates, units, directions, operating
domain, temporal evidence, causal signal availability, harmonics, duplicates,
and split leakage.

This is a non-training result. It does not claim that any analytical law or
PINN formulation is accurate.

## Dataset And Split Evidence

- Paired operating conditions: `969`
- Directional curves scanned: `1938`
- Numeric rows scanned: `75585373`
- Curve row range: `10799` to
  `194401`
- Train / validation / test conditions: `678` /
  `194` / `97`
- Stable split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`
- Full nominal Cartesian grid:
  `true`
- Surface coverage: `Fw=969`,
  `Bw=969`,
  `global_pairable=969`

The nominal grid contains 17 speed values, 19 torque magnitudes, and three
temperature setpoints. Every held-out condition is a withheld Cartesian
combination inside axis values represented by the training split.

## Coordinate, Unit, And Sign Contract

- `theta` is the input-encoder cumulative angle divided by the ratio `81` and
  wrapped into one output-equivalent revolution.
- `theta_TE` is the zeroing-corrected output angle minus the ratio-scaled input
  angle; it is a derived target, not a dedicated sensor channel.
- `Fw` has positive measured mean `theta_dot`; `Bw` has negative measured mean
  `theta_dot`.
- Filename torque is a nonnegative nominal magnitude. `tau_load` is signed
  measured output torque and must retain its sign.
- Harmonic order is expressed in cycles per output revolution; FFT phase is in
  radians.

All curves cover between
`0.999814849` and
`1.000010447` output
revolutions after directional unwrapping.

## Operating-Metadata Anomalies

Phase 1 eligible conditions:
`966` of
`969`.

The following conditions remain in the provenance inventory but are excluded
from Phase 1 fitting and held-out scoring:

- `speed_500rpm__torque_600Nm__temperature_35degC` (train): `nominal_speed_mismatch`
- `speed_800rpm__torque_200Nm__temperature_25degC` (train): `nominal_torque_mismatch`
- `speed_1400rpm__torque_800Nm__temperature_35degC` (train): `nominal_torque_mismatch`

## Domain And Temporal Evidence

- Held-out conditions: `291`
- Held-out extrapolation conditions:
  `0`
- Held-out conditions with an axis value absent from training:
  `0`
- Time-ordered rows: available
- Explicit timestamp column: unavailable
- Provenance sample interval: `0.00025 s`
- Angular acceleration: causally reconstructable with one-step speed history
- Continuous reversal trajectories: unavailable in the directional curve files
- Per-condition load inertia: unavailable
- `DataValid`: applied upstream; absent from polished files

## Causal And PLC Availability

The signal matrix distinguishes measured, measured-derived, causal-derived,
reconstructable, target-only, upstream-only, offline-oracle, and unavailable
quantities. Current direct or causal deployment inputs are angle, speed,
signed torque, oil temperature, direction, and optional one-step acceleration.

Detailed contact state, component errors, load inertia, efficiency losses,
wear state, and synchronized motor current are not current online inputs. Later
phases must use them only as offline oracles, synthetic variables, or explicit
instrumentation-gated branches.

## Harmonic Evidence

The audit resampled every curve to
`2048`
uniform angular points and measured orders 1 through
`400`.

- Fw prevalent-order ranking:
  `1, 39, 3, 40, 78, 240, 81, 159, 2, 156, 162, 80, 120, 237, 42, 234, 243, 191, 206, 297`
- Bw prevalent-order ranking:
  `1, 3, 78, 156, 39, 240, 159, 2, 40, 162, 42, 237, 158, 80, 160, 287, 234, 243, 318, 206`

This ranking is evidence, not an automatic model-order selection. Phase 1 must
compare paper orders, local orders, ONNX orders, and PLC orders explicitly.

## Exit-Gate Checks

- `paired_manifest_validated`: `true`
- `all_directional_curves_scanned`: `true`
- `all_values_finite`: `true`
- `all_curves_cover_one_revolution`: `true`
- `all_direction_speed_signs_valid`: `true`
- `full_nominal_cartesian_grid`: `true`
- `all_held_out_axes_supported_by_training`: `true`
- `operating_metadata_anomalies_explicitly_quarantined`: `true`
- `all_three_surfaces_represented`: `true`
- `signal_causality_matrix_complete`: `true`
- `harmonic_map_complete`: `true`
- `duplicate_and_leakage_audit_passed`: `true`

## Artifacts

- Audit YAML:
  `output/analysis/pinn_program_foundations/phase0_foundation_audit.yaml`
- Curve audit:
  `output/analysis/pinn_program_foundations/phase0_curve_audit.csv`
- Condition support:
  `output/analysis/pinn_program_foundations/phase0_condition_support.csv`
- Harmonic prevalence:
  `output/analysis/pinn_program_foundations/phase0_harmonic_prevalence.csv`
- Signal availability:
  `output/analysis/pinn_program_foundations/phase0_signal_availability.csv`

## Phase 1 Boundary

Phase 1 may now evaluate Polynomial-Fourier formulations because every required
current input and held-out condition is represented by a versioned contract.
The next implementation is Bauer preprocessing and complete quadratic
coefficient fitting on the frozen paired split.
