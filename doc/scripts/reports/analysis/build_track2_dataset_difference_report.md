# TE Curve Verification Pipeline Dataset Difference Report Builder

## Overview

`scripts/reports/analysis/build_track2_dataset_difference_report.py` builds a
dataset-difference visual report for the split `TE Curve Verification
Pipeline` workflow.

The builder compares explicit simplified-trained and polished-trained
candidate pairs on the same selected evaluation dataset and surface scope. It
plots the measured curve, the simplified-trained prediction, the
polished-trained prediction, and the direct `polished - simplified` prediction
delta.

## Inputs

Required inputs:

- `--config-path`: TE curve-verification matrix configuration;
- `--dataset`: `polished_dataset` or `simplified_dataset`;
- `--surface-scope`: `forward`, `backward`, or `global`;
- `--candidate-pair`: one or more
  `PAIR_ID:SIMPLIFIED_CANDIDATE_ID:POLISHED_CANDIDATE_ID` values.

Optional inputs:

- `--report-date`: dated report bundle label;
- `--curves-per-pair`: deterministic representative curve count;
- `--output-root`: generated artifact root;
- `--report-topic-root`: Markdown report root.

## Output

The default report output is:

```text
doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/dataset_difference_report/[YYYY-MM-DD]/<dataset>/<surface>/track2_dataset_difference_report.md
```

Generated plots and CSV metrics are stored under:

```text
output/validation_checks/track2_dataset_difference_report/
```

The builder is intended for operator-launched verification runs after the
full-wave polished retraining closure artifacts have been merged locally.
