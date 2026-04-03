# Codex Repo-Local Workflow

## Overview

This guide explains how the repository-local Codex system works inside
StandardML - Codex.

It focuses on the practical workflow used in this repository:

- repository-owned skills;
- repository-owned subagents;
- automatic skill use;
- approval-gated subagent proposals;
- task-oriented examples.

This is not a generic Codex product guide.

It is a repository-local guide for the working rules and artifacts that exist
inside this project.

## What Exists In This Repository

The repository currently exposes two Codex artifact families:

- skills under `.codex/skills/`
- subagents under `.codex/agents/`

The difference is operational:

- a skill changes how Codex conducts the work directly;
- a subagent delegates a bounded part of the work to a specialized reviewer or
  analyst.

## Current Skills

The current repository-owned skills are:

- `campaign-architect`
  for training campaign planning, campaign-safe workflow checks, YAML naming,
  launcher alignment, and registry-aware reasoning;
- `powershell-campaign-tooling`
  for PowerShell campaign launchers and launcher-note consistency;
- `scientific-reference-synthesizer`
  for turning `reference/` material and repository summaries into
  implementation-facing conclusions;
- `pytorch-training-workflows`
  for repository Python, PyTorch, PyTorch Lightning, and adjacent ML workflow
  work;
- `markdown-report-qa`
  for repository Markdown quality, touched-file warning checks, and
  documentation hygiene;
- `styled-report-pdf-qa`
  for styled report export, real PDF validation, and layout-discipline checks;
- `presentation-export-workflows`
  for Markdown-to-PPTX generation, slide PDF export, and presentation
  validation;
- `git-commit-preflight`
  for approval-gated commit preparation, changed-file checks, and commit
  message drafting;
- `twincat-export-preparation`
  for TwinCAT-facing export preparation, PLC-friendly simplification, and
  deployment-readiness discipline.
- `remote-lan-training-campaigns`
  for SSH-backed remote training campaigns, launcher hardening, LAN preflight,
  and remote artifact-sync bookkeeping.

## Current Subagents

The current repository-owned subagents are:

- `repo-ml-reviewer`
  for ML workflow review, campaign/config review, report-generation risk review,
  and artifact-bookkeeping review;
- `repo-test-strategist`
  for defining the minimum safe verification matrix for a repository change;
- `twincat-deployment-analyst`
  for TwinCAT, PLC-friendly, and deployment-facing model analysis;
- `campaign-package-reviewer`
  for campaign-package integrity review:
  planning report, launcher, active state, manifest, winner artifacts,
  registries, and replay-path clarity.

## When Skills Are Used Automatically

Repository-owned skills are used automatically when the task clearly matches
their purpose.

You do not need to explicitly request them every time.

Typical automatic activation patterns are:

- campaign request -> `campaign-architect`
- PowerShell campaign launcher request -> `powershell-campaign-tooling`
- reference or paper synthesis request -> `scientific-reference-synthesizer`
- training/model implementation request -> `pytorch-training-workflows`
- Markdown or report cleanup request -> `markdown-report-qa`
- styled PDF export or repair request -> `styled-report-pdf-qa`
- presentation generation/export request -> `presentation-export-workflows`
- request to prepare a commit -> `git-commit-preflight`
- TwinCAT/export-preparation request -> `twincat-export-preparation`
- remote training-campaign request -> `remote-lan-training-campaigns`

The practical effect is not delegation.

Codex still does the work directly, but with a repository-specific workflow and
checklist applied.

## When A Subagent May Be Proposed

Subagents are not launched silently.

When a subagent seems useful, Codex should first tell you:

- which subagent is proposed;
- why it is useful for the current task;
- which bounded subtask or review scope it would handle.

The launch happens only after your explicit approval.

This means the normal flow is:

1. Codex analyzes the task.
2. If direct work is enough, Codex proceeds alone.
3. If specialization or deeper review would help, Codex proposes a subagent.
4. You approve or reject that launch.
5. If approved, Codex launches the subagent and integrates the result.

## How Skills And Subagents Function In Practice

### Direct Codex Work

Codex reads the local repository, follows the repository rules, and performs
the task directly.

This is the default path.

### Skill-Driven Work

A skill adds a repository-specific workflow discipline.

Examples:

- before campaign changes, Codex checks active campaign state and protected
  files;
- before TwinCAT/export claims, Codex reads the TwinCAT reference notes and
  separates deployed facts from inference;
- before a commit, Codex checks changed files, required documentation updates,
  and GitHub size limits.

### Subagent-Delegated Work

A subagent handles a narrower specialist question in parallel or as a secondary
review.

Examples:

- `repo-ml-reviewer` can review ML workflow risk on a change you already asked
  Codex to implement;
- `repo-test-strategist` can decide which checks are truly required;
- `campaign-package-reviewer` can inspect replay-path and bookkeeping issues in
  a completed campaign package.

The main Codex agent stays responsible for the final integration and final
answer.

## Typical Task Mapping

### Campaign Preparation

Likely skill:

- `campaign-architect`

Possible additional skill:

- `powershell-campaign-tooling`

Possible proposed subagent:

- `campaign-package-reviewer`
  if the task includes reviewing or auditing a prepared or completed campaign
  package.

### Training Or Model Workflow Change

Likely skill:

- `pytorch-training-workflows`

Possible proposed subagents:

- `repo-ml-reviewer`
- `repo-test-strategist`

### Remote LAN Training Campaign Execution

Likely skills:

- `remote-lan-training-campaigns`
- `campaign-architect`

Possible additional skill:

- `powershell-campaign-tooling`

### Report Or PDF Work

Likely skills:

- `markdown-report-qa`
- `styled-report-pdf-qa`

Possible proposed subagent:

- `repo-test-strategist`
  if the change needs a more explicit validation strategy.

### Presentation Work

Likely skill:

- `presentation-export-workflows`

Possible additional skill:

- `markdown-report-qa`
  if the source deck or surrounding Markdown documentation also needs cleanup.

### TwinCAT Or Export Preparation

Likely skill:

- `twincat-export-preparation`

Possible proposed subagents:

- `twincat-deployment-analyst`
- `repo-ml-reviewer`
  if the task also touches model or artifact claims.

### Commit Preparation

Likely skill:

- `git-commit-preflight`

No commit is created automatically.

Codex prepares the commit flow and waits for explicit user approval before the
commit is made.

## Approval Rules That Matter Most

The most important repository-local rules are:

- a technical document is created before implementation work;
- repository-relevant skills may be used automatically;
- subagent use must be declared before launch and approved explicitly;
- touched Markdown files should be checked before closure;
- user approval is required before creating a Git commit;
- guide Markdown and guide PDF companions should both exist for new guides.

## How To Read Codex Behavior During A Task

If Codex says it is using a skill, that means:

- it is applying a repository-specific workflow directly.

If Codex proposes a subagent, that means:

- it wants to delegate one bounded specialist task;
- it is still waiting for your approval;
- the work has not yet been delegated until you approve it.

## Practical Takeaway

Use this mental model:

- skills are automatic workflow tools;
- subagents are approval-gated specialists;
- Codex remains the main operator either way.

When the repository grows, this system should reduce process drift, make review
more consistent, and keep campaign, report, training, and deployment work more
inspectable.
