# Phase 13 Cross-Formulation Tournament Report

## Decision

The Phase 13 roster contains zero isolated full-PINN-eligible candidates, so the correct tournament result is no contest and no training campaign.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `PHASE0` | common contract | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/phase0_pinn_program_foundations_report.md` |
| `PHASE1` | semi-analytical benchmark | `true` | `true` | `doc/reports/analysis/model_development_waves/wave_5_2/polynomial_fourier_benchmark/[2026-07-25]/phase1_polynomial_fourier_analytical_benchmark_report.md` |
| `PHASE2` | harmonic decision | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.md` |
| `PHASE3` | compliance decision | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-20-13-18_phase3_quasi_static_compliance_pinn_campaign_results_report.md` |
| `PHASE4` | hysteresis decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/hysteresis_friction_memory_pinn/[2026-07-26]/phase4_hysteresis_friction_memory_feasibility_report.md` |
| `PHASE5` | bidirectional decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/bidirectional_backlash_lost_motion_pinn/[2026-07-26]/phase5_bidirectional_te_backlash_lost_motion_report.md` |
| `PHASE6` | dynamics decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/dynamic_acceleration_inertia_pinn/[2026-07-26]/phase6_dynamic_acceleration_inertia_trajectory_report.md` |
| `PHASE7` | contact decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/contact_mesh_stiffness_load_sharing_pinn/[2026-07-26]/phase7_contact_mesh_stiffness_load_sharing_report.md` |
| `PHASE8` | energy decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/energy_friction_efficiency_pinn/[2026-07-26]/phase8_energy_friction_efficiency_report.md` |
| `PHASE9` | geometry decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/geometry_tolerances_mmt_pinn/[2026-07-26]/phase9_geometry_tolerances_mmt_manufacturing_report.md` |
| `PHASE10` | wear decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/wear_degradation_pinn/[2026-07-26]/phase10_wear_degradation_report.md` |
| `PHASE11` | electromechanical decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/electromechanical_coupling_pinn/[2026-07-26]/phase11_electromechanical_coupling_report.md` |
| `PHASE12` | hybrid decision | `true` | `false` | `doc/reports/analysis/model_development_waves/wave_5_2/hybrid_analytical_learned_residual_pinn/[2026-07-26]/phase12_hybrid_analytical_learned_residual_report.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `common_split_contract` | `available` | `false` | `false` | Phase 0 |
| `curve_first_promotion` | `zero_candidates` | `false` | `false` | Phase 2 and Phase 3 negative results |
| `isolated_full_pinn_candidate` | `zero_candidates` | `false` | `false` | Phases 2 through 12 |
| `semi_analytical_benchmark` | `available` | `true` | `true` | Phase 1 |
| `empirical_comparators` | `available` | `true` | `true` | Phases 5, 6, and 12 |
| `offline_oracles` | `available` | `false` | `false` | mechanism-specific phase reports |
| `synthetic_oracles` | `available` | `false` | `false` | Phases 4 and 7 through 11 |
| `tournament_training_roster` | `empty` | `false` | `false` | zero eligible isolated candidates |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `TOUR-P1` | `real_data_trainable` | `false` | Benchmark is useful but not a governing-law PINN. |
| `TOUR-P2` | `offline_oracle_only` | `false` | Tested constraints failed curve-first promotion. |
| `TOUR-P3` | `offline_oracle_only` | `false` | Compliance residual failed repeatability and joint gates. |
| `TOUR-P4` | `offline_oracle_only` | `false` | Current data support reversal comparison but not repeated-loop training. |
| `TOUR-P5` | `real_data_trainable` | `false` | Empirical paired comparator exists without identifiable physical state. |
| `TOUR-P6` | `real_data_trainable` | `false` | Empirical dynamic comparator exists without identifiable inertia residual. |
| `TOUR-P7` | `synthetic_oracle_only` | `false` | Contact states and parameters are unavailable. |
| `TOUR-P8` | `synthetic_oracle_only` | `false` | Input power and internal loss are unavailable. |
| `TOUR-P9` | `synthetic_oracle_only` | `false` | Unit metrology and causal MMT parameters are unavailable. |
| `TOUR-P10` | `synthetic_oracle_only` | `false` | Longitudinal lifecycle evidence is unavailable. |
| `TOUR-P11` | `synthetic_oracle_only` | `false` | Synchronized electrical evidence is unavailable. |
| `TOUR-P12` | `real_data_trainable` | `false` | Empirical hybrids contain no promoted physical residual. |

## Key Findings

- All thirteen phase-evidence files exist.
- Zero isolated formulations passed the full-PINN entry gate.
- Semi-analytical and empirical candidates remain valid reference branches.
- Rejected, offline, synthetic, deferred, and blocked mechanisms were not ranked as winners.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase14: true`

Next: Phase 14, Integrated Multi-Physics PINNs.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase13_cross_formulation_tournament_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase13_cross_formulation_tournament_audit.yaml
```
