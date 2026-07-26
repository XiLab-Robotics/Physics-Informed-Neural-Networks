# Phase 6 Dynamic Acceleration, Inertia, And Trajectory Report

## Decision

Phase 6 is complete as a non-training observability result. Causal
acceleration is mathematically reconstructable from the raw input
encoder, and every condition contains a forward-to-backward
transition. After a 101-row causal filter, however, transition
acceleration is not robustly separated from valid-window derivative
noise at P95. Load inertia, commanded drive law, and a validated
transient TE target are also unavailable. No dynamic full-PINN
residual is therefore promoted.

`PINN-D4` remains a trainable empirical periodic-plus-temporal
comparator, but the current steady-speed target windows do not turn it
into a dynamic PINN. No campaign was prepared.

## Dataset Evidence

- Canonical raw conditions: `969`.
- Raw rows scanned: `99696607`.
- Derivative convention: strictly causal backward difference.
- Causal smoothing windows: `5`, `21`, and `101` rows.
- `DataValid` directional windows and the inter-window transition are
  reported separately.

## Split Surfaces

| Split | Conditions | Median valid speed MAD Fw/Bw (rpm) | Median valid accel P95, causal 101 (rpm/s) | Median transition accel P95, causal 101 (rpm/s) | Median valid/transition ratio | Stable valid speed | Robust transition excitation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| train | 678 | 0.446574 / 0.542309 | 69.709 | 69.983 | 0.995817 | 678 | 0 |
| validation | 194 | 0.465140 / 0.561727 | 70.239 | 70.884 | 0.999388 | 194 | 0 |
| test | 97 | 0.417810 / 0.477489 | 65.729 | 66.065 | 1.004905 | 97 | 0 |

The raw one-step derivative includes encoder discontinuities and
large isolated spikes, so it cannot be used as a physical target
without a stated causal filtering and outlier policy. Rare upper
tail transition samples are dominated by those discontinuities;
the robust P95 comparison does not separate transition excitation
from valid-window derivative noise. The transition is also outside
the validated steady-direction TE curve contract.

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-D1` | `offline_oracle_only` | `false` | Acceleration is causally reconstructable, but the selected TE windows are steady-direction regions and the reversal acceleration lies outside the validated curve-extraction contract. |
| `PINN-D2` | `blocked_by_data_contract` | `false` | No per-condition load inertia or validated rig-inertia registry is available, so an inertia-weighted balance is not identifiable. |
| `PINN-D3` | `offline_oracle_only` | `false` | Raw ordering and one reversal support offline trajectory analysis, but repeated drive laws, state resets, and validated transient TE targets are absent. |
| `PINN-D4` | `real_data_trainable` | `false` | The empirical temporal comparator is trainable on causal windows, but the current steady-speed target windows do not identify a new dynamic physical residual. |
| `PINN-D5` | `blocked_by_data_contract` | `false` | A latent inertia is algebraically confounded with residual amplitude without an independent inertia observation or source-backed local prior. |

## Exit Gate

- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `empirical_temporal_comparator_retained: true`
- `advance_to_phase7: true`

Phase 7 may now audit contact, mesh stiffness, and load sharing.
Phase 6 dynamic trajectories remain offline evidence until a
validated transient target, drive-law label, and inertia contract
are available.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_dynamics/build_phase6_dynamic_observability_audit.py
python -B scripts/analysis/pinn_program_dynamics/validate_phase6_dynamic_observability_audit.py
```
