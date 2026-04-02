# Overview

This document evaluates the current Codex-native customization set against the
repository's broader workflow surface and the external reference collections
under `reference/agents/`.

The current project-local set covers:

- campaign planning and campaign-safe tooling;
- Markdown and report-document QA;
- scientific-reference synthesis;
- ML-oriented repository review;
- TwinCAT / PLC-facing deployment analysis.

That first wave is useful, but it does not yet cover several recurrent workflow
needs that are already visible in this repository:

- PyTorch / PyTorch Lightning implementation and refactor support;
- testing and validation strategy for training, smoke-test, and report flows;
- styled PDF layout QA for analytical reports and model reports;
- commit-preflight hygiene and commit-message preparation under the
  repository's approval-gated commit policy.

The goal of this follow-up is to add a second repository-owned Codex
customization wave with narrowly scoped artifacts that are immediately useful
for current work and likely to remain useful as the repository grows.

## Technical Approach

## 1. Re-Scan The External Agent Repositories For High-Signal Patterns

The external repositories under `reference/agents/` contain a large catalog of
generic roles, but only a subset maps well to this repository.

The most relevant inputs for this follow-up are:

- `reference/agents/wshobson-agents/`
  especially its structured skill packaging and the skill areas around Python
  development, testing, code review, changelog/commit hygiene, and
  documentation workflows;
- `reference/agents/awesome-claude-code-subagents/`
  especially its `machine-learning-engineer`, `mlops-engineer`,
  `python-pro`, `code-reviewer`, `test-automator`,
  `git-workflow-manager`, `documentation-engineer`, and PowerShell-oriented
  role ideas;
- `reference/agents/claude-code-agents/`
  especially its concise `code-reviewer`, `test-strategist`,
  `report-generator`, `technical-writer`, and research personas;
- `reference/agents/claude-code-subagents/`
  mainly as a low-priority source for framework-specific expert role wording
  such as Python, NumPy, scikit-learn, and PyTorch experts.

The follow-up should keep adapting these ideas into repository-native Codex
artifacts rather than importing them directly.

## 2. Prioritize Repository-Specific Gaps Instead Of Generic Catalog Expansion

The repository already has strong rules around:

- campaign preparation and artifact bookkeeping;
- training execution approval;
- Markdown quality;
- technical-document creation;
- PDF validation for analytical reports;
- commit approval and GitHub size checks.

Therefore the missing value is not "more generic experts". The missing value is
workflow-specific specialization for the tasks that repeatedly appear in this
codebase.

The highest-value additions are:

### Proposed New Skill: `git-commit-preflight`

This skill should support the repository's approval-gated commit flow without
automating commits prematurely.

It should be used for:

- commit-scope review before asking for commit approval;
- changed-file audit against repository rules;
- staged commit-title and commit-body drafting aligned with repository style;
- GitHub `100 MB` file-size limit checks;
- verification that required documentation, requirements, and usage-guide
  updates have not been missed.

It should not create a commit automatically. It should prepare the commit
cleanly and surface any blockers before the final approval checkpoint.

This directly addresses the user's example request for a commit-related skill
while staying aligned with the repository rule that commits remain explicitly
user-approved.

### Proposed New Skill: `pytorch-training-workflows`

This skill should help with repository-specific Python / PyTorch /
PyTorch-Lightning implementation and refactor tasks.

It should be used for:

- model-family implementation work in `scripts/models/`;
- training and datamodule changes in `scripts/training/`;
- training-loop and metric-flow refactors;
- configuration-aware updates that affect training behavior;
- local reasoning about NumPy, scikit-learn, and adjacent ML tooling where the
  repository already uses those ecosystems.

It should explicitly remind Codex to:

- read relevant references before design changes;
- use Context7 before library-specific implementation choices for PyTorch,
  PyTorch Lightning, NumPy, SciPy, and scikit-learn;
- preserve TE-domain inputs and analytical-vs-ML separation;
- keep artifact, smoke-test, and validation implications visible.

### Proposed New Skill: `styled-report-pdf-qa`

This repository spends significant effort on styled analytical reports,
explanatory model reports, and PDF validation.

The existing `markdown-report-qa` skill is useful, but it does not cover the
full styled-PDF workflow deeply enough.

This new skill should be used for:

