# Phase 7 Contact, Mesh Stiffness, And Load-Sharing Gate

## Overview

Phase 7 evaluates whether contact, mesh-stiffness, non-penetration,
complementarity, and load-sharing relations can become deployable full-PINN
constraints on the current TE dataset. The available references provide rich
contact mechanics and synthetic-model evidence, but the local signal contract
does not directly expose clearances, interface stiffnesses, contact forces,
load shares, or unit-specific manufacturing errors.

The phase covers `PINN-K1` through `PINN-K6` and explicitly preserves
synthetic-oracle work even when real-data training is blocked. It also
introduces a reusable, configuration-driven portfolio feasibility audit for
the later source-heavy PINN phases.

This technical document is automatically approved under the user's standing
document approval through 2026-07-27 12:50 Europe/Rome. Training,
protected-file changes, and the Phase 7 commit remain covered by the earlier
general approval through 2026-07-26 22:37:56 Europe/Rome.

## Technical Approach

1. Verify every cited contact-mechanics source and repository implementation
   path.
2. Build a required-quantity matrix for geometry, component errors,
   clearances, bearing and mesh stiffness, contact forces, load shares, and
   simulator outputs.
3. Cross-check each quantity against the Phase 0 causal signal contract and
   subsequent MMT, compliance, bidirectional, and dynamic negative evidence.
4. Distinguish:
   source equations, independently measured quantities, offline simulator
   oracles, synthetic unit tests, and unavailable deployment inputs.
5. Classify `PINN-K1` through `PINN-K6` as `real_data_trainable`,
   `offline_oracle_only`, `synthetic_oracle_only`, or
   `blocked_by_data_contract`.
6. Require any real-data contact residual to have independently available
   state and parameters; TE target fitting may not manufacture contact forces,
   clearances, stiffnesses, or load shares.
7. Produce a reusable YAML-driven feasibility builder and validator so later
   theory branches retain the same evidence and decision schema.
8. Prepare training only if at least one contact candidate is both full-PINN
   eligible and real-data trainable.

## Involved Components

- `config/analysis/pinn_program_portfolios/`
- `scripts/analysis/pinn_program_portfolios/`
- `output/analysis/pinn_program_contact/`
- `output/analysis/pinn_program_foundations/`
- `output/analysis/pinn_program_hysteresis/`
- `output/analysis/pinn_program_bidirectional/`
- `output/analysis/pinn_program_dynamics/`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md`
- `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2025_xu_hysteresis_torsional_rigidity_lost_motion_rv_reducer.pdf`
- `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_chen_predictive_te_geometric_errors_wear_rv_reducer.pdf`
- `reference/MMT_TEModeling.pdf`
- `doc/reports/analysis/model_development_waves/wave_5_2/contact_mesh_stiffness_load_sharing_pinn/[2026-07-26]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `site/`

No subagent is planned for this phase.

## Implementation Steps

1. Create the Phase 7 portfolio YAML with references, required quantities,
   formulation decisions, and exit rules.
2. Implement the reusable portfolio feasibility builder and validator.
3. Generate reference, quantity, formulation, YAML, and Markdown artifacts.
4. Validate source existence, evidence paths, decision taxonomy, and
   training-gate consistency.
5. Record which contact laws remain synthetic or offline oracles and which are
   blocked.
6. Update the roadmap, backlog, ledger, master summary, user guide, and
   documentation portal.
7. Run Python compilation, YAML validation, Markdown warning checks,
   markdownlint, `git diff --check`, and a warning-free Sphinx build.
8. Check staged file sizes and create the dedicated Phase 7 Git commit.
