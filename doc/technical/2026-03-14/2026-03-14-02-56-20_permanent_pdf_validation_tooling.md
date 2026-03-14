# Permanent PDF Validation Tooling

## Overview

The repository already contains a stable report exporter:

- `scripts/reports/generate_styled_report_pdf.py`

What is still missing is a permanent, reusable validation tool for the real exported PDF. At the moment the PDF-validation step is repeatedly reconstructed with ad hoc commands:

- temporary dependency setup;
- temporary rasterization commands;
- temporary screenshot cleanup.

This is slower than necessary and makes the validation workflow harder to repeat consistently. A permanent validation utility would reduce repeated setup work and make PDF quality checks easier to run after every report change.

## Technical Approach

The best practical approach is to add a dedicated validation script instead of continuing to rebuild the workflow manually.

Recommended structure:

1. keep `scripts/reports/generate_styled_report_pdf.py` focused on export;
2. add a new script such as `scripts/reports/validate_report_pdf.py`;
3. use a stable PDF renderer directly from Python to rasterize the exported PDF pages into deterministic preview images;
4. emit a compact validation summary with:
   - page count;
   - generated raster paths;
   - optional quick warnings when page count is zero, file is missing, or rasterization fails.

For repeatability and speed, the validator should rely on an installed Python dependency instead of creating throwaway environments per run. The most practical candidate is `PyMuPDF`, because it provides direct page rasterization with a simple local API and avoids browser-PDF-viewer quirks during validation.

This means the implementation would likely include:

- a reusable raster-validation script under `scripts/reports/`;
- `pymupdf` added to `requirements.txt`;
- usage guidance added to `doc/guide/project_usage_guide.md`.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
  Existing export script that should remain the canonical PDF generator.
- `scripts/reports/validate_report_pdf.py`
  Proposed new permanent validator for real exported PDFs.
- `requirements.txt`
  Will need the validation dependency tracked if the script uses `PyMuPDF`.
- `doc/guide/project_usage_guide.md`
  Must document the new validation workflow before the final commit.
- `README.md`
  Main project index that must reference this technical note.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. After user approval, add `scripts/reports/validate_report_pdf.py`.
3. Implement argument parsing for:
   - input PDF path;
   - output image directory;
   - optional raster scale or DPI-like multiplier.
4. Rasterize each PDF page to PNG and print a compact validation summary.
5. Add `pymupdf` to `requirements.txt`.
6. Update `doc/guide/project_usage_guide.md` with the permanent export-plus-validation workflow.
7. Use the new script to revalidate the updated campaign report PDF and confirm the workflow replaces the current ad hoc temporary-command path.
