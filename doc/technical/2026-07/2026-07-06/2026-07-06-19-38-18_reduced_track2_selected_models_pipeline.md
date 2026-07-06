# Reduced TE Curve Verification Pipeline For Selected Models

## Overview

This document plans the repository-wide integration of the model-family
pruning decision into the `TE Curve Verification Pipeline`, report generation,
script documentation, and operational backlog.

The requested target state is a simplified active verification surface:

- evaluate only selected model families;
- exclude `global` from active generation;
- generate four active reports only:
  - `polished_dataset` / `forward`;
  - `polished_dataset` / `backward`;
  - `simplified_dataset` / `forward`;
  - `simplified_dataset` / `backward`;
- pause overlay reports with multiple models superimposed;
- pause simplified-vs-polished comparison reports;
- keep all broad, global, overlay, collage, and dataset-difference reports
  available only as explicit on-demand workflows.

This work changes reporting and verification tooling, not training. No new
training campaign is planned by this document.

## Technical Approach

The implementation should add an explicit reduced selected-model pipeline
instead of destructively rewriting the broad historical `TE Curve Verification
Pipeline`.

The active selected-model candidate set will be based on the approved pruning
report:

- `periodic_gru_sequence`;
- `periodic_mlp_harmonic`;
- `wave4_3_mixture_density_k3`;
- `wave52b_offset_centered_shape_harmonic`;
- selected anchors:
  - RCIM forward/reference anchors where available;
  - `feedforward`;
  - `tree`;
  - `harmonic_regression`.

The reduced pipeline will support two datasets and two direction scopes:

| Dataset | Direction |
| --- | --- |
| `polished_dataset` | `forward` |
| `polished_dataset` | `backward` |
| `simplified_dataset` | `forward` |
| `simplified_dataset` | `backward` |

The active report generation should produce separate report bundles for each
of these four surfaces. `global` rows must not be generated in the active
reduced flow.

The broad historical pipeline must remain reproducible. Existing full-matrix,
global, visual overlay, collage, and simplified-vs-polished comparison tools
should be marked as paused / on-demand in documentation and default workflow
notes, not deleted.

## Involved Components

Expected implementation targets after approval:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  for a reduced selected-model matrix configuration or equivalent candidate
  manifest;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
  only if the existing dataset and scope filtering is insufficient;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  only if selected-candidate filtering cannot be expressed in config;
- a new or updated launcher under `scripts/campaigns/track_2/`;
- a matching launcher note under `doc/scripts/campaigns/track_2/`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  if the active report surface changes enough to affect the master summary;
- relevant `doc/scripts/reports/analysis/` notes for paused report builders;
- newly generated selected-model report outputs under
  `doc/reports/analysis/te_curve_verification_pipeline/`;
- validation artifacts under `output/validation_checks/`.

Protected-file check:

- `doc/running/active_training_campaign.yaml` records the polished-dataset
  `TE Curve Verification Pipeline` refresh as completed and closed.
- The previous refresh still lists protected files, including
  `full_track2_matrix_template.yaml`,
  `reference_family_vs_feedforward_support.py`,
  `build_track2_official_model_verification_report.py`, and the previous
  polished refresh launcher/note.
- This implementation should avoid editing those listed protected files where
  possible by adding new reduced selected-model entry points.
- If implementation proves that one of those listed files must be edited, issue
  a `CRITICAL WARNING` and obtain explicit user approval before modifying that
  file.

No subagent is planned. If later review would benefit from a subagent, its
name, reason, and exact scope must be recorded and explicitly approved before
launch.

## Implementation Steps

1. Obtain explicit user approval for this technical document.
2. Inventory the current matrix runner, candidate configuration, dataset-scope
   filtering, launchers, and report builders.
3. Define the reduced selected-model candidate manifest and verify that all
   selected candidates resolve to existing registry or reference artifacts for
   the relevant dataset and direction.
4. Add a reduced selected-model configuration or runner option that excludes
   `global` and includes only selected candidates.
5. Add or update a Track 2 launcher that generates exactly four active reports:
   polished forward, polished backward, simplified forward, simplified
   backward.
6. Mark broad/global/full-matrix visual overlay, collage, and
   simplified-vs-polished comparison report generation as paused / on-demand in
   launcher notes, script notes, backlog, and status documents.
7. Generate the four reduced selected-model reports and store them under a
   dated selected-model report root.
8. Validate generated YAML/CSV/Markdown artifacts and confirm no `global`
   report is produced by the active flow.
9. Run Python validation for touched scripts, scoped Markdown QA, and Sphinx if
   portal scope changes.
10. Report completion and wait for explicit commit approval.
