# Python Entrypoint Platform Flag Plan

## Overview

This document plans the next Linux portability tranche for the Unimore Aries
migration. The previous sweep completed Bash equivalents for Windows launcher
scripts, leaving the Python command-line surface as the remaining broad class
that still needs explicit `--linux` / `--windows` handling.

The current portability inventory reports `50` Python CLI-like scripts without
platform flags and `3` scripts marked for platform review. This tranche will
make those entrypoints accept a consistent platform selector, keep `--windows`
as the default behavior, and route path or operating-system assumptions through
repository-relative logic before the scripts are considered Linux-runnable.

No subagent use is planned for this tranche.

## Technical Approach

The implementation will start from the current inventory in
`doc/reports/analysis/utilities/linux_script_portability/[2026-05-16]/` and inspect the
listed scripts before editing them. Scripts will be grouped by behavior instead
of applying a blind textual change:

- campaign preparation scripts that generate YAML, launch commands, or state
  references;
- dataset, report, tooling, and training scripts that expose user-facing CLI
  entrypoints;
- RCIM paper-reimplementation entrypoints that read or write workflow-local
  artifacts;
- review-only scripts that may already be portable but need explicit inventory
  classification.

Where multiple scripts need the same CLI contract, the implementation may add a
small shared helper under the existing Linux portability tooling area. The
helper must preserve the current Windows default, expose mutually exclusive
`--windows` and `--linux` flags, and return an explicit platform mode that
callers can use for path selection or no-op compatibility.

Path handling will remain repository-root-relative. New absolute paths,
hard-coded drive prefixes, or shell-dependent path separators will be avoided
unless they are part of a user-supplied argument. Scripts that do not need
different runtime behavior on Linux will still accept the platform flags so the
repository command surface is uniform.

## Involved Components

The planned scope is the Python portion of the portability inventory:

- `scripts/campaigns/paper_reference/rcim_original/`
- `scripts/campaigns/track_1/exact_paper/`
- `scripts/campaigns/wave_1/`
- `scripts/datasets/`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- `scripts/reports/analysis/`
- `scripts/reports/closeout/`
- `scripts/reports/pdf/`
- `scripts/reports/presentation/`
- `scripts/reports/track1/`
- `scripts/tooling/lan_ai/`
- `scripts/tooling/linux_portability/`
- `scripts/tooling/markdown/`
- `scripts/tooling/session/`
- `scripts/tooling/technical_documents/`
- `scripts/tooling/video_guides/`
- `scripts/training/`
- `doc/reports/analysis/utilities/linux_script_portability/[2026-05-16]/`
- `doc/README.md`

The protected-campaign file rule remains in force. If inspection shows that a
prepared or active campaign file must be modified, the implementation will stop
and request explicit protected-file approval before touching it.

## Implementation Steps

1. Inspect the `50` missing-flag scripts and the `3` review-only scripts from
   the current inventory, then classify each by required platform behavior.
2. Add or reuse a small platform-argument helper if that reduces repeated
   boilerplate without changing each script's existing defaults.
3. Update campaign preparers first, because they are the largest set and are
   most likely to emit platform-sensitive commands or paths.
4. Update RCIM reimplementation, dataset, report, tooling, and training
   entrypoints with the same platform-flag contract.
5. Resolve the `needs_review` entries either by adding platform flags or by
   making the inventory classification explicit.
6. Regenerate the Linux portability inventory and confirm that the Python
   missing-platform-flag count reaches zero or that any remaining item is
   intentionally excluded with a documented reason.
7. Run focused CLI checks on representative scripts, including `--help`,
   default Windows mode, and `--linux` mode where a non-destructive dry run is
   available.
8. Run Markdown QA on touched authored Markdown and rebuild the Sphinx portal
   if the approved implementation changes portal-visible documentation.
9. Stop after the implementation summary and wait for explicit commit approval
   unless the user gives commit approval in the same instruction.
