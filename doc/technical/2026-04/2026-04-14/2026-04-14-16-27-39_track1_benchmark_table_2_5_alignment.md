# Track 1 Benchmark Table 2-5 Alignment

## Overview

The canonical `Track 1` benchmark in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md` currently mixes two
different numbering schemes:

- the true paper tables for amplitude/phase error matrices;
- a repository-owned derived table named `Table 2 - Harmonic Selection And
  Deployed Family Direction`, which does not correspond to paper Table 2.

This creates a consistency problem for `Track 1`, because the intended
objective is faithful paper-table replication. The benchmark must therefore be
realigned so that repository sections labeled `Table 2`, `Table 3`, `Table 4`,
and `Table 5` match the actual paper tables:

- `Table 2` -> amplitude `A_k` MAE;
- `Table 3` -> amplitude `A_k` RMSE;
- `Table 4` -> phase `phi_k` MAE;
- `Table 5` -> phase `phi_k` RMSE.

The current repository-owned harmonic/family direction summary should no longer
claim to be paper `Table 2`.

## Technical Approach

The benchmark alignment will be implemented in three coordinated steps.

First, recover or reconstruct the true paper `Table 2` values from the
repository reference surface, using `reference/RCIM_ML-compensation.pdf` as the
canonical source and any existing repository-owned exact-paper artifacts only as
supporting evidence. The result must be explicitly labeled as a paper-owned
table reconstruction, not as a newly invented repository summary.

Second, rewrite the canonical benchmark structure so that the full-matrix
replication block contains four coherent sections:

- paper `Table 2` and repository-side analogous matrix for amplitude MAE;
- paper `Table 3` and repository-side analogous matrix for amplitude RMSE;
- paper `Table 4` and repository-side analogous matrix for phase MAE;
- paper `Table 5` and repository-side analogous matrix for phase RMSE.

Third, rename or relocate the current harmonic/family direction summary so it
becomes an explicitly repository-derived support section instead of a
misnumbered paper-table claim. The colored-cell maintenance path already added
for the full-matrix tables must remain intact, and it must be extended if
needed so that future `Track 1` updates preserve the correct `Table 2-5`
mapping and keep the `🟢/🟡/🔴` markers synchronized with the numeric values.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `scripts/reports/refresh_track1_benchmark_colored_markers.py`
- repository-owned exact-paper validation reports under
  `doc/reports/analysis/validation_checks/`
- `doc/README.md`

## Implementation Steps

1. Inspect the paper reference and extract the actual `Table 2` amplitude-MAE
   matrix for the target harmonics and model families used by `Track 1`.
2. Rewrite the benchmark so that sections labeled `Table 2-5` map exactly to
   the paper tables and keep the repository-side analogous matrices aligned to
   those same tables.
3. Demote the current harmonic/family direction section into a clearly
   repository-derived support section with non-paper numbering or naming.
4. Update the colored-marker refresh script if required so future campaign
   refreshes preserve the corrected section layout and marker semantics.
5. Run Markdown QA on the touched Markdown files before closing the task.
