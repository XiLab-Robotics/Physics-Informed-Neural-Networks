# Phase 5 Bidirectional TE, Backlash, And Lost-Motion Gate

## Overview

Phase 5 evaluates which bidirectional transmission-error relations can become
real full-PINN constraints without deriving physical inputs or latent
component errors from the measured TE target. The phase keeps the `Fw`, `Bw`,
and global surfaces distinct and tests the `PINN-B1` through `PINN-B5`
portfolio defined by the canonical full-PINN roadmap:

- separate `Fw` and `Bw` heads with a shared periodic trunk;
- a forward-reverse compatibility loss;
- a global lost-motion latent variable;
- a backlash dead-zone or smooth complementarity residual;
- a direction-transition state model.

The starting point is a deterministic paired-condition audit over the
canonical `969` operating conditions. A training campaign is prepared only if
the audit identifies a compatibility law whose inputs are causal, whose
parameters are identifiable on training data, and whose validation does not
require target-derived component errors.

This technical document is automatically approved under the user's standing
document approval recorded on 2026-07-26 and valid through 2026-07-27 12:50
Europe/Rome. Training, protected-file changes, and the Phase 5 commit are also
covered by the earlier general approval through 2026-07-26 22:37:56
Europe/Rome.

## Technical Approach

1. Pair every canonical `Fw` and `Bw` curve by operating condition and verify
   split, condition metadata, angular coverage, sample count, and direction
   conventions.
2. Align paired curves only through deterministic angular-coordinate
   operations. Any target-informed phase or offset estimator is restricted to
   offline audit evidence and may not become a training or inference input.
3. Quantify paired raw TE, mean-centered shape, mean offset, amplitude,
   harmonic phase, slope, continuity, zero-crossing, and reversal-gap
   behavior on separate train, validation, and test surfaces.
4. Distinguish three concepts:
   empirical `Fw`/`Bw` curve difference, a globally observable lost-motion
   proxy, and a mechanism-backed backlash state. The first does not prove the
   other two.
5. Audit every required quantity against the Phase 0 causal-data contract and
   the Phase 4 reversal evidence.
6. Classify each candidate as `real_data_trainable`,
   `offline_oracle_only`, `synthetic_oracle_only`, or
   `blocked_by_data_contract`.
7. If a reduced compatibility law passes source fidelity, dimensional,
   observability, identifiability, and leakage checks, create the required
   campaign plan, YAML matrix, local and `-Remote` launcher, persistent state,
   and matched controls before training.
8. If no law passes, close Phase 5 as a valid feasibility result and preserve
   the measured paired-surface evidence for later multi-task work without
   promoting a false backlash residual.

## Involved Components

- `data/polished_dataset/`
- `data/simplified_dataset/`
- `output/analysis/pinn_program_foundations/`
- `output/analysis/pinn_program_hysteresis/`
- `output/analysis/pinn_program_bidirectional/`
- `scripts/analysis/pinn_program_bidirectional/`
- `config/analysis/pinn_program_bidirectional/`
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `reference/te_modeling/theoretical_mechanics/kinematics_and_transmission_error/2024_wang_bidirectional_drive_te_positioning_accuracy_cycloid_reducer.pdf`
- `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2025_xu_hysteresis_torsional_rigidity_lost_motion_rv_reducer.pdf`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/full_pinn_theory_validation_test_roadmap.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/bidirectional_backlash_lost_motion_pinn/[2026-07-26]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `site/`

No subagent is planned for this phase.

## Implementation Steps

1. Inspect the source references, Phase 0 contracts, Phase 4 evidence, and the
   real paired `Fw`/`Bw` file schemas.
2. Implement a persistent Phase 5 paired-condition and identifiability audit.
3. Generate condition-level and split-level evidence for raw, centered,
   offset, harmonic, phase, slope, continuity, zero-crossing, and gap
   behavior.
4. Validate row counts, pairing, split isolation, deterministic results, and
   the absence of target-derived model inputs.
5. Classify `PINN-B1` through `PINN-B5` under the four-lane feasibility
   taxonomy.
6. Decide whether the Phase 5 exit gate authorizes a reduced real-data PINN
   campaign.
7. If authorized, prepare and validate the campaign contract before execution;
   otherwise record a non-training closeout.
8. Update the roadmap, backlog, ledger, master summary, user guide, and
   documentation portal with the evidence-backed decision.
9. Run Python compilation, YAML validation, Markdown warning checks,
   markdownlint, `git diff --check`, and a warning-free Sphinx build.
10. Check staged file sizes and create the dedicated Phase 5 Git commit.
