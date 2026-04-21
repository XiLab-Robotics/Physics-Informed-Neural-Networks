# Track 1 Scope Separation From Harmonic-Wise Branch

## Overview

This technical document formalizes a stricter scope separation between the
canonical `Track 1` objective and the repository-owned harmonic-wise
comparison branch.

The current repository documentation still contains mixed framing in a few
canonical documents. In particular:

- `Track 1` status is sometimes still described through `Table 6` harmonic
  closure language;
- some summaries still present the harmonic-wise branch as the primary active
  `Track 1` branch;
- some wording still implies that harmonic-wise progress is part of the main
  `Track 1` completion gate.

That is no longer the intended interpretation.

The requested repository rule is now:

- `Track 1` is the exact-paper family-bank implementation track;
- its progress must be summarized through the four full-matrix replication
  tables only:
  - `Table 2 - Amplitude MAE Full-Matrix Replication`
  - `Table 3 - Amplitude RMSE Full-Matrix Replication`
  - `Table 4 - Phase MAE Full-Matrix Replication`
  - `Table 5 - Phase RMSE Full-Matrix Replication`
- `Track 1` is considered complete only when the repository has the expected
  `19` accepted models for each of the `10` algorithm families;
- the harmonic-wise branch should be postponed into a separate follow-up track,
  named either `Track 1.5` or `Track 2`, rather than remaining part of
  canonical `Track 1` status.

## Technical Approach

The documentation repair should separate three concepts that are still partly
blended today:

1. exact-paper family-bank replication status;
2. harmonic-wise diagnostic or reconstruction research;
3. broader direct-TE or later-wave repository comparisons.

The intended post-repair interpretation is:

- canonical `Track 1` progress is measured only through the four full-matrix
  replication tables and the family-bank completion count;
- `Table 6` may remain in the benchmark as a historical or secondary support
  surface only if it is no longer treated as a canonical `Track 1` closure
  gate;
- harmonic-wise validation results must no longer be described as the primary
  `Track 1` branch;
- harmonic-wise work should be renamed in canonical summaries as a separate
  follow-up track, with the exact label chosen consistently across the touched
  documents;
- `Training Results Master Summary.md` and
  `RCIM Paper Reference Benchmark.md` must both reflect the same scope
  boundary so future status summaries do not drift back to the older framing.

The preferred naming convention for now is:

- `Track 1`: exact-paper full family-bank replication, with `19` models for
  each of `10` families;
- `Track 1.5`: postponed harmonic-wise branch used for later analysis,
  reconstruction experiments, or TE-level support metrics.

If needed for stronger long-term clarity, the harmonic-wise branch can instead
be labeled `Track 2`, but the touched documents should use one label
consistently in the same pass.

No subagent is planned for this task. The scope is a local documentation and
reporting alignment.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/technical/2026-04/2026-04-20/README.md`
- `doc/README.md`

## Implementation Steps

1. Create and register this technical document for the `Track 1` scope repair.
2. Update `RCIM Paper Reference Benchmark.md` so canonical `Track 1` status is
   defined only through `Table 2-5` and the `10 x 19` family-bank completion
   rule.
3. Remove or downgrade any wording that treats `Table 6` harmonic closure as a
   primary `Track 1` status gate.
4. Update `Training Results Master Summary.md` so the active and planned branch
   wording no longer presents harmonic-wise work as the main `Track 1` branch.
5. Rename the harmonic-wise branch consistently as a postponed follow-up track
   such as `Track 1.5` or `Track 2`.
6. Run repository Markdown warning checks on the touched Markdown scope.
7. Report the changes and stop before any Git action.
