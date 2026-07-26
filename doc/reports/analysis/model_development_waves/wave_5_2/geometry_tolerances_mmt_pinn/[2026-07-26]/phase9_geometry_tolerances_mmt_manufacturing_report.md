# Phase 9 Geometry, Tolerances, MMT, And Manufacturing Priors Report

## Decision

Geometry and manufacturing knowledge is retained for synthetic recovery, sensitivity, and oracle work. No unit-specific metrology, multi-instance population, or validated synthetic-to-real transfer closes the real-data gate.

No training campaign was prepared because no formulation is both
`real_data_trainable` and full-PINN eligible.

## Evidence Files

| ID | Role | Exists | Executable oracle | Path |
| --- | --- | --- | --- | --- |
| `MMT-PAPER` | paper-faithful equivalent-mechanism source | `true` | `false` | `reference/MMT_TEModeling.pdf` |
| `MMT-MATLAB` | harmonic linkage synthetic demonstrator | `true` | `true` | `reference/te_modeling/implementations/mmt_linkage_matlab/main.m` |
| `JIN-TOLERANCE` | part-tolerance virtual prototype source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2025_jin_part_tolerances_virtual_prototype_rv40e.pdf` |
| `CHEN-GEOMETRY` | geometric-error and wear source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_chen_predictive_te_geometric_errors_wear_rv_reducer.pdf` |
| `WANG-FEA` | FEA population and surrogate source | `true` | `false` | `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_wang_ensemble_learning_te_prediction_optimization_rv_reducer.pdf` |
| `MMT-SUMMARY` | current MMT blocker and reusable oracle decision | `true` | `false` | `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md` |

## Required Quantities

| Quantity | Availability | Causal runtime | Online input | Evidence |
| --- | --- | --- | --- | --- |
| `nominal_reducer_geometry` | `known_constant` | `true` | `true` | repository geometry constants and reduction ratio |
| `unit_specific_component_errors` | `unavailable` | `false` | `false` | no metrology for the tested reducer |
| `unit_specific_tolerances` | `unavailable` | `false` | `false` | no as-built tolerance record |
| `reducer_instance_identity` | `unavailable` | `false` | `false` | canonical dataset contains one unidentified reducer instance |
| `condition_varying_mmt_errors` | `unavailable` | `false` | `false` | completed MMT parameter blocker |
| `validated_fea_population` | `unavailable` | `false` | `false` | source population is not shipped as repository data |
| `synthetic_geometry_oracle` | `synthetic_oracle_only` | `false` | `false` | equations and MATLAB demonstrator support bounded synthetic tests |
| `synthetic_to_real_transfer_protocol` | `unavailable` | `false` | `false` | no validation against unit-specific metrology |

## Candidate Decisions

| Candidate | Feasibility | Full PINN eligible | Decision basis |
| --- | --- | --- | --- |
| `PINN-G1` | `synthetic_oracle_only` | `false` | Manufacturing priors can be tested synthetically but are not unit-specific. |
| `PINN-G2` | `synthetic_oracle_only` | `false` | Source studies motivate a surrogate, but their simulation population is not available locally. |
| `PINN-G3` | `synthetic_oracle_only` | `false` | The retained MMT equation chain supports synthetic tests without claiming local identification. |
| `PINN-G4` | `blocked_by_data_contract` | `false` | Condition-varying component errors and causal contact states remain unavailable. |
| `PINN-G5` | `blocked_by_data_contract` | `false` | One unidentified reducer instance cannot identify a hierarchical geometry latent. |

## Key Findings

- All six MMT, tolerance, geometry, FEA, and synthesis paths are present.
- Nominal constants are available but are condition-invariant.
- Unit-specific errors, tolerances, instance identity, and FEA populations are absent.
- Paper-faithful MMT remains deferred while synthetic MMT tests remain allowed.

## Exit Gate

- `status: failed_no_training_authorized`
- `full_pinn_training_authorized: false`
- `physical_residual_promoted: false`
- `advance_to_phase10: true`

Next: Phase 10, Wear And Degradation PINNs.

## Reproduction

```powershell
python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase9_geometry_portfolio_audit.yaml
python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `
  --config config/analysis/pinn_program_portfolios/phase9_geometry_portfolio_audit.yaml
```
