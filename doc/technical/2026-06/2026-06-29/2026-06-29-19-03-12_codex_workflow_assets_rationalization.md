# Codex Workflow Assets Rationalization

## Overview

This document plans the approved rationalization of repository-local Codex
workflow assets after the updated subagent reference submodules were reviewed
together with repository rules, skills, active subagents, GitHub automation, and
Codex documentation.

The work keeps the existing active repository subagents, improves their
discoverability and intended-use boundaries, keeps
`reference/agents/wshobson-agents` as the primary external agent/skill
reference, removes obsolete external agent-reference submodules after a final
reference check, and adds a small set of repository-specific workflow assets for
repeatable governance.

No training campaign or training experiment is part of this work.

## Technical Approach

The implementation will keep repository-owned workflow behavior narrow and
evidence-driven:

1. Preserve the four active repository subagents:
   `campaign-package-reviewer`, `repo-ml-reviewer`, `repo-test-strategist`, and
   `twincat-deployment-analyst`.
2. Improve the active subagents by clarifying trigger boundaries, expected
   evidence, and handoff outputs instead of replacing them with generic external
   agents.
3. Keep `reference/agents/wshobson-agents` as the primary external reference
   because it includes Codex-facing plugin manifests and portable skill/agent
   organization.
4. Remove obsolete external reference submodules only after confirming that
   their useful patterns are either already captured by repository-local assets
   or superseded by `wshobson-agents`.
5. Add repository-specific workflow assets rather than importing broad external
   catalogs:
   - a `standardml-workflow-gate` skill for deciding which repository gates
     apply to a task;
   - a deterministic preflight hook or script proposal for mechanical checks;
   - a `repo-doc-governance-reviewer` subagent for documentation coherence
     review;
   - a `track2-decision-auditor` subagent for independent TE Curve Verification
     Pipeline decision review.

Subagents will not be launched during implementation unless separately proposed
with name, reason, and delegated scope, then explicitly approved by the user.

## Involved Components

- `AGENTS.md`
- `.gitmodules`
- `.codex/agents/`
- `.codex/skills/`
- possible `.codex/config.toml` or `.codex/hooks.json`
- `reference/agents/`
- `doc/guide/Codex Repo-Local Workflow/`
- `doc/reports/analysis/utilities/Skill and Subagent Operational Test.md`
- `doc/README.md`
- `.github/`

## Implementation Steps

1. Re-read the active subagent definitions and the Codex repo-local workflow
   guide before editing agent files.
2. Update the four active subagent definitions only where trigger boundaries,
   expected evidence, or final-output shape are ambiguous.
3. Create the `standardml-workflow-gate` skill with concise trigger metadata and
   a short gate-selection procedure that references existing specialist skills.
4. Design a deterministic preflight hook or script as a proposal-first asset:
   start with a non-blocking report mode unless the user later approves
   enforcement behavior.
5. Add `repo-doc-governance-reviewer` and `track2-decision-auditor` subagent
   definitions with read-first targets and narrow review priorities.
6. Confirm useful external references in the three non-primary submodules are
   redundant or superseded, then remove the obsolete submodule entries and
   working-tree references.
7. Update documentation that explains active repository skills, subagents, and
   external reference sources.
8. Run Markdown QA over touched Markdown files and syntax/format checks over any
   changed scripts or configuration files.
9. Stop after verified implementation and wait for explicit commit approval.
