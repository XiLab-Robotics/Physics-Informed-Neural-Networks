# Wave 5.2R Integrated Specialist Model Roadmap

## Overview

This technical document defines the approval-gated roadmap for a future
empirical integrated-specialist transmission-error model. The roadmap follows
the completed Wave 5.2R forward tournament, K01/H08 cross-surface promotion,
and H08 backward/global defect analysis.

The proposed branch is deliberately separate from the closed Wave 6
physics-integrated PINN entry gate. It combines empirically demonstrated model
behaviors and inspectable analytical structures; it does not claim that any
imported component is a validated physical law or that the resulting model is
a full PINN.

The design objective is not to average all available predictions. It is to
test whether complementary behaviors can be introduced one at a time without
transferring each source candidate's known defect:

- K01 supplies the causal temporal baseline and the strongest cross-surface
  raw, offset, and centered-shape evidence;
- H08 supplies forward-only non-temporal harmonic and phase structure, with
  its offset channel and global formulation excluded;
- Stage 12 F01 supplies a centered-shape hypothesis, not a qualified
  checkpoint;
- Stage 12 S01 supplies a harmonic and closure optimization hypothesis, not a
  qualified checkpoint;
- H04 supplies an inspectable analytical anchor and compact centered-shape
  reference;
- Stage 10 R00 supplies evidence that an extended condition-interaction
  library has incremental predictive value, but not a sparse law;
- Stage 10 S01 supplies a compactness ablation and negative control because it
  did not meet sparsity or stability gates.

The accepted periodic GRU and periodic harmonic MLP remain frozen temporal and
non-temporal controls. No integrated candidate may replace an incumbent,
enter a registry, or acquire a deployable-leader label without later training,
official TE Curve Verification Pipeline review, export parity, and TwinCAT
runtime qualification.

This document does not authorize implementation code, campaign preparation,
training, registry modification, model promotion, or PLC changes. No subagent
is planned or authorized.

## Technical Approach

### Program Boundary

The branch will be identified as a Wave 5.2R empirical integrated-specialist
study. It must not be named or reported as:

- a full PINN;
- a physics-integrated Wave 6 model;
- a validated mixture of physical mechanisms;
- a deployable PLC leader;
- or a replacement for the accepted periodic GRU or harmonic MLP.

The Phase 14 and Phase 15 no-integration decisions remain valid because zero
physical components passed the required isolated full-PINN gates. The present
roadmap instead tests a bounded ML architecture using causal inputs already
available to the repository.

### Reference And Evidence Boundary

The repository references support a modular decomposition but do not prescribe
the final implementation:

- the bidirectional cycloidal-drive source requires forward, reverse, and
  global positioning-error surfaces to remain distinct;
- the load-, velocity-, and temperature-dependent Fourier source supports
  explicit operating-condition modulation of harmonic amplitude and phase;
- the hysteresis sources require direction, history, initialization, and
  causal state to remain explicit when a memory mechanism is claimed;
- the ML compensation synthesis supports separating broad interpretable
  behavior from a bounded learned residual;
- the ensemble-learning RV-reducer source demonstrates that heterogeneous
  learners can improve a synthetic design surrogate, but its FEA error inputs
  and stacking result do not validate an operational TE ensemble for this
  dataset.

These references justify explicit routing, bounded residuals, and inspectable
intermediate contributions. They do not justify importing unobserved
clearance, stiffness, friction, wear, contact, or component-error variables.

### Frozen Candidate Evidence

| Ingredient | Verified value | Known defect or boundary | Permitted roadmap role |
| --- | --- | --- | --- |
| K01 seed `271828` | Cross-surface temporal offline leader; improves matched GRU raw, offset, and shape on `Fw`, `Bw`, and `global` | Backward peak-to-peak caveat; TwinCAT runtime acceptance pending | Frozen causal baseline and temporal backbone reference |
| H08 seed `161803` | Forward non-temporal specialist with useful shape, harmonic, phase, and peak-to-peak behavior | Offset regression on `Fw`; raw and offset regression on `Bw` and `global`; global-fit interference | `Fw`-gated centered harmonic residual only; no `a0` transfer |
| Stage 12 F01 | Best trained Stage 12 raw and centered-shape candidate | Failed mean, closure, correction magnitude, chunk equivalence, and frozen-K01 comparison gates | Shape-loss or zero-mean residual hypothesis only |
| Stage 12 S01 | Improved its matched standard-training control on raw, mean, shape, P95, and closure | Remained `8.75%` worse than frozen K01 raw MAE and failed correction and chunk gates | Harmonic/closure auxiliary-objective hypothesis only |
| H04 | Compact analytical residual; strong forward centered shape, derivative, phase, and closure evidence | Raw and offset regressions prevent balanced promotion | Frozen analytical anchor and inspectable shape control |
| Stage 10 R00 | Dense extended condition library improves raw and mean error over the quadratic control | Dense, non-parsimonious, forward-only diagnostic; not identified physics | Optional causal condition-feature basis after simpler branches pass |
| Stage 10 S01 | Sequential-thresholded ridge preserves some extended-library benefit | Retains `86.9%` of coefficient slots and fails sparsity/stability qualification | Compactness negative control; never a promoted symbolic law |

