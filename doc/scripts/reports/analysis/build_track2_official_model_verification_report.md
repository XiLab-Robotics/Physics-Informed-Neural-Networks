# Track 2 Official Model Verification Report Builder

## Overview

`scripts/reports/analysis/build_track2_official_model_verification_report.py`
builds the dated official `Track 2` model-verification Markdown report from
the same artifacts produced by an operator-launched `Track 2` refresh.

It is used by the `Track 2H` verification-refresh launchers so the normal
launcher path produces a self-contained package: matrix report, collage report,
overlay report, official decision report, and PDF exports.

## Inputs

Required inputs:

- `--matrix-summary-path`: `validation_summary.yaml` from the matrix refresh;
- `--collage-summary-path`: `track2_best_model_collage_summary.yaml`;
- `--overlay-summary-path`: `track2_multi_model_curve_comparison_summary.yaml`;
- `--report-date`: dated report bundle label;
- `--refresh-label`: human-readable refresh name;
- `--candidate-source-label`: registry source label that must be visible in
  the matrix and visual summaries.

Optional inputs:

- `--decision`: official decision text;
- `--next-step`: closeout next-step text;
- `--output-report-path`: explicit Markdown output path;
- `--operator-log-root`: launcher log directory recorded in the source package.

## Output

The default output is:

```text
doc/reports/analysis/track2/official_model_verification_report/[YYYY-MM-DD]/track2_official_model_verification_report.md
```

The builder fails if the requested candidate source is missing from the matrix
summary, missing from the collage summary, or missing from the overlay summary.
This prevents a launcher from completing with a stale official report that does
not contain the newly verified candidates.
