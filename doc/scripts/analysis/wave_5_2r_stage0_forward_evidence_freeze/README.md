# Wave 5.2R Stage 0 Forward Evidence Freeze

This workflow builds and validates the non-training baseline contract used by
the polished-setpoint forward `Wave 5.2R` program.

## Scope

- dataset: `polished_dataset`;
- inputs: `setpoints`;
- surface: `Fw`;
- held-out conditions: `97`;
- candidates: `PF_A_LOCAL_QUADRATIC`, accepted harmonic MLP, and accepted
  sequence GRU.

## Build

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage0_forward_evidence_freeze/build_stage0_forward_evidence_freeze.py
```

## Validate

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage0_forward_evidence_freeze/validate_stage0_forward_evidence_freeze.py
```

The builder checks the split signature, materializes the eligible forward
condition manifest, normalizes the three baseline metric surfaces, aggregates
selected harmonic bands, hashes all source evidence, and compares the fresh
replays against canonical tolerances.

The validator fails if the split, roster, row counts, surface, provenance
hashes, or reproduction comparisons drift.

## Outputs

Canonical artifacts are written under:

`output/analysis/wave_5_2r/stage0_forward_evidence_freeze/frozen_contract/`

The workflow never launches training.
