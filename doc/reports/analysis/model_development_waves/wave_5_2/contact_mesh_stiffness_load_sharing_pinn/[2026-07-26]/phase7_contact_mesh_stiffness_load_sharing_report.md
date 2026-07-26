# Phase 7 Contact, Mesh Stiffness, And Load-Sharing PINNs Report

## Decision

Contact equations are scientifically relevant but remain synthetic-oracle or instrumentation work. The current dataset cannot identify stiffness, clearance, force, load share, or contact state independently of TE.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `REF-SYNTHESIS` | implementation-facing mechanics synthesis | `true` | `false` | `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md` |
| `MMT-SYNTHESIS` | equivalent-mechanism and contact-state limitations | `true` | `false` | `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md` |
| `XU-CONTACT` | stiffness, clearance, hysteresis, and lost-motion source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2025_xu_hysteresis_torsional_rigidity_lost_motion_rv_reducer.pdf` |
| `CHEN-CONTACT` | tooth and load contact, Hertz contact, and wear source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_chen_predictive_te_geometric_errors_wear_rv_reducer.pdf` |
| `MMT-PAPER` | equivalent contact mechanism source | `true` | `false` | `reference/MMT_TEModeling.pdf` |
| `MMT-MATLAB` | retained harmonic linkage demonstrator | `true` | `true` | `reference/te_modeling/implementations/mmt_linkage_matlab/main.m` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `angular_position` | `measured_derived` | `true` | `true` | Phase 0 encoder coordinate contract |
| `load_torque` | `measured` | `true` | `true` | Phase 0 measured output-side torque |
| `direction` | `causal_derived` | `true` | `true` | Phase 0 explicit direction contract |
| `component_manufacturing_errors` | `unavailable` | `false` | `false` | Phase 0 and MMT parameter audit |
| `bearing_stiffness` | `unavailable` | `false` | `false` | no unit-specific stiffness registry |
| `mesh_or_interface_stiffness` | `offline_oracle_only` | `false` | `false` | source equations only; absent from measured dataset |
| `contact_clearance` | `unavailable` | `false` | `false` | no unit-specific clearance metrology |
| `contact_force` | `offline_oracle_only` | `false` | `false` | requires contact model or instrumentation |
| `normalized_load_share` | `offline_oracle_only` | `false` | `false` | no measured per-contact force distribution |
| `active_contact_state` | `unavailable` | `false` | `false` | no validated causal contact-state reconstruction |
| `trusted_contact_simulator_output` | `unavailable` | `false` | `false` | papers and demonstrator exist but no validated local contact solver |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-K1` | `synthetic_oracle_only` | `false` | Positive stiffness is a valid synthetic constraint, but no unit-specific mesh stiffness or independently observed elastic contact state exists. |
| `PINN-K2` | `synthetic_oracle_only` | `false` | Non-penetration can be unit-tested synthetically, while clearance, geometry, and active-contact state are unavailable on real samples. |
| `PINN-K3` | `synthetic_oracle_only` | `false` | Smooth complementarity is differentiable, but its gap and force variables have no independent local observations. |
| `PINN-K4` | `synthetic_oracle_only` | `false` | The load-share sum can be tested against synthetic force partitions, but the repository does not measure individual contact forces. |
| `PINN-K5` | `synthetic_oracle_only` | `false` | The references support future oracle construction, but no validated repository contact solver currently produces paired oracle targets. |
| `PINN-K6` | `blocked_by_data_contract` | `false` | Neither a trusted simulation population nor measured contact-state labels exist, leaving the latent state unidentifiable from TE alone. |

## Key Findings

- All six required source and implementation paths are present.
- Basic angle, torque, and direction inputs are causal.
- Unit-specific geometry, stiffness, clearance, force, and contact state are absent.
- The retained MMT MATLAB demonstrator is not a validated condition-varying contact solver.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase8: true`

Next: Phase 8, Energy, Friction, And Efficiency PINNs.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase7_contact_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase7_contact_portfolio_audit.yaml
```
