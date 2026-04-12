# Exact Paper Faithful Campaign Stabilization Debug

## Overview

This technical document covers the stabilization debug for the currently active
`exact_paper_faithful_reproduction_campaign_2026_04_10_21_47_55`.

The new coordinated launcher was started successfully, and the first run
`exact_paper_recovered_reference` completed end to end. The second run
`exact_paper_amplitude_phase_reference` then failed, not on model fitting or
ONNX conversion, but during Markdown-report generation after a successful
component-level evaluation pass.

The observed crash is:

- `KeyError: 'export_failure_mode'`
- raised inside
  `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
  while building the exact-paper Markdown report
- triggered by a configuration with `enable_onnx_export: false`

This means the new campaign package exposed a recurring workflow defect:
report-building logic still assumes the ONNX export summary always carries the
full export metadata, even when export is intentionally disabled.

## Technical Approach

The stabilization pass should make the exact-paper workflow robust across both:

- export-enabled exact-paper runs;
- export-disabled exact-paper runs used for pure component-side benchmarking.

The fix should remain minimal and campaign-safe:

1. reproduce the failure through the active coordinated launcher path or the
   exact failing run in isolation;
2. inspect the exact-paper export-summary contract for the
   `enable_onnx_export: false` branch;
3. normalize the export-summary schema so report-building and summary-building
   code receive the same required keys regardless of whether export is enabled;
4. rerun the failing run in isolation;
5. rerun the full coordinated campaign launcher until the campaign survives the
   previously failing boundary.

If further recurring failures appear during the rerun, continue iterating in
the same debug pass until the prepared launcher is stable enough to hand back
to the user.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/campaigns/run_exact_paper_faithful_reproduction_campaign.ps1`
- `config/paper_reimplementation/rcim_ml_compensation/paper_faithful_reproduction/campaigns/2026-04-10_exact_paper_faithful_reproduction_campaign/02_exact_paper_amplitude_phase_reference.yaml`
- `output/training_campaigns/exact_paper_faithful_reproduction_campaign_2026_04_10_21_47_55/logs/`

No subagent is planned for this task. The failure is narrow and local to the
repository-owned support layer.

## Implementation Steps

1. Re-read the active campaign state and treat protected campaign files as
   locked unless a direct campaign-package edit becomes unavoidable.
2. Inspect the failing log and the exact-paper support-layer contract for the
   export-disabled path.
3. Patch the repository-owned exact-paper support layer so export-disabled runs
   still emit a complete report-compatible ONNX summary structure.
4. Rerun the failing run in isolation first.
5. Rerun the full coordinated launcher and continue debugging until no further
   recurring campaign-breaking defects remain.
6. Run Markdown checks on any touched repository-owned Markdown files before
   closing the task.
