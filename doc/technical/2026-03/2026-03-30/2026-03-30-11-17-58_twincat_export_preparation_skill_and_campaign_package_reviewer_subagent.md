# Twincat Export Preparation Skill And Campaign Package Reviewer Subagent

## Overview

This document defines a focused extension of the repository-owned Codex
artifact set in two directions identified as still missing after the recent
operational-test waves:

- a new skill for TwinCAT and export-preparation workflows;
- a new subagent specialized in campaign-package review.

The intent is not to add generic artifacts. The goal is to close two concrete
workflow gaps:

1. there is currently deployment analysis for TwinCAT, but no procedural skill
   that drives export-preparation work in a repeatable repository-specific way;
2. there is currently a broad ML reviewer, but no narrower reviewer specialized
   in campaign packages, replay paths, launcher behavior, bookkeeping, and
   campaign artifact integrity.

## Technical Approach

The implementation should add one new skill and one new subagent:

1. `twincat-export-preparation`
   - a repository skill that activates when a task concerns TwinCAT-facing
     model preparation, export planning, PLC-friendly simplification, or
     inspectable inference-path design;
   - it should force the workflow to read the current TwinCAT reference notes,
     keep the real rig variables explicit, distinguish deployment-plausible
     from deployment-ready, and prefer explicit intermediate quantities over
     opaque export stories.

2. `campaign-package-reviewer`
   - a repository subagent dedicated to reviewing prepared or completed
     campaign packages;
   - it should focus on planning-report alignment, launcher behavior,
     launch-command ambiguity, campaign-manifest correctness, winner-artifact
     exposure, registry synchronization, and replay/audit traceability.

The new artifacts should remain complementary to the existing ones rather than
overlapping them blindly:

- `twincat-deployment-analyst` remains the higher-level deployment analyst;
- `twincat-export-preparation` becomes the procedural skill used during actual
  export-facing tasks;
- `repo-ml-reviewer` remains the broad ML workflow reviewer;
- `campaign-package-reviewer` becomes the narrower specialist for campaign
  package integrity.

## Involved Components

- `.codex/skills/`
- `.codex/agents/`
- `doc/reference_codes/testrig_twincat_ml_reference.md`
- `doc/technical/2026-03/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `output/training_campaigns/`
- `output/registries/`

Planned subagent usage for the approved implementation:

- `campaign-package-reviewer`
  - Intended task boundary: none during implementation of this artifact.
  - This document proposes creating the subagent artifact itself, not launching
    it at runtime during the implementation.
  - Runtime launch would still require explicit user approval in a future task.

No other runtime subagent use is planned for this implementation.

## Implementation Steps

1. Create the new skill directory
   `.codex/skills/twincat-export-preparation/` with a repository-specific
   `SKILL.md`.
2. Define the skill workflow around:
   TwinCAT reference reading, export-boundary checks, inspectable intermediate
   quantities, rig-variable preservation, and deployment-readiness discipline.
3. Create the new subagent definition file
   `.codex/agents/campaign-package-reviewer.toml`.
4. Define the subagent scope around:
   campaign plans, launcher scripts, launcher notes, active campaign state,
   campaign manifests, best-run artifacts, registries, and replay/audit
   consistency.
5. Keep the new artifact descriptions concise and complementary to the existing
   `twincat-deployment-analyst` and `repo-ml-reviewer`.
6. Run Markdown QA on any touched repository-owned Markdown files before
   closing the task.
