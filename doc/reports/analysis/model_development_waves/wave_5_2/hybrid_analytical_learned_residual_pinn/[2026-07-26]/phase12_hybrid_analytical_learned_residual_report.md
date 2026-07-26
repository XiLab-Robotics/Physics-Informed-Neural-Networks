# Phase 12 Hybrid Analytical And Learned Residual PINNs Report

## Decision

Five hybrid architectures are empirically trainable, but none qualifies as a full PINN because Phases 2 through 11 promoted no validated physical residual and the Phase 1 anchor remains a semi-analytical predictor.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `PHASE1-BENCHMARK` | semi-analytical Polynomial-Fourier benchmark | `true` | `true` | `doc/reports/analysis/model_development_waves/wave_5_2/polynomial_fourier_benchmark/[2026-07-25]/phase1_polynomial_fourier_analytical_benchmark_report.md` |
| `PHASE2-CLOSEOUT` | harmonic and kinematic constraint decision | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.md` |
| `PHASE3-CLOSEOUT` | compliance residual decision | `true` | `false` | `doc/reports/campaign_results/wave_5_2/2026-07-26-20-13-18_phase3_quasi_static_compliance_pinn_campaign_results_report.md` |
| `HYBRID-SYNTHESIS` | analytical plus learned compensation pattern | `true` | `false` | `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `semi_analytical_curve_component` | `measured_data_benchmarked` | `true` | `true` | Phase 1 Polynomial-Fourier implementations |
| `promoted_physical_residual` | `unavailable` | `false` | `false` | Phase 2 and Phase 3 promoted no tested residual |
| `learned_residual_target` | `target_only` | `false` | `false` | measured TE can supervise training but is not an inference input |
| `direction_specific_structure` | `available` | `true` | `true` | direction-separated common split and reference implementations |
| `temporal_history` | `available_for_windowed_models` | `true` | `true` | accepted periodic GRU contract |
| `uncertainty_evidence` | `offline_evaluation_only` | `false` | `false` | Wave 4.2 exploratory quantile results |
| `validated_physical_regime_gate` | `unavailable` | `false` | `false` | no isolated physical mechanism was promoted |
| `plc_analytical_execution_path` | `reference_implementation` | `true` | `true` | direction-specific Polynomial Fourier Series PLC implementation |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-R1` | `real_data_trainable` | `false` | Trainable as an empirical hybrid, but no promoted physical constraint survives. |
| `PINN-R2` | `real_data_trainable` | `false` | Causal temporal residuals are feasible, but the anchor is semi-analytical. |
| `PINN-R3` | `real_data_trainable` | `false` | Localization is testable, but the component is not a validated physical law. |
| `PINN-R4` | `real_data_trainable` | `false` | Uncertainty can be modeled empirically but does not supply physical consistency. |
| `PINN-R5` | `blocked_by_data_contract` | `false` | No physical regime gate passed an isolated pilot. |
| `PINN-R6` | `real_data_trainable` | `false` | Directional sharing is feasible, but the trunk remains semi-analytical. |

## Key Findings

- The Polynomial-Fourier anchor and learned residuals can be combined causally.
- Empirical trainability is not equivalent to full-PINN eligibility.
- Phase 2 and Phase 3 physical constraints failed promotion.
- A regime-gated mixture is blocked because no physical regime was validated.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase13: true`

Next: Phase 13, Cross-Formulation Tournament.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase12_hybrid_residual_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase12_hybrid_residual_portfolio_audit.yaml
```
