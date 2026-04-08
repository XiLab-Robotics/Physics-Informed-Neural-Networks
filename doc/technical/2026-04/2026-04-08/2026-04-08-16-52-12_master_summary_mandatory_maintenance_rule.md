# Master Summary Mandatory Maintenance Rule

## Overview

This task formalizes the repository rule that the canonical training-results
master summary must remain continuously aligned with the current TE-model
program state. The report already exists and is now generated automatically,
but the repository instructions do not yet state explicitly that it is a
mandatory maintained surface rather than an optional convenience document.

The change should promote the master summary into an explicit project-control
artifact that stays current after each new training campaign and after
meaningful result-registry updates.

## Technical Approach

The implementation should update the repository governance instructions so the
canonical report at `doc/reports/analysis/Training Results Master Summary.md`
is named explicitly as a required maintained document.

The new rule should make these expectations unambiguous:

1. the master summary is the canonical colleague-facing status surface for the
   training program;
2. new completed training campaigns must refresh it automatically as part of
   the normal workflow;
3. any task that materially changes family-best registries, program-best
   registries, active family status, or roadmap status must leave the master
   summary aligned before task closure;
4. documentation and usage references should continue pointing readers toward
   this report as the main current-state entry point.

This is a narrow policy-alignment task. No subagent is planned or needed.

## Involved Components

- `AGENTS.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-08/2026-04-08-16-52-12_master_summary_mandatory_maintenance_rule.md`

## Implementation Steps

1. Add a repository rule in `AGENTS.md` that names the master summary as a
   mandatory maintained canonical report.
2. Clarify in that rule that campaign completion and result-registry updates
   must keep the report synchronized before task closure.
3. Register this technical document in `doc/README.md`.
4. Run the required Markdown warning checks on the touched Markdown scope.
5. Report completion and wait for explicit approval before creating any Git
   commit.
