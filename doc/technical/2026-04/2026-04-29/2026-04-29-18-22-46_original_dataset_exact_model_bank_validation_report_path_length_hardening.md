# Original Dataset Exact Model Bank Validation Report Path Length Hardening

## Overview

The remote overnight campaign
`track1_forward_last_three_open_cells_overnight_mega_campaign_2026-04-29_18_09_41`
failed on run `1/240` after successful training, evaluation, and ONNX export.
The failure happened when the original-dataset exact-model-bank validation
runner tried to write the Markdown validation report under
`doc/reports/analysis/validation_checks/`.

The generated report path was too long for the remote Windows environment. The
current naming rule concatenates a timestamp, the model family, the full
`output_run_name`, and the long suffix
`original_dataset_exact_model_bank_report.md`. For the overnight mega campaign,
that produced a path of roughly `302` characters and triggered
`OSError: [Errno 22] Invalid argument`.

This document defines one narrow fix that:

- repairs the current overnight mega campaign so it can be launched again;
- hardens the shared validation-report naming rule for future exact-paper
  campaigns so the same class of failure cannot recur.

## Technical Approach

The fix should be applied at the shared validation-report path builder used by
the original-dataset exact-model-bank branch, not at the individual campaign
launcher level.

The implementation should:

- replace the current verbose Markdown report filename pattern with a compact,
  deterministic pattern that still preserves traceability;
- keep the report root
  `doc/reports/analysis/validation_checks/` unchanged;
- preserve enough identity in the filename to connect the report to the run
  metadata, family, and campaign surface without embedding the full
  `output_run_name`;
- add an explicit path-length safety rule so future campaign names cannot
  silently regenerate unsafe report filenames;
- verify that the overnight mega campaign uses the hardened shared path builder
  without needing campaign-specific exceptions.

The preferred pattern is a short timestamp plus compact run identity, with any
long human-readable detail moved into the Markdown body and existing YAML
artifacts rather than the filename itself.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
  Shared helper that builds the Markdown validation report path.
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
  Validation runner that consumes the shared report path and writes the report.
- `doc/running/active_training_campaign.yaml`
  Canonical active-campaign state that must remain coherent while the broken
  overnight campaign is repaired and relaunched.
- `doc/scripts/campaigns/run_track1_forward_last_three_open_cells_overnight_mega_campaign.md`
  Launcher note that may need a short operator-facing note if the recovery or
  relaunch flow changes.
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-29-17-59-02_track1_forward_last_three_open_cells_overnight_mega_campaign_plan_report.md`
  Approved plan for the affected overnight campaign.

Subagents:

- No subagent use is planned for this fix.
- If subagent use becomes necessary later, it must be proposed explicitly and
  approved before launch.

## Implementation Steps

1. Re-read the active campaign state and confirm the overnight mega campaign is
   still only `prepared` and not partially running in the background.
2. Patch the shared original-dataset exact-model-bank validation-report path
   builder to emit short, deterministic, Windows-safe Markdown filenames.
3. Add a defensive length guard or equivalent normalization rule so future
   exact-paper campaigns cannot recreate overlong validation report paths.
4. Smoke-check the hardened naming logic against the current overnight mega
   campaign identity and confirm the resulting path stays comfortably below the
   Windows-risk zone.
5. Update any affected operator-facing note if the relaunch workflow needs one
   concise clarification.
6. Run Markdown QA on the touched documentation scope.
7. Stop after reporting the prepared fix and wait for explicit approval before
   implementing code changes or relaunching the campaign.
