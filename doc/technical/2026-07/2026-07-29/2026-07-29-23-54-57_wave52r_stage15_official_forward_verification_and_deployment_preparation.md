# Wave 5.2R Stage 15 Official Forward Verification And Deployment Preparation

## Overview

Stage 15 moves the tournament-qualified `H04` bounded complex harmonic
coefficient residual model into a separate forward-only
`TE Curve Verification Pipeline` evaluation. The accepted forward harmonic MLP,
the accepted forward GRU, and the frozen Polynomial-Fourier analytical anchor
remain the comparison references.

The stage does not assume that `H04` is accepted. Stage 14 established only that
it is the sole formulation eligible for official comparison: it improved
mean-centered shape error while still trailing the incumbent GRU on raw and
offset error. Official acceptance therefore requires the repository's
multi-index curve-first policy and deployment-parity evidence.

This document is approved under the user's active twenty-four-hour
authorization. No subagent is planned; repository instructions require a
separate explicit approval before any delegation.

## Technical Approach

The implementation will add a dedicated `H04` candidate adapter to the existing
comparison infrastructure. The adapter will load the immutable Stage 5
checkpoint and its training contract, reproduce the frozen causal input
normalization and PF-A coefficient anchor, apply the learned bounded
coefficient corrections, and reconstruct the full periodic curve on the same
official held-out records used for every forward candidate.

The official candidate set is:

| Candidate | Role |
| --- | --- |
| `H04` | Stage 15 challenger |
| Polynomial-Fourier `PF-A` | analytical anchor |
| periodic harmonic MLP `Fw` | accepted non-temporal reference |
| periodic GRU `Fw` | accepted incumbent |

The dedicated matrix must remain forward-only and preserve the common test
surface. It will report raw error, mean-centered shape fidelity, offset and
continuity behavior, harmonic and phase fidelity, robustness, visual evidence,
and deployment readiness. No registry is updated before the resulting official
decision is inspected and accepted.

The deployment preparation will define an explicit TwinCAT-facing graph:

```text
causal setpoints
  -> frozen normalization
  -> PF-A analytical coefficients
  -> bounded learned coefficient corrections
  -> corrected coefficients
  -> harmonic reconstruction
  -> output saturation and diagnostics
```

The first parity target is Python versus ONNX on the frozen Stage 15 payload.
PLC parity will be specified against the same exported inputs, intermediate
coefficients, and reconstructed output. Passing static export checks alone is
not equivalent to PLC runtime acceptance.

The heavy official matrix will not be executed by the implementation agent.
The repository-owned launcher will support local and `-Remote` modes, but the
operator must run it and report completion before generated evidence can be
accepted or the stage can be closed.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  candidate loading, inference, and official comparison pipeline.
- `scripts/models/complex_harmonic_coefficient_residual_network.py`
  inspectable `H04` inference graph.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  dedicated forward-only Stage 15 matrix configuration.
- `scripts/campaigns/track_2/`
  local and remote verification launcher.
- `doc/scripts/campaigns/track_2/`
  operator contract and exact commands.
- `output/training_runs/complex_harmonic_coefficient_residuals/`
  immutable selected Stage 5 checkpoint and supporting contract.
- `models/polished_dataset/setpoints/`
  accepted forward reference inventories.
- `doc/reports/analysis/te_curve_verification_pipeline/`
  official overlays, collages, multi-index decision report, and PDF.
- family and program registries, updated only if the official evidence supports
  acceptance.
- project master summary and closeout ledger, updated after the final decision.

## Implementation Steps

1. Validate the selected `H04` checkpoint, configuration, split identity,
   harmonic orders, and causal input contract without regenerating training
   artifacts.
2. Add an explicit Stage 5 coefficient-residual candidate kind to the
   `TE Curve Verification Pipeline`, with strict dataset, surface, split, and
   checkpoint checks.
3. Create a dedicated forward-only matrix containing `H04`, `PF-A`, the
   accepted harmonic MLP, and the incumbent GRU.
4. Create a repository-owned PowerShell launcher supporting local execution,
   `-Remote`, and bounded preflight validation.
5. Document the launcher and provide the exact local and remote commands.
6. Define the TwinCAT inference graph, intermediate diagnostics, numerical
   tolerances, saturation policy, and Python/ONNX/PLC parity contract.
7. Run only static and preflight checks during preparation.
8. Stop and wait for the operator to run the official launcher and confirm
   successful completion.
9. Inspect the returned matrix, overlays, collages, and per-surface
   multi-index evidence.
10. Export and validate the final Markdown and PDF report.
11. Update registries and program status only if the acceptance gates pass;
    otherwise retain `H04` as exploratory.
12. Perform Markdown, Sphinx, workflow, artifact-size, and commit preflight
    checks before the Stage 15 commit.