The two candidates named `S01` must remain namespace-qualified as
`stage12_s01` and `stage10_s01` in configuration, reports, and code.

### Proposed Prediction Decomposition

The first architecture candidate will preserve a measurable decomposition:

```text
predicted_te = predicted_mean + predicted_centered_curve

predicted_mean = bounded_temporal_mean_head

predicted_centered_curve =
    centered_temporal_baseline
  + forward_gate * bounded_h08_centered_residual
  + bounded_shape_residual
  + optional_condition_interaction_residual
```

The constraints are:

- `forward_gate` is deterministic and equals zero for `Bw`;
- the H08 contribution is explicitly mean-centered before integration;
- H08 coefficient `a0` and the current global H08 formulation are excluded;
- every added residual is bounded and individually exported;
- no branch can use measured TE, future samples, validation labels, or
  target-derived states at inference time;
- the complete model must preserve the K01 reset, causal-prefix, state-carry,
  and non-overlapping 32-sample chunk contract;
- the implementation must expose mean, centered baseline, each residual,
  routing state, validity state, and final output separately.

This decomposition is a starting hypothesis. The campaign plan must compare it
with simpler frozen-output and single-branch alternatives before implementation
or training is authorized.

### K01 Baseline Topology

The campaign plan must compare two frozen K01 baseline topologies before adding
specialists:

- direction-specific K01 `Fw` and `Bw` checkpoints behind deterministic
  routing;
- the direction-aware global K01 checkpoint with its explicit direction input.

The topology decision must use separate `Fw`, `Bw`, and `global` multi-index
evidence, state behavior, export cost, and PLC complexity. It cannot be chosen
from campaign scalar rank alone. Specialist arms will attach only to the
selected topology, while the other topology remains a required frozen control.

### Architecture Sequence

The roadmap uses an ordered sequence so that failed components cannot hide
inside a full model.

1. **Contract freeze.** Replay frozen K01, H08, H04, F01, Stage 12 S01, Stage
   10 R00, and Stage 10 S01 artifacts; record their exact inputs, outputs,
   state, normalization, split, seed, and failure contracts.
2. **Baseline decomposition.** Reproduce K01 and split its output into mean and
   centered components without changing its prediction.
3. **Forward harmonic branch.** Add only the mean-centered H08 contribution
   behind a deterministic forward gate. Prove that its output is exactly zero
   on `Bw` and that global evaluation is the union of independently routed
   directional behavior.
4. **Shape branch.** Test a bounded zero-mean shape residual using H04 as the
   inspectable control and F01 only as an objective or initialization
   hypothesis.
5. **Harmonic and closure objective.** Test Stage 12 S01-derived loss terms
   without importing its failed checkpoint as a qualified expert.
6. **Condition-interaction branch.** Test Stage 10 R00 feature interactions
   only after the simpler model passes. Compare Stage 10 S01 as the explicit
   compactness control.
7. **Integrated candidate.** Combine only branches that independently pass
   their ablation gates. A branch that fails remains excluded even if the full
   combination improves scalar MAE.

No learned router is planned for the first campaign. Directional routing must
remain deterministic, inspectable, and testable in PLC-oriented execution.

### Required Ablation Matrix

The preliminary campaign plan must freeze at least the following ablations:

| Ablation | Temporal base | H08 `Fw` centered branch | Shape branch | Harmonic/closure objective | Condition library |
| --- | --- | --- | --- | --- | --- |
| `A00` | K01 replay | off | off | off | off |
| `A01` | K01 decomposed | off | off | off | off |
| `A02` | K01 decomposed | on | off | off | off |
| `A03` | K01 decomposed | off | H04 control | off | off |
| `A04` | K01 decomposed | off | F01 hypothesis | off | off |
| `A05` | K01 decomposed | off | off | Stage 12 S01 hypothesis | off |
| `A06` | K01 decomposed | off | off | off | Stage 10 R00 |
| `A07` | K01 decomposed | off | off | off | Stage 10 S01 control |
| `A08` | K01 decomposed | passed branches only | passed branches only | passed branches only | passed branches only |

The campaign plan may add bounded diagnostic arms, but it may not remove the
single-component controls or introduce a full combination without its parent
ablations.

### Surface And Data Contract

Every trained or replayed candidate must use:

