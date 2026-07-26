# Phase 4 Hysteresis, Friction, And Memory Feasibility Gate

## Overview

Phase 4 evaluates whether the repository contains the ordered, causal
state-history evidence required to support hysteresis-, friction-, and
memory-informed PINN formulations. The phase starts with a source-data audit
and does not authorize a training campaign unless real chronological
trajectories, repeated reversal cycles, warm-up state, and deterministic state
initialization can be established.

The audit covers the `PINN-Y1` through `PINN-Y6` portfolio defined by the
canonical full-PINN roadmap:

- Bouc-Wen state residual;
- rolling-friction hysteresis residual;
- rate-independent play or stop operator;
- temperature- and load-conditioned hysteresis;
- white-box hysteresis state plus learned residual;
- matched-history NARX or GRU comparator.

This technical document is automatically approved under the user's standing
approval recorded on 2026-07-26 and valid through 2026-07-26 22:37:56
Europe/Rome.

## Technical Approach

1. Build a deterministic inventory of the available polished and simplified
   source files, their schemas, timestamp-like fields, angular coordinates,
   direction labels, condition metadata, and file-level ordering evidence.
2. Test whether rows inside each curve provide a usable causal sequence and
   distinguish angular sampling order from experiment-level acquisition
   chronology.
3. Search for condition repeats, paired forward/backward measurements,
   within-file direction reversals, between-file reversal sequences, minor and
   major loops, warm-up segments, dwell periods, and reset markers.
4. Audit whether torque, speed, temperature, angular position, angular
   velocity, and TE are measured causally or only reconstructed from target or
   post-processed data.
5. Reconcile the new evidence with the Phase 0 data contract and the completed
   Wave 4.4 latent-state campaign without treating model hidden state as proof
   of physical hysteresis observability.
6. Classify each candidate formulation as:
   `real_data_trainable`, `synthetic_oracle_only`,
   `offline_oracle_only`, or `blocked_by_data_contract`.
7. Produce machine-readable CSV and YAML evidence plus a canonical Markdown
   decision report. If the exit gate fails, close Phase 4 as a valid
   feasibility result without preparing or running training.

The audit is read-only with respect to source datasets. Any generated outputs
are derived inventories and decisions stored under the Phase 4 analysis and
validation namespaces.

## Involved Components

- `data/polished_dataset/`
- `data/simplified_dataset/`
- `output/analysis/pinn_program_foundations/`
- `output/analysis/pinn_program_hysteresis/`
- `scripts/analysis/pinn_program_hysteresis/`
- `config/analysis/pinn_program_hysteresis/`
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/full_pinn_theory_validation_test_roadmap.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/hysteresis_friction_memory_pinn/[2026-07-26]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `site/`

No subagent is planned for this phase.

## Implementation Steps

1. Inspect the source schemas, Phase 0 contracts, reference synthesis, and
   Wave 4.4 evidence.
2. Implement a persistent Phase 4 chronology and state-observability audit.
3. Generate per-file and per-condition evidence for chronology, repeats,
   reversals, loops, warm-up, reset, and causal signal availability.
4. Validate the generated evidence against explicit row-count, schema, and
   decision-consistency checks.
5. Classify `PINN-Y1` through `PINN-Y6` using the four-lane feasibility
   taxonomy.
6. Decide whether the Phase 4 exit gate permits a real-data campaign.
7. Update the canonical roadmap, backlog, ledger, master summary,
   documentation portal, and user guide with the evidence-backed decision.
8. Run Python compilation, YAML validation, Markdown warning checks,
   markdownlint, `git diff --check`, and a warning-free Sphinx build.
9. Check staged file sizes and create the dedicated Phase 4 Git commit.
