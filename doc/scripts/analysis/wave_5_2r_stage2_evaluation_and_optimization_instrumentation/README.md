# Wave 5.2R Stage 2 Instrumentation Validation

## Overview

The validation entry point is:

- `scripts/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/validate_stage2_instrumentation.py`

It verifies that loss interaction can be observed and controlled before a
physics-guided training campaign is prepared.

## Scope

The harness covers:

1. named loss components with explicit units and normalization scales;
2. raw values and exponential moving averages;
3. per-component shared-parameter gradient norms;
4. pairwise gradient cosine similarity;
5. update-to-parameter ratio;
6. fixed, gradient-statistics, ReLoBRaLo-style, and conflict-aware adapters;
7. staged loss activation;
8. parameter freeze-unfreeze schedules;
9. deterministic seeds and dataloader fingerprints;
10. functional-gradient isolation from parameter `.grad` buffers;
11. main-loss-preserving projection of conflicting auxiliary gradients;
12. the four matched controls required by the roadmap.

The smoke problem deliberately contains one auxiliary residual whose gradient
opposes the protected data loss. This creates a falsifiable projection test
without using target-derived project variables or running a training campaign.

## Command

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/validate_stage2_instrumentation.py
```

## Outputs

The validator writes:

- `stage2_control_matrix.yaml`;
- `stage2_diagnostic_records.csv`;
- `stage2_gradient_interaction_matrix.csv`;
- `stage2_exit_gate_summary.json`.

All outputs are stored under:

```text
output/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/
```

The successful terminal contract begins with:

```text
WAVE52R_STAGE2_VALIDATION_OK
```
