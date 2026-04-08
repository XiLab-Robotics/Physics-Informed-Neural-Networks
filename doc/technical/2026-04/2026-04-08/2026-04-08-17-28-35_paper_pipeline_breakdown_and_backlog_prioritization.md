# Paper Pipeline Breakdown And Backlog Prioritization

## Overview

This task breaks down the remaining paper-aligned implementation gap into
explicit pipeline components and translates them into an actionable backlog
priority order.

The repository already records the high-level gap between the current offline
training results and the paper's end-to-end `Table 9` benchmark. What is still
missing is a practical decomposition of that gap into concrete implementation
stages, together with a recommendation about what should be implemented
immediately versus what should be deferred until the earlier stages are stable.

## Technical Approach

The implementation should update the live backlog so the remaining paper gap is
tracked in a structured and prioritized way instead of only as a high-level
roadmap statement.

The six pipeline components should be explained and prioritized as follows:

1. harmonic-wise prediction of paper-style amplitude and phase terms;
2. TE reconstruction from the predicted harmonic terms;
3. motion-profile playback for `Robot` and `Cycloidal` style tests;
4. online compensation loop execution during motion rather than offline-only
   evaluation;
5. measurement and reporting of uncompensated versus compensated `TE RMS` and
   `TE max`;
6. final `Table 9` style benchmark report and target-closure decision.

The backlog update should not treat these six items as equal in immediate
priority. The repository should first focus on the pieces that unlock
comparable offline validation and that reduce uncertainty for later online
compensation work.

The practical prioritization should therefore be:

- implement now:
  - harmonic-wise prediction;
  - TE reconstruction;
  - motion-profile playback, at least in an offline replay/analysis form;
  - the paper-comparable offline validation protocol needed to close
    `Target A`;
- implement after that baseline is stable:
  - online compensation loop execution;
  - uncompensated vs compensated online measurement path;
  - final `Table 9` style benchmark report that closes `Target B`.

No subagent is planned for this implementation. The task is local,
documentation-centric, and directly tied to the repository backlog and paper
tracking reports.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-08/2026-04-08-17-28-35_paper_pipeline_breakdown_and_backlog_prioritization.md`

## Implementation Steps

1. Add a practical explanation of the six missing paper-aligned pipeline
   components to the live backlog.
2. Mark which of those components should be implemented immediately and which
   should be deferred until the offline baseline is stable.
3. Align the paper-reference benchmark report with the same prioritization so
   the narrative and the backlog stay consistent.
4. Register this technical document in `doc/README.md`.
5. Run the required Markdown checks on the touched Markdown scope.
6. Report completion and wait for explicit approval before creating any Git
   commit.
