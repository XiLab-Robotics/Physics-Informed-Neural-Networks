# Track 1 Closeout Reference Archive Refresh Enforcement

## Overview

The current Track 1 closeout surface is inconsistent. The completed
bidirectional original-dataset mega closeout rebuilds and refreshes the
canonical archive under `models/paper_reference/rcim_track1/`, but the newer
forward-only open-cell repair closeout updates the benchmark and summaries
without promoting improved target winners into the same archive.

This is a pipeline bug. The repository already formalized that accepted Track 1
closeouts must refresh `models/paper_reference/rcim_track1/` whenever a newly
accepted target winner improves the currently archived canonical entry. The
closeout tooling must therefore enforce this behavior for both:

- the current `forward` repair closeout path;
- any future `backward` closeout path that promotes improved target winners.

## Technical Approach

The fix should move the archive-refresh rule from a closeout-specific special
case into a reusable Track 1 closeout helper path. Instead of letting one
closeout script rebuild archives while another one forgets to do it, the
reference-archive promotion should become an explicit shared closeout stage.

The implementation should:

1. identify the reusable archive-refresh primitives already present in the
   bidirectional mega closeout and in the Track 1 archive refresh tooling;
2. refactor them into a callable helper surface that can operate on directional
   accepted winners;
3. wire the current `forward` open-cell repair closeout to refresh
   `models/paper_reference/rcim_track1/forward/` whenever promoted winners beat
   the stored archive entries;
4. prepare the same shared path so a future `backward` closeout script can
   refresh `models/paper_reference/rcim_track1/backward/` without duplicating
   logic;
5. keep the benchmark, master summary, closeout report, and archive documents
   synchronized after archive promotion.

## Involved Components

- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
- `scripts/reports/closeout/track1/closeout_track1_bidirectional_original_dataset_mega_campaign.py`
- `scripts/reports/track1/refresh_track1_family_reference_archives.py`
- `models/paper_reference/rcim_track1/`
- `models/README.md`
- `models/paper_reference/README.md`
- `models/paper_reference/rcim_track1/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Implementation Steps

1. inspect the existing bidirectional mega closeout archive-refresh logic and
   isolate the reusable directional archive-promotion steps;
2. extend the shared helper surface so a directional closeout can refresh only
   the affected branch of `models/paper_reference/rcim_track1/`;
3. update the forward open-cell repair closeout to call the shared archive
   refresh stage after winner promotion and before final report materialization;
4. verify the resulting forward archive against the accepted winners from the
   completed forward repair campaign;
5. update the repository archive documentation if the shared closeout contract
   wording needs strengthening for future `backward` closeouts;
6. run Markdown QA, PDF validation on the affected closeout report if it is
   regenerated, and a warning-free Sphinx build.