- `polished_dataset` setpoint inputs;
- the frozen grouped split signature used by the official Wave 5.2R evidence;
- separate `Fw`, `Bw`, and direction-aware `global` evaluation surfaces;
- three predeclared random seeds for every trainable arm;
- immutable timestamped `run_instance_id` output directories;
- training-only fitting of normalization, analytical anchors, feature
  libraries, residual scales, and any blend parameters;
- exactly one final test evaluation after configuration and thresholds freeze.

`global` is an evaluation and deployment surface with explicit direction, not
permission to train or route an undifferentiated H08 global expert.

### Incremental Acceptance Gates

Each branch must pass against its immediate parent and the relevant frozen
incumbents. The campaign plan must predeclare numerical tolerances before test
access. Acceptance must cover:

- raw MAE and P95 error;
- signed and absolute mean-offset error;
- centered-shape MAE;
- peak-to-peak envelope error;
- derivative fidelity and closure;
- harmonic amplitude and wrapped phase;
- operating-condition robustness by speed, torque, and oil temperature;
- seed stability;
- correction magnitude and saturation rate;
- deterministic replay, reset, causal-prefix, state-carry, and chunk
  equivalence;
- invalid-input fallback and direction-transition behavior;
- ONNX numerical parity, package size, and host-latency proxy.

No component qualifies through scalar MAE alone. A branch must improve its
declared specialty without violating non-regression limits on raw, offset,
shape, envelope, causality, or deployment evidence.

### Mandatory Negative Controls

The following controls must remain visible:

- K01-only baseline;
- accepted periodic GRU and periodic harmonic MLP;
- forward-gated H08 versus the rejected current global H08 behavior;
- H08 centered residual with and without `a0`, where the `a0` arm is diagnostic
  only and cannot enter the final model;
- frozen H04 versus learned shape residual;
- Stage 10 R00 dense library versus Stage 10 S01 thresholded library;
- shuffled-label or zero-residual specificity control for every new learned
  residual branch;
- full integrated candidate versus the best simpler passing ablation.

### PLC And Export Contract

The model must be designed for an inspectable TwinCAT path from the beginning:

- fixed tensor shapes and explicit state tensors;
- deterministic 32-sample temporal chunking when the K01 path is active;
- one explicit direction input and deterministic forward-specialist gate;
- bounded `REAL`-compatible intermediate contributions;
- operator-visible validity, initialization, reset, fallback, and active-branch
  state;
- separate parity tests for every intermediate output and the final TE;
- no Python-only feature reconstruction that lacks a documented PLC analogue;
- latency and memory accounting for each enabled branch.

Static ONNX, PLCopen XML, or isolated Structured Text parity does not establish
target activation, TF3820 licensing, ADS operation, or runtime compensation.
Those remain separate qualification gates.

### Decision Outcomes

The integrated study must close with one of these outcomes:

- `k01_only_retained`: no specialist adds balanced incremental value;
- `forward_harmonic_specialist_added`: the centered H08 branch qualifies only
  on `Fw`;
- `shape_specialist_added`: one bounded H04/F01-derived shape branch qualifies;
- `condition_interaction_specialist_added`: one Stage 10-derived branch adds
  stable incremental value;
- `multi_specialist_candidate_qualified`: at least two independently passing
  branches also pass together;
- `integration_rejected`: interactions or deployment costs invalidate the
  combined model.

None of these outcomes automatically changes accepted registries or establishes
TwinCAT deployment readiness.

### Approval Boundary

After this technical document is approved, the next authorized activity is to
prepare the preliminary campaign planning report and the complete campaign
package. The campaign package must include:

- immutable YAML manifests and per-arm configurations;
- a dedicated PowerShell launcher supporting local and `-Remote` execution;
- the matching launcher note;
- active-campaign state with local and remote commands;
- preflight-only validation and expected artifact contracts;
- the exact launch commands.

Training remains prohibited until both this technical document and the future
campaign plan have explicit approval. The user will run the campaign and report
completion before campaign artifacts are inspected or accepted.

## Involved Components

- `doc/reports/analysis/model_development_waves/wave_5_2/offline_leader_global_promotion/official_decision/[2026-07-31]/wave52r_cross_surface_offline_leader_promotion_decision.md`
  Canonical K01/H08 cross-surface roles and multi-index evidence.
- `doc/reports/analysis/model_development_waves/wave_5_2/h08_backward_global_defect_analysis/[2026-08-02]/wave52r_h08_backward_global_defect_analysis_report.md`
  H08 forward-only, offset, and global-interference contract.
- `doc/reports/analysis/model_development_waves/wave_5_2/official_forward_verification_and_deployment_preparation/[2026-07-30]/stage15_official_forward_verification_and_deployment_preparation_report.md`
  H04 analytical, shape, and deployment-preparation evidence.
- `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage12_advanced_constraint_optimization/stage12_advanced_constraint_optimization_model_report.md`
  Stage 12 F01 and S01 benefit and failure contracts.
