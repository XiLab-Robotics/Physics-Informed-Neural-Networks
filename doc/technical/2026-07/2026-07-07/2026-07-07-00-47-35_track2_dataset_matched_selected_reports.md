# Track 2 Dataset-Matched Selected Reports

## Overview

The reduced selected-model `TE Curve Verification Pipeline` reports generated
on `2026-07-06` need correction because the `simplified_dataset` reports reused
`polished_*` model candidates. This was not a wording-only problem: the reduced
matrix changed the evaluation dataset root but kept the candidate list tied to
polished model-development registries and polished RCIM reproduction artifacts.

The visual report builder also selected the four collage curves independently
per report. That makes the polished and simplified visual evidence harder to
compare, because the two dataset reports may show different operating
conditions for the same direction and candidate family.

## Technical Approach

The correction will enforce two separate rules.

First, model candidates must be dataset-matched:

- `polished_dataset` reports may use only `polished_*` model-development
  candidates, polished RCIM model-bank candidates, and other explicitly
  polished artifacts.
- `simplified_dataset` reports may use only simplified/original-dataset model
  candidates and must not silently resolve to `polished_dataset` registry
  winners.
- The same dataset/source rule applies to `forward`, `backward`, paused
  candidates, and future `global` candidates when global is eventually resumed.
- If a requested dataset-specific model artifact does not exist, the report
  generation must fail or mark the candidate unavailable instead of substituting
  a candidate from the other dataset.

Second, visual evidence curves must be aligned:

- For each direction, choose one canonical four-condition curve set.
- Use the same four operating conditions for `polished_dataset` and
  `simplified_dataset` reports in that direction.
- Keep forward and backward curve sets separate, because the phenomena are
  direction-specific.
- Record the selected condition keys in the generated report artifacts so
  future reruns remain auditable.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reduced_selected_track2_matrix.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/reports/analysis/build_track2_selected_model_visual_reports.py`
- `scripts/campaigns/track_2/run_reduced_selected_track2_reports.ps1`
- `doc/scripts/campaigns/track_2/run_reduced_selected_track2_reports.md`
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-06]/`
- `output/validation_checks/track2_reference_comparison/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`

Some involved files are listed as protected in
`doc/running/active_training_campaign.yaml`. Editing protected files requires a
separate explicit approval after the critical warning is surfaced.

## Implementation Steps

1. Audit current reduced reports, matrix YAML, and validation summaries to list
   every candidate whose model source does not match the report dataset.
2. Resolve the correct simplified/original-dataset candidate artifacts for the
   selected families. If a family has no valid simplified artifact, mark it
   unavailable instead of using the polished replacement.
3. Add dataset-source validation to the Track 2 candidate resolution path so
   `polished_dataset`, `simplified_dataset`, and future `global` runs cannot
   silently mix model artifacts across dataset roots.
4. Update the reduced selected-model matrix so polished and simplified reports
   use separate dataset-matched candidate sets.
5. Update the selected visual-report builder to derive one shared four-curve
   condition set per direction and reuse it for both datasets.
6. Regenerate the four selected reports, PDFs, collage assets, and validation
   artifacts.
7. Audit paused/non-generated Track 2 report builders and global-facing config
   text so the dataset-matched rule is documented for paused candidates and
   future global reactivation.
8. Run Python compile checks, Markdown checks, PDF export/validation, visual
   spot checks, and Sphinx portal build before closing the correction.
