---
name: campaign-architect
description: Use when preparing, reviewing, or extending repository training campaigns, launcher scripts, campaign plans, and artifact bookkeeping for StandardML - Codex. This skill is for campaign-safe workflow design, not for generic ML experimentation.
---

# Campaign Architect

Create or review campaign-oriented work in this repository with the campaign
rules kept explicit.

## Use This Skill For

- campaign preparation and review;
- campaign YAML set design;
- launcher and launcher-note consistency checks;
- active campaign state checks before editing;
- artifact layout, registry, and winner-selection reasoning.

## Do Not Use This Skill For

- generic single-run model tuning with no campaign implications;
- paper summaries with no workflow change;
- unrelated documentation editing.

## Required Checks

Before changing anything campaign-related:

1. Read `doc/running/active_training_campaign.yaml`.
2. Treat files listed in `protected_file_list` as locked until explicit user
   approval says otherwise.
3. Read the relevant planning report under `doc/reports/campaign_plans/`.
4. Verify the intended artifact locations under `output/`.

## Repository Workflow

When the task is campaign-oriented, keep this sequence explicit:

1. Technical document exists.
2. Campaign planning report exists.
3. User approval exists.
4. Campaign YAML files, launcher, and launcher note stay aligned.
5. Active campaign state remains accurate.
6. Result registries and campaign winner artifacts are considered in the final
   workflow.

## Working Rules

- Keep `run_name` separate from immutable `run_instance_id`.
- Do not introduce new legacy flat output roots.
- Prefer narrow, inspectable campaign batches over loosely defined sweeps.
- Close out completed campaigns before any optional `Track 2` refresh. The
  normal closeout covers campaign-results Markdown/PDF, active-state cleanup,
  registry/status synchronization, and QA; it must not run the heavy `Track 2`
  matrix inside Codex.
- If `Track 2` is requested after closeout, prepare an operator-facing
  PowerShell launcher with local and `-Remote` execution paths, then wait for
  the user to run it and confirm completion.
- When reviewing changes, check naming consistency across:
  `campaign_name`, config filenames, run names, launcher names, and report
  titles.
- If a running campaign would be affected, stop and surface a critical warning.

## File Targets To Read First

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/`
- `doc/scripts/campaigns/`
- `scripts/campaigns/`
- `config/training/`
- `output/training_campaigns/`
- `output/registries/`

## Typical Outputs

- campaign design review;
- campaign preparation checklist;
- YAML/config consistency findings;
- launcher/script alignment findings;
- post-campaign registry update checklist.
