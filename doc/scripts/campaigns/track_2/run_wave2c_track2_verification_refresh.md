# Wave 2.3 TE Curve Verification Pipeline Verification Refresh Launcher

## Overview

This launcher runs the operator-approved `TE Curve Verification Pipeline` offline verification refresh
for the completed `Wave 2.3` residual harmonic temporal hybrid campaign.

It adds the current registry-backed `Wave 2.3` candidate surfaces to the
official direction-aware matrix through:

- `residual_harmonic_gru_sequence_sparse_rcim_global`,
  `residual_harmonic_gru_sequence_sparse_rcim_Fw`, and
  `residual_harmonic_gru_sequence_sparse_rcim_Bw`;
- `residual_harmonic_gru_sequence_dense240_global`,
  `residual_harmonic_gru_sequence_dense240_Fw`, and
  `residual_harmonic_gru_sequence_dense240_Bw`;
- `residual_harmonic_gru_sequence_dense360_global`,
  `residual_harmonic_gru_sequence_dense360_Fw`, and
  `residual_harmonic_gru_sequence_dense360_Bw`;
- `residual_harmonic_lstm_sequence_sparse_rcim_global`,
  `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, and
  `residual_harmonic_lstm_sequence_sparse_rcim_Bw`;
- `residual_harmonic_lstm_sequence_dense240_global`,
  `residual_harmonic_lstm_sequence_dense240_Fw`, and
  `residual_harmonic_lstm_sequence_dense240_Bw`;
- `residual_harmonic_lstm_sequence_dense360_global`,
  `residual_harmonic_lstm_sequence_dense360_Fw`, and
  `residual_harmonic_lstm_sequence_dense360_Bw`.

The launcher is intentionally operator-facing. Codex prepares it and provides
the command, but does not run the heavy `TE Curve Verification Pipeline` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_wave2c_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_wave2c_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local TE Curve Verification Pipeline launcher, config, script,
registry, prior `Wave 2.2` baseline summary, and `Wave 2.3` checkpoint paths to
the remote checkout before execution. It then syncs only the generated artifact
paths listed by the run-local artifact sync manifest back to the local
repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\track_2\run_wave2c_track2_verification_refresh.ps1 `
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

By default, the matrix uses the completed `Wave 2.2` refresh as the configured
baseline summary and only evaluates the new `Wave 2.3` incremental candidates.
The grouped report-plot sync is scoped to the new
`wave2c_residual_harmonic_temporal_registry` source. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track_2/verification_plots/` visual refresh is required.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-28]/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-28]/`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-28]/`

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
- `output/registries/families/residual_harmonic_*`
- `output/training_runs/residual_harmonic_*`
- the completed `Wave 2.2` `TE Curve Verification Pipeline` baseline summary and per-condition metrics

Remote artifact synchronization retrieves:

- the current run's `output/validation_checks/track2_reference_comparison/...`
  directory;
- the current run's visual-report output directories when visual reports are
  enabled;
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- the dated visual-report and official-report bundles for the selected
  `-ReportDate`;
- the current run's operator log directory and `artifact_sync_manifest.txt`;
- `doc/reports/campaign_results/track_2/verification_plots/wave2c_residual_harmonic_temporal_registry/`
  when present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog
and master summary. The normal launcher path already generates the official
report and includes it in the PDF export.
