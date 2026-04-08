# Harmonic-Wise Pipeline Before Wave2 Temporal Models

## Overview

This task changes the immediate roadmap priority between the completed `Wave 1`
stage and the future `Wave 2` temporal-model branch.

The previous backlog wording still treated `Wave 2` temporal models as the next
main implementation branch. The user has now clarified a different priority:
before opening the temporal-model wave, the repository should first implement a
stable paper-aligned harmonic-wise prediction pipeline that creates a stronger
comparison framework against the reference paper.

This intermediate branch should sit logically between `Wave 1` and the later
temporal-model work.

## Technical Approach

The live backlog should be updated so the immediate execution branch is no
longer described as `Wave 2 temporal models`.

Instead, the next main branch should become an explicit intermediate
`harmonic-wise pipeline` stage focused on:

1. harmonic-wise prediction of `A_k` and `phi_k`;
2. TE reconstruction from predicted harmonic terms;
3. offline `Robot` / `Cycloidal` motion-profile playback;
4. paper-comparable offline validation to close `Target A`.

The temporal-model wave should remain planned, but it should be moved behind
this intermediate harmonic-wise branch rather than remaining the immediate next
execution focus.

The paper-reference benchmark report should also be aligned with this roadmap
decision so the repository's narrative remains consistent across backlog and
analysis documents.

No subagent is planned for this implementation. The task is a local
documentation and planning realignment.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-08/2026-04-08-17-51-22_harmonic_wise_pipeline_before_wave2_temporal_models.md`

## Implementation Steps

1. Update the live backlog so the immediate next execution branch is the
   harmonic-wise paper-aligned pipeline rather than `Wave 2` temporal models.
2. Reposition the temporal-model wave behind that intermediate branch while
   keeping it planned for later.
3. Align the paper-reference benchmark report with the same priority change.
4. Register this technical document in `doc/README.md`.
5. Run the required Markdown checks on the touched Markdown scope.
6. Report completion and wait for explicit approval before creating any Git
   commit.
