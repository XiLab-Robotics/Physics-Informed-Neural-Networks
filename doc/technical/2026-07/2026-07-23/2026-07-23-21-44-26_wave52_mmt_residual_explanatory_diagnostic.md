# Wave 5.2 MMT Residual-Explanatory Diagnostic

## Overview

This technical document prepares the next step selected by the approved
`Wave 5.2` post-causal-offset decision gate.

The work is a non-training diagnostic. It will test whether leakage-safe
signatures derived from the repository-owned MMT analytical model explain
held-out residual structure from the accepted polished-setpoint windowed and
non-windowed baselines.

The diagnostic must distinguish three evidence classes:

- reference-backed mechanical relationships from `MMT_TEModeling.pdf`;
- repository-implemented MMT equations, parameter inventory, and model
  predictions;
- open hypotheses about whether MMT signatures explain residual offset,
  fragile harmonics, phase, or derivative behavior in the repository dataset.

No model implementation, campaign preparation, training, registry promotion,
or full `TE Curve Verification Pipeline` refresh is authorized by this
document. No subagent is planned. If review help becomes useful, the proposed
subagent name, reason, and exact delegated scope will be declared before
requesting approval.

## Technical Approach

The diagnostic will use existing repository MMT and curve-verification
components to build an auditable residual-explanation matrix.

### Baseline Scope

The primary baseline set is:

| Surface | Windowed baseline | Non-windowed baseline |
| --- | --- | --- |
| `Fw` | `polished_setpoints_periodic_gru_sequence_Fw` | `polished_setpoints_periodic_mlp_harmonic_Fw` |
| `Bw` | `polished_setpoints_periodic_gru_sequence_Bw` | `polished_setpoints_periodic_mlp_harmonic_Bw` |

The `global` surface remains paused under the current reduced-selection policy.
The diagnostic must not collapse forward and backward behavior into one
competition.

### Leakage Boundary

The implementation must establish the exact train, validation, and held-out
group boundary used by each baseline before fitting any equivalent-error
calibration.

Allowed inputs include:

- geometry constants verified for the reducer;
- causal operating metadata such as input speed, applied torque, oil
  temperature, direction, and encoder-zeroing or `DataValid` context when
  represented in the canonical dataset;
- MMT signatures computed without measured held-out TE;
- equivalent-error parameters calibrated only from training groups.

Forbidden inputs include:

- held-out curve means or harmonic coefficients used as explanatory inputs;
- future measured TE samples;
- per-curve calibration fitted on validation or test targets;
- offline polishing operations embedded in the inference-side feature path.

If the exact split or provenance boundary cannot be reconstructed, the
diagnostic must stop at a descriptive, non-fitted report and record the
blocker. It must not silently substitute a new random split.

### Explanatory Comparisons

For every surface and baseline architecture, the diagnostic will compare:

1. operating metadata only;
2. geometry-locked MMT signatures;
3. training-only calibrated equivalent-error signatures;
4. operating metadata plus allowed MMT signatures;
5. shuffled-signature controls that preserve the evaluation shape but destroy
   the mechanical association.

The explanatory targets are baseline residual summaries, not new model
predictions:

- raw residual MAE;
- curve-mean or offset residual;
- mean-centered residual shape;
- harmonic amplitude and phase residuals;
- peak-to-peak residual;
- derivative agreement and ripple-related residual metrics.

The implementation should use a transparent low-capacity explanatory method
with inspectable coefficients or contributions. Any library-specific solver or
API choice must be checked against current Context7 documentation before code
is implemented.

### Decision Gate

An MMT signature is actionable only if:

- its explanatory value survives held-out evaluation;
- it exceeds metadata-only and shuffled controls;
- its direction and sign remain stable across relevant condition groups;
- it is visible for both baseline architectures or is explicitly identified as
  architecture-specific;
- every required runtime quantity is available, reconstructable, or causally
  predicted;
- the conclusion is supported by multiple residual views rather than one
  scalar score.

Passing this gate would authorize a later technical proposal for a compact MMT
feature or auxiliary-prediction pilot. It would not authorize training
directly. Weak soft constraints remain secondary, and full PINN work remains
deferred.

## Involved Components

Existing read-only inputs:

