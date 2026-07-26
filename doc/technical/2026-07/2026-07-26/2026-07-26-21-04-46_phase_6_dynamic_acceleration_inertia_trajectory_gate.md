# Phase 6 Dynamic Acceleration, Inertia, And Trajectory Gate

## Overview

Phase 6 evaluates whether the repository can support a dynamic full-PINN
residual based on angular acceleration, load inertia, or causal trajectory
state. The source literature identifies acceleration and inertia as dominant
drivers of variable-speed transmission error, but the local dataset was
designed primarily around steady directional validity windows. The phase must
therefore separate physically meaningful dynamics from numerical derivative
noise, encoder discontinuities, direction-transition transients, and
unobserved rig parameters.

The audit covers the `PINN-D1` through `PINN-D5` portfolio:

- acceleration-conditioned TE residual;
- reduced inertia and acceleration balance;
- causal state-space dynamic residual;
- periodic analytical component plus temporal dynamic residual;
- learned latent inertia with a bounded prior.

This technical document is automatically approved under the user's standing
document approval through 2026-07-27 12:50 Europe/Rome. Training,
protected-file changes, and the Phase 6 commit remain covered by the earlier
general approval through 2026-07-26 22:37:56 Europe/Rome.

## Technical Approach

1. Reuse the exact `969` canonical raw-condition inventory and common
   train/validation/test assignment established in Phases 0 and 4.
2. Reconstruct input-side speed and acceleration from cumulative encoder angle
   using strictly causal backward differences at the documented `0.25 ms`
   sample interval.
3. Quantify raw one-step derivative noise, robust outliers, and the effect of
   causal moving-average windows without using centered or future-looking
   filters.
4. Keep forward-valid, backward-valid, inter-window transition, pre-valid, and
   post-valid regions separate. Test whether selected TE curves are effectively
   constant-speed null cases and whether meaningful acceleration excitation is
   confined outside the current training target windows.
5. Audit load inertia, commanded drive law, motor current, and synchronized
   trajectory labels against the Phase 0 causal-data contract.
6. Distinguish an observable acceleration signal from an identifiable dynamic
   TE law. Acceleration alone cannot identify an inertia-weighted balance when
   inertia and contact state are unavailable.
7. Classify each candidate as `real_data_trainable`,
   `offline_oracle_only`, `synthetic_oracle_only`, or
   `blocked_by_data_contract`.
8. Prepare a training campaign only if a source-backed, leakage-safe dynamic
   residual survives the constant-speed null, derivative-noise, excitation,
   and missing-inertia gates.

## Involved Components

- `data/original_dataset/`
- `data/polished_dataset/`
- `output/analysis/pinn_program_foundations/`
- `output/analysis/pinn_program_hysteresis/`
- `output/analysis/pinn_program_dynamics/`
- `scripts/analysis/pinn_program_dynamics/`
- `config/analysis/pinn_program_dynamics/`
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2025_xu_dynamic_transmission_accuracy_variable_speed_rv_reducer.pdf`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/full_pinn_theory_validation_test_roadmap.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/dynamic_acceleration_inertia_pinn/[2026-07-26]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `site/`

No subagent is planned for this phase.

## Implementation Steps

1. Inspect the dynamic references, raw schema, Phase 0 signal contract, and
   Phase 4 trajectory inventory.
2. Implement a persistent raw-trajectory dynamic observability audit.
3. Generate condition- and split-level metrics for causal speed,
   acceleration, outliers, filter sensitivity, validity-window excitation, and
   transition excitation.
4. Validate all condition counts, split isolation, region masks, causal
   derivative definitions, and missing-signal decisions.
5. Classify `PINN-D1` through `PINN-D5` under the four-lane feasibility
   taxonomy.
6. Decide whether the Phase 6 exit gate authorizes a dynamic PINN campaign.
7. If authorized, prepare the required campaign plan and launcher contract;
   otherwise record a non-training closeout.
8. Update the roadmap, backlog, ledger, master summary, user guide, and
   documentation portal.
9. Run Python compilation, YAML validation, Markdown warning checks,
   markdownlint, `git diff --check`, and a warning-free Sphinx build.
10. Check staged file sizes and create the dedicated Phase 6 Git commit.
