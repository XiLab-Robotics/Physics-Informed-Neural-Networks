# Polished-Dataset TE Curve Verification Pipeline Refresh Launcher

## Overview

This launcher runs the operator-approved official `TE Curve Verification
Pipeline` refresh for the completed polished-dataset retraining closeouts.

It evaluates two new polished source groups:

| Source | Scope |
| --- | --- |
| `polished_rcim_model_bank_reproduction` | Polished RCIM model-bank exports for `Fw` and `Bw` |
| `polished_model_development_registry` | 36 polished model-development families over `global`, `Fw`, and `Bw` |

Codex prepares the launcher, but the heavy matrix is operator-launched.
The launcher pins the comparison dataset to `polished_dataset`; generated
matrix summaries must report `data\polished_dataset` as their dataset root.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_polished_dataset_track2_verification_refresh.ps1
```

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_polished_dataset_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs source/configuration files, family registries, training-run
artifacts, polished RCIM validation artifacts, and the configured baseline
matrix summary before launching on the remote checkout. It then retrieves only
the artifacts listed by the run-local artifact sync manifest.

## Resume Command

If the matrix, collage report, and overlay report already completed but a
post-processing step failed, resume from visual source-coverage validation:

```powershell
.\scripts\campaigns\track_2\run_polished_dataset_track2_verification_refresh.ps1 -ResumeAfterVisualReports
```

This mode reuses the latest matching matrix, collage, and overlay artifacts,
then runs visual source-coverage validation, official report generation, PDF
export, and artifact-manifest generation.

Do not use resume mode when the latest matrix summary reports
`data\simplified_dataset`; that indicates a pre-fix run and requires a full
launcher rerun.

## Workflow

The launcher runs:

1. polished RCIM `reference_inventory.yaml` generation from the completed
   validation summaries;
2. the full direction-aware `TE Curve Verification Pipeline` matrix;
3. best-model collage report generation;
4. multi-model curve-comparison report generation;
5. visual source-coverage validation for registry-backed polished candidates;
6. official model-verification report generation;
7. PDF export for the collage, overlay, and official verification reports.

Use `-SkipVisualReports` to run only the inventory builder and matrix. Use
`-SkipPdfExport` to leave the reports as Markdown plus image artifacts.

## Expected Outputs

Matrix artifacts:

- `output/validation_checks/track2_reference_comparison/`

Generated polished RCIM inventories:

- `output/validation_checks/rcim_model_bank_reproduction/reference_inventories/`

Canonical matrix report:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Dated report bundles:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-07-02]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-07-02]/`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-07-02]/`

Operator logs:

- `output/validation_checks/track2_operator_launch_logs/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, visual reports, official report, PDFs, and
logs before updating the TE live backlog, Training Results Master Summary, and
TE Program Status And Closeout Ledger.
