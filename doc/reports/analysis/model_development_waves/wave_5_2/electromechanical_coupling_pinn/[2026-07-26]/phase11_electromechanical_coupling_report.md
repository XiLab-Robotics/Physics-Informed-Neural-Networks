# Phase 11 Electromechanical Coupling PINNs Report

## Decision

Electromechanical PINNs are not identifiable from the current TE dataset because synchronized motor-current, drive-state, electrical-power, sideband, health-label, and latency channels are absent.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `E-ELECTROMECHANICAL` | PMSM, reducer dynamics, and current-sideband source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2026_e_electromechanical_coupling_fault_diagnosis_rv_reducer.pdf` |
| `MECHANICS-SYNTHESIS` | electromechanical implementation and observability synthesis | `true` | `false` | `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md` |
| `DATASET-SUMMARY` | verified local measurement schema | `true` | `false` | `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `mechanical_speed_torque_angle` | `measured` | `true` | `true` | raw encoder and load-torque channels |
| `synchronized_motor_current` | `unavailable` | `false` | `false` | absent from the verified dataset schema |
| `drive_voltage_and_switching_state` | `unavailable` | `false` | `false` | no synchronized drive-state channel |
| `electrical_input_power` | `unavailable` | `false` | `false` | current and voltage are both absent |
| `current_frequency_sidebands` | `unavailable` | `false` | `false` | paper evidence is not a local synchronized observation |
| `fault_or_health_label` | `unavailable` | `false` | `false` | no healthy-fault state contract |
| `synchronized_sensor_latency` | `unavailable` | `false` | `false` | no cross-domain timestamp or latency calibration |
| `synthetic_electromechanical_oracle` | `synthetic_oracle_only` | `false` | `false` | coupled PMSM and reducer equations can be tested synthetically |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-M1` | `blocked_by_data_contract` | `false` | Synchronized motor current and locally observed sidebands are absent. |
| `PINN-M2` | `synthetic_oracle_only` | `false` | Mechanical states exist, but electrical input and drive states do not. |
| `PINN-M3` | `blocked_by_data_contract` | `false` | Fault or health labels and synchronized electrical channels are absent. |
| `PINN-M4` | `synthetic_oracle_only` | `false` | Observer equations can be tested synthetically but not identified locally. |

## Key Findings

- All three electromechanical evidence paths are present.
- Mechanical speed, torque, and angle do not close an electrical balance.
- Paper-reported current sidebands are not local measured features.
- TwinCAT acquisition must be extended before this branch can activate.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase12: true`

Next: Phase 12, Hybrid Analytical And Learned Residual PINNs.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase11_electromechanical_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase11_electromechanical_portfolio_audit.yaml
```
