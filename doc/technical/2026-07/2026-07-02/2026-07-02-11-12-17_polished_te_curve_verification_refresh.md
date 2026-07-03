# Polished-Dataset TE Curve Verification Pipeline Refresh

## Overview

This document plans the separate official `TE Curve Verification Pipeline`
refresh for the completed `polished_dataset` retraining work. The refresh must
cover the polished closeouts already committed locally:

- `ddb05003fdc108a514084936fe7cd741fc658417`: polished
  `RCIM Model-Bank Reproduction` closeout.
- `fd68c7ba682dd0dc54ec06b65ab2a2a3689e8be2`: polished early-wave parallel
  retraining closeout.
- `21342ca5bf87bfe91dbc19e16d9bced46d7611f8`: polished full-wave retraining
  closeout.

The normal campaign closeouts are complete, but they intentionally did not run
the heavy official curve-verification matrix. The missing deliverable is a
complete direction-aware `TE Curve Verification Pipeline` report package that
evaluates the newly retrained polished candidates against the existing
reference, paper-derived, and model-development baselines.

The current campaign state is clear: `doc/running/active_training_campaign.yaml`
has `status: none`, records the full-wave campaign as the latest completed
campaign, and marks the polished RCIM, early-wave, and full-wave closeouts as
`te_curve_verification_status: not_run_in_closeout`.

No subagent use is planned. If a subagent becomes useful, its scope must be
declared and explicitly approved before launch.

## Technical Approach

The refresh will follow the repository's operator-launched verification pattern:
Codex prepares the matrix configuration, launcher, launcher note, and status
bookkeeping, then stops and provides exact local and `-Remote` commands. The
operator runs the launcher. After completion, Codex inspects the generated
artifacts, validates the PDFs, and synchronizes the official status documents.

The matrix will use the existing full direction-aware configuration:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`

The launcher will be a dedicated polished refresh wrapper under:

- `scripts/campaigns/track_2/`

The launcher note will be added under:

- `doc/scripts/campaigns/track_2/`

The wrapper must support local execution and `-Remote`, sync the required
registry and training artifacts for the polished candidate families, and write
operator logs under:

- `output/validation_checks/track2_operator_launch_logs/`

The refresh must preserve the direction semantics already used by the
verification matrix:

| Surface | Training or archive scope | Evaluation scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

The final decision must use the repository's multi-index curve-first selection
policy, not scalar campaign leaderboard rank alone. The decision evidence must
distinguish raw error, mean-centered shape fidelity, offset / continuity
behavior, harmonic / phase fidelity, robustness, visual evidence, and
deployment readiness when the artifacts expose those dimensions.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  - Must remain clear before launcher preparation.
  - Will be updated only to record the prepared verification refresh if the
    repository convention requires it for operator visibility.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  - Candidate-source blocks must be checked against the current polished
    registry state.
  - Existing registry-backed candidate blocks may already resolve many polished
    families through the latest family registries; missing polished-specific
    source grouping must be added explicitly.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - Must be inspected before patching.
  - Should only change if polished candidates need new inference-shape or
    registry-loading support.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
  - Matrix execution entry point.
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
  - Collage report generation.
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
  - Multi-model overlay report generation.
- `scripts/reports/analysis/build_track2_official_model_verification_report.py`
  - Official decision report generation.
- `scripts/reports/pdf/run_report_pipeline.py`
  - Styled PDF export and validation.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - Canonical matrix report.
- `doc/reports/analysis/track2/best_model_collage_report/[2026-07-02]/`
  - Expected dated collage bundle for this refresh.
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-07-02]/`
  - Expected dated overlay bundle for this refresh.
- `doc/reports/analysis/track2/official_model_verification_report/[2026-07-02]/`
  - Expected dated official verification report bundle.
- `doc/reports/analysis/track2/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`
  - Canonical decision policy.
- `doc/running/te_model_live_backlog.md`
  - Must be synchronized after the official decision.
- `doc/reports/analysis/Training Results Master Summary.md`
  - Must be synchronized after the official decision.
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`
  - Must be synchronized after the official decision or explicitly checked as
    unchanged.

## Implementation Steps

1. Inspect the current matrix template and support code to determine whether the
   polished candidates can be represented through existing registry-backed
   blocks or require polished-specific candidate-source blocks.
2. Build the expected candidate inventory from the three polished closeouts:
   polished RCIM, polished early-wave, and polished full-wave retraining.
3. Add or adjust matrix candidate blocks so the new polished candidates are
   visible with stable source labels and direction surfaces.
4. Add a dedicated operator launcher for the polished verification refresh with:
   - local execution;
   - `-Remote` execution;
   - UTF-8/no-capture conda execution;
   - log capture under `output/validation_checks/track2_operator_launch_logs/`;
   - artifact manifest synchronization for remote mode.
5. Add a launcher note documenting the exact local and remote commands, expected
   outputs, and post-run closeout responsibility.
6. Update any required protected campaign-state or index document only after
   confirming no active campaign is protected.
7. Run package validation that does not execute the heavy matrix:
   - PowerShell syntax parsing for the launcher.
   - Python syntax checks for modified Python files, if any.
   - YAML parse checks for modified matrix configuration.
   - Markdown checks for touched authored Markdown.
8. Stop and provide the exact operator commands. Do not run the heavy
   verification matrix inside Codex during preparation.
9. After the operator reports completion, inspect the matrix summary, generated
   visual reports, official report, logs, and artifact manifest.
10. Export and validate the real PDFs for the collage, overlay, and official
    verification report.
11. Update the backlog, master summary, and TE closeout ledger with the official
    curve-verification decision.
12. Run final QA and wait for explicit commit approval.
