# Retroactive Model Report Diagrams And PDF Image Integration

## Overview

This document defines the work required to retroactively add explanatory diagrams to the four already created structured-model reports and to ensure that the same images are preserved in the exported PDFs.

The scope covers:

- diagram generation for the existing explanatory reports;
- integration of those diagrams into the Markdown reports;
- support or verification for image rendering in the styled PDF exporter;
- export and validation of the final PDFs.

The target reports are:

- `feedforward`
- `harmonic_regression`
- `periodic_feature_network`
- `residual_harmonic_network`

## Technical Approach

The work will proceed in four linked stages.

1. Create report-local visual assets
   Each model report will receive one or more compact schematic images that explain:
   - the model structure;
   - the main data flow;
   - the branch structure when relevant.

2. Integrate the images into the Markdown reports
   The diagrams will be inserted in the conceptual explanation sections instead of leaving the reports purely text-based.

3. Extend or verify PDF image support
   The current styled PDF exporter already handles headings, lists, paragraphs, and tables, but it does not currently expose explicit Markdown image rendering logic. The exporter will therefore need either:
   - explicit Markdown image support; or
   - another equivalent repository-owned path that preserves local report images in the exported PDF.

4. Export and validate the final PDFs
   After the image integration is complete, the four reports will be exported to PDF and validated with the existing PDF validation workflow.

The preferred image format is a repository-friendly vector or high-quality static asset that remains crisp in PDF export and does not add heavy dependencies unless truly necessary.

## Involved Components

The work will involve:

- `doc/reports/analysis/2026-03-18-00-31-18_feedforward_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-31-58_harmonic_regression_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-32-37_periodic_feature_network_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-33-16_residual_harmonic_network_model_explanatory_report.md`

- a new report-local asset location for model-report diagrams
  This will store the generated images in a discoverable way near the reports they support.

- `scripts/reports/generate_styled_report_pdf.py`
  May need explicit support for Markdown image rendering and image styling in the exported HTML/PDF.

- `scripts/reports/validate_report_pdf.py`
  Will be used to validate the final exported PDFs.

- `README.md`
- `doc/README.md`
  Documentation indexes for the new technical note and the resulting PDF artifacts.

## Implementation Steps

1. Create a consistent asset location for the model-report diagrams.
2. Generate one or more schematic images for each of the four existing model reports.
3. Insert the generated images into the corresponding Markdown reports.
4. Extend or verify the styled PDF exporter so embedded report images render correctly.
5. Export one PDF per report.
6. Validate each exported PDF using the existing rasterization workflow.
7. Update the documentation indexes with the resulting `.pdf` artifacts if needed.
