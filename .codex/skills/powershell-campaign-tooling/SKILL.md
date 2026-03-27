---
name: powershell-campaign-tooling
description: Use when creating, refactoring, or reviewing PowerShell launcher scripts and related campaign tooling notes in StandardML - Codex. This skill is for repository campaign automation, not general PowerShell administration.
---

# PowerShell Campaign Tooling

Standardize PowerShell campaign launchers and their repository documentation.

## Use This Skill For

- campaign launcher script creation or review;
- PowerShell wrapper hardening for training workflows;
- consistency checks between launcher, campaign YAML, and launcher note;
- small PowerShell tooling refactors around campaign execution.

## Do Not Use This Skill For

- generic Windows administration;
- non-campaign PowerShell modules with no repository workflow impact;
- protected-file edits during an active campaign without explicit approval.

## Required Checks

1. Read `doc/running/active_training_campaign.yaml`.
2. Check whether the target launcher or related docs are protected.
3. Read the matching launcher note under `doc/scripts/campaigns/`.
4. Confirm the PowerShell command still maps to the intended campaign files.

## Script Design Rules

- Keep the launcher simple and explicit.
- Avoid hidden argument rewriting.
- Keep campaign identity visible in variable names and status prints.
- Prefer clear failure surfaces over silent fallback behavior.
- Ensure the documented launch command matches the real script behavior.

## Review Priorities

- wrong config paths;
- stale campaign names;
- mismatch between launcher and planning report;
- broken environment assumptions;
- documentation drift between script and launcher note.

## File Targets To Read First

- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `config/training/`
