# Wave 5.2R H08 Backward And Global Defect Analysis

## Overview

This technical document defines a non-training diagnostic of the Wave 5.2R
H08 backward and direction-aware global defects. H08 remains the preserved
non-temporal `Fw` offline specialist, but it did not pass cross-surface
promotion because its `Bw` and `global` raw-error and offset results regress
against the matched periodic harmonic MLP incumbent.

The official cross-surface decision provides the starting evidence:

| Surface | Selected H08 seed | Raw MAE change | Offset change | Shape change |
| --- | ---: | ---: | ---: | ---: |
| `Fw` | 161803 | +0.35% | -4.48% | +5.04% |
| `Bw` | 161803 | -1.10% | -15.03% | +1.13% |
| `global` | 314159 | -7.90% | -22.01% | -2.78% |

Positive values mean improvement over the matched non-temporal incumbent.
These results show that the defect cannot be represented by one scalar metric:
H08 preserves useful forward and harmonic behavior, has a small backward shape
gain, but loses offset and envelope fidelity on the backward and combined
surfaces.

The diagnostic will determine whether the failure is primarily:

- an offset or coefficient-`a0` calibration defect;
- a direction-conditioned coefficient-surface defect;
- a high-dynamic-condition envelope defect;
- interference introduced by fitting one `global` model across both
  directions;
- seed-sensitive behavior;
- or a mixed failure that should remain excluded from later integration.

This document does not authorize model retraining, checkpoint modification,
new campaign execution, registry promotion, accepted-model replacement, PLC
changes, or the integrated-specialist roadmap. No subagent is planned or
authorized.

## Technical Approach

### Evidence Boundary

The analysis will replay existing immutable artifacts only. Its primary H08
surface contains nine runs: three seeds for each of `Fw`, `Bw`, and `global`.
The frozen payloads already expose `194` conditions for global runs, `2048`
angular samples per curve, and the following inspectable arrays:

- measured curve;
- predicted curve;
- predicted complex coefficient vector;
- learned coefficient correction;
- condition identifier.

The analytical anchor coefficients can be recovered as predicted coefficients
minus learned corrections. The H08 coefficient contract contains one offset
coefficient and sine/cosine pairs for the data-selected orders `1`, `2`, `3`,
`39`, `40`, `42`, `78`, `80`, `81`, `120`, `156`, `158`, `159`, `160`,
`162`, `237`, and `240`.

The analysis will compare H08 against:

- the matched accepted periodic harmonic MLP on each valid surface;
- matched H04 anchors for coefficient-level attribution;
- all three H08 seeds, not only the selected checkpoints;
- the H08 `Fw` surface as the positive specialist control;
- K01 only as contextual cross-surface evidence, not as the H08 repair target.

No metric will be recomputed from a different split. The diagnostic must prove
that every loaded curve matches the frozen split signature and expected
surface count before drawing conclusions.

### Reference-Backed Hypotheses

The source literature supports a diagnostic decomposition, not a conclusion
about H08:

- the cycloidal-drive Fourier reference models amplitude and phase as
  condition-dependent functions of torque, velocity, and temperature;
- the bidirectional RV-reducer reference treats forward TE, reverse TE, and
  global lost motion as related but non-interchangeable surfaces;
- the hysteresis references require direction, load path, temperature, and
  state to remain explicit and warn against treating a static curve fit as a
  validated memory law;
- the repository reference synthesis separates periodic shape, mean or elastic
  offset, and hysteretic state rather than collapsing them into one target.

These sources justify the questions to test. They do not prove that hysteresis,
lost motion, compliance, or any other specific mechanism caused the observed
H08 defect. Mechanism language in the final report must therefore be labeled
as confirmed artifact evidence, supported inference, or unresolved hypothesis.

### Diagnostic Layers

The diagnostic will use five ordered layers.

1. **Artifact and reproduction audit.** Verify the nine H08 artifacts,
   checkpoint provenance, three surfaces, three seeds, split signature,
   condition identifiers, array shapes, curve counts, and official summary
   reproduction.
