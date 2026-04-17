# Active Training Campaign Lock And Auto-Generation Workflow

## Overview

The user requested a stricter operational workflow for future training campaigns.

The new requirements are:

1. when a training campaign is prepared, the repository should automatically generate the YAML configuration files required by the approved planning report;
2. the user should also receive the exact terminal command needed to launch the prepared campaign;
3. once the user declares that the campaign has started, the repository should persistently record that campaign as active;
4. while a campaign is active, any later request that would modify files used by that campaign must trigger a `CRITICAL WARNING` before any edit is made;
5. those protected files may be changed only after explicit user approval;
6. when the user declares that the campaign is finished, the active campaign state should be used to collect the generated training artifacts and prepare the final post-training results report workflow;
7. when the user cancels an active campaign, the repository should support a controlled assessment of:
   - completed runs;
   - still-pending queued runs;
   - failed runs;
   - the most sensible handling of partial results.

This request extends the campaign workflow around the already approved queue-based training runner and the existing mandatory planning/results report rules.

## Technical Approach

The requested behavior should become the default campaign workflow for this repository.

### Campaign Preparation Rule

Whenever the user asks to create a new training campaign, the approved preparation stage should include all of the following:

1. create or update the technical document;
2. create or update the planning report in `doc/reports/campaign_plans/`;
3. after approval, generate the campaign YAML files in the appropriate training-preset or queue-preparation location;
4. provide the exact terminal command needed to enqueue or execute that campaign.

This means campaign creation should no longer stop at the planning report alone.

### Active Campaign State

The repository should gain a persistent state file dedicated to the currently active campaign, for example:

```text
doc/running/active_training_campaign.yaml
```

This state file should record at least:

- campaign name;
- planning report path;
- campaign execution root under `output/training_campaigns/` when known;
- queue root in use;
- queue configuration file list;
- run names expected by the campaign;
- protected file list that must not be modified silently during the campaign;
- campaign status such as:
  - `prepared`
  - `running`
  - `completed`
  - `cancelled`

### Protected File Logic

The active campaign state should list the files that materially affect reproducibility of the running campaign.

At minimum, the protected file set should include:

- the queued YAML files for the active campaign;
- reusable preset files if they are used directly by the campaign;
- the campaign runner entry point:
  - `training/run_training_campaign.py`
- the single-run training entry point used by the campaign:
  - `training/train_feedforward_network.py`
- any model or dataset-processing file directly used by the active runs when those files were part of the approved campaign baseline.

When a future request would edit any protected file while the campaign is active, the assistant must stop before editing and issue a clear `CRITICAL WARNING`.

The warning should explain:

- which active campaign is in progress;
- which protected file would be modified;
- why that would change the execution baseline of a running or resumable campaign.

Only explicit user approval should allow those edits to proceed.

### Campaign Completion Flow

When the user later says that the campaign is finished, the assistant should:

1. inspect the active campaign state;
2. collect the campaign execution report and manifest from `output/training_campaigns/...`;
3. gather the per-run metrics and reports referenced there;
4. prepare the mandatory results report in `doc/reports/campaign_results/`;
5. update the active campaign state accordingly.

This final report generation should still respect the repository rule that implementation/report work follows explicit user approval.

### Campaign Cancellation Flow

When the user says that the campaign is cancelled, the assistant should:

1. inspect the active campaign state;
2. summarize completed, failed, running, and pending queue items;
3. propose the safest handling for:
   - already completed results;
   - queue items still waiting;
   - queue items that should be archived, removed, or retained;
4. wait for user direction before making destructive queue changes.

This keeps partial compute results usable instead of discarding them blindly.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index that should also reference this technical document.
- `AGENTS.md`
  Main repository instruction file that should be updated after approval to encode the new campaign workflow rule.
- `doc/reports/campaign_plans/mixed_training/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
  Already approved planning report for the mixed feedforward campaign that should be used as the first concrete application of this workflow.
- `config/training/feedforward/presets/`
  Source location for canonical feedforward presets used to generate campaign-specific queue YAML files.
- `config/training/queue/`
  Queue root where campaign YAML files should be staged for execution.
- `training/run_training_campaign.py`
  Queue-based batch runner that will execute the campaign.
- `training/train_feedforward_network.py`
  Single-run trainer used by the queue runner for the current feedforward campaign.
- `output/training_campaigns/`
  Campaign artifact root containing manifest, execution report, and logs.
- `doc/running/`
  Proposed new location for persistent active-campaign state tracking.
- `doc/guide/project_usage_guide.md`
  User-facing guide that should document the new campaign-preparation and active-campaign workflow after approval.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, update the repository instructions so that every approved training campaign automatically includes:
   - generated YAML files;
   - the exact terminal command to launch the campaign.
3. Add persistent active-campaign tracking under `doc/running/active_training_campaign.yaml`.
4. Define and document the protected-file logic used to trigger a `CRITICAL WARNING` before modifying files used by the active campaign.
5. Apply the workflow immediately to the approved mixed training campaign by:
   - generating its `9` YAML files;
   - placing them in the correct queue-preparation location;
   - providing the exact command needed to start that campaign.
6. Extend the workflow so that user messages such as `campaign started`, `campaign finished`, or cancellation requests can be handled through the stored active-campaign state.
7. Update `doc/guide/project_usage_guide.md` and any permanent instruction files after approval so the workflow is reproducible in future sessions.
