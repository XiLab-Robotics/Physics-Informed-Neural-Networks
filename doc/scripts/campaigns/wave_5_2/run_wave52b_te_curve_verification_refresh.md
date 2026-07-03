# Wave 5.2B TE Curve Verification Pipeline Refresh Launcher

## Overview

This launcher runs the operator-approved official `TE Curve Verification
Pipeline` refresh for the completed `Wave 5.2B` offset and harmonic guided
campaign.

It adds the strongest Wave 5.2B profile to the direction-aware matrix across
the three required surfaces:

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `offset_centered_shape_harmonic` | `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` |

The launcher is operator-facing. Codex prepares it and provides the command,
but does not run the heavy `TE Curve Verification Pipeline` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local `TE Curve Verification Pipeline`
launcher, config, scripts, Wave 5.2B harmonic-profile family registries, Wave
5.2B harmonic-profile training-run artifacts, and the completed `Wave 2.3`
baseline summary to the remote checkout before execution. It then syncs the
generated artifact paths listed by the run-local artifact sync manifest back to
the local repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1 `
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
4. the visual source-coverage validation for the refreshed Wave 5.2B source;
5. the official model-verification report generation;
6. the PDF export for the collage, overlay, and official verification reports.

Use `-SkipVisualReports` to run only the matrix, or `-SkipPdfExport` to leave
the generated visual and official reports as Markdown plus image artifacts.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-07-02]/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-07-02]/`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-07-02]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

Remote artifact synchronization retrieves:

- the current run's `output/validation_checks/track2_reference_comparison/...`
  directory;
- the current run's visual-report output directories when visual reports are
  enabled;
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- the dated visual-report and official-report bundles for the selected
  `-ReportDate`;
- the current run's operator log directory and `artifact_sync_manifest.txt`;
- `doc/reports/campaign_results/track_2/verification_plots/wave52b_offset_harmonic_guided_registry/`
  when present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog,
master summary, and closeout ledger.
