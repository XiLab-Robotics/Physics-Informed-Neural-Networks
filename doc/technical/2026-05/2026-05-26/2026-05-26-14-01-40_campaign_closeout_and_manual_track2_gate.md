# Campaign Closeout And Manual TE Curve Verification Pipeline Gate

## Overview

Formalize the revised campaign-closeout workflow after the interrupted
`Wave 2.2` TE Curve Verification refresh attempt.

The immediate campaign evidence shows that
`wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` completed all `9`
training runs with `0` failures. The normal campaign closeout can therefore
continue from the completed campaign artifacts.

The attempted in-agent TE Curve Verification refresh was intentionally interrupted by the
operator after running overnight with memory and disk pressure. The partial
TE Curve Verification Pipeline output only contains initial metadata files, so it must not be treated
as a completed verification refresh.

This document changes the default workflow rule for future campaign closeouts:
closeout and TE curve verification are separate phases. Codex should complete
the normal campaign closeout first, then ask whether to prepare TE Curve Verification Pipeline. If
TE Curve Verification Pipeline is approved, Codex must generate a PowerShell launcher with local and
`-Remote` execution support and wait for the operator to run it.

No subagent use is planned for this policy update. If a subagent becomes useful,
this document must be updated with the proposed subagent name, task boundary,
and approval requirement before launching it.

## Technical Approach

Separate the workflow into two explicit gates:

1. Normal campaign closeout.
2. Optional operator-launched TE curve verification.

The normal closeout phase may inspect campaign outputs, create the campaign
results report, export and validate the campaign-results PDF, update normal
campaign state, update registries and summaries, and clear
`doc/running/active_training_campaign.yaml` when the completed campaign has
been recorded.

The TE Curve Verification Pipeline phase must not run automatically inside Codex. When TE Curve Verification Pipeline is
requested, Codex should prepare:

- a dedicated TE Curve Verification Pipeline technical or refresh plan;
- a local PowerShell launcher that runs the heavy matrix, visual report, and
  PDF pipeline;
- a `-Remote` option for running the same approved workflow on a stronger
  machine when available;
- a launcher note documenting the exact command and expected outputs.

After generating the launcher package, Codex stops and waits for the operator
to confirm that the TE Curve Verification Pipeline job has completed. Only then should Codex inspect
the resulting artifacts and finish the TE curve-verification report decision.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  Persistent campaign state and protected-file boundary.
- `doc/reports/campaign_results/`
  Normal campaign closeout report and PDF target.
- `doc/reports/analysis/Training Results Master Summary.md`
  Normal campaign summary refreshed by the training runner and by closeout.
- `doc/running/te_model_live_backlog.md`
  Backlog surface that should distinguish completed campaign closeout from
  optional TE curve verification.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  curve-verification candidate matrix configuration to prepare but not execute in-agent.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  TE Curve Verification Pipeline inference support, including temporal sequence-family handling.
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
  curve-verification collage report builder.
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
  TE Curve Verification Pipeline overlay report builder.
- `scripts/campaigns/`
  Location for operator-facing PowerShell launchers.
- `.codex/skills/track2-verification-refresh/`
  Repository-local skill and checklist that must be revised to make the
  operator-launched TE Curve Verification Pipeline gate explicit.

## Implementation Steps

1. Record the current interrupted TE Curve Verification Pipeline state:
   - no Python process remains active;
   - the partial TE Curve Verification Pipeline output directory contains only `run_metadata.yaml`
     and `training_config.yaml`;
   - no matrix report, visual report, official report, or PDF was completed.
2. Remove or quarantine the partial TE Curve Verification Pipeline output from the interrupted attempt.
3. Revert or park the in-progress TE Curve Verification Pipeline code/config changes from the aborted
   in-agent refresh unless they are needed by the later operator launcher
   package.
4. Complete the normal Wave 2.2 campaign closeout:
   - verify `9` completed and `0` failed runs;
   - create the campaign-results Markdown report;
   - export and validate the campaign-results PDF;
   - update `doc/running/active_training_campaign.yaml` from `prepared` to a
     completed or cleared state with the Wave 2.2 completion record;
   - update `doc/README.md`, `doc/running/te_model_live_backlog.md`, and
     `Training Results Master Summary.md` for closeout only.
5. Update repository rules and local skill notes so future closeouts do not
   automatically run TE Curve Verification Pipeline inside Codex.
6. Add the durable instruction to Codex memory: after campaign closeout,
   propose TE Curve Verification Pipeline separately and, when approved, generate an operator-run
   PowerShell launcher with optional `-Remote` support.
7. Run Markdown QA on touched authored Markdown.
8. Stop before any Git commit and wait for explicit user approval.

## Current Recovery Decision

Do not restart TE Curve Verification Pipeline from inside Codex.

Resume from the normal Wave 2.2 closeout. Treat the interrupted TE Curve Verification Pipeline attempt
as incomplete and non-authoritative. TE Curve Verification Pipeline should be prepared later as a
separate operator-launched package if the user explicitly approves it after the
normal closeout or after any requested commit/PDF refinements.
