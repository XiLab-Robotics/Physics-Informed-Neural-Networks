# 2026-04-25-22-43-08 Track1 Interrupted Mega Campaign Discard Closeout And Remote Micro Relaunch Gate

## Overview

The current remote `Track 1` bidirectional original-dataset mega-campaign is
not scientifically reusable as a live continuation point.

The interrupted execution already mixed several launcher generations:

- the first remote run happened before the final progress-surface cleanup;
- the campaign later absorbed multiple hardening fixes for ONNX preflight,
  remote-path handling, and `MLP` stabilization;
- the local operator process crashed, so the wrapper-level completion state and
  final artifact synchronization are incomplete.

The user requested an explicit reset:

- formally close the interrupted mega-campaign while discarding its partial
  results;
- prepare a new small remote diagnostic campaign with exactly one training run
  per algorithm family;
- use that micro-campaign as the gate before preparing a fresh mega-campaign
  from zero.

## Technical Approach

The work is divided into three sequential phases.

Phase `1` is an interrupted discard closeout of the current mega-campaign:

- reconcile `doc/running/active_training_campaign.yaml` with the real
  interrupted state;
- produce an interrupted campaign-results report that explicitly marks the
  partial wave as discarded for scientific comparison purposes;
- do not propagate the interrupted wave into
  `RCIM Paper Reference Benchmark.md`, registries, or paper-reference archives;
- preserve only the operational evidence needed for traceability.

Phase `2` is a fresh remote micro-campaign:

- create a new remote campaign package with one run per family;
- keep the scope to `10` total runs by using `forward` only;
- reuse the current hardened launcher stack and the current `MLP`
  stabilization;
- keep the goal purely diagnostic, not scientific.

Phase `3` is gated mega-campaign re-preparation:

- only after the `10`-run remote micro-campaign completes cleanly;
- regenerate the full bidirectional mega-campaign from zero;
- treat the interrupted wave as discarded and non-resumable.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_diagnostic_campaign.py`
- `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_diagnostic_campaign.ps1`
- `doc/scripts/campaigns/`

Subagent use:

- no subagents are planned for this task;
- closeout, campaign preparation, and remote-diagnostic packaging stay in the
  main rollout.

## Implementation Steps

1. Create the companion planning report for the interrupted discard closeout,
   the `10`-run remote micro-campaign, and the subsequent fresh mega-campaign
   regeneration gate.
2. After approval, close the current mega-campaign as `interrupted` with an
   explicit discard rationale and without promoting the partial results into
   benchmark or registry surfaces.
3. Prepare a fresh forward-only remote micro-campaign with one run for each of
   the `10` exact-paper families and its own launcher plus launcher note.
4. Update the active campaign state so the micro-campaign becomes the new
   canonical prepared run, with protected files and remote metadata aligned.
5. Provide the exact remote launch command for the micro-campaign and wait for
   the user to execute it.
6. If the micro-campaign completes cleanly, prepare a brand-new bidirectional
   mega-campaign package from zero rather than resuming the interrupted one.