- `doc/reports/campaign_results/model_development_waves/wave_5_2/2026-07-29-20-23-30_wave52r_stage10_sparse_and_symbolic_formulation_discovery_results_report.md`
  Stage 10 R00 and S01 condition-library, sparsity, and stability evidence.
- `doc/reports/analysis/model_development_waves/wave_5_2/integrated_multi_physics_pinn/[2026-07-26]/phase14_integrated_multi_physics_report.md`
  Boundary separating this empirical roadmap from the closed full-PINN
  integration gate.
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
  Mandatory future offline selection policy.
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
  Reference-backed decomposition, causal-state, direction, and deployment
  boundaries.
- `reference/te_modeling/theoretical_mechanics/numerical_and_fea_models/2026_wang_ensemble_learning_te_prediction_optimization_rv_reducer.pdf`
- `reference/te_modeling/theoretical_mechanics/kinematics_and_transmission_error/2024_wang_bidirectional_drive_te_positioning_accuracy_cycloid_reducer.pdf`
- `reference/te_modeling/bibliography/polynomial_fourier/2025_bauer_load_velocity_temperature_dependent_cycloidal_te_fourier_model.pdf`
  Primary sources used to bound ensemble, direction, and harmonic-condition
  claims.
- `scripts/models/causal_temporal_analytical_residual_network.py`
  Existing K01 causal temporal model contract.
- `scripts/models/complex_harmonic_coefficient_residual_network.py`
  Existing H08 coefficient and analytical-anchor contract.
- `scripts/models/mean_centered_shape_multi_head_network.py`
  Existing mean/centered decomposition pattern.
- `scripts/training/advanced_constraint_optimization.py`
  Existing Stage 12 optimization and diagnostic contract.
- `scripts/campaigns/wave_5_2/run_wave52r_stage10_sparse_symbolic_discovery.py`
  Stage 10 condition-library and sparse-control implementation to inventory
  before reuse.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/`
  Parallel standalone PLC qualification surface; not modified by this roadmap.
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  Status surfaces to synchronize only after the roadmap is approved and the
  campaign package is prepared or a later decision changes program state.
- `doc/README.md`
  Canonical registration point for this technical document.

## Implementation Steps

1. Register this technical document and wait for explicit user approval.
2. After approval, audit the exact K01, H08, H04, Stage 12 F01/S01, and Stage
   10 R00/S01 artifact schemas, hashes, split signatures, normalization, state,
   and export contracts.
3. Create a preliminary campaign planning report that freezes the architecture
   sequence, ablation matrix, seeds, thresholds, resource estimates, expected
   artifacts, and local/remote execution contract.
4. Create the immutable campaign YAML, per-arm configurations, dedicated
   PowerShell launcher, launcher note, and persistent active-campaign state.
5. Implement the smallest reusable mean/centered decomposition and deterministic
   direction-routing interfaces only after the technical document is approved.
6. Implement K01-equivalent replay as `A00` and decomposition-equivalent replay
   as `A01`; require numerical identity before adding specialists.
7. Implement the H08 branch as an explicitly mean-centered, forward-gated,
   bounded residual. Keep `a0` and the current global H08 formulation out of
   the candidate path.
8. Implement H04/F01 shape and Stage 12 S01 harmonic/closure arms as separate
   hypotheses with independent gates.
9. Implement Stage 10 R00 and Stage 10 S01 condition-library arms only if the
   simpler branches pass preflight and resource gates.
10. Add deterministic replay, causal-prefix, reset, state-carry, chunk,
    direction-transition, invalid-input, fallback, saturation, export-parity,
    latency, and package-size validators.
11. Produce the dedicated explanatory model report before the integrated model
    is used, covering architecture, operating principle, intermediate outputs,
    advantages, disadvantages, files, classes, and functions.
12. Run campaign package validation and provide exact local and `-Remote`
    commands. Stop for explicit approval of the campaign plan before training.
13. After the user reports campaign completion, inspect the persistent state,
    required winner artifacts, per-arm evidence, and failure records before
    normal campaign closeout.
14. Complete the campaign-results Markdown and styled PDF report, validate the
    real PDF, synchronize registries and status without automatic promotion,
    and clear active campaign state normally.
15. Propose the heavy TE Curve Verification Pipeline refresh as a separate
    optional step. If approved, prepare its local/remote launcher and wait for
    the user to run it.
16. Require separate `Fw`, `Bw`, and `global` official decisions plus export
    and TwinCAT runtime gates before any accepted-model or deployability claim.
17. Run touched-scope Python, YAML, launcher, Markdown, final-newline, Sphinx,
    diff, and staged-size QA at every relevant approval and commit boundary.
18. Report completion and wait for explicit approval before each Git commit.
