# TE Curve Verification Pipeline Dataset-Surface Report Split

## Overview

This technical document defines the preparation scope for a substantial
`TE Curve Verification Pipeline` rework that separates the current broad
single report into dataset-specific, surface-specific, and dataset-difference
report bundles with explicit progress logging.

The rework starts from the current repository state:

- the legacy and earlier wave candidates include models trained on
  `simplified_dataset`;
- the polished early-wave parallel campaign is already closed locally;
- the `Wave 5.2B` offset and harmonic guided campaign is closed locally as
  scalar evidence on `polished_dataset`;
- the external 108-run full-wave polished retraining campaign is reported by
  the operator as finished and currently closing out on the other workstation,
  but its local merge and artifact acceptance are still pending;
- the existing `TE Curve Verification Pipeline` report remains a single broad
  matrix/report surface that can mix model source, training dataset, evaluation
  dataset, and direction scope too easily.

The implementation must prepare the code and launcher surfaces now, but the
real heavy pipeline launch must wait until the full-wave polished retraining
closure commits and artifacts are merged locally. The launcher must expose this
merge gate clearly instead of silently running against an incomplete local
candidate set.

No subagent is planned for this implementation. If a later review requires a
subagent, the proposed subagent name, delegated task boundary, and explicit
approval requirement must be recorded before launch.

## Technical Approach

The rework will turn the current single `TE Curve Verification Pipeline`
artifact set into a deterministic report family. Dataset identity must be
explicit at every entry point, artifact path, summary file, and report title.
The pipeline must not infer the evaluation dataset from mutable local config
state when the report name says `polished_dataset` or `simplified_dataset`.

The primary output family will contain six dataset-surface reports:

- `forward polished_dataset`;
- `backward polished_dataset`;
- `global polished_dataset`;
- `forward simplified_dataset`;
- `backward simplified_dataset`;
- `global simplified_dataset`.

The comparative output family will contain three dataset-difference reports:

- `forward simplified_dataset vs polished_dataset`;
- `backward simplified_dataset vs polished_dataset`;
- `global simplified_dataset vs polished_dataset`.

Each difference report should align matching operating conditions and show, at
minimum, the measured curve, the simplified-dataset candidate curve, and the
polished-dataset candidate curve on the same plot. Where the data are
available, it should also include the direct curve delta between the polished
and simplified predictions so the report is not only visual overlay.

The current broad matrix can remain as a compact index or inventory artifact,
but it should stop being the primary human-facing closeout report. Official
promotion decisions must still follow the multi-index curve-first selection
policy: raw error, mean-centered shape fidelity, offset and continuity,
harmonic or phase fidelity, robustness, visual evidence, and deployment
readiness must remain separate axes.

Progress logging will be added in two layers:

- launcher-level stage logs for each dataset, surface, report, export, and
  validation stage;
- Python-level progress for expensive loops such as candidate evaluation,
  curve reconstruction, collage generation, overlay generation, and dataset
  difference plotting.

The repository already uses `tqdm` in dataset tooling, so the implementation
may reuse that dependency pattern when available. The progress surface must
remain compatible with local and `-Remote` PowerShell execution, including
log-file capture and terminal-visible status lines.

## Involved Components

State and campaign gates:

- `doc/running/active_training_campaign.yaml`
- the full-wave polished retraining closure commits and synchronized artifacts
- `output/registries/families/`
- `output/training_campaigns/`
- `output/training_runs/`

Dataset and candidate matrix configuration:

- `config/datasets/transmission_error_dataset.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`

Report builders and validators:

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/reports/analysis/build_track2_official_model_verification_report.py`
- a new or extended dataset-difference report builder under
  `scripts/reports/analysis/`
- `scripts/reports/analysis/validate_track2_visual_source_coverage.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`

Operator-facing launcher and documentation to create or update:

- a dedicated PowerShell launcher under `scripts/campaigns/track_2/` or a
  clearly named cross-wave verification root;
- a matching launcher note under `doc/scripts/campaigns/track_2/` or the same
  topic-local documentation root;
- `doc/README.md`;
- the relevant Sphinx source pages under `site/` when the approved work
  changes canonical portal scope.

Expected report roots:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/dataset_surface_report/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/dataset_difference_report/`
- existing companion roots may remain for compatibility:
  `best_model_collage_report/`, `multi_model_curve_comparison_report/`, and
  `official_model_verification_report/`.

## Implementation Steps

1. Re-inspect `doc/running/active_training_campaign.yaml` and the worktree
   before code edits. Confirm no local protected campaign is active.
2. Treat the full-wave polished retraining campaign as operationally complete
   for planning, but keep a hard launch gate requiring its closure commits and
   artifacts to be merged locally before the heavy pipeline command is run.
3. Inventory the locally available simplified-trained and polished-trained
   candidate registries, including `Wave 5.2B` and the incoming full-wave
   polished retraining families after merge.
4. Patch the matrix runner and report builders so `--dataset
   polished_dataset|simplified_dataset` is propagated explicitly through
   matrix evaluation, collage generation, overlay generation, official
   summaries, artifact names, and report titles.
5. Remove or replace any hardcoded `source_contract: data/simplified_dataset`
   summary field so the summary records the actual resolved evaluation
   dataset.
6. Add surface filters for `forward`, `backward`, and `global` report bundles
   without changing the established direction semantics:
   - `Fw` candidates evaluate forward curves only;
   - `Bw` candidates evaluate backward curves only;
   - `global` candidates evaluate both directions while keeping direction
     breakdowns visible.
7. Create or extend a dataset-difference report builder that aligns shared
   operating conditions across `simplified_dataset` and `polished_dataset`,
   then plots measured curves, simplified-model predictions, polished-model
   predictions, and prediction deltas where available.
8. Add incremental progress logging with terminal-safe `tqdm` or equivalent
   repository-consistent progress output for candidate, curve, plot, and report
   loops.
9. Create the operator-facing launcher with local and `-Remote` modes. The
   launcher must support preparation and dry-run style validation without
   starting the heavy matrix, and it must refuse or warn clearly when the
   full-wave closure merge gate is not satisfied.
10. Create the launcher note with exact local and `-Remote` commands, expected
    output roots, progress/log locations, and the required merge gate before
    launch.
11. Run lightweight validation before requesting launch approval:
    - Python syntax checks for modified scripts;
    - launcher parser/preflight checks that do not execute the heavy matrix;
    - Markdown checks on touched authored Markdown;
    - Sphinx build if portal scope changes.
12. Stop before running the heavy `TE Curve Verification Pipeline` command.
    After the full-wave closure merge is present and the operator approves the
    launch, run or provide the final launcher command.
13. After operator completion, inspect the real matrix summaries, generated
    Markdown reports, plot bundles, PDFs, and validation images before updating
    official status documents.
14. Synchronize `doc/running/te_model_live_backlog.md`,
    `doc/reports/analysis/project_status/current/Training Results Master Summary.md`, and
    `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md` only after
    the split reports have been generated and reviewed.
