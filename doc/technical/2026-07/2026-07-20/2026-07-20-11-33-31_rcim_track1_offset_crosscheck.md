# RCIM Track 1 Offset Cross-Check

## Overview

This document defines the diagnostic plan for investigating the unexpected
curve-offset behavior observed after the latest `RCIM Model-Bank Reproduction`
retraining on `polished_dataset` with `actual_values` inputs.

The goal is to isolate whether the offset is caused by data extraction,
FFT/harmonic decomposition, harmonic target selection, per-family model
selection, archived best-model selection, harmonic recomposition, or the
plotting/report path. The first pass must compare `original`, `retuned`, the
older historical `simplified_dataset` references, and the newly retrained
`simplified_dataset` setpoint models. The polished RCIM pass follows only after
the simplified/reference discrepancy is understood.

No Codex subagent is planned for the first pass. If a subagent becomes useful,
the proposed subagent name, reason, and delegated scope must be presented to the
user and explicitly approved before launch.

## Technical Approach

The audit will proceed evidence-first and read-only until a concrete defect is
identified. The first pass will inventory and compare:

- dataset and input-mode provenance for every evaluated archive;
- FFT preprocessing and harmonic coefficient conventions, including `a_0` /
  DC component handling;
- train/validation/test split inputs and selected harmonic target lists;
- model-family grid outputs for amplitude and phase targets;
- best-model pointer files, inventories, and report-side candidate selection;
- harmonic recomposition code, sign/phase conventions, direction handling, and
  curve reconstruction units;
- plot-builder logic used by the recent reports, with particular attention to
  previously repaired candidate-selection and graph-source issues.

Generated diagnostic outputs should be written into a dedicated dated analysis
bundle under `doc/reports/analysis/rcim_paper_reference/` or a temporary
validation-check output root, depending on whether the result is a canonical
report or a throwaway reproduction artifact.

The simplified/reference pass must compare both historical visual evidence and
freshly generated plots from the current familywise report pipeline. It must
also check why older Wave `4.3` mixture-density reports can show good curve
tracking while newly retrained model-development reports look poor, separating
real training degradation from report-side dataset, model, surface, or plotting
selection mistakes.

## Involved Components

- `data/simplified_dataset/`
- `data/polished_dataset/`
- `reference/rcim_ml_compensation_recovered_assets/`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`
- `doc/reports/analysis/rcim_paper_reference/`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/reports/campaign_results/cross_wave/polished_dataset/`
- `models/simplified_dataset/`
- `models/polished_dataset/paper_reference/rcim_track1/`
- `models/simplified_dataset/setpoints/`
- `output/training_campaigns/`
- `output/validation_checks/`
- `scripts/paper_reimplementation/`
- `scripts/reports/analysis/`

## Implementation Steps

1. Read the repository reference summaries and the current campaign state.
2. Inventory the `original`, `retuned`, historical `simplified_dataset`
   `rcim_track1`, and newly retrained `simplified_dataset` setpoint archives
   without modifying artifacts.
3. Inspect the recent familywise report figures, the 12 current report outputs,
   and older known-good simplified/retuned/reference plots.
4. Trace the FFT extraction path and confirm coefficient ordering, units,
   harmonic indexing, `a_0` handling, and direction-specific sign conventions.
5. Trace per-harmonic training targets and best-model selection for each model
   family, amplitude/phase target, surface, and input mode.
6. Trace the report-side archive resolver and model selector to confirm the
   plotted models match the intended dataset/input-mode surface.
7. Re-run a bounded inference-only reproduction for original paper, retuned,
   older `simplified_dataset`, and newly retrained `simplified_dataset`
   archives, producing comparable curve plots and numeric offset diagnostics.
8. After the simplified/reference cause is understood, inspect polished
   `rcim_track1` setpoints training, plotting, and best-component selection,
   including complete paper-style Tables `2`-`5` with highlighted selected
   best candidates.
9. If a defect is confirmed, prepare the smallest implementation fix in the
   affected code path and verify it with focused regression checks.
10. If only analysis artifacts or reports are produced, run Markdown QA on
   touched Markdown files before closeout.
