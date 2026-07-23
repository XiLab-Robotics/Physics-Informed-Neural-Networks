# Wave 5.2 Post-Causal-Offset Decision Gate

## Overview

This technical document defines the next repository step after the completed
causal offset / mean calibration pilot and its bounded `TE Curve Verification
Pipeline` screen.

The causal-offset branch did not promote either candidate. The accepted
`polished_setpoints_periodic_gru_sequence_Fw` baseline remains the forward
recommendation, while the direct residual-offset GRU failed the shape gate and
the non-windowed causal harmonic MLP remained behind the accepted baselines.
The bounded-screen output-readability and measured-versus-predicted plot gaps
have since been repaired.

The next step is therefore a documentation and evidence-integration gate. It
will close the stale output-repair action in the canonical status documents
and decide whether the next `Wave 5.2` branch should:

- remain diagnostic-only;
- use leakage-safe MMT-derived features or auxiliary predictions;
- use a weak MMT-informed soft constraint;
- remain deferred because the available physical parameters or validation
  evidence are insufficient.

This gate does not authorize model implementation, campaign preparation, or
training. No subagent is planned. If review help becomes useful, the proposed
subagent name, reason, and exact delegated scope will be declared before
requesting approval.

## Technical Approach

The work will synthesize the current repository evidence into one dated
decision report. The decision must be based on the real completed artifacts,
not on scalar campaign ranking alone.

The evidence review will cover:

1. The completed causal offset / mean calibration pilot and bounded
   curve-first screen.
2. The completed shape-gate, shape-objective, and shape-first distillation
   pilots and their bounded screens.
3. The `Wave 5.2A` paired-dataset diagnostics and MMT parameter inventory.
4. The completed `Wave 5.2B` offset-and-harmonic-guided results and official
   curve-verification evidence.
5. The analytical MMT reference boundaries, including explicit mechanical
   parameters, harmonic traceability, and unavailable contact-geometry terms.
6. The accepted forward baselines and the reduced active model-family set.

The report will evaluate each candidate path against explicit gates:

- inference-time causality and absence of target leakage;
- availability and traceability of required mechanical parameters;
- raw-error behavior;
- mean-centered shape fidelity;
- offset and continuity behavior;
- harmonic amplitude and phase fidelity;
- derivative, ripple, and robustness behavior;
- compatibility with inspectable TwinCAT / PLC-oriented inference;
- preservation of both time-windowed and non-windowed candidate roads.

The output must make one concrete recommendation and record why the other
paths are rejected or deferred. A recommendation for future training will
still require a separate campaign planning report and explicit approval.

## Involved Components

Primary reference and evidence inputs:

- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`;
- `doc/reports/analysis/te_modeling/analytical_mmt/`;
- `doc/reports/analysis/model_development_waves/wave_4/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/`;
- recent bounded `TE Curve Verification Pipeline` reports and reranker
  artifacts for the shape and causal-offset branches;
- `output/validation_checks/wave52a_paired_dataset_diagnostics/`;
- completed `Wave 5.2B` training, registry, and verification artifacts.

Canonical status inputs and planned synchronized outputs:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- `doc/README.md`.

Planned new output after approval:

- a dated decision report under
  `doc/reports/analysis/model_development_waves/wave_5_2/post_causal_offset_decision_gate/[2026-07-23]/`.

Deferred components:

- Python model or training implementation;
- campaign YAML files;
- PowerShell campaign launchers;
- `doc/running/active_training_campaign.yaml` changes;
- registry promotion;
- training or training-related experiments;
- heavy full-matrix `TE Curve Verification Pipeline` execution.

## Implementation Steps

1. Inspect the completed causal-offset pilot, bounded screen, repaired plot
   package, and final curve-first decision.
2. Extract common failure modes from the recent shape-gate, shape-objective,
   shape-first distillation, and causal-offset screens.
3. Re-evaluate the `Wave 5.2A` MMT diagnostics, parameter inventory, paired
   dataset evidence, and completed `Wave 5.2B` results against those failure
   modes.
4. Compare diagnostic-only, MMT feature or auxiliary-output, and weak
   MMT-informed soft-constraint paths using the explicit decision gates.
5. Draft one dated decision report with a single recommended next branch,
   rejection or deferral rationale for the alternatives, and a clear
   no-training boundary.
6. Synchronize the backlog, closeout ledger, master summary, and documentation
   index so the completed output repair is no longer listed as pending and the
   selected next gate is canonical.
7. Run the repository Markdown warning checks on every touched authored
   Markdown file and confirm a single normal final newline.
8. Stop for explicit approval before preparing any campaign package or
   implementing any model or training change.

## Implementation Record

The approved decision gate was completed without model implementation or
training.

The resulting report selects a leakage-safe MMT residual-explanatory
diagnostic as the next branch. The MMT path remains diagnostic-only until its
signatures demonstrate held-out value beyond operating-metadata and shuffled
controls across the accepted time-windowed and non-windowed `Fw` / `Bw`
baselines.

The canonical backlog, closeout ledger, training-results master-summary
surfaces, and documentation index were synchronized with this decision.
