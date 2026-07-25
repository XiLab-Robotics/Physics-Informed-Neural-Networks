# Phase 0 PINN Program Foundation Audit

## Purpose

This non-training workflow completes the shared dataset, coordinate, unit,
direction, domain, temporal, causal-signal, and harmonic contracts required by
the sixteen-phase Wave 5.2 PINN roadmap.

It scans all 1,938 polished directional curve files referenced by the canonical
paired manifest. Detailed contact, wear, efficiency, inertia, MMT, and
electromechanical variables are classified explicitly instead of being
silently treated as observed inputs.

## Build Command

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/pinn_program_foundations/build_phase0_foundation_audit.py
```

The full scan reads approximately 6.7 GiB of polished curve data and prints
progress after every 100 paired conditions.

## Validation Command

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/pinn_program_foundations/validate_phase0_foundation_audit.py
```

The validator confirms artifact hashes, row counts, and the declared Phase 0
exit-gate status.

## Outputs

- `output/analysis/pinn_program_foundations/phase0_foundation_audit.yaml`
- `output/analysis/pinn_program_foundations/phase0_curve_audit.csv`
- `output/analysis/pinn_program_foundations/phase0_condition_support.csv`
- `output/analysis/pinn_program_foundations/phase0_harmonic_prevalence.csv`
- `output/analysis/pinn_program_foundations/phase0_signal_availability.csv`
- the canonical Phase 0 report under the full-PINN analysis tree
