# TE Curve Verification Dataset-Surface Launcher Post-Rebase Fix

## Overview

The dataset/surface split launcher was prepared before the full-wave polished
closure and before the analysis-report directory reorganization settled on the
canonical `te_curve_verification_pipeline` tree. After merging the closure
commits, the launcher needs a small compatibility pass before it can be used as
the operator entry point for the new split reports.

## Technical Approach

The fix keeps the launcher conservative: it should still refuse to run while a
training campaign is prepared or active, but it must accept the current
post-closeout `completed` state when the TE refresh itself is marked completed
and the operator supplies the explicit full-wave closure acknowledgement.

The visual-report and dataset-difference output roots will also be aligned with
the canonical post-reorganization analysis tree under
`doc/reports/analysis/te_curve_verification_pipeline/`.

The crash observed in the forward overlay resume path will be fixed by making
the screened Wave 1 overlay selection tolerate single-direction metric
summaries. The launcher will also stream each child process live while logging
it, and progress bars will use ASCII output plus raw launcher-side
carriage-return handling to avoid mojibake, PowerShell stderr error-record
noise, and line-per-refresh `tqdm` output in Windows PowerShell logs.

The simplified-dataset cross-check will also adapt pointwise and sequence input
matrices to each loaded model's declared feature contract. This prevents
polished-schema checkpoints that expect four features from receiving the
simplified five-feature matrix with `direction_flag`.

The matrix template and support default paths will be realigned so the
canonical directional comparison report is regenerated under
`doc/reports/analysis/te_curve_verification_pipeline/00_overview/` instead of
the retired `doc/reports/analysis/track2/` tree.

## Involved Components

- `scripts/campaigns/track_2/run_track2_dataset_surface_report_split.ps1`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_dataset_difference_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `doc/scripts/campaigns/track_2/run_track2_dataset_surface_report_split.md`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Update the launcher gate to accept `status: none` or the completed polished
   TE refresh state, while still rejecting prepared/running campaign states.
2. Move dataset/surface visual report roots from legacy `track2` paths to
   `te_curve_verification_pipeline/02_visual_reports/dataset_surface_report/`.
3. Move the dataset-difference builder default topic root to
   `te_curve_verification_pipeline/03_cvp_diagnostics/dataset_difference_report/`.
4. Keep the launcher note aligned with the actual generated paths.
5. Add `-ResumeFromStep` so a failed long run can continue from a named step
   without recomputing already-completed matrix or collage reports.
6. Use ASCII, fixed-width `tqdm` progress bars and live PowerShell tee logging
   for more readable operator feedback.
7. Move the matrix canonical report path and default validation-report root out
   of the retired `track2` report tree.
8. Add a launcher-owned progress smoke test that exercises the same `conda run`
   wrapper without loading TE model candidates and verifies the child-process
   working directory.
9. Adapt cross-dataset candidate inference to the loaded model input-feature
   dimension before normalization.
10. Validate syntax, dry-run behavior, gate logic, Markdown hygiene, and diff
   cleanliness without launching the heavy TE matrix.
