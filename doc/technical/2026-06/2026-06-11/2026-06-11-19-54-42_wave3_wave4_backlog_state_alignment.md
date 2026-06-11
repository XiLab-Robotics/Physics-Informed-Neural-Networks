# Wave 3 And Wave 4 Backlog State Alignment

## Overview

This technical document plans a documentation-only alignment pass after the
committed `Wave 3` and `Wave 4A` pre-implementation work.

The current detailed design reports, script notes, validation artifacts, and
`doc/README.md` entries already record the new scaffold state. However, the
operational backlog and the training master summary still describe `Wave 3`
and `Wave 4` mostly as generic pending future branches. That is not precise
enough for the next implementation pass.

The goal is to make the canonical roadmap documents resume from the actual
current state:

- `Wave 3` has a `wave3_harmonic_prior_residual` skeleton;
- `Wave 3` is `training-smoke-ready`, not campaign-ready;
- `Wave 3` has a one-batch validation artifact and a dry-run launcher;
- `Wave 4A` has an MMT diagnostic adapter and generated diagnostic report;
- `Wave 4A` remains diagnostic-only until the MMT parameter inventory and
  leakage-safe calibration are resolved.

## Technical Approach

This is a documentation-only update. It should not add model code, training
queues, launchers, registries, or output artifacts.

The update should make three kinds of changes:

1. Upgrade `doc/running/te_model_live_backlog.md` from generic `Wave 3` /
   `Wave 4` placeholders to actionable next-step entries.
2. Repair and align the relevant `Wave 3` / `Wave 4` entries in
   `doc/reports/analysis/Training Results Master Summary.md`, which currently
   shows duplicated and malformed roadmap text around those waves.
3. Verify whether `doc/README.md` needs only the already-present links or a
   small cross-reference to the backlog alignment technical note.

The roadmap must preserve these boundaries:

- `Track 2H` closeout remains the next dependency for choosing robust-loss
  defaults;
- no real `Wave 3` campaign is approved by the pre-implementation work;
- `Wave 4A` diagnostic output is not evidence of dataset causality yet;
- integrated multi-task / multi-head modeling remains deferred until `Track
  2H`, `Wave 3`, and `Wave 4A` evidence are available.

## Involved Components

Expected files to inspect:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`;
- `doc/reports/analysis/wave4/Wave 4 PINN Formulation And First PINN.md`;
- `doc/reports/campaign_plans/wave3_wave4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md`;
- `doc/reports/campaign_plans/wave3_wave4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md`;
- `doc/README.md`.

Expected files to modify after approval:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- `doc/README.md` only if the new technical document needs registration or an
  additional roadmap pointer.

No subagent is planned for this work. If a subagent becomes useful later, its
scope and approval requirement must be recorded before launch.

## Implementation Steps

1. Create and approve this technical document.
2. Update `doc/running/te_model_live_backlog.md` with:
   - the concrete `Wave 3` current state;
   - the concrete `Wave 4A` current state;
   - the next-step order from `Track 2H` closeout through `Wave 3` campaign
     packaging and `Wave 4A` parameter inventory.
3. Repair the malformed `Wave 3` / `Wave 4` block in
   `doc/reports/analysis/Training Results Master Summary.md` and align it with
   the real pre-implementation state.
4. Register this technical document from `doc/README.md`.
5. Run scoped Markdown QA on touched Markdown files.
6. Run `git diff --check`.
7. Stop for explicit user approval before any commit.

## Approval Gate

This technical document authorizes only documentation updates after explicit
approval. It does not authorize model implementation, training execution,
campaign queue preparation, active-campaign state mutation, registry updates,
or official `Track 2` verification.
