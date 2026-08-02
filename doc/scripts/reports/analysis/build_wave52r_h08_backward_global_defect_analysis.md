# Wave 5.2R H08 Backward And Global Defect Analysis

## Overview

`scripts/reports/analysis/build_wave52r_h08_backward_global_defect_analysis.py`
replays the frozen Wave 5.2R H08 promotion payloads and the matching official
CVP 1.2 per-curve evidence. It produces a non-training diagnostic of the H08
backward and direction-aware global defects.

The companion validator is
`scripts/reports/analysis/validate_wave52r_h08_backward_global_defect_analysis.py`.

## Inputs

The canonical configuration is:

- `config/analysis/wave52r_h08_backward_global_defect_analysis.yaml`

It freezes the nine H08 run directories, the matched periodic harmonic MLP
incumbents, the official metric-reproduction contract, coefficient names, and
the expected surface and seed coverage.

The builder reads existing immutable training and verification artifacts. It
does not train a model, modify a checkpoint, or update a registry.

## Outputs

Machine-readable artifacts are written under:

- `output/analysis/wave_5_2r/h08_backward_global_defect_analysis/<run_id>/`

The canonical report and visual assets are written under:

- `doc/reports/analysis/model_development_waves/wave_5_2/h08_backward_global_defect_analysis/[YYYY-MM-DD]/`

The package contains selected-candidate comparisons, global-versus-specialist
penalties, condition-factor summaries, worst-condition evidence, coefficient
`a0` and harmonic-band attribution, seed stability, source inventory, a YAML
decision summary, and six plots.

## Usage

Build the canonical diagnostic from the repository root:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/reports/analysis/build_wave52r_h08_backward_global_defect_analysis.py `
  --config config/analysis/wave52r_h08_backward_global_defect_analysis.yaml
```

Use an explicit immutable run identifier when reproducing a recorded package:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/reports/analysis/build_wave52r_h08_backward_global_defect_analysis.py `
  --config config/analysis/wave52r_h08_backward_global_defect_analysis.yaml `
  --run-id 2026-08-02-17-12-57
```

Validate the generated package:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/reports/analysis/validate_wave52r_h08_backward_global_defect_analysis.py `
  --config config/analysis/wave52r_h08_backward_global_defect_analysis.yaml `
  --run-directory `
    output/analysis/wave_5_2r/h08_backward_global_defect_analysis/2026-08-02-17-12-57
```

## Interpretation Boundary

The builder can confirm metric decomposition, direction dependence,
global-fit interference, coefficient behavior, operating-condition
concentration, and seed stability. It cannot identify hysteresis, compliance,
lost motion, or another physical mechanism without additional causal evidence.

The diagnostic does not authorize retraining, model promotion, accepted-model
replacement, PLC qualification, or integrated-specialist implementation.
