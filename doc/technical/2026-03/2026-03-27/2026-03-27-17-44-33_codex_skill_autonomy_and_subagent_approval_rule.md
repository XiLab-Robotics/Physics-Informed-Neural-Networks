# Overview

This document defines a repository-level clarification for how Codex-native
skills and custom subagents should be used during future repository work.

The user approved automatic use of repository-relevant skills whenever the
request clearly matches their intended scope.

The user also approved a stricter policy for subagents: subagents may be
proposed proactively when useful, but they must not be launched silently. Their
planned use must be declared explicitly before execution and approved by the
user.

This document exists to make that workflow explicit and repeatable across
future technical documents and approval checkpoints.

## Technical Approach

## 1. Treat Repository Skills As Automatic Workflow Tools

Repository-owned skills should be used automatically when the request clearly
matches their documented purpose.

This includes cases such as:

- `campaign-architect` for campaign planning, YAML preparation, launcher
  expectations, and artifact/registry workflow design;
- `powershell-campaign-tooling` for PowerShell campaign launchers and related
  script structure;
- `scientific-reference-synthesizer` for turning `reference/` material and
  repository summaries into implementation-facing notes or reports;
- `markdown-report-qa` for touched-Markdown validation and local warning
  cleanup.

The user should not need to explicitly ask for these skills every time.

## 2. Keep Subagent Use Approval-Gated

Custom subagents should remain approval-gated even when they are clearly useful
for the task.

Codex may identify that a subagent would improve quality, speed, or separation
of concerns, but it should stop before launching the subagent and request user
approval.

The approval request should state:

- which subagent is proposed;
- why the subagent is useful for the current task;
- the concrete subtask or review scope assigned to it.

This creates a clear delegation boundary and avoids silent parallelization.

## 3. Declare Planned Subagent Use In The Technical Document

When a future task is expected to benefit from a subagent, the technical
document for that task should say so explicitly.

The technical document should record:

- whether subagent use is expected;
- which subagent is expected;
- the intended purpose and task boundary for that subagent;
- the fact that execution still requires explicit user approval at runtime.

If no subagent is expected, the technical document should make that clear
instead of leaving the decision implicit.

## 4. Mirror The Same Declaration In The Approval Request

When requesting approval for the technical document, the approval message should
also explicitly mention any planned subagent usage.

The approval request should therefore cover both:

- approval of the technical document itself;
- approval of any proposed subagent launch, if the implementation phase is
  expected to use one.

This keeps the approval checkpoint aligned with the plan recorded in the
technical document.

## 5. Keep Skill And Subagent Roles Distinct

The repository should preserve a sharp distinction between:

- skills as local workflow instructions that Codex may apply automatically;
- subagents as delegated work units that require an explicit approval step
  before launch.

This distinction matters because the operational cost, execution model, and
oversight expectations are different.

## 6. Apply The Rule To Future Repository Instructions

The repository instructions should be updated so that future work follows this
policy consistently.

The rule update should make explicit that:

- repository-relevant skills may be used automatically;
- proposed subagent use must be declared before launch;
- planned subagent use must be documented in the technical document when known
  during planning;
- the approval request should mention both the technical document and the
  proposed subagent usage when applicable.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/technical/2026-03/2026-03-27/2026-03-27-17-44-33_codex_skill_autonomy_and_subagent_approval_rule.md`
- existing Codex subagent definitions under `.codex/agents/`
- existing repository skills under `.codex/skills/`

## Implementation Steps

1. Create this technical document with the repository-approved skill and
   subagent workflow clarification.
2. Register this technical document in `README.md`.
3. Wait for explicit user approval before modifying repository instructions.
4. After approval, update `AGENTS.md` so the repository rules explicitly encode
   automatic skill use and approval-gated subagent use.
5. When future work expects subagent help, record that expectation in the new
   task's technical document and restate it in the user approval request before
   any subagent is launched.
