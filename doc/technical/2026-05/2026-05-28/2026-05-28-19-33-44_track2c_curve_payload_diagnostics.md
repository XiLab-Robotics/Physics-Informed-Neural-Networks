# CVP 1.2 Curve Payload Diagnostics

## Overview

This document plans the `CVP 1.2 Curve Payload Diagnostics` branch. The branch
will not train new models. It will extend the already accepted `TE Curve Verification Pipeline`
offline verification surface so selected candidates can be compared on richer
curve-shape diagnostics, not only on the aggregate metrics already available in
`CVP 1.1`.

The goal is to decide the next modeling branch with stronger evidence:

- whether existing paper-reference, RCIM Model-Bank Reproduction, Wave 1, Wave 2.2, or Wave 2.3
  candidates fail because of amplitude, phase, local slope, or continuity
  errors;
- whether a retraining pass should change the loss/reranking objective for
  existing families;
- whether a new model-family wave is justified before adding curve-aware
  losses;
- which candidates are practical compensation starting points under continuous
  motor motion.

The runtime input constraint remains unchanged. Candidate models consume only
the current point-level operating state, an explicitly supported short causal
history of already observed points, or derived causal features. Full curves are
used only for validation, diagnostics, report generation, and promotion
decisions.

No subagent is planned for this phase.

## Technical Approach

The implementation should reuse the existing `TE Curve Verification Pipeline` evaluator rather than
introducing a new dataset or training surface.

The branch should:

- identify a compact screened candidate set from `CVP 1.1`;
- run or reuse `TE Curve Verification Pipeline` evaluation with curve payloads enabled for that set;
- export per-curve truth and prediction arrays in a machine-readable bundle;
- compute diagnostics that explain curve-following quality:
  - peak-to-peak normalized error;
  - selected harmonic amplitude error;
  - selected harmonic phase error;
  - local derivative or slope error;
  - residual smoothness or residual autocorrelation indicators;
  - boundary mismatch when representative revolutions are stitched in
    sequence;
- keep direction-valid reporting separated into `global`, `Fw`, and `Bw`
  surfaces;
- generate a canonical Markdown report with tables and interpretation focused
  on compensation readiness.

The first pass should stay conservative. If a diagnostic requires assumptions
that are not yet robust, the implementation should mark that diagnostic as
experimental or deferred rather than blocking the report.

The branch must not update family registries or the program-best registry
automatically. It creates analysis evidence for the later training or promotion
decision.

## Involved Components

Primary documentation targets:

- `doc/reports/analysis/track2/`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/README.md`

Primary implementation targets to inspect:

- `scripts/reports/analysis/build_track2_curve_first_reranking_report.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`

Primary data and artifact inputs:

- `doc/reports/analysis/track2/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`
- `output/validation_checks/track2_curve_first_reranking/2026-05-28-19-27-46__track2b_curve_first_reranking/track2_curve_first_reranking_summary.yaml`
- latest accepted `TE Curve Verification Pipeline` validation summary under
  `output/validation_checks/track2_reference_comparison/`
- current model artifacts under `models/`
- family and program registries under `output/registries/`

Initial screened candidate set:

| Role | Candidate |
| --- | --- |
| Forward curve-first leader | `rcim_retuned_GBM19_Fw` |
| Backward curve-first leader | `rcim_retuned_GBM19_Bw` |
| Strong scalar registry winner | `periodic_gru_sequence_Bw` |
| Best global curve-first surface | `periodic_lstm_sequence_global` |
| Strong Wave 2.3 backward residual candidate | `residual_harmonic_lstm_sequence_sparse_rcim_Bw` |
| Strong Wave 2.3 global residual candidate | `residual_harmonic_lstm_sequence_sparse_rcim_global` |
| Wave 1 structured baseline | `harmonic_regression_Bw` or direction-valid harmonic leader after inspection |
| Negative/simple-shape comparison | `tree_Bw` and/or `tree_global` |

The final implementation may adjust this list if the current candidate
inventory or payload availability makes a candidate unsuitable.

## Implementation Steps

1. Inspect the current `TE Curve Verification Pipeline` evaluation support code and confirm the
   existing curve-payload switch, output schema, and candidate filtering path.
2. Define a compact candidate configuration for the screened `CVP 1.2`
   diagnostic set.
3. Implement a repository-owned report script or extension that exports curve
   payloads without changing model inputs or dataset structure.
4. Add deterministic curve diagnostics:
   - peak-to-peak normalized error;
   - harmonic amplitude and phase error for selected orders;
   - local derivative or slope error;
   - residual smoothness statistics;
   - stitched-revolution boundary mismatch.
5. Write machine-readable outputs under
   `output/validation_checks/track2_curve_payload_diagnostics/<run_instance_id>/`.
6. Generate a dated report under
   `doc/reports/analysis/track2/curve_payload_diagnostics_report/[YYYY-MM-DD]/`.
7. Update script-level documentation if a new operator-facing script is added.
8. Update `doc/running/te_model_live_backlog.md`,
   `doc/reports/analysis/Training Results Master Summary.md`, and `doc/README.md`
   with the diagnostic conclusion.
9. Update `doc/guide/project_usage_guide.md` and the Sphinx portal if the work
   adds or changes a runnable user-facing script.
10. Run Markdown QA on touched authored Markdown.
11. Run Sphinx with warnings as errors if the touched scope affects the portal.
12. Stop after reporting completion; do not commit until the user explicitly
    requests it.

The expected next decision after `CVP 1.2` is one of:

- prepare a compact curve-aware retraining pass for existing families;
- prepare a new family wave with stronger curve-shape inductive bias;
- keep current candidates and move toward deployment/export preparation;
- extend diagnostics again if curve-payload evidence is still inconclusive.