2. **Raw, offset, and centered-shape decomposition.** Report signed curve-mean
   error, absolute offset error, raw MAE, centered MAE, peak-to-peak error,
   derivative fidelity, closure, and the fraction of raw error attributable to
   mean displacement for every surface and direction subset.
3. **Coefficient and harmonic-band attribution.** Separate analytical anchor,
   learned correction, and final prediction for coefficient `a0`, order `1`,
   low orders, reducer-related middle orders, high-order ripple, and exploratory
   residual orders. Quantify which bands change sign, saturate, or transfer
   poorly between Fw and Bw.
4. **Condition and direction audit.** Rank degradation by speed, torque, oil
   temperature, and their observed combinations. Match Fw and Bw conditions
   where the setpoint tuple agrees, and split each global checkpoint into Fw
   and Bw subsets to distinguish global-fit interference from a backward-only
   defect.
5. **Seed, support, and visual audit.** Separate stable structural behavior
   from seed selection, identify worst and best condition cells, and generate
   measured-versus-predicted, mean-centered, offset, envelope, and coefficient
   attribution plots for deterministic evidence cells.

The condition audit is explanatory rather than causal. Correlation with speed,
torque, or temperature will not be described as a physical cause without an
independent intervention or source-backed identifiable relation.

### Decision Contract

The final diagnostic will place H08 into one of these bounded outcomes:

- `offset_dominant_repair_candidate`: centered shape remains useful and a
  causal, direction-specific offset correction is justified for later study;
- `direction_conditioned_coefficient_candidate`: specific coefficient bands
  transfer poorly and a direction-explicit structured variant is justified;
- `support_envelope_limited`: failures concentrate outside a defensible
  operating support and H08 remains a bounded specialist;
- `global_interference_confirmed`: separate Fw/Bw models outperform the global
  formulation because the combined coefficient surface transfers the defect;
- `mixed_or_unresolved`: no narrow repair is supported and H08 remains frozen
  as a forward-only research specialist.

No outcome automatically authorizes a repair or training campaign. Any repair
requires a new technical document, and any training experiment additionally
requires a campaign planning report and explicit approval.

## Involved Components

- `doc/reports/analysis/model_development_waves/wave_5_2/offline_leader_global_promotion/official_decision/[2026-07-31]/wave52r_cross_surface_offline_leader_promotion_decision.md`
  Canonical cross-surface decision and selected-candidate evidence.
- `output/training_runs/complex_harmonic_coefficient_residuals/`
  Nine immutable H08 promotion runs and their curve/coefficient payloads.
- `output/validation_checks/track2_reference_comparison/`
  Existing per-condition and surface-level official verification artifacts.
- `output/analysis/wave_5_2r/offline_leader_cross_surface_track2/`
  Existing diagnostics and inspected Fw, Bw, and global visual evidence.
- `scripts/models/complex_harmonic_coefficient_residual_network.py`
  Implemented H08 coefficient, anchor, correction, and reconstruction
  contract.
- `reference/te_modeling/bibliography/polynomial_fourier/2025_bauer_load_velocity_temperature_dependent_cycloidal_te_fourier_model.pdf`
  Source for condition-dependent Fourier amplitude and phase behavior.
- `reference/te_modeling/theoretical_mechanics/kinematics_and_transmission_error/2024_wang_bidirectional_drive_te_positioning_accuracy_cycloid_reducer.pdf`
  Source for the separation and relationship of forward, reverse, and global
  positioning-error surfaces.
- `reference/te_modeling/bibliography/hysteresis_and_backlash/2023_mesmer_investigation_compensation_hysteresis_robot_joints_cycloidal_drives.pdf`
  Source for load, temperature, friction, and hysteresis boundaries.
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
  Repository interpretations used to keep physical claims bounded.
