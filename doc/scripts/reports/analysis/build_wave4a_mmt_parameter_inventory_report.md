# Build Wave 4A MMT Parameter Inventory Report

## Purpose

`build_wave4a_mmt_parameter_inventory_report.py` classifies the inputs required
by the repository-owned `MMT_TEModeling` equation chain before those equations
are promoted to calibrated diagnostics, `Wave 4B` features, or `Wave 4C` weak
PINN losses.

## Command

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py
```

## Outputs

- Markdown report under
  `doc/reports/analysis/wave4/mmt_parameter_inventory/[YYYY-MM-DD]/`.
- Parameter-inventory CSV and summary YAML under
  `output/validation_checks/wave4_mmt_parameter_inventory/`.

## Boundary

This script does not train models, generate campaign YAMLs, calibrate
equivalent-error parameters, or update active campaign state. It records which
MMT inputs are known, dataset-available, train-only calibratable, blocked, or
target-only so that later `Wave 4B` and `Wave 4C` work can remain leakage-safe.
