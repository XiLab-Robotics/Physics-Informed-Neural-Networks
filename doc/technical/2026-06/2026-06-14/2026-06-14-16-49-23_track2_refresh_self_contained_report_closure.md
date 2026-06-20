# TE Curve Verification Pipeline Refresh Self-Contained Report Closure

## Overview

Repeated `TE Curve Verification Pipeline` verification refreshes currently require a manual Codex
closure step after the operator launcher completes. The launcher runs the
matrix, collage builder, overlay builder, visual coverage validation, and PDF
export for the two visual reports, but it does not generate or export the
official model-verification decision report. This leaves the final PDF package
stale or incomplete until Codex re-runs report tooling manually.

The fix is to make the operator launcher produce a self-contained report
closure package: matrix, visual reports, official decision report, and PDF
exports must all be generated from the same run artifacts before the launcher
prints completion.

## Technical Approach

Add a repository-owned official `TE Curve Verification Pipeline` refresh report builder that reads the
latest matrix `validation_summary.yaml`, collage summary, overlay summary, and
launcher metadata. The builder will write the dated official Markdown report
under `doc/reports/analysis/track2/official_model_verification_report/` and
copy enough evidence paths into the report for the styled PDF export.

Patch the `TE Curve Verification Pipeline` refresh launchers so the normal path performs:

1. matrix refresh;
2. best-model collage generation;
3. multi-model overlay generation;
4. visual source-coverage validation;
5. official verification report generation;
6. styled PDF export for collage, overlay, and official report.

The launcher should still support `-SkipVisualReports` and `-SkipPdfExport`.
If visual reports are skipped, the official report builder may either skip or
emit a matrix-only report explicitly marked as lacking visual evidence. The
default path must be the complete package.

Remote mode must sync the generated official report bundle and PDF back to the
local repository through the artifact manifest. Launcher documentation should
state that the command now produces the complete closure package and that Codex
only needs to inspect/validate/synchronize status afterward, not regenerate the
reports.

## Involved Components

- `scripts/campaigns/track_2/run_track2h_mixture_density_heads_track2_verification_refresh.ps1`
- `scripts/campaigns/track_2/run_track2h_quantile_probabilistic_track2_verification_refresh.ps1`
- `scripts/campaigns/track_2/run_track2h_track2_verification_refresh.ps1`
- shared `TE Curve Verification Pipeline` refresh launchers for earlier branches where the same
  pattern exists
- `scripts/reports/analysis/` official `TE Curve Verification Pipeline` report builder to add
- `scripts/reports/pdf/run_report_pipeline.py`
- `doc/scripts/campaigns/track_2/` launcher notes
- `doc/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Implement a reusable official `TE Curve Verification Pipeline` verification report builder that can
   be called from PowerShell with `--matrix-summary-path`,
   `--collage-summary-path`, `--overlay-summary-path`, `--report-date`,
   `--refresh-label`, `--candidate-source-label`, and decision metadata.
2. Add report-local table layout defaults that match the recurring TE Curve Verification Pipeline PDF
   requirements: narrow rank/profile columns, wider candidate/source columns,
   equal metric columns, and no technical-document section in the final PDF.
3. Patch the current `Wave 4 series` refresh launchers so PDF export includes the
   official report path after visual report generation.
4. Patch artifact manifest generation so local and remote runs include the
   official report bundle.
5. Update launcher notes and documentation indices to describe the
   self-contained closure behavior.
6. Run focused PowerShell/script validation, Python compile checks, Markdown
   checks on touched Markdown, and the styled PDF pipeline on the current
   `Wave 4.3` mixture-density heads artifacts to prove the official report is
   included without manual reruns.

No subagent is planned for this change.
