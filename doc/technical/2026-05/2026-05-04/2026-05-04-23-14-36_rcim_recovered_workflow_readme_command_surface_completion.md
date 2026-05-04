# RCIM Recovered Workflow README Command Surface Completion

## Overview

This document plans the completion pass for the recovered-original RCIM
workflow README so it explicitly lists the full operator command surface that
is now available after the unified paper-reference launcher redesign.

The goal is to make
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
the practical single reference for:

- the direct Python entrypoints;
- the unified PowerShell launcher;
- the compatibility wrapper launchers;
- the main branch and stage options;
- the most relevant operator command examples.

## Technical Approach

The README will be extended without changing the code surface itself. The new
content will consolidate the launcher and workflow commands that are currently
split between the workflow README, the launcher notes under `doc/scripts/`,
and recent operator handoff messages.

The completion pass will add command coverage for:

- the canonical unified launcher:
  - `-Branch Forward|Backward|Both`
  - `-Stage Original|Retune|Eval|Export|LoadBest`
  - `-NoEval`
  - `-NoExport`
  - `-Families`
  - `-BestParameterSummaryPath`
  - `-PrintOnly`
- the direct Python training modes:
  - `export`
  - `retune`
  - `paper_eval`
  - `paper_export`
- the forward and backward compatibility wrappers, including their practical
  mapping to the new canonical launcher.

The README update will stay descriptive and operator-facing. It will not
introduce new behavior, rename files, or change the existing command surface.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/technical/2026-05/2026-05-04/2026-05-04-23-14-36_rcim_recovered_workflow_readme_command_surface_completion.md`
- `doc/technical/2026-05/2026-05-04/README.md`
- `doc/README.md`

## Implementation Steps

1. Expand the recovered-original workflow README with one dedicated command
   section for the unified RCIM original reference launcher.
2. Add representative commands for every relevant branch/stage mode, including
   `Forward`, `Backward`, `Both`, `Original`, `Retune`, `Eval`, `Export`, and
   `LoadBest`.
3. Add the key command options that an operator is expected to use frequently,
   including `-Families`, `-BestParameterSummaryPath`, `-NoEval`, `-NoExport`,
   and `-PrintOnly`.
4. Keep the compatibility-wrapper commands visible in the same README so the
   transition from the old surface to the new canonical launcher is explicit.
5. Run Markdown QA on the touched documentation scope before closing the pass.
