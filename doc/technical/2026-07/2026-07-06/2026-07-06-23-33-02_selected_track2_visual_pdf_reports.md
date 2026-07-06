# Selected TE Curve Verification Visual PDF Reports

## Overview

This document plans the correction of the reduced selected-model `TE Curve
Verification Pipeline` reports so that the delivered PDFs are complete visual
reports, not table-only exports.

The current reduced reports correctly evaluate the selected candidates across:

- `polished_dataset` / `forward`;
- `polished_dataset` / `backward`;
- `simplified_dataset` / `forward`;
- `simplified_dataset` / `backward`.

However, the generated PDFs are incomplete for review because:

- they do not include the expected measured-versus-predicted curve collages;
- the PDF table column proportions are not tuned for Track 2 selected-model
  tables;
- the `Candidate Inventory` table needs wider `Candidate` and `Source`
  columns, narrower `Family` and `Surface` columns, and a less crushed layout
  for long identifiers;
- the report-building rules are not yet encoded as stable report/PDF policy.

The target deliverable is a regenerated set of four selected-model Markdown
and PDF reports with curve evidence and table layout rules suitable for future
reuse.

## Technical Approach

The implementation should keep the reduced reporting policy intact:

- do not regenerate `global`;
- do not re-enable broad full-matrix reporting by default;
- do not re-enable the old overlay or simplified-vs-polished reports as the
  active default;
- generate only the four selected-model report surfaces listed above.

The visual report should include, for each selected surface, a compact collage
section with measured TE and predicted TE curves. The collage should use a
bounded number of representative curves, preferably four curves per report,
and should be tied to the candidate set used by the reduced selected-model
matrix.

Candidate choice for the visual section should be explicit and reproducible.
The first implementation should include the strongest candidate from the
selected-model matrix for each report surface, with room to add future
replacement candidates later if requested.

The PDF table rules should be implemented in the repository-owned PDF exporter
instead of manually editing exported HTML. At minimum:

- add a Track 2 selected-candidate inventory table class;
- use a wider first column for `Candidate`;
- use a wider `Source` column;
- compress `Family`, `Kind`, `Surface`, and `Valid Directions`;
- preserve numeric metric tables with stable, readable widths;
- validate with real rasterized PDF pages before accepting the result.

The generated Markdown reports should reference the collage image files using
repository-relative image paths that the existing styled PDF exporter can
embed. The companion image assets should live inside the dated selected-model
report bundle so the report folder remains self-contained.

## Involved Components

Expected implementation targets after approval:

- `scripts/reports/analysis/` for a selected-model visual report builder or
  an extension around the existing Track 2 curve-plotting utilities;
- `scripts/reports/pdf/generate_styled_report_pdf.py` for stable PDF table
  layout rules;
- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-06]/`
  for regenerated Markdown, PDF, and collage assets;
- `output/validation_checks/track2_reference_comparison/` for the existing
  selected-model matrix summaries and per-condition metrics used as source
  data;
- `.temp/report_pipeline/pdf_validation/` for PDF raster validation evidence;
- `doc/scripts/campaigns/track_2/run_reduced_selected_track2_reports.md` if
  the launcher note needs to document the final visual/PDF behavior;
- `doc/README.md`, `doc/running/te_model_live_backlog.md`, and current project
  status reports only if the final report locations or policy wording changes.

Protected-file check:

- `doc/running/active_training_campaign.yaml` records the previous polished
  `TE Curve Verification Pipeline` refresh as completed and closed.
- The protected list still includes `full_track2_matrix_template.yaml`,
  `reference_family_vs_feedforward_support.py`,
  `build_track2_official_model_verification_report.py`, and the previous
  polished refresh launcher/note.
- This work should avoid those protected files. If one becomes necessary, issue
  a `CRITICAL WARNING` and wait for explicit approval before editing it.

No subagent is planned. If later visual/PDF review would benefit from a
subagent, the exact subagent name, reason, and delegated scope must be recorded
and explicitly approved first.

## Implementation Steps

1. Obtain explicit user approval for this technical document.
2. Inspect the existing Track 2 collage/curve plotting builders, selected-model
   validation summaries, per-condition metrics, and PDF exporter table logic.
3. Define the selected-model visual report contract: four reports, four
   representative curves per report, measured-versus-predicted overlays, and
   no `global`.
4. Implement a selected-model report builder or targeted augmentation step that
   inserts the collage section and writes the companion image assets into the
   dated report folder.
5. Implement reusable PDF table layout rules for selected Track 2 reports,
   including improved `Candidate Inventory` proportions.
6. Regenerate the four selected-model Markdown reports and their PDFs.
7. Raster-validate all four PDFs and inspect representative pages for clipped
   borders, crushed identifiers, table fit, and collage visibility.
8. Run Python validation for modified scripts, Markdown style checks,
   Markdownlint, and Sphinx if documentation or portal scope changes.
9. Report the final artifact paths, validation evidence, and any residual
   layout limitations. Wait for explicit commit approval before committing.
