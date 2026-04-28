# Reference Family Vs Feedforward Comparison Script

## Overview

This script runs the first `Track 2` repository-owned comparison between one
paper-faithful exact-paper family archive and one repository direct-TE
baseline.

The script is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`

## Main Role

This workflow exists to compare:

- the curated `LGBM-19` exact-paper reference archive;
- the canonical best `feedforward` TE baseline;

on one shared held-out TE-curve evaluator built from the repository test
manifest.

It performs these stages:

1. load the curated `LGBM` reference inventory and Python estimators;
2. resolve the current best `feedforward` run from the family registry;
3. rebuild the repository held-out TE-curve test split;
4. decompose those held-out curves into the selected paper harmonic set;
5. predict harmonic amplitudes and phases with the archived `LGBM-19` bank;
6. reconstruct TE curves from those harmonic predictions;
7. predict the same TE curves directly with the best `feedforward` checkpoint;
8. compare `LGBM-19`, `feedforward`, and oracle harmonic truncation with one
   shared curve-space metric bundle;
9. save a machine-readable summary, per-condition CSV table, preview plots when
   available, and a Markdown report.

## Main Components Used

### `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward_support.py`

Provides:

- reference-inventory loading and archived-estimator loading;
- canonical best-feedforward checkpoint loading;
- shared held-out curve-manifest construction;
- `LGBM-19` harmonic reconstruction;
- direct-TE `feedforward` inference;
- metric aggregation, per-condition export, preview plotting, and report
  generation.

### `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/baseline.yaml`

Provides:

- the repository dataset config path;
- the curated `LGBM` reference inventory path;
- the canonical `feedforward` leaderboard path;
- the percentage-error denominator policy;
- the preview-curve count.

## Outputs

The script writes its immutable validation artifact under:

- `output/validation_checks/track2_reference_comparison/`

Typical artifacts include:

- `training_config.yaml`
- `run_metadata.yaml`
- `validation_summary.yaml`
- `per_condition_metrics.csv`
- `preview_curves/`

It also writes a repository-owned Markdown report under:

- `doc/reports/analysis/validation_checks/track2/`

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/baseline.yaml `
  --output-suffix baseline_validation
```

Use this script when:

- the project needs the first `Track 2` `paper-faithful bank vs direct-TE`
  comparison;
- the team wants one shared TE-curve metric surface before extending the same
  workflow to other `Track 1` families;
- future cherry-picked harmonic banks will reuse the same evaluator contract.

Operational note:

- this script is a result-level comparison on held-out TE curves;
- it does not claim that the direct-TE `feedforward` path is paper-faithful at
  the internal prediction-task level.
