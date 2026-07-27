# Wave 5.2R Stage 3 Analytical Anchor Stress Tests

## Overview

Stage 3 independently refits and qualifies `PF_A_LOCAL_QUADRATIC` as a bounded
analytical component for the frozen `polished_dataset`, setpoint-input, `Fw`
contract.

The workflow is non-training. It fits Polynomial-Fourier coefficient surfaces
on the frozen training partition and evaluates them on unchanged validation
and test partitions.

## Run Command

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage3_analytical_anchor_reproduction_and_stress_tests/run_stage3_analytical_anchor_stress_tests.py
```

The successful terminal contract begins with:

```text
WAVE52R_STAGE3_RUN_OK
```

## Validation Command

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage3_analytical_anchor_reproduction_and_stress_tests/validate_stage3_analytical_anchor_stress_tests.py
```

The validator checks:

- the frozen split signature;
- all twelve exit gates;
- exact Phase 1 reproduction;
- six required analytical variants;
- sixty-four deterministic bootstrap refits;
- seventeen train-only operating-condition holdouts;
- thirty-eight anchor-corruption arms;
- finite predictions on all `966` eligible forward curves;
- all three report plots.

The successful terminal contract begins with:

```text
WAVE52R_STAGE3_VALIDATION_OK
```

## Outputs

Machine-readable evidence is written under:

```text
output/analysis/wave_5_2r/stage3_analytical_anchor_reproduction_and_stress_tests/
```

The report assets are written beside the Stage 3 analytical report under:

```text
doc/reports/analysis/model_development_waves/wave_5_2/
physics_guided_pinn_reassessment/[2026-07-27]/
stage3_analytical_anchor_reproduction_and_stress_tests/assets/
```

## Interpretation

The pass qualifies `PF-A` only inside the declared `supported_core` envelope.
It does not promote the reduced, paper-order, recovered ONNX, or PLC-safe
subsets. It also does not claim that numerical finiteness outside the training
envelope implies physical trustworthiness.
