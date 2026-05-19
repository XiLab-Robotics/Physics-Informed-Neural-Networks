# RCIM Paper Original Table Audit

## Overview

This document plans the correction of `Track 1` status markers in
`doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md` after commit
`ce0237d27cd7466bd14e16d767fccf125e3ee2eb` corrected several Table 2 paper
original values.

The work also checks the other paper-original forward tables against the local
RCIM paper source before changing the benchmark report.

## Technical Approach

- Use `reference/RCIM_ML-compensation.pdf` as the paper-side source for
  original forward Tables `2`-`5`.
- Compare the current benchmark report's `Paper Original` sections with the
  paper table values.
- Recompute the forward Table 2 `Track 1` marker colors using the existing
  report rule: compare Track 1 forward values against the better value between
  `paper original` and `paper retuned`.
- Keep the edit limited to benchmark report marker corrections unless the
  paper audit finds additional original-value transcription errors.
- No subagent is planned for this work.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/README.md`
- Markdown QA tooling under `scripts/tooling/markdown/`

## Implementation Steps

1. Extract or inspect the original paper values for forward Tables `2`-`5`.
2. Compare those values against the current benchmark report.
3. Update Table 2 `Track 1` marker colors affected by the corrected Table 2
   paper-original baseline.
4. Apply any additional paper-original value corrections found during the
   audit.
5. Run scoped Markdown QA on the touched authored Markdown files.
6. Check Git size risk before the requested commit.
7. Commit the approved, narrow documentation update.
