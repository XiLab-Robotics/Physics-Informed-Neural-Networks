# Harmonic-Wise Comparison Pipeline

## Overview

This task opens the implementation branch for the paper-aligned
harmonic-wise comparison pipeline that now sits between completed `Wave 1` and
the later `Wave 2` temporal-model work.

The purpose of this branch is to create a stable offline comparison framework
against `reference/RCIM_ML-compensation.pdf` before any online compensation or
temporal-model expansion is attempted.

The implementation should therefore focus on the repository-owned offline path
needed to close `Target A`:

1. harmonic-wise prediction of `A_k` and `phi_k`;
2. TE reconstruction from predicted harmonic contributions;
3. offline motion-profile playback for `Robot` and `Cycloidal` style tests;
4. paper-comparable offline validation and reporting.

## Technical Approach

The implementation should build a dedicated repository-owned workflow that is
separate from the current direct TE end-to-end family benchmarks.

The branch should introduce an explicit harmonic-wise path where selected
harmonics are modeled through operating-condition inputs such as speed, torque,
and oil temperature, and then recomposed into reconstructed TE curves.

The implementation is expected to cover at least these work areas:

1. target-definition and artifact structure for harmonic-level prediction;
2. data-preparation support for amplitude/phase-style labels;
3. model-training or evaluation entry points for harmonic-wise prediction;
4. TE reconstruction utilities from predicted harmonic terms;
5. offline `Robot` / `Cycloidal` playback tooling for reconstructed TE
   evaluation;
6. a paper-comparable offline benchmark report path that can state whether
   `Target A` has been met.

This branch should remain explicitly offline. It should not yet attempt the
online compensation loop, uncompensated-vs-compensated runtime measurements, or
the final `Table 9` style benchmark closure.

No subagent is planned for this implementation. The work is tightly coupled to
repository-owned training, reporting, and backlog artifacts.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/campaign_plans/`
- `doc/running/te_model_live_backlog.md`
- `doc/README.md`
- `scripts/training/`
- `scripts/models/`
- `scripts/reports/`
- `output/training_runs/`
- `output/registries/`

## Implementation Steps

1. Define the harmonic-wise target representation, selected harmonics, and the
   offline artifact/reporting path needed for the new branch.
2. Prepare the repository-owned training/evaluation workflow for predicting
   harmonic-wise terms.
3. Implement TE reconstruction from the predicted harmonic contributions.
4. Add offline `Robot` and `Cycloidal` motion-profile playback support for the
   reconstructed TE pipeline.
5. Create the paper-comparable offline validation/reporting path for
   `Target A`.
6. Update the relevant backlog and documentation entry points as needed.
7. Run the required Markdown checks on the touched Markdown scope.
8. Report completion and wait for explicit approval before creating any Git
   commit.
