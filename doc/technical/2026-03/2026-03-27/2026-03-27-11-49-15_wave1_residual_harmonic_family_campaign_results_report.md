# Wave 1 Residual Harmonic Family Campaign Results Report

## Overview

The aligned `Wave 1` residual-harmonic family campaign has completed and its
artifacts are now consistently named under the `Wave 1` scope.

The next task is to produce the mandatory final campaign-results deliverable in
`doc/reports/campaign_results/`, including:

- the canonical Markdown report;
- the styled PDF export;
- real post-export PDF validation against the repository report standard.

The report must synthesize the full campaign ranking, identify the best
configuration explicitly, interpret the main residual-family trends, and record
practical follow-up actions.

## Technical Approach

The reporting workflow should reuse the repository-owned campaign artifacts and
styled-report tooling instead of rebuilding the comparison manually.

The planned approach is:

1. read the aligned campaign manifest, leaderboard, best-run summary, and the
   per-run `metrics_summary.yaml` / `training_test_report.md` artifacts;
2. write a campaign-results Markdown report in
   `doc/reports/campaign_results/` with clear sections for overview, ranking,
   configuration comparison, winner analysis, interpretation, and next steps;
3. export the report to PDF using the repository styling pipeline;
4. validate the real exported PDF output and only consider the task complete if
   the exported pages pass the expected layout checks.

## Involved Components

- `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/`
  Campaign-level manifest, leaderboard, best-run files, and execution report.
- `output/training_runs/residual_harmonic_mlp/`
  Per-run metric snapshots and training reports for the 15 aligned campaign runs.
- `output/registries/families/residual_harmonic_mlp/`
  Family-level leaderboard and best-run registry that should stay consistent
  with the final report narrative.
- `doc/reports/campaign_results/`
  Destination for the final Markdown report and styled PDF.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF export entry point.
- `scripts/reports/validate_report_pdf.py`
  Real-PDF validation entry point.
- `scripts/reports/run_report_pipeline.py`
  Repository orchestration utility for export and validation.
- `README.md`
  Main project document that must reference this technical note.

## Implementation Steps

1. Read the aligned campaign outputs and collect the final ranking plus the
   most relevant per-run metrics and interpretations.
2. Create the final campaign-results Markdown report under
   `doc/reports/campaign_results/`.
3. Export the report to a styled PDF using the repository-owned report tooling.
4. Validate the real exported PDF output and correct any layout problems if
   necessary.
5. Update `README.md` with this technical note reference if needed.
6. Report completion and wait for explicit user approval before creating any
   Git commit.