- `reference/MMT_TEModeling.pdf`;
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`;
- `scripts/paper_reimplementation/mmt_te_modeling/`;
- `scripts/models/wave4_mmt_diagnostic_adapter.py`;
- `scripts/features/wave4b_mmt_feature_generator.py`;
- `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py`;
- `scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py`;
- `doc/reports/analysis/model_development_waves/wave_4/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/`;
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/selected_active_track2_polished_setpoints_matrix.yaml`;
- accepted baseline registries and archived Python / ONNX model artifacts under
  `output/registries/families/` and `models/polished_dataset/setpoints/`;
- existing per-curve and shape-gated `TE Curve Verification Pipeline`
  artifacts for the selected baselines.

Planned implementation outputs after approval:

- diagnostic builder:
  `scripts/reports/analysis/build_wave52_mmt_residual_explanatory_diagnostic.py`;
- diagnostic configuration:
  `config/analysis/wave52_mmt_residual_explanatory_diagnostic.yaml`;
- machine-readable run artifacts under
  `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/<run_instance_id>/`;
- dated analytical report under
  `doc/reports/analysis/model_development_waves/wave_5_2/mmt_residual_explanatory_diagnostic/[2026-07-23]/`;
- documentation registration in `doc/README.md`;
- synchronized decision status in the live backlog, program ledger, and master
  summary only after the diagnostic produces a valid conclusion.

Expected machine-readable artifacts:

- resolved baseline and provenance manifest;
- split-boundary audit;
- per-curve residual feature table;
- MMT signature table;
- metadata-only, MMT, combined, and shuffled-control comparison tables;
- per-surface and per-architecture decision summary;
- run configuration and validation summary.

Deferred components:

- training YAML files;
- PowerShell campaign launchers;
- campaign planning or result reports;
- `doc/running/active_training_campaign.yaml` changes;
- model factory or training-module changes;
- registry promotion;
- full PINN, weak-soft-constraint, or Wave 6 implementation.

## Implementation Steps

1. Resolve the four accepted baseline artifacts and their training provenance
   from canonical registries and archived model metadata.
2. Audit and reconstruct the exact train, validation, and held-out
   operating-condition groups used by each baseline.
3. Inventory the MMT signatures that can be computed from geometry constants
   and causal operating metadata without target leakage.
4. Define training-only calibration rules for eligible equivalent-error
   groups and block unavailable contact-geometry terms.
5. Reuse or extend repository prediction utilities to generate aligned
   per-curve baseline residuals for `Fw` and `Bw`.
6. Build metadata-only, geometry-locked, calibrated-MMT, combined, and
   shuffled-control explanatory comparisons.
7. Report raw, offset, centered-shape, harmonic, peak-to-peak, derivative, and
   ripple-related residual evidence separately for each surface and baseline
   architecture.
8. Generate machine-readable artifacts and a dated analytical report that
   distinguishes implemented facts, reference-backed claims, and inferences.
9. Apply the decision gate and state one result:
   - MMT remains diagnostic-only;
   - an MMT feature or auxiliary-prediction pilot is justified;
   - evidence is blocked by provenance or parameter availability.
10. Synchronize canonical status documents only after a valid diagnostic
    conclusion exists.
11. Validate Python syntax and the diagnostic's bounded test fixture, parse all
    generated YAML or CSV outputs, run Markdown QA on touched documentation,
    and run the Sphinx warning-free build if portal-scope documentation changes.
12. Stop for explicit approval before preparing any later training campaign.

## Implementation Record

Implementation completed on `2026-07-24`.

- Added the configuration and non-training diagnostic builder.
- Resolved all four frozen baseline inventories, ONNX files, checkpoints, and
  training snapshots.
- Reconstructed the canonical split as 1,356 training, 388 validation, and 194
  test curves.
- Audited 388 selected residual rows and found that every row belongs to the
  held-out test split.
- Materialized geometry-locked MMT signatures and confirmed that they are
  constant across operating conditions.
- Performed no residual fit, no model training, no registry update, and no
  campaign-state change.
- Closed the diagnostic as `blocked_by_missing_training_residuals`.
- Set the next step to frozen-baseline residual replay over the exact training
  and validation manifests before rerunning the explanatory comparison.
