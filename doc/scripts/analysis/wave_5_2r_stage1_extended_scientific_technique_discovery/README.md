# Wave 5.2R Stage 1 Technique Register Validation

This non-training workflow validates the source-backed technique register for
the polished-setpoint forward `Wave 5.2R` program.

## Scope

- dataset: `polished_dataset`;
- inputs: setpoint speed, torque, temperature, and angular coordinate;
- surface: `Fw`;
- training: none;
- purpose: reject unobservable or target-leaking mechanisms before Stage 2.

## Validate

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage1_extended_scientific_technique_discovery/validate_stage1_technique_register.py
```

The validator checks:

- every technique has a primary or repository-primary source;
- all thirteen roadmap search families are represented;
- every real-data technique uses only the frozen causal runtime variables or
  training-derived quantities;
- no real-data technique has a missing variable;
- every technique has a local formulation, matched control, falsification
  rule, deployment assessment, priority, and target stage;
- target-derived runtime variables are absent.

## Outputs

Canonical inputs and generated artifacts live under:

`output/analysis/wave_5_2r/stage1_extended_scientific_technique_discovery/`

The source YAML files are the authored registers. The validator generates a
flat candidate CSV and a JSON exit-gate summary with content hashes.
