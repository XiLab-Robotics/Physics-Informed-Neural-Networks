# Project Usage Guide Update Rule

## Overview

This document defines a new repository workflow rule to be applied before creating the final Git commit for a user-requested change.

The requested rule is:

- if the approved work creates or changes functions, scripts, modules, models, or files that introduce new user-facing functionality, `doc/guide/project_usage_guide.md` must be updated in detail before the final commit is created.

The goal is to keep the project usage guide aligned with the actual runnable functionality of the repository, especially as new training, inference, export, and model components are added.

## Technical Approach

The rule should be added to the repository workflow documentation so it becomes part of the standard modification sequence.

The rule should make the following distinction explicit:

1. if a change is purely internal and does not alter the available repository functionality, `project_usage_guide.md` does not need a feature-level update;
2. if a change adds or modifies functionality that a user can run, configure, or integrate, `project_usage_guide.md` must be updated before the final commit.

Typical examples that should trigger the guide update are:

- new training scripts;
- new neural-network architectures;
- new model configuration files;
- new inference or export scripts;
- new dataset-processing capabilities;
- new runtime commands or changed usage flows.

The update should be detailed enough to explain:

- what the new functionality does;
- which files and configs are involved;
- how to run it;
- what inputs and outputs are expected;
- any important prerequisites or constraints.

This rule is procedural and documentation-focused. It does not directly change runtime logic, but it affects the required completion criteria for future implementation tasks.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-03-10-16-41-20_project_usage_guide_update_rule.md`

## Implementation Steps

1. Add this technical document to `doc/technical/`.
2. After user approval, update `AGENTS.md` so the workflow explicitly requires a detailed `project_usage_guide.md` update before the final commit whenever new functionality is added or existing functionality changes.
3. After user approval, update `README.md` so the critical project rules reflect the same documentation requirement.
4. After user approval, update `doc/README.md` to reference this technical document.
5. Verify that the new workflow wording is consistent with the existing technical-document approval and mandatory-commit rules.
6. Create a Git commit summarizing the approved rule change.
