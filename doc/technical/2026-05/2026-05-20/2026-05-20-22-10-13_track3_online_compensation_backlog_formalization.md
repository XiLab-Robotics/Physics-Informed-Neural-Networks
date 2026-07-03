# Track 3 Online Compensation Backlog Formalization

## Overview

This technical document plans the documentation-only formalization of the
future `Track 3` branch.

The repository has now closed `Target A` as an offline
direction-qualified paper-comparable benchmark. The remaining paper-equivalent
gap is the online compensation branch previously described as the future online
track, the old Pipelines `8-10`, and the `Target B` / `Table 9` benchmark.

The planned canonical name is:

`Track 3. Online Compensation And Deployment Evaluation`

## Technical Approach

The implementation will update canonical documentation and backlog wording so
`Target B` is no longer described as a floating standalone target. Instead,
`Target B` becomes the explicit closeout objective for future `Track 3`.

The formalized scope will be:

- online compensation loop in the TestRig / TwinCAT execution path;
- repository-owned uncompensated versus compensated evaluation;
- `Robot` and `Cycloidal` style motion-profile validation;
- TE RMS and TE max reporting before and after compensation;
- final paper-style `Table 9` comparison;
- deployment-readiness interpretation for the selected repository model path.

The formalized status will be:

- not implemented;
- deferred until after the offline baseline is accepted as closed;
- not part of `Wave 5.1` hybrid/offline model exploration;
- tracked as a future vertical validation and deployment branch.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/README.md`
- possibly `doc/guide/project_usage_guide.md` if the user-facing roadmap text
  needs the same Track 3 label after backlog formalization

No subagent is planned. If subagent use becomes useful later, it must be
declared and approved before launch.

## Implementation Steps

1. Rename or cross-label the deferred `TwinCAT Deployment Evaluation` branch as
   `Track 3. Online Compensation And Deployment Evaluation`.
2. Move the `Target B` wording under the `Track 3` future branch and state that
   `Target B` is the Track 3 closeout objective.
3. Preserve `Wave 5.1` as an offline hybrid structured-model branch, separate
   from Track 3.
4. Update the master summary roadmap so future readers see Track 3 as the
   planned online compensation / deployment branch.
5. Update any user-facing roadmap entry if it currently mentions the old
   Pipelines `8-10` or `Target B` without the Track 3 label.
6. Run Markdown QA on every touched Markdown file.
7. Report completion and wait for explicit commit approval.
