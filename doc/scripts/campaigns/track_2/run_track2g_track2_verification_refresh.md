# Wave 3.3 TE Curve Verification Pipeline Verification Refresh Launcher

## Overview

This launcher runs the operator-approved official `TE Curve Verification Pipeline` offline
verification refresh for the completed `Wave 3.3` curve-aware training
campaign.

It adds twelve registry-backed candidates to the direction-aware matrix: four
loss profiles over the three required deployment surfaces.

| Loss Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `pointwise_control` | `track2g_curve_aware_pointwise_control_global` | `track2g_curve_aware_pointwise_control_Fw` | `track2g_curve_aware_pointwise_control_Bw` |
| `raw_centered_shape` | `track2g_curve_aware_raw_centered_shape_global` | `track2g_curve_aware_raw_centered_shape_Fw` | `track2g_curve_aware_raw_centered_shape_Bw` |
| `raw_offset` | `track2g_curve_aware_raw_offset_global` | `track2g_curve_aware_raw_offset_Fw` | `track2g_curve_aware_raw_offset_Bw` |
| `full_curve_composite` | `track2g_curve_aware_full_curve_composite_global` | `track2g_curve_aware_full_curve_composite_Fw` | `track2g_curve_aware_full_curve_composite_Bw` |

The launcher is operator-facing. Codex prepares it and provides the command,
but does not run the heavy `TE Curve Verification Pipeline` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2g_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2g_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local TE Curve Verification Pipeline launcher, config, scripts,
Wave 3.3 family registries, Wave 3.3 training-run artifacts, and the completed
`Wave 2.3` TE Curve Verification Pipeline baseline summary to the remote checkout before execution. It
then syncs only the generated artifact paths listed by the run-local artifact
sync manifest back to the local repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\track_2\run_track2g_track2_verification_refresh.ps1 `
  -Remote `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName pinns_env
```

## Workflow

The launcher runs:

1. the official full direction-aware `TE Curve Verification Pipeline` matrix;
2. the best-model collage report generation;
3. the multi-model curve-comparison report generation;
4. the visual source-coverage validation against the matrix candidate list;
5. the official model-verification report generation;
6. the PDF export for the collage, overlay, and official verification reports.

Use `-SkipVisualReports` to run only the matrix, or `-SkipPdfExport` to leave
the generated visual and official reports as Markdown plus image artifacts.
When visual reports are enabled, the launcher fails before PDF export if a
registry-backed matrix source is not visible in the collage and overlay
Markdown reports.

By default, the matrix uses the completed `Wave 2.3` refresh as the configured
baseline summary and only evaluates incremental current candidates. The new
candidate-source plot sync is scoped to
`track2g_curve_aware_training_registry`. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track_2/verification_plots/` visual refresh is required.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-06-09]/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-06-09]/`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-06-09]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

The official report step writes the
`05_track2_official_verification_report.log` file and builds the official
decision Markdown from the same matrix, collage, and overlay summaries used by
the operator run. The PDF export step includes all three dated reports.

Remote source synchronization sends:

- `scripts/`
- `config/`
- `doc/scripts/campaigns/track_2/`
- `output/registries/families/track2g_curve_aware_harmonic_residual_offset_*`
- `output/training_runs/track2g_curve_aware_harmonic_residual_offset_*`
- the completed `Wave 2.3` `TE Curve Verification Pipeline` baseline summary and per-condition metrics

Remote artifact synchronization retrieves:

- the current run's `output/validation_checks/track2_reference_comparison/...`
  directory;
- the current run's visual-report output directories when visual reports are
  enabled;
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- the dated visual-report and official-report bundles for the selected
  `-ReportDate`;
- the current run's operator log directory and `artifact_sync_manifest.txt`;
- `doc/reports/campaign_results/track_2/verification_plots/track2g_curve_aware_training_registry/`
  when present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog
and master summary. The normal launcher path already generates the official
report and includes it in the PDF export.