- `config/analysis/wave52r_h08_backward_global_defect_analysis.yaml`
  Proposed immutable diagnostic configuration.
- `scripts/reports/analysis/build_wave52r_h08_backward_global_defect_analysis.py`
  Proposed persistent analysis and report builder.
- `scripts/reports/analysis/validate_wave52r_h08_backward_global_defect_analysis.py`
  Proposed artifact, metric, plot, and decision-contract validator.
- `output/analysis/wave_5_2r/h08_backward_global_defect_analysis/`
  Proposed reproducible YAML, CSV, and plot artifact root.
- `doc/reports/analysis/model_development_waves/wave_5_2/h08_backward_global_defect_analysis/[2026-08-02]/`
  Proposed canonical report bundle with companion visual assets.
- `doc/scripts/analysis/`
  Proposed usage note for the persistent builder and validator.
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  Status documents to update only when the completed diagnostic materially
  changes the H08 role or the next modeling decision.
- `doc/guide/project_usage_guide.md` and `site/`
  User-facing and portal surfaces to update if the approved implementation
  introduces a reusable analysis command.
- `doc/README.md`
  Canonical registration point for this technical document.

## Implementation Steps

1. Register this technical document and wait for explicit user approval.
2. Freeze the nine H08 run paths, three matched incumbents, matched H04
   controls, split signature, expected curve counts, and source hashes in the
   diagnostic configuration.
3. Implement the persistent builder and validator using actual artifact field
   names confirmed from the frozen NPZ, YAML, and CSV schemas.
4. Reproduce the official selected-surface raw, offset, and centered-shape
   values within declared numerical tolerances before adding new diagnostics.
5. Generate the per-surface, per-direction, per-seed, and per-condition metric
   tables without changing the official split or candidate selection.
6. Recover analytical anchor coefficients and compute coefficient-`a0`, band,
   correction, and final-prediction attribution.
7. Pair matching Fw/Bw setpoint cells and split global predictions by direction
   to test direction transfer and global-fit interference.
8. Generate deterministic raw-curve, mean-centered, offset, envelope,
   coefficient, condition, and seed-stability visualizations.
9. Visually inspect the real generated plots and revise any ambiguous or
   misleading presentation before closeout.
10. Produce the canonical Markdown analysis report with explicit separation of
    implemented facts, reference-backed hypotheses, artifact-supported
    inferences, and unresolved questions.
11. Validate the complete artifact and report contract. Do not execute training
    or modify model checkpoints, accepted registries, or PLC artifacts.
12. Update the backlog, ledger, and master summary only if the diagnostic
    conclusion materially changes H08 status or the next-roadmap decision.
13. Add the repository-owned usage note and synchronize the project guide and
    Sphinx portal if a reusable command is introduced.
14. Run Python compilation, focused diagnostic validation, Markdown warning
    checks, Markdownlint, final-newline checks, `git diff --check`, and a
    warning-free Sphinx build when portal scope changes.
15. Report the completed diagnostic and wait for explicit approval before any
    Git commit or before preparing an H08 repair or integrated-specialist task.

## Implementation Outcome

The approved non-training implementation completed as diagnostic run
`2026-08-02-17-12-57`. It reproduced the official rounded H08 metrics within a
maximum absolute difference of `0.000000412 deg`, validated all nine H08 run
payloads, and generated the machine-readable package plus six visually
inspected plots.

The bounded decision is
`offset_dominant_direction_conditioned_with_global_interference`. Backward H08
retains a small centered-shape advantage but loses primarily through offset,
while the combined global H08 model is worse than the corresponding
directional specialist on both directions. H08 therefore remains frozen as the
non-temporal `Fw` offline specialist. The current global formulation is an
explicit exclusion and ablation contract for the future integrated-specialist
roadmap.

No training ran. No checkpoint, accepted registry, deployment baseline, or PLC
artifact changed. The reusable builder and validator are documented under
`doc/scripts/reports/analysis/` and exposed in the Sphinx API tree.
