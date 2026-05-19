# Report Pipeline Runner

## Overview

This script orchestrates the repository-owned report workflow.

The script is stored in:

- `scripts/reports/pdf/run_report_pipeline.py`

## Main Role

The runner coordinates the existing low-level report utilities:

- diagram regeneration through `generate_model_report_diagrams.py`;
- styled PDF export through `generate_styled_report_pdf.py`;
- real exported PDF validation through `validate_report_pdf.py`.

It is intended to replace repeated manual command chaining when the same report workflow must be rerun.

## Standardized Paths

The runner standardizes the report-pipeline workspace under:

- `.temp/report_pipeline/`

Inside that root, the current workflow uses:

- `.temp/report_pipeline/html_previews/`
- `.temp/report_pipeline/browser_profiles/`
- `.temp/report_pipeline/pdf_validation/<report_name>/`

The preferred repository-local tool environment for PDF validation is:

- `.tools/report_pdf_env/`

## Practical Use

Typical usage for the current explanatory model reports:

```powershell
conda run -n pinns_env python scripts/reports/pdf/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --validation-python-path C:\Users\XiLabTRig\miniconda3\envs\pinns_env\python.exe `
  --windows
```

Linux usage on a host with Chrome or Chromium available:

```bash
conda run -n pinns_env python scripts/reports/pdf/run_report_pipeline.py \
  --use-model-explanatory-reports \
  --regenerate-diagrams \
  --linux
```

If the local report tool environment does not exist yet, bootstrap it once:

```powershell
python scripts/reports/pdf/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --bootstrap-tool-env
```

## Key Options

- `--input-markdown-path`
  Add one Markdown report to the pipeline. Repeatable.
- `--use-model-explanatory-reports`
  Select the four currently tracked structured-model explanatory reports automatically.
- `--regenerate-diagrams`
  Rebuild the repository-owned SVG diagrams before PDF export.
- `--skip-pdf-export`
  Skip the export stage.
- `--skip-pdf-validation`
  Skip the raster-validation stage.
- `--validation-python-path`
  Use an explicit Python interpreter for PDF validation.
- `--prefer-tool-env`
  Prefer `.tools/report_pdf_env/` when it already exists.
- `--bootstrap-tool-env`
  Create the tool environment and install `PyMuPDF`.
- `--clean-temp`
  Remove `.temp/report_pipeline/` before running.
- `--cleanup-validation-images`
  Remove validation PNG pages after successful validation.
- `--windows` or `--linux`
  Select repository-relative path formatting and pass the same platform to the
  PDF exporter and validator.

## Notes

- The runner does not replace the specialized report scripts; it orchestrates them.
- PDF export still depends on a local Chrome, Chromium, or Edge installation.
- PDF validation depends on a Python environment where `PyMuPDF` is available.
- On Windows, `--validation-python-path` can be the simplest option when the main Conda environment already contains `PyMuPDF`.
- On Linux, pass `--chrome-executable-path` to `generate_styled_report_pdf.py`
  directly if the browser is not installed in one of the standard Chrome or
  Chromium locations.
- Validation page images use compact names such as `page_001.png`, which avoids deep-path failures during raster export.
