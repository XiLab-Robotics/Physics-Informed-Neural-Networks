# Exact Paper Faithful Reproduction Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the first
coordinated paper-faithful reproduction campaign after the exact-paper bank
stabilization pass.

Unlike the earlier exact-paper campaign, this package is intentionally mixed:

- exact-paper family-bank runs still use
  `run_exact_paper_model_bank_validation.py`;
- benchmark-facing offline runs still use
  `run_harmonic_wise_comparison_pipeline.py`.

That is a current repository limitation, not an accident. The repository does
not yet expose one single runner that bridges the recovered exact-paper family
bank directly into the shared offline evaluator used for `Target A`.

## Included Runs

The dedicated launcher forwards these YAML files:

1. `01_exact_paper_recovered_reference.yaml`
2. `02_exact_paper_amplitude_phase_reference.yaml`
3. `03_exact_paper_dominant_harmonic_specialized.yaml`
4. `04_track1_current_best_shared_evaluator_reference.yaml`

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/paper_faithful_reproduction/campaigns/2026-04-10_exact_paper_faithful_reproduction_campaign/`

## Purpose Of Each Block

### Recovered Exact Reference

This run keeps the recovered exact-paper family bank intact and requires a
strict export-complete outcome.

### Amplitude/Phase Component Reference

This run keeps the same recovered target schema but disables ONNX export so the
campaign can inspect the pure component-prediction surface separately from the
export layer.

### Dominant-Harmonic Specialized Offline Run

This run keeps the full RCIM harmonic set under the harmonic-wise evaluator
while investing more capacity in the dominant known error terms, especially the
leading harmonics.

### Current Best Shared-Evaluator Reference

This run is the benchmark anchor from the already completed second harmonic-wise
campaign, kept here so the new specialized run is judged under the same offline
evaluator and playback protocol.

## Practical Use

Run the canonical coordinated campaign launcher from the repository root:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_exact_paper_faithful_reproduction_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_exact_paper_faithful_reproduction_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

Exact-paper structural runs write under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

Harmonic-wise offline benchmark runs write under:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

All coordinated launcher logs write under:

- `output/training_campaigns/track1/exact_paper/exact_paper_faithful_reproduction_campaign_2026_04_10_21_47_55/logs/`

## Related Documents

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-10/2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.md`
