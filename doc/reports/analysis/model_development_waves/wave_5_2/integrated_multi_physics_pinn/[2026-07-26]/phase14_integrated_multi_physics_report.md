# Phase 14 Integrated Multi-Physics PINNs Report

## Decision

Integrated multi-physics training is not authorized because zero promoted physical components are available against a minimum requirement of two.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `PHASE13-ROSTER` | authoritative isolated-formulation roster | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/cross_formulation_tournament/[2026-07-26]/phase13_cross_formulation_tournament_report.md` |
| `PHASE2-CLOSEOUT` | rejected periodic and harmonic physical constraints | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.md` |
| `PHASE3-CLOSEOUT` | rejected compliance physical constraints | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-20-13-18_phase3_quasi_static_compliance_pinn_campaign_results_report.md` |
| `PHASE12-HYBRID` | empirical hybrid qualification boundary | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/hybrid_analytical_learned_residual_pinn/[2026-07-26]/phase12_hybrid_analytical_learned_residual_report.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `promoted_physical_component_count` | `zero` | `false` | `false` | Phase 13 roster |
| `minimum_required_component_count` | `two` | `false` | `false` | Phase 14 contract |
| `shared_variable_contract` | `unavailable` | `false` | `false` | no eligible component pair |
| `unit_and_scale_compatibility` | `untestable` | `false` | `false` | no eligible component pair |
| `gradient_and_loss_compatibility` | `untestable` | `false` | `false` | no eligible component pair |
| `joint_identifiability` | `untestable` | `false` | `false` | no eligible component pair |
| `complete_causal_input_matrix` | `unavailable` | `false` | `false` | mechanism inputs remain missing |
| `integrated_twincat_path` | `unavailable` | `false` | `false` | no integrated architecture |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `INT-1` | `blocked_by_data_contract` | `false` | Both tested physical constraints failed promotion. |
| `INT-2` | `blocked_by_data_contract` | `false` | Periodic constraint was rejected and hysteresis lacks repeated loops. |
| `INT-3` | `blocked_by_data_contract` | `false` | Periodic constraint was rejected and dynamic inertia is unidentifiable. |
| `INT-4` | `blocked_by_data_contract` | `false` | Neither isolated physical component passed promotion. |
| `INT-5` | `blocked_by_data_contract` | `false` | Compliance was rejected and hysteresis is not trainable locally. |
| `INT-6` | `synthetic_oracle_only` | `false` | Contact is synthetic and dynamic state lacks identifiable excitation. |
| `INT-7` | `blocked_by_data_contract` | `false` | No validated physical component exists to wrap. |
| `INT-8` | `synthetic_oracle_only` | `false` | Both branches require unavailable longitudinal or electrical datasets. |

## Key Findings

- The authoritative Phase 13 roster contains zero eligible physical components.
- Loss and identifiability interactions cannot be tested without a valid pair.
- Empirical, rejected, and synthetic mechanisms are not integration-ready physics.
- The integration sequence remains preserved with explicit reopening conditions.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase15: true`

Next: Phase 15, Wave 6 Entry.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase14_integrated_multi_physics_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase14_integrated_multi_physics_audit.yaml
```
