# Track 2 Curve-First Reranking Report Builder

## Overview

`scripts/reports/analysis/build_track2_curve_first_reranking_report.py` builds
the `Track 2B` curve-first reranking report from an existing `Track 2`
validation run.

The script is evaluation-only. It does not launch training, does not modify the
dataset structure, and does not supply future curve samples to the model path.

## Main Role

The report builder converts the existing `Track 2` per-condition metrics into a
promotion-oriented ranking surface for continuous `TE` compensation readiness.

It ranks candidates by:

- mean `Track 2` mean-percentage-error over each candidate's valid direction
  surface;
- P95 mean-percentage-error as the first tie-breaker;
- worst-condition mean-percentage-error as the second tie-breaker;
- mean curve `MAE` as the final numeric tie-breaker.

## Inputs

By default, the script reads the latest complete directory under:

- `output/validation_checks/track2_reference_comparison/`

A complete source directory must contain:

- `per_condition_metrics.csv`
- `validation_summary.yaml`

Use `--track2-run-directory` to rerank a specific `Track 2` run.

## Outputs

The script writes machine-readable artifacts under:

- `output/validation_checks/track2_curve_first_reranking/<run_instance_id>/`

The artifact bundle contains:

- `candidate_curve_first_ranking.csv`
- `direction_curve_first_ranking.csv`
- `track2_curve_first_reranking_summary.yaml`

The dated Markdown report is written under:

- `doc/reports/analysis/track2/curve_first_reranking_report/[YYYY-MM-DD]/`

## Practical Use

Run the latest available `Track 2` matrix reranking from the repository root:

```powershell
python -B scripts/reports/analysis/build_track2_curve_first_reranking_report.py
```

Refresh the canonical dated report bundle:

```powershell
python -B scripts/reports/analysis/build_track2_curve_first_reranking_report.py `
  --report-date 2026-05-28
```

Rerank a specific validation run:

```powershell
python -B scripts/reports/analysis/build_track2_curve_first_reranking_report.py `
  --track2-run-directory "output/validation_checks/track2_reference_comparison/<run_instance_id>"
```

## Notes

- The runtime input contract remains causal: current point, optional short
  causal history, or derived causal features only.
- Full curves are used as the validation and promotion surface because the
  deployment target is continuous `TE` compensation across many consecutive
  motor revolutions.
- Harmonic amplitude, harmonic phase, derivative continuity, and stitched
  revolution residual diagnostics require a future `Track 2` curve-payload
  export and are intentionally marked as deferred by this report.
