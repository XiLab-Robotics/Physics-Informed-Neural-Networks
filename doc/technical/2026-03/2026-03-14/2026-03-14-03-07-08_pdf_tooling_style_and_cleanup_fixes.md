# PDF Tooling Style And Cleanup Fixes

## Overview

The current PDF export and validation tooling has four issues that should be corrected together:

1. `scripts/reports/validate_report_pdf.py` does not yet match the repository programming style closely enough.
2. The validator imports `fitz`, which is inconvenient for local static analysis and currently triggers `Pylance reportMissingImports`.
3. The PDF export workflow still encourages persistent HTML preview files even when the real goal is only the final PDF artifact.
4. The temporary Chrome profile cleanup path is still fragile and can leave behind `doc/reports/campaign_results/.tmp_chrome_profiles/`, which then requires manual removal.

These are tooling-quality issues rather than model-training issues, but they directly affect the repeatability and cleanliness of the reporting workflow.

## Technical Approach

The fix should keep the current report-export behavior intact while tightening the implementation and cleanup workflow.

The recommended implementation is:

1. refactor `scripts/reports/validate_report_pdf.py` so it follows the local script style more closely:
   - grouped imports with short section comments;
   - explicit staged helper functions;
   - domain-explicit variable names;
   - concise title-case comments before logical blocks.
2. replace the direct `fitz` import with a package-level `pymupdf` import so dependency resolution is clearer to editors and static analyzers.
3. update `scripts/reports/generate_styled_report_pdf.py` so persistent HTML preview files are opt-in rather than the default expectation:
   - if an HTML path is explicitly requested, it can still be written;
   - if the user only wants the PDF, the script should be able to use a temporary HTML file and remove it automatically.
4. move temporary Chrome profile directories out of the report folder and into the operating-system temporary area so cleanup failures do not pollute the repository tree.
5. make temporary-profile cleanup more robust with explicit retry-oriented removal logic and a non-fatal warning path if a browser handle lingers briefly.

This approach is better than only suppressing the symptoms, because it fixes both the user-facing repository clutter and the underlying lifecycle of the export helper.

## Involved Components

- `scripts/reports/validate_report_pdf.py`
  Validator script that needs style alignment and dependency-import cleanup.
- `scripts/reports/generate_styled_report_pdf.py`
  Export script that should stop leaving unnecessary HTML preview files and repository-local Chrome profile residue.
- `requirements.txt`
  Already tracks `pymupdf`, but the validator import path should align with the tracked package name.
- `doc/guide/project_usage_guide.md`
  Must reflect the corrected export and validation workflow before the final commit.
- `README.md`
  Main project index that must reference this technical note.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. After user approval, refactor `scripts/reports/validate_report_pdf.py` to follow the local programming style and import `pymupdf` directly.
3. Update `scripts/reports/generate_styled_report_pdf.py` so temporary HTML export is the default path unless a persistent preview is explicitly requested.
4. Move Chrome temporary-profile creation to the OS temporary directory instead of `doc/reports/.../.tmp_chrome_profiles/`.
5. Add a robust cleanup helper for temporary browser-profile directories and keep any residual cleanup failure non-fatal.
6. Update `doc/guide/project_usage_guide.md` so the preferred commands no longer imply permanent preview-HTML leftovers.
7. Re-run the PDF export and PDF validation workflow on the current campaign results report to confirm:
   - no `Pylance` import issue in the validator path;
   - no unnecessary HTML artifact remains by default;
   - no repository-local `.tmp_chrome_profiles/` residue is produced.
