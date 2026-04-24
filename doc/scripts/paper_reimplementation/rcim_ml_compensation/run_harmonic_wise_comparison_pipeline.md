# Harmonic-Wise Comparison Pipeline Script

## Overview

This script runs the repository-owned offline harmonic-wise comparison
pipeline created to align the project with the benchmark paper
`reference/RCIM_ML-compensation.pdf`.

The script is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

## Main Role

The script creates the paper-aligned offline branch that now sits between
completed `Wave 1` and the later `Wave 2` temporal-model work.

It performs these stages:

1. load the harmonic-wise YAML configuration;
2. split the validated TE dataset with the repository-owned file-level split;
3. decompose each curve into the selected harmonic coefficients;
4. fit one tabular regressor per harmonic coefficient target;
5. reconstruct TE curves from the predicted harmonic stack on validation and
   test splits;
6. report paper-comparable offline curve metrics, including mean percentage
   error;
7. run offline `Robot` and `Cycloidal` style playback from the predicted
   harmonic models;
8. save a validation summary plus a Markdown report;
9. refresh `doc/reports/analysis/Training Results Master Summary.md`.

## Main Components Used

### `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`

Provides:

- harmonic decomposition by truncated least-squares fitting;
- coefficient-to-amplitude/phase conversion;
- per-target tree/boosting model fitting;
- TE reconstruction from predicted harmonics;
- offline motion-profile playback helpers;
- validation-summary and Markdown-report generation.

### `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/baseline.yaml`

Provides:

- the selected paper-aligned harmonics;
- decomposition stride;
- estimator hyperparameters;
- offline playback settings for `Robot` and `Cycloidal` style probes.

### `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/`

Provides staged `Track 1` second-iteration presets for:

- reduced harmonic-set debugging runs;
- engineered operating-condition features;
- refined `HistGradientBoosting` configurations;
- a diagnostic `RandomForest` comparison preset;
- promotion back to the full RCIM harmonic set.

## Outputs

The script writes its outputs under:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/`

Typical generated artifacts include:

- `training_config.yaml`
- `run_metadata.yaml`
- `validation_summary.yaml`
- `harmonic_model_bundle.pkl`

It also writes a repository-owned Markdown validation report under:

- `doc/reports/analysis/validation_checks/`

Operational note:

- this is an offline comparison pipeline, not a campaign runner and not a full
  online compensation benchmark;
- it is intended to close `Target A`, not `Target B`;
- the current `Robot` and `Cycloidal` playback blocks are repository-owned
  offline style probes, not the final TwinCAT/TestRig execution path.

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/baseline.yaml `
  --output-suffix baseline_validation
```

Use this script when:

- the project needs a paper-comparable offline harmonic baseline;
- a new harmonic set should be evaluated without opening a full training
  campaign;
- the team wants a colleague-facing offline `paper vs repository` checkpoint
  before any online compensation work.

Current second-iteration preset progression:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage1_h013.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage2_h01340.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage3_h0134078.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage4_full_rcim_engineered.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage1_h013_random_forest_diagnostic.yaml`
