# Physics-Guided Optimization Instrumentation

## Overview

The reusable implementation is stored in:

- `scripts/training/physics_guided_optimization_instrumentation.py`

It makes interaction among data, curve, harmonic, derivative, and physics
losses measurable before a Wave 5.2R training campaign is allowed to interpret
an observed gain as physical guidance.

The utility is opt-in. Existing training configurations retain their current
fixed-loss behavior until a future campaign explicitly imports and configures
the instrumentation.

## Main Components

`LossComponentConfiguration` declares:

- a stable component name;
- the raw unit label;
- a positive unit-normalization scale;
- the fixed control weight;
- the protected main-loss or auxiliary role;
- the activation schedule.

`PhysicsGuidedOptimizationInstrumentation` computes:

- raw and normalized loss values;
- exponential moving averages;
- per-loss gradient norms on declared shared parameters;
- every unique pairwise gradient cosine;
- fixed, gradient-statistics, ReLoBRaLo-style, and conflict-aware weights;
- a main-loss-preserving projected gradient when an auxiliary objective
  conflicts with the protected data loss.

Additional helpers provide:

- staged loss activation;
- parameter freeze-unfreeze schedules;
- exact update-to-parameter ratios;
- deterministic seed and dataloader configuration;
- ordered-batch SHA-256 fingerprints.

## Conflict-Aware Boundary

The conflict-aware adapter never projects the protected main data gradient.
Only an auxiliary gradient with a negative dot product against the main
gradient is projected onto the main-gradient normal plane.

The returned flattened gradient is intentionally explicit. A caller must
assign it to parameters and execute the optimizer step. This prevents hidden
gradient surgery inside otherwise unchanged Lightning automatic optimization.

## Determinism Boundary

The deterministic helper freezes Python and PyTorch random state, requests
deterministic algorithms, disables cuDNN benchmarking, and supplies a seeded
dataloader generator.

This guarantees repeatability only inside the same frozen software, hardware,
and device context. PyTorch does not guarantee bitwise identity across
releases, platforms, or CPU/GPU execution.

## Validation

Run the repository-owned Stage 2 harness:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/analysis/wave_5_2r/stage2_evaluation_and_optimization_instrumentation/validate_stage2_instrumentation.py
```

The harness does not train on project data. It uses a deterministic
shared-parameter toy problem to prove the instrumentation contract before
Stage 3 analytical-anchor work begins.
