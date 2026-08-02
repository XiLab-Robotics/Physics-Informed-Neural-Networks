# Live Backlog Priority Alignment

## Overview

This technical document defines a documentation-only alignment of the
canonical TE model live backlog after the completed Wave 5.2R cross-surface
verification and the published reusable TF3820 standalone predictor package.

The current backlog still identifies the operator-run 24-candidate
cross-surface verification as the next branch even though that verification
has already completed. The updated backlog will remove that stale execution
instruction and record the agreed working order:

1. PLC model testing continues manually and in parallel through the standalone
   TF3820 module;
2. the next repository modeling task is an analysis of the H08 `Bw` and
   `global` raw-error, offset, and envelope regressions;
3. the integrated-specialist roadmap follows only after the H08 analysis;
4. the paper-faithful MMT full PINN remains an inactive future option.

This task does not authorize PLC changes, runtime commissioning, H08 analysis
implementation, model training, campaign preparation, or integrated-model
design. No subagent is planned or authorized.

## Technical Approach

The implementation will make a narrow update to
`doc/running/te_model_live_backlog.md`. It will preserve completed Wave 5.2R
evidence and accepted-model decisions while correcting only the current and
next-work statements that have been superseded.

The revised current-focus text will distinguish the following independent
workstreams:

- manual PLC qualification through the already published standalone package,
  which proceeds in parallel and does not block backlog documentation;
- H08 backward/global defect analysis as the next modeling step;
- the integrated-specialist roadmap as a later, separately approval-gated
  task that depends on the H08 analysis;
- MMT as a deferred branch with no current implementation or training
  authorization.

The stale `Current Next Branch` entry will be replaced with an ordered queue.
The queue will not describe the standalone package as runtime-qualified: its
package-integrity and publication work are complete, while interactive XAE,
target-runtime, and TestRig evidence remain part of the parallel manual PLC
workstream.

The current completed campaign has an empty protected-file list, so the live
backlog is not protected by an active or prepared campaign. This documentation
change does not alter campaign state, registries, accepted leaders, model
archives, or deployment claims.

## Involved Components

- `doc/running/te_model_live_backlog.md`
  Canonical operational backlog whose stale next-branch statement will be
  replaced by the agreed ordered queue.
- `doc/running/active_training_campaign.yaml`
  Read-only campaign-state evidence confirming completed closeout and an empty
  protected-file list.
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
  Read-only supporting evidence for the completed Wave 5.2R decision, H08
  specialization boundary, deferred MMT branch, and integrated-specialist
  TODO. It is not modified by this task.
- `doc/technical/2026-08/2026-08-01/2026-08-01-20-54-14_tf3820_reusable_function_block_branch.md`
  Read-only source for the published standalone-package status and the
  boundary between structural validation and runtime commissioning.
- `doc/README.md`
  Canonical registration point for this technical document.

## Implementation Steps

1. Register this technical document in `doc/README.md` and wait for explicit
   user approval.
2. Replace the obsolete 24-candidate execution instruction in the live
   backlog with the agreed ordered queue.
3. Record manual standalone PLC work as an independent parallel workstream,
   without claiming completed runtime qualification.
4. Set H08 `Bw`/`global` defect analysis as the next modeling task and state
   that it requires its own technical document before implementation.
5. Place the integrated-specialist roadmap after the H08 analysis and retain
   its separate approval and campaign gates.
6. Preserve the MMT full PINN as an inactive future option that does not block
   current work.
7. Check the resulting diff for consistency with completed Wave 5.2R evidence
   and verify that no campaign, registry, model, or PLC file changed.
8. Run repository Markdown style and Markdownlint checks on the touched
   Markdown scope, confirm normal single final newlines, and run
   `git diff --check`.
9. Report completion and wait for explicit approval before any Git commit.
