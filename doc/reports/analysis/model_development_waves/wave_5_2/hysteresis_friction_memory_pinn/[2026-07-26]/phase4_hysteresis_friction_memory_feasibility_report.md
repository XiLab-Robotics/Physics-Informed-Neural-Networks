# Phase 4 Hysteresis, Friction, And Memory Feasibility Report

## Overview

Phase 4 is complete as a feasibility-first, non-training result. The
original raw files preserve one ordered forward-to-backward trajectory
per operating condition, including the unvalidated transition interval.
However, the repository does not contain repeated reversal cycles,
minor-loop labels, controlled warm-up labels, or a deterministic state
reset marker. The Phase 4 real-data training gate therefore fails.

No Phase 4 physical residual is promoted and no training campaign is
prepared. The raw trajectories remain useful as offline reversal
oracles, while Bouc-Wen, rolling-friction, play/stop, and white-box
state laws remain available for synthetic-oracle verification.

## Source Inventory

| Evidence | Value |
| --- | ---: |
| Raw CSV files | 975 |
| Canonical raw conditions | 969 |
| Ignored duplicate or connection files | 6 |
| Polished directional files | 1938 |
| Simplified files | 969 |

## Chronology And State Evidence

| Check | Result |
| --- | ---: |
| Raw trajectories with ordered direction windows | 969 |
| Raw trajectories with at least one physical reversal | 969 |
| Raw trajectories with repeated reversals | 0 |
| Raw trajectories with repeated major loops | 0 |
| Raw trajectories with minor-loop markers | 0 |
| Raw trajectories with controlled warm-up labels | 0 |
| Raw trajectories with deterministic reset markers | 0 |
| Offline reversal-oracle trajectories | 969 |

The raw row order plus the documented `0.25 ms` sample interval is
sufficient to reconstruct an offline time axis. Filesystem modification
times are explicitly excluded as acquisition chronology. The forward
and backward validity windows are each contiguous, with a transition
interval between them, but each condition supplies only one direction
pair rather than repeated major or minor loops.

## Dataset And Prior-Model Boundary

| Surface | Pairing | Reversal preserved | Repeated cycles | Boundary |
| --- | --- | --- | --- | --- |
| `original_dataset` | same_file_validity_windows | yes | no | `offline_oracle_only` |
| `polished_dataset` | separate_files_per_direction | no | no | `blocked_by_data_contract` |
| `simplified_dataset` | paired_columns_sorted_by_angle | no | no | `blocked_by_data_contract` |
| `wave4_4_training_view` | independent_direction_windows | no | no | `exploratory_comparator_only` |

Wave 4.4 demonstrated that short within-direction angular history can
be encoded by GRU or causal TCN models. It did not preserve the raw
forward-to-backward transition and therefore does not establish an
identified physical hysteresis state.

## Formulation Decisions

| Formulation | Model | Decision | Real-data training |
| --- | --- | --- | --- |
| `PINN-Y1` | Bouc-Wen state residual | `synthetic_oracle_only` | no |
| `PINN-Y2` | rolling-friction hysteresis residual | `synthetic_oracle_only` | no |
| `PINN-Y3` | rate-independent play or stop operator | `synthetic_oracle_only` | no |
| `PINN-Y4` | temperature- and load-conditioned hysteresis | `blocked_by_data_contract` | no |
| `PINN-Y5` | white-box hysteresis state plus learned residual | `synthetic_oracle_only` | no |
| `PINN-Y6` | matched-history NARX or GRU comparator | `offline_oracle_only` | no |

### Decision Interpretation

- `PINN-Y1`, `PINN-Y2`, `PINN-Y3`, and `PINN-Y5` remain eligible
  for equation-level and synthetic-oracle tests only.
- `PINN-Y4` is blocked because condition variation cannot be separated
  from unknown hysteresis initialization without matched repeats.
- `PINN-Y6` may be evaluated as an offline reconstructed-trajectory
  comparator, but not promoted as a real-data hysteresis model.

## Exit Gate

**Status: `failed_no_training_authorized`.**

| Requirement | Passed |
| --- | --- |
| `all_canonical_raw_files_scanned` | yes |
| `ordered_acquisition_available` | yes |
| `single_reversal_transition_available` | yes |
| `repeated_reversal_cycles_available` | no |
| `repeated_major_and_minor_loops_available` | no |
| `controlled_warmup_state_available` | no |
| `deterministic_reset_evidence_available` | no |
| `stable_causal_state_evolution_testable` | no |

The mandatory repeated-reversal and stable-state requirements are not
met. Phase 4 closes without training and the sixteen-phase roadmap
advances to Phase 5, where bidirectional TE and lost-motion laws can
use the existing paired `Fw` and `Bw` surfaces without pretending
that the missing transition-state labels are available.

## Reproducibility

- Configuration: `config/analysis/pinn_program_hysteresis/phase4_hysteresis_feasibility_audit.yaml`
- Raw trajectory audit: `output/analysis/pinn_program_hysteresis/phase4_raw_trajectory_audit.csv`
- Dataset contract audit: `output/analysis/pinn_program_hysteresis/phase4_dataset_contract_audit.csv`
- Formulation decisions: `output/analysis/pinn_program_hysteresis/phase4_formulation_feasibility.csv`
- Machine-readable summary: `output/analysis/pinn_program_hysteresis/phase4_hysteresis_feasibility_audit.yaml`
