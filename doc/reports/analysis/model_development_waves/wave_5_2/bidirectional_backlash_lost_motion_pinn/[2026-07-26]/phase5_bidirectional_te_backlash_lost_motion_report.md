# Phase 5 Bidirectional TE, Backlash, And Lost-Motion Report

## Decision

Phase 5 is complete as a non-training identifiability result. The
paired dataset supports direct measurement of separate `Fw` and `Bw`
TE surfaces and an offline directional-gap proxy. It does not contain
an independent global lost-motion measurement, component-error
metrology, contact clearances, or a repeated transition-state contract.
No full-PINN compatibility, lost-motion, or backlash residual is
therefore promoted.

`PINN-B1` remains a valid empirical shared-trunk/two-head comparator,
but it does not qualify as a full PINN by itself. Training it in this
phase would not test a new physical law, so no campaign was prepared.

## Dataset Evidence

- Paired operating conditions: `969`.
- Source rows scanned: `37805294`.
- Pairing unit: one operating condition with measured `Fw` and `Bw`
  curves.
- The common train/validation/test assignment remains condition-level
  and direction-paired.
- All directional-gap and target-alignment quantities are explicitly
  marked offline-only.

## Split Surfaces

| Split | Conditions | Median abs mean gap (arcmin) | P95 abs mean gap (arcmin) | Median raw RMSE (deg) | Median centered RMSE (deg) | Median centered correlation | Median target-derived shift (deg) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| train | 678 | 4.674202 | 8.322073 | 0.07793907 | 0.00210843 | 0.985187 | 0.703125 |
| validation | 194 | 4.780030 | 8.433419 | 0.07985382 | 0.00197521 | 0.987027 | 0.703125 |
| test | 97 | 3.792923 | 8.169105 | 0.06323698 | 0.00172060 | 0.989958 | 0.703125 |

The target-derived alignment is diagnostic evidence only. It cannot
be computed from TE during deployment and therefore cannot enter
model inputs, latent-state initialization, or held-out parameter
fitting.

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-B1` | `real_data_trainable` | `false` | Direction and all basic operating inputs are causal, but a shared-trunk multi-head model is an empirical architecture rather than a physical residual. |
| `PINN-B2` | `blocked_by_data_contract` | `false` | The paper-faithful compatibility equation requires component errors and geometry-specific equivalence parameters, while a target-fitted compatibility relation would not be an independent physical law. |
| `PINN-B3` | `offline_oracle_only` | `false` | Paired TE curves expose an offline directional-gap proxy, but no independent global lost-motion measurement identifies the latent state. |
| `PINN-B4` | `synthetic_oracle_only` | `false` | Clearance, contact force, interface stiffness, and dead-zone state are unavailable in the measured data contract. |
| `PINN-B5` | `offline_oracle_only` | `false` | Raw trajectories contain one Fw-to-Bw transition per condition but no repeated loops or deterministic reset contract for trainable state identification. |

## Interpretation

The measured difference between paired directional targets is real
dataset evidence, but it is not an independently observed backlash
state. Defining a latent lost-motion output as exactly the predicted
`Fw`/`Bw` difference would be algebraically underdetermined: the
latent variable could absorb any mismatch without identifying a
mechanism. Likewise, enforcing shared centered shape would be an
empirical regularizer unless a source-complete local compatibility
equation is available.

The source-faithful Wang relation remains blocked by missing
component-error measurements and geometry-specific pin-gear
equivalence parameters. The Xu dead-zone/contact branch remains
synthetic-only because clearance, stiffness, and contact force are
unobserved. The single raw reversal retained by Phase 4 remains an
offline transition oracle, not a reusable state label.

## Exit Gate

- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `empirical_bidirectional_comparator_retained: true`
- `advance_to_phase6: true`

Phase 6 may now audit acceleration, inertia, and trajectory
constraints. The paired directional metrics remain available for
later Wave 6 multi-head evaluation, without being relabeled as
identified backlash physics.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_bidirectional/build_phase5_bidirectional_identifiability_audit.py
python -B scripts/analysis/pinn_program_bidirectional/validate_phase5_bidirectional_identifiability_audit.py
```
