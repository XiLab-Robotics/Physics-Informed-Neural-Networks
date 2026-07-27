# Wave 5.2R Stage 0 Forward Evidence Freeze

## Overview

This project implements Stage 0 of the approved `Wave 5.2R` roadmap. It will
freeze the non-training evidence contract for `polished_dataset`, setpoint
inputs, and the `Fw` surface before any new residual or physics-loss model is
implemented.

The stage will reproduce or replay the three entry baselines on the immutable
Phase 0 split:

- `PF_A_LOCAL_QUADRATIC`;
- `polished_setpoints_periodic_mlp_harmonic_Fw`;
- `polished_setpoints_periodic_gru_sequence_Fw`.

The project does not execute training. The user has authorized automatic
approval of technical documents for all sixteen `Wave 5.2R` stages, so this
document is considered approved immediately after registration.

## Technical Approach

The stage will combine a fresh, isolated rerun of the Phase 1
Polynomial-Fourier benchmark with an inference-only forward replay of the two
accepted neural references. It will avoid overwriting the prior Phase 0,
Phase 1, or Phase 2 canonical evidence.

A repository-owned freeze builder will then:

1. verify the Phase 0 split signature and eligible-condition counts;
2. select exactly the `97` eligible `Fw` test conditions;
3. verify candidate provenance and source hashes;
4. aggregate raw, centered, offset, peak-to-peak, derivative, harmonic,
   robustness, and runtime evidence where available;
5. record metric-source differences explicitly instead of conflating
   analytical and neural replay contracts;
6. produce a machine-readable YAML decision, CSV inventories, and a
   human-readable results report.

The report will distinguish exact numerical reproduction, replay equivalence,
and evidence carried forward from a different but compatible diagnostic.

## Involved Components

The stage is expected to add:

- a Stage 0 analysis configuration under
  `config/analysis/wave_5_2r/stage0_forward_evidence_freeze/`;
- a Stage 0 builder and validator under
  `scripts/analysis/wave_5_2r/stage0_forward_evidence_freeze/`;
- machine-readable evidence under
  `output/analysis/wave_5_2r/stage0_forward_evidence_freeze/`;
- a results report and PDF under
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/stage0_forward_evidence_freeze/`;
- documentation-index and program-status updates where the completed gate
  changes the next executable stage.

The stage will reuse:

- the Phase 0 foundation audit;
- the common split manifest;
- the Phase 1 Polynomial-Fourier implementation;
- the accepted polished-setpoint forward model inventories;
- the repository reference-family comparison pipeline;
- the styled report PDF pipeline.

No subagents are planned.

## Implementation Steps

1. Create isolated Stage 0 configurations for analytical and neural replay.
2. Run the Polynomial-Fourier benchmark into a Stage 0 output root.
3. Run the two accepted forward neural models on the same immutable test
   condition set without training.
4. Build the frozen condition manifest and candidate provenance inventory.
5. Aggregate comparable metrics and preserve contract-specific metrics.
6. Validate hashes, counts, finite values, surface restrictions, and expected
   reproduction tolerances.
7. Write the Stage 0 results report and explicit pass or fail decision.
8. Export and visually validate the real PDF.
9. Synchronize the roadmap, backlog, master summary, ledger, and index.
10. Run Python, Markdown, PDF, whitespace, and file-size preflight checks.
11. Commit the complete Stage 0 package with a dedicated repository-style
    commit.

## Implementation Outcome

Stage 0 completed successfully. The isolated `PF-A` replay and accepted neural
replay cover the same `97` eligible forward test conditions. The frozen
contract contains the forward condition manifest, normalized baseline and
operating-cell metrics, harmonic-band diagnostics, provenance hashes, and
twelve reproduction comparisons.

All eight exit-gate checks pass. The final report is
`doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-27]/stage0_forward_evidence_freeze/stage0_forward_evidence_freeze_report.md`.
