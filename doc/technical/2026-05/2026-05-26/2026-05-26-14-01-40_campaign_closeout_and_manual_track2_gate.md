# Campaign Closeout And Manual Track 2 Gate

## Overview

Formalize the revised campaign-closeout workflow after the interrupted
`Wave 2B` Track 2 refresh attempt.

The immediate campaign evidence shows that
`wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` completed all `9`
training runs with `0` failures. The normal campaign closeout can therefore
continue from the completed campaign artifacts.

The attempted in-agent Track 2 refresh was intentionally interrupted by the
operator after running overnight with memory and disk pressure. The partial
Track 2 output only contains initial metadata files, so it must not be treated
as a completed verification refresh.

This document changes the default workflow rule for future campaign closeouts:
closeout and Track 2 verification are separate phases. Codex should complete
the normal campaign closeout first, then ask whether to prepare Track 2. If
Track 2 is approved, Codex must generate a PowerShell launcher with local and
`-Remote` execution support and wait for the operator to run it.

No subagent use is planned for this policy update. If a subagent becomes useful,
this document must be updated with the proposed subagent name, task boundary,
and approval requirement before launching it.

## Technical Approach

Separate the workflow into two explicit gates:

1. Normal campaign closeout.
2. Optional operator-launched Track 2 verification.

The normal closeout phase may inspect campaign outputs, create the campaign
results report, export and validate the campaign-results PDF, update normal
campaign state, update registries and summaries, and clear
`doc/running/active_training_campaign.yaml` when the completed campaign has
been recorded.

The Track 2 phase must not run automatically inside Codex. When Track 2 is
requested, Codex should prepare:

- a dedicated Track 2 technical or refresh plan;
- a local PowerShell launcher that runs the heavy matrix, visual report, and
  PDF pipeline;
- a `-Remote` option for running the same approved workflow on a stronger
  machine when available;
- a launcher note documenting the exact command and expected outputs.

After generating the launcher package, Codex stops and waits for the operator
to confirm that the Track 2 job has completed. Only then should Codex inspect
the resulting artifacts and finish the Track 2 report decision.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  Persistent campaign state and protected-file boundary.
- `doc/reports/campaign_results/`
  Normal campaign closeout report and PDF target.
- `doc/reports/analysis/Training Results Master Summary.md`
  Normal campaign summary refreshed by the training runner and by closeout.
- `doc/running/te_model_live_backlog.md`
  Backlog surface that should distinguish completed campaign closeout from
  optional Track 2 verification.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  Track 2 candidate matrix configuration to prepare but not execute in-agent.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  Track 2 inference support, including temporal sequence-family handling.
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
  Track 2 collage report builder.
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
  Track 2 overlay report builder.
- `scripts/campaigns/`
  Location for operator-facing PowerShell launchers.
- `.codex/skills/track2-verification-refresh/`
  Repository-local skill and checklist that must be revised to make the
  operator-launched Track 2 gate explicit.

## Implementation Steps

1. Record the current interrupted Track 2 state:
   - no Python process remains active;
   - the partial Track 2 output directory contains only `run_metadata.yaml`
     and `training_config.yaml`;
   - no matrix report, visual report, official report, or PDF was completed.
2. Remove or quarantine the partial Track 2 output from the interrupted attempt.
3. Revert or park the in-progress Track 2 code/config changes from the aborted
   in-agent refresh unless they are needed by the later operator launcher
   package.
4. Complete the normal Wave 2B campaign closeout:
   - verify `9` completed and `0` failed runs;
   - create the campaign-results Markdown report;
   - export and validate the campaign-results PDF;
   - update `doc/running/active_training_campaign.yaml` from `prepared` to a
     completed or cleared state with the Wave 2B completion record;
   - update `doc/README.md`, `doc/running/te_model_live_backlog.md`, and
     `Training Results Master Summary.md` for closeout only.
5. Update repository rules and local skill notes so future closeouts do not
   automatically run Track 2 inside Codex.
6. Add the durable instruction to Codex memory: after campaign closeout,
   propose Track 2 separately and, when approved, generate an operator-run
   PowerShell launcher with optional `-Remote` support.
7. Run Markdown QA on touched authored Markdown.
8. Stop before any Git commit and wait for explicit user approval.

## Current Recovery Decision

Do not restart Track 2 from inside Codex.

Resume from the normal Wave 2B closeout. Treat the interrupted Track 2 attempt
as incomplete and non-authoritative. Track 2 should be prepared later as a
separate operator-launched package if the user explicitly approves it after the
normal closeout or after any requested commit/PDF refinements.
