# Canonical Training Results Master Summary

## Overview

This task introduces a canonical repository-owned master document that keeps
the TE-model training program under continuous control. The document should act
as the main human-facing status surface for the user and for colleagues,
showing the current project state, what has already been implemented, what is
still planned, which model families are complete, which are under active
improvement, and how the best results compare across families.

The same task also needs an update path that keeps this master document aligned
automatically whenever a new training campaign produces tracked results.

## Technical Approach

The implementation should create one canonical summary report under `doc/` that
is intentionally different from campaign-local reports and from the live
backlog. Its role is cross-campaign synthesis plus current-state visibility.

The document should contain at least these sections:

1. current project status and roadmap state;
2. implemented, active-improvement, and future model families;
3. best result per family with a cross-family comparison table;
4. family-local result breakdowns ordered by ranking and interpreted through
   both quality and cost/complexity;
5. explicit notes about current global winner, strongest neural branch, and
   deployment-relevant constraints;
6. source-of-truth references pointing to campaign reports, registries, and
   winner artifacts.

The implementation should also introduce a repository-owned update path so the
document can be regenerated or refreshed automatically from canonical sources
such as:

- `doc/running/te_model_live_backlog.md`;
- `output/registries/program/current_best_solution.yaml`;
- `output/registries/families/*/latest_family_best.yaml`;
- campaign-level winner and leaderboard artifacts under
  `output/training_campaigns/`;
- selected final campaign reports under `doc/reports/campaign_results/`.

Useful additional content for colleague-facing tracking should also be included:

- clear status labels such as `completed`, `active`, `planned`, `deferred`;
- a compact model-family maturity table;
- a small "what changed since the last update" section;
- explicit ranking-policy notes so readers understand why one result is
  considered better than another;
- a deployment-readiness caution section that distinguishes predictive quality
  from practical TwinCAT/PLC suitability.

No subagent is planned for this implementation. The work is local,
documentation-centric, and tightly coupled to repository-owned results and
reporting artifacts.

## Involved Components

- `doc/reports/analysis/`
- `doc/running/te_model_live_backlog.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `scripts/reports/`
- `output/registries/program/current_best_solution.yaml`
- `output/registries/families/*/latest_family_best.yaml`
- `output/training_campaigns/`

## Implementation Steps

1. Define the canonical location, filename, and role of the master summary
   document.
2. Design the document structure so it remains readable for both internal
   decision-making and colleague-facing presentation.
3. Implement a repository-owned update workflow that rebuilds or refreshes the
   document automatically from canonical result artifacts after new campaigns.
4. Update the relevant documentation entry points and usage guidance for this
   new master-summary workflow.
5. Run the required Markdown checks on the touched Markdown scope.
6. Report the completed summary workflow and wait for explicit approval before
   creating any Git commit.