- analytical report and model-report final QA;
- styled PDF export preparation;
- post-export validation against the repository's PDF golden standard;
- table-balance review, page-break review, and edge-pressure review;
- local coordination between report Markdown, export scripts, and validation
  scripts under `scripts/reports/`.

### Proposed New Subagent: `repo-test-strategist`

This subagent should cover a gap that is only partially addressed by
`repo-ml-reviewer`.

`repo-ml-reviewer` is strong for bug/risk review, but it is not specialized for
planning the actual verification matrix when a new model, training workflow, or
tooling change is introduced.

A dedicated `repo-test-strategist` should focus on:

- unit, smoke-test, validation-check, and campaign-verification planning;
- identifying the minimum safe test matrix for a proposed change;
- mapping code changes to repository verification commands and evidence;
- spotting where testing obligations are missing from the implementation plan.

This would be useful now and later as the repository adds more model families
and export paths.

## 3. Keep The Second Wave Narrow And High-Value

The second wave should not try to mirror the huge external catalogs.

It should stay focused on a compact set of artifacts with clear repository
ownership:

- one commit-oriented skill;
- one ML implementation skill;
- one report/PDF QA skill;
- one testing-strategy subagent.

This is enough to materially improve current workflows without creating a large
maintenance burden.

## 4. Preserve The Approval Boundary For Subagents

The repository rule added on `2026-03-27` requires that planned subagent use be
declared in the technical document and then approved explicitly by the user
before launch.

For this task, the implementation is expected to create a new subagent
definition file, but no runtime subagent launch is required to complete the
implementation itself.

Planned subagent use during implementation:

- none required.

Planned new subagent artifact to be created if the user approves the feature
scope:

- `repo-test-strategist`.

## 5. Avoid Redundant Or Low-Value Additions

The follow-up should avoid creating:

- a generic `code-reviewer` duplicate of `repo-ml-reviewer`;
- a generic `python-expert` with no repository-specific guidance;
- a generic `documentation-writer` that overlaps heavily with existing rules;
- a skill that auto-commits or bypasses the repository's approval sequence.

If a role cannot add repository-specific decision quality, it should not be
implemented.

## 6. Update Repository Documentation Only Where Necessary

This follow-up should primarily create:

- new `.codex/skills/<skill_name>/SKILL.md` directories;
- new `.codex/agents/<agent_name>.toml` definitions;
- optional skill-local references or helper notes if they improve quality.

No protected campaign file should be touched unless separately authorized.

If the final approved scope changes public-facing repository usage or available
workflow entry points, then `README.md` and `doc/guide/project_usage_guide.md`
should be updated according to repository rules, with campaign protection
checks applied first.

## Involved Components

- `README.md`
- `AGENTS.md`
- `doc/technical/2026-03/2026-03-27/2026-03-27-17-48-41_additional_codex_skills_and_subagents_for_ml_testing_reports_and_commit_workflows.md`
- `.codex/agents/repo-ml-reviewer.toml`
- `.codex/agents/twincat-deployment-analyst.toml`
- future `.codex/agents/repo-test-strategist.toml`
- future `.codex/skills/git-commit-preflight/`
- future `.codex/skills/pytorch-training-workflows/`
- future `.codex/skills/styled-report-pdf-qa/`
- existing `.codex/skills/`
- `reference/agents/wshobson-agents/`
- `reference/agents/awesome-claude-code-subagents/`
- `reference/agents/claude-code-agents/`
- `reference/agents/claude-code-subagents/`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Reconfirm the active campaign protection boundary before touching any
   repository-owned documentation outside the local Codex artifact area.
3. Implement the `git-commit-preflight` skill with repository-specific commit
   gating, changed-file checks, and commit-message drafting rules.
4. Implement the `pytorch-training-workflows` skill with Context7-first ML
   library guidance and repository-specific training constraints.
5. Implement the `styled-report-pdf-qa` skill with explicit PDF validation and
   layout-review guidance.
6. Implement the `repo-test-strategist` subagent definition focused on
   repository verification planning.
7. Verify the new artifacts for naming clarity, activation scope, and alignment
   with repository rules.
8. If required by the approved scope and safe with respect to campaign
   protection, update user-facing documentation references for the new Codex
   artifacts.
