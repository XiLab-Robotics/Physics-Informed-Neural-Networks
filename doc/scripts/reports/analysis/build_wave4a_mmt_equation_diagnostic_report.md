# Build Wave 5.2A MMT Equation Diagnostic Report

## Purpose

`build_wave4a_mmt_equation_diagnostic_report.py` runs the repository-owned
MMT equation-chain demonstration through the `Wave4MMTDiagnosticAdapter` and
generates a diagnostic-only report for `Wave 5.2A`.

## Command

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py
```

## Outputs

- Markdown report under
  `doc/reports/analysis/model_development_waves/wave_4/mmt_equation_diagnostic/[YYYY-MM-DD]/`.
- Curve CSV, harmonic-summary CSV, and summary YAML under
  `output/validation_checks/wave4_mmt_equation_diagnostic/`.

## Boundary

This script does not train a model, calibrate the MMT equations to the dataset,
create PINN losses, or update model registries. It only records whether the
MMT equation chain is useful enough to justify the later `Wave 5.2B` or `Wave
4C` implementation steps.
