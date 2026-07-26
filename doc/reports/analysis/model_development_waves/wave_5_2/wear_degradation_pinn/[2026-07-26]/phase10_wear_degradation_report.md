# Phase 10 Wear And Degradation PINNs Report

## Decision

Wear laws remain synthetic research because the repository has no longitudinal reducer identity, acquisition chronology, load-cycle count, wear measurement, lubrication state, or maintenance-event contract.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `CHEN-WEAR` | Archard wear and contact progression source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_chen_predictive_te_geometric_errors_wear_rv_reducer.pdf` |
| `MECHANICS-SYNTHESIS` | wear and geometry implementation synthesis | `true` | `false` | `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md` |
| `DATASET-SUMMARY` | dataset chronology and identity contract | `true` | `false` | `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `torque_speed_temperature` | `measured` | `true` | `true` | Phase 0 operating inputs |
| `reducer_instance_identity` | `unavailable` | `false` | `false` | no multi-unit identity contract |
| `acquisition_session_time` | `unavailable` | `false` | `false` | filesystem timestamps are not acquisition evidence |
| `cumulative_load_cycles` | `unavailable` | `false` | `false` | no lifecycle counter |
| `lubrication_state` | `unavailable` | `false` | `false` | temperature is not a unique lubrication label |
| `direct_wear_measurement` | `unavailable` | `false` | `false` | no inspection or metrology channel |
| `maintenance_event` | `unavailable` | `false` | `false` | no reset or service registry |
| `synthetic_wear_oracle` | `synthetic_oracle_only` | `false` | `false` | Archard-inspired progression can be tested synthetically |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-W1` | `blocked_by_data_contract` | `false` | Cumulative load cycles and session chronology are unavailable. |
| `PINN-W2` | `synthetic_oracle_only` | `false` | Archard progression is testable synthetically but not identifiable locally. |
| `PINN-W3` | `synthetic_oracle_only` | `false` | Monotonicity is a synthetic prior without longitudinal health labels. |
| `PINN-W4` | `synthetic_oracle_only` | `false` | A future contact simulator can supply oracle data; none is validated locally. |
| `PINN-W5` | `blocked_by_data_contract` | `false` | Reducer identity, ordered sessions, and maintenance events are absent. |

## Key Findings

- All three wear and provenance evidence paths are present.
- Operating inputs do not establish lifecycle chronology.
- Filesystem modification time is not acquisition evidence.
- Temperature and TE drift cannot be relabeled as degradation.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase11: true`

Next: Phase 11, Electromechanical Coupling PINNs.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase10_wear_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase10_wear_portfolio_audit.yaml
```
