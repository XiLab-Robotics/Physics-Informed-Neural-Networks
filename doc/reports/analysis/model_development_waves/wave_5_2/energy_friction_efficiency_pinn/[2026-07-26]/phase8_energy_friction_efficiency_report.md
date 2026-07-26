# Phase 8 Energy, Friction, And Efficiency PINNs Report

## Decision

Output torque, speed, temperature, and direction are causal, but input power, internal force, friction loss, and efficiency are not observed. Energy inequalities remain synthetic and the balance remains offline.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `MECHANICS-SYNTHESIS` | efficiency and force-model synthesis | `true` | `false` | `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md` |
| `HYSTERESIS-SYNTHESIS` | load and temperature dependence of friction | `true` | `false` | `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md` |
| `WANG-EFFICIENCY` | nonlinear efficiency and internal loss source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2024_wang_nonlinear_transmission_efficiency_cycloid_reducer.pdf` |
| `MESMER-FRICTION` | load- and temperature-dependent friction source | `true` | `false` | `reference/te_modeling/bibliography/hysteresis_and_backlash/2023_mesmer_investigation_compensation_hysteresis_robot_joints_cycloidal_drives.pdf` |
| `ELECTROMECHANICAL` | motor-drive and mechanical power coupling source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2026_e_electromechanical_coupling_fault_diagnosis_rv_reducer.pdf` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `output_load_torque` | `measured` | `true` | `true` | Phase 0 output-side torque sensor |
| `input_speed` | `measured_derived` | `true` | `true` | Phase 0 encoder derivative |
| `oil_temperature` | `measured` | `true` | `true` | Phase 0 oil-temperature sensor |
| `direction` | `causal_derived` | `true` | `true` | Phase 0 direction contract |
| `input_motor_torque` | `unavailable` | `false` | `false` | no synchronized motor-torque channel |
| `motor_current_and_drive_state` | `unavailable` | `false` | `false` | Phase 0 signal contract |
| `input_power` | `unavailable` | `false` | `false` | input torque or electrical power is absent |
| `output_power` | `reconstructable` | `true` | `false` | output torque and ratio-scaled speed support a proxy |
| `internal_contact_force` | `offline_oracle_only` | `false` | `false` | requires contact model or force instrumentation |
| `friction_loss` | `unavailable` | `false` | `false` | torque and speed do not identify internal loss distribution |
| `transmission_efficiency` | `unavailable` | `false` | `false` | both input and output power are required |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-E1` | `synthetic_oracle_only` | `false` | Non-negative dissipation is a valid synthetic inequality, but dissipated power is not independently observed in the local dataset. |
| `PINN-E2` | `synthetic_oracle_only` | `false` | Efficiency bounds can be unit-tested, while input power and measured efficiency targets are unavailable. |
| `PINN-E3` | `blocked_by_data_contract` | `false` | Internal friction loss is not identifiable from output torque, speed, and TE without input torque, contact force, or power measurements. |
| `PINN-E4` | `blocked_by_data_contract` | `false` | Temperature is measured but is not a unique friction-loss label or internal energy state. |
| `PINN-E5` | `offline_oracle_only` | `false` | The head can be evaluated if future input-power or simulator oracles are supplied, but current output-power proxies cannot close the balance. |

## Key Findings

- All five energy and friction evidence paths are present.
- Output power is reconstructable only as a one-sided proxy.
- Input torque, electrical power, internal force, and friction loss are absent.
- Efficiency cannot be identified from output power alone.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase9: true`

Next: Phase 9, Geometry, Tolerances, MMT, And Manufacturing Priors.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase8_energy_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase8_energy_portfolio_audit.yaml
```
