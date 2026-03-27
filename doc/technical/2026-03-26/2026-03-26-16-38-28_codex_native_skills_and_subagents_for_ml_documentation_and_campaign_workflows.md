# Overview

This document defines a Codex-native customization layer for this repository
using reusable skills and custom subagents derived from the external reference
collections currently stored under `reference/agents/`.

The goal is not to import Claude-oriented agent packs directly. The goal is to
extract the parts that match this repository's actual needs and repackage them
into Codex-compatible artifacts that can improve execution quality for:

- TE-model and campaign-oriented code review;
- training and campaign workflow planning;
- scientific-reference synthesis from `reference/`;
- TwinCAT / PLC-oriented deployment analysis;
- PowerShell campaign tooling standardization;
- Markdown and report quality assurance.

This work is motivated by two observations:

1. Codex already supports native subagents and skills through its own
   configuration model.
2. The four external agent repositories under `reference/agents/` contain
   reusable role descriptions, orchestration patterns, and skill structures,
   but they are primarily designed for Claude Code rather than Codex.

The requested repository feature should therefore adapt, not copy, the external
agent content.

## Technical Approach

## 1. Separate Codex-Native Artifacts From External Reference Repositories

The external repositories under `reference/agents/` should remain reference
material only.

The implementation should create repository-owned Codex-native artifacts in a
local project structure such as:

- `.codex/agents/`
- repository-owned skills folder for Codex skills

Those new files should be authored for Codex's actual conventions rather than
preserving Claude-specific metadata such as:

- `tools: Read, Write, Edit, Bash`
- `/plugin ...`
- `~/.claude/agents/`
- Claude model names and Claude-specific delegation semantics

## 2. Define The Initial High-Value Codex Customization Set

The first implementation wave should stay narrow and focus on the roles that
map well to this repository's active workflows.

### Proposed Custom Subagents

- `repo-ml-reviewer`
  Review training code, model code, campaign YAML, metric handling, and
  experiment regressions with this repository's TE-specific rules in mind.
- `twincat-deployment-analyst`
  Analyze export and deployment implications for TwinCAT / PLC-friendly
  execution, with emphasis on inspectable intermediate quantities.

### Proposed Skills

- `campaign-architect`
  Guide campaign preparation, launcher expectations, artifact layout, and
  registry updates according to repository rules.
- `scientific-reference-synthesizer`
  Read `reference/` material and related summaries, then produce repository
  reports, comparisons, and implementation-facing design notes.
- `powershell-campaign-tooling`
  Standardize and review campaign launchers and related PowerShell helper
  structure.
- `markdown-report-qa`
  Run repository Markdown and documentation QA workflows, including lint and
  report-layout checks where applicable.

This initial scope is intentionally smaller than the full external catalog.

## 3. Use The External Agent Repositories As Design Inputs Only

The external repositories have different practical value levels.

The implementation should mainly mine:

- `reference/agents/wshobson-agents/`
  best source for structured skills, workflow packaging, and orchestration
  concepts;
- `reference/agents/awesome-claude-code-subagents/`
  best source for role ideas such as embedded systems, scientific literature,
  PowerShell architecture, and MCP work;
- `reference/agents/claude-code-agents/`
  useful source for concise review and documentation personas;
- `reference/agents/claude-code-subagents/`
  broad but more generic prompt bank, useful only as a secondary source.

The final Codex-native instructions should be rewritten to reflect:

- this repository's documentation rules;
- campaign-state protection rules;
- TE-domain constraints;
- the current Codex tool model;
- Context7-first requirements for library-specific work;
- the repository's Python and reporting style conventions.

## 4. Respect The Active Campaign Protection Boundary

At the time of this document, `doc/running/active_training_campaign.yaml`
reports an active running campaign and marks several files as protected.

This matters because the requested feature may eventually require updates to:

- `doc/guide/project_usage_guide.md`

That file is currently listed as protected by the active campaign state.

Therefore:

- the technical-document phase can proceed safely now;
- implementation that would modify protected campaign files must not proceed
  without explicit user approval after issuing a critical warning;
- if the user wants to avoid any risk to the running campaign baseline, the
  Codex agent and skill implementation should be deferred until the campaign is
  finished or until protected-file edits are explicitly authorized.

## 5. Keep The First Implementation Self-Contained

The first implementation wave should prefer creating:

- new Codex agent definition files;
- new skill directories with `SKILL.md`;
- optional skill-local `references/`, `assets/`, and helper scripts;
- concise usage documentation that explains invocation patterns and intended
  use.

It should avoid:

- modifying the running campaign configuration;
- changing training code that is on the protected list;
- broad repository restructuring;
- importing large external prompt collections wholesale.

## 6. Document How These Customizations Should Be Used

The implementation should describe both:

- when the custom skill or subagent should trigger;
- when it should not trigger.

This boundary-setting is important because Codex skill activation and subagent
use depend strongly on clear descriptions and narrow role scope.

The resulting documentation should include:

- the intended workflow for each custom artifact;
- a few short example prompts or invocation patterns;
- repository-local ownership and maintenance expectations.

## Involved Components

- `README.md`
- `doc/running/active_training_campaign.yaml`
- new technical document in `doc/technical/2026-03-26/`
- future Codex-native agent definitions in `.codex/agents/`
- future repository-owned skill directories for Codex skills
- `reference/agents/wshobson-agents/`
- `reference/agents/awesome-claude-code-subagents/`
- `reference/agents/claude-code-agents/`
- `reference/agents/claude-code-subagents/`
- `doc/guide/project_usage_guide.md` if later implementation is approved during
  a safe window or with explicit protected-file authorization

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Confirm the active campaign protection boundary and identify which future
   documentation files are currently protected.
3. Select the initial Codex-native customization set:
   `repo-ml-reviewer`, `twincat-deployment-analyst`, `campaign-architect`,
   `scientific-reference-synthesizer`, `powershell-campaign-tooling`, and
   `markdown-report-qa`.
4. Write Codex-native agent definitions and skill directories without copying
   Claude-specific metadata verbatim.
5. Add concise repository-owned usage documentation for the new artifacts.
6. If required by the final approved scope, update
   `doc/guide/project_usage_guide.md` only after explicit approval for touching
   protected campaign files.
7. Verify the new artifacts are internally consistent and aligned with the
   repository instructions before reporting completion.

## Deferred Follow-Up

The user approved the technical document while explicitly deferring edits to
currently protected files. The implementation may therefore create project-local
Codex artifacts now, but the follow-up documentation pass for protected files
such as `doc/guide/project_usage_guide.md` remains open until the active
campaign is finished and those files are no longer locked.
