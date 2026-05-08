# Track1 Exact-Paper Families Alias And Csv Support

## Overview

This task applies a narrow follow-up refinement to the exact-paper
family-stage launcher introduced earlier on `2026-05-08`.

The current launcher exposes `-Family` with one explicit family selector and
`All` as the batch mode. The requested alignment is to keep that surface, but
also accept the recovered-original-style `-Families` parameter so the operator
can pass either:

- one single family name; or
- one comma-separated family list.

The goal is CLI compatibility and usability only. The exact-paper search
protocol, family definitions, and mathematical workflow must remain unchanged.

## Technical Approach

The implementation will extend the current exact-paper launcher to accept both:

- `-Family`
- `-Families`

`-Families` will accept:

- one single family token such as `MLP`;
- one CSV list such as `MLP,RF,GBM`;
- the special batch token `All`.

The launcher will normalize the requested family surface into one internal
family selection list, then filter the prepared paper-faithful queue against
that normalized list before local or remote execution.

The original `-Family` parameter will remain supported so the just-added
single-family surface does not break. The new alias behavior will be
documented in the launcher note, the exact-paper README, and the user guide.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Extend the exact-paper launcher parameter surface with a `-Families`
   argument while keeping `-Family` supported.
2. Add one normalization helper that accepts a single value, CSV list, or
   `All`, and converts that request into the internal family filter list.
3. Update the queue-filter logic so one exact-paper invocation can select
   multiple families from the prepared `20`-run package when requested.
4. Preserve the existing single-family examples and add recovered-original-like
   `-Families "MLP,RF"` examples to the launcher note and README surfaces.
5. Run focused verification plus scoped Markdown QA on the touched
   documentation.
