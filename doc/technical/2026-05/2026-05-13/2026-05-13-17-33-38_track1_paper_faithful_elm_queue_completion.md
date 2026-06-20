# RCIM Model-Bank Reproduction Paper-Faithful ELM Queue Completion

## Overview

The RCIM Model-Bank Reproduction exact-paper implementation already supports `ELM` as an
operational family in the shared Python family bank and in the PowerShell
launcher argument surface. The prepared bidirectional paper-faithful campaign
queue still contains only the original `10` paper families for each direction,
so a launcher command that requests `ELM` cannot currently select an `ELM`
YAML.

This change will complete the prepared queue so the existing launcher command
can run the `11` supported operational families:

```powershell
.\scripts\campaigns\track_1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM" `
  -Stage Search `
  -GridSearchVerboseOverride 3 `
  -HistoricalCrossValidateVerboseOverride 10 `
  -Remote
```

The active campaign state currently marks the earlier parent campaign as
`cancelled`, but the launcher remains listed in `protected_file_list`. This
technical document therefore records the protected-file override requirement
before any launcher or campaign YAML edits.

## Technical Approach

The implementation will add `ELM` to the existing prepared campaign queue
without changing the mathematical search protocol used by the exact-paper
family-bank runner.

The planned update is narrow:

- add one forward `ELM` YAML under the existing
  `bidirectional_paper_faithful_grid_search/forward/elm/` campaign tree;
- add one backward `ELM` YAML under the matching
  `bidirectional_paper_faithful_grid_search/backward/elm/` campaign tree;
- add companion queue README files for both `ELM` queue directories if the
  existing family folders use them as operator-facing queue documentation;
- update `doc/running/active_training_campaign.yaml` so the persisted campaign
  state and protected-file list include the new `ELM` queue entries;
- update the launcher documentation so the example `11`-family command is
  recorded as a supported launch surface; and
- keep the launcher code itself unchanged unless inspection shows a concrete
  mismatch between the accepted `ELM` family list and queue selection logic.

The existing planning report remains the parent campaign plan. If the live
file inspection shows that it explicitly freezes the queue at `20` runs rather
than describing the paper-faithful campaign family set generically, the plan
will be amended or a short campaign-plan addendum will be created before
launching training.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/`
  Existing prepared RCIM Model-Bank Reproduction paper-faithful campaign config root that needs
  forward and backward `ELM` YAML entries.
- `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
  Protected launcher requested by the operator. It already accepts `ELM`, but
  will be inspected for queue-selection consistency.
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
  Operator-facing launcher note that should include the `ELM` command surface.
- `doc/running/active_training_campaign.yaml`
  Persistent campaign state. It is protected and must be updated only after
  explicit approval because the current file still records the previous
  cancelled campaign and its protected-file list.
- `doc/reports/campaign_plans/track_1/exact_paper/2026-05-04-12-13-07_track1_paper_faithful_search_protocol_and_campaign_replacement_plan_report.md`
  Existing campaign planning report used by the prepared bidirectional
  paper-faithful queue.

No subagent is planned for this change.

## Implementation Steps

1. Wait for explicit user approval of this technical document and the
   protected-file override.
2. Inspect one existing forward YAML and one existing backward YAML to preserve
   naming, run identity, output roots, stage settings, and exact-paper runner
   configuration.
3. Create the forward and backward `ELM` YAML entries by mirroring the existing
   family-specific queue layout and changing only the family/run identity
   fields required for `ELM`.
4. Add or update the matching `ELM` queue README files if the existing family
   folders use queue-local operator notes.
5. Update the persistent campaign state so `queue_config_path_list`,
   `pending_family_list`, `protected_file_list`, and launch documentation
   reflect the new `ELM` entries.
6. Run non-training verification:
   - confirm the launcher selects `11` forward configs when `ELM` is included;
   - confirm it still selects `10` forward configs when `ELM` is omitted;
   - parse the touched PowerShell launcher if edited;
   - parse/read the touched YAML files;
   - run Markdown QA on touched Markdown files.
7. Stop after verification and report the exact launch command. Do not start
   training and do not create a Git commit without explicit follow-up approval.
