# RCIM Track1 Retrained Paper Tables Report

## Overview

This technical document plans a repository-owned analytical report that mirrors
the four model-bank tables from the original RCIM paper for the newly
retrained `rcim_track1` model-bank archives. The report will live beside the
current familywise RCIM report bundle at
`doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/rcim_track1/[2026-07-19]/`
and will expose the harmonic-wise best cells that should feed the later
composite model selection.

The requested report is documentation and analysis only. It will not launch a
training run, modify campaign configuration, or promote any model.

## Technical Approach

The report will be generated from the archived RCIM model-bank inventories and
validation summaries already present in the repository. For each dataset/input
mode, it will build paper-style tables for the RCIM selected harmonic targets:

- Table 2 equivalent: amplitude MAE by family and harmonic;
- Table 3 equivalent: amplitude RMSE by family and harmonic;
- Table 4 equivalent: phase MAE by family and harmonic;
- Table 5 equivalent: phase RMSE by family and harmonic.

The report will include three dataset/input-mode sections:

- `simplified_dataset/setpoints`;
- `polished_dataset/setpoints`;
- `polished_dataset/actual_values`.

Each table will keep the model-family columns visible and will mark the
per-target best cell with `**BEST**`. For retrained polished archives, the
selected component bank will be cross-checked against
`target_winner_registry` in the corresponding `validation_summary.yaml`. For
the historical simplified archive, best cells will be derived from the
available component reference inventories using the same metric ordering used
by the familywise RCIM loader.

## Involved Components

- `models/simplified_dataset/paper_reference/rcim_track1/`
- `models/polished_dataset/paper_reference/rcim_track1/setpoints/`
- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`
- `output/validation_checks/rcim_track1/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/rcim_track1/[2026-07-19]/`
- `doc/README.md`

No subagent is planned for this implementation.

## Implementation Steps

1. Inspect all relevant `reference_inventory.yaml` and `validation_summary.yaml`
   files for the three dataset/input-mode groups.
2. Build a small repository-owned report generator or reuse existing report
   support code if the table extraction is already implemented locally.
3. Generate a Markdown report in the existing RCIM familywise report bundle.
4. Highlight best cells per harmonic target and identify the selected component
   family for the future composite model bank.
5. Register the new report from `doc/README.md`.
6. Run scoped Markdown QA on the new report and updated index.
